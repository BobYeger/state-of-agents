---
title: "Running Agents on Kubernetes with Agent Sandbox"
aliases:
  - "Agent Sandbox"
  - "Sandbox CRD"
source_type: "article"
kind: "k8s-sandbox-runtime"
status: "verified"
year: 2026
publication_date: "2026-03-20"
publication_date_basis: "kubernetes_blog_page"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Kubernetes SIG Apps (kubernetes-sigs/agent-sandbox)"
venue: "Kubernetes blog (kubernetes.io)"
url: "https://kubernetes.io/blog/2026/03/20/running-agents-on-kubernetes-with-agent-sandbox/"
pdf_url: ""
created: 2026-07-03
updated: 2026-07-03
---

# Kubernetes Agent Sandbox

## Summary

- Upstream Kubernetes project (SIG Apps, kubernetes-sigs/agent-sandbox) introducing a Sandbox CRD for isolated, stateful, singleton agent workloads. The post argues explicitly that StatefulSets, Services, and PVCs mismatch agent workloads, which are mostly idle with bursts of activity.
- Native runtime isolation via gVisor and Kata Containers for untrusted agent-generated code; each Sandbox gets a stable hostname and network identity, which supports multi-agent discovery.
- SandboxWarmPool plus SandboxClaim extensions eliminate the roughly 1-second pod cold start by claiming pre-provisioned sandboxes from a warm pool defined by a SandboxTemplate.
- Lifecycle management scales idle environments to zero and resumes with state preserved — designed for long-running, mostly-idle agents.
- The repository (github.com/kubernetes-sigs/agent-sandbox) released v0.5.0 on 2026-06-24, ships Go and Python SDKs, has 3,000+ stars, and remains pre-GA.

## Connections

- [[operations/sandboxes]]
- [[operations/agent infrastructure]]
- [[concepts/durable dormant agents]]
- [[safety/sandbox escape and credential exposure]]
- [[sources/kagent]]
- [[sources/Cloudflare Sandboxing AI Agents]]

## Notes

- Canonical URL: https://kubernetes.io/blog/2026/03/20/running-agents-on-kubernetes-with-agent-sandbox/
- This is Kubernetes itself (a SIG Apps subproject), not a vendor, standardizing the agent runtime primitive — the self-hosted counterpart to vendor-cloud sandbox offerings already in the vault.
- Pre-GA: the Sandbox CRD and its extensions (SandboxWarmPool, SandboxClaim, SandboxTemplate) may change before a stable release; star counts and version numbers reflect a 2026-07 fetch.
