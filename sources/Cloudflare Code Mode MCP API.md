---
title: "Code Mode: give agents an entire API in 1,000 tokens"
aliases: []
source_type: "article"
status: "verified"
year: 2026
publication_date: "2026-02-20"
publication_date_basis: "cloudflare_article_published_time"
source_updated_date: null
source_updated_date_basis: null
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Matt Carey"
venue: "Cloudflare"
url: "https://blog.cloudflare.com/code-mode-mcp/"
pdf_url: ""
artifacts:
  - "raw/articles/cloudflare-code-mode-mcp-api.md"
created: 2026-05-26
updated: 2026-10-05
---

# Code Mode: give agents an entire API in 1,000 tokens

## Summary

- Introduces a server-side Code Mode MCP server for the Cloudflare API.
- Collapses a large API surface into two executable discovery/action tools: `search()` and `execute()`.
- Important because it treats MCP as a boundary while replacing giant tool-schema exposure with progressive code-based API discovery.
- Explicitly compares Code Mode with client-side Code Mode, CLIs, and dynamic tool search.

## Evidence and Limits

- Reports roughly 1,000 tokens for the two exposed tools, compared with 1.17 million tokens for the equivalent direct API schema surface, measured with tiktoken. This is schema footprint, not total task tokens: discovery results, generated code, and observations still cost context and execution.
- The example searches an API specification with over 2,500 endpoints and executes through an authenticated client in a Worker isolate. OAuth scopes restrict available effects; hiding schemas does not grant permission.
- Useful implementation evidence for progressive discovery plus code composition, not a benchmark proving improved task success over all retrieval approaches.

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Connections

- [[protocols/MCP]]
- [[concepts/agent operating surfaces]]
- [[concepts/programmatic tool calling]]
- [[concepts/dynamic tool discovery]]
- [[concepts/tool-use contracts]]
- [[operations/cost control]]
- [[operations/sandboxes]]
- [[sources/CodeAct]]
- [[sources/LLMCompiler]]

## Artifacts

- [[raw/articles/cloudflare-code-mode-mcp-api.md]]

## Notes

- Canonical URL: https://blog.cloudflare.com/code-mode-mcp/
- Publication date basis: cloudflare_article_published_time.
