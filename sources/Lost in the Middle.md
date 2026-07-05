---
title: "Lost in the Middle: How Language Models Use Long Contexts"
aliases:
  - "Lost in the Middle"
source_type: "paper"
kind: "long-context-evaluation"
status: "verified"
year: 2023
publication_date: "2023-07-06"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2307.03172"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Nelson F. Liu"
  - "Kevin Lin"
  - "John Hewitt"
  - "Ashwin Paranjape"
  - "Michele Bevilacqua"
  - "Fabio Petroni"
  - "Percy Liang"
venue: "TACL 2024 / arXiv"
url: "https://arxiv.org/abs/2307.03172"
pdf_url: "https://arxiv.org/pdf/2307.03172"
artifacts:
  - "raw/papers/Lost in the Middle - How Language Models Use Long Contexts.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# Lost in the Middle

## Summary

- Documents U-shaped positional performance: models are best when relevant information sits at the beginning (primacy) or end (recency) of the context and degrade significantly when it sits in the middle — even for explicitly long-context models.
- Two controlled tasks isolate position effects: multi-document QA (permuting the position of the gold document among distractors) and synthetic key-value retrieval.
- Position alone can drop multi-document QA accuracy by roughly 20+ points mid-context; the paper carries 16 figures of position-sweep evidence.
- arXiv v1 2023-07-06, final 2023-11-20; published in TACL 2024.

## Claims

- [[claims/Claim - Context management is an agent architecture choice]]

## Connections

- [[concepts/context engineering]]
- [[concepts/context retrieval]]
- [[concepts/context compaction]]
- [[concepts/task-aware context pruning]]

## Artifacts

- [[raw/papers/Lost in the Middle - How Language Models Use Long Contexts.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2307.03172
- The canonical positional-degradation half of the "bigger windows don't remove memory needs" argument; pairs with the length-scaling evidence in [[sources/Context Rot]].
- Measured on 2023-era models; the U-shape's magnitude on current frontier models needs re-verification, though later work (Context Rot, 2025) confirms length-driven degradation persists.
