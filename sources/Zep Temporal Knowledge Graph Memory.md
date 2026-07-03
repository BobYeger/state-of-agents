---
title: "Zep: A Temporal Knowledge Graph Architecture for Agent Memory"
aliases:
  - "Zep paper"
  - "Graphiti"
source_type: "paper"
kind: "temporal-kg-memory"
status: "verified"
year: 2025
publication_date: "2025-01-20"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2501.13956"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Preston Rasmussen"
  - "Pavlo Paliychuk"
  - "Travis Beauvais"
  - "Jack Ryan"
  - "Daniel Chalef"
venue: "arXiv (Zep AI)"
url: "https://arxiv.org/abs/2501.13956"
pdf_url: "https://arxiv.org/pdf/2501.13956"
created: 2026-07-03
updated: 2026-07-03
---

# Zep Temporal Knowledge Graph Memory

## Summary

- Core engine is Graphiti, a temporally-aware (bi-temporal) knowledge graph that records both when a fact became true and when it stopped being true, with automatic fact invalidation and episode-level provenance.
- 94.8% on Deep Memory Retrieval (DMR) vs MemGPT's 93.4% on the same benchmark.
- Up to 18.5% accuracy improvement on LongMemEval with roughly 90% response latency reduction versus full-context baselines.
- Integrates conversational and structured business data into one graph, rather than treating memory as static document retrieval.
- By 2026 the open-source Graphiti engine crossed 20,000 GitHub stars and roughly 25,000 weekly PyPI downloads.

## Claims

- [[claims/Claim - Context management is an agent architecture choice]]

## Connections

- [[operations/agent memory]]
- [[concepts/context retrieval]]
- [[sources/Zep Markdown Is Not Agent Memory]]
- [[sources/Zep Smart Context Assembly]]
- [[sources/LongMemEval]]
- [[sources/MemGPT]]

## Notes

- Canonical URL: https://arxiv.org/abs/2501.13956
- This is the underlying paper the vault's two Zep blog cards rest on; benchmark numbers are vendor-reported (Zep AI authors evaluating their own system).
- The DMR comparison against MemGPT uses a benchmark MemGPT's own authors have criticized as saturated; the LongMemEval results are the more informative evidence.
