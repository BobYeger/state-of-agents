---
title: "OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments"
aliases:
  - "OSWorld"
source_type: "paper"
kind: "computer-use-benchmark"
status: "verified"
year: 2024
publication_date: "2024-04-11"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: "2024-05-30"
source_updated_date_basis: "arxiv_v2_revision_date"
source_version: "arxiv_v2"
arxiv_id: "2404.07972"
authors:
  - "Tianbao Xie"
  - "Danyang Zhang"
  - "Jixuan Chen"
  - "Xiaochuan Li"
  - "Siheng Zhao"
  - "Ruisheng Cao"
  - "Toh Jing Hua"
  - "Zhoujun Cheng"
  - "Dongchan Shin"
  - "Fangyu Lei"
  - "Yitao Liu"
  - "Yiheng Xu"
  - "Shuyan Zhou"
  - "Silvio Savarese"
  - "Caiming Xiong"
  - "Victor Zhong"
  - "Tao Yu"
venue: "arXiv; NeurIPS 2024 Datasets and Benchmarks"
url: "https://arxiv.org/abs/2404.07972"
pdf_url: "https://arxiv.org/pdf/2404.07972v2"
evidence_class: "computer-use-environment-and-benchmark-experiments"
artifacts: []
created: 2026-10-05
updated: 2026-10-05
---

# OSWorld

## Contribution

Introduces a real-computer environment and 369 tasks spanning desktop applications, browser work, files, and multi-application workflows. Initial-state setup and executable evaluators check resulting state, permitting different action sequences to satisfy a task. This complements offline next-action prediction in [[sources/Mind2Web]].

## Evidence and Boundaries

The 2024 experiments compare observation formats and examine interface grounding, operational knowledge, window perturbations, and trajectory history. Their low baseline scores describe those models and budgets, not current capability. Desktop task completion also leaves personal-assistant questions unmeasured: useful initiative, evolving preferences, interruption cost, and honoring commitments over weeks.

Record the benchmark version, environment, observation/action interfaces, step budget, and grading rules. Later OSWorld releases and OSWorld2.0 are distinct evaluation configurations; results must not be silently compared with this original paper. No reviewed evidence establishes that all current personal-agent products use this benchmark or its methods.

## Connections

- [[concepts/persistent personal agents]]
- [[systems/personal assistant agents]]
- [[benchmarks/agent evaluation]]
- [[concepts/agent loop]]
- [[sources/Mind2Web]]

## Primary Reading

- [Versioned full text](https://arxiv.org/html/2404.07972v2), sections 2–5.
- [Author project](https://os-world.github.io/) and [benchmark repository](https://github.com/xlang-ai/OSWorld).
