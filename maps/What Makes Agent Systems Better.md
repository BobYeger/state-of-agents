# What Makes Agent Systems Better

This map answers the positive version of [[claims/Claim - More agents are not automatically better]]: if agent count is not the main lever, what actually improves agent systems?

## Core Answer

Agent systems get better when structure, runtime control, tools, context, memory, and feedback loops are designed around the task. The recurring pattern across the vault is not "add agents"; it is "shape the work so agents can act, observe, verify, and improve."

## Improvement Levers

| Lever | What improves | Main notes |
|---|---|---|
| Task-fit and decomposition | Use multiple agents only when the task has breadth, dependencies, separable context, measurable quality gaps, or useful specialization. | [[claims/Claim - Agent systems improve when structure matches the task]], [[sources/Anthropic Building Effective AI Agents eBook]], [[sources/Claude Common Workflow Patterns for AI Agents]] |
| Team organization | Make roles, ownership, shared state, communication, verification, and observability explicit before scaling team size. | [[claims/Claim - Agent teams need explicit organization]], [[maps/Agent Teams and Workforces Map]] |
| Deliberative control | Separate planning, execution, observation, verification, and revision when the task benefits from explicit control flow. | [[methods/deliberative control]] |
| Prompt, role, and topology search | Treat prompts, roles, and communication graph as design variables. | [[methods/topology optimization]], [[methods/agentic workflow search]] |
| Scaling-compatible design | Prefer structures that improve with more compute, search, learning, traces, feedback, and experience. | [[concepts/scaling with computation]] |
| Runtime routing and pruning | Route by task state, role, model cost, uncertainty, and observed redundancy. | [[methods/runtime routing]], [[sources/OpenRouter Fusion Beats Frontier]] |
| Supervision and verification | Add monitors, critics, evaluators, stopping criteria, and repair loops. | [[claims/Claim - Runtime control and verification improve agent reliability]], [[methods/runtime supervision]] |
| Harness and context design | Make the loop, state, tools, approvals, compaction, and handoffs explicit. | [[claims/Claim - Harnesses tools and context are core agent performance levers]], [[operations/agent harnesses]] |
| Loop engineering | Design how agents are re-entered over time: wake trigger, recurrence, durable state, verification, retry, escalation, and stop policy. | [[concepts/loop engineering]], [[sources/Claude Code Scheduled Tasks]], [[sources/Addy Osmani Loop Engineering]] |
| Self-improving code loops | Mutate executable artifacts only when evaluator evidence improves, with rollback and sandboxing. | [[methods/self-improving code loops]], [[sources/Darwin Godel Machine]], [[sources/Meta-Harness]], [[sources/SkillOpt]], [[sources/AlphaEvolve]] |
| Context management | Choose between compaction, masking, clearing, retrieval, memory offload, handoff, and task-aware pruning. | [[claims/Claim - Context management is an agent architecture choice]], [[maps/Context Management Map]] |
| Fresh-context coding loops | Use files, tests, commits, and task ledgers as durable state across repeated agent runs. | [[methods/ralph loop]] |
| Tool contracts | Improve schemas, errors, affordances, permissions, and observability. | [[concepts/tool use]], [[concepts/tool-use contracts]] |
| Memory and skills | Reuse successful procedures, strategies, learned rules, and skill packages. | [[claims/Claim - Agent memory and skills create compounding improvement loops]], [[maps/Agent Skills Map]], [[sources/SkillOpt]], [[concepts/reasoning memory]] |
| Operating substrate | Add durable state, versioned context, dynamic tools, rubric graders, subagents, and event streams around the model. | [[maps/Recent Agent Operating Concepts]] |
| Evals and observability | Measure multi-turn behavior, tool use, cost, failure modes, and interventions. | [[operations/agent evals]], [[operations/agent observability]] |
| Human-in-the-loop control | Route ambiguous, risky, or high-authority actions to humans at the right time. | [[concepts/human-in-the-loop agents]], [[operations/permissions]] |

## First Reading Path

1. [[sources/Anthropic Building Effective Agents]]
2. [[sources/Anthropic Building Effective AI Agents eBook]]
3. [[sources/Claude Common Workflow Patterns for AI Agents]]
4. [[sources/Rich Sutton The Bitter Lesson]]
5. [[sources/Anthropic Multi-Agent Research System]]
6. [[sources/Google Scaling Agent Systems]]
7. [[sources/Anthropic Multi-Agent Coordination Patterns]]
8. [[sources/Multi-Agent Teams Hold Experts Back]]
9. [[sources/SAND]]
10. [[sources/VeriMAP]]
11. [[sources/AgentFlow]]
12. [[sources/Multi-Agent Design - MASS]]
13. [[sources/Why Do Multi-Agent LLM Systems Fail]]
14. [[sources/Stop Wasting Your Tokens]]
15. [[sources/OpenRouter Fusion Beats Frontier]]
16. [[sources/Anthropic Writing Tools for Agents]]
17. [[sources/Anthropic Effective Harnesses for Long-Running Agents]]
18. [[sources/SkillsBench]]
19. [[sources/Google ReasoningBank]]
20. [[sources/Anthropic Managed Agents Dreaming Outcomes]]
21. [[sources/Agentic Context Engineering]]
22. [[sources/The Complexity Trap]]
23. [[sources/ACON]]
24. [[sources/ContextBench]]
25. [[sources/MCP-Zero]]
26. [[sources/OpenAI Symphony]]

## Related Maps

- [[maps/Claims Map]]
- [[maps/Multi-Agent Systems Map]]
- [[maps/MAS Orchestration and Architecture]]
- [[maps/Agent Teams and Workforces Map]]
- [[maps/Production Infrastructure Map]]
- [[maps/Evaluation Map]]
- [[maps/Context Management Map]]
- [[maps/Recent Agent Operating Concepts]]
- [[concepts/loop engineering]]
- [[methods/self-improving code loops]]
