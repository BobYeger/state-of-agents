---
title: "EMMA: Structured Episodic Memory for Multi-Agent Workflow Synthesis"
aliases:
  - "EMMA"
source_type: "paper"
kind: "configuration-as-episodic-memory"
status: "verified"
year: 2026
publication_date: "2026-10-25"
publication_date_basis: "arxiv_v1_submission_date"
source_version: "arxiv_v1"
arxiv_id: "2610.35966"
authors:
  - "Ruijia Niu"
  - "Kaiwen Liu"
  - "Rose Yu"
  - "Kristina Klinkner"
venue: "arXiv"
url: "https://arxiv.org/abs/2610.35966"
pdf_url: "https://arxiv.org/pdf/2610.35966v1"
discovery_url: "https://academy.dair.ai/papers/emma-structured-episodic-memory-for-multi-agent-workflow-synthesis-2610.35966"
evidence_class: "author-run-research-experiments"
metrics_status: "author-reported"
created: 2026-11-09
updated: 2026-11-09
---

# EMMA

## Mechanism

Memory is workflow configuration: routing rules, inheriting specialist prompts, and procedural skills. Frozen models learn configuration from training-task failures. Each reflection proposes one edit at the diagnosed scope; guards enforce compatibility, 60% prompt-line retention, bounded pools, leakage checks, and strategy changes. Accepted edits are re-executed but persist even after failure; acceptance does not require demonstrated improvement. A separate chain-end update records routing lessons.

## Evidence and Limits

KramaBench, AppWorld, and BBEH-mini use disjoint splits, with independently learned artifacts per benchmark/backbone, frozen for evaluation. Five-backbone consistency is not transfer of one artifact between models. AppWorld challenge mean task-goal completion is 73.8% versus ACE's 67.4%.

Reported 17–38% savings count training executions, not tokens, dollars, or inference overhead. Ablations use Opus 4.5 on KramaBench; controller memory is present throughout, so its contribution is not isolated. Harmful retained edits remain possible.

## Reading

[Full text: sections 3, 5–6; Appendices B–D](https://arxiv.org/html/2610.35966v1). DAIR supplied discovery; claims were checked against the paper.

## Connections

- [[concepts/procedural memory]]
- [[methods/multi-agent learning]]
- [[reports/Memory and Dreaming Update - 2026-11-09]]
