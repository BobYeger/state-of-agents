---
title: "kagent — Kubernetes-native AI agent runtime"
aliases:
  - "kagent"
source_type: "docs"
kind: "k8s-agent-runtime"
status: "verified"
year: 2025
publication_date: "2025-05-22"
publication_date_basis: "cncf_sandbox_acceptance_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "kagent maintainers / Solo.io"
venue: "kagent.dev docs + CNCF project page"
url: "https://kagent.dev/docs/kagent/introduction/what-is-kagent"
pdf_url: ""
artifacts:
  - "raw/docs/kagent.md"
created: 2026-07-03
updated: 2026-07-05
---

# kagent

## Summary

- Kubernetes-native AI agent runtime accepted as a CNCF Sandbox project on 2025-05-22; created at Solo.io with first commit 2025-01-21. CNCF health score 78, 2,807 GitHub stars (+153% YoY), 989 contributing orgs as of mid-2026.
- Agents are defined as Kubernetes CRDs (Agent, ModelConfig, ToolServer) — versioned in Git, reviewed in PRs, deployed via kubectl/GitOps, making agent definitions cluster-native declarative workloads.
- The engine builds on Google's ADK with Go and Python runtimes and can also wrap LangGraph/CrewAI/custom frameworks; A2A is first-class for agent-to-agent discovery and delegation, and MCP tooling arrives via the companion kmcp project.
- Ships built-in agents integrating Kubernetes, Argo, Istio, Prometheus, Grafana, and Helm; includes human-in-the-loop tool-approval gates, vector-backed long-term memory, Postgres-backed storage, and OpenTelemetry tracing plus Prometheus metrics.
- As of June 2026, kagent can schedule agents onto Agent Substrate (Solo.io + Google) instead of 1:1 agent-to-pod, gaining snapshot/suspend-resume and sandboxed execution.

## Connections

- [[operations/agent infrastructure]]
- [[operations/agent observability]]
- [[protocols/A2A]]
- [[protocols/MCP]]
- [[systems/Google ADK]]
- [[concepts/human-in-the-loop agents]]

## Artifacts

- [[raw/docs/kagent.md]]

## Notes

- Canonical URL: https://kagent.dev/docs/kagent/introduction/what-is-kagent
- Publication date is the CNCF Sandbox acceptance date; the docs themselves are undated and continuously updated (facts reflect a 2026-07 fetch).
- Star counts and CNCF health-score figures are point-in-time and drift quickly; the durable fact is the CRD-based, GitOps-reviewable agent-definition model.
