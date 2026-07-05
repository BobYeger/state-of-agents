---
title: "G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems"
aliases:
  - "G-Memory"
source_type: "paper"
kind: "multi-agent-memory"
status: "verified"
year: 2025
publication_date: "2025-06-09"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2506.07398"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Guibin Zhang"
  - "Muxin Fu"
  - "Guancheng Wan"
  - "Miao Yu"
  - "Kun Wang"
  - "Shuicheng Yan"
venue: "arXiv (cs.MA)"
url: "https://arxiv.org/abs/2506.07398"
pdf_url: "https://arxiv.org/pdf/2506.07398"
artifacts:
  - "raw/papers/G-Memory - Tracing Hierarchical Memory for Multi-Agent Systems.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# G-Memory

## Summary

- Hierarchical multi-agent-system memory inspired by organizational memory theory: a three-tier graph hierarchy of insight, query, and interaction graphs.
- Bi-directional memory traversal retrieves both high-level generalizable insights and fine-grained condensed, agent-specific interaction trajectories — cross-trial lesson propagation without flattening per-agent context.
- Improves embodied-action success by up to +20.89% and knowledge-QA accuracy by up to +10.12% across five benchmarks, three LLM backbones, and three MAS frameworks, with no framework modifications.
- arXiv v1 2025-06-09, v2 2025-06-16; code at github.com/bingreeky/GMemory.

## Claims

- [[claims/Claim - Agent memory and skills create compounding improvement loops]]

## Connections

- [[operations/agent memory]]
- [[concepts/multi-agent systems]]
- [[methods/multi-agent learning]]
- [[concepts/lifelong agent learning]]
- [[sources/When Agents Misremember Collectively]]

## Artifacts

- [[raw/papers/G-Memory - Tracing Hierarchical Memory for Multi-Agent Systems.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2506.07398
- Reference constructive design for team-wide memory: the insight/query/interaction split shows how to propagate lessons across a team while keeping each agent's memory customized.
- Gains are measured on simulated MAS benchmarks (embodied action, knowledge QA); no production-deployment evidence yet.
