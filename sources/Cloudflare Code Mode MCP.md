---
title: "Code Mode: the better way to use MCP"
aliases: []
source_type: "article"
status: "verified"
year: 2025
publication_date: "2025-09-26"
publication_date_basis: "cloudflare_article_published_time"
source_updated_date: null
source_updated_date_basis: null
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Cloudflare"
venue: "Cloudflare"
url: "https://blog.cloudflare.com/code-mode/"
pdf_url: ""
artifacts:
  - "raw/articles/cloudflare-code-mode-mcp.md"
created: 2026-05-18
updated: 2026-10-05
---

# Code Mode: the better way to use MCP

## Summary

- Argues that exposing every MCP tool directly to a model is often inefficient.
- Introduces a code-mode approach where tools can be represented as a TypeScript API instead of a large tool list.
- Important for token-efficient tool exposure and tool-use ergonomics.

## Evidence and Limits

- Primary engineering experiment from September 26, 2025: tool schemas become a TypeScript API, and generated code passes intermediate outputs between calls without sending each value through the model.
- The article supplies an SDK implementation and examples, not a controlled benchmark showing universal superiority over direct tool calls. Its training-data explanation is the author's hypothesis.
- MCP still supplies discovery, connectivity, and authorization boundaries. Executable code needs a restricted runtime and mediated capabilities; small model-visible tool count is not small authority.

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Connections

- [[protocols/MCP]]
- [[concepts/tool-use contracts]]
- [[operations/cost control]]
- [[concepts/programmatic tool calling]]
- [[sources/CodeAct]]
- [[sources/LLMCompiler]]
- [[sources/Cloudflare Code Mode MCP API]]

## Artifacts

- [[raw/articles/cloudflare-code-mode-mcp.md]]

## Notes

- Canonical URL: https://blog.cloudflare.com/code-mode/
- Publication date basis: cloudflare_article_published_time.
