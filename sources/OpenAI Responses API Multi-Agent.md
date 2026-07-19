---
title: "Multi-agent in the Responses API"
aliases:
  - "OpenAI Responses API Multi-Agent"
  - "Responses API multi-agent"
source_type: "docs"
kind: "multi-agent-api"
status: "verified"
year: 2026
publication_date: "2026-07-13"
publication_date_basis: "accessed_living_docs_no_visible_publication_date"
source_updated_date: "2026-07-13"
source_updated_date_basis: "snapshot_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "OpenAI"
venue: "OpenAI Developers"
url: "https://developers.openai.com/api/docs/guides/responses-multi-agent"
pdf_url: ""
artifacts:
  - "raw/docs/openai-responses-api-multi-agent.md"
created: 2026-07-13
updated: 2026-07-13
---

# Multi-agent in the Responses API

## Summary

- Beta API for GPT-5.6 models in which a root agent can create a tree of subagents, message or interrupt them, assign follow-up work, wait for results, and synthesize the final response. Agents share the request's model and tools but keep separate bounded contexts.
- OpenAI recommends multi-agent execution for concrete independent workstreams such as parallel codebase exploration, research, implementation, testing, or competing hypotheses. It recommends one agent for ordered reasoning chains, frequent writes to shared mutable state, or workflows dominated by one slow external operation.
- The default and recommended `max_concurrent_subagents` is three across the whole tree. The API sets no fixed tree-depth or total-subagent limit, so the concurrency cap, token budget, and spawning instructions are the practical controls.
- HTTP and WebSocket expose the same orchestration semantics, but WebSocket is recommended for tool-heavy and long-running work because function outputs can be injected as they arrive without waiting for a whole response continuation.
- Enabling multi-agent also enables automatic server-side compaction independently for the root and every subagent. Manual `/responses/compact`, `reasoning.summary`, and `max_tool_calls` are not supported in the beta, making per-agent compaction behavior part of the API contract.

## Claims

- [[claims/Claim - Agent teams need explicit organization]]
- [[claims/Claim - Context management is an agent architecture choice]]

## Connections

- [[concepts/subagent context isolation]]
- [[methods/multi-agent orchestration]]
- [[operations/agent harnesses]]
- [[operations/agent observability]]
- [[operations/cost control]]
- [[systems/OpenAI Agents SDK]]
- [[sources/OpenAI GPT-5.6]]

## Artifacts

- [[raw/docs/openai-responses-api-multi-agent.md]]

## Notes

- Canonical URL: https://developers.openai.com/api/docs/guides/responses-multi-agent
- Living beta documentation snapshot from 2026-07-13; item schemas and unsupported features may change.
- The API's agents use the same model and tool surface. Its value comes from parallelism and context isolation, not heterogeneous specialist models.
