---
title: "Defeating Prompt Injections by Design (CaMeL)"
aliases:
  - "CaMeL"
source_type: "paper"
kind: "injection-defense"
status: "verified"
year: 2025
publication_date: "2025-03-24"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2503.18813"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Edoardo Debenedetti"
  - "Ilia Shumailov"
  - "Tianqi Fan"
  - "Jamie Hayes"
  - "Nicholas Carlini"
  - "Daniel Fabian"
  - "Christoph Kern"
  - "Chongyang Shi"
  - "Andreas Terzis"
  - "Florian Tramèr"
venue: "arXiv / Google DeepMind / ETH Zurich; IEEE SaTML 2026"
url: "https://arxiv.org/abs/2503.18813"
pdf_url: "https://arxiv.org/pdf/2503.18813"
created: 2026-07-03
updated: 2026-07-03
---

# Defeating Prompt Injections by Design (CaMeL)

## Summary

- Architecture that defends against prompt injection by construction rather than detection: a Privileged LLM generates a Python-like execution plan from the trusted user query only, a Quarantined LLM parses untrusted data with no tool access, and a custom interpreter tracks data provenance and enforces security policies before every tool call.
- Untrusted data can never influence control flow by construction; "capabilities" (metadata attached to values) block exfiltration over unauthorized data flows — deterministic taint tracking rather than model-based judgment.
- Solves 77% of AgentDojo tasks with provable security, versus 84% for an undefended system (v1 numbers; v2 of 2025-06-24 re-evaluates with newer models).
- Explicitly identifies and fixes flaws in Willison's 2023 Dual LLM pattern, where untrusted data could still exfiltrate via data dependencies.
- Code released at github.com/google-research/camel-prompt-injection; accepted at IEEE SaTML 2026; assigned reading in MIT 6.5660 (Spring 2026).

## Claims

- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[safety/prompt injection]]
- [[operations/agent harnesses]]
- [[operations/permissions]]
- [[sources/AgentDojo]]
- [[sources/Design Patterns for Securing LLM Agents]]
- [[sources/Willison Dual LLM Pattern]]
- [[sources/FIDES]]

## Notes

- Canonical URL: https://arxiv.org/abs/2503.18813
- Repository: https://github.com/google-research/camel-prompt-injection
- The 77% vs 84% utility gap is from v1 (2025-03-24); v2 (2025-06-24) re-evaluates with newer models, so quote version-specific numbers with care.
- SaTML 2026 acceptance is a post-cutoff venue update; verify the final camera-ready version when citing.
