---
title: "LLM-based Multi-Agent Blackboard System for Information Discovery in Data Science"
aliases:
  - "blackboard vs coordinator LLM study"
source_type: "paper"
kind: "blackboard-coordination"
status: "verified"
year: 2025
publication_date: "2025-09-30"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2510.01285"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Alireza Salemi"
  - "Mihir Parmar"
  - "Palash Goyal"
  - "Yiwen Song"
  - "Jinsung Yoon"
  - "Hamed Zamani"
  - "Tomas Pfister"
  - "Hamid Palangi"
venue: "arXiv (cs.MA), UMass Amherst / Google"
url: "https://arxiv.org/abs/2510.01285"
pdf_url: "https://arxiv.org/pdf/2510.01285"
artifacts:
  - "raw/papers/LLM-based Multi-Agent Blackboard System for Information Discovery in Data Science.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# LLM Multi-Agent Blackboard System

## Summary

- Direct LLM-era evaluation of blackboard vs coordinator-directed (master-slave) coordination: instead of the central agent assigning subtasks to named agents, it posts requests to a shared blackboard and subordinate agents volunteer based on self-assessed capability.
- 13%-57% relative improvement in end-to-end success across three data-science benchmarks (KramaBench, modified DSBench, DA-Code) and up to 9% relative gain in data-discovery F1 over the strongest baseline.
- Removes the requirement that the coordinator know each sub-agent's expertise or internal knowledge — the scalability argument for blackboard pickup over direct task assignment.
- v1 submitted 2025-09-30; revised v2 published 2026-01-31 — the v2 revision is the version to cite.

## Claims

- [[claims/Claim - Agent systems improve when structure matches the task]]

## Connections

- [[methods/multi-agent orchestration]]
- [[methods/runtime routing]]
- [[concepts/multi-agent systems]]
- [[sources/Corkill Blackboard Systems]]
- [[sources/AutoGen SelectorGroupChat]]

## Artifacts

- [[raw/papers/LLM-based Multi-Agent Blackboard System for Information Discovery in Data Science.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2510.01285
- Fills the gap for LLM-era evaluations of blackboard vs message-passing coordination with concrete win margins; volunteer-based task pickup from a shared store was previously uncovered in the vault.
- Evaluated on data-science information-discovery tasks; margins may not transfer to code-generation or long-horizon agent workloads.
