---
title: "ProAgentBench: Evaluating LLM Agents for Proactive Assistance with Real-World Data"
aliases:
  - "ProAgentBench"
source_type: "paper"
kind: "proactive-assistance-benchmark"
status: "verified"
year: 2026
publication_date: "2026-02-04"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: "2026-02-09"
source_updated_date_basis: "arxiv_v2_revision_date"
source_version: "arxiv_v2"
arxiv_id: "2602.04482"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Yuanbo Tang"
  - "Huaze Tang"
  - "Tingyu Cao"
  - "Lam Nguyen"
  - "Anping Zhang"
  - "Xinwen Cao"
  - "Chunkang Liu"
  - "Wenbo Ding"
  - "Yang Li"
venue: "arXiv"
url: "https://arxiv.org/abs/2602.04482"
pdf_url: "https://arxiv.org/pdf/2602.04482v2"
evidence_class: "observational-workflow-dataset-and-offline-experiments"
metrics_status: "timing-and-content-prediction-not-live-productivity"
artifacts: []
created: 2026-10-05
updated: 2026-10-05
---

# ProAgentBench

## Contribution

Separates when to offer assistance from what to offer, using continuous user workflow records. The dataset contains 28,528 events, including 7,222 LLM-related events, from over 500 hours. Evaluation isolates users and splits by time.

## Evidence

With equal-sized training sets, Llama-3.1-8B supervised tuning on real observations achieves 74.0% timing accuracy, versus 62.1% on synthetic data and 57.3% zero-shot (Table 3). Context and memory ablations test the information needed before intervention.

## Boundaries

The population is primarily students, annotations use a VLM, and privacy filtering removes some workflows. Predicting recorded LLM use or matching a user's query is not a causal demonstration that unsolicited intervention helps. These are offline results; timing, content, interruption burden, and completed-task value still need joint evaluation in use.

## Connections

- [[concepts/background agents]]
- [[concepts/event-driven agents]]
- [[concepts/human-in-the-loop agents]]
- [[sources/Proactive Agent]]

## Primary Links

- [Submission and revision history](https://arxiv.org/abs/2602.04482)
- [Full text, v2, sections 3–6, Table 3, and limitations](https://arxiv.org/html/2602.04482v2)
