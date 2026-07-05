---
title: "Mixture-of-Agents Enhances Large Language Model Capabilities"
aliases:
  - "MoA"
source_type: "paper"
kind: "layered-aggregation"
status: "verified"
year: 2024
publication_date: "2024-06-07"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2406.04692"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Junlin Wang"
  - "Jue Wang"
  - "Ben Athiwaratkun"
  - "Ce Zhang"
  - "James Zou"
venue: "arXiv / ICLR 2025 Spotlight (Together AI / Duke / Stanford)"
url: "https://arxiv.org/abs/2406.04692"
pdf_url: "https://arxiv.org/pdf/2406.04692"
artifacts:
  - "raw/papers/Mixture-of-Agents Enhances Large Language Model Capabilities.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# Mixture-of-Agents

## Summary

- Layered aggregation architecture: each layer contains multiple LLM agents, and each agent takes all outputs from the previous layer as auxiliary information when generating its response — aggregation by regeneration rather than by voting.
- Using only open-source models, MoA scored 65.1% on AlpacaEval 2.0 vs 57.5% for GPT-4 Omni, topping the leaderboard "by a substantial gap"; also evaluated on MT-Bench and FLASK.
- Documents the "collaborativeness of LLMs" phenomenon: models generate better responses when shown other models' outputs, even when those auxiliary outputs are individually worse.
- Accepted at ICLR 2025 as a Spotlight (OpenReview forum h0ZfDIrj7T; proceedings entry published 2025-01-22).

## Connections

- [[concepts/scaling with computation]]
- [[methods/multi-agent orchestration]]
- [[sources/OpenRouter Fusion Beats Frontier]]
- [[sources/X-MAS]]
- [[sources/Self-Consistency Improves Chain of Thought Reasoning]]

## Artifacts

- [[raw/papers/Mixture-of-Agents Enhances Large Language Model Capabilities.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2406.04692
- Canonical citation for the mixture-of-agents layering pattern: synthesis-style aggregation beating both voting and any single frontier model.
- Headline result is on AlpacaEval 2.0 (LLM-judged, length-controlled win rate), not on agentic or tool-use tasks; transfer to agent harnesses is an open question.
