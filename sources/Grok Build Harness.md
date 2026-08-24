---
title: "Grok Build Harness"
aliases:
  - "xai-org/grok-build"
  - "Grok Build"
  - "grok CLI"
source_type: "repository"
kind: "coding-agent-harness-repository"
status: "verified"
year: 2026
publication_date: "2026-07-14"
publication_date_basis: "github_repository_created_at"
source_updated_date: "2026-08-23"
source_updated_date_basis: "pinned_main_commit_author_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "SpaceXAI"
venue: "GitHub"
url: "https://github.com/xai-org/grok-build"
pdf_url: ""
license: "Apache-2.0"
license_url: "https://github.com/xai-org/grok-build/blob/07b2f7144fd5c5c9d3dd1966937a87852d2dbdb8/LICENSE"
evidence_class: "open-source-implementation-and-maintainer-documentation"
metrics_status: "implementation-evidence-without-published-comparative-results"
artifacts: []
created: 2026-08-24
updated: 2026-08-24
---

# Grok Build Harness

## Summary

- Grok Build is SpaceXAI's open Rust coding-agent harness and terminal UI. The same runtime supports interactive TUI use, headless execution, scripting and CI, and editor clients through ACP; the public repository is periodically synchronized from an internal monorepo.
- Sessions persist prompts, responses, tool calls, task state, rewind points, usage, compaction checkpoints, and child-session metadata on disk. The harness also exposes project rules, skills, plugins, MCP, lifecycle hooks, cross-session memory, background tasks, goals, worktrees, permission modes, and OS sandbox profiles.
- Subagents are independent child sessions with separate context windows. They return a result to the parent, can run in the background, can resume a completed child's context, and can optionally receive an isolated Git worktree whose changes are later applied by an explicit worktree operation.
- Rhai workflows provide bounded scripted fan-out and gather through `agent()` and `parallel()` calls. Agent-count budgets and concurrency caps bound child launches, while a workflow dashboard exposes progress, rosters, and results.

## Multi-Agent Boundary

Grok Build's documented multi-agent mechanisms are parent-child subagents and workflow-script orchestration. The Agent Dashboard is a human control plane over top-level local sessions and forks: a person can dispatch sessions, inspect them, answer requests, and send or queue follow-up input. It does not establish an agent-callable peer-addressing or peer-mailbox protocol.

That distinction matters when comparing Grok Build with [[sources/Grok Bot]], Claude Code cross-session messaging, or DeepSeek Agent Teams. A dashboard containing several agents is not itself agent-to-agent communication, and a workflow's `parallel()` panel is declared fan-out rather than an autonomous peer team.

## Evidence Boundary

This card audits main commit `07b2f7144fd5c5c9d3dd1966937a87852d2dbdb8`, dated August 23, 2026. Its `SOURCE_REV` points to internal monorepo revision `956313d459bee15ae8f17bf73e0633605e18dddd`; the public history is a sequence of periodic syncs rather than the complete development history. The repository had no Git tags at capture time, so the audited commit should not be treated as a formal release boundary.

Code, tests, and maintainer documentation establish a substantial implemented harness but do not establish comparative coding quality, production reliability, or sandbox safety under every configuration. Subagent context isolation is not filesystem isolation unless worktree mode is selected. Hooks and permission modes are policy mechanisms; their presence alone does not prove containment of arbitrary tools or plugins.

## Connections

- [[concepts/cross-session agent communication]]
- [[concepts/subagent context isolation]]
- [[operations/agent harnesses]]
- [[operations/durable sessions]]
- [[operations/worktree isolation]]
- [[operations/agent memory]]
- [[concepts/agent skills]]
- [[concepts/agent plugins]]
- [[protocols/ACP]]
- [[maps/Harness Tracker]]

## Notes

- Canonical repository: https://github.com/xai-org/grok-build
- Audited snapshot: https://github.com/xai-org/grok-build/tree/07b2f7144fd5c5c9d3dd1966937a87852d2dbdb8
- Repository overview and architecture: https://github.com/xai-org/grok-build/blob/07b2f7144fd5c5c9d3dd1966937a87852d2dbdb8/README.md
- Subagents and worktree isolation: https://github.com/xai-org/grok-build/blob/07b2f7144fd5c5c9d3dd1966937a87852d2dbdb8/crates/codegen/xai-grok-pager/docs/user-guide/16-subagents.md
- Durable session layout: https://github.com/xai-org/grok-build/blob/07b2f7144fd5c5c9d3dd1966937a87852d2dbdb8/crates/codegen/xai-grok-pager/docs/user-guide/17-sessions.md
- Agent Dashboard: https://github.com/xai-org/grok-build/blob/07b2f7144fd5c5c9d3dd1966937a87852d2dbdb8/crates/codegen/xai-grok-pager/docs/user-guide/23-dashboard.md
- Workflow controls: https://github.com/xai-org/grok-build/blob/07b2f7144fd5c5c9d3dd1966937a87852d2dbdb8/crates/codegen/xai-grok-pager/docs/user-guide/04-slash-commands.md#workflow
- Apache-2.0 applies to first-party code; vendored and ported third-party code retains its original licenses and notices.
- No repository content was copied into the vault.
