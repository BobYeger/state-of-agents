---
title: "Claude apps gateway spend limits"
aliases:
  - "Claude Code gateway spend caps"
source_type: "docs"
kind: "spend-cap-gateway"
status: "verified"
year: 2026
publication_date: "2026-07"
publication_date_basis: "undated_docs_fetch_month"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Anthropic (Claude Code docs)"
venue: "Claude Code docs"
url: "https://code.claude.com/docs/en/claude-apps-gateway-spend-limits"
pdf_url: ""
created: 2026-07-03
updated: 2026-07-03
---

# Claude Apps Gateway Spend Limits

## Summary

- Anthropic's self-hosted gateway enforces per-developer spend caps live on every request; over-cap requests return 429 with `error.type: billing_error` and `x-should-retry: false`. The docs frame this explicitly as the circuit breaker preventing "one runaway agent fleet" from spending the org's entire commitment on a shared upstream credential (Bedrock/Vertex/Foundry).
- Caps are set via an Admin API (`POST /v1/organizations/spend_limits`) with `{scope, amount, period}`. Scope resolution order per period: per-user override, then most-restrictive group cap, then org default, then unlimited. Amounts are USD-cent strings; periods are daily/weekly/monthly, each enforced independently.
- Anti-evasion mechanics: unknown model IDs are priced at a $5/$25 per-million-token fallback tier rather than zero, so unrecognized IDs cannot bypass caps unmetered; client-aborted streams are billed via a conservative ~4-chars-per-token floor estimate, so a capped developer cannot stream-and-abort to spend uncounted.
- The enforcement pre-check is one Postgres query with a 2-second timeout. It fails open by default (a store outage does not become an inference outage), with `enforcement.fail_closed_on_error: true` available to guarantee no unmetered spend instead.
- Spend limits estimate at USD list price and are explicitly "a circuit breaker, not an invoice" — authoritative billing reconciles against the Anthropic Usage & Cost Admin API, Bedrock invocation logs, or Cloud Monitoring.
- Data lifecycle: per-principal spend counters retained 13 months, admin audit trail 365 days, PII (last-seen email/name/groups) 90 days since activity; every cap mutation writes a before/after audit row in the same transaction.

## Connections

- [[operations/cost control]]
- [[operations/agent infrastructure]]
- [[systems/Claude Code]]
- [[sources/Claude Code Manage Costs]]
- [[sources/LiteLLM Proxy Budgets and Spend Tracking]]

## Notes

- Canonical URL: https://code.claude.com/docs/en/claude-apps-gateway-spend-limits
- Docs page is undated and versionless; facts reflect a 2026-07 fetch. Defaults (fail-open, fallback pricing tier) may change between gateway releases.
- Notably specific about failure modes most vendor docs omit: fail-open vs fail-closed tradeoff, abort-billing evasion, and unknown-model fallback pricing.
