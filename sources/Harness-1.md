---
title: "Harness-1: Reinforcement Learning for Search Agents with State-Externalizing Harnesses"
aliases:
  - "Harness-1"
source_type: "paper"
kind: "harness-engineering"
status: "verified"
year: 2026
publication_date: "2026-06-01"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: null
source_updated_date_basis: null
arxiv_id: "2606.02373"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors: []
venue: "arXiv"
url: "https://arxiv.org/abs/2606.02373"
pdf_url: "https://arxiv.org/pdf/2606.02373"
artifacts:
  - "raw/papers/Harness-1 - Reinforcement Learning for Search Agents with State-Externalizing Harnesses.pdf"
created: 2026-07-01
updated: 2026-07-01
---

# Harness-1: Reinforcement Learning for Search Agents with State-Externalizing Harnesses

## Summary

- Search-agent paper centered on a state-externalizing harness rather than only a better prompt or model.
- The harness keeps working memory, evidence links, verification records, compressed and deduplicated observations, and budget-aware context rendering outside the model.
- Important because it makes harness state into a trainable and inspectable control surface for search agents.
- Strong fit for the talk thesis: capable agents increasingly depend on designed loop substrate: memory, state, evidence, budget, and verification.

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
- [[claims/Claim - Context management is an agent architecture choice]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[maps/Harness Tracker]]
- [[maps/Context Management Map]]
- [[operations/agent harnesses]]
- [[operations/agent memory]]
- [[operations/agent evals]]
- [[concepts/context engineering]]

## Artifacts

- [[raw/papers/Harness-1 - Reinforcement Learning for Search Agents with State-Externalizing Harnesses.pdf]]

## Notes

- Canonical arXiv URL: https://arxiv.org/abs/2606.02373
- arXiv metadata: submitted June 1, 2026.
- Main vault use: evidence that harnesses can be the locus of learning and performance, not just the environment around the model.
