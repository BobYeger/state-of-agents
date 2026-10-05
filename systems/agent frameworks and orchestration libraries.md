# Agent frameworks and orchestration libraries

Frameworks define reusable abstractions for building agent systems: agent graphs, roles, handoffs, tools, memory, workflows, eval hooks, and orchestration patterns.

This node is a routing hub. Individual framework source notes stay in the sources folder until a framework deserves a dedicated synthesis page.

## Choosing What to Own

[[methods/agent runtime selection|Agent runtime selection]] distinguishes an existing agent product, a managed harness API, an embedded harness SDK, an orchestration framework, and a custom loop. These choices can compose: a framework can run a durable business workflow while a managed agent performs one bounded task. Choose using the actual workload, required control points, permission and state ownership, recovery behavior, and total cost per accepted outcome. Packaged harnesses change which runtime code a builder needs to own; they do not eliminate application integration or make a working framework obsolete.

## Current Anchors

- [[sources/LangGraph Docs]]
- [[sources/LangChain Deep Agents Docs]]
- [[sources/LangChain Deep Agents v0.6]]
- [[sources/LangChain Delta Channels]]
- [[sources/LangSmith Context Hub]]
- [[sources/CrewAI Docs]]
- [[sources/OpenAI Agents SDK Docs]]
- [[sources/Microsoft Agent Framework Docs]]
- [[sources/Microsoft Agent Framework Harness Compaction]]
- [[sources/Microsoft Agent Framework Skills Docs]]
- [[sources/AgentScope 1.0]]
- [[sources/Youtu-Agent]]
- [[sources/Qwen-Agent Repository]]
- [[sources/Coze Studio Repository]]
- [[sources/agentUniverse Repository]]

## Related

- [[operations/agent harnesses]]
- [[maps/Harness Tracker]]
- [[operations/agent infrastructure]]
- [[concepts/multi-agent systems]]
- [[protocols/agent protocols]]
- [[sources/AgentScope Docs]]
- [[sources/LoongFlow]]
