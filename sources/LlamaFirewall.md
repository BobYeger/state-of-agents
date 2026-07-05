---
title: "LlamaFirewall: An open source guardrail system for building secure AI agents"
aliases:
  - "LlamaFirewall"
source_type: "paper"
kind: "runtime-guardrail"
status: "verified"
year: 2025
publication_date: "2025-05-06"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2505.03574"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Sahana Chennabasappa"
  - "Cyrus Nikolaidis"
  - "Daniel Song"
  - "David Molnar"
venue: "arXiv / Meta"
url: "https://arxiv.org/abs/2505.03574"
pdf_url: "https://arxiv.org/pdf/2505.03574"
artifacts:
  - "raw/papers/LlamaFirewall - An open source guardrail system for building secure AI agents.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# LlamaFirewall

## Summary

- Open-source guardrail framework with three layers: PromptGuard 2 (universal jailbreak/injection detector model), AlignmentCheck (chain-of-thought auditor detecting injection-induced goal deviation), and CodeShield (online static analysis blocking insecure generated code).
- On its AgentDojo-based evaluation, PromptGuard 2 alone cuts attack success rate from 17.6% to 7.5%, AlignmentCheck reaches 2.9%, and the combined stack reaches 1.75% ASR (over 90% reduction) while preserving task utility.
- AlignmentCheck is a classifier over agent reasoning traces rather than inputs — catching indirect injections that input scanners miss.
- CodeShield targets coding agents specifically, making this a reference runtime guardrail design for code factories.

## Claims

- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[safety/prompt injection]]
- [[operations/agent harnesses]]
- [[concepts/code factories]]
- [[sources/AgentDojo]]
- [[sources/The Attacker Moves Second]]
- [[sources/Constitutional Classifiers]]

## Artifacts

- [[raw/papers/LlamaFirewall - An open source guardrail system for building secure AI agents.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2505.03574
- 19 Meta authors; frontmatter lists the first four.
- Per-layer ASR numbers come from Meta's own AgentDojo-based evaluation; classifier-layer defenses of this type are among those adaptive-attack work shows can be bypassed under defense-aware pressure.
