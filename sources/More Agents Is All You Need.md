---
title: "More Agents Is All You Need"
aliases:
  - "Agent Forest"
source_type: "paper"
kind: "ensemble-scaling"
status: "verified"
year: 2024
publication_date: "2024-02-03"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2402.05120"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Junyou Li"
  - "Qin Zhang"
  - "Yangbin Yu"
  - "Qiang Fu"
  - "Deheng Ye"
venue: "TMLR (arXiv 2402.05120), Tencent"
url: "https://arxiv.org/abs/2402.05120"
pdf_url: "https://arxiv.org/pdf/2402.05120"
artifacts:
  - "raw/papers/More Agents Is All You Need.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# More Agents Is All You Need

## Summary

- Simple sampling-and-voting ("Agent Forest"): LLM performance scales with the number of instantiated agents, orthogonal to other enhancement methods; ensembles tested up to 40 samples (10 for the more expensive debate baselines).
- Llama2-13B with 15 agents reaches 59% on GSM8K, beating single-query Llama2-70B (54%); GPT-3.5-Turbo with 20 agents reaches GPT-4 single-query level on GSM8K.
- GPT-3.5-Turbo gains at ensemble size 40: GSM8K 0.73 to 0.85 (+12pp), MATH 0.29 to 0.39 (+10pp), MMLU 0.59 to 0.70 (+11pp).
- Gain magnitude correlates with task difficulty: Llama2-13B shows roughly 69% relative gain on GSM8K vs roughly 200% on the harder MATH benchmark.
- Accepted at TMLR; v2 posted 2024-10-11; code publicly released.

## Claims

- [[claims/Claim - Coordination is a cost the task must justify]]

## Connections

- [[concepts/scaling with computation]]
- [[methods/multi-agent orchestration]]
- [[sources/Towards a Science of Scaling Agent Systems]]
- [[sources/Self-Consistency Improves Chain of Thought Reasoning]]

## Artifacts

- [[raw/papers/More Agents Is All You Need.pdf]]

## Notes

- Era note (2026-07-05): 2024 sampling-ensemble result on Llama2-era models; the scaling shape holds as lineage, the absolute numbers do not transfer. Voting gains are capped by error correlation ([[sources/Correlated Errors in Large Language Models]]). Live guidance: [[methods/debate and aggregation]].
- Canonical URL: https://arxiv.org/abs/2402.05120
- Canonical pro-scaling side of the agent-count debate: the empirical baseline that [[sources/Towards a Science of Scaling Agent Systems]] and later coordination-cost work correct. Listed under the "more agents are not automatically better" claim as the strongest counter-evidence, not as support.
- "Agents" here are independent samples of the same model aggregated by majority vote — no inter-agent communication — so results speak to inference-time sampling more than to coordinated multi-agent systems.
