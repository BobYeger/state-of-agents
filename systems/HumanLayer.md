---
title: "HumanLayer"
aliases: ["HumanLayer coding-agent orchestration"]
tags: [systems, orchestration, coding-agents]
implementation_class: "orchestrator-control-plane"
created: 2026-11-09
updated: 2026-11-09
---

# HumanLayer

HumanLayer coordinates coding-agent work through tasks, sessions, artifacts, reviews, and host daemons. The current open repository includes its applications and supporting services as well as Research–Plan–Implement workflows. See [[sources/HumanLayer Open Source Agent Orchestration]] for the pinned implementation, release history, license, and inspection limits.

## Why It Belongs in This Project

Its research value is an inspectable implementation of the layer between an issue and a coding agent: workflow selection, staged artifacts, workspaces, session continuation, review, and conditional progression. It complements the product descriptions in [[maps/Code Factory Playbook]] with code that can be compared against the documented contracts.

It is especially useful for studying [[methods/deliberative control]] and [[concepts/human-in-the-loop agents]]. The relevant distinction is between a documented review checkpoint, a user-configured transition, and an externally validated result. The inspected auto-advance code identifies phase completion from artifacts or extracted suggestions; that alone does not certify correctness.

## Research Questions

- Does staged review reduce rework and reviewer effort compared with direct implementation on matched tasks?
- Do task artifacts preserve intent and evidence across sessions and different coding agents?
- How do interruption, retries, concurrent collaborators, and worktree changes affect phase transitions?
- Which workflow controls are enforced in software, and which depend on skill instructions or human practice?

These are proposed evaluations. The repository review supplies architecture evidence, not answers to those questions. Self-hosting documentation is still in progress; the stack was not run locally.

## Related

- [[maps/Builder Ecosystem Map]]
- [[reports/Code Factories Update - 2026-11-09]]
- [[operations/worktree isolation]]
- [[operations/durable sessions]]
