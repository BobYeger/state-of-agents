# ACP

ACP, the Agent Client Protocol, standardizes communication between coding agents and code editors or IDE clients.

[[sources/Buzz Repository]] is a concrete open-source ACP composition case: `buzz-acp` turns signed relay events into prompts for arbitrary ACP-compatible agents. The first-party `buzz-agent` is one such implementation and can reach shell/file tools through the separate `buzz-dev-mcp` server; Codex, Claude Code, goose, and other ACP agents need not use it. The harness serializes prompts per channel, batches queued events, and respawns crashed agent subprocesses. Its `--agents N` pool should be read as concurrent ACP capacity under one identity, not an agent-to-agent protocol or team architecture.

In the protocol stack, ACP is the editor-facing counterpart to:

- [[protocols/MCP]] for agent-tool/data access.
- [[protocols/A2A]] for agent-agent interoperability.
- [[protocols/A2UI]] and [[protocols/AG-UI]] for agent-interface integration.
- [[protocols/AP2]] and [[protocols/UCP]] for payments and commerce flows.

## Related Sources

- [[sources/ACP Specification]]
- [[sources/Buzz Repository]]
