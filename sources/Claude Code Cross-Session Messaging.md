---
title: "Message your other Claude Code sessions"
aliases:
  - "Claude Code Cross-Session Messaging"
  - "Claude Code peer messaging"
source_type: "docs"
kind: "session-messaging"
status: "verified"
year: 2026
publication_date: "2026-08-07"
publication_date_basis: "minimum_supported_version_npm_publication_date"
source_updated_date: "2026-08-24"
source_updated_date_basis: "snapshot_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Anthropic"
venue: "Claude Code Docs"
url: "https://code.claude.com/docs/en/cross-session-messaging"
pdf_url: ""
artifacts: []
created: 2026-08-24
updated: 2026-08-24
---

# Claude Code Cross-Session Messaging

## Summary

- Official Claude Code documentation for text messaging between independent sessions that the user starts and steers, rather than sessions spawned inside an agent team.
- Claude discovers reachable sessions with `ListAgents` and sends to a named target with `SendMessage`. Delivered messages carry the sender's session name and normally a reply address; a one-way cross-machine send can lack the reply address.
- An active receiver reads a delivered message between tool calls, without interrupting a running tool. An idle receiver starts a new turn with the message. A receiver can reply through the same mechanism.
- `crossSessionInbound` gives the receiver `accept`, `hold`, or `refuse` behavior. Incoming peer text cannot approve permissions, change configuration, or execute slash commands, and any resulting work remains subject to the receiver's permissions.
- Same-machine traffic uses a per-session Unix socket or Windows named pipe and does not pass through Anthropic servers. Cross-machine and web-session traffic uses Anthropic infrastructure.

## Harness Reading

- The important addition is an identified peer channel: discovery, sender identity, a reply path, wake-on-message behavior, inbound trust policy, and delivery feedback are explicit harness concerns.
- The channel is plain text only. It does not transfer files or conversation history, and it does not create a shared task list or team lead.
- The documentation describes reachable, running sessions and queues accepted messages while a receiver is mid-turn. It does not promise a restart-safe offline mailbox for a local session that has ended; held messages expire or end with the session under documented conditions.
- Delivery is bounded rather than unlimited: burst sends can be refused, repeated-message loops are throttled, and the receiver queues at most 50 accepted messages for Claude to read.
- `notify_when_idle` is a separate one-shot local subscription: it does not poll or spend tokens in the watched session and expires after 12 hours.

## Claims

- [[claims/Claim - Agent teams need explicit organization]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Connections

- [[systems/Claude Code]]
- [[sources/Claude Code Agent Teams]]
- [[concepts/cross-session agent communication]]
- [[concepts/agent teams]]
- [[operations/agent harnesses]]
- [[operations/durable sessions]]
- [[operations/permissions]]
- [[operations/worktree isolation]]
- [[maps/Agent Teams and Workforces Map]]

## Notes

- Canonical URL: https://code.claude.com/docs/en/cross-session-messaging
- Minimum versions: Claude Code v2.1.224 on macOS, Linux, and WSL 2; v2.1.234 on native Windows. The npm registry published v2.1.224 on 2026-08-07.
- Agent Teams remain a separate experimental feature with a lead, teammates, and shared task state; see [[sources/Claude Code Agent Teams]].
- Evidence boundary: this card records the official product contract. It does not infer exactly-once delivery, restart persistence, or reliability beyond the documented limits.
