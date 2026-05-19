# What Makes Agent Systems Better

This map answers the positive version of [[claims/Claim - More agents are not automatically better]]: if agent count is not the main lever, what actually improves agent systems?

## Core Answer

Agent systems get better when structure, runtime control, tools, context, memory, and feedback loops are designed around the task. The recurring pattern across the vault is not "add agents"; it is "shape the work so agents can act, observe, verify, and improve."

## Improvement Levers

| Lever | What improves | Main notes |
|---|---|---|
| Task-fit and decomposition | Use multiple agents only when the task has breadth, separable context, or useful specialization. | [[claims/Claim - Agent systems improve when structure matches the task]] |
| Deliberative control | Separate planning, execution, observation, verification, and revision when the task benefits from explicit control flow. | [[methods/deliberative control]], [[methods/runtime supervision]] |
| Prompt, role, and topology search | Treat prompts, roles, and communication graph as design variables. | [[methods/topology optimization]], [[methods/agentic workflow search]] |
| Scaling-compatible design | Prefer structures that improve with more compute, search, learning, traces, feedback, and experience. | [[concepts/scaling with computation]], [[methods/agentic workflow search]] |
| Runtime routing and pruning | Route by task state, role, model cost, uncertainty, and observed redundancy. | [[methods/runtime routing]] |
| Supervision and verification | Add monitors, critics, evaluators, stopping criteria, and repair loops. | [[claims/Claim - Runtime control and verification improve agent reliability]], [[methods/runtime supervision]] |
| Harness and context design | Make the loop, state, tools, approvals, compaction, and handoffs explicit. | [[claims/Claim - Harnesses tools and context are core agent performance levers]], [[operations/agent harnesses]] |
| Tool contracts | Improve schemas, errors, affordances, permissions, and observability. | [[concepts/tool use]], [[concepts/tool-use contracts]] |
| Memory and skills | Reuse successful procedures, strategies, learned rules, and skill packages. | [[claims/Claim - Agent memory and skills create compounding improvement loops]], [[maps/Agent Skills Map]] |
| Evals and observability | Measure multi-turn behavior, tool use, cost, failure modes, and interventions. | [[operations/agent evals]], [[operations/agent observability]] |
| Human-in-the-loop control | Route ambiguous, risky, or high-authority actions to humans at the right time. | [[concepts/human-in-the-loop agents]], [[operations/permissions]] |

## First Reading Path

1. [[sources/Anthropic Building Effective Agents]]
2. [[sources/Rich Sutton The Bitter Lesson]]
3. [[sources/Anthropic Multi-Agent Research System]]
4. [[sources/Google Scaling Agent Systems]]
5. [[sources/SAND]]
6. [[sources/VeriMAP]]
7. [[sources/AgentFlow]]
8. [[sources/Multi-Agent Design - MASS]]
9. [[sources/Why Do Multi-Agent LLM Systems Fail]]
10. [[sources/Stop Wasting Your Tokens]]
11. [[sources/Anthropic Writing Tools for Agents]]
12. [[sources/Anthropic Effective Harnesses for Long-Running Agents]]
13. [[sources/SkillsBench]]
14. [[sources/Google ReasoningBank]]

## Related Maps

- [[maps/Claims Map]]
- [[maps/Multi-Agent Systems Map]]
- [[maps/Production Infrastructure Map]]
- [[maps/Agent Skills Map]]
- [[maps/Evaluation Map]]
