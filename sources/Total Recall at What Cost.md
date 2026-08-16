---
title: "Total Recall at What Cost? Benchmarking the Serving Cost of Agentic Memory Systems"
aliases:
  - "Total Recall at What Cost"
  - "Serving Cost of Agentic Memory Systems"
source_type: "paper"
kind: "memory-cost-benchmark"
status: "verified"
year: 2026
publication_date: "2026-08-12"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: null
source_updated_date_basis: null
arxiv_id: "2608.11879"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Natchanon Pollertlam"
  - "Witchayut Kornsuwannawit"
venue: "arXiv"
url: "https://arxiv.org/abs/2608.11879"
pdf_url: "https://arxiv.org/pdf/2608.11879"
license: "CC BY 4.0"
license_url: "https://creativecommons.org/licenses/by/4.0/"
created: 2026-08-16
updated: 2026-08-16
---

# Total Recall at What Cost?

## Summary

- This author-run cost benchmark compares Mem0, Hindsight, and Mastra Observational Memory with a ten-turn rolling window and full-transcript resubmission. It accounts for billable ingest, retrieval, consolidation, and answer-stage model calls rather than counting only the retrieved payload.
- Cost experiments cross two backbones, two reasoning-effort settings, conversation lengths up to 400 turns, and several message sizes. Each main memory-system grid cell has eight synthetic-dialogue runs with different seeds; two additional Mastra OM scale cells have three runs each.
- A regression using conversation depth and message size predicts the two window baselines with under 6.5% held-out error but misses memory systems by 18–69%. Their serving cost depends on internal state, including extraction schedules, reflection thresholds, and generated memory volume.
- Measured sustained break-even against full history varies sharply. Across 400-turn cells, Mastra OM crosses at turns 0–86, Mem0 at 0–342, and Hindsight from 60 to never within the measured horizon. In one 200-token, GPT-OSS-20B-low cell, the respective points are 0, 82, and 356.
- By turn 400, full history costs as much as 12.7 times a memory system that has already crossed break-even. Conversely, Hindsight costs as much as 3.3 times full history in small-message cells where it does not break even.
- Accuracy is evaluated separately on 665 LoCoMo questions from four dialogues. Across system–backbone–effort cells it ranges from 0.214 to 0.541, with no system winning both accuracy and cost. Backbone choice changes the cost surface as much as memory-system choice.

## Report Implications

Memory economics should be represented as a workload-dependent break-even curve, not one token-saving percentage. A comparison registry needs conversation depth, message size, ingest cadence, consolidation trigger, retrieval budget, answer model, reasoning effort, prompt caching, provider prices, and cost per correctly answered task.

The builder baseline should include both a bounded recent window and full history where feasible. A memory adapter earns its complexity only when its measured quality–latency–cost frontier beats those controls for the expected workload.

## Evidence Boundary

This is a two-author Bricks Technology arXiv v1 preprint. The cost dialogues are synthetic, while accuracy comes from only four LoCoMo dialogues; the reported Wilson intervals treat 665 questions as independent and understate dialogue-level clustering.

The regression is descriptive and extrapolates poorly for all three memory systems. Hindsight's ingest backend was accidentally fixed rather than controlled across cells, so its cross-backbone and reasoning comparisons are invalid and excluded by the authors. Provider routing and prompt-cache misses introduce billing variance, and one full-history serving run ends at turn 374. Cost per correct answer also omits latency, abstention, retrieval quality, and answer length.

## Claims

- [[claims/Claim - Context management is an agent architecture choice]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Connections

- [[operations/agent memory]]
- [[operations/cost control]]
- [[operations/agent evals]]
- [[concepts/cache-aware harness design]]
- [[sources/Mem0]]
- [[sources/LongMemEval]]

## Notes

- Canonical arXiv URL: https://arxiv.org/abs/2608.11879
- The authors are affiliated with Bricks Technology.
- arXiv lists only v1 at capture time.
- The paper is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
