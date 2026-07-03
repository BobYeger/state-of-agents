---
title: "The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections"
aliases:
  - "Attacker Moves Second"
source_type: "paper"
kind: "adaptive-attack-evaluation"
status: "verified"
year: 2025
publication_date: "2025-10-10"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2510.09023"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Milad Nasr"
  - "Nicholas Carlini"
  - "Chawin Sitawarin"
  - "Sander V. Schulhoff"
  - "Jamie Hayes"
  - "Michael Ilie"
  - "Juliette Pluto"
  - "Shuang Song"
  - "Harsh Chaudhari"
  - "Ilia Shumailov"
  - "Abhradeep Thakurta"
  - "Kai Y. Xiao"
  - "Andreas Terzis"
  - "Florian Tramèr"
venue: "arXiv (joint OpenAI / Anthropic / Google DeepMind / ETH Zurich)"
url: "https://arxiv.org/abs/2510.09023"
pdf_url: "https://arxiv.org/pdf/2510.09023"
created: 2026-07-03
updated: 2026-07-03
---

# The Attacker Moves Second

## Summary

- Systematically attacks 12 recently published jailbreak/prompt-injection defenses (prompting-, training-, and classifier-based) with adaptive, defense-aware attackers and substantial compute budgets.
- Four attack methods: systematically tuned gradient descent, reinforcement learning, random search, and human-guided exploration.
- Achieves attack success rates above 90% against most defenses that had originally reported near-zero ASR; human red-teamers reached 100% across defenses.
- Core methodological claim: evaluating defenses against static attack strings or weak optimizers is invalid — the attacker always moves second and counters the defense's design.
- Rare three-lab collaboration (OpenAI, Anthropic, Google DeepMind authors) — effectively an industry consensus statement on defense evaluation standards.
- Establishes the negative result motivating by-design/deterministic architectures (CaMeL, FIDES): heuristic in-band defenses do not survive adaptive pressure.

## Connections

- [[safety/prompt injection]]
- [[benchmarks/agent evaluation]]
- [[sources/CaMeL]]
- [[sources/FIDES]]
- [[sources/LlamaFirewall]]
- [[sources/Constitutional Classifiers]]

## Notes

- Canonical URL: https://arxiv.org/abs/2510.09023
- Also on OpenReview; check which of the 12 attacked defenses overlap with cards in this vault before citing per-defense numbers.
