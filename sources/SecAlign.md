---
title: "SecAlign: Defending Against Prompt Injection with Preference Optimization"
aliases:
  - "SecAlign"
source_type: "paper"
kind: "training-based-defense"
status: "verified"
year: 2024
publication_date: "2024-10-07"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2410.05451"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Sizhe Chen"
  - "Arman Zharmagambetov"
  - "Saeed Mahloujifar"
  - "Kamalika Chaudhuri"
  - "David Wagner"
  - "Chuan Guo"
venue: "arXiv / ACM CCS 2025 (Meta / UC Berkeley)"
url: "https://arxiv.org/abs/2410.05451"
pdf_url: "https://arxiv.org/pdf/2410.05451"
created: 2026-07-03
updated: 2026-07-03
---

# SecAlign

## Summary

- Builds a preference dataset where each prompt-injected input is paired with a secure response (follows the legitimate instruction) and an insecure one (follows the injected instruction), then trains via preference optimization to favor the secure output.
- Reduces success rates of various prompt injections to below 10%, including attacks substantially more sophisticated than those seen in training; utility remains comparable to the undefended model.
- Accepted at ACM CCS 2025; v3 released 2025-07-03; code open-sourced on GitHub.
- Represents the adversarial-preference-optimization layer of the defense stack, superseding the same group's StruQ.

## Connections

- [[safety/prompt injection]]
- [[sources/The Instruction Hierarchy]]
- [[sources/AgentDojo]]
- [[sources/The Attacker Moves Second]]

## Notes

- Canonical URL: https://arxiv.org/abs/2410.05451
- Weights-level defense: the <10% attack-success figure is against the paper's evaluated attack suite; adaptive-attack results (The Attacker Moves Second) argue such numbers overstate robustness against defense-aware attackers.
