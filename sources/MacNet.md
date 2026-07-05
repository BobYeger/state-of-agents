---
title: "Scaling Large Language Model-based Multi-Agent Collaboration (MacNet)"
aliases:
  - "MacNet"
  - "collaborative scaling law"
source_type: "paper"
kind: "multi-agent-topology"
status: "verified"
year: 2024
publication_date: "2024-06-11"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2406.07155"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Chen Qian"
  - "Zihao Xie"
  - "YiFei Wang"
  - "Weize Chen"
  - "Cheng Yang"
  - "Zhiyuan Liu"
  - "Maosong Sun"
venue: "ICLR 2025 (arXiv 2406.07155), Tsinghua"
url: "https://arxiv.org/abs/2406.07155"
pdf_url: "https://arxiv.org/pdf/2406.07155"
artifacts:
  - "raw/papers/Scaling Large Language Model-based Multi-Agent Collaboration (MacNet).pdf"
created: 2026-07-03
updated: 2026-07-05
---

# MacNet

## Summary

- MacNet organizes agents on directed acyclic graphs for topologically orchestrated interactive reasoning; supports collaboration among over 1,000 agents.
- Irregular topologies outperform regular ones — topology choice, not raw agent count, drives quality.
- Proposes the "collaborative scaling law": performance follows logistic growth as agent count scales, with collaborative emergence occurring earlier than emergence in neural (parameter) scaling laws.
- Mechanism claim: scaling agents catalyzes multidimensional consideration during interactive reflection and refinement, producing more comprehensive artifacts.
- Accepted at ICLR 2025; v3 posted 2025-03-17; implementation ships inside the ChatDev repository.

## Claims

- [[claims/Claim - Agent systems improve when structure matches the task]]
- [[claims/Claim - More agents are not automatically better]]

## Connections

- [[methods/topology optimization]]
- [[concepts/multi-agent systems]]
- [[concepts/scaling with computation]]
- [[sources/ChatDev]]
- [[sources/More Agents Is All You Need]]

## Artifacts

- [[raw/papers/Scaling Large Language Model-based Multi-Agent Collaboration (MacNet).pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2406.07155
- Bridges the "more agents" camp and the coordination-cost camp: agent count helps along a logistic curve, but the topology-beats-count result is the transferable design lesson.
- Implementation lives in the ChatDev repository (already carded as a system source); this card covers the paper, not the codebase.
