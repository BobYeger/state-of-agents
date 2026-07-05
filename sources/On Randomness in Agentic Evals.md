---
title: "On Randomness in Agentic Evals"
source_type: "paper"
kind: "eval-statistics"
status: "verified"
year: 2026
publication_date: "2026-02-06"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2602.07150"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Bjarni Haukur Bjarnason"
  - "André Silva"
  - "Martin Monperrus"
venue: "arXiv / KTH"
url: "https://arxiv.org/abs/2602.07150"
pdf_url: "https://arxiv.org/pdf/2602.07150"
artifacts:
  - "raw/papers/On Randomness in Agentic Evals.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# On Randomness in Agentic Evals

## Summary

- Empirically quantifies run-to-run variance in agentic evaluation: 60,000 agent trajectories collected across three models and two scaffolds on SWE-Bench-Verified.
- Single-run pass@1 estimates vary by 2.2-6.0 percentage points depending on which run is selected; standard deviations exceed 1.5pp even at temperature 0.
- Concludes that reported improvements of 2-3pp — the typical size of harness tweaks — may be evaluation noise rather than genuine progress.
- Token-level analysis shows trajectories diverge within the first few percent of tokens, cascading into entirely different solution strategies, so variance is intrinsic to the agent loop, not just sampling temperature.
- Recommends three practices: multi-run pass@1 estimation, statistical power analysis to set run counts, and reporting pass@k (optimistic) alongside pass^k (pessimistic) for k>1.

## Connections

- [[operations/agent evals]]
- [[benchmarks/agent evaluation]]
- [[methods/self-improving code loops]]
- [[sources/Adding Error Bars to Evals]]
- [[sources/Tau-Bench]]

## Artifacts

- [[raw/papers/On Randomness in Agentic Evals.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2602.07150
- Variance figures are specific to SWE-Bench-Verified with the studied models/scaffolds; the magnitude (not the existence) of the effect may differ elsewhere.
