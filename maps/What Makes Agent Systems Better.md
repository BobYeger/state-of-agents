# What Makes Agent Systems Better

This map answers the positive version of [[claims/Claim - Coordination is a cost the task must justify]]: if agent count is not the main lever, what actually improves agent systems?

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
| Hook-based control | Run deterministic gates, validators, context injections, and continuation checks at lifecycle points in the agent loop. | [[methods/hook-based control]], [[sources/Claude Code Hooks]] |
| Harness and context design | Make the loop, state, tools, approvals, compaction, and handoffs explicit. | [[claims/Claim - Harnesses tools and context are core agent performance levers]], [[operations/agent harnesses]] |
| Loop engineering | Design how agents are re-entered over time: wake trigger, recurrence, durable state, verification, retry, escalation, stop policy, and human/product feedback cadence. | [[concepts/loop engineering]], [[sources/Claude Code Scheduled Tasks]], [[sources/Addy Osmani Loop Engineering]], [[sources/Andrew Ng Three Key Loops]], [[sources/Armin Ronacher The Coming Loop]] |
| Code factory control plane | Connect signals, specs, isolated agent work, verification, review, release, monitoring, and learning into an auditable SDLC loop. | [[concepts/code factories]], [[sources/Factory 2.0 Software Factory]], [[sources/Microsoft Agentic Platform Agent Factory]], [[sources/Microsoft Spec-Driven AI-Native Engineering]] |
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
4. [[sources/Claude Code Hooks]]
5. [[sources/Addy Osmani Loop Engineering]]
6. [[sources/Factory 2.0 Software Factory]]
7. [[sources/Andrew Ng Three Key Loops]]
8. [[sources/Armin Ronacher The Coming Loop]]
9. [[sources/Rich Sutton The Bitter Lesson]]
10. [[sources/Anthropic Multi-Agent Research System]]
11. [[sources/Google Scaling Agent Systems]]
12. [[sources/Anthropic Multi-Agent Coordination Patterns]]
13. [[sources/Multi-Agent Teams Hold Experts Back]]
14. [[sources/SAND]]
15. [[sources/VeriMAP]]
16. [[sources/AgentFlow]]
17. [[sources/Multi-Agent Design - MASS]]
18. [[sources/Why Do Multi-Agent LLM Systems Fail]]
19. [[sources/Stop Wasting Your Tokens]]
20. [[sources/OpenRouter Fusion Beats Frontier]]
21. [[sources/Anthropic Writing Tools for Agents]]
22. [[sources/Anthropic Effective Harnesses for Long-Running Agents]]
23. [[sources/SkillsBench]]
24. [[sources/Google ReasoningBank]]
25. [[sources/Anthropic Managed Agents Dreaming Outcomes]]
26. [[sources/Agentic Context Engineering]]
27. [[sources/The Complexity Trap]]
28. [[sources/ACON]]
29. [[sources/ContextBench]]
30. [[sources/MCP-Zero]]
31. [[sources/OpenAI Symphony]]

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
- [[concepts/code factories]]
- [[methods/hook-based control]]
- [[methods/self-improving code loops]]
