---
title: "Codex App Server"
aliases:
  - "OpenAI Codex App Server Docs"
  - "Codex App Server Docs"
  - "Codex thread/turn protocol"
source_type: "docs"
kind: "harness-docs"
status: "verified"
year: 2026
publication_date: "2026-07-01"
publication_date_basis: "accessed_living_docs_no_visible_publication_date"
source_updated_date: "2026-08-24"
source_updated_date_basis: "snapshot_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "OpenAI"
venue: "OpenAI Developers"
url: "https://developers.openai.com/codex/app-server"
pdf_url: ""
artifacts:
  - "raw/docs/openai-codex-app-server.md"
created: 2026-07-01
updated: 2026-08-24
---

# Codex App Server

## Summary

- Official Codex docs for the local App Server protocol that exposes Codex as a client-controllable harness.
- Important because it defines the fundamental runtime objects behind Codex thread orchestration: thread, turn, item, streamed events, approval requests, and persistent session state.
- Provides the public analogue for the desktop tool surface used by coordinator threads: `thread/start`, `thread/resume`, `thread/fork`, `turn/start`, `turn/steer`, thread naming, archiving, compaction, and interruption.
- The v0.149 repository protocol also documents an experimental `thread/queue/*` family for durable future user turns. The released `codex queue` CLI is a narrower client of `thread/queue/add`; see [[sources/OpenAI Codex Session Queueing]].
- Keep `thread/inject_items`, `turn/steer`, `turn/start`, and `thread/queue/add` separate: they respectively append model-visible history, steer an active turn, start a turn now, and persist a future user turn.
- Best understood with [[sources/OpenAI Unlocking Codex Harness]], which explains why App Server exists as a stable JSON-RPC surface over Codex core.

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
- [[claims/Claim - Agent teams need explicit organization]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[systems/Codex]]
- [[operations/agent infrastructure]]
- [[operations/agent observability]]
- [[operations/durable sessions]]
- [[operations/permissions]]
- [[methods/codex thread orchestration]]
- [[methods/multi-agent orchestration]]
- [[sources/OpenAI Codex Session Queueing]]
- [[maps/Harness Tracker]]
- [[maps/Agent Teams and Workforces Map]]

## Artifacts

- [[raw/docs/openai-codex-app-server.md]]

## Notes

- Canonical URL: https://developers.openai.com/codex/app-server
- Open-source protocol reference: https://github.com/openai/codex/blob/main/codex-rs/app-server/README.md
- Publication date basis: living OpenAI Developers docs accessed on 2026-07-01, no stable visible publication date.
- The living OpenAI Developers page was rechecked on 2026-08-24; the queue family is documented in the versioned open-source protocol and remains experimental rather than part of the stable method catalog.
- Do not confuse public App Server method names with local `codex_app.*` bindings or the main-branch `codex_tui` task tools. They share underlying thread concepts but are separate product surfaces with different availability and message semantics.
