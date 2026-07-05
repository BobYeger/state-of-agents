---
title: "Claude Agent SDK: Streaming Input vs Single Message mode"
aliases:
  - "Agent SDK streaming input mode"
  - "streaming-vs-single-mode"
source_type: "docs"
kind: "harness-input-modes"
status: "verified"
year: 2026
publication_date: "2026-07"
publication_date_basis: "docs_access_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Anthropic"
venue: "Claude Code Docs (code.claude.com)"
url: "https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode"
pdf_url: ""
artifacts:
  - "raw/docs/claude-agent-sdk-streaming-vs-single-message.md"
created: 2026-07-03
updated: 2026-07-05
---

# Claude Agent SDK Streaming vs Single Message

## Summary

- Streaming input mode — the default and recommended mode — runs the agent as a long-lived process fed by an AsyncGenerator of user messages; single message input explicitly does not support image attachments, dynamic message queueing, real-time interruption, or natural multi-turn conversation.
- Queued messages process sequentially with the ability to interrupt mid-queue; interruption is a first-class client action alongside message injection in the documented session sequence.
- Python `interrupt()` drain rule (from the SDK reference): after `interrupt()`, messages of the interrupted task — including a `ResultMessage` with subtype `"error_during_execution"` — remain in the stream and must be drained with `receive_response()` before reading the next query's response.
- Documented failure-mode gotchas: a TypeScript generator exception surfaces as the misleading "Claude Code process aborted by user"; a Python generator exception is logged at debug level and the session stalls silently without raising.
- Single-message mode is positioned for stateless environments (e.g. lambda); multi-turn there requires session resume via `continue`/`continue_conversation` options rather than a live stream.

## Claims

- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[operations/agent harnesses]]
- [[operations/durable sessions]]
- [[systems/Claude Code]]
- [[concepts/human-in-the-loop agents]]
- [[sources/Claude Managed Agents Session Event Stream]]
- [[sources/LangGraph Interrupts]]

## Artifacts

- [[raw/docs/claude-agent-sdk-streaming-vs-single-message.md]]

## Notes

- Canonical URL: https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode
- Primary source for which harness capabilities (interrupt, message queueing/injection, images) exist only on a persistent input stream — the queued-vs-injected distinction.
- Living docs page with no visible publication date; the date above is the access date. The Python drain rule is stated on the SDK reference page rather than this overview page.
