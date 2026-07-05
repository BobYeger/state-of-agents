---
title: "Atomix: Timely, Transactional Tool Use for Reliable Agentic Workflows"
aliases:
  - "Atomix"
source_type: "paper"
kind: "transactional-tool-use"
status: "verified"
year: 2026
publication_date: "2026-02-16"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2602.14849"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Bardia Mohammadi"
  - "Nearchos Potamitis"
  - "Lars Klein"
  - "Akhil Arora"
  - "Laurent Bindschaedler"
venue: "arXiv (v1 2026-02-16, v2 2026-05-29)"
url: "https://arxiv.org/abs/2602.14849"
pdf_url: "https://arxiv.org/pdf/2602.14849"
artifacts:
  - "raw/papers/Atomix - Timely, Transactional Tool Use for Reliable Agentic Workflows.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# Atomix

## Summary

- Names the concrete failure modes of agent orchestrators that mishandle tool side effects: partial effects, losing-branch residue, stale writes, and irreversible sends.
- Diagnosis: orchestrators conflate two concerns — which effects must settle together (atomicity scope) vs when earlier conflicting work can no longer interfere (timeliness).
- Mechanism: progress-aware transactions that record reads and effects during execution, seal a transaction when its data footprint completes, and commit only after per-resource frontiers confirm no earlier conflicting work remains.
- Settlement policy stratifies effects: bufferable effects are released, reversible external effects accepted as final, irreversible effects gated; on abort, unreleased effects are suppressed and reversible externalized effects compensated.
- Reports microsecond-scale wrapper overhead relative to tool latency, plus clean recovery under injected faults and isolation of contending or speculative work on representative agent workloads.

## Claims

- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[operations/agent infrastructure]]
- [[operations/durable sessions]]
- [[concepts/tool-use contracts]]
- [[sources/Restate Durable AI Loops]]
- [[sources/Temporal OpenAI Agents SDK Integration]]

## Artifacts

- [[raw/papers/Atomix - Timely, Transactional Tool Use for Reliable Agentic Workflows.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2602.14849
- The strongest 2026 treatment of concurrency semantics for multi-writer agent execution: named patterns (seal/commit/settle, per-resource frontiers) for the stale-write and idempotent-retry problems.
- Research prototype; not yet validated inside a production orchestrator or a mainstream agent framework.
