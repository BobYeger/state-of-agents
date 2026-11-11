---
title: "Rethinking Verification in Agent Harnesses"
aliases: ["Verification placement in agent harnesses"]
tags: [sources, harnesses, verification]
source_type: "paper"
status: "verified"
evidence_class: "research-benchmark"
publication_date: "2026-10-25"
publication_date_basis: "arxiv_v1_submission_date"
source_version: "arxiv_v1"
arxiv_id: "2610.34577"
authors: ["Zhengxin Zhang", "Erkang Zhu", "Yin Lin", "Claire Cardie", "Bolin Ding", "Jingren Zhou"]
venue: "arXiv"
url: "https://arxiv.org/abs/2610.34577"
discovery_url: "https://academy.dair.ai/papers/rethinking-verification-in-agent-harnesses-2610.34577"
created: 2026-11-09
updated: 2026-11-09
---

# Rethinking Verification in Agent Harnesses

## Design and Evidence

Seventeen designs compare instructions, reminders, completion self-check prompts, and independent review across seven coding models. Automatic graders evaluate selected TB/SWE tasks; three trials are configured per model/task. TB contains 31 tasks; SWE begins with 30 before adjustment. Qwen3.7-Plus critiques from fresh context with sandbox access but cannot edit deliverables.

Instructions/reminders give modest, model-dependent gains. Rejection gates cost more. Critics add 5.9–9.5/3.9–6.6 percentage points on TB/SWE at 1.13–1.25/1.00–1.04× baseline model cost, including revision.

VisualBench uses 18 internal tasks, two configured trials, and blinded human comparisons; critic net preference is +13.2–23.8 points, not automatic correctness.

## Limits

Model pricing and selected tasks constrain transfer. Early gates trigger at 80% of task deadlines; no uniform cap is specified. Critic width runs sequentially. Completion self-checking is distinct from objective CI gates.

## Connections

- [[concepts/evaluator reliability]]
- [[reports/Code Factories Update - 2026-11-09]]

[Primary methods, results, and execution rules](https://arxiv.org/html/2610.34577v1).
