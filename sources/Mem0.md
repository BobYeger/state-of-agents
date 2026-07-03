---
title: "Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory"
aliases:
  - "Mem0"
source_type: "paper"
kind: "agent-memory-system"
status: "verified"
year: 2025
publication_date: "2025-04-28"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2504.19413"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Prateek Chhikara"
  - "Dev Khant"
  - "Saket Aryan"
  - "Taranjeet Singh"
  - "Deshraj Yadav"
venue: "arXiv (Mem0)"
url: "https://arxiv.org/abs/2504.19413"
pdf_url: "https://arxiv.org/pdf/2504.19413"
created: 2026-07-03
updated: 2026-07-03
---

# Mem0

## Summary

- Pipeline dynamically extracts and consolidates salient facts from conversation into a memory store; evaluated on LoCoMo across single-hop, temporal, multi-hop, and open-domain question types.
- 26% relative improvement in LLM-as-a-Judge metric over OpenAI's memory feature on LoCoMo.
- 91% lower p95 latency and over 90% token cost savings versus the full-context approach.
- The graph-memory variant (Mem0-g) adds only about 2% over the base vector configuration — a concrete data point that graph structure buys little on conversational QA.
- Compared against six baseline categories: memory systems, RAG variants, full-context, and commercial solutions.

## Claims

- [[claims/Claim - Context management is an agent architecture choice]]

## Connections

- [[operations/agent memory]]
- [[concepts/context retrieval]]
- [[sources/Zep Temporal Knowledge Graph Memory]]
- [[sources/LongMemEval]]
- [[sources/Memora]]

## Notes

- Canonical URL: https://arxiv.org/abs/2504.19413
- The base-vs-graph delta (~2%) is direct substrate-tradeoff evidence: on conversational QA, extraction quality matters more than graph structure. Contrast with corpus-level tasks where GraphRAG-style structure wins.
- Vendor-authored evaluation of the authors' own product; LoCoMo is a conversational benchmark, distinct from the LongMemEval results Mem0 reported later (94.4 with its 2026 algorithm).
