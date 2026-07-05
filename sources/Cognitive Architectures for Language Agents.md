---
title: "Cognitive Architectures for Language Agents"
aliases:
  - "CoALA"
source_type: "paper"
kind: "cognitive-architecture"
status: "verified"
year: 2023
publication_date: "2023-09-05"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2309.02427"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Theodore R. Sumers"
  - "Shunyu Yao"
  - "Karthik Narasimhan"
  - "Thomas L. Griffiths"
venue: "TMLR 2024 / arXiv (Princeton)"
url: "https://arxiv.org/abs/2309.02427"
pdf_url: "https://arxiv.org/pdf/2309.02427"
artifacts:
  - "raw/papers/Cognitive Architectures for Language Agents.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# Cognitive Architectures for Language Agents

## Summary

- Framework organizing language agents along three axes: modular memory components, a structured action space split into internal memory actions vs external environment actions, and a generalized decision-making cycle.
- Memory taxonomy distinguishes working memory (active context) from long-term episodic, semantic, and procedural memory — the vocabulary now standard across agent-memory papers and surveys.
- Decision cycle: a planning stage (proposal, evaluation, selection over candidate actions) followed by execution; grounds LLM agents in production-systems and cognitive-architecture history (SOAR, ACT-R).
- arXiv v1 2023-09-05; v3 is the TMLR camera-ready, 2024-03-15.

## Claims

- [[claims/Claim - Context management is an agent architecture choice]]

## Connections

- [[operations/agent memory]]
- [[concepts/procedural memory]]
- [[concepts/reasoning memory]]
- [[concepts/agentic systems]]

## Artifacts

- [[raw/papers/Cognitive Architectures for Language Agents.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2309.02427
- This is the citable origin for the working/episodic/semantic/procedural memory split the vault's memory concept notes use implicitly.
- A conceptual framework paper: it contributes taxonomy and design space, not empirical results.
