---
title: "Using agent memory (Claude Managed Agents memory stores)"
aliases:
  - "Claude Managed Agents Memory Stores"
  - "Managed Agents memory"
source_type: "docs"
kind: "shared-memory-store"
status: "verified"
year: 2026
publication_date: "2026-04-23"
publication_date_basis: "vendor_launch_blog_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Anthropic"
venue: "Claude Platform Docs"
url: "https://platform.claude.com/docs/en/managed-agents/memory"
pdf_url: ""
created: 2026-07-03
updated: 2026-07-03
---

# Claude Managed Agents Memory Stores

## Summary

- A memory store is a workspace-scoped collection of text documents mounted as a directory under `/mnt/memory/<slug>/` in the session sandbox; stores attach via `resources[]` at session creation only (beta header `managed-agents-2026-04-01`), with `read_write` (default) or `read_only` access enforced at the filesystem level.
- Limits: max 8 memory stores per session, 2,000 memories per store, 100 kB (~25k tokens) per memory, per-store instructions capped at 4,096 characters.
- Conflict resolution is optimistic concurrency: a `content_sha256` precondition on `memories.update` means an update applies only if the stored hash matches what was read, else the writer re-reads and retries.
- Every mutation creates an immutable memory version (`memver_...`) attributed to the writing session, retained 30 days, with a redact endpoint for scrubbing secrets/PII from history while preserving the audit trail; versions outlive deleted memories.
- Recommended namespacing: one read-only shared reference store attached to many sessions plus per-user/team/project read-write stores; the docs carry an explicit prompt-injection warning that a read_write shared store lets injected content become trusted memory in later sessions.
- The companion launch post (2026-04-23) cites Rakuten 97% fewer first-pass errors and Wisedocs 30% faster verification; dreaming sessions consolidate a fragmented store into a new output store.

## Claims

- [[claims/Claim - Agent memory and skills create compounding improvement loops]]

## Connections

- [[operations/agent memory]]
- [[operations/agent infrastructure]]
- [[concepts/dreaming and memory consolidation]]
- [[safety/prompt injection]]
- [[sources/Anthropic Managed Agents]]
- [[sources/Anthropic Managed Agents Dreaming Outcomes]]

## Notes

- Canonical URL: https://platform.claude.com/docs/en/managed-agents/memory
- Companion launch post: https://claude.com/blog/claude-managed-agents-memory (2026-04-23); the docs page itself is undated, so the launch-post date is used.
- Rakuten and Wisedocs figures are vendor-reported customer metrics, not independently verified.
- Canonical answer to which memory stores can be attached across agents: write authority, concurrency, audit, and namespacing mechanics are all specified here.
