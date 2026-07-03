---
title: "Bias in the Loop: How Humans Evaluate AI-Generated Suggestions"
aliases: []
source_type: "paper"
kind: "human-oversight-experiment"
status: "verified"
year: 2025
publication_date: "2025-09-10"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2509.08514"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Jacob Beck"
  - "Stephanie Eckman"
  - "Christoph Kern"
  - "Frauke Kreuter"
venue: "arXiv; Harvard Data Science Review 8.2 (Spring 2026)"
url: "https://arxiv.org/abs/2509.08514"
pdf_url: "https://arxiv.org/pdf/2509.08514"
created: 2026-07-03
updated: 2026-07-03
---

# Bias in the Loop

## Summary

- Randomized experiment with 2,784 participants reviewing AI-generated suggestions; manipulated early AI suggestion quality, correction burden, and performance-based financial incentives.
- Friction drives rubber-stamping: when flagging an AI error required typing a corrected value, participants made fewer corrections and accepted more incorrect suggestions — direct design guidance that rejection must be as cheap as approval in review UIs.
- Pre-existing attitude toward AI was the strongest predictor of performance, outweighing demographics: AI-skeptical participants detected errors more reliably and were more accurate; automation-favorable participants accepted more wrong suggestions.
- Measured outcomes include accuracy, correction activity, overcorrection, and undercorrection — a reusable measurement vocabulary for review-gate evaluation.

## Connections

- [[concepts/human-in-the-loop agents]]
- [[concepts/code factories]]
- [[operations/permissions]]
- [[sources/How Humans Review AI-Generated Pull Requests]]

## Notes

- Canonical URL: https://arxiv.org/abs/2509.08514
- The cleanest controlled experiment on approval-fatigue mechanics: isolates the interface variable (correction burden) and the human variable (AI attitude) that determine whether a human gate actually catches errors.
- Task was data-annotation-style suggestion review with crowd participants, not code review by engineers; magnitudes may differ in developer settings.
