# block/buzz repository — structured implementation snapshot

- Repository: https://github.com/block/buzz
- Snapshot commit: `28ae6cd2174309529305724e455c7ca082f6fe4b`
- Snapshot URL: https://github.com/block/buzz/tree/28ae6cd2174309529305724e455c7ca082f6fe4b
- Repository created: 2026-03-06
- Snapshot captured: 2026-08-02
- License: Apache-2.0
- Capture mode: targeted audit of architecture, harness, benchmark, protocol, security, and formal-method artifacts

## System Shape

- A Nostr relay is the authoritative event and access-control boundary for a community. The current architecture has no gossip, peer replication, or peer-to-peer community state.
- The agent surface includes an agent-first JSON CLI, an ACP relay harness, a small ACP agent, an MCP development-tool server, workflows, and persona definitions.
- `buzz-acp` speaks ACP to downstream agent subprocesses. The first-party `buzz-agent` can start `buzz-dev-mcp` and speaks MCP to that tool process; other ACP agents need not use it. First-party sessions have separate context, history, and MCP subprocesses, with bounded output/process lifetime and process-tree cleanup.

## Two Different Meanings of “Multiple Agents”

### ACP pool

- `buzz-acp --agents N` launches 1–32 subprocesses sharing one Nostr identity.
- Work is serialized within a channel and can run concurrently across channels.
- This is partitioned concurrency and crash capacity, not a deliberating team.

### Harbor Buzz Orchestra

- One orchestrator and multiple workers use distinct identities over the production relay/PostgreSQL stack while sharing the task filesystem.
- Persona prompts tell the orchestrator not to perform task work, assign one concrete step to one worker, avoid overlapping edits, and wait on dependencies. They tell workers to report commands, exit status, and real output, and call for a different worker to run the task's actual success check. These are prompt contracts, not runtime tool restrictions.
- The runtime checks process liveness and accepts completion only when the orchestrator identity publishes a message beginning `DONE:`.
- Condition manifests record roster, roles, endpoint/model labels, prompt SHA-256s, generation controls, price tables, and timeout. The runtime launches the manifest's `endpoint`; `model_revision` is recorded but not separately enforced. Trials receive fresh keys/private channels and preserve event timelines plus per-agent logs.
- The default checked-in condition is one Sonnet 4.6 orchestrator plus two Haiku 4.5 workers for Terminal-Bench 2.1.

## Benchmark Evidence Boundary

- No public score table, single-agent baseline, pass rate, cost result, paper, or controlled evidence of multi-agent lift was found as of the snapshot date. Block separately publishes anecdotal operator claims about coordination and productivity.
- The adapter declares no ATIF trajectory support.
- Token and cost fields exist in configuration/result schemas, but the audited container runtime does not populate the result fields or enforce those budgets; wall-clock/call-round limits are wired.
- Database tables anticipate LLM receipts/spans, but no ingestion path was found in the benchmark package.
- Treat this as a well-specified evaluation harness, not empirical evidence that Buzz Orchestra improves performance.

## Memory, Observability, and Accounting

- **NIP-AE / Agent Engrams:** implemented encrypted, owner-readable and agent-authored durable memory using addressable events, blinded slugs, core memory, hierarchical entries, and tombstones. Core memory is injected when a session starts, not live-refreshed. Relay migration is manual and NIP-44 has no forward secrecy. Agent-key compromise permits reading and rewriting that agent's memory; owner-key compromise permits reading it but not producing agent-authored rewrites.
- **NIP-AO / Agent Observability:** implemented encrypted ephemeral observer frames for raw ACP traffic, semantic activity, lifecycle, and cancellation. Sequence numbers permit drop detection, but the stream is intentionally not persisted or searched.
- **NIP-AM / Agent Turn Metrics:** implemented encrypted durable per-turn usage records with model/harness/session/channel identifiers. Unknown values remain null and decreasing counters do not become negative deltas. Records are agent-reported and not billing-grade.
- These documents are draft optional protocol proposals implemented by Buzz; they are not evidence of adoption as general Nostr standards.

## Identity and Authorization Findings

- NIP-OA separates authorization from authorship: the owner signs an attestation for an independent agent key, while the agent remains author of its events.
- NIP-AA can derive relay admission from an owner's membership without inheriting the owner's channel roles or administrative privileges.
- The current `verify_auth_tag` validates condition syntax and signature but is not passed an event kind or timestamp. The relay membership path verifies the credential and owner membership without evaluating its `created_at` conditions. NIP-AA itself warns that `kind=` clauses do not restrict connection-level access unless optional per-event enforcement exists.
- Owner removal blocks a new connection but need not terminate an active one; credentials are reusable and not relay- or purpose-bound; owner and agent become linkable to the relay.
- The benchmark provisioner stores trial handles containing agent and model secrets in its isolated PostgreSQL testbed. This is a disposable benchmark design, not a production secret-storage pattern.

## Formal-Methods Artifacts

- Git-on-object-storage uses immutable content-addressed objects and a CAS-updated pointer. Its TLA+ model checks durability/order/closure and concurrent-update safety in a bounded state space, with mutation tests for invariant non-vacuity and explicit object-store assumptions. It does not prove performance, garbage collection, or general liveness.
- Multi-tenant isolation has TLA+ and Tamarin artifacts plus conformance/mutation tests. The security model remains draft and excludes timing/resource isolation, database/cryptographic implementation correctness, and liveness/performance.
- The multi-tenant report identifies a deployment gap: NIP-98 replay tracking is currently pod-local. Multi-replica conformance therefore requires event-sticky routing or a shared atomic seen-set such as Redis.
- Pairing, push leases, and unread-state CRDTs have smaller formal or exhaustive-model artifacts.

## Product Maturity Boundaries

- Workflow approval schema, API, UI, and database pieces exist, but ordinary `request_approval` execution does not yet persist and resume a waiting run; it is marked failed. `send_dm` and `set_channel_topic` are schema-visible stubs.
- The launch scenario in which a release waits for an approval reaction and then ships is therefore a target workflow rather than fully working end to end.
- Remote-agent deployment is a draft specification. The Kubernetes provider described by the document is not present on the audited main tree.

## Primary Files Audited

- `README.md`, `ARCHITECTURE.md`, `VISION.md`, `VISION_AGENT.md`, `VISION_ACTIVITY.md`
- `crates/buzz-acp/README.md`, `crates/buzz-agent/README.md`
- `benchmarks/harbor-buzz-orchestra/README.md`, manifests, personas, runtime, tests, and SQL schema
- `docs/nips/NIP-AA.md`, `NIP-AE.md`, `NIP-AM.md`, `NIP-AO.md`, `NIP-OA.md`
- `docs/git-on-object-storage.md`, `docs/spec/GitOnObjectStore.tla`
- `docs/multi-tenant-relay.md`, `docs/spec/MultiTenantRelay.tla`, `docs/spec/MultiTenantAuth.spthy`
- workflow executor/engine and owner-attestation verification/admission paths
