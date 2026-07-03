---
title: "Introducing GPT-5.5"
aliases:
  - "GPT-5.5"
source_type: "article"
kind: "frontier-model-release"
status: "partial"
year: 2026
publication_date: "2026-04-23"
publication_date_basis: "secondary_reports_openai_page_not_fetched"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "OpenAI"
venue: "OpenAI Blog"
url: "https://openai.com/index/introducing-gpt-5-5/"
pdf_url: ""
created: 2026-07-03
updated: 2026-07-03
---

# OpenAI GPT-5.5

## Summary

- Released 2026-04-23 in ChatGPT and Codex, with API availability 2026-04-24 alongside GPT-5.5 Pro; 1M-token context window. In Codex it serves a 400K window at included pricing, with a fast mode at 2.5x rates.
- Benchmarks (per Vellum's roundup of OpenAI's numbers): Terminal-Bench 2.0 82.7% (vs Opus 4.7's 69.4%), SWE-bench Pro 58.6% (behind Claude's 64.3%), long-context 512K-1M 74.0% vs GPT-5.4's 36.6%, OSWorld-Verified 78.7%, CyberGym 81.8%.
- API pricing $5/M input, $30/M output — a 2x increase over GPT-5.4, which OpenAI says is offset by a ~40% token-efficiency gain, delivering better Codex results with fewer tokens.
- Positioned as agent-first: "moving across tools until a task is finished" — operating software, building documents and spreadsheets, researching, debugging.
- Sits in a rapid 2026 Codex model cadence: GPT-5.2-Codex and GPT-5.3-Codex (with its own system card) preceded it; GPT-5.6 "Sol" was previewed after.

## Connections

- [[systems/Codex]]
- [[operations/cost control]]
- [[sources/Terminal-Bench]]
- [[sources/SWE-bench Pro]]
- [[sources/OpenAI Codex Agent Loop]]

## Notes

- Canonical URL: https://openai.com/index/introducing-gpt-5-5/
- openai.com returned 403 to the fetcher, so the canonical page could not be fetch-verified; existence and facts were corroborated via search results, the NVIDIA blog, 9to5Mac, and a fetched Vellum analysis. Re-verify against the OpenAI page when accessible.
- Benchmark figures are OpenAI's own numbers as relayed by Vellum, not independent measurements.
