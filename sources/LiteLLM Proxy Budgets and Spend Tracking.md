---
title: "LiteLLM Proxy: Budgets, Rate Limits, and Spend Tracking"
aliases:
  - "LiteLLM budgets"
source_type: "docs"
kind: "llm-gateway"
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
  - "BerriAI / LiteLLM"
venue: "LiteLLM docs"
url: "https://docs.litellm.ai/docs/proxy/users"
pdf_url: ""
artifacts:
  - "raw/docs/litellm-proxy-budgets-and-spend-tracking.md"
created: 2026-07-03
updated: 2026-07-05
---

# LiteLLM Proxy Budgets and Spend Tracking

## Summary

- Budget hierarchy spans 8 levels: global proxy, team, team-member, internal user, virtual key, per-model-on-key, end-customer (the request `user` param), and agents — each with `max_budget` in USD plus `budget_duration` reset windows (e.g. 30s/30m/30h/30d).
- Agent-specific caps target runaway loops directly: `max_iterations` caps agent call count per session and `max_budget_per_session` caps dollars per agent session.
- A single key can carry multiple concurrent budget windows at different time scales (e.g. $10/day AND $100/month); exceeding any window fails requests with an auth error naming current spend vs max budget.
- Budget resets are checked every 10 minutes by default (configurable via `proxy_budget_rescheduler_min_time`/`max_time`); budgets require PostgreSQL because SQLite budget decrements race under concurrency.
- Spend tracking (companion page docs.litellm.ai/docs/proxy/cost_tracking) writes per-request rows to `LiteLLM_SpendLogs` attributed by hashed key, user, team, end-user, and tags; query endpoints include `/spend/logs`, `/user/daily/activity`, and `/global/spend/report` grouped by team/customer/key.
- Cost is computed from a built-in pricing DB across 100+ LLMs (prompt tokens x input price + completion tokens x output price + cache tokens), with provider tiers (Vertex PayGo, Bedrock service levels) applied from response metadata.

## Connections

- [[operations/cost control]]
- [[operations/agent infrastructure]]
- [[sources/Claude Apps Gateway Spend Limits]]
- [[sources/Envoy AI Gateway 1.0]]

## Artifacts

- [[raw/docs/litellm-proxy-budgets-and-spend-tracking.md]]

## Notes

- Canonical URL: https://docs.litellm.ai/docs/proxy/users
- Docs pages are undated and continuously updated; facts above reflect a 2026-07 fetch of the users and cost_tracking pages.
- This is the enforcement layer where per-tenant/per-agent budgets actually live in many self-hosted stacks; numbers (reset cadence, level count) can drift with releases.
