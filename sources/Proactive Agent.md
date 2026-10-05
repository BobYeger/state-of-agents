---
title: "Proactive Agent: Shifting LLM Agents from Reactive Responses to Active Assistance"
aliases:
  - "Proactive Agent"
  - "ProactiveBench 2024"
source_type: "paper"
kind: "proactive-assistance-and-intervention-timing"
status: "verified"
year: 2024
publication_date: "2024-10-16"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: "2024-12-03"
source_updated_date_basis: "arxiv_v3_revision_date"
source_version: "arxiv_v3"
arxiv_id: "2410.12361"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Yaxi Lu"
  - "Shenzhi Yang"
  - "Cheng Qian"
  - "Guirong Chen"
  - "Qinyu Luo"
  - "Yesai Wu"
  - "Huadong Wang"
  - "Xin Cong"
  - "Zhong Zhang"
  - "Yankai Lin"
  - "Weiwen Liu"
  - "Yasheng Wang"
  - "Zhiyuan Liu"
  - "Fangming Liu"
  - "Maosong Sun"
venue: "arXiv; ICLR 2025"
url: "https://arxiv.org/abs/2410.12361"
pdf_url: "https://arxiv.org/pdf/2410.12361v3"
evidence_class: "benchmark-and-finetuning-experiments"
metrics_status: "reward-model-evaluated-assistance-predictions"
artifacts: []
created: 2026-10-05
updated: 2026-10-05
---

# Proactive Agent

## Contribution

Predicts possible assistance from user activity, environment events, and state, including the option to remain silent. This makes initiating interaction an evaluated capability rather than a consequence of running asynchronously.

## Evidence

ProactiveBench combines 6,790 generated training events with 233 real-world-derived test events. Qwen2-7B-Proactive reaches 66.47% F1 versus 60.74% before tuning (Table 3). Its precision remains 49.78%; the paper's false-alarm measure is 50.22%. More initiative therefore does not imply well-timed assistance.

## Boundaries

Evaluation uses a learned reward model as a proxy for acceptance. Training relies on simulated users and environments; the test set is small. The results do not establish long-term user benefit, reliable autonomous execution, or acceptable interruption rates in deployment. This ProactiveBench differs from similarly named later benchmarks.

## Connections

- [[concepts/background agents]]
- [[concepts/event-driven agents]]
- [[concepts/human-in-the-loop agents]]
- [[sources/ProAgentBench]]

## Primary Links

- [Submission and revision history](https://arxiv.org/abs/2410.12361)
- [Full text, v3, sections 3–4 and Tables 1–3](https://arxiv.org/html/2410.12361v3)
- [ICLR paper](https://openreview.net/pdf?id=sRIU6k2TcU)
- [Author code and data](https://github.com/thunlp/ProactiveAgent)
