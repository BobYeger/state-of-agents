---
title: "OpenCode Harness"
aliases:
  - "anomalyco/opencode"
  - "OpenCode coding agent"
source_type: "repository"
kind: "coding-agent-harness-repository"
status: "verified"
year: 2025
publication_date: "2025-04-30"
publication_date_basis: "github_repository_created_at"
source_updated_date: "2026-08-19"
source_updated_date_basis: "pinned_dev_commit_author_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "OpenCode"
venue: "GitHub"
url: "https://github.com/anomalyco/opencode"
pdf_url: ""
license: "MIT"
license_url: "https://github.com/anomalyco/opencode/blob/31406ccc51b4bd2a4e1e086b2bcaa5f7f804f26d/LICENSE"
evidence_class: "open-source-implementation-maintainer-documentation-and-release-artifacts"
metrics_status: "tests-and-ui-performance-benchmarks-without-agent-quality-results"
artifacts: []
created: 2026-08-19
updated: 2026-08-19
---

# OpenCode Harness

## Summary

- OpenCode is an official open-source coding-agent harness with terminal, headless server, web, desktop, and protocol-facing clients. Its TUI is a client of a local HTTP server; the same server publishes an OpenAPI 3.1 interface and generated SDK surface, making client/server separation part of the shipped architecture rather than a wrapper added later.
- Stable release `v1.18.18` runs a persisted session loop: it creates user and assistant records, streams model events through a processor, resolves tools and permissions, continues after tool calls, applies an optional step cap, compacts when necessary, and exits on a completed or failed assistant turn.
- Session, message, part, usage, fork, revert, and parent-child data are SQLite-backed. Compaction creates explicit summary messages and marks sufficiently old tool results as compacted for model projection; this is durable operational state, but it is not documented as a full-fidelity append-only replay contract.
- Built-in tools cover shell, read/search, edits and patches, web retrieval/search, questions, skills, tasks, and extensibility through custom tools and MCP; the LSP tool is experimental. Tools are enabled without prompts by default; ordered `allow`/`ask`/`deny` rules, agent overrides, external-directory and repeat-call guards, and `--auto` provide policy control. This permission layer does not isolate arbitrary shell execution from the host OS.

## Harness Profile

| Dimension | Verified stable behavior in `v1.18.18` |
| --- | --- |
| Architecture | A Bun/TypeScript runtime exposes sessions, files, providers, tools, permissions, MCP, PTYs, and an event stream through a local server. The TUI, headless `serve`, web surface, SDK, and ACP command are clients or interfaces over that runtime. |
| Loop and state | A `while (true)` session loop streams provider events into persisted message/part state, handles tool-call continuation, status and aborts, step limits, overflow, summaries, forks, and reverts. SQLite tables back the session projection. |
| Tools and control | Most permissions default to `allow`; `.env` reads default to `deny`, while external-directory access and repeated identical calls default to `ask`. The last matching granular rule wins. `--auto` approves only `ask` decisions and preserves explicit denies. Plan restricts edits and shell by default; Build is full-access. |
| Multi-agent | Build and Plan are primary agents; General, Explore, and Scout are built-in subagents. Task calls create or resume child sessions with derived permissions and a configurable nesting limit. Foreground child sessions are shipped; background subagents are gated by `OPENCODE_EXPERIMENTAL_BACKGROUND_SUBAGENTS`, so they should not be presented as stable orchestration. |
| Observability | The server exposes server-sent events, session status, message parts, diffs, and tool lifecycle state. `opencode stats` aggregates sessions, tokens, cost, tool frequency, and per-model usage. These are operator signals, not benchmark results or billing-grade external verification. |

## Stable, Experimental, and Development Boundaries

The stable baseline is release tag `v1.18.18`, commit `31406ccc51b4bd2a4e1e086b2bcaa5f7f804f26d`, published August 13, 2026. The repository's default branch is `dev`; its captured head `da4730e4a41dcbb2cb2d907dd2b06ac481b8f962` (August 19) is untagged and diverged from that release. Dev-head fixes and generated changes are therefore not described here as shipped.

Even the stable tree contains V1 types alongside an `EventV2Bridge`, event-sourcing migrations, and explicit experimental flags for the event system, workspaces, code mode, LSP tooling, WebSockets, and background subagents. Those files are evidence of active internal migration and feature work, not a stable V2 API or roadmap promise. The audited official materials publish no separate completion schedule for that migration.

The repository's unit, HTTP API, and UI performance tests support implementation confidence but do not publish controlled agent-quality, reliability, cost, or comparative benchmark results. Desktop is labeled beta. Custom tools, MCP servers, plugins, and the shell can execute powerful local actions; permissions and localhost-by-default server binding reduce exposure but are not a sandbox. If the server is exposed beyond localhost, authentication must be configured by the operator.

## Connections

- [[operations/agent harnesses]]
- [[operations/durable sessions]]
- [[operations/permissions]]
- [[operations/sandboxes]]
- [[concepts/agent skills]]
- [[concepts/agent teams]]
- [[protocols/ACP]]
- [[maps/Harness Tracker]]

## Notes

- Canonical repository: https://github.com/anomalyco/opencode
- Stable release `v1.18.18`: https://github.com/anomalyco/opencode/releases/tag/v1.18.18
- Audited stable snapshot: https://github.com/anomalyco/opencode/tree/31406ccc51b4bd2a4e1e086b2bcaa5f7f804f26d
- Captured development snapshot: https://github.com/anomalyco/opencode/tree/da4730e4a41dcbb2cb2d907dd2b06ac481b8f962
- Server/client architecture: https://github.com/anomalyco/opencode/blob/31406ccc51b4bd2a4e1e086b2bcaa5f7f804f26d/packages/web/src/content/docs/server.mdx
- Agents and subagents: https://github.com/anomalyco/opencode/blob/31406ccc51b4bd2a4e1e086b2bcaa5f7f804f26d/packages/web/src/content/docs/agents.mdx
- Permission defaults and rule order: https://github.com/anomalyco/opencode/blob/31406ccc51b4bd2a4e1e086b2bcaa5f7f804f26d/packages/web/src/content/docs/permissions.mdx
- Tools and extension surface: https://github.com/anomalyco/opencode/blob/31406ccc51b4bd2a4e1e086b2bcaa5f7f804f26d/packages/web/src/content/docs/tools.mdx
- Session loop: https://github.com/anomalyco/opencode/blob/31406ccc51b4bd2a4e1e086b2bcaa5f7f804f26d/packages/opencode/src/session/prompt.ts
- Session persistence: https://github.com/anomalyco/opencode/blob/31406ccc51b4bd2a4e1e086b2bcaa5f7f804f26d/packages/opencode/src/session/session.ts
- Compaction: https://github.com/anomalyco/opencode/blob/31406ccc51b4bd2a4e1e086b2bcaa5f7f804f26d/packages/opencode/src/session/compaction.ts
- Task/subagent lifecycle: https://github.com/anomalyco/opencode/blob/31406ccc51b4bd2a4e1e086b2bcaa5f7f804f26d/packages/opencode/src/tool/task.ts
- Experimental flags: https://github.com/anomalyco/opencode/blob/31406ccc51b4bd2a4e1e086b2bcaa5f7f804f26d/packages/opencode/src/effect/runtime-flags.ts
- Local usage statistics: https://github.com/anomalyco/opencode/blob/31406ccc51b4bd2a4e1e086b2bcaa5f7f804f26d/packages/opencode/src/cli/cmd/stats.ts
- License: [MIT](https://github.com/anomalyco/opencode/blob/31406ccc51b4bd2a4e1e086b2bcaa5f7f804f26d/LICENSE), copyright 2025 opencode.
- No repository content was copied into the vault.
