---
title: "Why SWE-bench Verified no longer measures frontier coding capabilities"
aliases:
  - "SWE-bench Verified retirement"
source_type: "article"
kind: "benchmark-retirement"
status: "partial"
year: 2026
publication_date: "2026-02"
publication_date_basis: "openai_announcement_month"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "OpenAI"
venue: "OpenAI blog"
url: "https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/"
pdf_url: ""
created: 2026-07-03
updated: 2026-07-03
---

# Why SWE-bench Verified No Longer Measures Frontier Coding Capabilities

## Summary

- Contamination audit found every tested frontier model (GPT-5.2, Claude Opus 4.5, Gemini 3 Flash) could reproduce verbatim gold patches or problem-specific details from Verified tasks — training-data leakage.
- A separate audit of 138 hard problems found 59.4% had flawed test cases that reject functionally correct solutions.
- OpenAI stopped reporting SWE-bench Verified, recommends other labs do the same, and endorses SWE-bench Pro as the replacement (announced via @OpenAIDevs, February 2026).
- By October 2025 frontier scores had climbed past ~75% (GPT-5 74.9%, Claude 4 Sonnet 77.2%); contamination, saturation, and grading flaws combined to end the benchmark's useful life.
- The clearest documented case of benchmark death by contamination and saturation — a lifecycle lesson for anyone designing the eval layer of a code factory.

## Connections

- [[benchmarks/agent evaluation]]
- [[operations/agent evals]]
- [[concepts/code factories]]
- [[sources/SWE-bench]]
- [[sources/SWE-bench Verified]]

## Notes

- Canonical URL: https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/
- openai.com blocks automated fetch (HTTP 403); existence and content corroborated by OpenAI's X announcement, a Hacker News thread (item 47910388), and press coverage — hence status "partial".
- Publication date known only to the month (February 2026).
