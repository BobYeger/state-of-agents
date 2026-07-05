---
title: "Claude Code: Manage costs effectively"
aliases:
  - "Claude Code cost docs"
source_type: "docs"
kind: "cost-governance"
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
url: "https://code.claude.com/docs/en/costs"
pdf_url: ""
artifacts:
  - "raw/docs/claude-code-manage-costs.md"
created: 2026-07-03
updated: 2026-07-05
---

# Claude Code Manage Costs

## Summary

- First-party fleet cost datapoints from enterprise deployments: average ~$13 per developer per active day, $150-250 per developer per month, with 90% of users staying under $30 on any active day.
- Agent teams use approximately 7x more tokens than standard sessions when teammates run in plan mode, because each teammate is a separate Claude instance with its own context window. Stated mitigations: Sonnet for teammates, small teams, focused spawn prompts, shutting down idle teammates.
- Per-user TPM/RPM provisioning scales down with org size — 200k-300k TPM/user at 1-5 users down to 10k-15k TPM/user at 500+ users — because concurrency drops in larger orgs; limits apply org-wide, not per user.
- `/usage` attributes recent token usage across the subagent tree to skills, subagents, plugins, and individual MCP servers as percentages of total, with a 24h/7d toggle.
- Governance mechanisms: workspace spend limits in the Claude Console on the auto-created "Claude Code" workspace, workspace rate limits to protect production workloads, and `/usage-credits` monthly limits on Pro/Max. On Bedrock/Vertex/Foundry no metrics flow to Anthropic, so per-user attribution requires the self-hosted gateway or another LLM gateway.
- Background token usage (resume summarization, status commands) typically costs under $0.04 per session even when idle.

## Connections

- [[operations/cost control]]
- [[systems/Claude Code]]
- [[concepts/agent teams]]
- [[sources/Claude Code Agent Teams]]
- [[sources/Claude Apps Gateway Spend Limits]]

## Artifacts

- [[raw/docs/claude-code-manage-costs.md]]

## Notes

- Canonical URL: https://code.claude.com/docs/en/costs
- Docs page is undated and continuously updated; figures reflect a 2026-07 fetch and are self-reported vendor aggregates, not independently audited.
- The 7x agent-team token multiplier is the only published first-party quantification of multi-agent cost overhead in a shipping harness; useful as a planning anchor for fleet budgeting.
