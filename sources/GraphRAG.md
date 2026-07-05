---
title: "From Local to Global: A Graph RAG Approach to Query-Focused Summarization"
aliases:
  - "GraphRAG"
  - "Microsoft GraphRAG"
source_type: "paper"
kind: "graph-rag"
status: "verified"
year: 2024
publication_date: "2024-04-24"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2404.16130"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Darren Edge"
  - "Ha Trinh"
  - "Newman Cheng"
venue: "arXiv (Microsoft Research)"
url: "https://arxiv.org/abs/2404.16130"
pdf_url: "https://arxiv.org/pdf/2404.16130"
artifacts:
  - "raw/papers/From Local to Global - A Graph RAG Approach to Query-Focused Summarization.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# GraphRAG

## Summary

- Two-stage pipeline: an LLM derives an entity knowledge graph from source documents, then pre-generates community summaries for entity clusters; at query time each community summary yields a partial answer, consolidated map-reduce style.
- Targets "global sensemaking" questions over whole corpora (roughly the 1M-token range) that conventional top-k vector RAG structurally cannot answer, because no small set of chunks contains the answer.
- Reports substantial wins over vector RAG on comprehensiveness and diversity of answers for these corpus-level questions.
- arXiv v2 revised 2025-02-19; open-sourced as the microsoft/graphrag project.

## Connections

- [[concepts/context retrieval]]
- [[concepts/LLM-maintained knowledge bases]]
- [[operations/agent memory]]
- [[sources/HippoRAG]]

## Artifacts

- [[raw/papers/From Local to Global - A Graph RAG Approach to Query-Focused Summarization.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2404.16130
- Canonical graph-substrate paper for corpus-level knowledge — the graph end of the graph-vs-vector-vs-markdown memory substrate axis.
- Evaluation is LLM-judged pairwise comparison on comprehensiveness/diversity, not exact-match QA accuracy; the indexing stage carries significant upfront LLM cost.
