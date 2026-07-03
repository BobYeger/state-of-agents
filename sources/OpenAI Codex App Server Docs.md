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
source_updated_date: "2026-07-01"
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
updated: 2026-07-01
---

# Codex App Server

## Summary

- Official Codex docs for the local App Server protocol that exposes Codex as a client-controllable harness.
- Important because it defines the fundamental runtime objects behind Codex thread orchestration: thread, turn, item, streamed events, approval requests, and persistent session state.
- Provides the public analogue for the desktop tool surface used by coordinator threads: `thread/start`, `thread/resume`, `thread/fork`, `turn/start`, `turn/steer`, thread naming, archiving, compaction, and interruption.
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
- [[maps/Harness Tracker]]
- [[maps/Agent Teams and Workforces Map]]

## Artifacts

- [[raw/docs/openai-codex-app-server.md]]

## Notes

- Canonical URL: https://developers.openai.com/codex/app-server
- Open-source protocol reference: https://github.com/openai/codex/blob/main/codex-rs/app-server/README.md
- Publication date basis: living OpenAI Developers docs accessed on 2026-07-01, no stable visible publication date.
- Do not confuse the public app-server method names with the local `codex_app.*` tool names exposed inside this Codex desktop environment. They map to the same conceptual control plane, but `codex_app.*` is a session-local tool binding, not the public API.
