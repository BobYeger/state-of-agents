---
title: "MCP Events in ChatGPT"
aliases: []
source_type: "docs"
kind: "event-triggered-agent-runtime"
status: "verified"
year: 2026
publication_date: null
publication_date_basis: "living_docs_no_exact_initial_release_date_verified"
source_updated_date: "2026-10-05"
source_updated_date_basis: "documentation_access_date"
authors:
  - "OpenAI"
venue: "OpenAI Developers"
url: "https://developers.openai.com/plugins/build/mcp-events"
evidence_class: "official-integration-documentation-for-draft-extension"
artifacts: []
created: 2026-10-05
updated: 2026-10-05
---

# OpenAI MCP Events

Servers expose event discovery and subscription methods; matching updates reach subscribed chats through signed webhooks. The documentation specifies persistence, refresh, revocation, retry identity, and out-of-order delivery. Receipt acknowledgment is separate from asynchronous processing.

The integration uses a draft MCP Events extension and supports webhook delivery, not every delivery/control mode in the draft. Its appearance in the [September 28–October 2 recap](https://learn.chatgpt.com/docs/whats-new/september-28-october-2-2026) is not proof of an exact launch date.

## Evidence Boundary

An implementation contract, not proof that proactive intervention is useful or that downstream effects occur exactly once.

## Connections

- [[concepts/event-driven agents]]
- [[concepts/background agents]]
- [[protocols/MCP]]
- [[sources/Hearsay-II]]
- [[sources/SCLATE]]
