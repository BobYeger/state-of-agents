---
title: "Context Rot: How Increasing Input Tokens Impacts LLM Performance"
aliases:
  - "Context Rot"
source_type: "report"
kind: "context-degradation-study"
status: "verified"
year: 2025
publication_date: "2025-07-14"
publication_date_basis: "vendor_report_page"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Kelly Hong"
  - "Anton Troynikov"
  - "Jeff Huber"
venue: "Chroma technical report"
url: "https://www.trychroma.com/research/context-rot"
pdf_url: ""
artifacts:
  - "raw/reports/context-rot.md"
created: 2026-07-03
updated: 2026-07-05
---

# Context Rot

## Summary

- Tested 18 models across 4 organizations (Claude Opus 4/Sonnet 4/3.7/3.5/Haiku 3.5; o3, GPT-4.1 family, GPT-4o, GPT-4 Turbo, GPT-3.5; Gemini 2.5 Pro/Flash, 2.0 Flash; Qwen3 235B/32B/8B) — all 18 degrade as input length grows, even on trivial tasks.
- Needle-question semantic similarity (0.445-0.829 cosine range) modulates the rot: lower-similarity pairs degrade faster with length, so length and semantic difficulty compound.
- Distractor effects are non-uniform and amplified at length: one topically similar distractor lowers accuracy, four compound it further; models also perform better on shuffled haystacks than logically coherent ones.
- LongMemEval comparison: focused prompts (~300 tokens of relevant content) consistently beat full prompts (~113k tokens) across every model family — direct evidence for retrieval/compaction over dump-everything.
- A repeated-words task (replicate a sequence with one unique inserted word, 25-10,000 words) shows even pure copy tasks degrade with length.

## Claims

- [[claims/Claim - Context management is an agent architecture choice]]

## Connections

- [[concepts/context engineering]]
- [[concepts/context compaction]]
- [[concepts/task-aware context pruning]]
- [[sources/Lost in the Middle]]
- [[sources/LongMemEval]]
- [[sources/Cloudflare Agent Memory]]

## Artifacts

- [[raw/reports/context-rot.md]]

## Notes

- Canonical URL: https://www.trychroma.com/research/context-rot (original URL research.trychroma.com/context-rot now 301s here).
- Origin of the term "context rot", already used without citation in [[sources/OpenAI Codex Subagents]] and [[sources/Self-Driving Codebases Long-Running Async Agents Talk]].
- Chroma sells a retrieval database, so the conclusion favors its business; the cross-vendor 18-model dataset is nonetheless the strongest length-degradation evidence available.
