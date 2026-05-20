# cost control

Cost control covers token efficiency, runtime routing, tool-context compression, budget-aware orchestration, and other production constraints that shape agent system design.

Cost is part of system quality for agents. A design that only works through unbounded subagents, repeated searches, large tool schemas, or uncontrolled retries is not robust even when it occasionally succeeds.

## Improvement Levers

- Route easy work to cheaper paths and reserve expensive models/teams for hard cases.
- Drop redundant agents or messages at runtime.
- Optimize topology and LLM choice under a budget.
- Expose token, latency, retry, and tool-call costs in traces.
- Compress tool/context exposure where code or MCP can reduce prompt overhead.

## Related

- [[methods/runtime routing]]
- [[methods/runtime supervision]]
- [[methods/topology optimization]]
- [[operations/agent observability]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]
- [[maps/What Makes Agent Systems Better]]

## Related Sources

- [[sources/Google Scaling Agent Systems]]
- [[sources/BAMAS]]
- [[sources/AgentDropout]]
- [[sources/Stop Wasting Your Tokens]]
- [[sources/MasRouter]]
- [[sources/X-MAS]]
- [[sources/Anthropic Code Execution with MCP]]
- [[sources/Cloudflare Code Mode MCP]]
