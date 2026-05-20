---
title: "Delta Channels: Evolving our Runtime for Long-Running Agents"
aliases:
  - "Delta Channels"
source_type: "article"
status: "verified"
year: 2026
publication_date: "2026-05-12"
publication_date_basis: "langchain_visible_published_date"
source_updated_date: null
source_updated_date_basis: null
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Sydney Runkle"
venue: "LangChain Blog"
url: "https://www.langchain.com/blog/delta-channels-evolving-agent-runtime"
pdf_url: ""
artifacts:
  - "raw/articles/langchain-delta-channels.md"
created: 2026-05-20
updated: 2026-05-20
---

# Delta Channels

## Summary

- Runtime checkpointing primitive for long-running agents that stores state deltas rather than full snapshots at every step.
- Important because durable execution, replay, observability, and human-in-the-loop recovery become expensive when session histories and filesystem state grow.
- Concrete infrastructure lever for keeping long-running agent state inspectable without quadratic storage blowup.

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Connections

- [[operations/durable sessions]]
- [[operations/agent observability]]
- [[operations/cost control]]
- [[operations/agent infrastructure]]

## Artifacts

- [[raw/articles/langchain-delta-channels.md]]

## Notes

- Canonical URL: https://www.langchain.com/blog/delta-channels-evolving-agent-runtime
