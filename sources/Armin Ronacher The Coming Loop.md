---
title: "The Coming Loop"
aliases:
  - "Armin Ronacher The Coming Loop"
  - "Harness-level loop"
source_type: "article"
kind: "practitioner-analysis"
status: "verified"
year: 2026
publication_date: "2026-06-23"
publication_date_basis: "visible_page_date"
source_updated_date: "2026-07-01"
source_updated_date_basis: "snapshot_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Armin Ronacher"
venue: "lucumr.pocoo.org"
url: "https://lucumr.pocoo.org/2026/6/23/the-coming-loop/"
pdf_url: ""
artifacts:
  - "raw/articles/armin-ronacher-the-coming-loop.md"
created: 2026-07-01
updated: 2026-07-01
---

# The Coming Loop

## Summary

- Ronacher distinguishes the inner coding-agent loop from the harness-level loop that keeps a task alive after the model would normally stop.
- The harness-level loop puts work into a queue, lets a machine attempt it, then decides whether to continue the same session, inject a new message, restart with modified context, or send the task elsewhere.
- Strong fit cases: porting, performance exploration, security scanning, research, mechanical transformations, and short-lived artifacts with useful verification signals.
- Main caution: loops can amplify local, defensive, over-complex code and widen comprehension debt when humans no longer understand what shipped.
- Future harness implication: task queues, orchestration, subagents, durable sessions, legible change review, and bounded human supervision become first-class engineering concerns.

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[concepts/loop engineering]]
- [[concepts/code factories]]
- [[operations/agent harnesses]]
- [[operations/durable sessions]]
- [[operations/agent observability]]
- [[operations/worktree isolation]]
- [[methods/ralph loop]]
- [[sources/Addy Osmani Loop Engineering]]
- [[sources/Andrew Ng Three Key Loops]]

## Artifacts

- [[raw/articles/armin-ronacher-the-coming-loop.md]]

## Notes

- Canonical URL: https://lucumr.pocoo.org/2026/6/23/the-coming-loop/
- Useful as a skeptical practitioner counterweight to optimistic loop/factory narratives.
