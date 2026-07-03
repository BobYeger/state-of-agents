---
title: "Announcing Envoy AI Gateway 1.0 — A Stable, Production-Ready AI Gateway"
aliases:
  - "Envoy AI Gateway"
source_type: "article"
kind: "llm-gateway"
status: "verified"
year: 2026
publication_date: "2026-06-23"
publication_date_basis: "vendor_blog_page"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Envoy AI Gateway project"
venue: "Envoy AI Gateway blog"
url: "https://aigateway.envoyproxy.io/blog/v1.0-release-announcement/"
pdf_url: ""
created: 2026-07-03
updated: 2026-07-03
---

# Envoy AI Gateway 1.0

## Summary

- v1.0 GA on 2026-06-23. Rate limiting, budgets, and quotas are token-aware with separate cost attribution for input, output, cached, and reasoning tokens — including capturing cached-token statistics from providers like Anthropic and Bedrock so prompt-caching cost attribution stays accurate.
- Token-based rate limiting exists because request-count limits do not control LLM usage; token rates can be limited per provider, per model, or per client over a defined time period, with route-scoped costs, fleet-wide defaults, and quota-aware routing.
- Single OpenAI-compatible API across 16 providers (OpenAI, Azure OpenAI, Gemini, Vertex, Bedrock, Anthropic, Mistral, Cohere, Groq, Together, DeepInfra, DeepSeek, Hunyuan, SambaNova, Grok, Tetrate ARS) with cross-provider translation.
- Ships a full MCP gateway: server multiplexing behind one endpoint, tool routing/filtering, and fine-grained CEL-based authorization over which tools clients can access, configured via an `MCPRoute` CRD.
- Observability: Prometheus GenAI token metrics, time-to-first-token and inter-token latency, OpenTelemetry tracing with OpenInference compatibility, and separate reasoning-token accounting for thinking models.
- Control-plane API promoted from v1alpha1 to v1beta1 with a no-breaking-changes commitment; built on CNCF's Envoy Gateway, originally a Bloomberg + Tetrate collaboration announced in early 2025. Maintainers span Tetrate, Bloomberg, Tencent, Netflix, and Nutanix.

## Connections

- [[operations/cost control]]
- [[operations/agent infrastructure]]
- [[operations/agent observability]]
- [[protocols/MCP]]
- [[sources/LiteLLM Proxy Budgets and Spend Tracking]]
- [[sources/agentgateway]]

## Notes

- Canonical URL: https://aigateway.envoyproxy.io/blog/v1.0-release-announcement/
- Release announcement by the project itself; feature claims (16 providers, reasoning-token attribution) are vendor-stated, though the project is open source and verifiable in-repo.
- Overlaps in role with [[sources/agentgateway]] — both are CNCF/LF-adjacent data planes for agent traffic; Envoy AI Gateway is Envoy-based and Kubernetes Gateway API-centric.
