---
title: "Stop Overvaluing Multi-Agent Debate — We Must Rethink Evaluation and Embrace Model Heterogeneity"
aliases:
  - "If Multi-Agent Debate is the Answer, What is the Question?"
source_type: "paper"
kind: "debate-critique"
status: "verified"
year: 2025
publication_date: "2025-02-12"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2502.08788"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Hangfan Zhang"
  - "Zhiyao Cui"
  - "Jianhao Chen"
  - "Xinrun Wang"
  - "Qiaosheng Zhang"
  - "Zhen Wang"
  - "Dinghao Wu"
  - "Shuyue Hu"
venue: "arXiv (Penn State / Shanghai AI Lab / NWPU / SMU)"
url: "https://arxiv.org/abs/2502.08788"
pdf_url: "https://arxiv.org/pdf/2502.08788"
artifacts:
  - "raw/papers/Stop Overvaluing Multi-Agent Debate - We Must Rethink Evaluation and Embrace Model Heterogeneity.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# Stop Overvaluing Multi-Agent Debate

## Summary

- Systematic evaluation of 5 representative multi-agent debate (MAD) methods across 9 benchmarks and 4 foundation models under matched conditions.
- Headline finding: MAD methods "often fail to outperform simple single-agent baselines such as Chain-of-Thought and Self-Consistency, even when consuming significantly more inference-time computation."
- Identifies model heterogeneity (mixing different base models among debaters) as "a universal antidote" that consistently improves current MAD frameworks — converging with X-MAS from the framework-design side.
- Retitled between versions: v1 (2025-02-12) "If Multi-Agent Debate is the Answer, What is the Question?"; v3 (2025-06-21) "Stop Overvaluing Multi-Agent Debate" — one paper, not two.

## Claims

- [[claims/Claim - Coordination is a cost the task must justify]]

## Connections

- [[methods/multi-agent orchestration]]
- [[operations/agent evals]]
- [[sources/X-MAS]]
- [[sources/Why Do Multi-Agent LLM Systems Fail]]
- [[sources/Multiagent Debate Improves Factuality and Reasoning]]
- [[sources/Self-Consistency Improves Chain of Thought Reasoning]]

## Artifacts

- [[raw/papers/Stop Overvaluing Multi-Agent Debate - We Must Rethink Evaluation and Embrace Model Heterogeneity.pdf]]

## Notes

- Era note (2026-07-05): one of the two evaluations that settled the debate-era question; its model-heterogeneity antidote remains cited. Read as settled evidence, not an open controversy. Live guidance: [[methods/debate and aggregation]].
- Canonical URL: https://arxiv.org/abs/2502.08788
- The most-cited critical evaluation of MAD: compute-matched evidence on when debate converges vs entrenches, with an actionable fix (heterogeneous debaters).
- Beware duplicate citations under the v1 title; both titles resolve to arXiv 2502.08788.
