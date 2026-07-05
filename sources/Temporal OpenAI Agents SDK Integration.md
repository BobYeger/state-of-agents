---
title: "Production-ready agents with the OpenAI Agents SDK + Temporal"
aliases:
  - "Temporal OpenAI Agents SDK integration"
source_type: "article"
kind: "durable-execution"
status: "verified"
year: 2025
publication_date: "2025-07-30"
publication_date_basis: "vendor_blog_page"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Cornelia Davis"
venue: "Temporal blog"
url: "https://temporal.io/blog/announcing-openai-agents-sdk-integration"
pdf_url: ""
artifacts:
  - "raw/articles/temporal-openai-agents-sdk-integration.md"
created: 2026-07-03
updated: 2026-07-05
---

# Temporal OpenAI Agents SDK Integration

## Summary

- The reference mapping of durable execution onto an agent harness: the agent orchestration loop runs as a Temporal Workflow while every agent/LLM invocation and tool call executes as a Temporal Activity; OpenAI made `Runner` an abstract base class specifically so Temporal could supply an Activity-creating implementation.
- Event history records each Activity invocation, its arguments, completion status, and return values; after a crash the workflow replays deterministically and picks up where it left off without re-running completed steps or re-spending tokens.
- Explicitly targets three failure classes: rate-limited LLMs (automatic retry when capacity returns), sporadic network connectivity, and process crashes.
- Minimal code delta: a plain Agents SDK loop becomes durable by wrapping it in `@workflow.defn`/`@workflow.run` — developers keep `await Runner.run(agent, input=prompt)` and gain durability via configuration.
- Launched in Public Preview July 2025 (Python SDK); reached General Availability 2026-03-23.
- Each microagent can run in its own process or thread for loose coupling and independent scaling; workflows can span days or weeks with state checkpointed at every transition.

## Connections

- [[operations/durable sessions]]
- [[operations/agent harnesses]]
- [[operations/agent infrastructure]]
- [[systems/OpenAI Agents SDK]]
- [[concepts/durable dormant agents]]
- [[sources/Restate Durable AI Loops]]

## Artifacts

- [[raw/articles/temporal-openai-agents-sdk-integration.md]]

## Notes

- Canonical URL: https://temporal.io/blog/announcing-openai-agents-sdk-integration
- Vendor announcement post; the July 2025 page was later updated to reflect the 2026-03-23 GA, so preview-era and GA-era details are mixed on one page.
