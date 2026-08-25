---
title: "How We Built Our Knowledge Base"
aliases:
  - "Cerebras Knowledge"
  - "Cerebras enterprise knowledge base"
  - "Cerebras company brain"
source_type: "article"
kind: "vendor-engineering-report"
status: "verified"
year: 2026
publication_date: "2026-07-15"
publication_date_basis: "cerebras_visible_page_date"
source_updated_date: "2026-07-16"
source_updated_date_basis: "cerebras_article_modified_metadata"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Isaac Tai"
  - "Daniel Kim"
  - "Mike Gao"
venue: "Cerebras"
url: "https://www.cerebras.ai/blog/how-we-built-our-knowledge-base"
pdf_url: ""
evidence_class: "vendor-production-architecture-report"
metrics_status: "vendor-reported-adoption-without-quality-evaluation"
artifacts: []
created: 2026-08-25
updated: 2026-08-25
---

# How We Built Our Knowledge Base

## Summary

- Cerebras describes an internal organizational knowledge system used by people, automations, and agents. The company reports more than 15,000 questions per day roughly three months after launch and calls it one of its most widely adopted internal tools.
- Authoritative work remains in source-specific systems such as Slack, code repositories, documents, Jira, and internal databases. Connectors continuously copy and normalize that material into a common Postgres retrieval schema rather than forcing employees to author in one central wiki.
- Slack ingestion combines exact full-text search, embeddings, inverse-document-frequency signal, and age decay. It re-fetches a whole thread on each update, uses an LLM to distill a searchable question, summary, resolution, and code/system references, and separately embeds selected same-author message bursts that would be lost in a thread summary.
- Code repositories are indexed incrementally with CocoIndex while literal code search remains a separate `ripgrep` tool. Teams can add custom sources through small connector modules that emit the common row schema.
- Query-time orchestration runs planner-selected retrieval tools in parallel, fuses rankings with reciprocal rank fusion, deduplicates and diversifies candidates, reranks them, restores neighboring context, and synthesizes a cited answer. The web UI owns this full pipeline; MCP exposes narrower, mostly LLM-free retrieval primitives so an external agent can orchestrate them itself.
- Projects bundle relevant channels, repositories, databases, and document spaces into a default query scope. The article also names authentication, authorization, auditing, and analytics as a required layer, but does not document how source ACLs propagate into retrieval.

## Architectural Reading

This is a production example of [[concepts/organizational knowledge systems|organizational knowledge infrastructure]], not a generated company wiki. Its core move is to preserve ergonomic source systems while adding a common evidence interface over continuously refreshed copies. It is adjacent to [[concepts/LLM-maintained knowledge bases]] but moves more synthesis to query time and serves both humans and agents.

The design also separates retrieval from orchestration. MCP tools expose stable evidence primitives such as Slack, code, unified search, and expertise lookup; the calling agent decides which tools to combine. That makes the organizational evidence layer reusable across interfaces without turning one answer-generating agent into the only access path.

## Evidence Boundary

All architecture and adoption claims are first-party. The article gives no active-user denominator, answer-quality benchmark, productivity outcome, latency, cost, or controlled comparison. Its statement that structured Slack distillation increased accuracy “significantly” is unquantified and should not be read as a statistical result. The system serves humans, automations, and agents, but the article does not break the reported daily question volume down by caller type; query count is not a count of distinct users or needs.

The article names authentication, authorization, and audit, and separately describes repository file-path allowlists/denylists plus project scopes; it does not specify row-level ACL propagation, deletion, retention, or retrieval-time enforcement. A project is therefore a relevance scope, not an established security boundary. The article does not release the system or link an implementation repository; CocoIndex is only one open-source component. The system demonstrates retrieval and freshness, not autonomous learning, contradiction resolution, or self-improvement.

## Claims

- [[claims/Claim - Context management is an agent architecture choice]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Connections

- [[concepts/organizational knowledge systems]]
- [[concepts/LLM-maintained knowledge bases]]
- [[concepts/context retrieval]]
- [[operations/agent memory]]
- [[operations/permissions]]
- [[protocols/MCP]]
- [[maps/Context Management Map]]

## Notes

- Canonical article: https://www.cerebras.ai/blog/how-we-built-our-knowledge-base
- X article mirror, published July 16, 2026: https://x.com/cerebras/article/2077822555159945507
- No source content was copied into the vault.
