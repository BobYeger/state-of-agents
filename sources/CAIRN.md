---
title: "CAIRN: Dynamic Fact–Intent DAGs for Multi-Agent Exploration"
aliases: ["CAIRN", "Cairn fact–intent coordination"]
source_type: "paper"
status: "verified"
publication_date: "2026-09-26"
publication_date_basis: "arxiv_v1_submission_date"
source_version: "arxiv_v1"
arxiv_id: "2609.32700"
authors: ["Zuyao Xu", "Yuyang Jia", "Junwei Guan", "Xiang Li", "Kaiwen Shen", "Zhiqiang Dong"]
venue: "arXiv"
url: "https://arxiv.org/abs/2609.32700"
evidence_class: "author-run-controlled-benchmark"
metrics_status: "author-reported"
created: 2026-11-09
updated: 2026-11-09
tags: [research, multi-agent, cyber, shared-memory]
---

# CAIRN

A reasoner proposes investigations from a persistent fact–intent graph; workers return findings that support later branches. Recorded “facts” remain agent claims, not independently verified truth. [Author implementation](https://github.com/oritera/Cairn).

## Evidence and Limits

Same GLM-5.1 model, Pi 0.85.1 loop, isolated environments, and five-hour limits; CAIRN changes prompts/tools and uses up to six shared reasoner/worker slots. Evaluation includes 12 public FrontierMath problems and 40 Cybench tasks.

On Cybench, direct execution finishes sooner on 30/40 tasks: mean 7.31 versus 8.49 minutes, using 0.83M versus 3.22M tokens. The headline 76.5% faster result concerns 17 high-effort tasks pooled across both benchmarks, grouped by observed baseline token consumption. It is not a general cyber success rate or a prospective routing rule. Concurrency examples use one math problem; the paper does not clearly specify a uniform repetition count.

This September architecture study is separate from October observations of criminal use. It does not establish the models, versions, or success of those deployments.

[Primary methods and results, Sections 2–4 and Appendix D](https://arxiv.org/html/2609.32700v1).

## Connections

- [[concepts/shared agent memory]]
- [[methods/multi-agent orchestration]]
- [[benchmarks/multi-agent benchmarks]]
