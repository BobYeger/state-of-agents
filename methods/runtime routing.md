# Runtime Routing

Runtime selection of models, agents, tools, collaboration modes, and execution paths based on task state, budget, and risk.

Routing matters because fixed agent teams are often wasteful or brittle. A runtime router can choose whether to use a single agent or a team, which model should handle each role, which tools should be exposed, and when to drop or add agents as evidence accumulates.

For long-horizon and multi-agent systems, cost is part of correctness. A design that only succeeds by spawning too many agents, repeating searches, or running unbounded retries may be operationally unusable even if it occasionally reaches the right answer.

## Routing Targets

- Model choice by role, task difficulty, latency, and cost.
- Agent participation: add, remove, or silence agents at runtime.
- Topology choice: star, chain, tree, graph, blackboard, or supervisor-mediated.
- Risk path: route sensitive actions through stricter confirmation or sandboxing.

## Improvement Claim

Routing improves agent systems by making participation conditional. Instead of every agent speaking every round, the runtime chooses who acts, which model is worth using, when to escalate, and when to stop.

## Budget Controls

- Route easy tasks to cheaper models or single-agent paths.
- Cap subagents, tool calls, retry loops, and environment runtime.
- Use agent dropout or runtime supervision to stop redundant work.
- Make cost visible in traces next to accuracy, latency, and safety events.
- Match budget to task value instead of using one fixed agent team for everything.

## Related Sources

- [[sources/AgentDropout|AgentDropout: Dynamic Agent Elimination for Token-Efficient and High-Performance LLM-Based Multi-Agent Collaboration]]
- [[sources/BAMAS|BAMAS: Structuring Budget-Aware Multi-Agent Systems]]
- [[sources/Graph-of-Agents|Graph-of-Agents: A Graph-based Framework for Multi-Agent LLM Collaboration]]
- [[sources/MasRouter|MasRouter: Learning to Route LLMs for Multi-Agent Systems]]
- [[sources/Stop Wasting Your Tokens|Stop Wasting Your Tokens: Towards Efficient Runtime Multi-Agent Systems]]
- [[sources/X-MAS|X-MAS: Towards Building Multi-Agent Systems with Heterogeneous LLMs]]
