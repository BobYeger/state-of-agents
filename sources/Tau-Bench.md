---
title: "τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains"
aliases:
  - "tau-bench"
  - "TAU-bench"
source_type: "paper"
kind: "benchmark"
status: "verified"
year: 2024
publication_date: "2024-06-17"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2406.12045"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Shunyu Yao"
  - "Noah Shinn"
  - "Pedram Razavi"
  - "Karthik Narasimhan"
venue: "arXiv / Sierra"
url: "https://arxiv.org/abs/2406.12045"
pdf_url: "https://arxiv.org/pdf/2406.12045"
artifacts:
  - "raw/papers/Tau-bench - A Benchmark for Tool-Agent-User Interaction in Real-World Domains.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# Tau-Bench

## Summary

- Origin of the pass^k metric: the probability an agent succeeds on all k of k i.i.d. trials of the same task — a pessimistic reliability bound, in contrast to optimistic pass@k (at least one success in k).
- GPT-4o-era function-calling agents succeed on fewer than 50% of tasks, and pass^8 falls below 25% in the retail domain — consistency collapses much faster than average success rates suggest.
- Emulates dynamic conversations between an LM-simulated user and an agent equipped with domain-specific API tools and policy guidelines, in retail and airline domains; failures include policy-rule violations, not just task misses.
- Evaluation compares the final database state against an annotated goal state — outcome-based grading rather than trajectory-based.
- pass^k has since been adopted in frontier-lab reporting as the standard pessimistic reliability bound for deployed agents.

## Connections

- [[benchmarks/agent evaluation]]
- [[operations/agent evals]]
- [[concepts/tool use]]
- [[sources/On Randomness in Agentic Evals]]
- [[sources/Rigorous Agentic Benchmarks]]

## Artifacts

- [[raw/papers/Tau-bench - A Benchmark for Tool-Agent-User Interaction in Real-World Domains.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2406.12045
- The ABC audit ([[sources/Rigorous Agentic Benchmarks]]) later found a grading bug in τ-bench: empty responses were counted as successes on some tasks — a caveat on early reported numbers.
- User simulation is itself an LM, so user-side behavior adds a second source of run variance.
