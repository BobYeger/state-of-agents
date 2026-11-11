---
title: "Instant Software Factories"
aliases: ["Instant Software Factories"]
tags: [sources, code-factories]
source_type: "paper"
status: "verified"
evidence_class: "operator-observational-study"
publication_date: "2026-10-26"
publication_date_basis: "arxiv_v1_submission_date"
source_version: "arxiv_v1"
arxiv_id: "2610.36254"
authors: ["Wenxin Jiang", "Mikola Lysenko"]
venue: "arXiv"
url: "https://arxiv.org/abs/2610.36254"
created: 2026-11-09
updated: 2026-11-09
---

# Instant Software Factories

## Contribution

Socket observes two manually configured industrial factories for 15 and 17 days. One coordinates scheduled, bounded agents through GitHub issues, PRs, and checks. The proposed one-session bootstrap remains unevaluated.

## Evidence and Boundaries

Daily CLI merges rose from 2.2 to about 35 during rollout; this is an association. Agents filed 95% of new issues and authored 40/58 CI-changing PRs. By day 17, at least 25/450 issues marked fixed had incorrect fixes; seven shipped unrepaired.

Both factories retained human approval. One organization, changing configurations, short observation, incomplete defect detection, and no architectural control limit generalization. The paper reports no intentional gaming.

## Implication

A factory changes its own backlog and evaluator. Count independently validated changes that reach users and survive later checks, alongside throughput.

## Connections

- [[concepts/code factories]]
- [[concepts/evaluator reliability]]
- [[reports/Code Factories Update - 2026-11-09]]

## Primary Link

[Full text v1, Sections III–VI](https://arxiv.org/html/2610.36254v1).
