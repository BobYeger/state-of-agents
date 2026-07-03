---
title: "Compaction (Claude Platform Docs) — server-side context compaction API"
aliases:
  - "Claude API compaction"
  - "compact_20260112"
source_type: "docs"
kind: "context-compaction"
status: "verified"
year: 2026
publication_date: "2026-01-12"
publication_date_basis: "api_version_string_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Anthropic"
venue: "Claude Platform Docs"
url: "https://platform.claude.com/docs/en/build-with-claude/compaction"
pdf_url: ""
created: 2026-07-03
updated: 2026-07-03
---

# Claude API Compaction

## Summary

- Server-side compaction (edit type `compact_20260112`, beta header `compact-2026-01-12`) summarizes older conversation content into a compaction block when input tokens hit a configurable trigger — default 150,000, minimum 50,000. Compaction thereby moves from harness-side code into the API itself.
- On subsequent requests the API automatically drops all content blocks before the compaction block; `pause_after_compaction: true` returns stop_reason `compaction` so the harness can adjust messages before continuing.
- The `instructions` parameter fully replaces the default summarization prompt — the API-native version of compact-with-focus.
- Billing subtlety: compaction adds a sampling iteration reported in `usage.iterations[]`; top-level `input_tokens`/`output_tokens` do not include the compaction iteration.
- Documented cache interaction: place a `cache_control` breakpoint on the compaction block and keep the system prompt cached separately to maximize hits across compaction events.
- Supported on Fable 5, Mythos 5, Opus 4.6-4.8, and Sonnet 4.6/5; `count_tokens` applies existing compaction blocks and reports `context_management.original_input_tokens`.

## Claims

- [[claims/Claim - Context management is an agent architecture choice]]

## Connections

- [[concepts/context compaction]]
- [[concepts/handoff over compaction]]
- [[operations/agent harnesses]]
- [[operations/cost control]]
- [[sources/OpenAI Agents SDK Compaction Sessions]]
- [[sources/Google ADK Context Compression]]
- [[sources/Claude API Prompt Caching]]

## Notes

- Canonical URL: https://platform.claude.com/docs/en/build-with-claude/compaction
- Beta feature as documented; the publication date is inferred from the `compact_20260112` version string, and trigger defaults may change while in beta.
