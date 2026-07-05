---
title: "HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models"
aliases:
  - "HippoRAG"
source_type: "paper"
kind: "kg-retrieval"
status: "verified"
year: 2024
publication_date: "2024-05-23"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2405.14831"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Bernal Jiménez Gutiérrez"
  - "Yiheng Shu"
  - "Yu Gu"
  - "Michihiro Yasunaga"
  - "Yu Su"
venue: "NeurIPS 2024 / arXiv (Ohio State / Stanford)"
url: "https://arxiv.org/abs/2405.14831"
pdf_url: "https://arxiv.org/pdf/2405.14831"
artifacts:
  - "raw/papers/HippoRAG - Neurobiologically Inspired Long-Term Memory for Large Language Models.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# HippoRAG

## Summary

- Models long-term memory on hippocampal indexing theory: an LLM-built open knowledge graph acts as the "index", and Personalized PageRank performs single-step multi-hop retrieval over it.
- Up to 20% improvement over state-of-the-art retrieval methods on multi-hop QA.
- Matches or beats iterative retrieval (IRCoT) while being 10-30x cheaper and 6-13x faster at query time — single-step graph traversal replaces repeated LLM retrieval rounds.
- Combining HippoRAG with IRCoT yields further substantial gains, showing the substrate and the retrieval control loop compose rather than compete.

## Connections

- [[concepts/context retrieval]]
- [[operations/agent memory]]

## Artifacts

- [[raw/papers/HippoRAG - Neurobiologically Inspired Long-Term Memory for Large Language Models.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2405.14831
- The KG+PageRank substrate most later memory papers benchmark against; its single-step-vs-iterative cost numbers are core evidence in the graph-vs-vector substrate tradeoff.
- Evaluated on multi-hop QA corpora, not conversational agent memory; substrate conclusions transfer with that caveat.
