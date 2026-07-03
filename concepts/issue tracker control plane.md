# Issue Tracker Control Plane

An issue tracker control plane treats the issue tracker as the durable work-queue and state machine of a code factory. Tickets are the unit of dispatched work, ticket state transitions are the factory's execution state, and agents, workspaces, evidence, and review attach to tickets rather than to chat sessions.

The important shift is from supervising individual agent sessions to managing work. Sessions crash, compact, and expire; the ticket persists. Everything that must survive any single run — what work exists, what state it is in, who or what has claimed it, and what evidence supports closing it — lives in the tracker, which is why the tracker rather than the harness is the control plane.

## Pattern

```text
signal -> dedup/group -> classify and score -> ticket -> claim -> isolated workspace -> evidence attached -> review -> close or reopen
```

## Stages

| Stage | Decision it owns | Deployed evidence |
|---|---|---|
| Signal intake | which raw events (crashes, alerts, CI failures, human reports) enter the queue | [[sources/RCACopilot]] routes each incoming incident by alert type to a matching handler before any model runs |
| Dedup and grouping | the work-unit boundary: which events are the same fault | [[sources/Sentry Issue Noise Reduction]] cut new issues 40% with embeddings dedup behind deterministic fingerprinting; [[sources/Sentry Issue Grouping v2]] prevents 70% of would-be issues and halved overgrouping |
| Classification and scoring | which tickets deserve agent compute, at what priority and risk tier | [[sources/Sentry Seer]] scans every incoming issue and scores actionability before any fix run starts |
| Dispatch | which agent, which workspace, under what policy | [[sources/GitHub Copilot Coding Agent]] boots a CI VM when an issue is assigned to the agent; [[sources/OpenAI Symphony]] gives each issue its own workspace under bounded concurrency |
| Evidence trail | what proof returns to the ticket | [[sources/Azure SRE Agent Docs]] files prefilled tickets with root-cause hypothesis and diagnostics; [[sources/OpenAI Symphony]] requires proof of work per run |

## Design Guidance

**Grouping sets the work-unit boundary, and its two error modes are not symmetric.** An overgrouped issue hands an agent two faults under one acceptance criterion, so the ticket can never be closed correctly. An undergrouped stream spawns duplicate dispatches that waste compute and collide at merge, but each unit is still well-formed. [[sources/Sentry Issue Grouping v2]] encodes exactly this asymmetry: its model is calibrated to err toward separation when ambiguous, halved overgrouping from 8% to 4%, and turned overgrouping into a continuously measured metric via LLM batch-labeling of merged issues — triage quality becomes a regression-testable property of the factory rather than an impression.

**Put a cheap deterministic gate in front of every model stage.** [[sources/Sentry Issue Noise Reduction]] runs embeddings matching only on hashes that survive traditional fingerprinting, so the deterministic path absorbs the bulk of event volume at sub-100ms with near-zero false merges. The pricing of [[sources/Sentry Seer]] states the same economics from the outside: $0.003 per issue scan against $1 per fix run — a roughly 300x cost asymmetry that makes scanning every signal viable precisely because the expensive stage is entered selectively.

**Record signal provenance at intake, because provenance predicts tractability.** [[sources/Passerine]] found machine-reported bugs (sanitizers, fuzzers) received plausible patches at 73% against 25.6% for human reports. Severity is therefore not the only routing label: a low-severity machine-filed crash with a reproduction is a better auto-dispatch target for [[methods/automated program repair]] than a high-severity human report that needs clarification first. High-severity production signals route through [[operations/incident response]] instead, and its output — agent-written tickets with hypothesis and evidence — re-enters this same queue.

**Treat ticket pickup as a distributed-systems problem.** A tracker consumed by an agent fleet is a message queue, and exactly-once handoff to unreliable consumers is impossible ([[sources/You Cannot Have Exactly-Once Delivery]] grounds this in the Two Generals problem and FLP), so dispatch is at-least-once and claim transitions must be idempotent — two agents grabbing the same ticket must converge instead of double-shipping. Durable-execution runtimes supply the machinery underneath: [[sources/Restate Durable AI Loops]] journals each step and makes suspension first-class, so "awaiting human approval" is a persistent ticket state rather than a live process burning compute ([[operations/durable sessions]], [[operations/harness fault tolerance]]).

**Attach policy and identity at dispatch, not inside the agent.** [[sources/GitHub Copilot Coding Agent]] shows the shape: assigning an issue to the agent is the entire trigger surface, and dispatch carries the guardrails — the agent pushes only to branches it created, the requester cannot approve the agent's PR, and the agent runs behind an internet allowlist. [[sources/OpenAI Symphony]] generalizes this to per-issue workflow policy with retries and human review. When several vendors' agents consume one queue, identity moves to the platform layer: [[sources/GitHub Agent HQ]] gives agents team-member-style identity and access management plus per-branch CI controls. The triage automation itself needs the same governance — [[sources/GitHub Agentic Workflows]] compiles triage loops into CI workflows with read-only defaults and safe outputs, so the control plane's own automation cannot mutate what it only observes.

**Close the loop by writing evidence to the ticket, not the transcript.** [[sources/Azure SRE Agent Docs]] shows agent-written intake with provenance intact: the filed ticket arrives prefilled with the root-cause hypothesis and the diagnostics supporting it, so downstream dispatch inherits the evidence base. [[sources/Meta Agentic Program Repair]] shows why the trail matters at the output end: its 1,589 published diffs and 25.5% landing rate are knowable only because every agent diff flowed through the review system. Acceptance rates per signal class are the feedback that recalibrates intake scoring — without the trail, the factory cannot learn which tickets were worth dispatching ([[concepts/code factories]] closes this learning loop; [[operations/release engineering]] governs what merges and ships).

## The Scale Ladder

The pattern recurs at three sizes. Locally, Git worktrees are the one-developer version: each task or agent thread gets an isolated checkout while the harness decides review and merge — [[sources/OpenAI Codex App Worktrees]] makes worktrees a first-class background-task environment with handoff between local and background work ([[operations/worktree isolation]]). In the cloud, [[sources/Cursor Scaling Long-Running Autonomous Coding]] describes sandboxed per-agent environments with branch handoff back to the developer. At factory scale, [[sources/OpenAI Symphony]] applies the same one-workspace-per-unit-of-work discipline with the issue tracker as the coordinating store. The invariant across all three: work units own isolation; the control plane owns state.

## Related

- [[concepts/code factories]]
- [[operations/incident response]]
- [[operations/release engineering]]
- [[methods/automated program repair]]
- [[operations/agent harnesses]]
- [[operations/worktree isolation]]
- [[operations/durable sessions]]
- [[operations/harness fault tolerance]]
- [[operations/agent observability]]
- [[operations/permissions]]
- [[systems/Codex]]
