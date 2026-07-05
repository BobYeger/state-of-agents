---
title: "AI Agents That Matter"
source_type: "paper"
kind: "agent-eval-methodology"
status: "verified"
year: 2024
publication_date: "2024-07-01"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2407.01502"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Sayash Kapoor"
  - "Benedikt Stroebl"
  - "Zachary S. Siegel"
  - "Nitya Nadgir"
  - "Arvind Narayanan"
venue: "arXiv (cs.LG) / Princeton"
url: "https://arxiv.org/abs/2407.01502"
pdf_url: "https://arxiv.org/pdf/2407.01502"
artifacts:
  - "raw/papers/AI Agents That Matter.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# AI Agents That Matter

## Summary

- Identifies five shortcomings in agent benchmarking: narrow accuracy focus without cost; conflation of model-developer vs downstream-developer benchmarking needs; inadequate or absent holdout sets; agents overfitting via shortcuts; and lack of standardization causing pervasive irreproducibility.
- Argues accuracy-only leaderboards produce needlessly complex, costly SOTA agents; proposes jointly optimizing the cost-accuracy Pareto frontier instead, and demonstrates on HumanEval that simple baselines match complex agent architectures at greatly reduced cost.
- Shows inadequate holdouts let agents take shortcuts that inflate accuracy but break on real tasks — the foundational argument for holdout/refresh design in agent evals.
- Documents a reproducibility crisis in agent evaluation and distinguishes what model developers need from benchmarks versus what downstream application developers need.
- Single-version arXiv preprint (v1 2024-07-01); founding paper of the Princeton evaluation line of work that later produced the Holistic Agent Leaderboard.

## Connections

- [[operations/agent evals]]
- [[operations/cost control]]
- [[benchmarks/agent evaluation]]
- [[sources/Holistic Agent Leaderboard]]
- [[sources/Evaluation and Benchmarking of LLM Agents - A Survey]]

## Artifacts

- [[raw/papers/AI Agents That Matter.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2407.01502
- Cost figures use 2024 API pricing; the Pareto-frontier argument is pricing-independent but specific dollar comparisons are dated.
