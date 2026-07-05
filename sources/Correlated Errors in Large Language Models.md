---
title: "Correlated Errors in Large Language Models"
aliases: []
source_type: "paper"
kind: "error-correlation"
status: "verified"
year: 2025
publication_date: "2025-06-09"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2506.07962"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Elliot Kim"
  - "Avi Garg"
  - "Kenny Peng"
  - "Nikhil Garg"
venue: "arXiv / ICML 2025 (Cornell / Cornell Tech)"
url: "https://arxiv.org/abs/2506.07962"
pdf_url: "https://arxiv.org/pdf/2506.07962"
artifacts:
  - "raw/papers/Correlated Errors in Large Language Models.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# Correlated Errors in Large Language Models

## Summary

- Empirical study of error correlation across 350+ LLMs using leaderboard data plus a resume-screening task.
- On one leaderboard dataset, models agree 60% of the time when both models err — far above independence, breaking the Condorcet jury theorem assumption behind majority voting.
- Correlation is driven by shared architectures and shared providers, but larger and more accurate models have highly correlated errors even across distinct architectures and providers — diversity cannot be bought by mixing frontier vendors.
- Demonstrates downstream consequences in two aggregation settings: LLM-as-judge evaluation (judge errors correlate with judged-model errors) and hiring/resume screening (algorithmic monoculture — many firms making identical mistakes).
- Accepted to ICML 2025.

## Claims

- [[claims/Claim - More agents are not automatically better]]

## Connections

- [[concepts/multi-agent systems]]
- [[operations/agent evals]]
- [[concepts/code factories]]
- [[sources/Judging LLM-as-a-Judge with MT-Bench]]
- [[sources/X-MAS]]
- [[sources/Aligned Agents Biased Swarm]]

## Artifacts

- [[raw/papers/Correlated Errors in Large Language Models.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2506.07962
- Quantifies why adding voters saturates and why heterogeneous ensembles and independent verification channels (tests, execution) matter in both MAS harnesses and code factories.
- Correlation estimates come mainly from static benchmark answers, not agentic trajectories; error correlation in tool-use settings may differ.
