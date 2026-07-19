---
title: "Programmatic Tool Calling"
aliases:
  - "OpenAI Programmatic Tool Calling"
  - "OpenAI PTC"
source_type: "docs"
kind: "tool-use-docs"
status: "verified"
year: 2026
publication_date: "2026-07-13"
publication_date_basis: "accessed_living_docs_no_visible_publication_date"
source_updated_date: "2026-07-13"
source_updated_date_basis: "snapshot_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "OpenAI"
venue: "OpenAI Developers"
url: "https://developers.openai.com/api/docs/guides/tools-programmatic-tool-calling"
pdf_url: ""
artifacts:
  - "raw/docs/openai-programmatic-tool-calling.md"
created: 2026-07-13
updated: 2026-07-13
---

# OpenAI Programmatic Tool Calling

## Summary

- Lets a model generate JavaScript that calls eligible tools in parallel or sequence, applies loops and conditions, and returns a compact result instead of placing every intermediate tool response into model context.
- Each program runs in a fresh isolated V8 runtime with top-level `await` but no Node.js, packages, direct network access, general filesystem, subprocesses, console, or persistent JavaScript state. External effects remain reachable only through explicitly enabled tools.
- OpenAI draws a clear decision boundary: use code for bounded, predictable data flow such as filtering, joining, ranking, deduplication, aggregation, and validation; use direct model tool calls when each result needs fresh semantic judgment.
- Writes, approval-sensitive actions, and final citation or native-artifact validation should default to direct calls. Tool arguments and permissions must still be checked application-side, and high-impact actions require approval regardless of whether the caller is the model or generated code.
- Supports Zero Data Retention workflows without a persistent code-execution container. The docs recommend evaluating it against direct calling on correctness, evidence coverage, tokens, latency, retries, recovery, and safety rather than assuming that fewer model-visible intermediates are automatically better.

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[concepts/programmatic tool calling]]
- [[concepts/tool use]]
- [[operations/permissions]]
- [[operations/cost control]]
- [[operations/agent harnesses]]
- [[sources/Anthropic Code Execution with MCP]]
- [[sources/Cloudflare Code Mode MCP API]]
- [[sources/OpenAI GPT-5.6]]

## Artifacts

- [[raw/docs/openai-programmatic-tool-calling.md]]

## Notes

- Canonical URL: https://developers.openai.com/api/docs/guides/tools-programmatic-tool-calling
- Living documentation snapshot from 2026-07-13. The docs deliberately avoid a universal efficiency claim and instruct teams to benchmark both routes on representative work.
