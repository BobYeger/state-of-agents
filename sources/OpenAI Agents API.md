---
title: "Introducing the Agents API"
aliases:
  - "OpenAI Agents API"
  - "Managed Codex harness API"
source_type: "article"
kind: "managed-agent-runtime"
status: "verified"
year: 2026
publication_date: "2026-09-10"
publication_date_basis: "visible_announcement_date"
source_updated_date: "2026-09-15"
source_updated_date_basis: "official_documentation_access_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "OpenAI"
venue: "OpenAI / OpenAI API documentation"
url: "https://openai.com/index/introducing-the-agents-api/"
pdf_url: ""
evidence_class: "official-product-announcement-and-runtime-documentation"
metrics_status: "product-contracts-with-uncontrolled-customer-testimonials"
artifacts: []
created: 2026-09-15
updated: 2026-09-15
---

# OpenAI Agents API

## Summary

- Public beta exposing the Codex harness as a managed runtime: OpenAI runs sessions, orchestration, context compaction, and recovery; the application supplies tools and selects OpenAI-hosted, self-hosted, partner, or no execution environment. This is a separate artifact from the embedded [[sources/OpenAI Agents SDK Docs|Agents SDK]] and the lower-level [[sources/OpenAI Responses API Multi-Agent|Responses API multi-agent]] surface.
- The announcement combines automatic compaction, on-demand tool search, programmatic tool calling, and parallel subagents. The design separates ownership of the model/tool loop from ownership of the computer where commands and files operate.
- Sessions accept new input and mid-turn steering, retain state for later continuation, and expose events, saved items, and webhooks. Skills, plugins, MCP connections, files, and code execution supply the application-specific operating context.
- Enabling multi-agent orchestration supplies create, message, wait, and interrupt tools. Workers have independent contexts, but the coordinator and workers share the environment's filesystem; spawning a worker does not create another sandbox. The documented concurrency default is six subagents, excluding the coordinator, as checked September 15.

## Evidence Boundary

The shipped beta API and documented architecture are stronger evidence than the announcement's customer performance testimonials, which lack disclosed controlled comparisons. Product availability does not establish universal gains from the harness or subagents.

Subagents inherit configured MCP tools, credentials, allowed tools, and web-search settings, and can use the shared environment. Custom function tools are currently unsupported in subagents. Shared file mutation therefore needs explicit ownership or additional isolation; separate context windows do not provide separate execution authority.

Coordination events may omit message text and are not a complete conversation transcript. A completed create or wait action does not mean a worker finished its task; inspect saved turns/items and the result. The API retains session state and currently supports US data residency without Zero Data Retention; a self-hosted sandbox does not change that API retention contract. These are dated beta constraints, not promises about later releases.

## Connections

- [[maps/Harness Tracker]]
- [[reports/Harness Engineering Report]]
- [[reports/Multi Agent Report]]
- [[operations/durable sessions]]
- [[operations/sandboxes]]
- [[concepts/subagent context isolation]]
- [[concepts/programmatic tool calling]]
- [[sources/OpenAI Codex Agent Loop]]
- [[sources/OpenAI Responses API Multi-Agent]]
- [[sources/Anthropic Managed Agents]]

## Notes

- [Announcement](https://openai.com/index/introducing-the-agents-api/), September 10, 2026.
- [Overview and retention boundary](https://developers.openai.com/api/docs/guides/agents-api/overview), [multi-agent contracts](https://developers.openai.com/api/docs/guides/agents-api/multi-agent), [architecture](https://developers.openai.com/api/docs/guides/agents-api/architecture). Documentation checked September 15, 2026.
- [Open-source Codex foundation](https://github.com/openai/codex) exposes core harness logic; it does not expose every managed-service component. No source content is archived here.
