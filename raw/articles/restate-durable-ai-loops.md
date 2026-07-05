Title: Durable AI Loops: Fault Tolerance across Frameworks and without Handcuffs

URL Source: https://www.restate.dev/blog/durable-ai-loops-fault-tolerance-across-frameworks-and-without-handcuffs

Published Time: 2025-06-19

Markdown Content:
An AI agent is just regular code - a loop or workflow to gather context ➜ call tools or an LLM ➜ figure out what to do next ➜ repeat. That simplicity is why we love them—and why they break so easily.

![Image 1: Tweet by Garry Tan](https://www.restate.dev/blog/ai/tweet.png)
In practice, **agents behave a lot like distributed systems**: every tool call is a remote hop, every user interaction is a pause, every retry risks doing the same work twice. Distributed systems fail in a million tiny ways, and agents inherit every single one of them. A single network hickup can mean that the agent loses all context and progress.

What no developer wants is to rebuild the kind of heavyweight _"defensive infrastructure"_ that classic distributed systems needed—message queues, checkpoint daemons, idempotency keys, custom replay logic, the works.

That's the itch we've been scratching for years. Our engineers spent a decade designing Apache Flink's fault‑tolerant runtime, or worked on Meta's event log systems (_LogDevice, Scribe_). The last two years, we have been building [Restate](https://restate.dev/), a lightweight engine that bakes innate resilience into ordinary functions. The same ideas map perfectly onto agent loops: wrap the step that might fail, let the runtime persist inputs and results, and your agent picks up right where it left off—no SDK‑specific magic, no extra scaffolding.

The rest of this post shows what that looks like in real code and why it lets you keep the elegant _agents‑are‑just‑code_ model without inheriting the failure baggage that usually comes with it.

Everything we show here is independent and orthogonal to any agent SDK. To illustrate that, we use both the [Vercel AI SDK](https://ai-sdk.dev/) (TypeScript) and [OpenAI Agent SDK](https://openai.github.io/openai-agents-python/) (Python) for our examples, demonstrating **resilience, suspendability, observability, human-in-the-loop support, and reliable multi-agent orchestration**. All the code snippets can be found in the [AI examples repository](https://github.com/restatedev/ai-examples/tree/main).

## Durable Execution: workflow guarantees for existing agents and code

One of Restate's tools is _durable execution_ — a near-magical approach that lets your code behave as if it could run forever without crashing: Failures result in retries that bring the agent back to the last completed step before the crash.

[Video 3](https://www.youtube.com/watch?v=frJP6yNWYFg)

An agent recovering from a crash without losing the progress it made. Durable Execution handles retries and recovery.

To make use of durable execution, we need to wrap expensive and non-deterministic actions (LLM inference calls and tool invocations) into durable steps that can be restored after a crash. Many popular AI SDKs (e.g., Vercel AI SDK, OpenAI Agents SDK) let you plug in middleware for that purpose. Here is an example of how you can turn a tool into a durable tool, whose results are restored after failures (_the Restate Context will be connected to Restate in the next step_).

Vanilla SDK

```
const model = openai("gpt-4o-2024-08-06");

const weather = tool({
  description: "Get current weather for a city.",
  parameters: z.object({ city: z.string() }),
  execute: async ({ city }) => {
      const result = await fetchWeather(city);
      return await parseWeatherResponse(result);
  },
});
```

Durable Model / Tool (Restate)

```
const model = wrapLanguageModel({
  model: openai("gpt-4o-2024-08-06"),
  middleware: durableCalls(
    restate_ctx, 
    { maxRetryAttempts: 3 }
  ),
});

const weather = tool({
  description: "Get current weather for a city.",
  parameters: z.object({ city: z.string() }),
  execute: async ({ city }) => {
    const result = await restate_ctx.run(
        async () => fetchWeather(city)
    );
    return await parseWeatherResponse(result);
  },
});
```

These are all the code changes you need in your agent.

As a final step, we need to [serve the agent and connect is to Restate](https://github.com/restatedev/ai-examples/blob/775341914005f37638c6bf32213d0b66f1d38fc5/agents/vercel-ai/restate/services/multi_tool.ts#L33). Restate’s server sits in front of your agent process, similar to a message broker or a reverse proxy. You call your agent through Restate, letting it take full control of the connection to transparently handle failure detection, retries, scaling, concurrency control, while keeping the agent process lightweight.

This setup gives you a fully resilient agentic workflow that can run for very long times and recover previous progress after failures! As a bonus, we also get idempotency for free and the ability to detach/re-attach from agents, schedule calls, or directly trigger agents from Kafka.

![Image 2: Durable Execution with Restate](https://www.restate.dev/blog/ai/durable_execution.gif)

Restate records the results of intermediate steps in the journal and uses it to recover the execution to the point where it failed.

## Observability

Because Restate manages the calls to the agentic workflow function and tracks the progress journal, it knows a great deal about what your agent is doing. Without setting up any additional infrastructure, you can see all executions and steps from your agentic workflows. You can also inspect how agents interact with each other and their state (sorry for the spoiler, keep reading to get the details).

![Image 3: Restate UI](https://www.restate.dev/blog/ai/observability.png)

The Restate UI showing the progress journal of a call to the weather agent with the [Restate + Vercel AI template](https://github.com/restatedev/ai-examples/tree/main/vercel-ai/template).

This is a treasure trove of information to learn, debug, and audit what your agents did. You can find more examples of what the UI shows you in [this blog post](https://www.restate.dev/blog/announcing-restate-ui/). Imagine how useful it would be to have this kind of information when deploying your agents to production!

## Long-running tasks & human-in-the-loop

Sometimes you need to include a human evaluator, approval step, or another external signal in an agentic workflow. In a simple standalone app, you could model this by awaiting a promise/future that gets completed via a callback. Luckily, Durable Execution allows us to do the exact same thing, without worrying about failures or interruptions.

On top of that, since all the agent's progress is stored in a journal, we can shut down the agent when it awaits the promise and restore it once the approval has come in (the promise is completed). This is particularly valuable for serverless platforms where you get billed by the millisecond: you pay for active work, not the wait time.

TypeScript

 
Python

![Image 4: Human in the loop Vercel AI SDK + Restate + TypeScript](https://www.restate.dev/blog/ai/human_approval_typescript.gif)

A human approval tool with the Vercel AI SDK that suspends while waiting.

![Image 5: Human in the loop OpenAI Agent SDK + Restate + Python](https://www.restate.dev/blog/ai/human_approval_python.gif)

A human approval tool with the OpenAI Agent SDK that suspends while waiting.

Depending on the deployment, you might want to suspend your agent even while it awaits the result of a long LLM inference call. You can do that simply by moving the inference calls to a different process and letting it call back into the agent by completing a durable promise with the inference result. Some Durable Execution platforms (for example Restate) let you mix and match FaaS and long-running processes/containers, so you can run the AI agent code on FaaS (like Lambda) and move the inference calls to a container (à la Fargate).

## Beyond Durable Execution: Sessions and memory

So far, we've focused on handling a single request and a single conversation. But in many scenarios, you have long-running multi-turn conversations with agents. A user might start a conversation now, respond hours later, and return again after a few days. Multiple users may be having separate conversations going on, and a single conversation may be open in multiple browser windows.

While Durable Execution doesn’t handle this directly, Restate extends it with a feature called _[Virtual Objects](https://docs.restate.dev/concepts/services#virtual-objects)_: durable functions with an identity and the ability to store state. A single object (identified by a key, such as _user\_id_ or _session\_id_) would represent a specific multi-step conversation, allowing for long-lived stateful interactions.

![Image 6: Sessions](https://www.restate.dev/blog/ai/sessions.png)

Virtual Objects guarantee that a single instance exists per key, queue interactions, and store transactional state. They offer a convenient way to store the message history and other data, like the last agent who the user talked to.

```
// Keyed by session ID
const agent = restate.object({
  name: "Agent",
  handlers: {
      run: async (restate_ctx: restate.ObjectContext, message: string) => {
          // Load the session context
          const messages = (await restate_ctx.get<Message[]>("messages")) ?? [];
          messages.push({role: "user", content: message});

          const result = await runVercelAIAgent(restate_ctx, messages);

          // Store the session context
          messages.push({role: "assistant", content: result});
          restate_ctx.set("messages", messages);
          return result;
      },
  }
});
```

The Restate UI gives us a nice overview of the state stored in the Agent objects:

![Image 7: Agent state Restate UI](https://www.restate.dev/blog/ai/agent_state.png)

This approach is complementary to AI memory solutions like _mem0_ or _graffiti_. You can use virtual objects to enforce session concurrency and queueing (optionally remember session context) while storing the agent's memory in mem0.

## Resilient multi-agent systems

We now have stateful, resilient, long-running agents; this includes multi-agent applications as modeled by the OpenAI SDK, where all agents share the same process and loop. In that setup, handing work over to another agent means primarily switching prompt, tool set, and some context/history information for the next loop iteration.

![Image 8: Restate multi-agent](https://www.restate.dev/blog/ai/multi-agent.png)

For true distributed multi-agent setups, where agents run concurrently as separate processes (to execute and scale independently), the final missing piece is reliable asynchronous communication:

*   Communication channels that recover from failures
*   End-to-end idempotency to avoid kicking off expensive work twice
*   Suspending the calling agent while the callee agents are doing work
*   Reliable scheduling of agent invocations, for periodic work

Restate extends Durable Execution with such messaging and RPC between durable functions, so handing over work to another agent looks just like RPC-ing them. The examples below expose remote agents via tools:

```
tool({
  description: "Handoff to BlueSky agent for research.",
  parameters: z.object({ prompt: z.string() }),
  execute: async ({ prompt }) =>
      await restate_ctx.serviceClient(blueSkyAgent).run_agent(prompt),
});
```

While this looks like a simple RPC client making a call, the invocation of the target agent is asynchronous and durable (like a queue), lets the caller suspend while awaiting a response, can be detached / re-attached, canceled, and lets you kick off and await multiple parallel remote agents. Because Restate acts simultaneously as the message/RPC broker and Durable Execution orchestrator on both caller and callee side, it can transparently guarantee end-to-end idempotency and resilience. The same mechanism also lets us reliably schedule invocations for later, for example, to schedule an agentic task for later.

```
tool({
  description: "Schedule a task to be executed by the agent after a delay.",
  parameters: z.object({ task: z.string(), delay: z.number() }),
  execute: async ({ task, delay }) => {
      restate_ctx
          .serviceSendClient(taskAgent)
          .doTask(task, restate.rpc.sendOpts({ delay }));
  },
});
```

If this feels reminiscent of [A2A](https://github.com/google-a2a/A2A), that is no co-incidence: Restate can be thought of as a general-purpose stateful task orchestration framework. A2A is an orchestration framework for agents, and can be easily implemented on top of the more general Restate framework. If you are adopting A2A, [here is an implementation of a fully resilient A2A server using Restate](https://github.com/restatedev/ai-examples/tree/main/a2a) that can be self-hosted and scale from laptop to multi-zone cluster.

## Build Agentic Workflows like any other code

At the end of the day, agents are just programs. The same principles that make any system or backend service resilient and scalable apply to them.

Durable Execution, paired with your existing SDKs, gives your agents a powerful upgrade: resilience to failure, observability by default, suspendability, memory, and multi-agent coordination, without locking you into a specific AI framework or cloud service.

And when agents look and run like any other code, it also becomes easy to navigate between deterministic workflows that use AI tools and some full-blown agentic workflow sections that employ LLM/tool loops for autonomous problem solving. And this is ultimately [the sweet-spot for AI applications](https://tomtunguz.com/agentic-workflows/) today.

If this resonates with you, here are some ways to get started:

*   🚀 Start with our [Vercel AI](https://github.com/restatedev/ai-examples/tree/main/vercel-ai/template) or [OpenAI](https://github.com/restatedev/ai-examples/tree/main/openai-agents/template) templates
*   🔧 Dive deeper into [how Durable Execution works under the hood](https://restate.dev/blog/building-a-modern-durable-execution-engine-from-first-principles/)
*   ☁️ Try [Restate Cloud](https://restate.dev/cloud/) or [self-host](https://docs.restate.dev/get-restate)

✨ [Star us on GitHub](https://github.com/restatedev/restate) and join the conversation on [Discord](https://discord.restate.dev/) or [Slack](https://slack.restate.dev/) — we’d love to hear what you’re building.

Note: Parallel tool calls aren’t supported out of the box due to non-deterministic replay. For that, use Restate’s promise combinators ([TS](https://docs.restate.dev/develop/ts/journaling-results#combineable-promise-combinators)/[Python](https://docs.restate.dev/develop/python/journaling-results#waiting-multiple-futures)) and [wrap the logic in a single tool](https://docs.restate.dev/ai/patterns/parallelization).
