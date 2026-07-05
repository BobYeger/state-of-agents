---
title: "Should we be going MAD? A Look at Multi-Agent Debate Strategies for LLMs"
aliases:
  - "Going MAD"
source_type: "paper"
kind: "debate-evaluation"
status: "verified"
year: 2023
publication_date: "2023-11-29"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2311.17371"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Andries Smit"
  - "Paul Duckworth"
  - "Nathan Grinsztajn"
  - "Thomas D. Barrett"
  - "Arnu Pretorius"
venue: "arXiv / ICML 2024 (InstaDeep)"
url: "https://arxiv.org/abs/2311.17371"
pdf_url: "https://arxiv.org/pdf/2311.17371"
artifacts:
  - "raw/papers/Should we be going MAD A Look at Multi-Agent Debate Strategies for LLMs.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# Should We Be Going MAD

## Summary

- First systematic benchmark of debate protocols against alternatives on cost, time, and accuracy: multi-agent debating systems "in their current form do not reliably outperform" self-consistency and ensembling with multiple reasoning paths.
- After hyperparameter tuning, some debate systems (notably Multi-Persona) do achieve superior performance — the gap is tuning sensitivity, not inherent inferiority.
- Named mechanism: adjusting agent agreement levels ("agreement modulation") "can significantly enhance performance and even surpass all other non-debate protocols" — a direct lever against sycophancy and premature consensus.
- Released an open-source repository with implementations of the protocols and evaluation scripts across standard reasoning datasets.
- Latest arXiv revision 2024-07-18; presented at ICML 2024 (poster 34657).

## Claims

- [[claims/Claim - Coordination is a cost the task must justify]]

## Connections

- [[methods/multi-agent orchestration]]
- [[operations/agent evals]]
- [[operations/cost control]]
- [[sources/Multiagent Debate Improves Factuality and Reasoning]]
- [[sources/Self-Consistency Improves Chain of Thought Reasoning]]

## Artifacts

- [[raw/papers/Should we be going MAD A Look at Multi-Agent Debate Strategies for LLMs.pdf]]

## Notes

- Era note (2026-07-05): one of the two evaluations that settled the debate-era question (debate does not reliably beat self-consistency and ensembling at matched cost); its agreement-modulation lever remains cited. Read as settled evidence, not an open controversy. Live guidance: [[methods/debate and aggregation]].
- Canonical URL: https://arxiv.org/abs/2311.17371
- The measured counterweight to Du et al.: gives harness designers a decision rule (debate vs self-consistency vs ensembling under a budget) plus the one tunable knob (agreement level) that makes debate pay off.
