---
title: "Cloud native agentic standards"
aliases:
  - "CNCF agentic standards"
source_type: "spec"
kind: "standards-framework"
status: "verified"
year: 2026
publication_date: "2026-03-23"
publication_date_basis: "cncf_blog_page"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "CNCF AI Technical Community Group (TCG)"
venue: "CNCF blog"
url: "https://www.cncf.io/blog/2026/03/23/cloud-native-agentic-standards/"
pdf_url: ""
artifacts:
  - "raw/protocols/cncf-cloud-native-agentic-standards.md"
created: 2026-07-03
updated: 2026-07-05
---

# CNCF Cloud Native Agentic Standards

## Summary

- First CNCF-published standards framework defining "agentic services" as autonomous, reasoning-capable container systems operating in event-driven microservice architectures.
- Covers four areas: general container best practices (least privilege, non-root, image scanning), control/communication protocols, observability, and governance/security (agent identity, tenancy isolation, data access).
- Names a concrete protocol stack: MCP (JSON-RPC 2.0 over HTTPS), Google's A2A, Google's AP2 cryptographic payment protocol, SPIFFE/SPIRE workload identity via SVIDs (JWT or X.509), and Kubernetes Gateway API Inference Extensions.
- Prescribes a MELT (Metrics, Events, Logs, Traces) observability stack with OpenTelemetry instrumentation for end-to-end agent tracing.
- Explicitly a living document "subject to a high-change revision cycle." The sibling CNCF TOC initiative #1746 ("Cloud-Native Foundations for Distributed Agentic Systems", accepted) is producing a whitepaper, a reference architecture, an "MCP-for-Clusters" proposal, and an Agent CRD schema.

## Connections

- [[protocols/agent protocol governance]]
- [[operations/agent infrastructure]]
- [[operations/agent observability]]
- [[protocols/AP2]]
- [[sources/kagent]]
- [[sources/OpenTelemetry GenAI Semantic Conventions]]

## Artifacts

- [[raw/protocols/cncf-cloud-native-agentic-standards.md]]

## Notes

- Canonical URL: https://www.cncf.io/blog/2026/03/23/cloud-native-agentic-standards/
- A vendor-neutral governance/identity/observability checklist rather than a testable conformance spec; treat the named protocol stack as CNCF's current endorsement snapshot, not a frozen standard.
- The document self-describes as high-churn; revisit when TOC initiative #1746 publishes its whitepaper and Agent CRD schema.
