# Dynamic Tool Discovery

Dynamic tool discovery lets agents retrieve, request, or search for tools at runtime instead of loading every possible tool definition into context.

The design goal is to preserve context budget and autonomy as tool ecosystems grow. The failure mode is hidden tool mismatch: the agent may choose poorly, retrieve stale capabilities, or miss a necessary tool unless retrieval and tool metadata are evaluated.

## Related Sources

- [[sources/MCP-Zero]]
- [[sources/ScaleMCP]]
- [[sources/Anthropic Advanced Tool Use]]
- [[sources/Anthropic Code Execution with MCP]]
- [[sources/Cloudflare Code Mode MCP API]]
- [[sources/OpenAI Agents SDK Tools]]

## Related

- [[concepts/tool use]]
- [[concepts/agent operating surfaces]]
- [[protocols/MCP]]
- [[operations/cost control]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
