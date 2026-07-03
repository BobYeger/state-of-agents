---
title: "AI Control: Improving Safety Despite Intentional Subversion"
aliases:
  - "AI Control"
source_type: "paper"
kind: "ai-control"
status: "verified"
year: 2023
publication_date: "2023-12-12"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2312.06942"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Ryan Greenblatt"
  - "Buck Shlegeris"
  - "Kshitij Sachan"
  - "Fabien Roger"
venue: "arXiv / ICML 2024 (Redwood Research)"
url: "https://arxiv.org/abs/2312.06942"
pdf_url: "https://arxiv.org/pdf/2312.06942"
created: 2026-07-03
updated: 2026-07-03
---

# AI Control: Improving Safety Despite Intentional Subversion

## Summary

- Founding paper of the AI control agenda: evaluate safety protocols under the assumption that the untrusted model (GPT-4) is intentionally trying to subvert them, with a weaker trusted model (GPT-3.5) and limited trusted human labor as the only resources.
- Threat model operationalized as backdoored code: logical errors in APPS programming solutions that pass all test cases.
- Trusted editing protocol: GPT-4 writes code, GPT-3.5 rates suspiciousness; below-threshold code is submitted, above-threshold code is rewritten by the trusted model.
- Untrusted monitoring protocol: a second GPT-4 instance checks for backdoors, with anti-collusion techniques (redaction/paraphrasing of inputs) to stop the monitor and policy coordinating.
- Introduces the control-evaluation methodology — red team supplies attack policies, blue team supplies protocols, results plotted as a safety-vs-usefulness Pareto frontier — reused by all later control work.

## Claims

- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[methods/runtime supervision]]
- [[safety/agent safety and security]]
- [[safety/agentic misalignment risk]]
- [[sources/Ctrl-Z Controlling AI Agents via Resampling]]
- [[sources/In-Context Scheming]]

## Notes

- Canonical URL: https://arxiv.org/abs/2312.06942
- v5 revised 2024-07-23; published at ICML 2024.
- Single-shot code-generation setting; Ctrl-Z extends the methodology to multi-step agent trajectories.
