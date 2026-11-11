---
title: "Auto-Dreamer: Learning Offline Memory Consolidation for Language Agents"
aliases:
  - "Auto-Dreamer"
source_type: "paper"
kind: "learned-offline-memory-consolidation"
status: "verified"
year: 2026
publication_date: "2026-05-20"
publication_date_basis: "arxiv_v1_submission_date"
source_version: "arxiv_v1"
arxiv_id: "2605.20616"
authors:
  - "Chongrui Ye"
  - "Yuxiang Liu"
  - "Yu Wang"
  - "Haofei Yu"
  - "Yining Zhao"
  - "Ge Liu"
  - "Julian McAuley"
  - "Jiaxuan You"
venue: "arXiv"
url: "https://arxiv.org/abs/2605.20616"
pdf_url: "https://arxiv.org/pdf/2605.20616v1"
evidence_class: "author-run-research-experiments"
metrics_status: "author-reported"
created: 2026-11-09
updated: 2026-11-09
---

# Auto-Dreamer

## Mechanism and Evidence

A GRPO-trained consolidator reads a selected memory region and provenance-linked trajectories, then replaces that region with synthesized entries. The task agent, writer, and retriever stay fixed; deployment changes the bank, not model parameters.

ScienceWorld training transfers to ALFWorld and a WebArena subset. With the Qwen3.5-9B ScienceWorld task agent, Table 1 reports 41.1% success versus UMEM's 34.1%, with 6,947 versus 80,918 active-bank tokens. Fixed-bank experiments isolate consolidation from acquisition.

## Boundaries

Active-bank size excludes training, consolidation, and trajectory-storage costs. Top-three retrieval favors compact banks. Appendix H supplies task-bootstrap intervals, but no seed or task-order variance; small ALFWorld/WebArena margins should not be treated as decisive. This is an earlier omission, not a November release.

## Reading

[Full text, Table 1 and Appendices A/H](https://arxiv.org/html/2605.20616v1); [submission history](https://arxiv.org/abs/2605.20616).

## Connections

- [[concepts/dreaming and memory consolidation]]
- [[concepts/procedural memory]]
- [[concepts/harness-aware agent learning]]
- [[reports/Memory and Dreaming Update - 2026-11-09]]
