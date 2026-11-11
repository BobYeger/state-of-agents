---
title: "Cursor Projects and Agent SDK"
aliases: ["Cursor Projects", "Cursor Agent SDK"]
tags: [sources, code-factories]
source_type: "grouped articles"
status: "verified"
evidence_class: "vendor-product-and-operator-report"
publication_date: "2026-09-10"
publication_date_basis: "projects_visible_publication_date"
source_updated_date: "2026-10-20"
source_updated_date_basis: "agent_sdk_separate_publication_date"
authors: ["Cursor"]
venue: "Cursor Blog"
url: "https://cursor.com/blog/projects"
created: 2026-11-09
updated: 2026-11-09
---

# Cursor Projects and Agent SDK

## Mechanisms

[Projects, September 10](https://cursor.com/blog/projects), introduces a persistent coordinator that delegates implementation, shares files across local/cloud workers, and responds to schedules and external events. Cursor describes multi-PR migrations and ongoing codebase maintenance. Its reported merge-volume gains are vendor observations without a disclosed causal design or quality-adjusted delivery measure. The launch labels Projects beta.

[Agent SDK, October 20](https://cursor.com/blog/agent-sdk), exposes the framework behind Cursor's managed bots: Markdown instructions, TypeScript tools, specialized agents, parallel subagents, evals, and event replay. Agents run on Cursor infrastructure or as a self-hosted Node process. The launch labels the SDK generally available.

The SDK article describes an internal reviewer that checks PRs against a lessons database and cites the relevant note. This is a concrete connection between organizational memory and verification, without an outcome evaluation.

## Boundaries

These articles establish product mechanisms and reported use, not independent evidence of end-to-end factory reliability. Shared context alone does not specify conflict resolution or memory authority.

## Connections

- [[concepts/code factories]]
- [[concepts/issue tracker control plane]]
- [[concepts/cross-session agent communication]]
- [[reports/Code Factories Update - 2026-11-09]]
