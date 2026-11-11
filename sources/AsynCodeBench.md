---
title: "AsynCodeBench: Benchmarking Collaboration of Asynchronous Multi-Agent Systems in Software Engineering"
aliases: ["AsynCodeBench"]
tags: [sources, multi-agent, code-factories]
source_type: "paper"
status: "verified"
evidence_class: "research-benchmark"
publication_date: "2026-09-26"
publication_date_basis: "arxiv_v1_submission_date"
source_version: "arxiv_v1"
arxiv_id: "2609.32662"
authors: ["Kaituo Zhang", "Zhen Xiong", "Zhimeng Jiang", "Mingyu Zhong", "Zhouyuan Yuan", "Zhecheng Li", "Bowen Lin", "Chia-Yuan Chang", "Mingzhi Hu", "Huazheng Wang", "Ying Lin"]
venue: "arXiv"
url: "https://arxiv.org/abs/2609.32662"
created: 2026-11-09
updated: 2026-11-09
---

# AsynCodeBench

## Contribution

Nineteen tasks from 16 repositories expose 52 validated dependencies. ADPR measures final dependency satisfaction; DRS measures first satisfaction at logical integration checkpoints, not elapsed time. Five protocols compare single-agent, serial, private asynchronous, and two manager variants using OpenHands and ten open-weight models.

## Evidence and Boundaries

Under the read-only-manager protocol, 32/190 model-task outcomes reach at least 80% test pass rate while resolving fewer than half their dependencies; 26 resolve none. Aggregate test progress can therefore hide incomplete integration.

The benchmark is small and curated. Protocol rankings depend on model and quality metric. DRS is unavailable for the single-agent condition, which exposes only a final workspace; token totals are not latency or dollar costs.

## Connections

- [[concepts/code factories]]
- [[concepts/evaluator reliability]]
- [[maps/Multi-Agent Systems Map]]

## Primary Link

[Full text v1, Sections 3–5 and Appendices B, E, H](https://arxiv.org/html/2609.32662v1).
