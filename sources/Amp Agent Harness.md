---
title: "Amp Agent Harness"
aliases:
  - "Amp harness"
  - "Amp Neo harness"
source_type: "docs"
kind: "harness-docs"
status: "verified"
year: 2026
publication_date: "2026-05-27"
publication_date_basis: "amp_neo_general_availability"
source_updated_date: "2026-08-19"
source_updated_date_basis: "living_manual_snapshot"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Amp Frontier Corporation"
venue: "Amp Owner's Manual and Chronicle"
url: "https://ampcode.com/manual"
pdf_url: ""
artifacts: []
evidence_class: "vendor-product-documentation"
metrics_status: "no-systematic-evaluation"
created: 2026-08-19
updated: 2026-08-19
---

# Amp Agent Harness

## Summary

- Amp is a concrete coding-agent harness delivered as a proprietary client plus cloud service. A thread holds messages, context, and tool calls; the rebuilt loop automatically compacts at 90% context use, supports queued or steered input and interruption, and can be driven interactively, through execute mode, streaming JSON, or the TypeScript/Python SDK.
- Its tool surface combines shell and built-in tools, MCP servers, skills, and plugin tools. The plugin lifecycle exposes `session.start`, `agent.start`, `tool.call`, `tool.result`, and `agent.end`; pre- and post-tool handlers can allow, reject, modify, synthesize, or replace results. Amp otherwise runs tools without approval by default, so policy is an explicit plugin/configuration choice rather than a safe default.
- State extends beyond one foreground turn: threads can resume, scheduled agents wake with their saved prompt and history, and orb webhooks persist an event before waking a paused environment. The current design supersedes the older [[sources/Amp Handoff|Handoff]] workflow with automatic compaction; the Handoff card remains useful as a historical alternative, not current Amp behavior.
- Multi-agent support has two levels. Built-in subagents use separate context, while plugin-defined agents can run one-shot or in persistent child threads. Agents can spawn threads, exchange messages and files, and execute locally, in a per-thread Amp-managed orb, or on a user-operated runner.
- Distributed execution is shipped: orbs clone a project into a fresh remote machine, while headless runners accept remotely created threads on machines the user controls. Web/mobile remote control, diffs, terminals, thread histories, plugin events, and streaming JSON provide operational visibility. The surveyed documentation does not expose a general trace/eval backend or a first-class requirements-design-tasks spec workflow.

## Design Consequences

- Thread identity is the durable coordination unit; executor placement is separable from the conversation, so the same control surface can target local, managed-orb, or runner execution.
- Plugins are both the extension plane and the policy boundary. This is flexible, but untrusted plugins execute code and the default tool posture is permissive; isolation and review cannot be inferred from the existence of hooks.
- Amp's multi-agent model is broader than parent-to-subagent summaries: persistent threads and cross-thread file/message transfer support asynchronous peer workflows and fan-out across machines.

## Evidence Boundary

The rebuilt Amp became generally available on May 27, 2026; orbs, runners, cross-thread agent spawning, schedules, multiplayer, and event-driven orbs are documented as shipped rather than previews. Amp nevertheless distributes a compiled client and cloud service under proprietary license terms and offers no self-hosted server. Architecture, durability, isolation, secret-redaction, and performance statements are therefore vendor claims, not conclusions from auditable source code or independent evaluation. The cited pages publish no representative task sample, success rate, recovery test, or comparative benchmark.

## Connections

- [[sources/Amp Handoff]]
- [[operations/agent harnesses]]
- [[operations/durable sessions]]
- [[operations/permissions]]
- [[operations/harness fault tolerance]]
- [[concepts/subagent context isolation]]
- [[concepts/agent plugins]]
- [[maps/Harness Tracker]]

## Notes

- Canonical manual: https://ampcode.com/manual
- Rebuilt loop and auto-compaction: https://ampcode.com/news/neo
- General-availability boundary: https://ampcode.com/news/drop-the-neo
- Orbs and durable webhook semantics: https://ampcode.com/manual/orbs
- Custom agents and thread API: https://ampcode.com/news/custom-agents
- Cross-thread/machine agent coordination: https://ampcode.com/news/from-agent-to-agent
- Security and system boundary: https://ampcode.com/security
- License terms: https://ampcode.com/terms
- No source artifact was vendored.
