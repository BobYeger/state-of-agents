---
title: "Bots for the last mile: Rollouts, Security Review"
aliases: ["Cursor Rollouts", "Cursor Security Reviewer"]
tags: [sources, code-factories]
source_type: "article"
status: "verified"
evidence_class: "vendor-product-report"
publication_date: "2026-09-23"
publication_date_basis: "visible_publication_date"
authors: ["Rustam Lalkaka"]
venue: "Cursor Blog"
url: "https://cursor.com/blog/rollouts-and-security-reviewer"
created: 2026-11-09
updated: 2026-11-09
---

# Cursor Rollouts and Security Reviewer

## Mechanism

Rollouts connects source control, deployment, and telemetry. Before merge it proposes a monitoring plan covering expected effects, risks, and instrumentation gaps; after deployment it compares signals with a baseline. Configured responses include notification, pausing a progressive rollout, or proposing a revert for approval.

Security Reviewer inspects PRs in repository context and proposes vulnerability fixes. The announcement reports availability on Teams and Enterprise plans.

## Boundaries

The article provides no detection precision, false-revert rate, incident reduction, or controlled comparison. Direct feature-flag traffic adjustment and release-train awareness are described as forthcoming, not shipped in this snapshot.

## What It Adds

Agent-mediated verification extends beyond PR tests into an explicit hypothesis about production behavior.

## Connections

- [[operations/release engineering]]
- [[operations/incident response]]
- [[maps/Code Factory Playbook]]

## Primary Link

[September 23 announcement](https://cursor.com/blog/rollouts-and-security-reviewer).
