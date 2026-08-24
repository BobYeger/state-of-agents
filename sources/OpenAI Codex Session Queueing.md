---
title: "codex queue and session queueing"
aliases:
  - "OpenAI Codex Session Queueing"
  - "Codex queue"
source_type: "release"
kind: "session-queueing"
status: "verified"
year: 2026
publication_date: "2026-08-20"
publication_date_basis: "github_release_date"
source_updated_date: "2026-08-24"
source_updated_date_basis: "repository_snapshot_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "OpenAI"
venue: "OpenAI Codex GitHub"
url: "https://github.com/openai/codex/releases/tag/rust-v0.149.0"
pdf_url: ""
artifacts: []
created: 2026-08-24
updated: 2026-08-24
---

# Codex Session Queueing

## Summary

- Codex CLI v0.149.0 added `codex queue --thread <THREAD> --message <TEXT>` for sending a text follow-up to an existing local or remote session, selected by thread UUID or exact name.
- The command calls the App Server's experimental `thread/queue/add` method. The queue is ordered and stored in SQLite; completed and failed turns start the next queued submission, while interrupted turns leave it paused until explicitly started.
- Queueing wakes an idle loaded thread, but does not cold-resume an unloaded one. The record remains queued until the target is separately loaded or resumed and can accept the turn.
- The App Server queue contract also exposes experimental list, update, delete, reorder, and start methods. Those methods require `capabilities.experimentalApi = true`; the released CLI command exposes the narrower act of adding one nonempty text message.
- Queue records contain the target thread, user input, a stable submission ID, and a client user-message ID. The v0.149 schema has no sender identity or reply address, so this is best classified as durable user-turn injection rather than an identified peer-agent message protocol.

## Surface Boundary

- Stable App Server thread/turn methods let a client create, resume, read, and start turns in worker threads; the queue family is explicitly experimental.
- `codex queue` is a released human/CLI surface over `thread/queue/add`. It should not be conflated with the full experimental queue-management API.
- A separate main-branch change on 2026-08-24 added model-callable `codex_tui` task tools for listing, reading, waiting on, creating, forking, messaging, renaming, archiving, and restoring tasks. Its `send_message_to_thread` wraps the source thread ID into a delegated prompt and starts a target turn; it is not the v0.149 queue record format.
- That task-tools commit postdated v0.149.1, the latest formal release at this snapshot. Treat it as first-party implementation evidence, not as a released cross-session contract.

## Claims

- [[claims/Claim - Agent teams need explicit organization]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[systems/Codex]]
- [[sources/OpenAI Codex App Server Docs]]
- [[concepts/cross-session agent communication]]
- [[methods/codex thread orchestration]]
- [[operations/agent infrastructure]]
- [[operations/durable sessions]]
- [[operations/agent observability]]
- [[maps/Agent Teams and Workforces Map]]

## Notes

- Release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
- Released CLI implementation: https://github.com/openai/codex/blob/rust-v0.149.0/codex-rs/cli/src/queue_cmd.rs
- Experimental queue protocol and lifecycle: https://github.com/openai/codex/blob/rust-v0.149.0/codex-rs/app-server/README.md#example-queue-a-follow-up-user-turn-experimental
- SQLite queue schema: https://github.com/openai/codex/blob/rust-v0.149.0/codex-rs/state/queue_migrations/0001_queued_items.sql
- Main-branch TUI task-tools commit: https://github.com/openai/codex/commit/a8468330bb5f45e9f4d2ec630b01ea8c52908be3
- Evidence boundary: durability is established for the queued user-input record. The schema does not establish peer identity, request-response correlation, acknowledgment semantics beyond queue acceptance, or exactly-once effects in the receiving task.
