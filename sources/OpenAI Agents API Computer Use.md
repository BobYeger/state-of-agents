---
title: "Computer use in the OpenAI Agents API"
aliases: []
source_type: "docs"
kind: "managed-browser-runtime"
status: "verified"
year: 2026
publication_date: "2026-09-29"
publication_date_basis: "official_API_changelog_feature_date"
source_updated_date: "2026-10-05"
source_updated_date_basis: "documentation_access_date"
authors:
  - "OpenAI"
venue: "OpenAI API documentation"
url: "https://developers.openai.com/api/docs/guides/agents-api/tools/computer-use"
evidence_class: "official-runtime-documentation"
artifacts: []
created: 2026-10-05
updated: 2026-10-05
---

# OpenAI Agents API Computer Use

Adds a hosted browser to managed agent sessions, with website-origin approvals, private sign-in handling, saved browser activity, and recovery. The [September 29 changelog](https://developers.openai.com/api/docs/changelog) dates the addition.

Origin approval does not enforce confirmation for every consequential action. A completed browser operation is not a completed task. These are documented boundaries, not a measured success rate or an isolation proof.

[[sources/Mind2Web]] is an earlier research reference for generalizing web actions. Its offline action-prediction evaluation does not validate this service or replace end-to-end browser evaluation.

## Connections

- [[sources/OpenAI Agents API]]
- [[concepts/agent loop]]
- [[concepts/tool use]]
- [[operations/sandboxes]]
- [[maps/Agent Capability Research Lineage]]
