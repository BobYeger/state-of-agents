---
title: "Establishing Best Practices for Building Rigorous Agentic Benchmarks"
aliases:
  - "Agentic Benchmark Checklist"
  - "ABC"
source_type: "paper"
kind: "benchmark-methodology"
status: "verified"
year: 2025
publication_date: "2025-07-03"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2507.02825"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Yuxuan Zhu"
  - "Tengjun Jin"
  - "Sayash Kapoor"
  - "Percy Liang"
  - "Daniel Kang"
venue: "arXiv / UIUC, Stanford, Berkeley, Princeton, MLCommons, UK AISI"
url: "https://arxiv.org/abs/2507.02825"
pdf_url: "https://arxiv.org/pdf/2507.02825"
artifacts:
  - "raw/papers/Establishing Best Practices for Building Rigorous Agentic Benchmarks.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# Rigorous Agentic Benchmarks

## Summary

- Introduces the Agentic Benchmark Checklist (ABC), organized into three assessment areas: task validity, outcome validity, and benchmark reporting (39 pages, 15 tables).
- Documents grading bugs that misestimate agent performance by up to 100% in relative terms: SWE-bench Verified uses insufficient test cases, and TAU-bench counted empty responses as successes.
- Audit of 10 popular agentic benchmarks found 7 with outcome-validity flaws, 7 with task-validity issues, and reporting limitations in all 10.
- Applying ABC to CVE-Bench reduced performance overestimation by 33%.
- v1 2025-07-03, revised through v5 on 2025-08-07.

## Connections

- [[benchmarks/agent evaluation]]
- [[operations/agent evals]]
- [[sources/Tau-Bench]]
- [[sources/SWE-bench Verified]]
- [[sources/AI Agents That Matter]]
- [[sources/Holistic Agent Leaderboard]]

## Artifacts

- [[raw/papers/Establishing Best Practices for Building Rigorous Agentic Benchmarks.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2507.02825
- The named grading bugs (SWE-bench Verified test insufficiency, TAU-bench empty-response successes) apply to specific benchmark versions at audit time; both projects have shipped fixes since, so verify version before repeating the numbers.
