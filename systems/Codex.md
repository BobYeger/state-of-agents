# Codex

Codex is OpenAI's software-engineering agent family and CLI/cloud harness for reading code, editing files, running commands, and iterating against tests.

For this vault, Codex is mainly a production-harness case study: the useful object is the loop around the model, including prompts, tool contracts, sandboxing, approvals, context management, telemetry, and failure recovery.

## Design Pattern

- Keep the model in a tight plan-act-observe loop over a real workspace.
- Use shell, file edits, tests, and execution logs as the main observation channel.
- Use worktrees to let multiple Codex threads or automations work against the same repository without disturbing the local checkout.
- Treat approvals, sandbox policy, and network access as part of the agent design rather than peripheral UI.

## Related

- [[concepts/long-horizon agents]]
- [[concepts/tool use]]
- [[concepts/context engineering]]
- [[concepts/issue tracker control plane]]
- [[concepts/agent operating surfaces]]
- [[operations/worktree isolation]]
- [[operations/agent infrastructure]]
- [[operations/sandboxes]]

## Related Sources

- [[sources/OpenAI Codex Agent Loop|Unrolling the Codex agent loop]]
- [[sources/OpenAI Responses API Computer Environment|From model to agent: Equipping the Responses API with a computer environment]]
- [[sources/OpenAI Running Codex Safely]]
- [[sources/OpenAI Unlocking Codex Harness]]
- [[sources/OpenAI Codex App]]
- [[sources/OpenAI Codex App Worktrees]]
- [[sources/OpenAI Symphony]]
- [[sources/OpenAI Agents SDK Tools]]
- [[sources/OpenAI Codex CLI Agents SDK Cookbook]]
