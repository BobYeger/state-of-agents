Title: Deep Agents overview - Docs by LangChain

URL Source: https://docs.langchain.com/oss/python/deepagents/overview

Published Time: Mon, 18 May 2026 06:04:31 GMT

Markdown Content:
> ## Documentation Index
> 
> 
> Fetch the complete documentation index at: [https://docs.langchain.com/llms.txt](https://docs.langchain.com/llms.txt)
> 
> 
> Use this file to discover all available pages before exploring further.

The easiest way to start building agents and applications powered by LLMs—with built-in capabilities for task planning, file systems for context management, subagent-spawning, and long-term memory. You can use deep agents for any task, including complex, multi-step tasks.We think of `deepagents` as an [“agent harness”](https://docs.langchain.com/oss/python/concepts/products#agent-harnesses-like-the-deep-agents-sdk). It is the same core tool calling loop as other agent frameworks, but with built-in tools and capabilities.

[`deepagents`](https://pypi.org/project/deepagents/) is a standalone library built on top of [LangChain](https://docs.langchain.com/oss/python/langchain)’s core building blocks for agents. It uses the [LangGraph](https://docs.langchain.com/oss/python/langgraph) runtime for durable execution, streaming, human-in-the-loop, and other features.The [`deepagents` repository](https://github.com/langchain-ai/deepagents) contains:

*   **Deep Agents SDK**: A package for building agents that can handle any task
*   [**Deep Agents Code**](https://docs.langchain.com/oss/python/deepagents/code): A terminal coding agent built on the Deep Agents SDK
*   [**ACP integration**](https://docs.langchain.com/oss/python/deepagents/acp): An Agent Client Protocol connector for using deep agents in code editors like Zed

[LangChain](https://docs.langchain.com/oss/python/langchain) is the framework that provides the core building blocks for your agents. To learn more about the differences between LangChain, LangGraph, and Deep Agents, see [Frameworks, runtimes, and harnesses](https://docs.langchain.com/oss/python/concepts/products). For a side-by-side comparison with Anthropic’s harness, see [Deep Agents vs. Claude Agent SDK](https://docs.langchain.com/oss/python/deepagents/comparison).

## Create a deep agent

*   Google

*   OpenAI

*   Anthropic

*   OpenRouter

*   Fireworks

*   Baseten

*   Ollama

```
# pip install -qU deepagents langchain-google-genai
from deepagents import create_deep_agent

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_deep_agent(
    model="google_genai:gemini-3.1-pro-preview",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)
```

```
# pip install -qU deepagents langchain-openai
from deepagents import create_deep_agent

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_deep_agent(
    model="openai:gpt-5.4",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)
```

```
# pip install -qU deepagents langchain-anthropic
from deepagents import create_deep_agent

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)
```

```
# pip install -qU deepagents langchain-openrouter
from deepagents import create_deep_agent

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_deep_agent(
    model="openrouter:anthropic/claude-sonnet-4-6",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)
```

```
# pip install -qU deepagents langchain-fireworks
from deepagents import create_deep_agent

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_deep_agent(
    model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)
```

```
# pip install -qU deepagents langchain-baseten
from deepagents import create_deep_agent

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_deep_agent(
    model="baseten:zai-org/GLM-5",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)
```

```
# pip install -qU deepagents langchain-ollama
from deepagents import create_deep_agent

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_deep_agent(
    model="ollama:devstral-2",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)
```

See the [Quickstart](https://docs.langchain.com/oss/python/deepagents/quickstart) and [Customization guide](https://docs.langchain.com/oss/python/deepagents/customization) to get started building your own agents and applications with Deep Agents.

## When to use the Deep Agents

Use the **Deep Agents SDK** when you want to build agents that can:

*   **Handle complex, multi-step tasks** that require planning and decomposition
*   **Manage large amounts of context** through file system tools and [summarization](https://docs.langchain.com/oss/python/deepagents/context-engineering#summarization)
*   **Swap filesystem backends** to use in-memory state, local disk, durable stores, [sandboxes](https://docs.langchain.com/oss/python/deepagents/sandboxes), or [your own custom backend](https://docs.langchain.com/oss/python/deepagents/backends)
*   **Execute shell commands** via the `execute` tool when using a [sandbox backend](https://docs.langchain.com/oss/python/deepagents/sandboxes)
*   **Run interpreter code** with [interpreters](https://docs.langchain.com/oss/python/deepagents/interpreters) for tool composition, subagent orchestration, and structured data transformations
*   **Delegate work** to specialized subagents for context isolation
*   **Persist memory** across conversations and threads
*   **Control filesystem access** with declarative [permission rules](https://docs.langchain.com/oss/python/deepagents/permissions) that restrict which files agents can read or write
*   **Require human approval** for sensitive operations with [human-in-the-loop](https://docs.langchain.com/oss/python/deepagents/human-in-the-loop) workflows
*   **Use any model** — [provider agnostic](https://docs.langchain.com/oss/python/deepagents/models) across frontier and open models

For building simpler agents, consider using LangChain’s [`create_agent`](https://docs.langchain.com/oss/python/langchain/agents) or building a custom [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview) workflow.

## Core capabilities

## Get started

* * *
