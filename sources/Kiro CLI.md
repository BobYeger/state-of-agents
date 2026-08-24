---
title: "Kiro CLI"
aliases:
  - "Kiro CLI v3"
  - "Kiro unified agent harness"
source_type: "docs"
kind: "harness-docs"
status: "verified"
year: 2026
publication_date: "2026-08-03"
publication_date_basis: "kiro_official_unified_harness_architecture_post"
source_updated_date: "2026-08-07"
source_updated_date_basis: "latest_cited_official_feature_announcement"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Kiro"
  - "Amazon Web Services"
venue: "Kiro Docs and Blog"
url: "https://kiro.dev/docs/cli/"
pdf_url: ""
artifacts: []
evidence_class: "vendor-product-documentation-and-architecture-report"
metrics_status: "no-systematic-evaluation"
created: 2026-08-19
updated: 2026-08-19
---

# Kiro CLI

## Summary

- Kiro CLI is generally available, but the unified-harness CLI 3.0 described here is an opt-in **Early Access** engine (`kiro-cli --v3`) running alongside stable 2.x. V3 changes session, hook, permission, tool, and agent-configuration formats; its classic non-TUI mode is not supported.
- Kiro describes the unified harness as a proprietary standalone process beside the codebase. It owns the agent loop, model communication, context/compaction, session management, tool execution, subagent delegation, and configuration. Clients connect through Agent Client Protocol (ACP): local clients use stdio, cloud clients use a Kiro WebSocket transport, and clients may vend their own tools while suppressing built-ins. The same binary can run locally or in a cloud VM, but that executor portability is not yet cross-environment session mobility.
- Sessions are saved and resumable; v3 adds manual and automatic compaction plus session export/import, but its session format is not backward-compatible with v2. Steering files, custom-agent configuration, MCP servers, skills, hooks, and permissions externalize state and control. Queue/steer/cancel input and lifecycle/tool hooks provide mid-run intervention; capability rules replace v2 trust flags.
- Subagents run in parallel with isolated contexts, tools, and permissions, return results to the main agent, and can be arranged as dependency DAGs. Custom agents can serve as subagents in CLI and IDE, while Web and Mobile currently expose only Kiro's built-ins.
- V3's built-in Spec agent implements a durable requirements -> design -> tasks -> execution workflow under `.kiro/specs/<name>/`, with task verification and editable artifacts. This is a CLI v3 Early Access capability, not evidence that stable 2.x has the same workflow.
- Kiro's Powers extension layer supports skills and MCP and was rolling out Agent Plugins 1.0 support on August 7, 2026. V3 documents automatic pickup of powers installed through the IDE; this should not yet be treated as a mature, independently installable CLI plugin runtime.
- Operator visibility includes saved/exported sessions, context-window and hook notifications over Kiro-ACP, subagent progress/tool-duration summaries, and local logs up to trace verbosity. The official material does not document a first-class distributed trace store, eval system, or reliability benchmark.

## Design Consequences

- A process/protocol boundary keeps client UI code out of the loop and lets one harness serve terminal, IDE, web, and mobile surfaces without requiring a shared implementation language.
- Standard ACP supplies session, streaming, and tool-call primitives; Kiro-ACP adds live steering, specs, richer permissions, context-use reporting, and hook notifications. Those extensions improve first-party consistency but are Kiro-specific rather than portable ACP guarantees.
- File-backed specs make planning state inspectable and resumable outside the transcript. They also let the same permissions, hooks, and MCP configuration govern both planning and execution.

## Evidence Boundary

The stable/preview distinction is load-bearing. Kiro CLI itself reached general availability on November 17, 2025, while CLI v3 remains Early Access; Kiro Web and iOS are preview surfaces. Kiro's architecture post explicitly says cross-environment session packaging and control of both local and cloud sessions from any client still need to be built, so “one continuous conversation across every surface” is a direction, not a shipped portability guarantee.

The Kiro CLI is licensed as AWS Content, not released as an open-source harness; the public Kiro repository is a product-information and issue surface rather than the implementation. Loop behavior, Cedar-backed policy properties, cross-client consistency, and performance/reliability improvements are vendor-described and not source-audited. No task corpus, sample size, error rate, durability experiment, or comparative evaluation accompanies the architecture report.

## Connections

- [[operations/agent harnesses]]
- [[operations/durable sessions]]
- [[operations/permissions]]
- [[operations/harness fault tolerance]]
- [[methods/hook-based control]]
- [[concepts/subagent context isolation]]
- [[concepts/agent plugins]]
- [[maps/Harness Tracker]]

## Notes

- Canonical CLI docs: https://kiro.dev/docs/cli/
- Unified-harness architecture and explicit maturity boundaries: https://kiro.dev/blog/one-agent/
- CLI v3 Early Access announcement: https://kiro.dev/changelog/cli/2-8/
- V3 status, breaking changes, and gaps: https://kiro.dev/docs/cli/v3/
- Spec workflow: https://kiro.dev/docs/cli/v3/specs/
- Subagent model: https://kiro.dev/docs/chat/subagents/
- Hooks: https://kiro.dev/docs/cli/hooks/
- Sessions and logs: https://kiro.dev/docs/cli/reference/cli-commands/
- Agent Plugins rollout through Powers: https://kiro.dev/blog/powers-supports-plugins/
- Product license: https://kiro.dev/license/
- Public product-information and issue repository: https://github.com/kirodotdev/Kiro
- No source artifact was vendored.
