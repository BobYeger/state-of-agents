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
- [[sources/Claude Fable 5 Prompting Guide]] documents model-specific harness effects on long turns, progress claims, subagent lifetimes, external memory, and premature stopping.
- [[sources/OpenAI Programmatic Tool Calling]] makes generated code versus direct model calls a selectable tool-orchestration path with different context, evidence, and approval properties.
- [[sources/Think Big Search Small]] shows that role factorization and role-specific model capacity can move accuracy and cost even when the answer generator is held fixed.
- [[sources/OpenAI GPT-5.6 System Card]] shows the safety side of the same thesis: persistence-oriented prompting can amplify scope expansion and unsupported completion claims unless the harness supplies permission and verification boundaries.
- [[sources/Context Engineering MCP CLAUDE-md Skills Hooks Talk]] frames MCP, Skills, Hooks, and Agents as different context and lifecycle mechanisms, and connects existing developer feedback tools to the agent loop.
- [[sources/Factory How Missions Work]] shows the same thesis at system scale through fresh contexts, externalized state, role-specific models, and deterministic milestone validation.
- [[sources/LoopsBench]] shows that model, coding harness, and outer continuation policy jointly determine sustained progress and regression on the same dependency-structured tasks.
- [[sources/Skill-Use]] shows that skill triggering, compliance, boundaries, and even model rankings change with the harness rather than behaving as fixed model capabilities.
- [[sources/Evo-Bench]] holds the policy model fixed during each executable harness-evolution run and finds strongly domain-dependent held-out gains; rerunning evolution with other policy models again improves each model's own baseline.

## Design Implications

- Improve tool contracts before adding agents.
- Make observations, errors, and state legible to the model.
- Keep progress artifacts durable outside the context window.
- Treat approvals, sandboxing, and compaction as part of performance, not only safety.
- Treat traces and failed trajectories as repair data for the harness itself.
- Ground progress and completion claims in tool or artifact evidence, especially on persistent high-effort runs.

## Related

- [[maps/What Makes Agent Systems Better]]
- [[methods/deliberative control]]
- [[methods/hook-based control]]
- [[operations/agent harnesses]]
- [[concepts/tool use]]
- [[concepts/context engineering]]
- [[operations/durable sessions]]
- [[operations/sandboxes]]
