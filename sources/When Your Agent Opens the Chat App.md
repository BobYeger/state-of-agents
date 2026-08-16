---
title: "When Your Agent Opens the Chat App: Agent-Controlled Search over Raw Chat Logs Rivals Structured Memory"
aliases:
  - "When Your Agent Opens the Chat App"
  - "ReFind"
  - "Agent-Controlled Search over Raw Chat Logs"
source_type: "paper"
kind: "memory-retrieval-study"
status: "verified"
year: 2026
publication_date: "2026-08-13"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: null
source_updated_date_basis: null
arxiv_id: "2608.12888"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Ruizhe Li"
  - "Licheng Zhang"
  - "Benfeng Xu"
  - "Mingxuan Du"
  - "Zheren Fu"
  - "Weidong Chen"
venue: "arXiv"
url: "https://arxiv.org/abs/2608.12888"
pdf_url: "https://arxiv.org/pdf/2608.12888"
license: "CC BY 4.0"
license_url: "https://creativecommons.org/licenses/by/4.0/"
created: 2026-08-16
updated: 2026-08-16
---

# When Your Agent Opens the Chat App

## Summary

- ReFind preserves the raw chat archive and builds only an append-only, turn-level BM25 access index. It creates no LLM-generated summaries, entities, graphs, or learned memory objects before a question arrives.
- A four-iteration ReAct searcher reformulates keywords from observed hits and saves evidence for a separate answer stage. Four chat-native controls add session-level reciprocal-rank fusion, ±2-turn local expansion, agent-specified temporal filtering, and exclusion of sessions already inspected.
- On six precise-retrieval and factual-update tasks from MemoryAgentBench, roughly 2,800 questions in total, ReFind reaches a 58.2 unweighted mean with GPT-4o-mini. HippoRAG 2 is the strongest structured baseline at 53.2 and one-shot BM25-RAG reaches 48.8.
- ReFind leads five of six task columns, but absolute performance is uneven: it reaches only 8.8 on multi-hop fact consolidation and narrowly trails BM25-RAG on EventQA, 74.1 versus 74.6. The result is a strong baseline for evidence-grounded refinding, not a solved general memory system.
- With GPT-5-mini on fixed LongMemEval-S and -M subsets, ReFind averages 93.2 ± 3.3 over 50 questions and 89.3 ± 6.0 over 15 questions across five executions. These standard deviations measure run variability, not question-sampling uncertainty.
- Matched controls support the interaction of adaptive search and chat structure. Generic iterative BM25 without the four controls reaches 78.7/82.2 on S/M, while a one-search variant reaches 84.7/68.9. Removing local expansion costs 9.2/4.9 points and removing seen-session filtering costs 1.2/9.3.
- The design shifts model computation from index construction to query time, averaging 2.5–2.6 searches and five LLM calls per question in the reported LongMemEval runs.

## Report Implications

A serious memory evaluation should include an immutable raw-record baseline with competent agent-controlled search before crediting gains to semantic construction. Session boundaries, timestamps, neighboring turns, and search-state metadata may supply enough structure for many exact-evidence workloads.

This does not remove the need for summaries, graphs, or visible state. ReFind addresses precise retrieval and fact tracking; semantic abstraction, low-latency reads, implicit association, prospective activation, and bounded always-visible constraints remain separate requirements. Report offline construction and online query cost separately.

## Evidence Boundary

This is an author-run arXiv v1 study. The main comparison reuses baseline values from MemoryAgentBench, and the LongMemEval comparison reuses most values from STITCH rather than rerunning every system locally. Backbones are matched, but implementation, tuning, and index-construction budgets are inherited from the source studies.

LongMemEval-M contains only 15 fixed questions, most ablations have three executions, and reported differences are descriptive rather than paired. The benchmark scope is text chat with discriminative surface forms and explicit session/time metadata; it does not test images, tool-state memories, proactive behavior, access control, or production latency and cost. “Raw” also means no semantic rewrite, not literally no structure: BM25 and archive metadata remain essential.

## Claims

- [[claims/Claim - Context management is an agent architecture choice]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Connections

- [[operations/agent memory]]
- [[operations/agent evals]]
- [[concepts/context retrieval]]
- [[maps/Context Management Map]]
- [[sources/LongMemEval]]
- [[sources/HippoRAG]]
- [[sources/GraphRAG]]

## Notes

- Canonical arXiv URL: https://arxiv.org/abs/2608.12888
- arXiv lists only v1 at capture time.
- The paper is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
