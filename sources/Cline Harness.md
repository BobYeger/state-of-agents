---
title: "Cline Harness"
aliases:
  - "cline/cline"
  - "Cline SDK"
  - "Cline CLI"
source_type: "repository"
kind: "coding-agent-harness-repository"
status: "verified"
year: 2024
publication_date: "2024-07-06"
publication_date_basis: "github_repository_created_at"
source_updated_date: "2026-08-19"
source_updated_date_basis: "pinned_main_commit_author_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Cline Bot Inc."
venue: "GitHub"
url: "https://github.com/cline/cline"
pdf_url: ""
license: "Apache-2.0"
license_url: "https://github.com/cline/cline/blob/dfa34ecea85b6b2689be37b3480b17678eeed915/LICENSE"
evidence_class: "open-source-implementation-maintainer-documentation-and-release-artifacts"
metrics_status: "eval-framework-partly-disabled-without-published-current-results"
artifacts: []
created: 2026-08-19
updated: 2026-08-19
---

# Cline Harness

## Summary

- Cline is an official coding-agent monorepo whose shared engine serves the CLI, VS Code extension, SDK, and parts of the separately hosted Kanban and closed-source JetBrains products. The auditable center is the SDK split: `@cline/agents` owns a stateless iteration loop and tool orchestration, while `@cline/core` owns session lifecycle, persistence, compaction, plugins, telemetry, hub services, and automation.
- Local and hub-backed runs use the same runtime boundary. The hub is an authority process to which clients can attach and detach; it brokers approvals, schedules, events, and client-provided capabilities while the run continues independently of any one UI.
- Full canonical session history and compacted working context are stored separately. Resume accepts a compaction projection only after hashing the covered canonical prefix; sessions destructively compacted under the older scheme remain best-effort because omitted history cannot be reconstructed.
- The plugin system is phase-ordered (`resolve` → `validate` → `setup` → frozen activation), capability-declared, and exposes typed lifecycle hooks. `beforeTool` may stop a call and `afterTool` may replace its result. In-process hooks and sandboxed plugin subprocesses are extension boundaries, not proof that the agent's shell or arbitrary third-party plugins are security-isolated.

## Harness Profile

| Dimension | Verified implementation |
| --- | --- |
| Architecture | Hosts call stateful `@cline/core`; core configures the stateless `@cline/agents` loop and `@cline/llms`. Local, shared-hub, and remote-hub runtime hosts implement a common session interface. |
| Loop and state | Each turn streams canonical text, reasoning, media, and tool events. Core persists messages, artifacts, origin (`user`, `automation`, `subagent`, or `team`), child lineage, usage, and the separately validated compaction projection. |
| Tools and control | The released CLI documents shell, file, web, MCP, checkpoints, Plan/Act, hooks, and headless NDJSON. Review behavior is surface- and mode-dependent: CLI tool calls are auto-approved by default; `--auto-approve false` prompts, while `--yolo` and `--zen` fully auto-approve and disable spawn/team tools by default. `--data-dir` says it enables sandbox mode, but the audited docs do not establish an OS-level isolation guarantee. |
| Multi-agent | Stable CLI `3.0.55` documents subagent spawning and persistent named teams. Child origin and aggregate root-plus-teammate usage are represented in core; yolo/zen remove those tools by default. Kanban adds worktree-per-card coordination in a separate repository and is not audited here. |
| Observability | The hub forwards structured text/reasoning/tool/agent lifecycle events; clients can correlate runs and render root-only or aggregate usage. The CLI can stream NDJSON, and completion telemetry is emitted once on explicit successful completion with a shutdown fallback. |

## Release and Evidence Boundary

This card audits main commit `dfa34ecea85b6b2689be37b3480b17678eeed915` (August 19, 2026), plus the latest visible stable CLI release `cli-v3.0.55` and VS Code release `v4.1.10` (both August 14). The Desktop `desktop-v0.0.14` release is newer, but the repository README still labels Desktop beta. There is no single monorepo version that proves every main-branch behavior shipped simultaneously in every host; the JetBrains implementation is explicitly not open source.

The repository contains extensive unit and end-to-end test commands and an evaluation framework. However, its own eval README says smoke-test CI is temporarily disabled while moving to the SDK CLI and nightly Cline Bench runs are still a TODO. No current comparative result table is published in the audited snapshot, so the repository establishes implementation and testability, not measured agent-quality superiority or production reliability.

The strongest control caveat is mode-specific: IDE copy emphasizes per-edit and per-command review, but stable CLI documentation states that tools are auto-approved by default. Tracker claims should therefore say “configurable approval policy” rather than “human approval required.” Plugin subprocess isolation must likewise not be generalized to shell execution, the whole agent, or untrusted plugins.

## Connections

- [[operations/agent harnesses]]
- [[operations/durable sessions]]
- [[operations/permissions]]
- [[operations/sandboxes]]
- [[concepts/agent plugins]]
- [[concepts/agent teams]]
- [[maps/Harness Tracker]]

## Notes

- Canonical repository: https://github.com/cline/cline
- Audited main snapshot: https://github.com/cline/cline/tree/dfa34ecea85b6b2689be37b3480b17678eeed915
- Architecture: https://github.com/cline/cline/blob/dfa34ecea85b6b2689be37b3480b17678eeed915/sdk/ARCHITECTURE.md
- Plugin contract: https://github.com/cline/cline/blob/dfa34ecea85b6b2689be37b3480b17678eeed915/sdk/.cline/skills/plugin.md
- CLI release `3.0.55`: https://github.com/cline/cline/releases/tag/cli-v3.0.55
- Released CLI documentation: https://github.com/cline/cline/blob/ad442cbb6a81d21773ceabc1398ea5eb58170718/apps/cli/README.md
- VS Code release `4.1.10`: https://github.com/cline/cline/releases/tag/v4.1.10
- Desktop release `0.0.14`: https://github.com/cline/cline/releases/tag/desktop-v0.0.14
- Tests: https://github.com/cline/cline/blob/dfa34ecea85b6b2689be37b3480b17678eeed915/package.json
- Evaluation framework and its disabled/TODO boundaries: https://github.com/cline/cline/blob/dfa34ecea85b6b2689be37b3480b17678eeed915/evals/README.md
- Separate Kanban repository: https://github.com/cline/kanban
- License: [Apache-2.0](https://github.com/cline/cline/blob/dfa34ecea85b6b2689be37b3480b17678eeed915/LICENSE).
- No repository content was copied into the vault.
