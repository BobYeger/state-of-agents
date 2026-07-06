# Topology Optimization

Topology optimization searches or adapts the communication structure among agents, such as star, chain, tree, graph, blackboard, or dynamic routing layouts.

## Improvement Claim

Topology is a performance lever, not decoration. Better agent systems search or choose communication structure based on task shape, role dependencies, cost, and verification needs.

## Quantitative Evidence

Topology selection is now backed by measured deltas rather than intuition:

- [[sources/Towards a Science of Scaling Agent Systems]]: across 260 configurations, the same task swings from +80.8% (decomposable reasoning under centralized coordination) to -70.0% (sequential planning under independent agents) against the single-agent baseline; independent topologies amplify trace errors 17.2x versus 4.4x under centralized control; a predictor built from coordination metrics selects the best architecture for 87% of held-out configurations.
- [[sources/MacNet]]: on DAGs scaling past 1,000 agents, irregular topologies outperform regular ones, and performance follows a logistic "collaborative scaling law" in agent count — structure choice persists as a lever after the marginal agent has decayed to nothing.
- [[sources/LLM Multi-Agent Blackboard System]]: replacing coordinator-assigned subtasks with volunteer pickup from a shared blackboard yields 13-57% relative end-to-end improvement on data-science benchmarks, because the hub no longer needs a capability model of every spoke.
- [[sources/Multi-Agent Design - MASS]]: joint optimization of prompts and topology beats optimizing either alone; prompt effects are large enough that topology comparisons made with untuned prompts mislead.

## Selection Heuristics

| Task signal | Favored structure | Basis |
|---|---|---|
| Strong single-agent baseline (above ~0.45 accuracy) | No topology at all — stay single-agent | Capability-saturation effect in [[sources/Towards a Science of Scaling Agent Systems]] |
| Decomposable work, error containment matters | Centralized hub (orchestrator-worker) | 4.4x vs 17.2x error amplification |
| Sequential dependencies | Chain or single thread; independent parallelism is the worst measured choice | The -70.0% cell is independent agents on sequential planning |
| Hub cannot know every worker's expertise | Blackboard with volunteer pickup | [[sources/LLM Multi-Agent Blackboard System]] win margins |
| Heterogeneous expertise, hub bottleneck | Graph or decentralized routing | [[sources/AgentNet]], [[sources/Graph-of-Agents]] |
| Tight budget | Prune edges and agents before adding any | [[sources/BAMAS]], and topology search only pays if it beats the tuned-prompt baseline per [[sources/Multi-Agent Design - MASS]] |

The consistent negative result: fully-connected "everyone talks every round" layouts are dominated — they maximize both token cost and the error-propagation surface. When the topology question is "same task, many samples" rather than "divided task, many roles," it belongs to [[methods/debate and aggregation]] instead.

## Related

- [[concepts/multi-agent systems]]
- [[maps/What Makes Agent Systems Better]]
- [[claims/Claim - Agent systems improve when structure matches the task]]
- [[methods/multi-agent orchestration]]
- [[methods/debate and aggregation]]
- [[methods/runtime routing]]

## Related Sources

- [[sources/Towards a Science of Scaling Agent Systems|Towards a Science of Scaling Agent Systems]]
- [[sources/MacNet|Scaling Large Language Model-based Multi-Agent Collaboration (MacNet)]]
- [[sources/LLM Multi-Agent Blackboard System|LLM-based Multi-Agent Blackboard System for Information Discovery in Data Science]]
- [[sources/AgentNet|AgentNet: Decentralized Evolutionary Coordination for LLM-based Multi-Agent Systems]]
- [[sources/BAMAS|BAMAS: Structuring Budget-Aware Multi-Agent Systems]]
- [[sources/Multi-Agent Design - MASS|Multi-Agent Design: Optimizing Agents with Better Prompts and Topologies]]
- [[sources/MultiAgentBench|MultiAgentBench: Evaluating the Collaboration and Competition of LLM agents]]
- [[sources/Graph-of-Agents|Graph-of-Agents: A Graph-based Framework for Multi-Agent LLM Collaboration]]
- [[sources/OpenRouter Fusion Beats Frontier]]
