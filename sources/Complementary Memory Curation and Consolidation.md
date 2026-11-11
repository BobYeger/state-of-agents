---
title: "Long-Term Agent Memory through Complementary Curation and Consolidation"
aliases:
  - "Complementary Memory Curation and Consolidation"
source_type: "paper"
kind: "hybrid-memory-consolidation"
status: "verified"
year: 2026
publication_date: "2026-10-29"
publication_date_basis: "arxiv_v1_submission_date"
source_version: "arxiv_v1"
arxiv_id: "2610.39790"
authors:
  - "Abhishek Gupta"
  - "Dongge Han"
  - "Daniel Madrigal Diaz"
  - "Wei-Ning Chen"
  - "Mayukh Das"
  - "Victor Rühle"
  - "Saravan Rajmohan"
venue: "arXiv"
url: "https://arxiv.org/abs/2610.39790"
pdf_url: "https://arxiv.org/pdf/2610.39790v1"
evidence_class: "author-run-research-experiments"
metrics_status: "author-reported"
created: 2026-11-09
updated: 2026-11-09
---

# Complementary Memory Curation and Consolidation

## Mechanism and Evidence

Combines timestamped episodic summaries with contextualized relational tuples. After session-level curation, clustering supplies candidates for LLM merging/deletion; retrieval searches both stores.

With GPT-4.1-mini, the unconsolidated hybrid scores 90.2% on LoCoMo's LLM judge and 85.5% on LongMemEval-S. Consolidation reduces the LoCoMo score to 89.2%, alongside reported 16.34% store compression. Full-context LoCoMo scores 91.3% with that backbone. Therefore the headline score is neither a consolidation gain nor superiority over full context.

## Boundaries

Several baseline scores are imported from earlier work. QA evidence is restricted to text conversations, model choice matters, and memory size is not lifecycle cost. The useful contribution is the measured representation/compression trade-off.

## Reading

[Full text, Tables 1–5 and limitations](https://arxiv.org/html/2610.39790v1); [metadata](https://arxiv.org/abs/2610.39790).

## Connections

- [[concepts/dreaming and memory consolidation]]
- [[benchmarks/agent memory benchmarks]]
- [[reports/Memory and Dreaming Update - 2026-11-09]]
