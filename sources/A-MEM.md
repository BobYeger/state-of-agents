---
title: "A-MEM: Agentic Memory for LLM Agents"
aliases:
  - "A-MEM"
source_type: "paper"
kind: "agentic-memory"
status: "verified"
year: 2025
publication_date: "2025-02-17"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2502.12110"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Wujiang Xu"
  - "Zujie Liang"
  - "Kai Mei"
  - "Hang Gao"
  - "Juntao Tan"
  - "Yongfeng Zhang"
venue: "NeurIPS 2025 / arXiv (Rutgers)"
url: "https://arxiv.org/abs/2502.12110"
pdf_url: "https://arxiv.org/pdf/2502.12110"
artifacts:
  - "raw/papers/A-MEM - Agentic Memory for LLM Agents.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# A-MEM

## Summary

- Applies Zettelkasten principles to agent memory: each new memory becomes a structured note (contextual description, keywords, tags) rather than a raw log entry.
- Dynamic link generation: the system analyzes historical memories and establishes links where meaningful similarities exist — the agent, not a fixed schema, decides the graph structure.
- Memory evolution: new entries can trigger updates to the contextual representations and attributes of existing memories (retroactive rewriting), so the store restructures itself as understanding improves.
- Improvements over state-of-the-art memory baselines shown across six foundation models; revised through v11 (2025-10-08), accepted at NeurIPS 2025.

## Claims

- [[claims/Claim - Agent memory and skills create compounding improvement loops]]

## Connections

- [[operations/agent memory]]
- [[concepts/LLM-maintained knowledge bases]]
- [[concepts/context evolution]]
- [[sources/Zep Markdown Is Not Agent Memory]]

## Artifacts

- [[raw/papers/A-MEM - Agentic Memory for LLM Agents.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2502.12110
- The agent-curated-notes substrate: the midpoint between markdown files and rigid knowledge graphs on the substrate tradeoff axis.
- Retroactive memory rewriting improves coherence but erases the original record — a provenance/audit tradeoff the paper does not address.
