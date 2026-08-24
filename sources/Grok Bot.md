---
title: "Grok Bot"
aliases:
  - "GrokBot"
  - "xAI Grok Bot"
  - "SpaceXAI Grok Bot"
source_type: "article-and-product-documentation"
kind: "hosted-agent-product"
status: "verified"
year: 2026
publication_date: "2026-08-11"
publication_date_basis: "xai_article_structured_metadata"
source_updated_date: null
source_updated_date_basis: null
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "xAI"
venue: "xAI"
url: "https://x.ai/news/introducing-grok-bot"
pdf_url: ""
license: "proprietary"
license_url: ""
evidence_class: "vendor-product-announcement-and-documentation"
metrics_status: "vendor-description-without-systematic-evaluation"
artifacts: []
created: 2026-08-24
updated: 2026-08-24
---

# Grok Bot

## Summary

- Grok Bot is a proprietary hosted beta for persistent, named AI teammates. A Bot keeps its own conversation, role, learned context, routines, and preferences, and can use a browser, terminal, files, connectors, and MCP on a persistent cloud computer.
- Bots can send asynchronous messages directly to other Bots: the receiver wakes, handles the request, and can reply later. Group chats place two to six Bots in one visible conversation where people or Bots can address members, pass work, and preserve handoffs.
- The important execution boundary is user-scoped rather than Bot-scoped. All of one user's Bots share the same cloud VM, workspace files, browser sessions, app logins, and command-line credentials; separate screens permit parallel computer use but do not create separate security boundaries.
- Skills and routines can be learned from a live demonstration and rerun on demand or on a schedule. This is vendor-documented persistence and procedure reuse, not evidence that the system autonomously improves its underlying model or harness.

## Harness Reading

Grok Bot combines a persistent-agent product, a shared computer, and a collaboration surface. Direct messages supply a peer channel; group transcripts make handoffs inspectable; shared files and authenticated browser sessions reduce setup cost between specialists. The same shared substrate also expands the blast radius: a file, login, or credential available to one Bot is available across the user's Bot roster.

Consequential actions can pause for approval, and Auto Review can apply require-approval or always-allow rules. The documentation explicitly describes Auto Review as model-based and recommends least privilege. It instructs users to take control for passwords, verification codes, CAPTCHAs, and payment confirmations; execution on the user's local computer is a separate capability whose default is to ask every time.

## Evidence Boundary

The launch article and live documentation establish product behavior and operator controls, not the implementation of the underlying harness. They publish no controlled task benchmark, reliability rate, coordination ablation, cost comparison, or independent security evaluation. Grok Bot should therefore be tracked as a `hosted-product`, not as an open harness implementation.

Do not treat a Bot identity as isolation, infer that group chat prevents duplicate or conflicting work, or equate learned routines with model self-improvement. Grok Bot is also distinct from [[sources/Grok Build Harness]], the Apache-2.0 terminal coding harness.

## Connections

- [[concepts/cross-session agent communication]]
- [[concepts/agent teams]]
- [[operations/agent harnesses]]
- [[operations/agent memory]]
- [[operations/permissions]]
- [[operations/sandboxes]]
- [[maps/Harness Tracker]]

## Notes

- Launch article, August 11, 2026: https://x.ai/news/introducing-grok-bot
- Product overview and shared-computer boundary: https://docs.x.ai/grok-bot/overview
- Bot lifecycle and memory: https://docs.x.ai/grok-bot/bots
- Direct messaging, wake behavior, and group chats: https://docs.x.ai/grok-bot/chat-and-collaboration
- Approvals, Auto Review, local execution, and credential boundary: https://docs.x.ai/grok-bot/approvals-security-and-privacy
- Documentation reviewed August 24, 2026.
