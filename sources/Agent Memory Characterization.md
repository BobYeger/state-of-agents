---
title: "Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads"
aliases:
  - "Agent Memory Characterization"
source_type: "paper"
kind: "agent-memory"
status: "verified"
year: 2026
publication_date: "2026-06-04"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: null
source_updated_date_basis: null
arxiv_id: "2606.06448"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Zeyu Liu"
  - "Xinyu Zhang"
  - "Yuxuan Wang"
  - "Wenhao Huang"
venue: "arXiv"
url: "https://arxiv.org/abs/2606.06448"
pdf_url: "https://arxiv.org/pdf/2606.06448"
artifacts:
  - "raw/papers/Agent Memory - Characterization and System Implications of Stateful Long-Horizon Workloads.pdf"
created: 2026-07-01
updated: 2026-07-01
---

# Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads

## Summary

- Systems characterization paper arguing that agent memory should be treated as infrastructure for stateful long-horizon workloads, not as a thin retrieval feature.
- Provides a taxonomy of memory systems along four axes and profiles ten representative memory systems.
- Useful for harness engineering because it frames memory construction, scheduling, freshness/latency tradeoffs, and fleet-scale management as runtime design problems.
- Pairs well with product examples such as [[sources/Cloudflare Agent Memory]] and newer memory research such as [[sources/Are We Ready For An Agent-Native Memory System]], [[sources/TokenPilot]], and [[sources/SWE-MeM]].

## Claims

- [[claims/Claim - Agent memory and skills create compounding improvement loops]]
- [[claims/Claim - Context management is an agent architecture choice]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Connections

- [[operations/agent memory]]
- [[maps/Context Management Map]]
- [[maps/Recent Agent Operating Concepts]]
- [[operations/agent harnesses]]
- [[concepts/context engineering]]

## Artifacts

- [[raw/papers/Agent Memory - Characterization and System Implications of Stateful Long-Horizon Workloads.pdf]]

## Notes

- Canonical arXiv URL: https://arxiv.org/abs/2606.06448
- arXiv metadata: submitted June 4, 2026.
- Main vault use: anchor the claim that memory is now a first-class operating subsystem for agents.
