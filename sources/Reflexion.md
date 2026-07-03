---
title: "Reflexion: Language Agents with Verbal Reinforcement Learning"
aliases:
  - "Reflexion"
source_type: "paper"
kind: "self-reflection-loop"
status: "verified"
year: 2023
publication_date: "2023-03-20"
publication_date_basis: "arxiv_abs_page"
source_updated_date: "2023-10-10"
source_updated_date_basis: "arxiv_v4_revision_date"
arxiv_id: "2303.11366"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Noah Shinn"
  - "Federico Cassano"
  - "Edward Berman"
  - "Ashwin Gopinath"
  - "Karthik Narasimhan"
  - "Shunyu Yao"
venue: "arXiv / NeurIPS 2023"
url: "https://arxiv.org/abs/2303.11366"
pdf_url: "https://arxiv.org/pdf/2303.11366"
created: 2026-07-03
updated: 2026-07-03
---

# Reflexion

## Summary

- Reinforces agents through linguistic feedback rather than weight updates: self-reflections are stored as text in an episodic memory buffer and prepended to later attempts.
- HumanEval pass@1 of 91% vs 80% for base GPT-4 — the self-critique is grounded in test-execution feedback, not pure introspection.
- Ablations across feedback signal types show the gains depend on the quality of the external evaluation signal (unit tests, environment reward).
- v4 revised 2023-10-10; NeurIPS 2023; the foundational citation for every "agent memory + retry" harness pattern.

## Claims

- [[claims/Claim - Runtime control and verification improve agent reliability]]
- [[claims/Claim - Agent memory and skills create compounding improvement loops]]

## Connections

- [[operations/agent memory]]
- [[methods/self-improving code loops]]
- [[concepts/lifelong agent learning]]
- [[sources/ReAct]]
- [[sources/Google ReasoningBank]]

## Notes

- Canonical URL: https://arxiv.org/abs/2303.11366
- The ablation result is the load-bearing fact for the vault: self-critique works when anchored to external evidence (tests, environment reward), not as free-floating introspection — the mechanism behind self-healing loops in code factories.
