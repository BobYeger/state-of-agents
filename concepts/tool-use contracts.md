# tool-use contracts

Tool-use contracts are the schemas, affordances, error surfaces, permissions, and interaction conventions that make tools usable by nondeterministic agents.

Weak tool contracts force the model to infer hidden semantics. Strong contracts tell the agent what a tool can do, how failure is represented, what authority the call carries, and what evidence should be returned for later verification.

## Improvement Levers

- Make schemas explicit with examples, constraints, and defaults.
- Design errors so agents can recover instead of hallucinating success.
- Separate read, write, delete, spend, and send authority.
- Return observations that support verification, not only terse success messages.
- Instrument tool calls with logs, approvals, and traces.

## Related

- [[concepts/tool use]]
- [[operations/permissions]]
- [[operations/agent observability]]
- [[operations/sandboxes]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
- [[maps/What Makes Agent Systems Better]]

## Related Sources

- [[sources/Anthropic Writing Tools for Agents]]
- [[sources/Anthropic Advanced Tool Use]]
- [[sources/Anthropic Code Execution with MCP]]
- [[sources/OpenAI Codex Agent Loop]]
- [[sources/OpenAI Responses API Computer Environment]]
- [[sources/Cloudflare Code Mode MCP]]
- [[sources/Cloudflare Code Mode MCP API]]
- [[sources/Cloudflare CLI for All Cloudflare]]
- [[sources/OpenAI Agents SDK Tools]]
