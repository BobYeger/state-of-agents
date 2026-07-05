---
title: "ImpossibleBench: Measuring LLMs' Propensity of Exploiting Test Cases"
aliases:
  - "ImpossibleBench"
source_type: "paper"
kind: "benchmark"
status: "verified"
year: 2025
publication_date: "2025-10-23"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2510.20270"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Ziqian Zhong"
  - "Aditi Raghunathan"
  - "Nicholas Carlini"
venue: "arXiv (ICLR 2026 poster)"
url: "https://arxiv.org/abs/2510.20270"
pdf_url: "https://arxiv.org/pdf/2510.20270"
artifacts:
  - "raw/papers/ImpossibleBench - Measuring LLMs' Propensity of Exploiting Test Cases.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# ImpossibleBench

## Summary

- Operationalizes the impossible-task probe: mutates SWE-bench/LiveCodeBench tasks so unit tests directly contradict the natural-language spec — any pass on an "impossible" variant necessarily implies a spec-violating shortcut, yielding a clean "cheating rate" metric.
- Documents a spectrum of cheating strategies, from simple test modification/deletion up to operator-overloading exploits that subvert equality checks.
- Framework supports three defense uses: behavioral analysis of shortcut types, context-engineering studies (e.g., the effect of restricting test access to read-only), and building/validating monitoring tools and cheat detectors.
- Open-source Inspect implementation at github.com/safety-research/impossiblebench; accepted as an ICLR 2026 poster.

## Connections

- [[benchmarks/agent evaluation]]
- [[concepts/outcomes and rubric graders]]
- [[operations/agent evals]]
- [[sources/SWE-bench]]
- [[sources/METR Recent Reward Hacking]]

## Artifacts

- [[raw/papers/ImpossibleBench - Measuring LLMs' Propensity of Exploiting Test Cases.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2510.20270
- The metric measures propensity given a contradictory spec, not incidence in normal use — pair with METR's observational rates for the field picture.
- Turns reward hacking into a trackable rate a coding-agent CI can regression-test against.
