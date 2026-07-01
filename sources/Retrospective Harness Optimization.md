---
title: "Evolving Agents in the Dark: Retrospective Harness Optimization via Self-Preference"
aliases:
  - "RHO"
  - "Retrospective Harness Optimization"
source_type: "paper"
kind: "self-improving-harness"
status: "verified"
year: 2026
publication_date: "2026-06-04"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: "2026-06-10"
source_updated_date_basis: "arxiv_v2_revision_date"
arxiv_id: "2606.05922"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Wenbo Pan"
  - "Shujie Liu"
  - "Chin-Yew Lin"
  - "Jingying Zeng"
  - "Xianfeng Tang"
  - "Xiangyang Zhou"
  - "Yan Lu"
  - "Xiaohua Jia"
venue: "arXiv"
url: "https://arxiv.org/abs/2606.05922"
pdf_url: "https://arxiv.org/pdf/2606.05922"
artifacts:
  - "raw/papers/RHO - Retrospective Harness Optimization via Self-Preference.pdf"
created: 2026-07-01
updated: 2026-07-01
---

# Evolving Agents in the Dark

## Summary

- Introduces Retrospective Harness Optimization, a self-supervised method for improving an agent harness using past trajectories rather than labeled validation sets.
- Selects difficult prior tasks, re-solves them in parallel, analyzes rollouts with self-validation/self-consistency, proposes harness updates, and chooses by pairwise self-preference.
- Important because it turns production history into optimization data when ground-truth labels are scarce.
- Needs caution: self-preference is attractive for bootstrapping but weaker than independent evaluation when failures are high-stakes.

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[methods/self-improving code loops]]
- [[maps/Harness Tracker]]
- [[operations/agent harnesses]]
- [[operations/agent evals]]
- [[concepts/loop engineering]]

## Artifacts

- [[raw/papers/RHO - Retrospective Harness Optimization via Self-Preference.pdf]]

## Notes

- Canonical arXiv URL: https://arxiv.org/abs/2606.05922
- arXiv metadata: submitted June 4, 2026; revised June 10, 2026.
