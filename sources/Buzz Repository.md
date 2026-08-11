---
title: "Buzz Repository"
aliases:
  - "block/buzz"
  - "Buzz open-source repository"
  - "Harbor Buzz Orchestra"
source_type: "repository"
kind: "human-agent-workspace-and-harness"
status: "verified"
year: 2026
publication_date: "2026-03-06"
publication_date_basis: "github_repository_created_at"
source_updated_date: "2026-08-02"
source_updated_date_basis: "captured_main_head"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Block"
venue: "GitHub"
url: "https://github.com/block/buzz"
pdf_url: ""
evidence_class: "open-source-implementation-and-specifications"
metrics_status: "benchmark-harness-without-published-results"
artifacts:
  - "raw/repositories/block-buzz-repository.md"
created: 2026-08-02
updated: 2026-08-02
---

# Buzz Repository

## Summary

- The repository supports the narrower description of Buzz as an identity-aware collaboration substrate: a central Nostr relay, agent-first CLI, ACP harness, small ACP agent, MCP tool server, workflows, personas, memory, observability, and Git hosting.
- `buzz-acp --agents N` is a partitioned worker pool sharing one identity. It serializes work within a channel and runs different channels concurrently; it is not a deliberating team.
- Harbor Buzz Orchestra is the explicit team artifact: distinct orchestrator and worker identities share a task filesystem, while persona prompts tell the orchestrator not to perform task work, prohibit overlapping assignments, and call for verification by a different worker. Those rules are prompt contracts; the runtime enforces liveness and accepts completion only from an orchestrator-authored `DONE:` message.
- Its manifest records many important condition inputs and trials are isolated, but **no benchmark results are published**. The adapter explicitly declares ATIF unsupported, and token/cost result population and budget enforcement remain incomplete. This is well-specified methodology, not evidence of multi-agent lift.
- Draft Nostr extensions turn agent memory, live observability, and durable usage accounting into encrypted protocol objects. Buzz implements them, but they are not established ecosystem standards.
- The repo is unusually candid about maturity: approval-resume is incomplete, some workflow actions are stubs, and remote agents remain a draft.

## Harness Findings

`buzz-acp` bridges relay events to arbitrary ACP-compatible agent subprocesses. The first-party `buzz-agent` is one such ACP implementation and can use the separate `buzz-dev-mcp` tool server; Codex, Claude Code, goose, and other ACP agents need not use that MCP server. In the first-party path, sessions isolate context, history, and MCP subprocesses, while the runtime bounds output and process lifetimes. Per-channel batching, agent-subprocess respawn, stale-mention replay, relay reconnect, configurable inbound author gating (owner-only by default; Orchestra uses `anyone`), and `!cancel` / `!rotate` / `!shutdown` make coordination a runtime concern rather than prompt etiquette.

The Orchestra prompts are the strongest reusable artifact. They specify single ownership for shared-file mutations, one concrete assignment per message, evidence-bearing worker reports, and verification by a different worker. These are prompt-level contracts rather than tool restrictions. The runtime-enforced part is completion authority: the terminal message must begin `DONE:` and come from the orchestrator identity.

## Protocol Findings

- **NIP-AE:** encrypted owner-readable, agent-authored memory with blinded slugs and explicit migration/key-compromise limits.
- **NIP-AO:** encrypted ephemeral observer frames, including lifecycle and cancellation, with sequence numbers for detecting gaps.
- **NIP-AM:** durable encrypted per-turn accounting with careful null/delta/order semantics; self-reported and not billing-grade.
- **NIP-OA / NIP-AA:** separate owner attestation from agent authorship and derive relay admission from owner membership without inheriting owner roles.

There is a notable implementation/spec gap in the last pair. The current verification function checks condition syntax and signature but receives no event timestamp or kind; the relay membership path therefore does not enforce `created_at` clauses. NIP-AA also says `kind=` clauses do not restrict connection admission unless optional per-event enforcement exists. Treat the current mechanism as attributable, owner-backed relay admission—not a general least-privilege delegation system.

## Formal-Methods Findings

The Git-on-object-storage protocol has a checked-in TLA+ model, explicit storage axioms, invariant mutation tests, and backend conformance checks. It is a strong example of pairing a bounded safety model with empirical admission tests while stating what remains unproved. Multi-tenant, pairing, push, and unread-state artifacts extend the formal-methods culture, but some remain draft and exclude implementation, resource-isolation, liveness, or performance properties. The multi-tenant report also records an HA boundary: NIP-98 replay tracking is currently pod-local, so multi-replica conformance requires event-sticky routing or a shared atomic seen-set such as Redis.

## Connections

- [[systems/Buzz]]
- [[benchmarks/multi-agent benchmarks]]
- [[concepts/agent teams]]
- [[operations/durable sessions]]
- [[operations/agent identity]]
- [[protocols/ACP]]
- [[sources/Block Buzz]]

## Artifacts

- [[raw/repositories/block-buzz-repository]]

## Evidence Boundary

This card distinguishes checked-in implementation, draft protocol/specification, and product vision at repository commit `28ae6cd2174309529305724e455c7ca082f6fe4b`. It records no benchmark lift because the repository publishes none. Code-path findings are point-in-time and may change quickly in this actively developed project.

## Notes

- Canonical repository: https://github.com/block/buzz
- Audited snapshot: https://github.com/block/buzz/tree/28ae6cd2174309529305724e455c7ca082f6fe4b
- Benchmark: https://github.com/block/buzz/tree/28ae6cd2174309529305724e455c7ca082f6fe4b/benchmarks/harbor-buzz-orchestra
- ACP bridge behavior: https://github.com/block/buzz/blob/28ae6cd2174309529305724e455c7ca082f6fe4b/crates/buzz-acp/README.md
- Orchestra prompt contract: https://github.com/block/buzz/blob/28ae6cd2174309529305724e455c7ca082f6fe4b/benchmarks/harbor-buzz-orchestra/personas/orchestrator-tb.md
- Orchestra runtime: https://github.com/block/buzz/blob/28ae6cd2174309529305724e455c7ca082f6fe4b/benchmarks/harbor-buzz-orchestra/src/harbor_buzz_orchestra/container_runtime.py
- Orchestra manifest implementation: https://github.com/block/buzz/blob/28ae6cd2174309529305724e455c7ca082f6fe4b/benchmarks/harbor-buzz-orchestra/src/harbor_buzz_orchestra/manifest.py
- Agent Engrams: https://github.com/block/buzz/blob/28ae6cd2174309529305724e455c7ca082f6fe4b/docs/nips/NIP-AE.md
- Agent Observability: https://github.com/block/buzz/blob/28ae6cd2174309529305724e455c7ca082f6fe4b/docs/nips/NIP-AO.md
- Agent Turn Metrics: https://github.com/block/buzz/blob/28ae6cd2174309529305724e455c7ca082f6fe4b/docs/nips/NIP-AM.md
- NIP-OA implementation: https://github.com/block/buzz/blob/28ae6cd2174309529305724e455c7ca082f6fe4b/crates/buzz-sdk/src/nip_oa.rs
- Relay admission path: https://github.com/block/buzz/blob/28ae6cd2174309529305724e455c7ca082f6fe4b/crates/buzz-relay/src/api/mod.rs
- Workflow executor: https://github.com/block/buzz/blob/28ae6cd2174309529305724e455c7ca082f6fe4b/crates/buzz-workflow/src/executor.rs
- Git formal specification: https://github.com/block/buzz/blob/28ae6cd2174309529305724e455c7ca082f6fe4b/docs/git-on-object-storage.md
- Multi-tenant report: https://github.com/block/buzz/blob/28ae6cd2174309529305724e455c7ca082f6fe4b/docs/multi-tenant-relay.md
- Remote-agent draft: https://github.com/block/buzz/blob/28ae6cd2174309529305724e455c7ca082f6fe4b/docs/remote-agents.md
