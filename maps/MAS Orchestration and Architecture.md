# MAS Orchestration and Architecture

This map collects the major sources for designing multi-agent systems as architectures, not just as collections of agents.

The organizing question is: what coordination structure should exist for a given task, and what control plane makes that structure reliable, observable, and cost-aware?

## Architecture Families

| Pattern | What It Optimizes | Anchor Sources |
|---|---|---|
| Architecture maps and scaling rules | When multi-agent coordination helps, when it saturates, and how orchestration becomes a control plane. | [[sources/Google Scaling Agent Systems]], [[sources/The Orchestration of Multi-Agent Systems]], [[sources/Multi-Agent Collaboration Mechanisms - A Survey of LLMs]], [[sources/AI Agent Systems - Architectures Applications and Evaluation]] |
| Orchestrator-worker systems | A lead agent decomposes, delegates, tracks progress, and replans across specialist agents. | [[sources/Anthropic Multi-Agent Research System]], [[sources/Magentic-One]], [[sources/MiniMax Agent Team]], [[sources/Cloudflare Project Think]] |
| Human-in-the-loop orchestration | Humans become part of planning, approval, co-tasking, interruption, and verification loops. | [[sources/Magentic-UI]], [[sources/Google ADK Multi-Agent Patterns]], [[concepts/human-in-the-loop agents]] |
| Workflow and topology optimization | Prompts, roles, workflows, communication graph, and tool placement are searched or learned. | [[sources/ADAS]], [[sources/AFlow]], [[sources/Multi-Agent Design - MASS]], [[sources/MAPRO]], [[sources/MAS2]] |
| Routing and runtime supervision | Select which agents or models act, remove redundant communication, and intervene only when risk or uncertainty warrants it. | [[sources/MasRouter]], [[sources/AgentDropout]], [[sources/Stop Wasting Your Tokens]], [[methods/runtime routing]], [[methods/runtime supervision]] |
| Planner-executor-verifier | Separate planning, execution, verification, and repair so handoffs and outputs become checkable. | [[sources/VeriMAP]], [[sources/AgentFlow]], [[sources/OWL]], [[methods/deliberative control]] |
| Failure analysis and architecture evaluation | Treat architecture as an experimental variable with failure modes, latency, cost, and coordination quality. | [[sources/Why Do Multi-Agent LLM Systems Fail]], [[sources/MultiAgentBench]], [[sources/Understanding Multi-Agent LLM Frameworks]], [[benchmarks/multi-agent benchmarks]] |
| Decentralized, graph, and swarm systems | Reduce centralized bottlenecks through dynamic DAGs, graph message passing, swarms, and selective agent activation. | [[sources/AgentNet]], [[sources/Graph-of-Agents]], [[sources/Kimi Agent Swarm]], [[sources/AgentScope 1.0]] |
| Framework orchestration patterns | Builder-facing patterns such as supervisor graphs, swarms, hierarchical crews, pipelines, and flows. | Google ADK multi-agent patterns, [[sources/Microsoft Agent Framework Docs]], [[sources/LangGraph Docs]], [[sources/CrewAI Docs]] |
| Protocol-mediated orchestration | Agent collectives coordinate through tool, peer, UI, and commerce protocols rather than only private framework calls. | [[protocols/MCP]], [[protocols/A2A]], [[sources/Google Developer Guide to AI Agent Protocols]], The Orchestration of Multi-Agent Systems |

## Design Heuristics

- Start with task structure. Parallelizable, broad, context-heavy tasks justify different orchestration than sequential reasoning tasks.
- Add a central orchestrator when task decomposition, progress tracking, and recovery matter more than decentralization.
- Add graph or swarm structures when agent selection, heterogeneous expertise, or bottleneck avoidance is the main problem.
- Use planner-executor-verifier patterns when handoffs need explicit contracts, structured outputs, tests, or safety checks.
- Prefer runtime routing, dropout, and supervision over fixed "everyone talks every round" designs.
- Treat A2A, MCP, AG-UI/A2UI, ACP, and AP2 as architecture surfaces, not only protocol specs.

## Related

- [[maps/Multi-Agent Systems Map]]
- [[maps/What Makes Agent Systems Better]]
- [[methods/multi-agent orchestration]]
- [[methods/topology optimization]]
- Runtime routing
- Runtime supervision
- Deliberative control
