---
title: "Beyond a Million Tokens: Benchmarking and Enhancing Long-Term Memory in LLMs"
aliases:
  - "BEAM"
  - "BEAM benchmark"
source_type: "paper"
kind: "agent-memory-benchmark"
status: "verified"
year: 2025
publication_date: "2025-10-31"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: "2026-02-21"
source_updated_date_basis: "arxiv_v2_submission_date"
arxiv_id: "2510.27246"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Mohammad Tavakoli"
  - "Alireza Salemi"
  - "Carrie Ye"
  - "Mohamed Abdalla"
  - "Hamed Zamani"
  - "J. Ross Mitchell"
venue: "ICLR 2026"
url: "https://arxiv.org/abs/2510.27246"
pdf_url: "https://arxiv.org/pdf/2510.27246"
license: "CC BY 4.0"
license_url: "https://creativecommons.org/licenses/by/4.0/"
created: 2026-08-16
updated: 2026-08-16
---

# BEAM

## Summary

- BEAM extends conversational-memory evaluation to release bands of 128K, 500K, 1M, and 10M. The paper's result tables label the first band 100K, so 100K and 128K should not be treated as separate splits without a revised release. It contains 100 synthetic but human-validated conversations across 19 domains and 2,000 probing questions—two questions for each of ten abilities in every conversation.
- The ten abilities are abstention, contradiction resolution, event ordering, information extraction, instruction following, knowledge update, multi-hop reasoning, preference following, summarization, and temporal reasoning.
- Nine abilities use human-authored atomic nuggets scored 0, 0.5, or 1 by an LLM judge. Event ordering uses Kendall tau-b after an LLM equivalence detector aligns response events to reference nuggets.
- The paper compares long-context prompting, top-k RAG, and its own LIGHT memory system across Qwen2.5-32B, Llama 4 Maverick, Gemini 2.0 Flash, and GPT-4.1 nano. Performance generally falls with conversation length; contradiction resolution remains the weakest ability across methods.
- BEAM's durable contribution is scale plus capability breadth, not the authors' method ranking. It makes retrieval budget and context band part of the benchmark configuration: increasing retrieved turns helped through a point, then additional noise hurt.

## Evidence Boundary

The conversations and probes are generated through a multi-model pipeline. Two annotators validate probes and sample sections from each conversation rather than reading every million-token history end to end. The benchmark therefore tests coherence under a controlled synthetic construction, not naturally accumulated production memory.

At 10M tokens, no evaluated reader consumes the complete conversation directly. Vanilla long-context arms receive the largest recent segment that fits each model's window. RAG instead indexes every user–assistant turn pair from the full conversation and sends the top five retrieved pairs to a 32K reader. LIGHT builds its episodic index and iterative scratchpad across the conversation, then answers from retrieved episodes, a filtered scratchpad, and recent working memory within a 32K reader context. Only vanilla uses recent-tail truncation; RAG and LIGHT use full-history memory construction with bounded query-time context.

The identity and reliability calibration of the result-scoring LLM judge, ordinary repeated-run count, and end-to-end cost are not reported. Treat scores as model–method–context-budget configurations, not intrinsic model-memory capability.

## Claims

- [[claims/Claim - Context management is an agent architecture choice]]

## Connections

- [[benchmarks/agent memory benchmarks]]
- [[operations/agent memory]]
- [[maps/Context Management Map]]
- [[sources/LongMemEval]]
- [[sources/MemoryAgentBench]]

## Notes

- Canonical arXiv URL: https://arxiv.org/abs/2510.27246
- OpenReview paper: https://openreview.net/forum?id=y59hf5lrMn
- Code and data: https://github.com/mohammadtavakoli78/BEAM
- The paper is arXiv v2 and an ICLR 2026 conference paper at capture time.
