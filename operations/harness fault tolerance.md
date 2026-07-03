# Harness Fault Tolerance

Harness fault tolerance is the engineering that keeps an agent loop correct when the provider, the network, a tool, or the harness process itself fails mid-run.

The framing that makes this tractable is that an agent loop is a distributed system: it makes remote calls with unreliable delivery, holds state that must survive crashes, and produces side effects that retries can duplicate. [[sources/Restate Durable AI Loops]] states the thesis directly — agents behave like distributed systems, so fault tolerance belongs in the runtime, not scattered through application code. [[sources/You Cannot Have Exactly-Once Delivery]] supplies the ground rule the whole area inherits: exactly-once delivery is impossible over unreliable channels, so every layer must choose at-most-once or at-least-once and design for the consequence (loss or duplicates).

## Failure Classes

| Failure | What breaks | Primary handling | Evidence |
|---|---|---|---|
| Provider error | The LLM call itself | Typed retry/backoff branching on error class | [[sources/Claude API Errors]] |
| Mid-stream error | A streaming response that already returned 200 | Stream-level error events, not HTTP status handling | [[sources/Claude API Errors]] |
| Context overflow | The next request no longer fits | Compaction with cache-aware placement; restorable truncation | [[sources/Claude API Compaction]], [[sources/Manus Context Engineering]] |
| Malformed tool call | The model emits an unparseable or invalid action | Feed the validation error back as an observation and let the model repair | [[sources/Manus Context Engineering]] |
| Duplicate side effects | A retried step re-executes a tool that already ran | Idempotent tools, deduplication, or transactional wrappers | [[sources/You Cannot Have Exactly-Once Delivery]], [[sources/Atomix]] |
| Process crash | The harness dies mid-turn | Durable execution with journal or event-history replay | [[sources/Temporal OpenAI Agents SDK Integration]], [[sources/Restate Durable AI Loops]] |
| Silent stall | The loop stops making progress without raising | Watchdogs, stream close signals, generator error surfacing | [[sources/Claude Agent SDK Streaming vs Single Message]] |

## Provider Errors Need Typed Retry Policies

A single exponential-backoff wrapper is not enough because provider error classes carry different meanings. [[sources/Claude API Errors]] documents the taxonomy a retry policy must branch on: 429 rate limits and 529 overload require distinct policies — 529 signals global overload across all users, while sharp per-organization spikes surface as 429 acceleration limits where the correct response is ramping traffic gradually, not backing off identically. 4xx errors other than 429 (invalid request, authentication, permission, request-too-large) are not retryable at all; retrying them wastes budget and hides bugs.

Two further constraints shape unattended operation. First, in SSE streaming an error can arrive after a 200 response has already been returned, so HTTP-status handling misses mid-stream failures — a harness that streams must handle error events inside the stream. Second, every response carries a request ID; a fault-tolerant harness logs it per step so failures can be correlated with provider-side records.

## Context Overflow Is a Recoverable Fault

Running out of context window is a predictable fault with a designed recovery path, not an exceptional crash. [[sources/Claude API Compaction]] moves this recovery into the API itself: server-side compaction summarizes older content when input tokens hit a configurable trigger, and `pause_after_compaction` returns a distinct stop reason so the harness can adjust messages before continuing — overflow recovery becomes an observable loop event rather than an opaque failure.

The complementary harness-side technique is restorable truncation. [[sources/Manus Context Engineering]] drops bulky observations (page content) while keeping the handle needed to re-fetch them (the URL), so trimming never causes irreversible information loss. The general rule: prefer reductions you can undo, because the information a future step needs is not knowable at truncation time. [[concepts/handoff over compaction]] covers the stronger alternative of starting a fresh context from durable artifacts.

## Malformed Actions Are Repaired In-Loop

When the model emits an invalid tool call — wrong schema, hallucinated tool, unparseable arguments — the productive response is to return the validation error as the tool result and let the model correct itself. [[sources/Manus Context Engineering]] makes the stronger claim that failure evidence should stay in context: erasing wrong turns removes the model's ability to update its beliefs, and error recovery is a core indicator of genuinely agentic behavior. Silently retrying or scrubbing the failed action trades short-term tidiness for repeated mistakes.

A design alternative is to shrink the surface where malformed actions can occur. [[sources/Mini-SWE-agent]] avoids the tool-calling interface entirely — bash as the only action, plain text as the protocol — and still scores over 74% on SWE-bench Verified, which bounds how much action-schema machinery current models actually require. [[concepts/tool-use contracts]] covers validation of the actions that remain.

## Side Effects: Idempotency Before Retry

Retry is only safe when re-execution is harmless. [[sources/You Cannot Have Exactly-Once Delivery]] gives the two admissible strategies: make the operations themselves idempotent, or deduplicate — and prefer distributing immutable facts over mutable operations so at-least-once delivery simulates exactly-once at the application level. For agent fleets this applies wherever tasks flow through queues between workers: task pickup must be at-least-once plus idempotent.

Agent loops add failure modes that plain idempotency does not cover. [[sources/Atomix]] names them: partial effects (some of a step's writes landed, others did not), losing-branch residue (a speculative branch's effects survive after the branch is abandoned), stale writes, and irreversible sends. Its mechanism — record reads and effects, seal a transaction when its footprint completes, commit only after per-resource frontiers confirm no earlier conflicting work remains — stratifies effects into bufferable, reversible, and irreversible, gating only the irreversible ones. It is a research prototype, but it supplies the vocabulary for reviewing any orchestrator's retry semantics: ask what happens to each effect class on abort.

The same discipline appears at the framework level. [[sources/LangGraph Interrupts]] documents that resuming from an interrupt restarts the entire node from the beginning, not from the interrupt line, so pre-interrupt code re-executes and must be idempotent — side effects belong after the interrupt point. This is the general shape of checkpoint-based recovery: everything between the last checkpoint and the failure runs twice.

## Crash Recovery vs Session Resume

These are different problems that share the word "resume":

| | Session resume | Crash recovery |
|---|---|---|
| Unit restored | Conversation state between turns | Execution state within a turn |
| Mechanism | Reload transcript/state, continue with a new request | Replay a journal or event history past completed steps |
| Cost of naive approach | Stale context, lost in-flight work | Re-run completed LLM calls and tool side effects |
| Examples | `thread/resume` in [[sources/OpenAI Codex App Server Docs]]; `continue_conversation` in [[sources/Claude Agent SDK Streaming vs Single Message]] | [[sources/Temporal OpenAI Agents SDK Integration]], [[sources/Restate Durable AI Loops]] |

Session resume is a harness feature: the loop ended cleanly and picks up later. Crash recovery is a runtime property: the loop died between a tool call and its result, and something must reconstruct exactly where it was without re-spending tokens or re-firing side effects.

## Durable Execution and Deterministic Replay

Durable-execution engines make crash recovery a configuration decision instead of application code. [[sources/Temporal OpenAI Agents SDK Integration]] is the reference mapping: the agent orchestration loop runs as a workflow, every LLM invocation and tool call runs as an activity, and event history records each activity's arguments and results — after a crash the workflow replays deterministically and skips completed steps. It explicitly targets three failure classes: rate-limited LLM calls, sporadic network failures, and process crashes. [[sources/Restate Durable AI Loops]] reaches the same guarantee with a per-invocation journal and adds first-class suspension: agents pause indefinitely awaiting external signals at zero cost and resume via journal replay, with durable promises providing transparent idempotency for agent-to-agent messages.

The two engines disagree on structure, and the disagreement is the design decision. Temporal asks the loop to be restructured around a workflow runtime with deterministic workflow code; Restate positions itself as middleware over existing SDK loops ("agents are just code") for dynamic, non-graph loops — noting its Temporal comparison is vendor positioning, not a neutral benchmark. The criterion: the more the agent's control flow is model-decided rather than statically known, the more the journal-over-existing-code style fits; the more the pipeline is fixed, the more workflow-native structure pays for itself.

## Checkpoint Critiques

Checkpointing — periodically persisting full state — is the default durability mechanism, and its critiques define the design space:

- **Granularity.** Recovery lands at the last checkpoint boundary, and everything after it re-executes; [[sources/LangGraph Interrupts]] node-restart semantics show the resulting idempotency burden. Journals and event histories ([[sources/Restate Durable AI Loops]], [[sources/Temporal OpenAI Agents SDK Integration]]) move the boundary to every recorded step.
- **Snapshot cost.** Full snapshots at every step are wasteful for long-running agents; [[sources/LangChain Delta Channels]] stores state deltas instead of full snapshots for exactly this reason.
- **Wrong state.** Checkpointing the transcript preserves bulk, not meaning. [[sources/Google ADK Durable Agents]] argues for explicit durable state — memory schemas, state machines, event-driven dormancy gates — decoupled from conversation transcript, so resume restores what the agent knows rather than everything it said. [[sources/Anthropic Effective Harnesses for Long-Running Agents]] makes the same move at the artifact level: incremental progress and handoff live in files and structured notes, not context.
- **Concurrency blindness.** Neither checkpoints nor replay address whether a restored step's effects still make sense next to concurrent writers; [[sources/Atomix]] treats that as a separate settlement problem.

Event-sourcing the session is the practical synthesis: [[sources/OpenHands Software Agent SDK]] reports that its event-sourced V1 architecture substantially reduced system-attributable failures versus V0 at negligible overhead, in production deployment data.

## Failure Modes of the Fault-Tolerance Layer Itself

- **Retry storms.** Undifferentiated retries against 529 overload or 429 acceleration limits amplify the outage and re-spend tokens; [[sources/Claude API Errors]] is explicit that the two demand different policies.
- **Duplicate irreversible sends.** Retrying a step whose effects were not stratified re-fires emails, payments, and deploys; this is the failure class [[sources/Atomix]] gates.
- **Silent stalls.** [[sources/Claude Agent SDK Streaming vs Single Message]] documents that a Python input-generator exception is logged at debug level and the session stalls without raising — fault tolerance requires liveness signals, not just error handlers.
- **Resume into stale context.** Session resume after a long gap continues from assumptions the world has invalidated; durable state with explicit freshness ([[sources/Google ADK Durable Agents]]) beats transcript replay here.
- **Losing the error evidence.** Recovery that scrubs the failed attempt from context removes the model's ability to avoid repeating it ([[sources/Manus Context Engineering]]).

## Related

- [[operations/durable sessions]]
- [[operations/agent harnesses]]
- [[operations/agent infrastructure]]
- [[concepts/cache-aware harness design]]
- [[concepts/context compaction]]
- [[concepts/handoff over compaction]]
- [[concepts/tool-use contracts]]
- [[concepts/durable dormant agents]]
- [[methods/hook-based control]]
- [[sources/Architecting Resilient LLM Agents]]
