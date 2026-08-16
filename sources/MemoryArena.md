---
title: "MemoryArena: Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks"
aliases:
  - "MemoryArena"
  - "Memory Arena"
source_type: "paper"
kind: "agent-memory-benchmark"
status: "verified"
year: 2026
publication_date: "2026-02-18"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: null
source_updated_date_basis: null
arxiv_id: "2602.16313"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Zexue He"
  - "Yu Wang"
  - "Churan Zhi"
  - "Yuanzhe Hu"
  - "Tzu-Ping Chen"
  - "Lang Yin"
  - "Ze Chen"
  - "Tong Arthur Wu"
  - "Siru Ouyang"
  - "Zihan Wang"
  - "Jiaxin Pei"
  - "Julian McAuley"
  - "Yejin Choi"
  - "Alex Pentland"
venue: "arXiv"
url: "https://arxiv.org/abs/2602.16313"
pdf_url: "https://arxiv.org/pdf/2602.16313"
created: 2026-08-16
updated: 2026-08-16
---

# MemoryArena

## Summary

- MemoryArena moves memory evaluation from post-hoc recall into a Memory–Agent–Environment loop. Each subtask runs in a fresh session, but later subtasks depend causally on actions, observations, preferences, or intermediate results from earlier sessions.
- Scale is snapshot-dependent. ArXiv v1 is internally inconsistent: Table 1 reports 766 tasks, while Table 2's component counts total 736 (150 bundled shopping, 270 group travel, 256 progressive search, 40 mathematics, and 20 physics). The official Hugging Face artifact at revision `da1a37c8b19280e18627ca01cf368195a5e1d92e` contains 701 test rows (150, 270, 221, 40, and 20 respectively). Treat the paper and released data as distinct snapshots and record the artifact revision.
- The paper reports averages of 6.9 interdependent subtasks and 57 agent steps per task; individual chains contain 2–16 sessions. These are paper-level statistics, not values recomputed from the 701-row artifact.
- The four task families test web navigation with compatibility constraints, preference-constrained planning, progressive information search, and sequential formal reasoning. Memory is updated after each subtask and retrieved at the start of the next session in the reported setup.
- Evaluation reports task success rate, progress score, success at dependency depth, task-specific soft progress where exact travel completion is near zero, and latency. This exposes degradation across dependency depth rather than collapsing every failure into final-answer accuracy.
- In the authors' fixed-task-agent comparison, external memory and RAG do not consistently beat raw long context. External memory helps when traces exceed effective context or reasoning saturates, while retrieval-based systems are more robust than heavily consolidated memory when later steps require exact reuse.

## Evidence Boundary

This is an author-run arXiv v1 benchmark. The code repository labels itself a preview, and no ordinary repeated-run count is reported. The paper's scale tables disagree, and the released data is a smaller snapshot, so a result without both paper version and artifact revision is underspecified. The task families use different environments and verifiers; live web search and hosted memory APIs add service drift, latency, and implementation confounds.

The main memory-method comparison holds the task agent at GPT-5.1-mini, but the paper also reports separate long-context backbone rows. Session-level retrieval is the benchmark's cost-saving default, not the only possible memory schedule. The result establishes that conversational recall does not predict interdependent action; it does not produce a universal ranking of memory substrates.

## Claims

- [[claims/Claim - Context management is an agent architecture choice]]
- [[claims/Claim - Agent memory and skills create compounding improvement loops]]

## Connections

- [[benchmarks/agent memory benchmarks]]
- [[benchmarks/long-horizon benchmarks]]
- [[operations/agent memory]]
- [[maps/Context Management Map]]
- [[sources/MemoryAgentBench]]
- [[sources/LongMemEval-V2]]

## Notes

- Canonical arXiv URL: https://arxiv.org/abs/2602.16313
- Project and public data: https://memoryarena.github.io/
- Preview code: https://github.com/ZexueHe/MemoryArena
- Pinned public-data snapshot: https://huggingface.co/datasets/ZexueHe/memoryarena/tree/da1a37c8b19280e18627ca01cf368195a5e1d92e
- The project data is CC BY 4.0; the code repository does not display a software license at capture time.
- The local PDF is intentionally not linked as a redistributable artifact because arXiv lists only its non-exclusive distribution license; use the canonical paper URL.
