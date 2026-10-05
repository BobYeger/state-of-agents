---
title: "Mind2Web: Towards a Generalist Agent for the Web"
aliases:
  - "Mind2Web"
  - "MindAct"
source_type: "paper"
kind: "web-agent-grounding-benchmark"
status: "verified"
year: 2023
publication_date: "2023-06-09"
publication_date_basis: "arxiv_v1_submission_history"
source_updated_date: "2023-12-09"
source_updated_date_basis: "arxiv_v3_submission_history"
source_version: "Original Mind2Web paper, arXiv v3 and NeurIPS 2023 proceedings; inspected October 5, 2026"
arxiv_id: "2306.06070"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "not assessed"
authors:
  - "Xiang Deng"
  - "Yu Gu"
  - "Boyuan Zheng"
  - "Shijie Chen"
  - "Samuel Stevens"
  - "Boshi Wang"
  - "Huan Sun"
  - "Yu Su"
venue: "NeurIPS 2023 Datasets and Benchmarks / The Ohio State University"
url: "https://arxiv.org/abs/2306.06070"
pdf_url: "https://arxiv.org/pdf/2306.06070v3"
license: "arXiv non-exclusive distribution"
license_url: "https://arxiv.org/licenses/nonexclusive-distrib/1.0/"
evidence_class: "peer-reviewed-web-agent-dataset-and-controlled-baseline-evaluation"
artifacts: []
created: 2026-10-05
updated: 2026-10-05
---

# Mind2Web

## Summary

- The original 2023 dataset contains 2,350 tasks from 137 real websites across 31 domains, with demonstrated actions and webpage snapshots. Splits test new tasks, websites, and domains separately.
- MindAct first ranks candidate page elements with a smaller model, then asks an LLM to select an element and operation. Observation filtering and action grounding are architectural components, not simply larger-model capabilities.
- This is an early research reference for browser agents using high-level goals and heterogeneous websites. It predates current managed browser services; that chronology does not establish a service's direct research lineage.

## Evidence Boundary

Each step is evaluated independently with **ground-truth previous actions**. The reported whole-task success requires every annotated step to match; it is not a live end-to-end completion test with the agent's own errors, recovery, or alternative valid routes.

The original MindAct uses textual page information, with limited interaction-dynamics modeling. English websites popular in the United States and MTurk demonstrations constrain representation. Keep this original benchmark distinct from later online or multimodal Mind2Web variants.

## Connections

- [[concepts/agent loop]]
- [[concepts/tool use]]
- [[concepts/computer use]]
- [[benchmarks/agent evaluation]]
- [[sources/ReAct]]
- [[sources/Does Learning to Predict the World Help Agents Act]]

## Sources

- [Versioned full text](https://arxiv.org/html/2306.06070v3), sections 2–4 and 6.
- [Submission history](https://arxiv.org/abs/2306.06070).
- [NeurIPS 2023 paper](https://proceedings.neurips.cc/paper_files/paper/2023/file/5950bf290a1570ea401bf98882128160-Paper-Datasets_and_Benchmarks.pdf).
- [Authors' project](https://osu-nlp-group.github.io/Mind2Web/).
