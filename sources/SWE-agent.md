---
title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
aliases:
  - "SWE-agent"
  - "ACI"
source_type: "paper"
kind: "agent-computer-interface"
status: "verified"
year: 2024
publication_date: "2024-05-06"
publication_date_basis: "arxiv_abs_page"
source_updated_date: "2024-11-11"
source_updated_date_basis: "arxiv_v3_revision_date"
arxiv_id: "2405.15793"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "John Yang"
  - "Carlos E. Jimenez"
  - "Alexander Wettig"
  - "Kilian Lieret"
  - "Shunyu Yao"
  - "Karthik Narasimhan"
  - "Ofir Press"
venue: "arXiv / NeurIPS 2024"
url: "https://arxiv.org/abs/2405.15793"
pdf_url: "https://arxiv.org/pdf/2405.15793"
created: 2026-07-03
updated: 2026-07-03
---

# SWE-agent

## Summary

- Introduces the Agent-Computer Interface (ACI): a purpose-built command/feedback layer for LM agents, distinct from human interfaces like vim or raw shells.
- Core claim: interface design — a file viewer, guarded edit with linting, search with concise output — drives coding-agent performance more than prompting, at fixed model capability.
- SWE-bench pass@1 of 12.5% and HumanEvalFix pass@1 of 87.7%, far exceeding prior non-interactive RAG baselines.
- Built by a Princeton team overlapping with the SWE-bench authors, making it the canonical companion paper to the benchmark; code and demo at swe-agent.com.
- v3 revised 2024-11-11; NeurIPS 2024.

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Connections

- [[operations/agent harnesses]]
- [[concepts/agent operating surfaces]]
- [[concepts/tool use]]
- [[sources/SWE-bench]]
- [[sources/Mini-SWE-agent]]
- [[sources/ReAct]]

## Notes

- Canonical URL: https://arxiv.org/abs/2405.15793
- Origin of the term "agent-computer interface"; this is the peer-reviewed anchor for the harness-design thesis that vendor blog posts in the vault assert without citation.
- The 12.5% figure is a 2024 result with 2024-era models; use it for the interface-vs-prompting comparison, not as a current capability number.
