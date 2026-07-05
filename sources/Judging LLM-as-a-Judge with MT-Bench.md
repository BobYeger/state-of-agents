---
title: "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena"
aliases:
  - "MT-Bench"
  - "LLM-as-a-Judge"
source_type: "paper"
kind: "llm-judge-methodology"
status: "verified"
year: 2023
publication_date: "2023-06-09"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2306.05685"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Lianmin Zheng"
  - "Wei-Lin Chiang"
  - "Ying Sheng"
  - "Siyuan Zhuang"
venue: "NeurIPS 2023 Datasets and Benchmarks Track (arXiv)"
url: "https://arxiv.org/abs/2306.05685"
pdf_url: "https://arxiv.org/pdf/2306.05685"
artifacts:
  - "raw/papers/Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# Judging LLM-as-a-Judge with MT-Bench

## Summary

- Origin paper of the LLM-as-a-judge paradigm: GPT-4 as judge reaches over 80% agreement with human preferences, the same level as human-human agreement, establishing that model judges can substitute for human raters at scale.
- Names and measures the three canonical judge biases that later reliability work builds on: position bias (preferring responses by presentation order), verbosity bias (favoring longer outputs), and self-enhancement bias (favoring outputs from similar models).
- Introduces MT-Bench, a multi-turn question set, validated against 3,000 expert votes and 30,000 crowdsourced Chatbot Arena conversations.
- Final revision December 24, 2023; the citation root for essentially all subsequent judge-reliability research.

## Connections

- [[concepts/outcomes and rubric graders]]
- [[operations/agent evals]]
- [[benchmarks/agent evaluation]]
- [[sources/Agent-as-a-Judge]]
- [[sources/Anthropic Demystifying Agent Evals]]

## Artifacts

- [[raw/papers/Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2306.05685
- Bias magnitudes are measured on 2023-era models (GPT-4, Claude-v1); absolute agreement numbers may not transfer to current judges, though the bias taxonomy has held up.
