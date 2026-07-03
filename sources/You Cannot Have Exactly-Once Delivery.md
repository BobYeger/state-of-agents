---
title: "You Cannot Have Exactly-Once Delivery"
aliases:
  - "exactly-once delivery impossibility"
source_type: "article"
kind: "delivery-semantics"
status: "verified"
year: 2015
publication_date: "2015-03-25"
publication_date_basis: "blog_post_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Tyler Treat"
venue: "Brave New Geek (blog)"
url: "https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/"
pdf_url: ""
created: 2026-07-03
updated: 2026-07-03
---

# You Cannot Have Exactly-Once Delivery

## Summary

- Canonical short argument that exactly-once delivery is impossible over unreliable channels, grounded in the Two Generals problem and the FLP impossibility result.
- Cleanly defines the three delivery semantics: at-most-once (ack before processing; loss possible), at-least-once (ack after processing; duplicates possible), exactly-once (impossible at the delivery layer).
- Prescription: make messages idempotent or dedupe — "either the messages themselves should be idempotent... or we remove the need for idempotency through deduplication."
- Design pattern: distribute immutable state changes or facts rather than mutable operations, letting at-least-once delivery simulate exactly-once semantics at the application level.

## Connections

- [[concepts/code factories]]
- [[operations/agent infrastructure]]
- [[operations/durable sessions]]
- [[sources/Armin Ronacher The Coming Loop]]
- [[sources/Restate Durable AI Loops]]

## Notes

- Canonical URL: https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/
- Standard citation for why agent task pickup must be designed at-least-once plus idempotent; the vault's task-queue discussion previously mentioned idempotency only in passing.
- Pre-LLM distributed-systems source (2015); applies to agent fleets wherever tasks flow through queues or messages between workers.
