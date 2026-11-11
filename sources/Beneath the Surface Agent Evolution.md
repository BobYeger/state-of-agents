---
title: "Beneath the Surface: What We Overlook When We Talk About Agent Evolution"
aliases: ["EvoAudit", "Audit-Guided Evolution", "AGE"]
source_type: "paper"
kind: "harness-evolution-evaluation"
status: "verified"
year: 2026
publication_date: "2026-11-05"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: "2026-11-05"
source_version: "arxiv_v1"
arxiv_id: "2611.07624"
authors: ["Xiaobo Wang", "Zimu Wang", "Siyu Ye", "Jiaqi Li", "Min Tang", "Jun Bai", "Yuling Shi", "Ruobing Wang", "Jingjing Zhang", "Chaofan Wang", "Kai Wu", "Mengnan Qi", "Kai Cai", "Xiaodong Gu", "Qi Liu", "Zilong Zheng"]
venue: "arXiv"
url: "https://arxiv.org/abs/2611.07624"
pdf_url: "https://arxiv.org/pdf/2611.07624v1"
created: 2026-11-09
updated: 2026-11-09
tags: [research, harness, evaluation]
---

# Beneath the Surface: Agent Evolution

## Contribution

Audits AHE, HyperAgents, A-Evolve, and GEPA under source-editable MiniSWE and outer-layer-only Codex, using GPT-5.4. Repeated evaluation separates average success, any-success task coverage, task turnover, and deployment versus evolution cost.

## Evidence and Limits

All sixteen evaluated evolved agents gain some tasks and lose others. One banking configuration improves average success by 5.2 points while losing ten previously covered tasks. Aggregate improvement therefore conceals regressions. Component interactions and candidate-admission replays further distinguish successful edits from productive parents and useful selection rules.

EvoAudit informs the AGE redesign; this is an author-run constructive follow-up. Eight evaluation passes improve visibility into stochastic outcomes but do not establish universal applicability. Results cover two task families, one backbone, and specific edit surfaces. Expert endorsement of proposed revisions is separate from measured outcomes or deployment safety.

## Connections

- [[concepts/evaluator reliability]]
- [[methods/self-improving code loops]]
- [[sources/Retrospective Harness Adaptation Study]]
- [[reports/Harness Self-Improvement Update - 2026-11-09]]

## Primary Links

- [Metadata](https://arxiv.org/abs/2611.07624)
- [Full text v1, Sections 3–8 and split-accounting appendices](https://arxiv.org/html/2611.07624v1)
