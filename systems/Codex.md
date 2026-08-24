# Codex

Codex is OpenAI's software-engineering agent family and CLI/cloud harness for reading code, editing files, running commands, and iterating against tests.

For this vault, Codex is mainly a production-harness case study: the useful object is the loop around the model, including prompts, tool contracts, sandboxing, approvals, context management, telemetry, and failure recovery.

## Design Pattern

- Keep the model in a tight plan-act-observe loop over a real workspace.
- Use shell, file edits, tests, and execution logs as the main observation channel.
- Use worktrees to let multiple Codex threads or automations work against the same repository without disturbing the local checkout.
- Treat approvals, sandbox policy, and network access as part of the agent design rather than peripheral UI.
- Treat goals, automations, and repeated thread/worktree runs as loop-engineering surfaces around the inner Codex agent loop.
- Use the App Server thread/turn control plane, or desktop bindings over it, when a coordinator needs to create, steer, inspect, and organize durable worker threads.
- Use `codex queue` when another process needs to persist a future user turn for an existing session. Do not treat the queue as an identified peer channel: its v0.149 record has no sender identity or reply address.
- Keep released CLI queueing, the experimental App Server queue API, and model-callable desktop/TUI task tools distinct; their availability and delivery contracts differ.

## Related

- [[concepts/long-horizon agents]]
- [[concepts/tool use]]
- [[concepts/context engineering]]
- [[concepts/issue tracker control plane]]
- [[concepts/agent operating surfaces]]
- [[concepts/loop engineering]]
- [[concepts/cross-session agent communication]]
- [[operations/worktree isolation]]
- [[operations/agent infrastructure]]
- [[operations/sandboxes]]
- [[methods/codex thread orchestration]]

## Related Sources

- [[sources/OpenAI Codex Agent Loop|Unrolling the Codex agent loop]]
- [[sources/OpenAI Codex Using Goals]]
- [[sources/OpenAI Responses API Computer Environment|From model to agent: Equipping the Responses API with a computer environment]]
- [[sources/OpenAI Running Codex Safely]]
- [[sources/OpenAI Unlocking Codex Harness]]
- [[sources/OpenAI Codex App Server Docs]]
- [[sources/OpenAI Codex Session Queueing]]
- [[sources/OpenAI Codex App]]
- [[sources/OpenAI Codex App Worktrees]]
- [[sources/OpenAI Symphony]]
- [[sources/OpenAI Agents SDK Tools]]
- [[sources/OpenAI Codex CLI Agents SDK Cookbook]]
- [[sources/SkillOpt]]
- [[sources/OpenAI GPT-5.5]] — agent-first frontier model serving a 400K-token window in Codex at included pricing, with vendor-reported ~40% token-efficiency gains on Codex tasks
