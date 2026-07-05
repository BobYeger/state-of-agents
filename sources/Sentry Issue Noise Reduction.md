---
title: "Using a Transformer-Based Text Embeddings Model to Reduce Sentry Alerts by 40% and Cut Through Noise"
aliases:
  - "Sentry embeddings dedup"
source_type: "article"
kind: "signal-dedup"
status: "verified"
year: 2025
publication_date: "2025-02-05"
publication_date_basis: "vendor_blog_page"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Tillman Elser"
  - "Josh Ferge"
venue: "Sentry Blog (engineering)"
url: "https://blog.sentry.io/how-sentry-decreased-issue-noise-with-ai/"
pdf_url: ""
artifacts:
  - "raw/articles/sentry-issue-noise-reduction.md"
created: 2026-07-03
updated: 2026-07-05
---

# Sentry Issue Noise Reduction

## Summary

- Embeddings-based deduplication runs as a second stage behind traditional fingerprinting: only novel hashes are sent to Seer (Sentry's AI/ML service) for semantic matching, so the cheap deterministic path handles the bulk of events.
- A 161M-parameter transformer text-embeddings model encodes stack traces; nearest-neighbor lookup uses a PostgreSQL pgvector HNSW index; a match above a conservative threshold merges the new hash into the existing issue.
- Results: 40% reduction in new issues created; false-positive grouping rate "virtually zero" in testing; sub-100ms end-to-end latency maintained.
- GPU inference on NVIDIA L4 was ~4x faster than CPU; reranking the top-100 candidates added ~1% recall at negligible latency cost.

## Connections

- [[concepts/code factories]]
- [[concepts/issue tracker control plane]]
- [[sources/Sentry Seer]]
- [[sources/Sentry Issue Grouping v2]]

## Artifacts

- [[raw/articles/sentry-issue-noise-reduction.md]]

## Notes

- Canonical URL: https://blog.sentry.io/how-sentry-decreased-issue-noise-with-ai/
- The hybrid fingerprint-then-embed architecture, conservative threshold calibration, and pgvector/HNSW choices are the reusable mechanism details for any intake-gate dedup design.
- Superseded in part by the 2026 grouping v2 work (ModernBERT-based), which reports better numbers.
