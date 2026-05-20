---
title: "Build Long-running AI agents that pause, resume, and never lose context with ADK"
aliases:
  - "Google ADK durable agents"
  - "ADK pause resume agents"
source_type: "article"
status: "verified"
year: 2026
publication_date: "2026-05-12"
publication_date_basis: "google_developers_visible_published_date"
source_updated_date: null
source_updated_date_basis: null
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Shubham Saboo"
  - "Eric Dong"
venue: "Google Developers Blog"
url: "https://developers.googleblog.com/build-long-running-ai-agents-that-pause-resume-and-never-lose-context-with-adk/"
pdf_url: ""
artifacts:
  - "raw/articles/google-adk-durable-agents.md"
  - "raw/repositories/google-adk-durable-agents-readme.md"
created: 2026-05-20
updated: 2026-05-20
---

# Google ADK durable agents

## Summary

- Production tutorial for long-running agents that pause, resume, and wake on events rather than replaying raw chat history.
- The core architecture is durable memory schemas, explicit state machines, event-driven dormancy gates, and multi-agent delegation.
- Important corrective to "just add context": the agent state is explicit, durable, and decoupled from conversation transcript bulk.

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Connections

- [[concepts/durable dormant agents]]
- [[concepts/context engineering]]
- [[operations/durable sessions]]
- [[operations/agent harnesses]]
- [[systems/Google ADK]]

## Artifacts

- [[raw/articles/google-adk-durable-agents.md]]
- [[raw/repositories/google-adk-durable-agents-readme.md]]

## Notes

- Canonical URL: https://developers.googleblog.com/build-long-running-ai-agents-that-pause-resume-and-never-lose-context-with-adk/
