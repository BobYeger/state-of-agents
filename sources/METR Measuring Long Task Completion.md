---
title: "Measuring AI Ability to Complete Long Software Tasks"
aliases:
  - "METR time horizon paper"
  - "50% task-completion time horizon"
source_type: "paper"
kind: "capability-measurement"
status: "verified"
year: 2025
publication_date: "2025-03-18"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2503.14499"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Thomas Kwa"
  - "Ben West"
  - "Joel Becker"
  - "METR (25 authors)"
venue: "arXiv / NeurIPS 2025"
url: "https://arxiv.org/abs/2503.14499"
pdf_url: "https://arxiv.org/pdf/2503.14499"
artifacts:
  - "raw/papers/Measuring AI Ability to Complete Long Software Tasks.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# Measuring AI Ability to Complete Long Software Tasks

## Summary

- Defines the 50%-task-completion time horizon: the human task duration at which an AI model succeeds 50% of the time, fit across human-baselined task suites (HCAST + RE-Bench + 66 new shorter SWAA tasks).
- Headline finding: the frontier time horizon has doubled roughly every 7 months since 2019, with acceleration in 2024; Claude 3.7 Sonnet sat at a ~50-minute horizon at publication.
- Identified improvement drivers: greater reliability, better mistake adaptation, improved logical reasoning, and tool-use competence.
- Extrapolation: at trend, AI automates many month-long human software tasks within 5 years.
- Published at NeurIPS 2025 (latest arXiv revision 2026-02-25); the standard quantitative frame for autonomy budgeting — how long an agent can be left to run per unit of human oversight.

## Connections

- [[concepts/long-horizon agents]]
- [[benchmarks/long-horizon benchmarks]]
- [[benchmarks/agent evaluation]]
- [[sources/METR Time Horizon 1.1]]
- [[sources/Anthropic Measuring Agent Autonomy]]

## Artifacts

- [[raw/papers/Measuring AI Ability to Complete Long Software Tasks.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2503.14499
- The headline "7-month doubling" was revised by METR's Time Horizon 1.1 update (2026-01-29): post-2023 doubling is estimated ~20% faster (~131 days). Quote the updated figures for recent-period claims.
- Citation count pending vault backfill.
