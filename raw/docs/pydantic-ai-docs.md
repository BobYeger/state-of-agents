Title: Pydantic AI

URL Source: https://pydantic.dev/docs/ai/overview/

Markdown Content:
_GenAI Agent Framework, the Pydantic way_

[![Image 1: CI](https://github.com/pydantic/pydantic-ai/actions/workflows/ci.yml/badge.svg?event=push)](https://github.com/pydantic/pydantic-ai/actions/workflows/ci.yml?query=branch%3Amain)[![Image 2: Coverage](https://coverage-badge.samuelcolvin.workers.dev/pydantic/pydantic-ai.svg)](https://coverage-badge.samuelcolvin.workers.dev/redirect/pydantic/pydantic-ai)[![Image 3: PyPI](https://img.shields.io/pypi/v/pydantic-ai.svg)](https://pypi.python.org/pypi/pydantic-ai)[![Image 4: versions](https://img.shields.io/pypi/pyversions/pydantic-ai.svg)](https://github.com/pydantic/pydantic-ai)[![Image 5: license](https://img.shields.io/github/license/pydantic/pydantic-ai.svg)](https://github.com/pydantic/pydantic-ai/blob/main/LICENSE)[![Image 6: Join Slack](https://img.shields.io/badge/Slack-Join%20Slack-4A154B?logo=slack)](https://logfire.pydantic.dev/docs/join-slack/)

Pydantic AI is a Python agent framework designed to help you quickly, confidently, and painlessly build production grade applications and workflows with Generative AI.

FastAPI revolutionized web development by offering an innovative and ergonomic design, built on the foundation of [Pydantic Validation](https://docs.pydantic.dev/) and modern Python features like type hints.

Yet despite virtually every Python agent framework and LLM library using Pydantic Validation, when we began to use LLMs in [Pydantic Logfire](https://pydantic.dev/logfire), we couldn’t find anything that gave us the same feeling.

We built Pydantic AI with one simple aim: to bring that FastAPI feeling to GenAI app and agent development.

1.   **Built by the Pydantic Team**: [Pydantic Validation](https://docs.pydantic.dev/latest/) is the validation layer of the OpenAI SDK, the Google ADK, the Anthropic SDK, LangChain, LlamaIndex, AutoGPT, Transformers, CrewAI, Instructor and many more. _Why use the derivative when you can go straight to the source?_ 😃

2.   **Model-agnostic**: Supports virtually every [model](https://pydantic.dev/docs/ai/models/overview) and provider: OpenAI, Anthropic, Gemini, DeepSeek, Grok, Cohere, Mistral, and Perplexity; Azure AI Foundry, Amazon Bedrock, Google Cloud, Ollama, LiteLLM, Groq, OpenRouter, Together AI, Fireworks AI, Cerebras, Hugging Face, GitHub, Heroku, Vercel, Nebius, OVHcloud, Alibaba Cloud, and SambaNova. If your favorite model or provider is not listed, you can easily implement a [custom model](https://pydantic.dev/docs/ai/models/overview#custom-models).

3.   **Seamless Observability**: Tightly [integrates](https://pydantic.dev/docs/ai/integrations/logfire) with [Pydantic Logfire](https://pydantic.dev/logfire), our general-purpose OpenTelemetry observability platform, for real-time debugging, evals-based performance monitoring, and behavior, tracing, and cost tracking. If you already have an observability platform that supports OTel, you can [use that too](https://pydantic.dev/docs/ai/integrations/logfire#alternative-observability-backends).

4.   **Fully Type-safe**: Designed to give your IDE or AI coding agent as much context as possible for auto-completion and [type checking](https://pydantic.dev/docs/ai/core-concepts/agent#static-type-checking), moving entire classes of errors from runtime to write-time for a bit of that Rust “if it compiles, it works” feel.

5.   **Powerful Evals**: Enables you to systematically test and [evaluate](https://pydantic.dev/docs/ai/evals/) the performance and accuracy of the agentic systems you build, and monitor the performance over time in Pydantic Logfire.

6.   **Extensible by Design**: Build agents from composable [capabilities](https://pydantic.dev/docs/ai/core-concepts/capabilities) that bundle tools, hooks, instructions, and model settings into reusable units. Use built-in capabilities for [web search](https://pydantic.dev/docs/ai/core-concepts/capabilities#provider-adaptive-tools), [thinking](https://pydantic.dev/docs/ai/core-concepts/capabilities#thinking), and [MCP](https://pydantic.dev/docs/ai/core-concepts/capabilities#provider-adaptive-tools), pick from the [Pydantic AI Harness](https://pydantic.dev/docs/ai/harness/overview) capability library, build your own, or install [third-party capability packages](https://pydantic.dev/docs/ai/guides/extensibility). Define agents entirely in [YAML/JSON](https://pydantic.dev/docs/ai/core-concepts/agent-spec) — no code required.

7.   **MCP, A2A, and UI**: Integrates the [Model Context Protocol](https://pydantic.dev/docs/ai/mcp/overview), [Agent2Agent](https://pydantic.dev/docs/ai/integrations/a2a), and various [UI event stream](https://pydantic.dev/docs/ai/integrations/ui/overview) standards to give your agent access to external tools and data, let it interoperate with other agents, and build interactive applications with streaming event-based communication.

8.   **Human-in-the-Loop Tool Approval**: Easily lets you flag that certain tool calls [require approval](https://pydantic.dev/docs/ai/tools-toolsets/deferred-tools#human-in-the-loop-tool-approval) before they can proceed, possibly depending on tool call arguments, conversation history, or user preferences.

9.   **Durable Execution**: Enables you to build [durable agents](https://pydantic.dev/docs/ai/integrations/durable_execution/overview) that can preserve their progress across transient API failures and application errors or restarts, and handle long-running, asynchronous, and human-in-the-loop workflows with production-grade reliability.

10.   **Streamed Outputs**: Provides the ability to [stream](https://pydantic.dev/docs/ai/core-concepts/output#streamed-results) structured output continuously, with immediate validation, ensuring real time access to generated data.

11.   **Graph Support**: Provides a powerful way to define [graphs](https://pydantic.dev/docs/ai/graph/) using type hints, for use in complex applications where standard control flow can degrade to spaghetti code.

Realistically though, no list is going to be as convincing as [giving it a try](https://pydantic.dev/docs/ai/overview/#next-steps) and seeing how it makes you feel!

**Sign up for our newsletter, _The Pydantic Stack_, with updates & tutorials on Pydantic AI, Logfire, and Pydantic:**

Here’s a minimal example of Pydantic AI:

hello_world.py

`from pydantic_ai import Agentagent = Agent(    'anthropic:claude-sonnet-4-6',  instructions='Be concise, reply with one sentence.',  )result = agent.run_sync('Where does "hello world" come from?')  print(result.output)"""The first known use of "hello, world" was in a 1974 textbook about the C programming language."""`

Register static [instructions](https://pydantic.dev/docs/ai/core-concepts/agent#instructions) using a keyword argument to the agent.

[Run the agent](https://pydantic.dev/docs/ai/core-concepts/agent#running-agents) synchronously, starting a conversation with the LLM.

_(This example is complete, it can be run “as is”, assuming you’ve [installed the `pydantic\_ai` package](https://pydantic.dev/docs/ai/overview/install))_

The exchange will be very short: Pydantic AI will send the instructions and the user prompt to the LLM, and the model will return a text response.

Not very interesting yet, but we can easily add [tools](https://pydantic.dev/docs/ai/tools-toolsets/tools), [dynamic instructions](https://pydantic.dev/docs/ai/core-concepts/agent#instructions), [structured outputs](https://pydantic.dev/docs/ai/core-concepts/output), or composable [capabilities](https://pydantic.dev/docs/ai/core-concepts/capabilities) to build more powerful agents.

Here’s the same agent with [thinking](https://pydantic.dev/docs/ai/core-concepts/capabilities#thinking) and [web search](https://pydantic.dev/docs/ai/core-concepts/capabilities#provider-adaptive-tools) capabilities:

hello_world_capabilities.py

`from pydantic_ai import Agentfrom pydantic_ai.capabilities import Thinking, WebSearchagent = Agent(    'anthropic:claude-sonnet-4-6',    instructions='Be concise, reply with one sentence.',    capabilities=[Thinking(), WebSearch(local='duckduckgo')],)result = agent.run_sync('What was the mass of the largest meteorite found this year?')print(result.output)"""The largest meteorite recovered this year weighed approximately 7.6 kg, found in the Sahara Desert in January."""`
Here is a concise example using Pydantic AI to build a support agent for a bank:

bank_support.py

`from dataclasses import dataclassfrom pydantic import BaseModel, Fieldfrom pydantic_ai import Agent, RunContextfrom bank_database import DatabaseConn@dataclassclass SupportDependencies:    customer_id: int  db: DatabaseConn  class SupportOutput(BaseModel):    support_advice: str = Field(description='Advice returned to the customer')  block_card: bool = Field(description="Whether to block the customer's card")  risk: int = Field(description='Risk level of query', ge=0, le=10)support_agent = Agent(    'openai:gpt-5.2',    deps_type=SupportDependencies,  output_type=SupportOutput,    instructions=(        'You are a support agent in our bank, give the '      'customer support and judge the risk level of their query.'  ),)@support_agent.instructions  async def add_customer_name(ctx: RunContext[SupportDependencies]) -> str:  customer_name = await ctx.deps.db.customer_name(id=ctx.deps.customer_id)  return f"The customer's name is {customer_name!r}"@support_agent.tool  async def customer_balance(  ctx: RunContext[SupportDependencies], include_pending: bool) -> float:  """Returns the customer's current account balance."""    return await ctx.deps.db.customer_balance(      id=ctx.deps.customer_id,      include_pending=include_pending,  )...  async def main():  deps = SupportDependencies(customer_id=123, db=DatabaseConn())  result = await support_agent.run('What is my balance?', deps=deps)    print(result.output)    """  support_advice='Hello John, your current account balance, including pending transactions, is $123.45.' block_card=False risk=1  """  result = await support_agent.run('I just lost my card!', deps=deps)  print(result.output)  """  support_advice="I'm sorry to hear that, John. We are temporarily blocking your card to prevent unauthorized transactions." block_card=True risk=8  """`

This [agent](https://pydantic.dev/docs/ai/core-concepts/agent) will act as first-tier support in a bank. Agents are generic in the type of dependencies they accept and the type of output they return. In this case, the support agent has type `Agent[SupportDependencies, SupportOutput]`.

Here we configure the agent to use [OpenAI's GPT-5 model](https://pydantic.dev/docs/ai/models/openai), you can also set the model when running the agent.

The `SupportDependencies` dataclass is used to pass data, connections, and logic into the model that will be needed when running [instructions](https://pydantic.dev/docs/ai/core-concepts/agent#instructions) and [tool](https://pydantic.dev/docs/ai/tools-toolsets/tools) functions. Pydantic AI's system of dependency injection provides a [type-safe](https://pydantic.dev/docs/ai/core-concepts/agent#static-type-checking) way to customise the behavior of your agents, and can be especially useful when running [unit tests](https://pydantic.dev/docs/ai/guides/testing) and evals.

Dynamic [instructions](https://pydantic.dev/docs/ai/core-concepts/agent#instructions) can be registered with the [`@agent.instructions`](https://pydantic.dev/docs/ai/api/pydantic-ai/agent/#pydantic_ai.agent.Agent.instructions) decorator, and can make use of dependency injection. Dependencies are carried via the [`RunContext`](https://pydantic.dev/docs/ai/api/pydantic-ai/tools/#pydantic_ai.tools.RunContext) argument, which is parameterized with the `deps_type` from above. If the type annotation here is wrong, static type checkers will catch it.

The [`@agent.tool`](https://pydantic.dev/docs/ai/tools-toolsets/tools) decorator let you register functions which the LLM may call while responding to a user. Again, dependencies are carried via [`RunContext`](https://pydantic.dev/docs/ai/api/pydantic-ai/tools/#pydantic_ai.tools.RunContext), any other arguments become the tool schema passed to the LLM. Pydantic is used to validate these arguments, and errors are passed back to the LLM so it can retry.

The docstring of a tool is also passed to the LLM as the description of the tool. Parameter descriptions are [extracted](https://pydantic.dev/docs/ai/tools-toolsets/tools#function-tools-and-schema) from the docstring and added to the parameter schema sent to the LLM.

[Run the agent](https://pydantic.dev/docs/ai/core-concepts/agent#running-agents) asynchronously, conducting a conversation with the LLM until a final response is reached. Even in this fairly simple case, the agent will exchange multiple messages with the LLM as tools are called to retrieve an output.

The response from the agent will be guaranteed to be a `SupportOutput`. If validation fails [reflection](https://pydantic.dev/docs/ai/core-concepts/agent#reflection-and-self-correction), the agent is prompted to try again.

The output will be validated with Pydantic to guarantee it is a `SupportOutput`, since the agent is generic, it'll also be typed as a `SupportOutput` to aid with static type checking.

In a real use case, you'd add more tools and longer instructions to the agent to extend the context it's equipped with and support it can provide.

This is a simple sketch of a database connection, used to keep the example short and readable. In reality, you'd be connecting to an external database (e.g. PostgreSQL) to get information about customers.

This [Pydantic](https://docs.pydantic.dev/) model is used to constrain the structured data returned by the agent. From this simple definition, Pydantic builds the JSON Schema that tells the LLM how to return the data, and performs validation to guarantee the data is correct at the end of the run.

Even a simple agent with just a handful of tools can result in a lot of back-and-forth with the LLM, making it nearly impossible to be confident of what’s going on just from reading the code. To understand the flow of the above runs, we can watch the agent in action using Pydantic Logfire.

To do this, we need to [set up Logfire](https://pydantic.dev/docs/ai/integrations/logfire#using-logfire), and add the following to our code:

bank_support_with_logfire.py

`...from pydantic_ai import Agent, RunContextfrom bank_database import DatabaseConnimport logfirelogfire.configure()  logfire.instrument_pydantic_ai()  logfire.instrument_sqlite3()  ...support_agent = Agent(  'openai:gpt-5.2',  deps_type=SupportDependencies,  output_type=SupportOutput,  instructions=(      'You are a support agent in our bank, give the '      'customer support and judge the risk level of their query.'  ),)`

Configure the Logfire SDK, this will fail if project is not set up.

This will instrument all Pydantic AI agents used from here on out. To instrument only a specific agent, add an [`Instrumentation`](https://pydantic.dev/docs/ai/api/pydantic-ai/capabilities/#pydantic_ai.capabilities.Instrumentation) entry to the agent's `capabilities=[...]`.

That’s enough to get the following view of your agent in action:

Logfire instrumentation for the bank agent — [View in Logfire](https://logfire-eu.pydantic.dev/public-trace/a2957caa-b7b7-4883-a529-777742649004?spanId=31aade41ab896144)

See [Monitoring and Performance](https://pydantic.dev/docs/ai/integrations/logfire) to learn more.

The Pydantic AI documentation is available in the [llms.txt](https://llmstxt.org/) format. This format is defined in Markdown and suited for LLMs and AI coding assistants and agents.

Two formats are available:

*   [`llms.txt`](https://ai.pydantic.dev/llms.txt): a file containing a brief description of the project, along with links to the different sections of the documentation. The structure of this file is described in details [here](https://llmstxt.org/#format).
*   [`llms-full.txt`](https://ai.pydantic.dev/llms-full.txt): Similar to the `llms.txt` file, but every link content is included. Note that this file may be too large for some LLMs.

As of today, these files are not automatically leveraged by IDEs or coding agents, but they will use it if you provide a link or the full text.

To try Pydantic AI for yourself, [install it](https://pydantic.dev/docs/ai/overview/install) and follow the instructions [in the examples](https://pydantic.dev/docs/ai/examples/setup).

Read the [docs](https://pydantic.dev/docs/ai/core-concepts/agent) to learn more about building applications with Pydantic AI.

Read the [API Reference](https://pydantic.dev/docs/ai/api/pydantic-ai/agent) to understand Pydantic AI’s interface.

Join [Slack](https://logfire.pydantic.dev/docs/join-slack/) or file an issue on [GitHub](https://github.com/pydantic/pydantic-ai/issues) if you have any questions.
