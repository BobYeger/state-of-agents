---
title: "DeepSeek Harness Repository"
aliases:
  - "deepseek-ai/deepseek-harness"
  - "DeepSeek Harness"
  - "dsh"
source_type: "repository"
kind: "agent-harness-repository"
status: "verified"
year: 2026
publication_date: "2026-08-13"
publication_date_basis: "github_repository_created_at"
source_updated_date: "2026-08-13"
source_updated_date_basis: "pinned_commit_author_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "DeepSeek AI"
venue: "GitHub"
url: "https://github.com/deepseek-ai/deepseek-harness"
pdf_url: ""
license: "MIT"
license_url: "https://github.com/deepseek-ai/deepseek-harness/blob/47f943859bef60e4160492346772ded9b24f765a/LICENSE"
evidence_class: "open-source-implementation-and-maintainer-documentation"
metrics_status: "benchmark-instructions-without-published-results"
created: 2026-08-17
updated: 2026-08-24
---

# DeepSeek Harness Repository

## Summary

- DeepSeek Harness is an official open-source agent harness in developer preview. Its organizing rule is “everything is a plugin”: model adapters, tools, the session log, the agent loop, persistence, policy, sandboxing, subagents, and interfaces are mounted through Cordis services and reversible registrations.
- Profiles compose ordered bundles and patch overlays into a plugin tree. This makes the running configuration inspectable and lets an operator replace a capability provider or one configuration row without patching a privileged agent core.
- The append-only session-event log is the canonical source for model history, replay, transcripts, and ledger telemetry; interchangeable persistence backends make it durable. A stated invariant requires every model-visible input to be reconstructable from logged events, while live `agent/*` events handle in-flight coordination and operational error/shutdown telemetry remains a separate channel.
- Tool execution is a centralized pipeline: pre-execution hooks and approval, monotonic guards, wrapped execution, post-processing, immutable final-outcome observation, and one durable model-facing result. Capability seams separate service definitions, providers, and consumers so filesystem, subprocess, sandbox, model, and subagent backends can be swapped together.
- Repository documentation records defensive rules for asynchronous ownership, quiescent teardown, callback isolation, credential-scrubbed subprocess environments, and private unpredictable spill paths.

## Design Consequences

- Treat the harness as a composition graph rather than a monolithic loop. Stable service keys and explicit event domains let policy, observability, persistence, and execution providers evolve independently.
- Separate durable facts from live control signals. If model-visible context is derived only from the durable log, replay and auditing share the same evidence surface as inference.
- Make policy an ordered execution boundary: approvals and non-bypassable guards belong before tool dispatch, while normalization and immutable outcome logging belong after it.
- Reversible registration improves reload and teardown, but security still depends on the selected sandbox, filesystem, subprocess, credential, and approval providers.

## Evidence Boundary

This card audits repository commit `47f943859bef60e4160492346772ded9b24f765a`, dated August 13, 2026. The project labels itself a developer preview and warns of compatibility-breaking changes. Its evidence is checked-in code, tests, generated architecture maps, and maintainer documentation; these establish an implementation surface, not production reliability or comparative performance.

`BENCHMARK.md` supplies only instructions for running independent tasks and publishes no scores, sample sizes, cost results, or baseline comparisons. Stated invariants and Cordis lifecycle guarantees are design contracts rather than external verification, and safe behavior across arbitrary third-party plugin combinations is not demonstrated.

At this snapshot the public repository had no tags or GitHub releases, while npm's `0.1.0-rc.6` default package was ahead of the CLI's `0.1.0-rc.5` version on visible `master`; the published artifact was therefore not traceable to a public release tag. Worker-thread workflows are documented as trusted-code, bash-equivalent execution rather than a security sandbox. The nonpersistent temporary-plugin tool is absent from the default `standard` preset but available through the shipped opt-in `cordis` preset; its VM boundary is likewise not a security boundary.

## Current Status Pointer — August 24, 2026

The historical audit above remains pinned to `47f943859bef60e4160492346772ded9b24f765a`. Since that snapshot, the repository has added release tags; current `master` is `dsh-v0.1.1-rc.2` at `b150a551b8d465e31e418e1b2eaf5e79bbb7d28e`, dated August 21. This supersedes only the old snapshot's present-tense “no tags” status, not the evidence captured at that commit.

The newer tree also contains an Agent Teams implementation with a durable peer mailbox and shared revisioned task DAG. Its two packages are explicitly private, live under `packages/experimental/`, and are mechanically excluded from release artifacts and stable-package dependencies. See [[sources/DeepSeek Harness Agent Teams]] for the separate current evidence boundary; do not read it back into the August 13 snapshot or describe it as a shipped stable harness feature.

## Connections

- [[sources/A Programming Paradigm for Spatiotemporal Composability]]
- [[operations/agent harnesses]]
- [[operations/harness fault tolerance]]
- [[operations/durable sessions]]
- [[concepts/agent plugins]]
- [[concepts/tool-use contracts]]
- [[maps/Harness Tracker]]

## Notes

- Canonical repository: https://github.com/deepseek-ai/deepseek-harness
- Audited snapshot: https://github.com/deepseek-ai/deepseek-harness/tree/47f943859bef60e4160492346772ded9b24f765a
- Snapshot commit: `47f943859bef60e4160492346772ded9b24f765a` (`Merge pull request #2519 from deepseek-harness/feat/npm-public`).
- Current-status pointer, not a repin: https://github.com/deepseek-ai/deepseek-harness/tree/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e (`dsh-v0.1.1-rc.2`, August 21, 2026).
- Default branch at capture time: `master`.
- License: [MIT](https://github.com/deepseek-ai/deepseek-harness/blob/47f943859bef60e4160492346772ded9b24f765a/LICENSE), copyright DeepSeek.
- Architecture: https://github.com/deepseek-ai/deepseek-harness/blob/47f943859bef60e4160492346772ded9b24f765a/docs/architecture.md
- Tool execution pipeline: https://github.com/deepseek-ai/deepseek-harness/blob/47f943859bef60e4160492346772ded9b24f765a/docs/tool-execution-pipeline.md
- Subagent lifecycle: https://github.com/deepseek-ai/deepseek-harness/blob/47f943859bef60e4160492346772ded9b24f765a/docs/subsystems/subagent.md
- Compaction lifecycle: https://github.com/deepseek-ai/deepseek-harness/blob/47f943859bef60e4160492346772ded9b24f765a/docs/subsystems/compaction.md
- Testing policy: https://github.com/deepseek-ai/deepseek-harness/blob/47f943859bef60e4160492346772ded9b24f765a/docs/testing.md
- Benchmark instructions without results: https://github.com/deepseek-ai/deepseek-harness/blob/47f943859bef60e4160492346772ded9b24f765a/BENCHMARK.md
- Published npm snapshot: https://www.npmjs.com/package/@deepseek-ai/dsh/v/0.1.0-rc.6
- No repository content was copied into the vault.
