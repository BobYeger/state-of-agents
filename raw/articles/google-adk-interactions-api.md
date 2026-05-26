Title: Building agents with the ADK and the new Interactions API

URL Source: https://developers.googleblog.com/en/building-agents-with-the-adk-and-the-new-interactions-api/

Published Time: 2025-12-11

Markdown Content:
DEC. 11, 2025

The landscape of AI development is shifting from stateless request-response cycles to stateful, multi-turn agentic workflows. With the beta launch of the [**Interactions API**](https://blog.google/technology/developers/interactions-api), Google is providing a unified interface designed specifically for this new era—offering a single gateway to both raw models and the fully managed [**Gemini Deep Research Agent**](https://blog.google/technology/developers/deep-research-agent-gemini-api).

For developers already working with the **Agent Development Kit (ADK)** and the **Agent2Agent (A2A)** protocol, this raises an exciting question: _How does this new API fit into my existing ecosystem?_

The answer is two-fold. The Interactions API acts as both an alternative to the existing `generateContent` inference API endpoint and as a powerful primitive you can use _within_ an existing agent framework.

In this post, we’ll explore two primary patterns for integration:

1.   **Powering your ADK Agents:** Using the Interactions API as the inference engine for your custom agents.
2.   **The Transparent Bridge:** Collaborating with built-in agents (like Gemini Deep Research Agent) at standard remote A2A agents using the Interactions API.


## Pattern 1: Writing Agents with ADK and Interactions API

When you build an agent using the [ADK (Agent Development Kit)](https://google.github.io/adk-docs/), you need a LLM like Gemini which generates the thoughts, plans, tool calls and responses. Previously, this was handled by `generateContent`.

The new Interactions API offers a native interface for complex state management. By upgrading your inference calls to use this new endpoint, your ADK agents gain access to capabilities designed specifically for agentic loops.

### **Why switch?**

*   **Unified Model & Agent Access:** The same API endpoint works for a standard model (`model=”gemini-3-pro-preview”`) or a built-in Gemini agent (`agent=”deep-research-pro-preview-12-2025”`).
*   **Simplified State Management:** You can optionally offload conversation history management to the server using `previous_interaction_id`, reducing the boilerplate code in your ADK agent.
*   **Background Execution:** The API supports long-running tasks (such as those performed by the Deep Research agent) via a background execution mode. By setting `background=True`, the API immediately returns an interaction ID and offloads the reasoning loop to the server. This allows the client to disconnect without hitting timeouts and asynchronously poll the endpoint to retrieve the final output.
*   **Native Thought Handling:** The API explicitly models "thoughts" separate from final responses, allowing your ADK agent to process reasoning chains more effectively.

### **How it looks**

Instead of managing a raw list of messages and sending them to `generateContent`, your ADK agent can maintain a lighter-weight pointer to the server-side state.

```
from google.adk.agents.llm_agent import Agent
from google.adk.models.google_llm import Gemini
from google.adk.tools.google_search_tool import GoogleSearchTool

root_agent = Agent(
    model=Gemini(
        model="gemini-2.5-flash",
        # Enable Interactions API
        use_interactions_api=True,
    ),
    name="interactions_test_agent",
    tools=[
        # Converted Google Search to a function tool
        GoogleSearchTool(bypass_multi_tools_limit=True),
        get_current_weather,
    ],
)
```

Python

Copied

For step by step instructions see the full [ADK sample with the Interactions API](https://github.com/google/adk-python/tree/main/contributing/samples/interactions_api).

This pattern allows you to keep the control flow and routing logic within the ADK while delegating the heavy lifting of context management and inference state to the Interactions API.

We often describe an inner loop (inside the API) and an outer loop (in your agent code), and this new API gives you more control over both.

## Pattern 2: Using Interactions API Agents as Remote A2A Agents

This is where the interoperability of the **Agent2Agent (A2A)** protocol shines.

If you have an existing ecosystem of A2A clients or agents, you might want them to consult the new **Gemini****Deep Research****Agent**. Historically, integrating a new third-party API would require writing a custom wrapper or adapter.

With the new **`InteractionsApiTransport`**, we have mapped the [A2A protocol](https://a2a-protocol.org/latest/) surface directly onto the Interactions API surface. It “speaks” A2A. This means you can treat an Interactions API endpoint as just another remote A2A agent. Your existing clients don't need to know they are talking to a Google-hosted agent; they just see an `AgentCard` and send messages as usual.

### **How the Bridge Works**

The `InteractionsApiTransport` layer performs a translation to A2A:

*   **A2A****`SendMessage`** → **Interactions****`create`**
*   **A2A****`Task`** → **Interaction ID**
*   **A2A****`TaskStatus`** → **Interaction Status** (e.g., `IN_PROGRESS` maps to `TASK_STATE_WORKING`)

Note: A2A push notifications, A2A extensions, and Interactions API callbacks are not yet supported in this mapping.

### **Code Example: The Transparent Integration**

To use this,simply configure your A2A client factory with the new transport and create a card that points to the model or agent you want to use.

```
from interactions_api_transport import InteractionsApiTransport
from a2a.client import ClientFactory, ClientConfig

# 1. Configure the factory to support Interactions API
client_config = ClientConfig()
client_factory = ClientFactory(client_config)

# Setup the transport (handles API keys and auth transparently)
InteractionsApiTransport.setup(client_factory)

# 2. Create an AgentCard for the Deep Research agent
# This helper method constructs the card with the necessary 'smuggled' config
card = InteractionsApiTransport.make_card(
    url="https://generativelanguage.googleapis.com",
    agent="deep-research-pro-preview-12-2025"
)

# 2a. You can also interact directly with a Gemini model
card = InteractionsApiTransport.make_card(
    url="https://generativelanguage.googleapis.com",
    model="gemini-3-pro-preview",
    request_opts={
        "generation_config": { "thinking_summaries": "auto" }
    }
)

# 3. Create a regular A2A client
client = client_factory.create(card)

# 4. Use it exactly like any other A2A agent
async for event in client.send_message(new_text_message("Research the history of Google TPUs")):
    # The transport converts Interactions API 'Thoughts' and 'Content'
    # into standard A2A Task events.
    print(event)
```

Python

Copied

### **Why this matters**

This approach makes the Interactions API "transparent" to your developer experience. You gain immediate access to powerful new tools like Deep Research without refactoring your multi-agent system.

And the best part, it just works.

*   **No new SDKs to learn:** Your A2A client code stays the same.
*   **Streaming Support:** The transport handles mapping streaming events, so you get real-time updates from the agent.
*   **Configuration Smuggling:** We use A2A extensions to pass specific configurations (like `thinking_summaries`) inside the `AgentCard` without breaking the standard protocol.

## Conclusion

The Gemini Interactions API represents a major step forward in how we model AI communication. Whether you are building custom agents from scratch using any framework like the ADK or connecting existing agents together via A2A, this is a new set of capabilities to start exploring today.

By treating the API as both a superior inference engine _and_ a compliant remote agent, you can rapidly expand the capabilities of your agentic mesh with minimal friction. Expect many more ADK and A2A resources over the next few weeks to help developers adopt this new API.

## Get started today

*   Read the [announcement for Gemini Interactions API](https://blog.google/technology/developers/interactions-api) and [docs](https://ai.google.dev/gemini-api/docs/interactions)
*   Read the [announcement for Gemini Deep Research Agent](https://blog.google/technology/developers/deep-research-agent-gemini-api) and [docs](https://ai.google.dev/gemini-api/docs/deep-research)
*   Check out the [ADK release notes](https://github.com/google/adk-python/blob/main/CHANGELOG.md), [docs](https://google.github.io/adk-docs/) and the [ADK sample with the Interactions API](https://github.com/google/adk-python/tree/main/contributing/samples/interactions_api)
*   Check out the [A2A sample which uses the Interactions API](https://github.com/a2aproject/a2a-samples/tree/interactions-api/samples/python/transports/interactions_api)

[](https://developers.googleblog.com/en/introducing-a2ui-an-open-project-for-agent-driven-interfaces/)
Previous

Next

[](https://developers.googleblog.com/en/real-world-agent-examples-with-gemini-3/)
