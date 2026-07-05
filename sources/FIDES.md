---
title: "Securing AI Agents with Information-Flow Control (FIDES)"
aliases:
  - "FIDES"
source_type: "paper"
kind: "information-flow-control"
status: "verified"
year: 2025
publication_date: "2025-05-29"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2505.23643"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Manuel Costa"
  - "Boris Köpf"
  - "Aashish Kolluri"
  - "Andrew Paverd"
  - "Mark Russinovich"
  - "Ahmed Salem"
  - "Shruti Tople"
  - "Lukas Wutschitz"
  - "Santiago Zanella-Béguelin"
venue: "arXiv / Microsoft Research"
url: "https://arxiv.org/abs/2505.23643"
pdf_url: "https://arxiv.org/pdf/2505.23643"
artifacts:
  - "raw/papers/Securing AI Agents with Information-Flow Control (FIDES).pdf"
created: 2026-07-03
updated: 2026-07-05
---

# Securing AI Agents with Information-Flow Control (FIDES)

## Summary

- First formal model for reasoning about both security and expressiveness of agent planners; builds a taxonomy of tasks to characterize the security-utility trade-off of planner designs.
- The FIDES planner ("Flow Integrity Deterministic Enforcement System") attaches confidentiality and integrity labels to data and propagates them via dynamic taint tracking; policy enforcement is deterministic, not model-based.
- Enforces two invariants: tool calls must be based on trusted-integrity data, and data may only flow to recipients permitted to read it.
- Novel hide/unhide primitives for selectively removing information from the planner's context broaden the range of tasks completable securely versus strict taint tracking alone — demonstrated on AgentDojo.
- v1 2025-05-29, v2 2025-09-03; code and tutorial at github.com/microsoft/fides; authors include Azure CTO Mark Russinovich.

## Claims

- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[safety/prompt injection]]
- [[operations/agent harnesses]]
- [[operations/permissions]]
- [[sources/CaMeL]]
- [[sources/AgentDojo]]

## Artifacts

- [[raw/papers/Securing AI Agents with Information-Flow Control (FIDES).pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2505.23643
- Repository: https://github.com/microsoft/fides
- The information-flow-control counterpart to CaMeL: same deterministic-enforcement premise, but framed as labels plus invariants, with hide/unhide primitives to recover task expressiveness.
