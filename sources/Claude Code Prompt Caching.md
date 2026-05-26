---
title: "Claude Code prompt caching"
aliases:
  - "Claude Code Prompt Caching"
source_type: "docs"
kind: "product-docs"
status: "verified"
year: 2026
publication_date: "2026-05-26"
publication_date_basis: "snapshot_date"
source_updated_date: "2026-05-26"
source_updated_date_basis: "snapshot_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Anthropic"
venue: "Claude Code Docs"
url: "https://code.claude.com/docs/en/prompt-caching"
pdf_url: ""
artifacts:
  - "raw/docs/claude-code-prompt-caching.md"
created: 2026-05-26
updated: 2026-05-26
---

# Claude Code Prompt Caching

## Summary

- Explains how Claude Code orders prompt layers and how compaction interacts with prompt caching.
- Useful because compaction has runtime cost and cache consequences, not only semantic consequences.
- Keep as an implementation detail connected to the context-management map.

## Connections

- [[concepts/context compaction]]
- [[operations/cost control]]
- [[operations/agent harnesses]]
- [[maps/Context Management Map]]

## Artifacts

- [[raw/docs/claude-code-prompt-caching.md]]

## Notes

- Canonical URL: https://code.claude.com/docs/en/prompt-caching
