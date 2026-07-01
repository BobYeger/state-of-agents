# Claim - Harnesses Tools And Context Are Core Agent Performance Levers

Agent systems improve when the harness, tools, and context are engineered as carefully as the model prompt. The useful unit is the full loop: prompt assembly, tool contracts, observations, state, approvals, compaction, execution environment, and recovery.

## Supporting Sources

- [[sources/Anthropic Building Effective Agents]] argues for simple composable workflow patterns before unnecessary agent complexity.
- [[sources/Anthropic Writing Tools for Agents]] argues that tool schema, descriptions, errors, affordances, and evals strongly shape agent performance.
- [[sources/Anthropic Effective Context Engineering]] treats context as agent runtime state.
- [[sources/Anthropic Effective Harnesses for Long-Running Agents]] shows how initialization, progress artifacts, and handoffs help across context windows.
- [[sources/OpenAI Codex Agent Loop]] gives a concrete production loop across model calls, tools, context, and compaction.
- [[sources/Claude Code Hooks]] shows how lifecycle hooks make tool calls, compaction, stop conditions, subagents, and worktree events programmable harness surfaces.
- [[sources/Cursor Improving Agent Harness]] treats harness improvement as an ongoing engineering discipline.
- [[sources/OpenClaw Agent Harness Plugins]] gives a clean boundary for the harness as executor of prepared agent turns.
- [[sources/Harness-1]] and [[sources/Agent Memory Characterization]] show that externalized state, memory construction, evidence records, and budget-aware rendering can be first-order performance levers.
- [[sources/Self-Harness]], [[sources/HarnessFix]], and [[sources/Adaptive Auto-Harness]] make the harness itself the object of optimization.
- [[sources/Harness-MU]] shows that governance belongs in deterministic harness controls rather than prompt-only policy.

## Design Implications

- Improve tool contracts before adding agents.
- Make observations, errors, and state legible to the model.
- Keep progress artifacts durable outside the context window.
- Treat approvals, sandboxing, and compaction as part of performance, not only safety.
- Treat traces and failed trajectories as repair data for the harness itself.

## Related

- [[maps/What Makes Agent Systems Better]]
- [[methods/deliberative control]]
- [[methods/hook-based control]]
- [[operations/agent harnesses]]
- [[concepts/tool use]]
- [[concepts/context engineering]]
- [[operations/durable sessions]]
- [[operations/sandboxes]]
