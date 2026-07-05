---
title: "Errors (Claude API reference)"
aliases:
  - "Claude API error taxonomy"
  - "Anthropic API errors"
source_type: "docs"
kind: "error-taxonomy"
status: "verified"
year: 2026
publication_date: "2026-07"
publication_date_basis: "docs_access_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Anthropic"
venue: "Claude Platform Docs"
url: "https://platform.claude.com/docs/en/api/errors"
pdf_url: ""
artifacts:
  - "raw/docs/claude-api-errors.md"
created: 2026-07-03
updated: 2026-07-05
---

# Claude API Errors

## Summary

- Full provider error taxonomy with exact type names a retry policy must branch on: 400 `invalid_request_error`, 401 `authentication_error`, 402 `billing_error`, 403 `permission_error`, 404 `not_found_error`, 413 `request_too_large`, 429 `rate_limit_error`, 500 `api_error`, 504 `timeout_error`, 529 `overloaded_error`.
- 429 and 529 require distinct retry policies: 529 signals global overload across all users, while sharp per-organization usage spikes surface as 429 "acceleration limits" — the docs advise ramping traffic gradually rather than backing off identically for both.
- In SSE streaming an error can occur after a 200 response has already been returned, so HTTP-status-based error handling does not cover mid-stream failures — a first-order design constraint for any harness that streams.
- Every response carries a `request-id` header (exposed as `message._request_id` in the SDKs); on AWS two IDs exist per request (`x-amzn-requestid` primary for CloudTrail, `request-id` for Anthropic support).
- Request size limits: Messages/Token Counting 32 MB, Batch API 256 MB, Files API 500 MB; the 413 for Messages is returned by Cloudflare before the request reaches API servers.
- SDKs validate that non-streaming requests will not exceed a 10-minute timeout and set TCP keep-alive; the docs push streaming or the Batch API for long requests.

## Connections

- [[operations/agent harnesses]]
- [[operations/agent infrastructure]]
- [[operations/durable sessions]]
- [[sources/Temporal OpenAI Agents SDK Integration]]
- [[sources/Restate Durable AI Loops]]
- [[sources/Architecting Resilient LLM Agents]]

## Artifacts

- [[raw/docs/claude-api-errors.md]]

## Notes

- Canonical URL: https://platform.claude.com/docs/en/api/errors
- Living reference page with no visible publication date; the date above is the access date. The URL moved from docs.anthropic.com/en/api/errors (now a 301) to platform.claude.com.
- The 429-vs-529 acceleration-limit distinction and the mid-stream-error caveat are the load-bearing facts for unattended retry design; specific size limits may change without a changelog entry.
