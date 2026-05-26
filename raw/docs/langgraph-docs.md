Title: LangGraph overview - Docs by LangChain

URL Source: https://docs.langchain.com/oss/python/langgraph/overview

Published Time: Mon, 18 May 2026 06:04:29 GMT

Markdown Content:
> ## Documentation Index
>
>
> Fetch the complete documentation index at: [https://docs.langchain.com/llms.txt](https://docs.langchain.com/llms.txt)
>
>
> Use this file to discover all available pages before exploring further.

Trusted by companies shaping the future of agents— including Klarna, Uber, J.P. Morgan, and more— LangGraph is a low-level orchestration framework and runtime for building, managing, and deploying long-running, stateful agents.LangGraph is very low-level, and focused entirely on agent **orchestration**. Before using LangGraph, we recommend you familiarize yourself with some of the components used to build agents, starting with [models](https://docs.langchain.com/oss/python/langchain/models) and [tools](https://docs.langchain.com/oss/python/langchain/tools).We will commonly use [LangChain](https://docs.langchain.com/oss/python/langchain/overview) components throughout the documentation to integrate models and tools, but you don’t need to use LangChain to use LangGraph. If you are just getting started with agents or want a higher-level abstraction, we recommend you use LangChain’s [agents](https://docs.langchain.com/oss/python/langchain/agents) that provide prebuilt architectures for common LLM and tool-calling loops.LangGraph is focused on the underlying capabilities important for agent orchestration: durable execution, streaming, human-in-the-loop, and more.

Show How LangChain products fit together

*   [Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview) is an [agent harness](https://docs.langchain.com/oss/python/concepts/products#agent-harnesses-like-the-deep-agents-sdk): planning, subagents, filesystem tools, and context management on top of LangGraph.
*   [LangChain](https://docs.langchain.com/oss/python/langchain/overview) is the agent framework: abstractions and integrations for models, tools, and agent loops.
*   [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview) is the orchestration runtime: durable execution, streaming, human-in-the-loop, and persistence.
*   [LangSmith](https://docs.langchain.com/langsmith/home) is the platform for tracing, evaluation, prompts, and deployment across frameworks.
*   [LangSmith Fleet](https://docs.langchain.com/langsmith/fleet/index) is the no-code agent builder for templates, integrations, and routine automation.

Read [Frameworks, runtimes, and harnesses](https://docs.langchain.com/oss/python/concepts/products) for a comparison of the open source stack.

## Install

Then, create a simple hello world example:

```
from langgraph.graph import StateGraph, MessagesState, START, END

def mock_llm(state: MessagesState):
    return {"messages": [{"role": "ai", "content": "hello world"}]}

graph = StateGraph(MessagesState)
graph.add_node(mock_llm)
graph.add_edge(START, "mock_llm")
graph.add_edge("mock_llm", END)
graph = graph.compile()

graph.invoke({"messages": [{"role": "user", "content": "hi!"}]})
```

## Core benefits

LangGraph provides low-level supporting infrastructure for _any_ long-running, stateful workflow or agent. LangGraph does not abstract prompts or architecture, and provides the following central benefits:

*   [Durable execution](https://docs.langchain.com/oss/python/langgraph/durable-execution): Build agents that persist through failures and can run for extended periods, resuming from where they left off.
*   [Human-in-the-loop](https://docs.langchain.com/oss/python/langgraph/interrupts): Incorporate human oversight by inspecting and modifying agent state at any point.
*   [Comprehensive memory](https://docs.langchain.com/oss/python/concepts/memory): Create stateful agents with both short-term working memory for ongoing reasoning and long-term memory across sessions.
*   [Debugging with LangSmith](https://docs.langchain.com/langsmith/home): Gain deep visibility into complex agent behavior with visualization tools that trace execution paths, capture state transitions, and provide detailed runtime metrics.
*   [Production-ready deployment](https://docs.langchain.com/langsmith/deployment): Deploy sophisticated agent systems confidently with scalable infrastructure designed to handle the unique challenges of stateful, long-running workflows.

## LangGraph ecosystem

While LangGraph can be used standalone, it also integrates seamlessly with any LangChain product, giving developers a full suite of tools for building agents. To improve your LLM application development, pair LangGraph with:

## Acknowledgements

LangGraph is inspired by [Pregel](https://research.google/pubs/pub37252/) and [Apache Beam](https://beam.apache.org/). The public interface draws inspiration from [NetworkX](https://networkx.org/documentation/latest/). LangGraph is built by LangChain Inc, the creators of LangChain, but can be used without LangChain.

* * *
