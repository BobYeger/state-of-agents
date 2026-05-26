# Agent Operating Surfaces

Agent operating surfaces are the interfaces through which agents discover capabilities and take action: MCP servers, CLIs, SDKs, APIs, config files, docs, schemas, skills, shell tools, and sandboxed code execution.

The important shift is not that CLIs replace MCP or APIs. APIs remain the source of truth for many systems, and MCP remains a useful interoperability layer. The shift is that direct exposure of large API or MCP tool surfaces does not scale well inside model context. Stronger systems give agents progressive, executable surfaces that let them search, inspect, compose, and verify operations before acting.

## Why It Matters

- Large tool lists consume context and encourage shallow one-call-at-a-time behavior.
- CLIs and SDKs give agents compact, discoverable, composable action surfaces.
- Code Mode turns a huge API into a small set of executable discovery and action tools.
- MCP can remain the transport or boundary while the usable surface becomes code, CLI, or dynamic search.
- Consistent output, flags, schemas, local/remote semantics, and error messages become part of agent reliability.

## Design Tension

The best operating surface depends on the execution environment:

- MCP works when tools are few, stable, and well described.
- Dynamic tool search works when the candidate set is known but too large to load upfront.
- Code Mode works when an agent can safely run code against typed APIs or schemas.
- CLIs work when the agent has shell access and the commands are consistent, documented, and machine-readable.
- Hosted or sandboxed execution is needed when code/CLI power would otherwise expand the attack surface.

## Related Sources

- [[sources/Anthropic Code Execution with MCP]]
- [[sources/Cloudflare Code Mode MCP]]
- [[sources/Cloudflare Code Mode MCP API]]
- [[sources/Cloudflare CLI for All Cloudflare]]
- [[sources/Anthropic Advanced Tool Use]]
- [[sources/OpenAI Agents SDK Tools]]
- [[sources/OpenAI Codex CLI Agents SDK Cookbook]]
- [[sources/OpenAI Codex Agent Loop]]
- [[sources/MCP-Zero]]
- [[sources/ScaleMCP]]

## Related

- [[protocols/MCP]]
- [[concepts/programmatic tool calling]]
- [[concepts/dynamic tool discovery]]
- [[concepts/tool-use contracts]]
- [[operations/agent harnesses]]
- [[operations/cost control]]
- [[operations/sandboxes]]
