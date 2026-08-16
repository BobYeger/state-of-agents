---
title: "Structured memory filtering with metadata in AgentCore Memory"
aliases:
  - "AWS AgentCore Structured Memory Filtering"
  - "AgentCore Memory metadata filtering"
source_type: "article"
kind: "vendor-technical-report"
status: "verified"
year: 2026
publication_date: "2026-07-01"
publication_date_basis: "aws_blog_visible_date"
source_updated_date: null
source_updated_date_basis: null
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Akarsha Sehwag"
  - "Abhi Verma"
  - "Lior Shoval"
venue: "AWS Machine Learning Blog"
url: "https://aws.amazon.com/blogs/machine-learning/structured-memory-filtering-with-metadata-in-agentcore-memory/"
pdf_url: ""
evidence_class: "vendor-technical-report"
metrics_status: "vendor-reported-small-test"
created: 2026-08-16
updated: 2026-08-16
---

# AWS AgentCore Structured Memory Filtering

## Summary

- AgentCore Memory layers structured metadata filters inside namespace isolation and applies them **before** vector similarity search. Namespaces establish the primary user, tenant, patient, or client boundary; metadata narrows that entity's memories by dimensions such as department, priority, agent role, workflow step, or time.
- The lifecycle is configuration, ingestion, and retrieval: declare indexed keys and a per-strategy schema; attach values or let an LLM infer them during extraction; then combine up to five filters with `AND` semantics before semantic search. A memory resource supports up to ten indexed keys, and adding a key does not backfill existing records.
- `STRICTLY_CONSISTENT` keys provide a deterministic path for application-known values. Up to three indexed `STRING` keys per strategy pass through unchanged, and AgentCore partitions extraction and consolidation by their exact value combination so records from different departments, tenants, or compliance classes do not merge.
- AWS reports that metadata filtering raised QA accuracy from 40% to 64% on a 151-question, LoCoMo-style multi-session test. On the undisclosed-size subset requiring contextual boundaries such as time, priority, or department, accuracy rose from 16% to 69%; AWS says time-bounded questions improved most.
- Builder guidance is narrower than the benchmark claim: use deterministic structure for known boundaries and provenance, LLM inference only for attributes that must be inferred, and namespace isolation for security. AWS explicitly warns against replacing tenant namespaces with a `tenant_id` filter that every caller must remember to apply.

## Evidence Boundary

The accuracy result is from a small, vendor-authored 151-question test, not the canonical LoCoMo benchmark. AWS does not publish the test set, contextual-boundary subset size, evaluated model and harness, number of runs, raw predictions, or uncertainty. The result supports testing structured pre-filtering where semantic similarity crosses known business boundaries; it does not establish a general 24-point gain for AgentCore or metadata filtering.

## Claims

- [[claims/Claim - Context management is an agent architecture choice]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[operations/agent memory]]
- [[concepts/context retrieval]]
- [[concepts/shared agent memory]]
- [[concepts/multi-agent systems]]

## Notes

- [Official AWS article](https://aws.amazon.com/blogs/machine-learning/structured-memory-filtering-with-metadata-in-agentcore-memory/) (2026-07-01).
- [Current structured-metadata documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/long-term-memory-metadata.html) and [SearchCriteria API reference](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_SearchCriteria.html).
- Release history: [metadata for long-term memory](https://aws.amazon.com/about-aws/whats-new/2026/05/agentcore-longterm-memory-metadata/) (2026-05-06) and [strictly consistent metadata](https://aws.amazon.com/about-aws/whats-new/2026/05/agentcore-memory-scmetadata/) (2026-06-15).
