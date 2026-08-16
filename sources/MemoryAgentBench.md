---
title: "Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions"
aliases:
  - "MemoryAgentBench"
  - "Memory Agent Bench"
source_type: "paper"
kind: "agent-memory-benchmark"
status: "verified"
year: 2025
publication_date: "2025-07-07"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: "2026-06-28"
source_updated_date_basis: "arxiv_v4_submission_date"
arxiv_id: "2507.05257"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Yuanzhe Hu"
  - "Yu Wang"
  - "Julian McAuley"
venue: "ICLR 2026"
url: "https://arxiv.org/abs/2507.05257"
pdf_url: "https://arxiv.org/pdf/2507.05257"
created: 2026-08-16
updated: 2026-08-16
---

# MemoryAgentBench

## Summary

- MemoryAgentBench evaluates four competencies that conversational-recall benchmarks do not cover together: accurate retrieval, test-time learning, long-range understanding, and selective forgetting.
- Its current arXiv v4 registry contains 2,071 questions over histories averaging 103K–1.44M tokens. It reformulates existing datasets and adds EventQA and FactConsolidation, then presents all inputs incrementally as simulated user–assistant turns rather than one static document.
- Accurate retrieval covers single- and multi-hop document QA, a 300-question LongMemEval reformulation, and temporal EventQA. Test-time learning covers intent classification and recommendation from examples accumulated during the conversation. Long-range understanding covers novel summarization and detective QA. FactConsolidation tests whether newer conflicting facts supersede older ones in single- and multi-hop reasoning.
- The common protocol injects chunks sequentially, asks the agent to memorize them, then asks multiple questions against the resulting state. This exposes construction and update behavior while amortizing the cost of million-token histories across many probes.
- The original evaluation spans long-context, lexical and embedding RAG, structured RAG, and agentic memory systems. No system dominates all four competencies; strong retrieval does not imply test-time learning, global understanding, or consistent supersession.

## Evidence Boundary

This is a composite benchmark built by transforming heterogeneous source datasets. Metrics differ by task, and the explicit “please memorize” wrapper reveals the need for storage rather than testing implicit activation. FactConsolidation also explicitly tells agents that later serial numbers are newer, so it tests update execution under a supplied policy rather than discovering the policy.

Most RAG and external-memory comparisons use GPT-4o-mini, while long-context rows use multiple backbones. GPT-4o judges the LongMemEval and summarization subsets; other tasks use accuracy, F1, or Recall@5. Ordinary repeated-run counts are not reported. Cost estimates cover only a subset, assume November 2025 OpenAI pricing and caching, and exclude one-time indexing.

## Claims

- [[claims/Claim - Context management is an agent architecture choice]]
- [[claims/Claim - Agent memory and skills create compounding improvement loops]]

## Connections

- [[benchmarks/agent memory benchmarks]]
- [[operations/agent memory]]
- [[maps/Context Management Map]]
- [[sources/LongMemEval]]
- [[sources/MemoryArena]]
- [[sources/Infini Memory]]

## Notes

- Canonical arXiv URL: https://arxiv.org/abs/2507.05257
- Code and data: https://github.com/HUST-AI-HYZ/MemoryAgentBench
- Current OpenReview status: ICLR 2026 poster.
- The public repository README still uses “Conflict Resolution” in one overview; arXiv v4 names the fourth competency “Selective Forgetting.” This card follows the current paper.
- The local PDF is intentionally not linked as a redistributable artifact because arXiv lists only its non-exclusive distribution license; use the canonical paper URL.
