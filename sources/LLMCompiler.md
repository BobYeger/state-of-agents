---
title: "An LLM Compiler for Parallel Function Calling"
aliases:
  - "LLMCompiler"
source_type: "paper"
kind: "dependency-aware-tool-orchestration"
status: "verified"
year: 2023
publication_date: "2023-12-07"
publication_date_basis: "arxiv_v1_submission_history"
source_updated_date: "2024-06-05"
source_updated_date_basis: "arxiv_v3_submission_history"
arxiv_id: "2312.04511"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Sehoon Kim"
  - "Suhong Moon"
  - "Ryan Tabrizi"
  - "Nicholas Lee"
  - "Michael W. Mahoney"
  - "Kurt Keutzer"
  - "Amir Gholami"
venue: "arXiv / ICML 2024"
url: "https://arxiv.org/abs/2312.04511"
pdf_url: "https://arxiv.org/pdf/2312.04511v3"
artifacts: []
created: 2026-10-05
updated: 2026-10-05
---

# LLMCompiler

## Summary

- Separates dependency planning, ready-task dispatch, and execution. The model emits a task graph with references to upstream outputs; a scheduler dispatches independent calls concurrently and substitutes completed results.
- Supports streamed planning and replanning when observations require new work. This schedules tool calls; it need not execute an unrestricted generated Python program.

## Evidence and Limits

- The paper reports up to 3.7× latency speedup and 6.7× cost reduction across its benchmark/model settings. Tables 1–2 are the comparison surface; latency comparisons use the strengthened ReAct baseline to address repetitive calls and early stopping.
- Tests include parallel retrieval, dependency-bearing ParallelQA, Game of 24, and WebShop. Gains depend on available parallelism, planning quality, and tool/model latency; maxima are not general guarantees.
- A dependency graph is not a transaction or authorization policy. Conflicting writes and irreversible actions need separate runtime controls.
- Read v3, dated June 5, 2024, rather than attributing all final results to the December 2023 preprint. [Author repository](https://github.com/SqueezeAILab/LLMCompiler).

## Connections

- [[concepts/programmatic tool calling]]
- [[concepts/loop engineering]]
- [[sources/CodeAct]]
- [[sources/Atomix]]
- [[sources/Cloudflare Code Mode MCP]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
