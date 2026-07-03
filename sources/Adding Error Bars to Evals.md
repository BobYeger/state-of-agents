---
title: "Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations"
source_type: "paper"
kind: "eval-statistics"
status: "verified"
year: 2024
publication_date: "2024-11-01"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2411.00640"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Evan Miller"
venue: "arXiv / Anthropic"
url: "https://arxiv.org/abs/2411.00640"
pdf_url: "https://arxiv.org/pdf/2411.00640"
created: 2026-07-03
updated: 2026-07-03
---

# Adding Error Bars to Evals

## Summary

- Frames eval questions as samples drawn from an unseen super-population, which makes the Central Limit Theorem applicable to eval scores and puts model comparisons on standard statistical footing.
- Provides concrete formulas for standard errors on eval scores, paired-difference analysis for comparing two models on the same questions, clustered standard errors, and variance-reduction techniques.
- Covers power analysis for experiment planning: how many questions and runs are needed to detect a given effect size before declaring one model or harness variant better.
- 14-page paper with specific numbered recommendations for running and reporting language model evaluations.
- Directly applicable to keep/revert decisions in self-improving systems, which are two-sample hypothesis tests whether or not builders treat them as such.

## Connections

- [[operations/agent evals]]
- [[benchmarks/agent evaluation]]
- [[methods/self-improving code loops]]
- [[sources/On Randomness in Agentic Evals]]
- [[sources/Anthropic Demystifying Agent Evals]]

## Notes

- Canonical URL: https://arxiv.org/abs/2411.00640
- Written for question-answering-style evals; agentic multi-run settings need the extensions in [[sources/On Randomness in Agentic Evals]] for trajectory-level variance.
