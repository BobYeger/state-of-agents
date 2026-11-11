---
title: "From AutoResearch to Continual AutoResearch: Do Agents Learn Across Tasks?"
aliases:
  - "Continual AutoResearch"
source_type: "paper"
kind: "cross-task-research-memory-evaluation"
status: "verified"
year: 2026
publication_date: "2026-11-03"
publication_date_basis: "arxiv_v1_submission_date"
source_version: "arxiv_v1"
arxiv_id: "2611.05108"
authors:
  - "Jeremy Qin"
  - "Ruizhi Deng"
  - "Mohamed Osama Ahmed"
  - "Frederick Tung"
  - "Leo Feng"
venue: "arXiv"
url: "https://arxiv.org/abs/2611.05108"
pdf_url: "https://arxiv.org/pdf/2611.05108v1"
discovery_url: "https://academy.dair.ai/papers/collections/self-improving-agents?view=latest"
evidence_class: "author-run-paired-agent-evaluation"
metrics_status: "author-reported"
created: 2026-11-09
updated: 2026-11-09
---

# Continual AutoResearch

## Protocol

Pairs persistent and reset native CLI agents across nine task families. Persistence retains sessions and workspaces, including code, results, and traces; weights stay fixed. Main streams contain 3–5 tasks, usually 30 minutes each. Task order is matched and fixed; transfer excludes the first task. Agents access each task's training/development data; private tests score submissions afterward. This is continual task adaptation, not frozen-memory evaluation after a separate task-training phase.

## Findings and Limits

All five agents improve mean time-integrated best-candidate utility, without consistent final gains: Opus 5 gains 7.5 normalized utility points but loses 0.9 final-reward points. An Energy-system ablation resets sessions and transfers only agent-authored insight cards, matched, shuffled, or absent; relevant cards do not reliably improve outcomes. Case studies show anchoring and overfitting.

Only GPT-5.6-Sol has three matched repetitions; other main comparisons use one. Short streams, fixed ordering, and native-harness differences limit generalization. Wall-clock utility is not token or monetary savings.

## Reading

[Full text: sections 3, 5–6; Appendices A, B.5, C–D](https://arxiv.org/html/2611.05108v1).

## Connections

- [[concepts/lifelong agent learning]]
- [[concepts/memory use calibration]]
- [[systems/autoresearch]]
- [[reports/Memory and Dreaming Update - 2026-11-09]]
