# MAS Orchestration and Architecture

This map collects the major sources for designing multi-agent systems as architectures, not just as collections of agents.

The organizing question is: what coordination structure should exist for a given task, and what control plane makes that structure reliable, observable, and cost-aware?

## Architecture Families

| Pattern | What It Optimizes | Anchor Sources |
|---|---|---|
| Architecture maps and scaling rules | When multi-agent coordination helps, when it saturates, and how orchestration becomes a control plane. | [[sources/Google Scaling Agent Systems]], [[sources/The Orchestration of Multi-Agent Systems]] |
| Orchestrator-worker systems | A lead agent decomposes, delegates, tracks progress, and replans across specialist agents. | [[sources/Anthropic Multi-Agent Research System]], [[sources/Magentic-One]] |
| Agent teams and workforces | Named teammates have roles, owned scopes, persistent context, team-state, verification, and observability. | [[maps/Agent Teams and Workforces Map]], [[sources/Claude Code Agent Teams]], [[sources/Anthropic Multi-Agent Coordination Patterns]] |
| Human-in-the-loop orchestration | Humans become part of planning, approval, co-tasking, interruption, and verification loops. | [[sources/Magentic-UI]], [[concepts/human-in-the-loop agents]] |
| Workflow and topology optimization | Prompts, roles, workflows, communication graph, and tool placement are searched or learned. | [[sources/AFlow]], [[sources/Multi-Agent Design - MASS]], [[methods/topology optimization]] |
| Routing and runtime supervision | Select which agents or models act, remove redundant communication, and intervene only when risk or uncertainty warrants it. | [[sources/MasRouter]], [[sources/Stop Wasting Your Tokens]], [[methods/runtime routing]], [[methods/runtime supervision]] |
| Planner-executor-verifier | Separate planning, execution, verification, and repair so handoffs and outputs become checkable. | [[sources/VeriMAP]], [[sources/AgentFlow]], [[methods/deliberative control]] |
| Failure analysis and architecture evaluation | Treat architecture as an experimental variable with failure modes, latency, cost, and coordination quality. | [[sources/Why Do Multi-Agent LLM Systems Fail]], [[sources/Understanding Multi-Agent LLM Frameworks]], [[benchmarks/multi-agent benchmarks]] |
| Decentralized, graph, and swarm systems | Reduce centralized bottlenecks through dynamic DAGs, graph message passing, swarms, and selective agent activation. | [[sources/AgentNet]], [[sources/Graph-of-Agents]] |
| Framework orchestration patterns | Builder-facing patterns such as supervisor graphs, swarms, hierarchical crews, pipelines, and flows. | [[sources/Google ADK Multi-Agent Patterns]], [[sources/Microsoft Agent Framework Docs]], [[systems/agent frameworks and orchestration libraries]] |
| Protocol-mediated orchestration | Agent collectives coordinate through tool, peer, UI, and commerce protocols rather than only private framework calls. | [[protocols/MCP]], [[protocols/A2A]], [[sources/Google Developer Guide to AI Agent Protocols]] |

## Design Heuristics

- Start with task structure. Parallelizable, broad, context-heavy tasks justify different orchestration than sequential reasoning tasks.
- Add a central orchestrator when task decomposition, progress tracking, and recovery matter more than decentralization.
- Use agent teams only when teammate context, clear ownership, shared state, and team-level verification justify the coordination overhead.
- Add graph or swarm structures when agent selection, heterogeneous expertise, or bottleneck avoidance is the main problem.
- Use planner-executor-verifier patterns when handoffs need explicit contracts, structured outputs, tests, or safety checks.
- Prefer runtime routing, dropout, and supervision over fixed "everyone talks every round" designs.
- Treat A2A, MCP, AG-UI/A2UI, ACP, and AP2 as architecture surfaces, not only protocol specs.

## Related

- [[maps/Multi-Agent Systems Map]]
- [[maps/Agent Teams and Workforces Map]]
- [[maps/What Makes Agent Systems Better]]
- [[methods/multi-agent orchestration]]
- [[operations/agent infrastructure]]
