---
title: "agentgateway — AI-native data plane for MCP, A2A, and LLM traffic"
aliases:
  - "agentgateway"
source_type: "repository"
kind: "agent-gateway"
status: "verified"
year: 2026
publication_date: "2026-06-22"
publication_date_basis: "github_release_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "agentgateway maintainers (originated at Solo.io)"
venue: "GitHub + Linux Foundation press release"
url: "https://github.com/agentgateway/agentgateway"
pdf_url: ""
created: 2026-07-03
updated: 2026-07-03
---

# agentgateway

## Summary

- Rust-based (61% Rust) unified proxy handling HTTP, gRPC, LLM provider APIs (OpenAI-compatible across OpenAI/Anthropic/Gemini/Bedrock/Vertex), MCP, and A2A traffic in one data plane. v1.3.1 released 2026-06-22; 3.6k GitHub stars.
- Donated to the Linux Foundation by Solo.io, announced 2025-08-25 at Open Source Summit Europe, with contributors from AWS, Cisco, Huawei, IBM, Microsoft, Red Hat, Shell, and Zayo.
- Joined the Agentic AI Foundation (AAIF) on 2026-06-04 as its fourth hosted project (after MCP, goose, and AGENTS.md); the project claims 300+ active contributors across 60+ organizations including CoreWeave, Adobe, Salesforce, and Amdocs.
- MCP "virtualization": federates multiple MCP tool servers behind one endpoint with per-tool access policies. Security stack includes JWT/OAuth/API-key auth, RBAC, external authz, mTLS, and declarative policies in Common Expression Language (CEL).
- Full Kubernetes Gateway API conformance; runs on bare metal, VMs, containers, and Kubernetes. LLM routing includes budget controls, guardrails/content filtering, and inference routing for self-hosted models.

## Connections

- [[operations/agent infrastructure]]
- [[protocols/MCP]]
- [[protocols/A2A]]
- [[protocols/agent protocol governance]]
- [[sources/Envoy AI Gateway 1.0]]
- [[sources/kagent]]

## Notes

- Canonical URL: https://github.com/agentgateway/agentgateway
- Contributor and star counts are project-reported and point-in-time (2026-07 fetch).
- Sits in the same niche as [[sources/Envoy AI Gateway 1.0]] but as a purpose-built Rust data plane rather than an Envoy extension; both now live under neutral foundations (AAIF/Linux Foundation vs CNCF).
