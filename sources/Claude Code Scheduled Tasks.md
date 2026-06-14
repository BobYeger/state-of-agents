---
title: "Run prompts on a schedule"
aliases:
  - "Claude Code Scheduled Tasks"
  - "Claude Code /loop"
  - "/loop"
source_type: "docs"
kind: "harness-docs"
status: "verified"
year: 2026
publication_date: "2026-06-14"
publication_date_basis: "accessed_living_docs_no_visible_publication_date"
source_updated_date: "2026-06-14"
source_updated_date_basis: "snapshot_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Anthropic"
venue: "Claude Code Docs"
url: "https://code.claude.com/docs/en/scheduled-tasks"
pdf_url: ""
artifacts:
  - "raw/docs/claude-code-scheduled-tasks.md"
created: 2026-06-14
updated: 2026-06-14
---

# Run prompts on a schedule

## Summary

- Official Claude Code docs for scheduled prompts: `/loop`, `loop.md`, and cron tools rerun prompts on a cadence inside the current Claude Code session.
- Important because it turns a prompt into a harness-managed timed control loop: the runtime owns cadence, task identity, expiry, resume behavior, and low-priority scheduling between turns.
- The docs distinguish `/loop` from `/goal`: `/goal` continues after each turn until a completion condition is met, while `/loop` continues after a time interval until stopped, expired, or judged complete.
- Operational limits matter: scheduled tasks are local and session-scoped, recur for up to 7 days, cap at 50 tasks per session, apply scheduler jitter, and do not catch up on missed runs after Claude Code is closed.

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[systems/Claude Code]]
- [[operations/agent harnesses]]
- [[operations/agent infrastructure]]
- [[operations/durable sessions]]
- [[operations/agent observability]]
- [[operations/permissions]]
- [[methods/ralph loop]]
- [[concepts/loop engineering]]

## Artifacts

- [[raw/docs/claude-code-scheduled-tasks.md]]

## Notes

- Canonical URL: https://code.claude.com/docs/en/scheduled-tasks
- Publication date is the access date because the living docs page did not expose a stable publication date in this pass.
- Treat `/loop` as a loop-engineering primitive, not as a durable workflow runtime: it is local, session-scoped, and timer-driven.
