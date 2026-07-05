---
title: "Governed Shared Memory for Multi-Agent LLM Systems"
aliases:
  - "MemClaw"
  - "ArgusFleet"
source_type: "paper"
kind: "shared-memory-governance"
status: "verified"
year: 2026
publication_date: "2026-06-23"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2606.24535"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Yanki Margalit"
  - "Nurit Cohen-Inger"
  - "Erni Avram"
  - "Ran Taig"
  - "Oded Margalit"
venue: "arXiv (cs.MA)"
url: "https://arxiv.org/abs/2606.24535"
pdf_url: "https://arxiv.org/pdf/2606.24535"
artifacts:
  - "raw/papers/Governed Shared Memory for Multi-Agent LLM Systems.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# Governed Shared Memory for Multi-Agent LLM Systems

## Summary

- Formalizes the fleet-memory problem and names four failure modes: unauthorized leakage, stale propagation, contradiction persistence, and provenance collapse.
- Defines four systems-level governance primitives — scoped retrieval, temporal supersession (newer writes override older conflicting data), provenance tracking, and policy-governed memory propagation — mapped to four dimensions: scope, time, provenance, propagation (who may read, which version is current, where a memory came from, how it crosses agent boundaries).
- Implemented in MemClaw, a production multi-tenant memory service, and evaluated with ArgusFleet, a reproducible governance-testing harness.
- Provenance evaluation reconstructed 100% of depth-four derivation chains with correct writer identity at sub-second per-hop latency; propagation showed high intra-fleet visibility with zero cross-fleet leakage.
- Governance testing surfaced real architectural bugs: scope-enforcement gaps in sub-tenant credential access and ordering conflicts between synchronous duplicate detection and asynchronous contradiction resolution.

## Connections

- [[operations/agent memory]]
- [[concepts/multi-agent systems]]
- [[safety/agent safety and security]]
- [[sources/When Agents Misremember Collectively]]
- [[sources/Memory Poisoning Attacks in LLM Agents]]

## Artifacts

- [[raw/papers/Governed Shared Memory for Multi-Agent LLM Systems.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2606.24535
- The closest published match to the write-authority / conflict-resolution / namespacing / lesson-propagation-without-error-propagation problem for agent fleets, with a production implementation and named failure modes.
- Evaluation is against the authors' own MemClaw service; no comparison to other shared-memory systems is reported.
