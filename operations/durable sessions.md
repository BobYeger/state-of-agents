# Durable Sessions

Durable sessions store agent events, state transitions, artifacts, and progress outside the model context window so work can resume, audit, and recover.

## Durable-Execution Engines

Durable-execution engines make the session's execution state — not just its transcript — survive crashes, by recording every step and replaying past completed work on recovery. [[sources/Temporal OpenAI Agents SDK Integration]] is the reference mapping: the agent loop runs as a workflow, each LLM invocation and tool call runs as an activity, and event history lets a crashed workflow replay deterministically without re-running completed steps or re-spending tokens. [[sources/Restate Durable AI Loops]] reaches the same guarantee with a per-invocation journal layered over existing SDK loops, and adds first-class suspension: agents pause indefinitely awaiting external signals at zero cost and resume via journal replay. The structural disagreement between the two — restructure the loop around a workflow runtime versus journal the loop as it is — is the main selection criterion, and [[operations/harness fault tolerance]] treats it in full alongside retry policy and side-effect idempotency.

Two boundary results scope what durability can promise. [[sources/You Cannot Have Exactly-Once Delivery]] shows exactly-once delivery is impossible over unreliable channels, so durable task pickup must be at-least-once plus idempotent. [[sources/Atomix]] shows that replaying steps is not enough when tool side effects interleave with concurrent work: partial effects, losing-branch residue, stale writes, and irreversible sends need transactional settlement, not just checkpoints.

Checkpoint granularity and content remain design choices inside this space: [[sources/LangChain Delta Channels]] stores state deltas rather than full snapshots, and [[sources/Google ADK Durable Agents]] argues for resuming from explicit durable state (memory schemas, state machines, event-driven wake) rather than replayed chat history.

## Streaming and Interruption Semantics

A durable session is usually consumed through a stream, and the stream's reconnect and interruption semantics decide what "resume" actually restores.

- [[sources/Claude Managed Agents Session Event Stream]] is the most explicit first-party spec: streams are resumable by ID-dedup rather than cursors (reconnect, list full event history to seed seen-IDs, then tail live), deltas are best-effort and never replayed, but buffered complete events always appear in history — so accumulated previews must never be treated as final. Mid-turn steering is a two-step protocol: `user.interrupt`, then a redirecting `user.message`.
- [[sources/Claude Agent SDK Streaming vs Single Message]] documents which session capabilities exist only on a persistent input stream — real-time interruption, message queueing and injection, images — while stateless environments fall back to session resume via `continue`/`continue_conversation` options.
- [[sources/LangGraph Interrupts]] shows the checkpointer-based version: `interrupt()` persists exact state with `thread_id` as the resume cursor, but resuming restarts the whole node, so pre-interrupt code re-executes and must be idempotent.
- [[sources/OpenAI Codex App Server Docs]] exposes the session objects themselves — thread, turn, item — with `thread/resume`, `thread/fork`, and `turn/steer` as client-callable operations, making durable sessions a control surface rather than only a recovery mechanism.

The common lesson across all four: durable sessions need two distinct guarantees, a durable event history that survives disconnects and crashes, and defined interruption points whose resume semantics (what re-executes, what is dropped, what is final) are explicit rather than assumed.

Buzz supplies a useful counterexample to equating those guarantees. Signed channel history and encrypted engrams are durable records, but the audited ordinary approval path does not persist a waiting action and resume it after approval. A system can preserve everything the team said and still lack durable workflow execution ([[sources/Buzz Repository]]).

## Related

- [[concepts/long-horizon agents]]
- [[concepts/context engineering]]
- [[concepts/durable dormant agents]]
- [[operations/agent infrastructure]]
- [[operations/harness fault tolerance]]
- [[operations/agent harnesses]]

## Related Sources

- [[sources/Cloudflare Agent Memory|Agents that remember: introducing Agent Memory]]
- [[sources/Google ADK Durable Agents|Build Long-running AI agents that pause, resume, and never lose context with ADK]]
- [[sources/LangChain Delta Channels|Delta Channels: Evolving our Runtime for Long-Running Agents]]
- [[sources/Cloudflare Think Docs|Cloudflare Think docs]]
- [[sources/Cloudflare Dynamic Workflows|Introducing Dynamic Workflows]]
- [[sources/OpenAI Symphony|OpenAI Symphony]]
- [[sources/OpenAI Codex Using Goals]]
- [[sources/Anthropic Effective Harnesses for Long-Running Agents|Effective harnesses for long-running agents]]
- [[sources/Cloudflare MCP Auth Durable Objects|Piecing together the Agent puzzle: MCP, authentication & authorization, and Durable Objects free tier]]
- [[sources/Cloudflare Project Think|Project Think: building the next generation of AI agents on Cloudflare]]
- [[sources/Anthropic Managed Agents|Scaling Managed Agents: Decoupling the brain from the hands]]
- [[sources/Temporal OpenAI Agents SDK Integration]]
- [[sources/Restate Durable AI Loops]]
- [[sources/Atomix]]
- [[sources/You Cannot Have Exactly-Once Delivery]]
- [[sources/Claude Managed Agents Session Event Stream]]
- [[sources/Claude Agent SDK Streaming vs Single Message]]
- [[sources/LangGraph Interrupts]]
- [[sources/OpenAI Codex App Server Docs]]
- [[sources/Buzz Repository]]
