---
title: "How the Claude Code team does code review"
aliases: ["Claude Code review at agent volume"]
tags: [sources, code-factories]
source_type: "article"
status: "verified"
evidence_class: "vendor-production-report"
publication_date: "2026-10-15"
publication_date_basis: "visible_publication_date"
authors: ["Addy Osmani", "Morgan Westlee Lunt", "Qing Wang"]
venue: "claude.dev"
url: "https://claude.dev/blog/solving-code-review-at-anthropic/"
created: 2026-11-09
updated: 2026-11-09
---

# Claude Code Review at Agent Volume

## Mechanism and Evidence

The team reports more than doubling merged PRs from June to September while the reverted share fell over 40% relatively. No absolute rates or causal attribution are supplied.

Layered verification combines executable evidence, automated bug/security review, CI, risk-tiered human approval, merge queues, staged releases, and rollback. Incidents become reviewer evals; clean PRs measure harmful false positives. Review convergence is measured explicitly, with capped rounds and narrower subsequent reviews.

## Boundaries

Internal approval policy exceeds the public product's authority: the product posts findings; internal low-risk changes may clear without human approval. Required human slots cannot be filled by agents, and approvals attach to a commit. The team reports no automatic circuit breaker yet for worsening revert/incident trends.

## Connections

- [[concepts/evaluator reliability]]
- [[methods/self-improving code loops]]
- [[operations/release engineering]]
- [[maps/Code Factory Playbook]]

## Primary Link

[Operating workflow and limitations](https://claude.dev/blog/solving-code-review-at-anthropic/).
