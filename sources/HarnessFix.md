---
title: "From Failed Trajectories to Reliable LLM Agents: Diagnosing and Repairing Harness Flaws"
aliases:
  - "HarnessFix"
source_type: "paper"
kind: "self-improving-harness"
status: "verified"
year: 2026
publication_date: "2026-06-04"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: null
source_updated_date_basis: null
arxiv_id: "2606.06324"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Mengzhuo Chen"
  - "Junjie Wang"
  - "Zhe Liu"
  - "Yawen Wang"
  - "Qing Wang"
venue: "arXiv"
url: "https://arxiv.org/abs/2606.06324"
pdf_url: "https://arxiv.org/pdf/2606.06324"
artifacts:
  - "raw/papers/HarnessFix - Diagnosing and Repairing Harness Flaws.pdf"
created: 2026-07-01
updated: 2026-07-01
---

# From Failed Trajectories to Reliable LLM Agents

## Summary

- Trace-guided framework for diagnosing failed agent trajectories and repairing the responsible harness layer.
- Compiles traces and harness code into a harness-aware trace intermediate representation, attributes failures to steps/layers, and maps recurring flaws to scoped repair operators.
- Important because it is more disciplined than generic self-improvement: it asks which harness layer caused the failure and validates targeted patches.
- Useful for explaining how harness engineering becomes an evidence loop.

## Claims

- [[claims/Claim - Runtime control and verification improve agent reliability]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Connections

- [[methods/self-improving code loops]]
- [[operations/agent observability]]
- [[operations/agent evals]]
- [[operations/agent harnesses]]
- [[maps/Harness Tracker]]

## Artifacts

- [[raw/papers/HarnessFix - Diagnosing and Repairing Harness Flaws.pdf]]

## Notes

- Canonical arXiv URL: https://arxiv.org/abs/2606.06324
- arXiv metadata: submitted June 4, 2026.
