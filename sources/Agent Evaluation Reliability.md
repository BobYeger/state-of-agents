---
title: "Agent Evaluation Reliability: More Tasks Won't (Always) Fix An Agent Leaderboard"
aliases:
  - "Agent Evaluation Reliability"
  - "More Tasks Won't Always Fix An Agent Leaderboard"
source_type: "paper"
kind: "agent-evaluation-variance-decomposition"
status: "verified"
year: 2026
publication_date: "2026-09-30"
publication_date_basis: "arxiv_v1_submission_history"
source_updated_date: null
source_updated_date_basis: null
source_version: "arXiv v1; full text inspected October 5, 2026"
arxiv_id: "2610.00651"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "not assessed"
authors:
  - "Michael Hardy"
  - "Ruhana Azam"
  - "Anka Reuel"
  - "Mykel Kochenderfer"
  - "Sanmi Koyejo"
venue: "arXiv / Stanford, University of Illinois Urbana-Champaign"
url: "https://arxiv.org/abs/2610.00651"
pdf_url: "https://arxiv.org/pdf/2610.00651v1"
license: "CC BY 4.0"
license_url: "https://creativecommons.org/licenses/by/4.0/"
evidence_class: "leaderboard-reanalysis-and-bayesian-measurement-method-preprint"
artifacts:
  - "raw/papers/Agent Evaluation Reliability - More Tasks Wont Always Fix An Agent Leaderboard.pdf"
created: 2026-10-05
updated: 2026-10-05
---

# Agent Evaluation Reliability

## Summary

- A Bayesian variance decomposition over 22 HAL and Harbor benchmarks separates variation relevant to a claim from variation that can change its rankings. Ranking a fixed model–scaffold system and ranking an underlying model are different measurement goals.
- Estimated reliability is 0.935–0.994 for fixed systems but 0.148–0.841 for underlying models. These are model-based reliability estimates, not task success rates.
- Adding arbitrarily many similarly constructed tasks can improve model-ranking reliability by at most 0.097 in the studied settings when limited scaffold coverage dominates uncertainty.
- Pooling diverse benchmarks projects better cross-task reliability at the same task budget. These are evaluation-design projections, not measured improvements to deployed agents.

## Architectural Implication

Before evaluating a loop, memory system, or training change, declare the object of comparison: a fixed deployed configuration, a model averaged across specified harnesses, or a harness across specified models. Spend further evaluation on the varying factor that limits the intended claim. More examples under one scaffold cannot identify all model–scaffold interactions.

## Evidence Boundary

The preprint reanalyzes sparse, selectively populated public leaderboards. Per-benchmark scaffold samples are often only two or three; results depend on the competitor set, task mix, and scaffold selection. Partial pooling does not correct selective reporting by itself. Estimates are on a latent logit scale and should not be read as exact observed-rank probabilities.

Reliability means consistent differentiation, not correspondence with useful real-world capability. A reliably ranked benchmark may still measure the wrong construct. Interventions proposed to improve coverage require additional empirical validation.

## Connections

- [[concepts/harness-aware agent learning]]
- [[concepts/evaluator reliability]]
- [[operations/agent evals]]
- [[sources/What Does an LLM-Agent Leaderboard Rank Actually Compare]]
- [[sources/Holistic Agent Leaderboard]]
- [[sources/Adding Error Bars to Evals]]
- [[sources/AI Agents That Matter]]
- [[sources/SCLATE]]

## Source And Archive

- [Versioned full text](https://arxiv.org/html/2610.00651v1), especially sections 3–5 and the limitations appendix.
- [Submission history](https://arxiv.org/abs/2610.00651): September 30, 2026, despite the October arXiv identifier.
- Unmodified PDF by the authors above, archived under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/): [[raw/papers/Agent Evaluation Reliability - More Tasks Wont Always Fix An Agent Leaderboard.pdf]].
