---
title: "Generative Agents: Interactive Simulacra of Human Behavior"
aliases:
  - "Generative Agents"
  - "Smallville"
source_type: "paper"
kind: "agent-simulation"
status: "verified"
year: 2023
publication_date: "2023-04-07"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2304.03442"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Joon Sung Park"
  - "Joseph C. O'Brien"
  - "Carrie J. Cai"
  - "Meredith Ringel Morris"
  - "Percy Liang"
  - "Michael S. Bernstein"
venue: "UIST 2023 / arXiv"
url: "https://arxiv.org/abs/2304.03442"
pdf_url: "https://arxiv.org/pdf/2304.03442"
artifacts:
  - "raw/papers/Generative Agents - Interactive Simulacra of Human Behavior.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# Generative Agents

## Summary

- Architecture combines a memory stream (complete natural-language record of experiences), retrieval scored by recency, importance, and relevance, reflection (synthesizing memories into higher-level inferences), and planning.
- Instantiated 25 agents in Smallville, a Sims-inspired sandbox town; agents perceive, converse, and act through the environment rather than direct agent-to-agent APIs.
- Emergence demonstration: from a single seeded intention (one agent wants to host a Valentine's Day party), agents autonomously spread invitations, formed new acquaintances, coordinated dates, and attended together over two in-game days.
- Ablations show observation, planning, and reflection each contribute critically to behavioral believability.
- arXiv v1 2023-04-07, revised 2023-08-06; published at UIST 2023.

## Connections

- [[operations/agent memory]]
- [[concepts/multi-agent systems]]
- [[concepts/dreaming and memory consolidation]]

## Artifacts

- [[raw/papers/Generative Agents - Interactive Simulacra of Human Behavior.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2304.03442
- Origin of the recency-importance-relevance retrieval triple that most subsequent agent memory scorers reuse, and of reflection as a memory-consolidation step.
- Results are about behavioral believability in a social simulation, not task performance; transfer of the retrieval triple to task agents is by adoption, not evidence in this paper.
