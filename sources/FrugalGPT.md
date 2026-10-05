---
title: "FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance"
aliases:
  - "FrugalGPT"
source_type: "paper"
kind: "cost-aware-model-cascades"
status: "verified"
year: 2023
publication_date: "2023-05-09"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: "2023-05-09"
source_updated_date_basis: "arxiv_v1_submission_date"
source_version: "arxiv_v1"
arxiv_id: "2305.05176"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Lingjiao Chen"
  - "Matei Zaharia"
  - "James Zou"
venue: "arXiv"
url: "https://arxiv.org/abs/2305.05176"
pdf_url: "https://arxiv.org/pdf/2305.05176v1"
evidence_class: "controlled-benchmark-experiments"
metrics_status: "historical-models-and-prices-task-specific-results"
artifacts: []
created: 2026-10-05
updated: 2026-10-05
---

# FrugalGPT

## Contribution

Learns a sequence of model calls and answer-quality thresholds under a budget. An accepted answer ends the cascade; otherwise another model is queried. It is an antecedent to conditional spending on stronger reasoning, rather than an executor asking an advisor for advice.

## Evidence

The v1 experiments use twelve APIs and three datasets. Table 3 reports cost savings at the best individual model's accuracy of 98.3% on HEADLINES, 73.3% on OVERRULING, and 59.2% on the adapted CoQA task. These are separate dataset results, not a universal saving.

## Boundaries

The learned scorer needs labeled, distribution-relevant training examples. Costs reflect March 2023 APIs; training overhead and sequential latency matter. The study does not test ongoing tool-using agents or autonomous consultation timing.

## Connections

- [[methods/runtime routing]]
- [[concepts/advisor agents]]
- [[operations/cost control]]
- [[sources/RouteLLM]]
- [[sources/Claude Advisor Tool]]

## Primary Links

- [Submission record](https://arxiv.org/abs/2305.05176)
- [Full text, v1, sections 3–5 and Table 3](https://arxiv.org/html/2305.05176v1)
