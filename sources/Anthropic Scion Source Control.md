---
title: "Redesigning source control at Anthropic"
aliases: ["Scion source control"]
tags: [sources, code-factories]
source_type: "article"
status: "verified"
evidence_class: "vendor-production-report"
publication_date: "2026-10-13"
publication_date_basis: "visible_publication_date"
source_updated_date: "2026-10-15"
source_updated_date_basis: "visible_update_notice"
authors: ["Anthropic Engineering"]
venue: "Anthropic"
url: "https://www.anthropic.com/research/redesigning-source-control"
created: 2026-11-09
updated: 2026-11-09
---

# Anthropic Scion Source Control

## Mechanism and Evidence

Anthropic reports monorepo merge volume rising from about 2,500/day in May to over 30,000/day in September. Scion moves history, commit creation, and merges to a service, with content-addressed caching and sparse/on-demand working copies. Reported infrastructure savings concern this exceptional workload, not generic repositories.

The team could not sustain a global merge-queue lock at this scale and invested in post-merge/pre-deploy tests. This admits concurrent conflicts and depends on rapid detection and repair. Human review emphasizes change intent and system constraints.

## Boundaries

Vendor-reported, without a controlled productivity comparison. The article explicitly disclaims general suitability and notes unusually large internal token budgets. The monorepo is distinct from the Claude Code repository in [[sources/Claude Code Review at Agent Volume]], which retains a merge queue.

## Connections

- [[concepts/code factories]]
- [[operations/release engineering]]
- [[maps/Code Factory Playbook]]

## Primary Link

[Architecture and operating experience](https://www.anthropic.com/research/redesigning-source-control).
