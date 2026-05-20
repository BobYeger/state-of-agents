---
title: "An open-source spec for Codex orchestration: Symphony"
aliases:
  - "Symphony"
  - "OpenAI Symphony"
source_type: "repo"
status: "verified"
year: 2026
publication_date: "2026-04-27"
publication_date_basis: "openai_visible_published_date"
source_updated_date: null
source_updated_date_basis: null
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "OpenAI"
venue: "OpenAI"
url: "https://github.com/openai/symphony"
pdf_url: ""
artifacts:
  - "raw/repositories/openai-symphony-readme.md"
  - "raw/repositories/openai-symphony-spec.md"
created: 2026-05-20
updated: 2026-05-20
---

# OpenAI Symphony

## Summary

- Open-source orchestration spec and reference implementation for turning issue-tracker work into isolated autonomous coding-agent runs.
- Important because it treats Linear-style tickets as a control plane: one workspace per issue, bounded concurrency, workflow policy, proof of work, retries, and human review.
- Bridges coding-agent harnesses with multi-session project management and always-on agent operations.

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Connections

- [[concepts/issue tracker control plane]]
- [[operations/agent harnesses]]
- [[operations/durable sessions]]
- [[operations/agent observability]]
- [[systems/Codex]]

## Artifacts

- [[raw/repositories/openai-symphony-readme.md]]
- [[raw/repositories/openai-symphony-spec.md]]

## Notes

- Official article URL: https://openai.com/index/open-source-codex-orchestration-symphony/
- The OpenAI article was blocked from local capture, so the archived artifacts are the official repository README and spec.
