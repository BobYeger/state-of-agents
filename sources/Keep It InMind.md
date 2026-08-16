---
title: "Keep It InMind: Benchmarking the Implicit-Association Blind Spot in Agent Memory"
aliases:
  - "Keep It InMind"
  - "InMind"
  - "InMind benchmark"
source_type: "paper"
kind: "agent-memory-benchmark"
status: "verified"
year: 2026
publication_date: "2026-07-27"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: null
source_updated_date_basis: null
arxiv_id: "2607.24368"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Ruizhe Li"
  - "Mingxuan Du"
  - "Benfeng Xu"
  - "Zhendong Mao"
venue: "arXiv"
url: "https://arxiv.org/abs/2607.24368"
pdf_url: "https://arxiv.org/pdf/2607.24368"
license: "CC BY 4.0"
license_url: "https://creativecommons.org/licenses/by/4.0/"
created: 2026-08-16
updated: 2026-08-16
---

# Keep It InMind

## Summary

- InMind isolates an **implicit-association blind spot**: a stored fact can matter to a later decision only through world knowledge that appears in neither the fact nor the query. Query-conditioned retrieval must judge relevance before the reasoning model can supply that bridge.
- The benchmark contains 125 expert-verified English tasks across ten life domains. Of these, 113 have citable public grounding and 12 are expert-authored; all user facts and conversations are synthetic.
- Four paired measurements separate failure causes: direct or “naive” recall tests whether the fact survived; an in-context control tests whether the backbone can apply the bridge; answer-blind target recall checks whether retrieval surfaced the fact; application checks whether the final answer used it.
- With GPT-5-mini as answerer, placing the decisive memory in context yields 84.0% application. The best query-time configuration reaches 16.0%, while the six evaluated vector, graph, and agentic memory systems top out at 14.4%, despite direct recall as high as 100.0%.
- Increasing embedding dimensionality from 384 to 3,072 raises target recall across the six systems but recovers only a few points of the roughly 70-point access gap. This is evidence against treating embedding scale as a complete solution, not against retrieval generally.
- A diagnostic always-in-state baseline maintains a GPT-5-mini-written Markdown profile capped at 200 lines. It reaches 68.8% indirect application and 98.4% direct recall. The result shows that pre-query visibility can recover much of the gap, but it is not a controlled ablation of any one memory system.

## Report Implications

The report's `retrieve(M, q)` abstraction is incomplete for memories whose relevance cannot be inferred from the query alone. A fuller design needs a routing or activation layer that decides which decision-critical facts remain visible before a future query is known, alongside a lossless record that can still be searched on demand.

The result supports hybrid memory: preserve raw or fine-grained history for exact recovery, maintain a bounded visible state for constraints with high consequence, and evaluate the routing decision separately from storage and answer quality.

## Evidence Boundary

This is an author-run arXiv v1 diagnostic benchmark. Its 125 synthetic tasks lean toward health, wellness, and safety; humor, institutional policy, and many everyday associations are not covered. A few percentage points are sampling noise, so system ordering inside the low-scoring retrieval group should not be over-read.

GPT-5-mini serves as both answerer and judge, although the paper reports an expert audit of judge decisions. The benchmark has no negative controls that penalize inappropriate warnings, so an optimized system could over-activate memories. The always-in-state probe changes both representation and updater and has a small fixed state budget; it demonstrates sufficiency under this setup rather than a production scaling law.

## Claims

- [[claims/Claim - Context management is an agent architecture choice]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Connections

- [[operations/agent memory]]
- [[operations/agent evals]]
- [[concepts/context retrieval]]
- [[concepts/context engineering]]
- [[maps/Context Management Map]]
- [[sources/LongMemEval]]

## Notes

- Canonical arXiv URL: https://arxiv.org/abs/2607.24368
- Project: https://keep-it-inmind.github.io/
- Repository and benchmark: https://github.com/imlrz/InMind
- arXiv lists only v1 at capture time.
- The paper is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
