---
title: "Prompt caching (Claude Platform Docs)"
aliases:
  - "Claude API prompt caching"
  - "Anthropic prompt caching docs"
source_type: "docs"
kind: "prompt-caching"
status: "verified"
year: 2026
publication_date: "2026-02-05"
publication_date_basis: "docs_update_note"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Anthropic"
venue: "Claude Platform Docs"
url: "https://platform.claude.com/docs/en/build-with-claude/prompt-caching"
pdf_url: ""
artifacts:
  - "raw/docs/claude-api-prompt-caching.md"
created: 2026-07-03
updated: 2026-07-05
---

# Claude API Prompt Caching

## Summary

- Pricing multipliers: 5-minute cache writes cost 1.25x base input, 1-hour writes 2x, cache reads 0.1x; controlled per-block via `cache_control` `{type: ephemeral, ttl}`.
- At most 4 explicit cache breakpoints per request; the prefix hierarchy is tools -> system -> messages, so a tool-definition change invalidates everything downstream, while `tool_choice` or image changes invalidate only the messages cache.
- Minimum cacheable prefix varies by model: 512 tokens (Fable 5/Mythos 5), 1,024 (Opus 4.8, Sonnet 4.5+), up to 4,096 (Haiku 4.5); automatic prefix checking looks back roughly 20 content blocks per breakpoint.
- The top-level `cache_control` field auto-places the breakpoint on the last cacheable block and moves it forward as the conversation grows — the API-native pattern for append-only agent loops.
- February 5, 2026 updates: caches are isolated per workspace (not just per organization) on the Claude API, and Opus 4.8 supports mid-conversation `{role: system}` messages that add instructions without invalidating the cached prefix.
- Cache pre-warming pattern: send a `max_tokens: 0` request to write the cache without sampling any output.

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Connections

- [[operations/cost control]]
- [[operations/agent harnesses]]
- [[concepts/context engineering]]
- [[sources/Claude Code Prompt Caching]]
- [[sources/Manus Context Engineering]]
- [[sources/Claude API Compaction]]

## Artifacts

- [[raw/docs/claude-api-prompt-caching.md]]

## Notes

- Canonical URL: https://platform.claude.com/docs/en/build-with-claude/prompt-caching
- Living docs page; the publication date is the changelog date of the most recent substantive update (workspace isolation, mid-conversation system messages), not a first-published date.
- Complements the Claude Code-level card ([[sources/Claude Code Prompt Caching]]), which covers how the harness orders prompt layers rather than the API mechanics.
