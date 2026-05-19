# Codex

Codex is OpenAI's software-engineering agent family and CLI/cloud harness for reading code, editing files, running commands, and iterating against tests.

For this vault, Codex is mainly a production-harness case study: the useful object is the loop around the model, including prompts, tool contracts, sandboxing, approvals, context management, telemetry, and failure recovery.

## Design Pattern

- Keep the model in a tight plan-act-observe loop over a real workspace.
- Use shell, file edits, tests, and execution logs as the main observation channel.
- Treat approvals, sandbox policy, and network access as part of the agent design rather than peripheral UI.

## Related

- [[concepts/long-horizon agents]]
- [[concepts/tool use]]
- [[concepts/context engineering]]
- [[operations/agent infrastructure]]
- [[operations/sandboxes]]

## Related Sources

- [[sources/OpenAI Codex Agent Loop|Unrolling the Codex agent loop]]
- [[sources/OpenAI Responses API WebSockets|Speeding up agentic workflows with WebSockets in the Responses API]]
- [[sources/OpenAI Agents SDK Skills Capability|OpenAI Agents SDK Skills capability]]
