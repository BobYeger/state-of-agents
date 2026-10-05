---
title: "Mid-conversation system messages and tool changes"
aliases:
  - "Claude inline tool definitions"
source_type: "docs"
kind: "runtime-tool-definition-mutation"
status: "verified"
year: 2026
publication_date: "2026-09-22"
publication_date_basis: "claude_platform_release_notes_inline_tool_definitions"
source_updated_date: "2026-10-05"
source_updated_date_basis: "living_docs_access_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Anthropic"
venue: "Claude Platform Docs"
url: "https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages"
pdf_url: ""
artifacts: []
created: 2026-10-05
updated: 2026-10-05
---

# Claude Mid-Conversation Tool Definitions

## Summary

- Defines new tools or replaces schemas in appended system-message blocks, preserving the prior cached prefix. MCP toolsets can arrive the same way; returned `mcp_tool_listing` blocks pin the fetched list when replayed.
- September 22 is the [release-note date](https://platform.claude.com/docs/en/release-notes/overview#september-22-2026) for inline definitions. The `inline-tools-2026-09-15` header is a protocol label, not the announcement date. Earlier system messages and tool references are separate features.

## Evidence and Limits

- Beta contract, not a benchmark of retrieval quality. Requires the inline-tools header; MCP additions require the MCP-client header too.
- Keep a non-deferred tool in the initial array to avoid a first-addition cache miss. Some types, including computer use, still require advance declaration. Placement and size limits apply.
- Pinning the listing stabilizes offered schemas; it does not freeze remote implementation or grant execution authority. Retain application-side permissions and version handling.
- Living documentation accessed October 5, 2026; canonical links retained without copying the page.

## Connections

- [[concepts/dynamic tool discovery]]
- [[concepts/cache-aware harness design]]
- [[concepts/tool-use contracts]]
- [[sources/Gorilla]]
- [[sources/ScaleMCP]]
- [[sources/Anthropic Advanced Tool Use]]
