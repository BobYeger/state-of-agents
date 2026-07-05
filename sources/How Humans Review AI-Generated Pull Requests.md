---
title: "These Aren't the Reviews You're Looking For: How Humans Review AI-Generated Pull Requests"
aliases:
  - "These Aren't the Reviews You're Looking For"
source_type: "paper"
kind: "agent-pr-review-study"
status: "verified"
year: 2026
publication_date: "2026-05-04"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2605.02273"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Kacper Duma"
  - "Patryk Wróblewski"
  - "Jagoda Bobińska"
  - "Julia Winiarska"
  - "Piotr Przymus"
venue: "arXiv (Nicolaus Copernicus University, Toruń)"
url: "https://arxiv.org/abs/2605.02273"
pdf_url: "https://arxiv.org/pdf/2605.02273"
artifacts:
  - "raw/papers/These Aren't the Reviews You're Looking For - How Humans Review AI-Generated Pull Requests.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# How Humans Review AI-Generated Pull Requests

## Summary

- Empirical study of review activity on agent-authored PRs using the AIDev dataset.
- The majority of AI-generated PRs receive no review activity at all.
- When agentic PRs are reviewed, the review is dominated by AI agents rather than humans; human-authored PRs are far more likely to get human-only review and direct human feedback.
- Human participation on agentic PRs typically takes the form of steering agents (automation-mediated interaction) rather than independent assessment of the diff.
- Core warning: conventional review metrics (reviewed/not-reviewed, comment counts) overstate the level of actual human oversight once agents both author and review PRs.

## Connections

- [[concepts/code factories]]
- [[concepts/human-in-the-loop agents]]
- [[sources/Modern Code Review at Google]]
- [[sources/DORA State of AI-assisted Software Development 2025]]
- [[sources/Bias in the Loop]]

## Artifacts

- [[raw/papers/These Aren't the Reviews You're Looking For - How Humans Review AI-Generated Pull Requests.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2605.02273
- Direct observational evidence of the rubber-stamping / oversight-erosion failure mode: at current agent volumes most agent PRs already bypass human review, and "reviewed" increasingly means "reviewed by another agent."
- Findings are on open-source repositories in the AIDev dataset; review behavior inside companies with mandatory gates may differ.
