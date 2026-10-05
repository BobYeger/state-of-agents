---
title: "How We Built Safety Into Muse"
source_type: "article"
kind: "personal-agent-runtime-architecture"
status: "verified"
year: 2026
publication_date: "2026-09-08"
publication_date_basis: "official_engineering_blog_date"
source_updated_date: "2026-10-05"
source_updated_date_basis: "accessed_snapshot"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Tarek Sheasha"
venue: "Meta AI Research"
url: "https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse"
pdf_url: ""
artifacts: []
created: 2026-10-05
updated: 2026-10-05
---

# Meta Muse Security Architecture

## Summary

- Meta documents a per-user Linux VM. Its Hatch agent harness, workspace and generated tools run inside a `systemd-nspawn` container. Durable application state resides separately in Postgres.
- A host-side Sentinel agent authorizes connector actions and network egress. Separate credential storage supplies surrogate tokens; real credentials are inserted only at the authorized network boundary. Built-in connector logic runs in restricted workers outside the agent container.
- Approvals travel through structured UI directly to Sentinel and have explicit scopes and lifetimes. Browser subagents receive accessibility-tree observations through a separate broker, without arbitrary page JavaScript. Kernel-level data-flow tracking adjusts egress approvals after processes read user data.

## Evidence and Limits

- This is a vendor architecture disclosure, not an independently validated security proof. It describes red teaming and bug bounties without product-level attack-success rates; Meta explicitly acknowledges remaining prompt-injection risk.
- The article explicitly cites [[sources/Willison Lethal Trifecta]]. It does not establish adoption of other similarly structured research systems.
- Confidential VM protection against provider access is described as forthcoming, distinct from the launched isolation design.
- Builder question: can action authority remain outside mutable agent code while preserving usable approval frequency?

## Connections

- [[sources/Meta Muse]]
- [[systems/personal assistant agents]]
- [[concepts/persistent personal agents]]
- [[operations/permissions]]
- [[safety/prompt injection]]
- [[safety/sandbox escape and credential exposure]]
