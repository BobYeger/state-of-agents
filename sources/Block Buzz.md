---
title: "Block Buzz engineering articles"
aliases:
  - "Block Buzz"
  - "Buzz!"
  - "Buzz: a workspace where humans and agents build together"
  - "A Buzz on your phone"
  - "Run your own Buzz relay"
  - "Buzz workspace"
  - "Buzz engineering launch"
source_type: "article"
kind: "vendor-architecture-corpus"
status: "verified"
year: 2026
publication_date: "2026-07-21"
publication_date_basis: "block_engineering_visible_date"
source_updated_date: "2026-07-31"
source_updated_date_basis: "latest_companion_article_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Tyler Longwell"
venue: "Block Engineering"
url: "https://engineering.block.xyz/blog/buzz"
pdf_url: ""
evidence_class: "vendor-architecture-and-operator-report"
metrics_status: "no-measured-multi-agent-or-productivity-results-formal-storage-safety-model-only"
artifacts:
  - "raw/articles/block-buzz-engineering-launch.md"
  - "raw/articles/block-buzz-mobile-security.md"
  - "raw/articles/block-buzz-relay-self-hosting.md"
created: 2026-08-02
updated: 2026-08-02
---

# Block Buzz engineering articles

## Summary

- Buzz is an open-source, self-hostable collaboration workspace built around a Nostr relay. Humans, agents, messages, workflows, repository events, and decisions share one signed event substrate.
- Its transferable idea is a **coordination and control plane**, not a new swarm algorithm: agents keep separate identities, communicate through ordinary channels, and leave durable discussion and decision history outside private model contexts.
- The engineering launch describes one frontier agent directing cheaper workers and agents spontaneously recruiting one another, but publishes no baseline, task set, score, cost table, or traces. These are operator observations rather than empirical findings.
- The mobile article states the sharp security boundary: Buzz agents typically run locally outside a sandbox with broad permission bypass. Owner-signature checks authenticate the direct command channel against relay impersonation and unauthorized commands; they do not contain execution or prevent indirect prompt injection.
- The self-hosting guide makes the operational model concrete: one Rust relay process plus PostgreSQL, Redis, and S3-compatible storage. The relay key is its signed identity; community selection is host-derived, and NIP-98 authentication separately requires exact scheme/host/port matching. Key rotation and host migration are therefore consequential in different ways.

## Architecture Reading

Buzz separates **authorization from authorship**: an agent acts under its own key and remains the attributed author even when an owner authorized it. Live telemetry/cancellation and durable encrypted memory/cost events are designed as different protocol objects. A channel can also become a branch/work unit whose conversation, patches, CI, review, and decision remain together.

The launch's portability language needs precision. A keypair is portable and signed history remains verifiable, but the current community runtime is a centralized relay with no peer replication. Portable identity does not automatically migrate relay-held history, memory, permissions, or reputation indexes.

## Security Reading

The phone article is more important than the generic “defined permissions” language in the announcement. If an agent runs outside a sandbox with ambient host credentials, knowing who sent a message is only one layer. The architecture still needs capability limits, egress control, isolation, and a policy for untrusted content the authorized owner asks the agent to inspect.

## Connections

- [[systems/Buzz]]
- [[operations/agent identity]]
- [[operations/sandboxes]]
- [[sources/Buzz Repository]]

## Artifacts

- [[raw/articles/block-buzz-engineering-launch]]
- [[raw/articles/block-buzz-mobile-security]]
- [[raw/articles/block-buzz-relay-self-hosting]]

## Evidence Boundary

The architecture, deployment shape, and disclosed security posture are first-party technical evidence. None of the four Buzz-specific posts publishes a measured multi-agent, productivity, or cost comparison; productivity, spontaneous-coordination, and scale claims are anecdotes. The launch's TLA+ material is bounded mechanized evidence about Git-storage safety, not swarm performance. Mobile privacy and self-hosting claims are design and operational descriptions rather than measured outcomes. Current implementation and protocol gaps are evaluated separately in [[sources/Buzz Repository]].

## Notes

- Corporate launch — Block, 2026-07-21 (reviewed; no distinct technical evidence, so not separately captured): https://block.xyz/inside/introducing-buzz-where-humans-and-agents-work-together
- Engineering launch — Tyler Longwell, 2026-07-21: https://engineering.block.xyz/blog/buzz
- Mobile/security — Tom Brow, 2026-07-29: https://engineering.block.xyz/blog/a-buzz-on-your-phone
- Self-hosting — Kalvin Chau, 2026-07-31: https://engineering.block.xyz/blog/run-your-own-buzz-relay
