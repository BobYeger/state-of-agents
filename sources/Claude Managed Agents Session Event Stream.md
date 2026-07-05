---
title: "Session event stream (Claude Managed Agents docs)"
aliases:
  - "Managed Agents events and streaming"
  - "managed-agents-2026-04-01 event stream"
source_type: "docs"
kind: "session-event-protocol"
status: "verified"
year: 2026
publication_date: "2026-04"
publication_date_basis: "beta_header_version_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Anthropic"
venue: "Claude Platform Docs"
url: "https://platform.claude.com/docs/en/managed-agents/events-and-streaming"
pdf_url: ""
artifacts:
  - "raw/docs/claude-managed-agents-session-event-stream.md"
created: 2026-07-03
updated: 2026-07-05
---

# Claude Managed Agents Session Event Stream

## Summary

- Protocol-grade spec for the Managed Agents session event stream (beta header `managed-agents-2026-04-01`): event type strings follow a `{domain}.{action}` convention — `user.*`/`system.message` inbound; `session.*`, `span.*`, `agent.*` outbound — with stream-only preview events `event_start`/`event_delta` as the exception.
- Mid-turn steering is a two-step protocol: send `user.interrupt` to stop the agent mid-execution, then a `user.message` to redirect; queued events carry `processed_at: null` until the harness handles them after preceding events finish.
- Streams are resumable by ID-dedup, not cursors: reconnect by opening a new stream first, listing full event history to seed seen-event-IDs, then tailing live while skipping duplicates. Deltas are never replayed ("no way to re-request missed deltas"), but buffered complete events (e.g. `agent.message`) always appear in history.
- Delta previews are best-effort: under load the server sheds deltas, delivering a contiguous prefix then silence — the buffered `agent.message` still arrives complete, so accumulated previews must never be treated as final. `span.model_request_end` is the guaranteed close signal even if a turn errors or is interrupted.
- Custom-tool pause protocol: `agent.custom_tool_use` is followed by `session.status_idle` with `stop_reason: requires_action` carrying blocking `event_ids[]`; the client executes the tools and returns `user.custom_tool_result` per id before the session transitions back to running.
- The delta wire format intentionally differs from the Messages API: one `event_start` then only `content_delta` events, with no per-content-block start/stop — Messages API accumulator code does not carry over.

## Claims

- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[operations/agent harnesses]]
- [[operations/durable sessions]]
- [[concepts/human-in-the-loop agents]]
- [[sources/Anthropic Managed Agents]]
- [[sources/Claude Managed Agents Define Outcomes]]
- [[sources/Claude Agent SDK Streaming vs Single Message]]

## Artifacts

- [[raw/docs/claude-managed-agents-session-event-stream.md]]

## Notes

- Canonical URL: https://platform.claude.com/docs/en/managed-agents/events-and-streaming
- Only first-party spec covering interrupt-then-redirect, queued-event semantics, and reconnect-after-disconnect in one place; the vault's other Managed Agents cards all point at blog posts.
- Beta-versioned surface (`managed-agents-2026-04-01`); event names and reconnect semantics may change across beta revisions. The date above is inferred from the beta header version string.
