---
title: "Ctrl-Z: Controlling AI Agents via Resampling"
aliases:
  - "Ctrl-Z"
  - "BashBench"
source_type: "paper"
kind: "ai-control"
status: "verified"
year: 2025
publication_date: "2025-04-14"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2504.10374"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Aryan Bhatt"
  - "Cody Rushing"
  - "Adam Kaufman"
  - "Tyler Tracy"
  - "Vasil Georgiev"
  - "David Matolcsi"
  - "Akbir Khan"
  - "Buck Shlegeris"
venue: "arXiv (Redwood Research)"
url: "https://arxiv.org/abs/2504.10374"
pdf_url: "https://arxiv.org/pdf/2504.10374"
created: 2026-07-03
updated: 2026-07-03
---

# Ctrl-Z: Controlling AI Agents via Resampling

## Summary

- First control evaluation in a multi-step agent environment, extending the original AI Control methodology beyond single-shot code generation.
- Introduces BashBench: 257 multi-step system-administration tasks in which an adversarial agent tries to covertly download and execute malicious code.
- Resample protocols dynamically take additional samples of suspicious actions, using the variance across samples to incriminate attackers.
- Best protocol cuts covert malicious-code-execution success from 58% to 7% at only a 5% cost to legitimate task performance.
- Best results combine resampling with analysis of historical steps in the trajectory, not just the current action.

## Claims

- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[sources/AI Control Despite Intentional Subversion]]
- [[methods/runtime supervision]]
- [[operations/sandboxes]]
- [[safety/agent safety and security]]

## Notes

- Canonical URL: https://arxiv.org/abs/2504.10374
- The 58%-to-7% headline is against the paper's own red-team attack policies on BashBench; safety numbers are protocol-vs-attack-policy specific, not general guarantees.
