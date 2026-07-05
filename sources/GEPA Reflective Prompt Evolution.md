---
title: "GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning"
aliases:
  - "GEPA"
source_type: "paper"
kind: "prompt-optimization"
status: "verified"
year: 2025
publication_date: "2025-07-25"
publication_date_basis: "arxiv_abs_page"
source_updated_date: "2026-02-14"
source_updated_date_basis: "arxiv_latest_revision_date"
arxiv_id: "2507.19457"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Lakshya A Agrawal"
venue: "arXiv / ICLR 2026 (oral)"
url: "https://arxiv.org/abs/2507.19457"
pdf_url: "https://arxiv.org/pdf/2507.19457"
artifacts:
  - "raw/papers/GEPA - Reflective Prompt Evolution Can Outperform Reinforcement Learning.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# GEPA Reflective Prompt Evolution

## Summary

- Genetic prompt-evolution optimizer whose selection policy samples candidates from the Pareto frontier of per-instance scores across the system's own attempts, rather than iterating from a single global best — the paper argues this preserves complementary "lessons" and avoids premature convergence.
- Mutation is reflective: an LLM reads its own full trajectories (reasoning, tool calls, evaluator feedback) in natural language, diagnoses failures, and proposes targeted prompt edits — no weight updates involved.
- Outperforms GRPO-based RL by 6% on average and up to 20% while using up to 35x fewer rollouts (headline numbers revised down from 10% average in v1); beats the prompt optimizer MIPROv2 by over 10% across two LLMs, including +12% accuracy on AIME-2025.
- Also demonstrated as an inference-time search strategy for code optimization.
- v1 2025-07-25; latest revision 2026-02-14; accepted as an ICLR 2026 oral with released code (gepa-ai/gepa).

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Connections

- [[methods/self-improving code loops]]
- [[methods/agentic workflow search]]
- [[concepts/context evolution]]
- [[concepts/loop engineering]]
- [[sources/Darwin Godel Machine]]
- [[sources/AFlow]]

## Artifacts

- [[raw/papers/GEPA - Reflective Prompt Evolution Can Outperform Reinforcement Learning.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2507.19457
- Names the Pareto-frontier selection pattern explicitly — the key contrast with score-greedy selection in DGM/SICA-style loops.
- The RL comparison numbers were revised between versions (10% → 6% average); cite the latest revision, not v1.
