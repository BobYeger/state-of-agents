# Claim - Harnesses Tools And Context Are Core Agent Performance Levers

Agent systems improve when the harness, tools, and context are engineered as carefully as the model prompt. The useful unit is the full loop: prompt assembly, tool contracts, observations, state, approvals, compaction, execution environment, and recovery.

## Supporting Sources

- [[sources/Anthropic Building Effective Agents]] argues for simple composable workflow patterns before unnecessary agent complexity.
- [[sources/Anthropic Writing Tools for Agents]] argues that tool schema, descriptions, errors, affordances, and evals strongly shape agent performance.
- [[sources/Anthropic Effective Context Engineering]] treats context as agent runtime state.
- [[sources/Anthropic Effective Harnesses for Long-Running Agents]] shows how initialization, progress artifacts, and handoffs help across context windows.
- [[sources/OpenAI Codex Agent Loop]] gives a concrete production loop across model calls, tools, context, and compaction.
- [[sources/Cursor Improving Agent Harness]] treats harness improvement as an ongoing engineering discipline.
- [[sources/OpenClaw Agent Harness Plugins]] gives a clean boundary for the harness as executor of prepared agent turns.
- [[sources/Plan-Then-Execute]] and [[sources/Web Agents Plan-Then-Execute]] show why the loop boundary between planning and execution affects trust, security, and control.

## Design Implications

- Improve tool contracts before adding agents.
- Make observations, errors, and state legible to the model.
- Keep progress artifacts durable outside the context window.
- Treat approvals, sandboxing, and compaction as part of performance, not only safety.

## Related

- [[maps/What Makes Agent Systems Better]]
- [[methods/deliberative control]]
- [[operations/agent harnesses]]
- [[concepts/tool use]]
- [[concepts/context engineering]]
- [[operations/durable sessions]]
- [[operations/sandboxes]]
