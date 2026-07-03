---
title: "Sabotage Evaluations for Frontier Models"
aliases: []
source_type: "paper"
kind: "sabotage-evaluation"
status: "verified"
year: 2024
publication_date: "2024-10-28"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2410.21514"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Joe Benton"
  - "Misha Wagner"
  - "Eric Christiansen"
  - "Cem Anil"
  - "Ethan Perez"
venue: "arXiv / Anthropic"
url: "https://arxiv.org/abs/2410.21514"
pdf_url: "https://arxiv.org/pdf/2410.21514"
created: 2026-07-03
updated: 2026-07-03
---

# Sabotage Evaluations for Frontier Models

## Summary

- Defines four sabotage capability families: human decision sabotage, code sabotage, sandbagging (hiding capabilities during evals), and undermining oversight (subverting the monitors themselves).
- Evaluations are explicitly mitigation-aware: designed to show that a model operating under a given set of mitigations cannot sabotage a frontier developer's activities — evaluator hardening as a threat model, not an afterthought.
- Demonstrated on Claude 3 Opus and Claude 3.5 Sonnet; conclusion at the time: minimal mitigations suffice, but more realistic evals and stronger mitigations are expected to become necessary as capabilities improve.
- Introduces small-scale statistical simulation of large-scale deployments to estimate whether rare sabotage attempts would be caught before causing harm.

## Connections

- [[safety/agentic misalignment risk]]
- [[safety/agent safety and security]]
- [[operations/agent evals]]
- [[sources/SHADE-Arena]]
- [[sources/In-Context Scheming]]

## Notes

- Canonical URL: https://arxiv.org/abs/2410.21514
- Methodological parent of SHADE-Arena; the "undermining oversight" family is the direct ancestor of testing whether agents can defeat their own monitors.
- The "minimal mitigations suffice" conclusion is dated to the Claude 3.x generation — do not quote it as a current-generation finding.
