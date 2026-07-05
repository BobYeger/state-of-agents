---
title: "The SWE-Bench Illusion: When State-of-the-Art LLMs Remember Instead of Reason"
aliases:
  - "The SWE-Bench Illusion"
source_type: "paper"
kind: "contamination-analysis"
status: "verified"
year: 2025
publication_date: "2025-06-14"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2506.12286"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Shanchao Liang"
  - "Spandan Garg"
  - "Roshanak Zilouchian Moghaddam"
venue: "arXiv / Purdue + Microsoft"
url: "https://arxiv.org/abs/2506.12286"
pdf_url: "https://arxiv.org/pdf/2506.12286"
artifacts:
  - "raw/papers/The SWE-Bench Illusion - When State-of-the-Art LLMs Remember Instead of Reason.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# SWE-bench Illusion

## Summary

- Diagnostic probe: SOTA models identify the buggy file path from the issue description alone — no repository access — with up to 76% accuracy on SWE-Bench Verified, but only up to 53% on repos outside SWE-Bench, evidence of memorization rather than reasoning.
- A function-reproduction probe shows up to 35% consecutive 5-gram verbatim accuracy on SWE-Bench Verified/Full versus only up to 18% on other coding benchmarks.
- Attributes the gap to repository-bias memorization: models overfit to the architectural patterns and problem distributions of the roughly 12 repositories underlying SWE-Bench.
- Directly implies SWE-bench Verified headline scores overstate generalizable software-engineering ability — a discount factor for any capability trend line built on them.
- v1 2025-06-14, revised through v4 on 2025-12-01.

## Connections

- [[benchmarks/agent evaluation]]
- [[sources/SWE-bench]]
- [[sources/SWE-bench Verified]]
- [[sources/SWE-bench Pro]]
- [[sources/LiveCodeBench]]

## Artifacts

- [[raw/papers/The SWE-Bench Illusion - When State-of-the-Art LLMs Remember Instead of Reason.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2506.12286
- The probes measure memorization signal, not how much of end-to-end resolve rate it explains; the paper argues contamination, it does not decompose headline scores into memorized versus reasoned fractions.
