---
title: "Does Learning to Predict the World Help Agents Act? Auditing World-Model Post-Training"
aliases:
  - "World-Model Post-Training Audit"
  - "Does Learning to Predict the World Help Agents Act"
source_type: "paper"
kind: "agent-world-model-training-attribution-audit"
status: "verified"
year: 2026
publication_date: "2026-09-27"
publication_date_basis: "arxiv_v1_submission_history"
source_updated_date: null
source_updated_date_basis: null
source_version: "arXiv v1; full text inspected October 5, 2026"
arxiv_id: "2609.33335"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "not assessed"
authors:
  - "Xinyu Che"
  - "Hang Yan"
  - "Yanchen Liu"
  - "Haochen Liu"
  - "Ruifeng Li"
  - "Anran Shi"
  - "Heng Wang"
  - "Jun Liu"
venue: "arXiv"
url: "https://arxiv.org/abs/2609.33335"
pdf_url: "https://arxiv.org/pdf/2609.33335v1"
license: "CC BY 4.0"
license_url: "https://creativecommons.org/licenses/by/4.0/"
evidence_class: "author-run-controlled-agent-training-audit-preprint"
artifacts: []
created: 2026-10-05
updated: 2026-10-05
---

# Does Learning to Predict the World Help Agents Act?

## Summary

- Separates learning accurate environment predictions from other effects of post-training. Controls replace correct next observations with mismatched observations or replace prediction rewards with independent random signals.
- In ALFWorld and ScienceWorld, mismatched targets reduce prediction accuracy substantially while retaining much task improvement. Broader action consideration and less looping accompany gains without requiring correct prediction content.
- In VisualWebArena, random-reward training raises pass@64 from 34.83% to 39.80%, a 14.3% relative increase; pass@1 moves from 11.48% to 12.66%. These measure different improvements.

## Evidence Boundary

Author-run preprint in simulated benchmarks with specified small open models. **Pass@64 measures coverage across repeated attempts, not reliable single-attempt completion.** Correct observation targets can still improve action selection. The audit does not show that accurate world models are generally useless or that random rewards are a universal training recipe.

The architectural lesson is to measure prediction quality, action quality, looping, and task success separately before attributing a better agent loop to a particular learned mechanism.

## Connections

- [[concepts/agent loop]]
- [[concepts/harness-aware agent learning]]
- [[concepts/tool use]]
- [[benchmarks/agent evaluation]]
- [[sources/Agent Evaluation Reliability]]
- [[sources/Mind2Web]]

## Sources

- [Versioned full text](https://arxiv.org/html/2609.33335v1), sections 2–4 and 6.
- [Submission history](https://arxiv.org/abs/2609.33335).
- [Authors' code repository](https://github.com/KosmoCHE/WM-PostTraining-Audit).
