---
title: "Sleep-time Compute: Beyond Inference Scaling at Test-time"
aliases:
  - "Sleep-time Compute"
source_type: "paper"
kind: "background-context-computation"
status: "verified"
year: 2025
publication_date: "2025-04-17"
publication_date_basis: "arxiv_v1_submission_date"
arxiv_id: "2504.13171"
authors:
  - "Kevin Lin"
  - "Charlie Snell"
  - "Yu Wang"
  - "Charles Packer"
  - "Sarah Wooders"
  - "Ion Stoica"
  - "Joseph E. Gonzalez"
venue: "arXiv / Letta and UC Berkeley"
url: "https://arxiv.org/abs/2504.13171"
pdf_url: "https://arxiv.org/pdf/2504.13171v1"
evidence_class: "author-run-research-experiments"
metrics_status: "author-reported"
artifacts: []
created: 2026-10-05
updated: 2026-10-05
---

# Sleep-time Compute

## Contribution and Test

Computes over persistent context before the next question arrives. Experiments separate context from queries and test amortization across related questions. Roughly fivefold lower query-time compute at matched accuracy is reported for low-budget Stateful GSM-Symbolic settings with GPT-4o/mini; AIME results vary by model, with limited gains for o1. This is not fivefold lower total compute. Predictable questions benefit more.

The software case study measures overlap with files changed in reference pull requests, not executable patch correctness. Benefits weaken at high query-time budgets; changing contexts and interleaved interactions exceed the simple two-phase experimental setup.

## Research Blog

The authors' [April 21, 2025 blog](https://www.letta.com/blog/sleep-time-compute/) connects the experiment to background memory editing and Letta's implementation. It is explanation and implementation evidence from the same team, not an independent replication.

## Reading

[Full text, sections 5–7](https://arxiv.org/html/2504.13171v1); [experiment code](https://github.com/letta-ai/sleep-time-compute).

## Connections

- [[concepts/background agents]]
- [[concepts/dreaming and memory consolidation]]
- [[concepts/harness-aware agent learning]]
- [[sources/MemGPT]]
- [[sources/SCLATE]]
