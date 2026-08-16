---
title: "Evaluating Memory in Production Agents"
aliases:
  - "Letta Context-Bench V2"
  - "Context-Bench V2"
source_type: "article"
kind: "vendor-benchmark-report"
status: "verified"
year: 2026
publication_date: "2026-07-28"
publication_date_basis: "letta_visible_published_date"
source_updated_date: "2026-07-29"
source_updated_date_basis: "official_benchmark_json_generated_at"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Letta"
venue: "Letta Research"
url: "https://www.letta.com/blog/evaluating-memory-in-production-agents/"
pdf_url: ""
evidence_class: "vendor-benchmark-report"
metrics_status: "vendor-run-one-attempt-per-model-scenario"
created: 2026-08-16
updated: 2026-08-16
---

# Letta Context-Bench V2

## Summary

- Context-Bench V2 separates **memory usage** into adherence and retrieval, and **memory generation** into generalization and hygiene. This is the useful contribution: retrieving an old fact, following it, turning feedback into a durable rule, and repairing the memory structure are distinct capabilities.
- Generation hygiene tests whether an agent replaces stale guidance, removes duplication and contradictions, preserves scope and grounding, and maintains navigable progressive disclosure. Letta's examples show why appending another dated correction can produce a correct immediate response while degrading the agent's future memory.
- Scenarios are synthesized from failure modes observed in Letta's production traces. Each stateful, multi-turn run uses an initialized memory profile modeled on an internal long-running agent; some scenarios compare an original messy profile with a cleaned counterpart. Sonnet-5 runs the user simulator and GPT-5.6-Sol judges the trajectory against a scenario-specific rubric.
- In the article's reported pattern, retrieval is the closest capability across providers, OpenAI has the provider-level edge on adherence, and Anthropic's largest advantage is in memory generation. GPT-5.6-Sol carries most of OpenAI's generation performance, while Kimi-K3 is the strongest non-Anthropic model on generation. These are benchmark diagnostics, not a universal model ranking.
- The official default-slice JSON contains 68 scenarios (38 usage and 30 generation), nine model configurations, and 612 attempts. Counts were recomputed directly from the JSON; grouping attempts by `(model, scenario)` yields exactly one attempt in every published default-slice cell. No model score is reproduced here because a single attempt per cell does not support fine-grained rank claims.

## Evidence Boundary

This is a vendor-created, private benchmark derived from Letta's internal agents and traces. The public JSON exposes scenario metadata, scores, costs, and attempt records, but not a runnable task suite or the complete production-derived evaluation assets. One attempt per model/scenario, provider-specific default reasoning settings, a fixed simulator and judge, and no uncertainty estimates make small differences fragile. Use the four dimensions and the memory-repair failure modes as design guidance; do not treat the leaderboard as an independently reproduced ordering of models.

## Claims

- [[claims/Claim - Agent memory and skills create compounding improvement loops]]
- [[claims/Claim - Context management is an agent architecture choice]]

## Connections

- [[operations/agent memory]]
- [[operations/agent evals]]
- [[concepts/context evolution]]
- [[concepts/procedural memory]]
- [[sources/Letta Context-Bench]]

## Notes

- [Official article](https://www.letta.com/blog/evaluating-memory-in-production-agents/) (2026-07-28).
- [Official raw benchmark JSON](https://www.letta.com/evaluating-memory-in-production-agents/data/benchmark.json), whose `generated_at` field is `2026-07-29T02:57:49+00:00`.
- The earlier [[sources/Letta Context-Bench]] evaluates filesystem navigation and skill discovery. V2 changes the target to using, following, generating, and repairing persistent agent memory.
