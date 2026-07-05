---
title: "Agent-as-a-Judge: Evaluate Agents with Agents"
aliases:
  - "DevAI"
source_type: "paper"
kind: "agentic-judge"
status: "verified"
year: 2024
publication_date: "2024-10-14"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2410.10934"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Mingchen Zhuge"
  - "Changsheng Zhao"
  - "Dylan Ashley"
  - "Jürgen Schmidhuber"
venue: "arXiv / Meta AI + KAUST"
url: "https://arxiv.org/abs/2410.10934"
pdf_url: "https://arxiv.org/pdf/2410.10934"
artifacts:
  - "raw/papers/Agent-as-a-Judge - Evaluate Agents with Agents.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# Agent-as-a-Judge

## Summary

- Replaces a bare LLM judge with an agentic judge (tool use, code inspection) for grading agent-built software: aligns 90.44% with human consensus on OpenHands output in the black-box setting vs 60.38% for LLM-as-a-Judge, and 92.07% vs 70.76% in gray-box.
- Judge shift (deviation from human consensus) is as low as 0.27% for Agent-as-a-Judge vs up to 31.42% for LLM-as-a-Judge.
- Costs $30.58 vs $1,297.50 for equivalent human evaluation (2.36% of cost) and takes 118.43 minutes vs 86.5 hours (saving 97.72% of time).
- Introduces DevAI: 55 realistic AI-development tasks with 365 hierarchical requirements structured as a dependency DAG, plus 125 optional preferences — grading intermediate requirements, not only final outcomes.
- Explicitly motivated as providing "rich and reliable reward signals for dynamic and scalable self-improvement" — positioning agentic judges as the reward channel for self-improving code systems.

## Connections

- [[concepts/outcomes and rubric graders]]
- [[methods/self-improving code loops]]
- [[operations/agent evals]]
- [[sources/Judging LLM-as-a-Judge with MT-Bench]]
- [[sources/OpenHands]]

## Artifacts

- [[raw/papers/Agent-as-a-Judge - Evaluate Agents with Agents.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2410.10934
- Alignment numbers are computed against a human consensus on DevAI specifically; the paper's own authors built both the benchmark and the judge, so independent replication on other task suites is worth checking before generalizing.
