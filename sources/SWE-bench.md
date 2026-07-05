---
title: "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"
aliases:
  - "SWE-bench"
source_type: "paper"
kind: "benchmark"
status: "verified"
year: 2023
publication_date: "2023-10-10"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2310.06770"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Carlos E. Jimenez"
  - "John Yang"
  - "Alexander Wettig"
  - "Shunyu Yao"
  - "Kexin Pei"
  - "Ofir Press"
  - "Karthik Narasimhan"
venue: "arXiv / ICLR 2024"
url: "https://arxiv.org/abs/2310.06770"
pdf_url: "https://arxiv.org/pdf/2310.06770"
artifacts:
  - "raw/papers/SWE-bench - Can Language Models Resolve Real-World GitHub Issues.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# SWE-bench

## Summary

- 2,294 software engineering problems drawn from real GitHub issues across 12 popular Python repositories; the model receives a full codebase plus an issue description and must produce a patch that passes held-out unit tests.
- At publication the best model (Claude 2) resolved 1.96% of issues; by late 2025 frontier models exceeded 75% on the Verified subset — the single clearest capability trend line for coding agents.
- Origin of the entire SWE-bench family (Verified, Pro, Multimodal, rebench) and the de-facto unit of measure for coding-agent progress; leaderboard at swebench.com.
- Published at ICLR 2024; latest arXiv revision v3 dated 2024-11-11.

## Connections

- [[benchmarks/agent evaluation]]
- [[operations/agent evals]]
- [[concepts/code factories]]
- [[sources/SWE-bench Verified]]
- [[sources/OpenAI Retires SWE-bench Verified]]
- [[sources/TheAgentCompany]]

## Artifacts

- [[raw/papers/SWE-bench - Can Language Models Resolve Real-World GitHub Issues.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2310.06770
- Scores on the original 2,294-task set are not directly comparable to Verified-subset scores; most 2024+ reported numbers use the 500-task Verified subset.
- Citation count pending vault backfill.
