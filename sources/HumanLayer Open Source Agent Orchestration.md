---
title: "HumanLayer open-source coding-agent orchestration"
aliases: ["HumanLayer Open Source Agent Orchestration", "HumanLayer core repository"]
source_type: "repository"
status: "verified"
authors: ["HumanLayer"]
venue: "GitHub / HumanLayer Docs"
publication_date: "2026-10-22"
publication_date_basis: "repository_replacement_commit_date_not_verified_first_public_availability"
announcement_date: "2026-11-02"
announcement_date_basis: "release_0.201.0_notes"
source_version: "f9bd73534a9fb7099a274f951b698b1297122fd9"
url: "https://github.com/humanlayer/humanlayer"
license: "Apache-2.0; vendored exceptions documented in NOTICE"
evidence_class: "primary-repository-and-release-documentation"
metrics_status: "implementation-inspection-not-performance-evaluation"
accessed: 2026-11-09
created: 2026-11-09
updated: 2026-11-09
tags: [harness, orchestration, code-factories, human-in-the-loop]
---

# HumanLayer Open Source Agent Orchestration

## Release and Scope

The October 22 [replacement commit](https://github.com/humanlayer/humanlayer/commit/d8197bab07017a2e2bef91bc25b2ebec6a4575b4) preserves earlier code on `legacy`/`legacy-final`. [November 2 release notes](https://docs.humanlayer.com/release-notes) announce the current core: desktop, daemon, CLI, web UI, API, and plugins. This is a new codebase publication within an older repository.

The [pinned README](https://github.com/humanlayer/humanlayer/blob/f9bd73534a9fb7099a274f951b698b1297122fd9/README.md) describes host execution through Claude Code, Codex, OpenCode, and Pi, shared task/session/artifact state, and Research–Plan–Implement skills. Apache-2.0 is the root license; some vendored code retains MIT. Self-hosting guides remain in progress.

## Inspected Mechanism

The [auto-advance implementation](https://github.com/humanlayer/humanlayer/blob/f9bd73534a9fb7099a274f951b698b1297122fd9/apps/riptide-api/src/orpc/daemon/sessions/check-auto-advance.ts) checks effective settings, session labels, artifact types or extracted next-step suggestions, and duplicate destination sessions before launching a phase. Owner/collaborator settings differ; workspace timing can alter the destination. These are workflow-completion signals, not independent judgments of artifact quality.

## Evidence Boundary

The [workflow explanation](https://github.com/humanlayer/humanlayer/blob/f9bd73534a9fb7099a274f951b698b1297122fd9/apps/docs/explanation/workflow-phases.md) specifies review checkpoints and configurable progression. Source availability enables inspection; it does not establish delivery gains, production self-hosting readiness, or autonomous self-improvement. No build, tests, or deployment were executed in this review.

## Connections

- [[systems/HumanLayer]]
- [[maps/Code Factory Playbook]]
- [[methods/deliberative control]]
- [[operations/durable sessions]]
