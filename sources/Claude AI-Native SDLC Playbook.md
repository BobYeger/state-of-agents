---
title: "The AI-Native SDLC playbook"
aliases:
  - "Claude AI-Native SDLC Playbook"
  - "Anthropic AI-Native SDLC Playbook"
source_type: "article"
kind: "vendor-methodology-playbook"
status: "verified"
year: 2026
publication_date: "2026-08-21"
publication_date_basis: "json_ld_date_published"
source_updated_date: "2026-08-24"
source_updated_date_basis: "json_ld_date_modified"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Louis Claxton"
venue: "Claude"
url: "https://claude.com/blog/the-ai-native-sdlc-playbook"
pdf_url: ""
evidence_class: "vendor-methodology-playbook"
metrics_status: "proposed-indicators-without-reported-outcomes"
artifacts: []
created: 2026-08-25
updated: 2026-08-25
---

# The AI-Native SDLC Playbook

## Summary

- The playbook treats faster code generation as a bottleneck shift: planning, review, governance, deployment, and maintenance must become agent-compatible rather than remaining human-speed stage gates.
- Its organizing mechanism is a version-controlled artifact chain: `intent.md` → `spec.md` → `plan.md` → diff and tests → PR and review findings → incident record or lessons → new `intent.md`. An accepted artifact can trigger the next stage, while Git and PR history provide the audit trail.
- Planning and building combine plan mode with a concise `CLAUDE.md`, reusable skills, deterministic hooks, parallel worktrees, and scoped subagents. For every artifact, the organization should name one source of truth or at least preserve bidirectional linkage between repository files and legacy systems.
- Testing and deployment move verification into the agent's working loop, regression-test changes to `CLAUDE.md`, skills, and hooks through continuous evals, and layer agentic review beneath human approval for consequential changes.
- The control hierarchy distinguishes advisory skills from deterministic hooks, managed settings, sandboxing, scoped credentials, branch protection, and environment-specific authority. The agent may prepare and act up to a production gate without being able to approve its own release.
- Maintenance closes the operational loop: deterministic monitoring bands can invoke a sandboxed agent with tiered read-only, proposal, or pre-approved runbook authority; the result re-enters the lifecycle as `intent.md`, and incidents become permanent eval cases.

## Taxonomy Reading

This is primarily a [[concepts/code factories|code-factory]] or AI-native SDLC playbook. Its unit of design is the organization-level path from signals and intent through delivery and production feedback. It is secondarily [[concepts/loop engineering]] because artifacts, commits, and monitoring events wake subsequent stages, and it depends on [[operations/agent harnesses|harness engineering]] for tools, context, permissions, execution, evaluation, and observability.

It is not evidence of a self-evolving codebase under [[methods/self-improving code loops]]. The article does not describe autonomous candidate mutation, benchmark-driven selection, an archive of variants, or a keep/revert policy for improved harnesses. Updating instructions after repeated mistakes, adding incidents to evals, and restarting delivery from production signals are improvement-adjacent practices, but they remain human-governed configuration maintenance and operational recurrence.

## Evidence Boundary

This is first-party vendor methodology. The article says its practices come from Anthropic's Applied AI work and customer experience, but gives no deployment cohort, measured customer outcome, baseline, controlled comparison, benchmark, effect size, latency, or cost. Each play proposes leading and lagging indicators; none is reported as an observed result. Statements about cycle times, review speed, or single-pass implementation should therefore be read as expectations rather than findings.

The examples are concrete but Claude-specific. The managed-settings block is explicitly a starting point to tailor, not an audited reference architecture, and the security claims depend on the surrounding identity, CI, sandbox, credential, and approval implementation.

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[concepts/code factories]]
- [[concepts/loop engineering]]
- [[concepts/versioned context]]
- [[concepts/human-in-the-loop agents]]
- [[operations/agent harnesses]]
- [[operations/agent evals]]
- [[operations/permissions]]
- [[operations/worktree isolation]]
- [[operations/release engineering]]
- [[operations/incident response]]
- [[methods/hook-based control]]
- [[maps/Code Factory Playbook]]

## Notes

- Canonical URL: https://claude.com/blog/the-ai-native-sdlc-playbook
- Published August 21, 2026; page metadata updated August 24, 2026.
- No source content was copied into the vault.
