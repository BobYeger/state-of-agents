---
title: "AgentBaton: Efficient Model Collaboration in Agentic Tasks"
aliases: ["AgentBaton"]
source_type: "paper"
status: "verified"
publication_date: "2026-10-25"
publication_date_basis: "arxiv_v1_submission_date"
source_version: "arxiv_v1"
arxiv_id: "2610.35959"
authors: ["Junlong Li", "Jindong Jiang", "Yonggan Fu", "Jiarui Yao", "Hanrong Ye", "Wonmin Byeon", "Peter Belcak", "Hao Zhang", "Pavlo Molchanov"]
venue: "arXiv"
url: "https://arxiv.org/abs/2610.35959"
discovery_url: "https://academy.dair.ai/papers/agentbaton-efficient-model-collaboration-in-agentic-tasks-2610.35959"
evidence_class: "author-run-agent-evaluation"
metrics_status: "author-reported"
created: 2026-11-09
updated: 2026-11-09
---

# AgentBaton

## Mechanism

A trained 2B detector chooses one permanent capable-to-efficient handoff within a task. The receiving model inherits the workspace and conversation or searchable history. Model pairs are fixed; timing is learned from 4,000 retrospectively labelled trajectories over 2,000 SWE-rebenchV2 tasks. Task-agent weights stay fixed.

## Evidence and Limits

Eleven pairs run DeepSWE v1.1 and TerminalBench 2.1 using mini-SWE-agent 2.4.0, with two-hour task limits. Average API cost falls 65.9%; only 12 of 22 pair/benchmark settings improve accuracy or lose less than 5% relatively. Local inference is priced at zero, so this is not total ownership cost. Training and detector serving also require accounting.

Fixed-progress comparisons use retrospectively known trajectory lengths. They explain timing effects but are not online policies.

[Primary methods and results, Sections 2–4.5](https://arxiv.org/html/2610.35959v1).

## Connections

- [[methods/runtime routing]]
- [[reports/Multi-Agent Research Update - 2026-11-09]]
- [[reports/DAIR Paper Review - 2026-11-09]]
