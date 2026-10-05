---
title: "RouteLLM: Learning to Route LLMs with Preference Data"
aliases:
  - "RouteLLM"
source_type: "paper"
kind: "preference-trained-model-routing"
status: "verified"
year: 2024
publication_date: "2024-06-26"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: "2025-02-23"
source_updated_date_basis: "arxiv_v4_revision_date"
source_version: "arxiv_v4"
arxiv_id: "2406.18665"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Isaac Ong"
  - "Amjad Almahairi"
  - "Vincent Wu"
  - "Wei-Lin Chiang"
  - "Tianhao Wu"
  - "Joseph E. Gonzalez"
  - "M Waleed Kadous"
  - "Ion Stoica"
venue: "ICLR 2025"
url: "https://arxiv.org/abs/2406.18665"
pdf_url: "https://arxiv.org/pdf/2406.18665v4"
evidence_class: "controlled-benchmark-experiments"
metrics_status: "query-routing-quality-and-model-call-tradeoffs"
artifacts: []
created: 2026-10-05
updated: 2026-10-05
---

# RouteLLM

## Contribution

Trains routers from preference comparisons to select a strong or weak model before generation. A threshold controls the quality–cost tradeoff. Unlike a cascade, it chooses one answering model per query; unlike an advisor, it does not return guidance to an ongoing executor.

## Evidence

With augmented preference data, the matrix-factorization router reaches 80% of the weak-to-strong performance gap on MT Bench using 31.31% strong-model calls, versus 78.08% for random routing (Table 1). Tests also cover MMLU, GSM8K, and transfer to unseen model pairs.

## Boundaries

Recovering 80% of a performance gap is not 80% absolute accuracy. Arena-only routers perform near or below random on MMLU/GSM8K; augmentation changes the result. This is query-level routing evidence, not proof of reliable consultation during long agent trajectories.

## Connections

- [[methods/runtime routing]]
- [[concepts/advisor agents]]
- [[operations/cost control]]
- [[sources/FrugalGPT]]
- [[sources/Think Big Search Small]]

## Primary Links

- [Submission and revision history](https://arxiv.org/abs/2406.18665)
- [Full text, v4, sections 3–5](https://arxiv.org/html/2406.18665v4)
- [ICLR paper](https://openreview.net/pdf?id=8sSqNntaMr)
