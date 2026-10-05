---
title: "Claude Code Mods and You should know"
aliases:
  - "Claude Code Mods and Watching Agent"
  - "Claude Code You Should Know"
source_type: "docs"
kind: "programmable-harness-and-side-agent"
status: "verified"
year: 2026
publication_date: "2026-10-01"
publication_date_basis: "official_v2.1.287_release_and_dated_tutorial"
source_updated_date: "2026-10-05"
source_updated_date_basis: "living_documentation_access_date"
source_version: "v2.1.287 release; documentation inspected 2026-10-05"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Anthropic"
  - "Addy Osmani (tutorial)"
venue: "Claude Code release notes and official documentation"
url: "https://github.com/anthropics/claude-code/releases/tag/v2.1.287"
pdf_url: ""
evidence_class: "official-release-and-runtime-documentation"
metrics_status: "shipped-interface-no-effectiveness-evaluation"
artifacts: []
created: 2026-10-05
updated: 2026-10-05
---

# Claude Code Mods and You Should Know

## Contribution

The October 1 release exposes deeper harness behavior through Mods and adds **You should know**, an optional built-in side agent that flags things the user or Claude might miss. The release limits that feature to first-party sessions with telemetry enabled.

Mods are session-resident JavaScript/TypeScript modules. Event handlers can observe, alter, or answer tool and turn events, register interfaces and tools, and retain host-managed state across hot reloads. The October 1 tutorial demonstrates these mechanisms; it does not evaluate the side agent.

## Evidence Boundary

The watcher is a shipped observer role, distinct from executor-initiated [[concepts/advisor agents|advice]]. The release does not establish its observation coverage, detection quality, intervention authority, independent operating-system process, or crash recovery. Host state surviving hot reload is not proof of durable execution. A versioned feature announcement supplies implementation evidence, not measured correctness.

## Connections

- [[concepts/background agents]]
- [[concepts/event-driven agents]]
- [[concepts/advisor agents]]
- [[methods/hook-based control]]
- [[methods/runtime supervision]]
- [[sources/AI Control Despite Intentional Subversion]]
- [[sources/Monitoring Reasoning Models for Misbehavior]]

## Primary Links

- [Version 2.1.287 release, October 1](https://github.com/anthropics/claude-code/releases/tag/v2.1.287)
- [Getting started with Claude Code mods, October 1](https://claude.dev/blog/getting-started-with-claude-code-mods/)
- [Mods overview, inspected October 5](https://code.claude.com/docs/en/plugins/mods/overview)
