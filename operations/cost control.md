# cost control

Cost control covers token efficiency, runtime routing, tool-context compression, budget-aware orchestration, and other production constraints that shape agent system design.

Cost is part of system quality for agents. A design that only works through unbounded subagents, repeated searches, large tool schemas, or uncontrolled retries is not robust even when it occasionally succeeds.

## Improvement Levers

- Route easy work to cheaper paths and reserve expensive models/teams for hard cases.
- Drop redundant agents or messages at runtime.
- Optimize topology and LLM choice under a budget.
- Expose token, latency, retry, and tool-call costs in traces.
- Compress tool/context exposure where code or MCP can reduce prompt overhead.
- Exploit prompt caching deliberately: [[sources/Claude API Prompt Caching]] documents 0.1x-priced cache reads against 1.25-2x writes, which makes append-only context layouts and stable prompt prefixes a cost-architecture decision, not a tuning detail.

## Budget Enforcement

Budgets only control spend when something in the request path can refuse a request. Three enforcement designs are now documented in production detail:

- [[sources/Claude Apps Gateway Spend Limits]]: per-developer caps enforced live at a self-hosted gateway, with the failure modes most docs omit made explicit — fail-open by default so a budget-store outage does not become an inference outage (fail-closed available), unknown model IDs priced at a fallback tier so they cannot bypass metering, and aborted streams billed by a conservative floor so stream-and-abort is not an evasion. The docs frame caps as "a circuit breaker, not an invoice": enforcement estimates, billing reconciles later.
- [[sources/LiteLLM Proxy Budgets and Spend Tracking]]: an eight-level budget hierarchy (global, team, member, user, key, model-on-key, end-customer, agent) with multiple concurrent reset windows per key, plus agent-specific caps — `max_iterations` per session and `max_budget_per_session` — that target runaway loops directly.
- [[sources/Envoy AI Gateway 1.0]]: token-aware rate limiting (request counts do not control LLM usage) with separate attribution for input, output, cached, and reasoning tokens, per provider, model, or client.

The shared design lesson: place budget enforcement at a gateway the agents cannot route around, decide fail-open versus fail-closed explicitly, and expect evasion paths (unknown models, aborted streams, retry storms) rather than discovering them.

## Metering and Attribution

Enforcement needs attribution to be actionable — a tripped org-level cap with no breakdown just converts a cost incident into an availability incident. Attribution has to follow the subagent tree: [[sources/Claude Code Manage Costs]] documents `/usage` splitting recent token spend across skills, subagents, plugins, and individual MCP servers, and notes that on third-party clouds no metrics flow to the vendor, so per-user attribution requires a gateway. [[sources/LiteLLM Proxy Budgets and Spend Tracking]] writes per-request spend rows keyed by user, team, key, and tag; [[sources/OpenTelemetry GenAI Semantic Conventions]] standardizes the token-usage attributes traces need to carry for any of this to be portable across platforms.

Published planning anchors are still scarce; the ones that exist are worth having. [[sources/Claude Code Manage Costs]] reports roughly $13 per developer per active day ($150-250/month) with 90% of users under $30 on any active day, and a ~7x token multiplier for agent teams versus single sessions — the only first-party quantification of multi-agent overhead in a shipping harness. [[sources/Cursor Agent Swarm Model Economics]] adds a vendor-scale role-routing case: approximately $1,339 for an Opus/Composer hybrid versus $10,565 for GPT-5.5 throughout, with similar reported quality but no independent audit. [[sources/Towards a Science of Scaling Agent Systems]] supplies the research-side counterpart: coordination overhead is architecture-dependent, tool-heavy tasks suffer disproportionately from multi-agent overhead, and coordination returns go negative once single-agent accuracy passes roughly 0.45 — cost control and topology choice are the same decision.

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
- [[sources/OpenRouter Fusion Beats Frontier]]
- [[sources/Anthropic Building Effective AI Agents eBook]]
- [[sources/Claude Code Hooks]]
- [[sources/X-MAS]]
- [[sources/Anthropic Code Execution with MCP]]
- [[sources/Cloudflare Code Mode MCP]]
- [[sources/Cloudflare Code Mode MCP API]]
- [[sources/Claude Code Workflows]]
- [[sources/OpenAI Codex Using Goals]]
- [[sources/MCP-Zero]]
- [[sources/ScaleMCP]]
- [[sources/LangChain Delta Channels]]
- [[sources/LangChain Deep Agents v0.6]]
- [[sources/Claude Apps Gateway Spend Limits]]
- [[sources/Claude Code Manage Costs]]
- [[sources/LiteLLM Proxy Budgets and Spend Tracking]]
- [[sources/Envoy AI Gateway 1.0]]
- [[sources/Claude API Prompt Caching]]
- [[sources/Towards a Science of Scaling Agent Systems]]
- [[sources/Claude Sonnet 5]] — $2/$10 per-M introductory pricing positioned explicitly as a cheaper way to run agents, the capability tier for orchestrator-plus-cheap-worker cost models
- [[sources/Cursor Agent Swarm Model Economics]] — vendor-reported planner/worker cost comparison and fleet-scale coordination economics
