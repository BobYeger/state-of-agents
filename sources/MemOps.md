---
title: "MemOps: Benchmarking Lifecycle Memory Operations in Long-Horizon Conversations"
aliases:
  - "MemOps"
  - "Lifecycle Memory Operations Benchmark"
source_type: "paper"
kind: "memory-lifecycle-benchmark"
status: "verified"
year: 2026
publication_date: "2026-07-14"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: null
source_updated_date_basis: null
arxiv_id: "2607.12893"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Xixuan Hao"
  - "Zeyu Zhang"
  - "Zehao Lin"
  - "Yihang Sun"
  - "Ziliang Guo"
  - "Xichong Zhang"
  - "Yuxuan Liang"
  - "Feiyu Xiong"
  - "Zhiyu Li"
venue: "arXiv"
url: "https://arxiv.org/abs/2607.12893"
pdf_url: "https://arxiv.org/pdf/2607.12893"
license: "arXiv non-exclusive distribution"
license_url: "https://arxiv.org/licenses/nonexclusive-distrib/1.0/"
created: 2026-08-16
updated: 2026-08-16
---

# MemOps

## Summary

- MemOps changes the evaluation unit from a final answer to a trace of lifecycle operations. Each event records its trigger, target, old and new values, scope, state transition, and exact supporting user turns.
- It defines five operation families: `Remember`, `Forget`, `Update`, `Reflect`, and `TrajectoryOps`, which composes several operations over time. Six probe families test event detection, target binding, state transition, candidate disambiguation, downstream application, and reconstruction of the state trajectory.
- The generated benchmark spans 100 topics, 403 evidence conversations, 1,209 segments, 9,672 turns, and 2,006 unique question–answer pairs. Pairing every probe with adjacent-evidence and distractor-heavy long-context conditions yields 4,012 instances; long contexts average 60,821 tokens and reach 68,309.
- Diagnostics include answer accuracy, Operation F1, provenance support, leakage of forgotten values, reuse of stale values, and precision of inferred reflections. A correct final answer can therefore still fail if it relies on an inconsistent or unsupported memory state.
- Evidence organization materially changes results. GPT-4.1-mini session-level RAG reaches 0.845 accuracy versus 0.618 for turn-level RAG; StateTrajectory accuracy is 0.549 versus 0.073. Preserving the surrounding session helps operations whose meaning depends on ordering and neighboring turns.
- Strong long-context models retain 0.663–0.808 overall answer accuracy, yet their StateTrajectory scores range only from 0.207 to 0.598. They can often select a plausible current value without faithfully reconstructing how the memory state evolved.
- In the paper's managed-memory comparison, MemOS reaches 0.785 overall accuracy versus Mem0 at 0.543; the authors attribute much of the gap to MemOS returning longer, dialogue-like context. This product comparison is not independent evidence of general system quality.

## Report Implications

Memory should be modeled as auditable state with an operation ledger, not only a collection of facts. A schema should distinguish active, stale, superseded, forgotten, and inferred values and retain trigger, target, evidence, transition, and transformation provenance.

The report's evaluation matrix should add operation-level probes and require state-trajectory accuracy, forgotten-value leakage, stale-value reuse, reflection precision, and provenance support alongside final task success.

## Evidence Boundary

This is an author-run arXiv v1 benchmark from a MemTensor-affiliated team. The conversational scenarios are model-generated, verified with deterministic checks and an LLM, and embedded in UltraChat-derived distractor histories. Operation diagnostics are graded by GPT-4o against gold traces; the paper identifies stronger human validation and judge calibration as future work.

The 100-topic English benchmark tests deliberately constructed memory events rather than naturally occurring production histories. Model and managed-memory rankings depend on prompts, output format, retrieval granularity, and versioned services. The durable contribution is the explicit lifecycle trace and diagnostic decomposition, not the leaderboard ordering.

## Claims

- [[claims/Claim - Runtime control and verification improve agent reliability]]
- [[claims/Claim - Context management is an agent architecture choice]]

## Connections

- [[operations/agent memory]]
- [[operations/agent evals]]
- [[concepts/versioned context]]
- [[concepts/context retrieval]]
- [[maps/Context Management Map]]
- [[sources/LongMemEval]]
- [[sources/Mem0]]

## Notes

- Canonical arXiv URL: https://arxiv.org/abs/2607.12893
- Repository: https://github.com/MemTensor/MemOps
- arXiv lists only v1 at capture time.
- arXiv lists its non-exclusive distribution license, not a Creative Commons reuse license.
