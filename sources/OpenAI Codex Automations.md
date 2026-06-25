---
title: "Automations"
aliases:
  - "Codex Automations"
  - "OpenAI Codex Automations"
  - "Codex thread automations"
source_type: "docs"
kind: "harness-docs"
status: "verified"
year: 2026
publication_date: "2026-06-24"
publication_date_basis: "accessed_living_docs_no_visible_publication_date"
source_updated_date: "2026-06-24"
source_updated_date_basis: "manual_fetch_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "OpenAI"
venue: "OpenAI Codex Docs"
url: "https://developers.openai.com/codex/app/automations"
pdf_url: ""
artifacts: []
created: 2026-06-24
updated: 2026-06-24
---

# Automations

## Summary

- Official Codex docs for recurring background tasks and thread automations in the Codex app.
- Relevant to [[concepts/loop engineering]] because thread automations are heartbeat-style recurring wake-up calls attached to a thread.
- The closest Codex analogue to Claude Code `/loop` is a thread automation, not Codex `/goal`: `/goal` is a persistent objective, while thread automation is a scheduled recurrence surface.
- Automations can run standalone or attached to a thread, can use skills and plugins, and inherit the user's sandbox and policy configuration.

## Connections

- [[sources/OpenAI Codex Using Goals]]
- [[sources/Claude Code Scheduled Tasks]]
- [[concepts/loop engineering]]
- [[operations/agent harnesses]]
- [[operations/cost control]]
- [[operations/permissions]]

## Harness Reading

Use automations when the agent should wake on a cadence: polling CI, checking PR status, reminding the thread to continue a review loop, or recurring research and triage. Use a thread automation when the next run should preserve the current conversation context. Use standalone or project automations when each run should be independent or appear as a separate automation run.

## Notes

- Canonical URL: https://developers.openai.com/codex/app/automations
- This note was created from the current Codex manual snapshot fetched on 2026-06-24.
