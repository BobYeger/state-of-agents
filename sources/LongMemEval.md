---
title: "LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory"
aliases:
  - "LongMemEval"
source_type: "paper"
kind: "benchmark"
status: "verified"
year: 2024
publication_date: "2024-10-14"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2410.10813"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Di Wu"
  - "Hongwei Wang"
  - "Wenhao Yu"
  - "Yuwei Zhang"
  - "Kai-Wei Chang"
  - "Dong Yu"
venue: "ICLR 2025 / arXiv (UCLA / Tencent AI Lab)"
url: "https://arxiv.org/abs/2410.10813"
pdf_url: "https://arxiv.org/pdf/2410.10813"
artifacts:
  - "raw/papers/LongMemEval - Benchmarking Chat Assistants on Long-Term Interactive Memory.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# LongMemEval

## Summary

- 500 questions over freely scalable user-assistant chat histories, testing five core abilities: information extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention.
- The knowledge-update and abstention subtasks make it double as a forgetting/supersession benchmark: systems must prefer newer facts over superseded ones and decline when memory lacks the answer.
- Commercial chat assistants and long-context LLMs show a 30% accuracy drop when memorizing information across sustained interactions.
- Proposes a three-stage memory design space (indexing, retrieval, reading) with session decomposition, fact-augmented key expansion, and time-aware query expansion as concrete optimizations.
- Now the de-facto reporting benchmark for memory systems: Zep reports up to +18.5% on it, and Mem0's 2026 algorithm reports 94.4. arXiv v2 2025-03-04.

## Connections

- [[benchmarks/agent evaluation]]
- [[benchmarks/long-horizon benchmarks]]
- [[operations/agent memory]]
- [[sources/Letta Context-Bench]]

## Artifacts

- [[raw/papers/LongMemEval - Benchmarking Chat Assistants on Long-Term Interactive Memory.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2410.10813
- Vendor scores reported against this benchmark (Zep, Mem0) come from vendor papers/posts and vary in setup; compare configurations before quoting deltas.
- The abstention/knowledge-update subtasks are the vault's best available evidence source for forgetting and supersession behavior.
