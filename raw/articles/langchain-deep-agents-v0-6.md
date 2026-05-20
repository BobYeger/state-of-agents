## Key Takeaways

- **Run capable agents on open-weight models** — Harness profiles let you get production-grade performance from models like Kimi, Qwen, and DeepSeek at 20x+ lower cost than closed frontier APIs.
- **Cut agent infrastructure costs at scale** — Delta channels reduce checkpoint storage by up to 100x for long-running agents, without sacrificing observability or resilience.
- **Build richer, real-time agent UIs** — The new streaming primitive gives you typed, subscribable event projections for messages, tool calls, and subagents, from runtime all the way to the frontend.

The latest Deep Agents release is centered around performance at the model layer, the agent layer, at scale, and over time. Five things in this release contribute:

- **Code interpreter:** a lightweight runtime for agents to compose tools, manage state, and control what reaches model context — without the overhead of a full sandbox.
- **Harness profiles:** per-model tuning so your harness gets the most out of whichever model you're running, including open-weight models like Kimi, Qwen, and DeepSeek.
- **Streaming:** typed projections for messages, tool calls, subagents, and custom application events — subscribe to exactly what your application needs instead of parsing raw stream output.
- `DeltaChannel`**:** efficient checkpoint storage as agents run longer and context accumulates, without sacrificing the durable execution guarantees that make agents resumable, observable, and resilient.
- `ContextHubBackend`**:** backed by [LangSmith Context Hub](https://smith.langchain.com/context), store the skills, policies, and memories that shape agent behavior in a versioned, collaborative home, so what your agent learns from one run can improve the next.

## Code interpreter

We’re releasing an installable code interpreter in Deep Agents, which give agents a programmable workspace where they can transform data, coordinate tool calls, and keep intermediate work out of the model context. The agent writes code to express its intent, then an in-memory runtime executes that code and returns the relevant results.

Where sandboxes are a code-first way for acting on an environment (such as running commands, installing dependencies, and editing files), interpreters are a code-first way for acting inside the agent loop: composing tools, preserving state, and deciding what information should be returned to the model.

```typescript
// Agent can write code like this:
const topics = ["retrieval", "memory", "evaluation"];

const reports = await Promise.all(
  topics.map((topic) =>
    tools.task({
      description:
          \`Research ${topic} in Deep Agents and return three concise findings.\`,
      subagent_type: "general-purpose",
    }),
  ),
);

reports.join("\n\n");
```

This enables a few new novel capabilities for agents that we’re particularly excited about:

### Model-agnostic PTC

Standard tool calling loops make the model the traffic controller for every step. The model asks for a tool, receives the full result in context, reasons over that result, and repeats. Even when an intermediate result is only needed to compute the next input, it still has to chain through multiple model calls.

Programmatic Tool Calling (PTC) changes that workflow. The model writes code that calls tools from inside an execution runtime, so workflows can run without a round-trip to a model for every individual tool invocation. Intermediate results can stay in runtime state where the interpreter can filter noisy outputs, process data, retry failures, and return only the relevant context back to the model.

```typescript
const pages = await Promise.all(
  urls.map((url) => tools.fetchUrl({ url })),
);

const relevant = pages
  .filter((page) => page.includes("interpreter"))
  .slice(0, 3);

relevant.map((page) => page.slice(0, 500));
```

This pattern of doing tool calling reduces token consumption, cuts down on avoidable model round trips, and makes the agent’s reasoning step smaller.

[Anthropic](https://www.anthropic.com/engineering/advanced-tool-use) helped popularize this pattern by adding it as an API behavior for their model family, but with an interpreter this can now be achieved by any agent with any model (including open source models).

### Recursive workflows

Interpreters let agents interact with the harness in more novel ways. Because tools and subagents are callable from code, an agent can take the output of one subagent, inspect it, transform it, and feed it into another step without routing every intermediate artifact back through the main model.

That makes recursive workflows possible: the agent can keep a queue of questions, call a subagent on the next question, store the result, generate follow-up work from that result, and continue until it has enough evidence to synthesize an answer. (This is more than just “call another LLM on the full input context”: the key is maintaining working state outside the model context and controlling what gets passed into each next call.)

```typescript
const frontier = ["What changed in interpreter middleware?"];
const findings = [];

while (frontier.length && findings.length < 6) {
  const question = frontier.shift();

  const report = await tools.task({
    description: 
        \`Answer this question. If there is a useful next question, \` +
        \`include it as "Follow-up: ..."\n\n${question}\`,
    subagent_type: "general-purpose",
  });

  findings.push(report);

  const next = report.match(/Follow-up: (.*)/)?.[1];
  if (next) frontier.push(next);
}

findings.join("\n\n");
```

This is adjacent to the idea behind **Recursive Language Models (RLM)**: keep working state outside the model context, call models or subagents on selected branches, and control what enters the next model call.

In Deep Agents, the interpreter becomes the working runtime for that pattern — without claiming we “do RLM” as originally defined at the model layer.

All of this can be enabled by installing `deepagents[quickjs]` on pypi, or `@langchain/quickjs` on npm and adding it as a middleware

```python
from deepagents import create_deep_agent
from langchain_quickjs import REPLMiddleware

agent = create_deep_agent(
        model="baseten:zai-org/GLM-5",
    middleware=[REPLMiddleware()],
)
```

See the [docs](https://docs.langchain.com/oss/python/deepagents/interpreters) for more information on interpreters.

## Harness profiles

Open-weight models like Kimi K2.6, GLM 5.1, and DeepSeek V4 are now viable for production agent work, often at 20×+ lower cost than closed frontier models. But models are post-trained on different tool-calling format and prompt conventions, while most harnesses are tuned for the closed model their authors built against. Drop one in cold, and you might see only a fraction of its true capability because the model is speaking a dialect the harness doesn’t understand.

That gap is large and measurable. In our own testing, harness-layer changes alone moved `gpt-5.2-codex` from 52.8% → 66.5% on Terminal-Bench 2.0 (Top 30 → Top 5), lifted `gpt-5.3-codex` 20% on tau2-bench, and `opus-4.7` 10%. Across tau2-bench, prompts and middleware can move scores by 10 to 20 points without changing the model.

The "harness" is around the model: the base system prompt, tools and their descriptions, and middleware that shapes each turn. A harness profile captures these per-model overrides as a named, versionable unit.

Deep Agents v0.6 makes harness profiles a first-class abstraction. You can diff, version, and swap a profile alongside the model, so tuning work carries forward. We're shipping built-in profiles for major models so strong performance is the default, and the same machinery is available for your own stack.

More in [tuning deep agents across different models](https://www.langchain.com/blog/tuning-deep-agents-different-models). See the [docs](https://docs.langchain.com/oss/python/deepagents/profiles) to write your own.

## Streaming

Agents do a lot of work before they return a final answer. For a good user experience, you want to surface that work as it happens, and give users the ability to steer the agent along the way: streaming is the primitive that makes this possible. LangChain’s new release makes streaming a first-class application primitive. With `stream_events(..., version="v3")`, agents and graphs now emit a unified event stream with ergonomic projections for primitives developers actually want to render: message text, reasoning blocks, tool calls, state updates, subgraphs, subagents, custom channels, and final output. The stream is content-block-centric, which means UIs no longer need to guess whether a chunk is text, reasoning, media, or tool-call data. Everything is organized around typed events, namespaces, and channels, all aligned with the new [Agent Streaming Protocol](https://github.com/langchain-ai/agent-protocol/tree/main/streaming).

```python
stream = agent.stream_events(
    {"messages": [{"role": "user", "content": "Research LangChain streaming"}]},
    version="v3",
)

for message in stream.messages:
    for delta in message.text:
        print(delta, end="", flush=True)

for subagent in stream.subagents:
    print(f"\\n[{subagent.name}] {subagent.status}")

    for message in subagent.messages:
        print(f"[{subagent.name}] ", end="")
        for delta in message.text:
            print(delta, end="", flush=True)
        print()
```

This streaming model also carries over the wire through new Agent Server endpoints and SDK support. The LangGraph SDK exposes remote event streaming through `client.threads.stream(...)`, with support for multimodal content, reconnect/replay behavior, and transport-agnostic delivery over SSE or WebSockets. Because local and remote streams now follow the same protocol, developers get a consistent way to observe agent runs across scripts, backend services, and production frontends. Applications can subscribe to exactly the parts of a run they need, such as messages from a specific subagent, updates from a custom channel, or events within a particular namespace.

On the frontend, this release brings v1 framework integrations for `@langchain/react`, `@langchain/vue`, `@langchain/svelte`, and `@langchain/angular`, giving teams idiomatic hooks and utilities for building rich streamed experiences without hand-rolling event parsers. To make the new stack easy to explore, we’re also publishing the [Streaming Cookbook](https://github.com/langchain-ai/streaming-cookbook): a collection of runnable examples covering message streaming, subgraphs, subagents, custom stream transformers, multimodal UI, reconnect behavior, and framework-specific patterns. The result is a streaming foundation that is lower-level where you need precision, higher-level where you want productivity, and consistent from agent runtime to user interface.

## Delta channels

Deep Agents is built on the LangGraph runtime, which checkpoints agent progress at every step. That's what makes observability, human-in-the-loop, and failure recovery possible: you always know exactly where an agent is and can resume from any point.

As agents get more capable:

1. They run longer, with message histories that grow across dozens or hundreds of steps
2. They use more context, utilizing the filesystem for context management and offloading

For `deepagents`, message history and files live in agent state, and with a snapshot-every-step approach, checkpoint storage grows at O(N²).

Delta channels are how we're evolving the runtime to keep up. Rather than serializing a full snapshot at every checkpoint, we store only the diff. For Deep Agents, that means delta-based storage for message histories and files.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a029525790bff5c3e6d132d_delta_channel_card_v2%20(1)%20(1).svg)

You still get a complete history of agent progress, just at a fraction of the storage cost. This also helps to mitigate the bottleneck of writes to the checkpointer (database) for long-running agents, and storage costs at scale are much more manageable.

Depending on the conversation length and context size, swapping to delta channels can reasonably bring 10-100x reductions in checkpointer storage.

Consider, for example, an experiment: a simulated multi-file coding session where an agent writes files, retrieves documentation, and reasons through its work — 200 turns of the kind of sustained, context-heavy work a capable coding agent actually does. Without delta channels, that session accumulates **5.27 GB** of checkpoint storage. With delta channels: **129 MB**.

Here’s a comparison of checkpointer storage for the same agent with and without delta channels:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a0296bb2b7db2e536d0d613_table_workload_b%20(2)%20(1).svg)

And a graphical representation of said explosion:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a0296c77f447828189b0736_chart_workload_b%20(1).svg)

Long-running agents with deep context are where the field is heading, and delta channels are how our runtime scales to meet their needs.

See the [full writeup](https://www.langchain.com/blog/delta-channels-evolving-agent-runtime) for more details.

## ContextHub Backend

Context Hub is a LangSmith-backed filesystem for Deep Agents. It gives you a versioned place for the files that shape agent behavior, so improvements to prompts, skills, and other context can carry forward across runs.

Under the hood, your agent reads from (and can write to) a Hub repo. Those writes land as commits with history, review, and environment tagging—so you can iterate in staging and promote to production without wiring up a separate storage layer.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a02201c12822b49ff00901d_context-hub-1.png)

To use it as your agent's filesystem backend:

```python
from deepagents import create_deep_agent
from deepagents.backends import ContextHubBackend

agent = create_deep_agent(
    model="google_genai:gemini-3.1-pro-preview",
    backend=ContextHubBackend("my-agent"),
)
```

Or scope just /memories/ to Hub while keeping the rest of the filesystem thread-scoped:

```python
from deepagents.backends import CompositeBackend, StateBackend, ContextHubBackend

agent = create_deep_agent(
    model="google_genai:gemini-3.1-pro-preview",
    backend=CompositeBackend(
        default=StateBackend(),
        routes={
            "/memories/": ContextHubBackend("my-agent"),
        },
    ),
)
```

Reads are served from cache, and writes are committed back to the Hub repo. If the repo doesn’t exist yet, the first write creates it—after that, you can diff, review, and tag changes like any other piece of versioned context.

Set `LANGSMITH_API_KEY` before using `ContextHubBackend`. See the [full docs](https://docs.langchain.com/oss/python/deepagents/backends#contexthubbackend) for conflict handling and limits.

## Wrapping up

The through-line across our Deep Agents May release is performance:

- **Harness profiles** help you squeeze performance out of a model with an optimal harness and unlock viable agent runs on open-weight models at a *fraction* of the cost of frontier APIs
- **Code interpreter** gives an agent more autonomy to write an execute code, helping it accomplish complex tasks and optimize context window usage.
- **Streaming** enables support for highly parallelized systems with a subscription model for tool and subagent progress.
- `DeltaChannel` introduces a storage primitive that supports checkpoints for long-running, long-context agents.
- `ContextHubBackend`**:** a versioned home for the files that power agent behavior, backed by [LangSmith Context Hub](https://smith.langchain.com/context), enables context improvements from one run to the next.

We’re excited for you to give the latest `deepagents` a spin. Let us know what you think!

Release notes:

[Python](https://docs.langchain.com/oss/python/releases/changelog)[TypeScript](https://docs.langchain.com/oss/javascript/releases/changelog)