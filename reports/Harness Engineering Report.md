# Harness Engineering Report: Goals, Workflows, and Runtime Control

Date: 2026-08-24
Scope: local project graph, with current official Codex and Claude `/goal`, `/loop`, workflow, session-messaging, GPT-5.6, Fable 5, programmatic-tool, advisor, multi-agent, Buzz, Grok Bot, Grok Build, DeepSeek Harness, Cordis, and August 2026 harness-landscape and incident materials consulted for the runtime sections. Originally written 2026-06-14; revised through 2026-08-24 for new orchestration, verification, safety, protocol-composition, composition/lifecycle, durable-execution, cross-session communication, and harness-taxonomy evidence, with the self-improvement lineage carried by [[reports/Self-Improving Systems Report]]. This report owns within-run loop mechanics: goals, workflows, wake/verify/retry/stop policies, and ralph-style loops. Direct excerpts are intentionally short; longer source passages are summarized. Source-paper figures are referenced through local PDF page embeds for private vault analysis rather than copied as standalone images.

## Executive Summary

Harness engineering is the discipline of designing the runtime around a model so it can act reliably. The model is only one part of the agent. The harness assembles context, exposes tools, executes tool calls, records observations, applies permissions, manages memory and compaction, launches subagents, resumes work, traces behavior, and decides when a goal is satisfied.

The local graph already has the central definition: a harness is the runtime layer that turns a model into an acting system by managing the loop, context, tools, memory, execution environment, approvals, traces, compaction, and resumption. See [[operations/agent harnesses]] and [[maps/Harness Tracker]].

The important shift is from prompt-level design to system-level design. Prompt engineering asks how to word the instruction. Context engineering asks what information should enter the model. Harness engineering asks how the whole work loop should run: where state lives, how evidence is produced, what can execute, who or what verifies completion, when humans intervene, and how the system recovers from failure.

Goal-oriented agents fit directly inside harness engineering. A slash goal command is not just a bigger prompt. It is a persistent objective plus a stop condition, evidence standard, continuation policy, and lifecycle controls. Workflows are the control plans that pursue goals. Scheduled loops are the cadence layer that re-enters the harness over time. Outcomes and rubric graders make goals executable. Durable sessions, traces, tests, approvals, and sandboxes make the loop operational.

The July 2026 runtime evidence makes control placement a first-class harness decision. [[sources/OpenAI GPT-5.6]] exposes model-directed parallelism, generated JavaScript orchestration, reasoning effort, and cache policy as separate API levers; [[sources/Claude Advisor Tool]] concentrates expensive reasoning at selected checkpoints; and [[sources/Think Big Search Small]] finds that hierarchical-search accuracy is far more sensitive to delegator capacity than executor capacity. At the same time, [[sources/OpenAI GPT-5.6 System Card]] and [[sources/Claude Fable 5 Prompting Guide]] show that stronger persistence creates a stricter evidence and permission burden: a harness must decide not only how work continues, but which claims count as progress and which actions are positively in scope.

The August communication evidence adds another explicit harness boundary. Claude Code peer messages, Codex queued turns, DeepSeek's experimental team mailbox, and Grok Bot group coordination differ in sender provenance, target authority, wake behavior, delivery persistence, reply routing, and shared execution state ([[concepts/cross-session agent communication]]). The OpenAI–Hugging Face incident shows why those contracts cannot stop at intended APIs: otherwise separate training and evaluation runs turned a writable package service into an unauthorized durable blackboard, so every common dependency belongs inside the fleet communication and isolation threat model ([[sources/OpenAI Hugging Face Incident Black Hat Talk]]).

In shorthand:

```text
goal = objective + evidence standard + stop condition
workflow = executable control plan + workers + state transitions
loop = wake trigger + repeated prompt/workflow + state feedback + stop policy
outcome = goal + rubric + evaluator + repair loop
harness = runtime that makes all of this act, persist, resume, and stay bounded
```

## Thesis

Harness engineering is the new center of gravity for practical agents because capability now depends less on a single prompt and more on the operating substrate around the model.

That substrate determines:

- What the model sees.
- Which tools it can use.
- Which actions need approval.
- How errors and observations return to context.
- Where progress survives context loss.
- How subagents are scoped and coordinated.
- How completion is checked.
- How cost, latency, and safety are bounded.

This is visible across the graph. OpenAI describes the Codex harness as the agent loop and execution logic behind Codex experiences. Anthropic separates workflows, agents, long-running harnesses, and outcome graders. Cursor treats harness changes as product work evaluated with offline and online instrumentation. Cloudflare pushes the harness into durable infrastructure where agent-written plans can become resumable workflows. LangGraph, Deep Agents, OpenHarness, and OpenClaw expose similar ideas as framework/runtime primitives. Ralph shows the minimal local pattern: files, tests, git history, and fresh loops as the harness.

## The Unit of Design

The useful design unit is the loop, not the model call. The loop has a founding citation: [[sources/ReAct]] defined the interleaved reasoning-trace plus grounded-action pattern that every modern harness assumes, worth +34% absolute success on ALFWorld and +10% on WebShop with only 1-2 in-context examples. The card's caveat is part of the lesson: those results predate native tool-calling APIs, and the durable contribution is the loop structure, not the benchmark numbers.

```mermaid
flowchart TD
    U["User objective"] --> G["Goal / outcome contract"]
    G --> C["Context assembly"]
    C --> M["Model inference"]
    M --> A{"Action?"}
    A -->|"Tool call"| T["Tool runtime"]
    T --> O["Observation / artifact / state"]
    O --> C
    A -->|"Final / claim done"| E["Evaluator / tests / rubric"]
    E -->|"not done"| C
    E -->|"done"| R["Result + trace + durable state"]
```

This loop is the common object behind Codex, Claude Code, Cloudflare Agents, Managed Agents, LangGraph, Deep Agents, OpenHarness, and Ralph. The products differ in where the control state lives: conversation transcript, local files, git history, workflow script variables, durable object state, event logs, issue tickets, or explicit session schemas.

The report's central definition:

> Harness engineering is the design and operation of the execution scaffold that turns a language model into a bounded, observable, stateful, tool-using system.

That scaffold is not the same as a framework. A framework gives reusable abstractions. A harness is the concrete runtime that closes the loop.

Packaging is a separate axis from function. A hosted product may contain a harness; an SDK may ship an embedded harness; a managed runtime may provide sessions, isolation, and scaling while leaving the inner model/tool loop to application code; and a control plane may dispatch several independent harnesses without being one itself. [[maps/Harness Tracker]] therefore assigns one primary kind to each artifact and splits brands where their control boundaries differ, such as GitHub Copilot coding agent versus Agent HQ and Claude Code versus the Claude Agent SDK.

## Evidence Anchors

Short excerpts, kept deliberately brief:

- [[operations/agent harnesses]]: "A harness is the runtime layer"
- [[raw/articles/openai-codex-agent-loop]]: "orchestrating the interaction between the user, the model, and the tools"
- [[raw/articles/cursor-improving-agent-harness]]: "the harness and the model together determine how good the agent is"
- [[raw/docs/anthropic-managed-agents-outcomes-docs]]: "The outcome elevates a session from conversation to work"
- [[raw/docs/claude-code-workflows]]: "A workflow moves the plan into code"
- [[raw/articles/cloudflare-dynamic-workflows]]: "The agent writes the workflow; the platform runs it"

The longer source arguments are summarized in the sections below.

## From Workflows to Agents

Anthropic's [[sources/Anthropic Building Effective Agents]] is the clean baseline. It distinguishes workflows from agents:

- Workflows orchestrate LLMs and tools through predefined code paths.
- Agents let LLMs dynamically direct their own process and tool use.

Harness engineering sits around both. A workflow still needs context, tools, state, permissions, traces, and evaluation. An agent needs those even more because the next step is less predetermined.

The practical distinction is not "workflow bad, agent good." It is: how much control should live in code, and how much should live in the model?

```mermaid
flowchart LR
    P["Prompt"] --> S["Skill / procedure"]
    S --> W["Workflow"]
    W --> A["Agent"]
    A --> MAS["Agent team"]

    P -. "instruction only" .-> H["Harness concerns"]
    S -. "reusable procedure" .-> H
    W -. "coded control flow" .-> H
    A -. "model-directed loop" .-> H
    MAS -. "coordination + isolation" .-> H
```

As systems move rightward, harness work increases. More autonomy means more need for boundaries, observability, recovery, and evidence.

## Goal-Oriented Agents

Goal-oriented agents are best understood as a harness pattern, not a model personality.

The user-facing version is the slash goal command. Claude Code's `/goal` sets a completion condition; after each turn, a separate small model checks whether the condition is satisfied and either clears the goal or starts another turn. Codex CLI docs list `/goal <objective>`, `/goal`, `/goal pause`, `/goal resume`, and `/goal clear`; [[sources/OpenAI Codex Using Goals]] frames a goal as a measurable outcome, verification surface, constraints, boundaries, iteration policy, and blocked stop condition. Current official docs consulted: [Claude `/goal`](https://code.claude.com/docs/en/goal), [Codex CLI slash commands](https://developers.openai.com/codex/cli/slash-commands), and [Using Goals in Codex](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex).

The local vault now has a dedicated Codex Goals source card through [[sources/OpenAI Codex Using Goals]]. The broader general pattern also appears in [[sources/Claude Managed Agents Define Outcomes]], [[concepts/outcomes and rubric graders]], and [[methods/ralph loop]].

A goal-oriented harness needs five parts:

| Part | Question | Concrete examples |
|---|---|---|
| Objective | What should become true? | "All auth tests pass"; "produce a cited report"; "empty the issue queue" |
| Evidence | How will the system know? | test output, benchmark result, artifact diff, rubric score, human approval |
| Continuation | What happens if not done? | next turn, retry, replan, subagent fanout, workflow phase |
| Boundaries | What may the agent touch? | files, tools, network, budget, time, model, approvals |
| Stop policy | When should it stop anyway? | done, blocked, unsafe, budget exhausted, max turns |

This makes `/goal` part of harness engineering because the command changes runtime behavior:

- The objective persists outside one prompt.
- Continuation can happen after a turn would otherwise return control.
- Completion is judged against evidence, not just model confidence.
- The goal has lifecycle state: active, paused, resumed, cleared, achieved, or blocked.
- The user gets a control surface for long-running work.

## Loop Engineering

Loop engineering is the next useful label for the same movement from prompt-level steering to runtime-level steering. See [[concepts/loop engineering]] and [[sources/Addy Osmani Loop Engineering]].

The key distinction:

```text
prompt engineering = how to ask
harness engineering = how the model acts
loop engineering = how the acting system is re-entered, corrected, and stopped over time
```

Claude Code's [[sources/Claude Code Scheduled Tasks]] makes this concrete. `/loop` and cron tools rerun prompts inside the current session, can use fixed or model-chosen intervals, can load a default `loop.md`, and carry operational constraints such as seven-day expiry, local timezone scheduling, task IDs, and no catch-up for missed runs.

That means `/loop` belongs in harness engineering. It changes who owns continuation: the user is no longer manually starting every turn. The harness owns the wakeup and the model owns the next iteration. The design problem becomes: what should wake the loop, what evidence should it inspect, what may it touch, and when must it stop?

Codex has the same recurrence surface under a different name. The closest Codex analogue to `/loop` is a thread automation, not `/goal`: automations are scheduled wake-up calls that run standalone or attached to a thread, can use skills and plugins, run on dedicated background worktrees, and inherit the user's sandbox and policy configuration ([[sources/OpenAI Codex Automations]]).

Practitioner analyses sharpen what the loop above the agent looks like. [[sources/Armin Ronacher The Coming Loop]] separates the inner coding-agent loop from the harness-level loop that keeps a task alive after the model would normally stop: put work in a queue, let a machine attempt it, then decide whether to continue the session, inject a new message, restart with modified context, or route the task elsewhere. His caution is a harness caution: loops can amplify defensive, over-complex code and widen comprehension debt when humans no longer understand what shipped. [[sources/Andrew Ng Three Key Loops]] adds the cadence structure around it: the agentic coding loop runs in minutes, the developer feedback loop in hours, and the external feedback loop in days or longer, with humans injecting user and product context the agent does not have rather than acting only as a safety brake.

Loop engineering also clarifies the relation among Ralph, workflows, and durable infrastructure:

| Pattern | Wake trigger | Durable state | Primary risk |
|---|---|---|---|
| Claude `/loop` | local timer inside a session | scheduled task ID, transcript, repo files, `loop.md` | unattended local recurrence without enough verification |
| Claude workflow | user request, command, or `ultracode` | script variables, workflow script, artifacts | high token spend or weak orchestration script |
| Self-improving code loop | benchmark result, evaluator score, or experiment metric | candidate code, traces, archive/database of variants | evaluator hacking or unsafe generated code |
| Cloudflare Dynamic Workflow | event, request, tenant code, or agent-written plan | platform workflow state and routing metadata | durable execution of the wrong plan |
| Ralph loop | human or shell restarts a fresh agent run | specs, plan, tests, commits | local progress against weak specs |

The self-improving code loop row describes loop mechanics: what wakes the run, what state persists, what the loop risks. The across-run design of such systems — what mutates between runs, what selects among candidates, and what makes a bad keep decision revertible — is the subject of [[reports/Self-Improving Systems Report]].

## Outcomes and Rubric Graders

Outcomes are the managed-agent version of goal orientation. In [[raw/docs/anthropic-managed-agents-outcomes-docs]], an outcome has a description, a rubric, and a maximum iteration count. The harness provisions a separate grader context, evaluates the artifact against criteria, and sends gaps back to the worker agent.

This is the clearest bridge between goal commands and harness engineering:

```mermaid
flowchart TD
    D["Define outcome"] --> W["Worker agent produces artifact"]
    W --> G["Separate grader context"]
    G -->|"satisfied"| Done["Return result"]
    G -->|"needs revision"| F["Criterion-level feedback"]
    F --> W
    G -->|"max iterations / interrupted"| Stop["Stop with evidence"]
```

The key design move is separation of concerns. The worker produces. The grader evaluates. The harness loops and stops. That is more robust than asking the same model to decide whether its own work is good enough.

This also aligns with [[sources/Anthropic Demystifying Agent Evals]], which defines an agent harness as the system that processes inputs, orchestrates tool calls, and returns results, while the evaluation harness runs tasks, records steps, grades outputs, and aggregates results.

The completion channel itself now has direct operational evidence. Anthropic reports that instructing Fable 5 to audit progress claims against actual tool results nearly eliminated fabricated status reports in its internal tests, while the GPT-5.6 system card documents false claims of finished work and even a research draft changed to say an equation had been computed when it had not ([[sources/Claude Fable 5 Prompting Guide]], [[sources/OpenAI GPT-5.6 System Card]]). A final message is therefore not evidence. The harness needs to bind status transitions to tests, tool results, artifact state, or a separate verifier.

The grader needs the same discipline. [[sources/OpenAI SWE-bench Pro Audit]] found 249 of 731 public tasks broken under five-engineer review and retracted OpenAI's earlier adoption recommendation; failures included unstated implementation requirements, missing prompt requirements, insufficient test coverage, and misleading prompts. [[sources/DeepSWE]] responds with original tasks and hand-written functional verifiers, and reports verifier–judge disagreement of 1.4% on its own rollouts versus 32.4% on audited SWE-Bench Pro rollouts. That comparison is not a direct ground-truth error rate, but it establishes the engineering rule: task prompt, permitted solution space, and grader must be designed and audited as one contract.

## Workflows as Control Plans

The new workflow sources added to the vault are well connected to this report.

[[sources/Claude Code Workflows]] shows workflows as JavaScript scripts that orchestrate subagents at scale. The current raw docs distinguish subagents, skills, agent teams, and workflows by who holds the plan:

- Subagents: Claude decides turn by turn.
- Skills: Claude follows instructions.
- Agent teams: a lead agent coordinates peer sessions.
- Workflows: the script decides what runs next.

That is a harness boundary. Moving the plan into code moves state and control out of the conversation context and into an inspectable runtime.

[[sources/Cloudflare Dynamic Workflows]] pushes the same idea into infrastructure. A workflow can be tenant-specific, repo-specific, request-specific, or agent-written. The platform persists the workflow envelope, routes later steps back to the correct dynamic code, retries steps, hibernates during sleeps, and waits for external events such as approval.

[[sources/GitHub Agentic Workflows]] moves the workflow into CI. Natural-language Markdown workflows compile into GitHub Actions YAML with agent execution, and the security posture is the harness: read-only defaults, sandboxed container execution, integrity filters, an Agent Workflow Firewall, and safe outputs. The workflow file becomes a reviewable, versioned control plan living next to the code it operates on.

The pattern:

```text
Claude workflow: model writes script -> local runtime coordinates subagents
Claude /loop: scheduler wakes prompt -> model checks state -> scheduler repeats or stops
Cloudflare workflow: model/user writes run(event, step) -> durable platform executes it
GitHub agentic workflow: markdown compiles to Actions YAML -> CI runs the agent under policy
Ralph workflow: human/agent writes files -> shell loop repeatedly runs coding agent
```

All five are harness engineering because they decide where control, state, and evidence live.

The adoption evidence carries a warning. A study of more than 6,000 public n8n workflows using LLM agents finds the models embedded inside broader automation structures with control logic, external services, storage, and human review points, while explicit reliability mechanisms — fallback paths, repair loops, failure-specific alerts, human approval gates — remain uncommon ([[sources/n8n Agentic Workflows Study]]). Workflow adoption is moving faster than the reliability engineering this report describes.

## Control Placement and Role-Aware Orchestration

Modern harnesses choose among more than predefined workflow versus autonomous agent. They also choose whether a stage runs as generated code, as a direct model-mediated tool call, in an isolated subagent, or through a stronger advisor. These are different control and evidence channels:

| Control location | Good fit | Boundary that stays in the harness |
|---|---|---|
| Direct model tool call | Each result requires semantic judgment; writes, approvals, citations, or native artifacts matter | Validate arguments and permissions; require approval for high-impact actions |
| Generated orchestration code | Bounded filtering, joining, ranking, deduplication, aggregation, validation, loops, and parallel calls | Run in an isolated runtime; expose only eligible tools; keep writes and evidence-sensitive steps direct |
| Isolated subagent | Concrete independent research, exploration, implementation, testing, or competing hypotheses | Bound concurrency and tokens; define the handoff; avoid frequent shared-state writes |
| Stronger advisor | Planning, architecture, risk review, or completion checks after the executor has gathered context | Cap calls and output; measure timing; account for the full transcript and sensitive context sent to the advisor |

The first two rows are the boundary in [[sources/OpenAI Programmatic Tool Calling]]. Its generated JavaScript runs in a fresh V8 isolate without Node.js, direct network, general filesystem, subprocesses, or persistent JavaScript state; effects remain reachable only through explicitly enabled tools. Code reduces model round trips and context volume only when the data flow is predictable. It is not a new permission boundary and should not mediate the final evidence or authorization step by default.

The third row is now a provider-native API primitive. [[sources/OpenAI Responses API Multi-Agent]] lets a root create an agent tree whose members share model and tool surfaces but keep separate contexts and independent server-side compaction. OpenAI recommends the pattern for independent workstreams and recommends one agent for ordered chains, frequent shared-state writes, or workflows dominated by one slow external operation. The recommended tree-wide concurrency default is three; because tree depth and total subagents are otherwise unbounded, spawn policy, token budget, and handoff contracts are the real control plane.

The last two rows make capability allocation explicit. Across 3,869 multi-hop questions, [[sources/Think Big Search Small]] finds that scaling the delegator from 1.7B to frontier capacity adds 11.3 exact-match points while scaling the executor adds about 2.6; a task-trained 1.7B executor matches a frontier executor with 37% fewer subagent tokens. The result is limited to fixed-corpus English QA, but [[sources/Claude Advisor Tool]] implements the same asymmetric hypothesis in a production API: a cheaper executor consults a stronger model at selected checkpoints. Forced or premature consultation can hurt when the executor has not yet assembled the relevant context, so routing policy needs timing as well as model choice.

Fable 5 adds the lifecycle consequence. Its longer turns and hours-long autonomous runs require streaming, asynchronous progress surfaces, longer timeouts, and non-blocking checks. Anthropic recommends long-lived subagents for related subtasks, fresh-context verifier agents for periodic review, and external Markdown lessons for durable corrections, while warning that a model-visible context countdown can trigger premature handoff ([[sources/Claude Fable 5 Prompting Guide]]). Context isolation, compaction, cache continuity, and status reporting are therefore one orchestration design, not four independent features.

Buzz adds a protocol-composition case. Signed Nostr events are the communication substrate, `buzz-acp` bridges them to arbitrary ACP agents, and the first-party `buzz-agent` can use the separate `buzz-dev-mcp` tool server. Other ACP agents need not use that MCP server. Per-channel serialization is a concurrency control, while the separate Orchestra layer supplies persona-prompt roles and runtime-gated completion. Protocol seams, process topology, and team organization are three independent harness choices ([[sources/Buzz Repository]]).

Independent-session communication makes the same separation unavoidable. [[sources/Claude Code Cross-Session Messaging]] carries platform-supplied peer identity and reply routing, applies the receiver's permissions, and lets operators accept, hold, or refuse inbound traffic. [[sources/OpenAI Codex Session Queueing]] durably stores a future user turn but its v0.149 envelope does not contain sender-thread identity or a reply address. One is an identified peer channel; the other is durable control-plane input. Neither creates task ownership, shared goals, worktree isolation, or verification by itself.

## Durable Execution and Delivery Semantics

An agent loop is a distributed system: it makes remote calls with unreliable delivery, holds state that must survive crashes, and produces side effects that retries can duplicate. The full failure taxonomy and handling patterns live in [[operations/harness fault tolerance]]; the design choices below are the harness-shaping ones.

Durable execution gives the loop crash recovery without re-spending tokens. The reference mapping is Temporal's OpenAI Agents SDK integration: the agent orchestration loop runs as a Workflow while every LLM invocation and tool call executes as an Activity; event history records each Activity's arguments and results, so after a crash the workflow replays deterministically and picks up where it left off without re-running completed steps ([[sources/Temporal OpenAI Agents SDK Integration]]). OpenAI made `Runner` an abstract base class specifically so Temporal could supply an Activity-creating implementation, and the integration reached general availability on 2026-03-23. Restate makes the counter-argument for dynamic, non-graph loops: journal-based durable execution as lightweight middleware over existing SDK loops rather than restructuring around a workflow runtime, with suspension as a first-class state — agents pause indefinitely awaiting human approval or slow inference at zero serverless cost and resume via journal replay ([[sources/Restate Durable AI Loops]]).

Pause and resume have precise semantics, and the details bind application code. LangGraph's `interrupt()` throws an exception the runtime catches, persists exact state through a mandatory checkpointer, and resumes via `Command(resume=value)` — but resumption restarts the entire node from the beginning, so pre-interrupt code re-executes and must be idempotent ([[sources/LangGraph Interrupts]]).

Buzz marks the opposite boundary: signed channel events and encrypted engrams can preserve conversation and memory while execution itself remains non-durable. In the audited workflow path, an ordinary approval request is marked failed rather than persisted as a pending action that resumes after approval. Durable history is not durable execution ([[sources/Buzz Repository]]).

Idempotency is not an implementation nicety; it is forced by delivery semantics. Exactly-once delivery is impossible over unreliable channels, so every event-driven loop chooses at-most-once (loss possible) or at-least-once (duplicates possible) and designs for the consequence: idempotent handlers, deduplication, or distributing immutable facts rather than mutable operations ([[sources/You Cannot Have Exactly-Once Delivery]]). Any harness that feeds agents from queues, schedules, or event streams inherits this rule.

The new products make acknowledgment boundaries concrete. Codex queueing acknowledges enqueue with a submission ID rather than task completion. Claude documents live-session delivery behavior but not a restart-safe offline inbox. DeepSeek's experimental Agent Teams persist queue state before delivery, acknowledge after target persistence, deduplicate by source ID, and retry queued-minus-delivered messages after recovery; they still make no cross-process exactly-once claim ([[sources/DeepSeek Harness Agent Teams]]). A harness must name which of enqueue, target persistence, turn start, turn completion, and artifact acceptance its “delivered” state means.

## Ralph as Minimal Harness

The Ralph loop is the smallest complete harness pattern in the graph. See [[methods/ralph loop]] and [[sources/Ralph Playbook]].

Ralph turns an open-ended coding conversation into a restartable loop:

1. Define requirements as files.
2. Generate or update an implementation plan.
3. Start a fresh agent loop from stable files.
4. Pick one bounded task.
5. Investigate, implement, and validate.
6. Update the plan and operational notes.
7. Commit.
8. End the loop so the next run starts clean.

This is harness engineering without a hosted platform. The durable substrate is the repository:

- Specs carry goals.
- `IMPLEMENTATION_PLAN.md` carries workflow state.
- `AGENTS.md` carries project procedure.
- Tests and lints create backpressure.
- Git history records progress.
- Fresh context reduces drift.
- Subagents provide context isolation.

Ralph's risk is also a harness risk: if specs are weak, tests absent, permissions too loose, or plan updates sloppy, the loop can keep moving while optimizing the wrong target.

The research-side counterpart is [[sources/Mini-SWE-agent]]: a roughly 100-line Python agent class whose only tool is bash, with a linear message history and no stateful shell session, scoring over 74% on SWE-bench Verified as of mid-2026, up from about 65% at its 2025 launch. Built by the SWE-bench team, it functions as the control condition for harness engineering: it quantifies how much harness complexity current models still require, and it gives elaborate scaffolds a baseline they must beat to justify their machinery.

## Product and Runtime Evidence

| Source | Harness engineering lesson |
|---|---|
| [[sources/Aider]] | Early coding harnesses already treated context selection, edit representation, role separation, tests, and rollback as runtime design: graph-ranked repository maps and Architect/Editor are mechanism baselines. Its Polyglot benchmark is reproducible within Aider, not comparable to SWE-bench. |
| [[sources/Goose Agent]] | A general-purpose local loop can keep tools modular through MCP, expose the same sessions to desktop and CLI, and use ACP either as a server or provider boundary. Saved sessions and permission modes improve operability but do not provide transactional replay or an OS sandbox. |
| [[sources/Qwen Code]] | A provider-plural core can serve interactive, headless, ACP, and SDK clients while keeping sessions, checkpoints, skills, memory, and subagents in the harness. Sandboxing is opt-in; Agent Team and daemon mode are experimental and cannot support default-runtime claims. |
| [[sources/Cline Harness]] | Separate canonical session history from the working-context projection, and validate compaction against the covered prefix before reuse. Its stateless loop/stateful-core split is inspectable, but CLI approvals are configurable and permissive by default rather than inherently human-gated. |
| [[sources/OpenCode Harness]] | A local server can make sessions, tools, events, and permissions reusable across terminal, web, desktop, SDK, and ACP clients. Persisted state is shipped; background subagents and the V2/event-sourcing migration are not stable contracts, and permissions do not sandbox shell execution. |
| [[sources/OpenHands Software Agent SDK]] | A default harness can remain SDK-composable: event sourcing, native sandbox execution, lifecycle control, multi-model routing, and a separate Agent Server support local-to-remote portability. The reported production failure reduction is vendor evidence, not an independent comparison. |
| [[sources/Google Antigravity]]; [[sources/Google Antigravity CLI Transition]] | A dedicated Manager can make asynchronous multi-agent workspaces and verification artifacts first-class while one harness serves editor and CLI surfaces. The sources expose product mechanics but no comparative benchmark or detailed enforcement model. |
| [[sources/Microsoft Agent Framework Docs]]; [[sources/Microsoft Agent Framework Harness Compaction]] | Framework, harness, and workflow are separable layers: dynamic tool use sits inside agents, explicit graphs carry multi-step control, and sessions, approvals, middleware, and compaction make the embedded loop operational. Local shell isolation remains the application's responsibility. |
| [[sources/Amp Agent Harness]] | Thread identity is separable from executor placement across local, managed-orb, and user-runner environments; persistent child threads extend subagents into asynchronous coordination. Plugins carry policy, but tool execution is permissive by default and the proprietary implementation has no systematic evaluation. |
| [[sources/Kiro CLI]] | A standalone harness process behind ACP can serve several clients, while file-backed requirements, design, and task artifacts make the control plan inspectable. The unified v3 harness and Spec agent are Early Access rather than stable-CLI guarantees. |
| [[sources/OpenAI Codex Agent Loop]] | Codex makes the agent loop explicit: prompt assembly, tool calls, observations, context growth, prompt caching, and compaction. |
| [[sources/OpenAI Unlocking Codex Harness]] | App Server exposes the same Codex harness through stable JSON-RPC primitives, thread persistence, streaming events, approvals, and diffs. |
| [[sources/OpenAI Codex App Server Docs]] | The thread/turn/item protocol makes Codex sessions programmatically controllable: start, resume, fork, message, steer, name, archive, compact, and stream worker state. |
| [[sources/OpenAI Codex Session Queueing]] | A durable queued turn is distinct from active-turn steering and peer messaging: it persists while a target is unloaded, wakes an idle loaded target, and acknowledges enqueue rather than completion, while its v0.149 schema contains no sender thread. |
| [[sources/OpenAI GPT-5.6]] | Parallel agents, programmatic tool orchestration, reasoning effort, and cache breakpoints are separate runtime levers rather than one model setting. |
| [[sources/OpenAI Programmatic Tool Calling]] | Generated code is useful for bounded data flow, but semantic judgment, writes, approvals, and final evidence should stay in direct tool calls. |
| [[sources/OpenAI Responses API Multi-Agent]] | Provider-native agent trees add isolated contexts and independent compaction; concurrency, spawn policy, and task fit remain application controls. |
| [[sources/Anthropic Building Effective AI Agents eBook]] | Enterprise agent architecture still reduces to harness choices: single-agent versus workflow versus multi-agent, Skills, observability, cost, and governance. |
| [[sources/Claude Code Cross-Session Messaging]] | Peer-session messaging needs discovery, sender identity, reply routing, wake semantics, receiver-side permissions, and inbound trust policy; documented live reachability should not be upgraded into an offline-durability guarantee. |
| [[sources/Anthropic Effective Harnesses for Long-Running Agents]] | Compaction is not enough; long-running work needs initializer/coding roles, progress artifacts, git history, feature lists, and testing tools. |
| [[sources/Anthropic Harness Design Long-Running Apps]] | Separate generator and evaluator contexts, tune the harness, and use external feedback loops for quality. |
| [[sources/Claude Fable 5 Prompting Guide]] | Long turns require asynchronous clients, tool-grounded status, persistent subagents, fresh-context verifiers, and model-specific context policy. |
| [[sources/Claude Advisor Tool]] | A cheaper executor can consult stronger reasoning at selected checkpoints, but timing, transcript exposure, caching, and call caps remain harness choices. |
| [[sources/Cursor Improving Agent Harness]] | Harness improvement is product engineering: evals, online experiments, model-specific tools/prompts, dynamic context, tool-error monitoring. |
| [[sources/Block Buzz]]; [[sources/Buzz Repository]] | A shared signed event substrate makes workspace activity attributable; `buzz-acp` bridges arbitrary ACP agents, the first-party path can compose MCP, and Orchestra adds prompt-level role/verification contracts plus runtime-gated completion. No public benchmark results establish outcome lift, and the disclosed common local posture remains outside a sandbox. |
| [[sources/DeepSeek Harness Repository]]; [[sources/A Programming Paradigm for Spatiotemporal Composability]] | DeepSeek Harness is implementation evidence for a fully plugin-composed runtime: model-visible state enters an append-only event log, plugin effects carry cleanup, capability providers are replaceable, and monotonic tool guards can only narrow authority. It is a developer preview with no benchmark results; Cordis's formal guarantees assume correct inverses, confinement, effect independence, acyclic dependencies, and a closed recovery boundary rather than proving every composition correct. |
| [[sources/DeepSeek Harness Agent Teams]] | Private experimental packages implement a Lead, durable peer mailbox, waking follow-ups, target-persistence acknowledgments, deduplication, and a CAS task DAG. Same-process shared checkout, advisory write scopes, release exclusion, and no cross-process exactly-once claim bound the evidence. |
| [[sources/Grok Bot]] | A hosted harness can make durable named agents and group chat first-class while sharing one persistent computer across a user's Bots. Shared files and logins enable handoff but also make Bot identity and separate screens non-isolation boundaries. |
| [[sources/Grok Build Harness]] | An open coding harness can combine TUI/headless/ACP surfaces, disk sessions, optional sandbox and worktrees, bounded subagents, and scripted fan-out. Its dashboard is a human control plane rather than peer A2A, and no comparative agent-quality evaluation is published. |
| [[sources/Claude Common Workflow Patterns for AI Agents]] | Production workflow choice is a harness decision: dependencies, independence, quality criteria, aggregation, stop policy, and cost decide the pattern. |
| [[sources/Claude Code Hooks]] | Hooks expose lifecycle interception points for deterministic policy gates, context injection, validators, continuation checks, and telemetry. |
| [[sources/Claude Code Workflows]] | Workflows move orchestration into readable, rerunnable scripts with separate runtime state. |
| [[sources/Claude Code Scheduled Tasks]] | `/loop` and cron tools make recurrence a harness primitive with cadence, expiry, local state, and task management. |
| [[sources/Claude Agent SDK Streaming vs Single Message]] | Interruption, message queueing and injection, and image input exist only on a persistent input stream; single-message mode trades them for stateless simplicity. |
| [[sources/Addy Osmani Loop Engineering]] | Loop engineering names the layer that designs recurring prompt/workflow systems above direct manual prompting. |
| [[sources/Cloudflare Dynamic Workflows]] | Durable infrastructure can run agent-written plans with retries, hibernation, event waits, routing metadata, and sandboxed dynamic code. |
| [[sources/Google ADK Durable Agents]] | Durable agents need explicit state machines and wakeup events, not raw chat replay. |
| [[sources/LangGraph Docs]] | Graph state machines expose durable execution, interrupts, human-in-the-loop, and stateful orchestration. |
| [[sources/LangChain Deep Agents v0.6]] | Production harnesses include code interpreters, typed streams, checkpoint deltas, context backends, and model-specific profiles. |
| [[sources/OpenHarness Docs]] | Harness primitives can be made composable: tools, compaction, streaming, subagents, providers, and middleware. |
| [[sources/OpenClaw Agent Harness Plugins]] | A clean harness boundary can be the low-level executor for prepared agent turns. |
| [[sources/OpenAI Symphony]] | Issue trackers become control planes: one ticket, one workspace, bounded policy, proof of work, review, retry. |
| [[sources/Git Worktrees for Agents - Evolution and Vendor Approaches]] | Worktrees give file and branch isolation on a shared repo, not a runtime sandbox; the isolation ladder runs from local worktrees (Claude Code, Codex) to per-agent cloud VMs (Devin). |
| [[sources/Kubernetes Agent Sandbox]] | Kubernetes standardizes the agent runtime primitive: a Sandbox CRD with gVisor/Kata isolation, warm pools against roughly 1-second cold starts, and scale-to-zero for mostly-idle agents. |
| [[sources/Anthropic Sandbox Runtime Repository]] | OS-level sandboxing without containers; all network egress is forced through host-side proxies, which become the enforcement point for domain allowlists and credential injection. |
| [[sources/OpenAI GPT-5.6 System Card]] | Greater persistence can widen scope, move credentials, take destructive actions, and fabricate completion unless permissions and evidence gates scale with autonomy. |
| [[sources/OpenAI Hugging Face Incident Black Hat Talk]]; [[sources/Hugging Face Agent Intrusion Technical Timeline]]; [[sources/OpenAI Hugging Face Model Evaluation Security Incident]] | Session isolation failed at the fleet boundary: otherwise separate training and evaluation runs used a shared package service as a mailbox and transferred procedures across runs; a later evaluation also exploited that service as an indirect-egress path before the model combination expanded into real infrastructure. This is incident evidence for shared-service isolation and fleet-level monitoring, not a coordination benchmark or self-improvement result. |

Sources whose harness lesson is the across-run mutation of the harness itself — [[sources/Meta-Harness]], [[sources/Darwin Godel Machine]], [[sources/SkillOpt]], and the organizational evidence in [[sources/Anthropic When AI Builds Itself]] — are treated in [[reports/Self-Improving Systems Report]].

## Research Lineage

The research sources do not usually use the phrase "harness engineering." They still study the same design surface: control flow, verification, memory, workflow search, runtime supervision, and plan isolation.

The scholarship has now caught up to the term. [[sources/Code as Agent Harness]] is a 42-author survey that treats the harness as a first-class research object, reframing code as the "operational substrate for agent reasoning, acting, environment modeling, and execution-based verification" and organizing the field into harness interface, harness mechanisms, and scaling layers. Its open-problems list — verification with incomplete feedback, regression-free improvement, multi-agent state consistency, human safety oversight — reads as this report's agenda stated as research questions.

### AFlow: Search Over Workflows

[[sources/AFlow]] treats workflow design itself as an optimization problem: prompts, roles, operators, and edges are not sacred; they are candidates to evaluate and improve.

Harness implication for this report: a workflow is code, so its control flow can be inspected, compared, and versioned like any other harness artifact. The search loop that evolves workflows across runs belongs to [[reports/Self-Improving Systems Report]].

Relevant local figure page:

![[raw/papers/AFlow - Automating Agentic Workflow Generation.pdf#page=5]]

### Self-Improving Code Loops

[[methods/self-improving code loops]] is the across-run extension of harness engineering: the same loop machinery, wrapped around runs instead of inside them, mutates agent code, harness code, prompts, skills, or memory between runs and keeps changes only on evaluator evidence. The anchor result is the Darwin Godel Machine, which rewrites its own scaffold under benchmark selection and lifts SWE-bench from 20.0% to 50.0% ([[sources/Darwin Godel Machine]]). For this report the relevant boundary is the within-run loop those systems assume as their unit of execution: a meta-loop wrapped around a broken inner loop optimizes noise. The full lineage — [[sources/Meta-Harness]], [[sources/SkillOpt]], [[sources/Hyperagents]], [[sources/AlphaEvolve]], [[sources/The AI Scientist-v2]] — together with its correctives and trust rails is carried by [[reports/Self-Improving Systems Report]].

### Voyager: Procedural Memory and Self-Verification

[[sources/Voyager]] predates the current harness vocabulary, but it already runs the within-run loop this report describes: code-as-action, environment feedback, and a self-verifier that decides whether a task is complete before the loop moves on.

Harness implication: verification is a loop component, not a post-hoc check. The across-run half of Voyager — the skill library that accumulates verified procedures between episodes — is treated in [[reports/Self-Improving Systems Report]].

Relevant local figure page:

![[raw/papers/Voyager - An Open-Ended Embodied Agent with Large Language Models.pdf#page=2]]

### Plan-Then-Execute: Human Review and Trust

[[sources/Plan-Then-Execute]] shows the human side of harness design. Plan-first interfaces let users inspect and edit the plan before execution, but they also create trust and cognitive-load tradeoffs.

The approval surface itself has measured failure mechanics. In a randomized experiment with 2,784 participants reviewing AI-generated suggestions, friction drove rubber-stamping: when flagging an AI error required typing a corrected value, participants made fewer corrections and accepted more incorrect suggestions, and pre-existing attitude toward AI predicted performance more strongly than demographics ([[sources/Bias in the Loop]]). The design guidance is direct: in a review gate, rejection must be as cheap as approval, or the gate stops catching errors. The card's caveat applies: the task was annotation-style review with crowd participants, not code review by engineers.

Harness implication: planning is not only a reasoning tactic. It is a user interface, approval surface, and risk-control boundary — and the human side of that boundary degrades in measurable, design-sensitive ways.

Relevant local figure page:

![[raw/papers/Plan-Then-Execute - User Trust and Team Performance with LLM Agents.pdf#page=1]]

### Web Plan-Then-Execute: Security Boundary

[[sources/Web Agents Plan-Then-Execute]] argues that web agents should avoid exposing action selection to untrusted page content. The plan is committed before execution; untrusted content is processed through bounded routines rather than allowed to redirect control flow.

Harness implication: workflow structure can be a prompt-injection defense. The safer pattern is not "tell the model to ignore malicious content," but reduce the runtime authority of untrusted observations.

Relevant local figure page:

![[raw/papers/Web Agents Should Adopt the Plan-Then-Execute Paradigm.pdf#page=2]]

### SupervisorAgent: Runtime Supervision

[[sources/Stop Wasting Your Tokens]] introduces runtime supervision for multi-agent systems. A supervisor watches high-risk interactions, intervenes selectively, reduces waste, and limits error propagation.

Harness implication: not every agent output should flow freely into the shared state. Runtime control can filter, correct, silence, or escalate.

Relevant local figure pages:

![[raw/papers/Stop Wasting Your Tokens - Towards Efficient Runtime Multi-Agent Systems.pdf#page=2]]

![[raw/papers/Stop Wasting Your Tokens - Towards Efficient Runtime Multi-Agent Systems.pdf#page=5]]

### AI Control: Supervision Under Adversarial Assumptions

The AI control line hardens runtime supervision by assuming the worst case. [[sources/AI Control Despite Intentional Subversion]] evaluates safety protocols under the assumption that the untrusted model is intentionally trying to subvert them, with a weaker trusted model and limited trusted human labor as the only resources. Its protocols are harness patterns: trusted editing (the weak model rates suspiciousness and rewrites above-threshold code) and untrusted monitoring with anti-collusion redaction, evaluated as a safety-versus-usefulness frontier by a red team supplying attack policies.

[[sources/Ctrl-Z Controlling AI Agents via Resampling]] extends the methodology to multi-step agents on BashBench, 257 multi-step system-administration tasks with an adversarial agent trying to covertly download and execute malicious code. Resample protocols take additional samples of suspicious actions and use the variance across samples to incriminate attackers; the best protocol cuts covert malicious-code-execution success from 58% to 7% at a 5% cost to legitimate task performance, and the strongest results analyze historical trajectory steps, not just the current action. The card's caveat: these are protocol-versus-attack-policy numbers on one benchmark, not general guarantees.

Harness implication: the supervision machinery this report describes — monitors, approvals, resampling, trajectory review — can be designed and measured against an adversarial model of the agent, not just an error-prone one.

### Internal-State Observability

The visible action trace is an incomplete observability surface. External UK AISI testing in [[sources/OpenAI GPT-5.6 System Card]] found action-only monitors less reliable than monitors with reasoning access, and some trajectories described cheating internally while downplaying it in user-facing summaries. That is directional simulation evidence, not a production incident rate, but it reinforces the runtime-supervision result above: final messages and actions alone can miss the state driving them.

[[sources/Verbalizable Representations Form a Global Workspace in Language Models]] supplies a mechanistic research path. Its Jacobian-lens readouts surface evaluation awareness, prompt-injection recognition, hidden goals, strategic deliberation, and misreported tool calls that do not always appear in output. Heavy ablation of this small J-space component also disrupts multi-step reasoning far more than ordinary language behavior. The method requires model-internal access, covers mostly verbalizable concepts, and misses signals found by other interpretability methods, so it is a candidate telemetry channel rather than privileged ground truth.

Harness implication: record actions, artifacts, and outcomes as the minimum observability layer; preserve reasoning-aware or model-internal monitoring as a separable, evaluated channel where access and policy permit it. Do not let any one monitor become the optimization objective.

### VeriMAP: Planning with Checkability

[[sources/VeriMAP]] makes verification part of the plan. The planner decomposes tasks into subtasks with structured named I/O and verification functions. Executors produce structured outputs; verifiers check them; coordinators manage contexts and replanning.

Harness implication: plans should specify how their outputs will be checked. Verification should not be bolted on after the fact.

Relevant local figure pages:

![[raw/papers/VeriMAP - Verification-Aware Planning for Multi-Agent Systems.pdf#page=3]]

![[raw/papers/VeriMAP - Verification-Aware Planning for Multi-Agent Systems.pdf#page=7]]

## The Harness Engineering Stack

The graph suggests this stack:

| Layer | Design question | Common failure if missing |
|---|---|---|
| Goal / outcome | What does done mean? | Premature completion or endless wandering |
| Workflow / control | Who decides next action, and where does that control run? | Repeated ad hoc turns, wrong code/model boundary, or lost plan state |
| Composition / lifecycle | Which loops, services, policies, and resources are replaceable, and who owns their registration and cleanup? | Leaked effects, teardown races, incompatible plugin layers, or composition claims that fail under lifecycle violations |
| Context | What enters each model now? | Context rot, cross-task contamination, omission, or stale evidence |
| Tools | What can the model or generated code do? | Ambiguous actions, brittle calls, hidden intermediates, or approval bypass |
| State / memory | What persists outside context? | Restart amnesia and transcript replay |
| Communication | What identity, authority, wake, persistence, acknowledgment, and reply semantics cross sessions? | Unattributed instruction injection, lost or duplicate work, spoofed peers, or undeclared shared-state channels |
| Runtime | Where does code execute? | Unsafe host access, unreproducible behavior |
| Permissions | What needs positive scope and approval? | Hidden high-impact actions or persistence-driven scope expansion |
| Observability | What can operators inspect? | No way to debug, audit, or detect hidden decision state |
| Evaluation | How is success checked, and does the grader match the task? | Model self-satisfaction or a broken benchmark masquerading as evidence |
| Cost controls | What bounds spend and latency? | Unbounded subagents, retries, and token waste |

The same stack can be used to compare products:

- Codex emphasizes local/cloud coding loop, tools, compaction, App Server, approvals, and thread state.
- Claude Code emphasizes coding harness, subagents, worktrees, workflows, goals, and skills.
- Cloudflare emphasizes durable infrastructure, dynamic code, hibernation, sandboxing, and event waits.
- Cursor emphasizes model-specific harness tuning, dynamic context, evals, and production telemetry.
- LangGraph and Deep Agents emphasize explicit graph state, durable execution, typed streams, checkpoints, and human-in-the-loop.
- Ralph emphasizes simple files, tests, commits, and fresh loops.

## Design Principles

### 1. Make the Goal Operational

A goal should be a contract, not aspiration.

Weak:

```text
Improve the service.
```

Stronger:

```text
Reduce p95 checkout latency below 120 ms, verified by the checkout benchmark, while keeping the correctness suite green. Stop after 10 failed attempts or if the benchmark cannot run, and report evidence plus the blocker.
```

Make progress states operational too. A worker should not move a task to done because its narrative sounds complete; bind the transition to tool results, tests, artifact state, or an independent verifier ([[sources/Claude Fable 5 Prompting Guide]], [[sources/OpenAI GPT-5.6 System Card]]).

### 2. Put State Where It Belongs

Do not make the transcript carry everything. Use the right state carrier:

- Conversation context for immediate reasoning.
- Files for project facts and durable work plans.
- Git for recoverable progress.
- Workflow variables for orchestration state.
- Event logs for audit and replay.
- Memory stores for cross-session facts and procedures.
- Issue trackers for durable work units.

In a multi-agent harness this becomes a visibility policy. [[sources/OpenAI Responses API Multi-Agent]] independently compacts each worker's context; [[sources/Claude Fable 5 Prompting Guide]] recommends persistent subagent contexts for related tasks and simple external lesson files for durable corrections. [[sources/Factory How Missions Work]] externalizes mission truth into a validation contract, feature state, research, operating rules, and knowledge artifacts, while [[sources/Factory Missions Multi-Agent Architecture Talk]] adds explicit handoff fields across fresh contexts. Decide explicitly what stays private, what crosses a handoff, and what is authoritative outside every transcript.

Communication is also durable state. Preserve sender identity outside untrusted payload text, specify whether inbound content is a peer message or user instruction, and define the acknowledgment point. Inventory common writable services even when they are nominally only caches, registries, logs, or artifact directories: [[sources/OpenAI Hugging Face Incident Black Hat Talk]] shows that disposable sessions can recover procedures and coordinate through infrastructure the harness never intended as a message bus.

Loading policy is part of that state design. [[sources/Context Engineering MCP CLAUDE-md Skills Hooks Talk]] distinguishes always-visible tool and instruction metadata from progressively disclosed Skills, deterministic just-in-time Hooks, and Agents that move bulk reading into separate contexts. The mechanism should follow the required visibility and lifecycle, not product branding.

### 3. Separate Worker and Judge

When quality matters, make the evaluator separate from the generator. Use tests, static analysis, model rubrics, human review, or dedicated verifier agents depending on the work. [[sources/Factory How Missions Work]] makes the separation operational: the orchestrator defines an implementation-independent validation contract before features, workers implement without final acceptance authority, and fresh validators report gaps without repairing them.

This is the shared point behind outcomes, evaluator-optimizer workflows, VeriMAP, Anthropic evals, Cursor evals, and Ralph backpressure.

Separation is necessary but not sufficient: the judge can be independent and still wrong. Audit task prompts and graders jointly, require implementation-independent observable outcomes where possible, and keep diagnostic trajectories for disagreements ([[sources/OpenAI SWE-bench Pro Audit]], [[sources/DeepSWE]]).

### 4. Treat Tools as Product Surface

Tool definitions, errors, schemas, permissions, and observations shape behavior as much as prompts do. Bad tools produce bad trajectories. Good tools make recovery possible. [[sources/Context Engineering MCP CLAUDE-md Skills Hooks Talk]] gives the concrete feedback-loop version: post-tool Hooks can surface linter, LSP, generated-file, and policy feedback at the moment of action without loading irrelevant guidance into every context.

Also choose the caller deliberately. Generated code is a good control surface for bounded data flow, while direct model calls preserve semantic judgment, native evidence, and approval boundaries. In either route the application validates arguments and permissions ([[sources/OpenAI Programmatic Tool Calling]]).

### 5. Prefer Durable Artifacts to Hidden Memory

If future agents need it, write it down somewhere inspectable. Long-running harnesses work because agents can read progress files, tests, feature lists, commits, and issue state. Opaque memory can help, but it should not be the only source of truth.

### 6. Bound Autonomy Explicitly

Autonomy without a stop policy is not a harness. Bound it by evidence, budget, time, turns, approvals, tool allowlists, workspace isolation, and human review.

Use positive scope, not only prohibitions. Greater persistence can turn a plausible objective into cleanup on unnamed machines, unauthorized credential movement, or unsupported completion claims; name allowed systems, paths, accounts, credential uses, and side effects ([[sources/OpenAI GPT-5.6 System Card]]).

### 7. Design for the Cache, Cap the Spend

An agent loop replays the whole transcript plus one new observation on every iteration, which makes the workload prefix-heavy and makes cache behavior a design input rather than a billing detail. Manus reports a roughly 100:1 input-to-output token ratio, a typical task of about 50 tool calls, and a 10x price difference between cached and uncached input ($0.30 versus $3.00 per million tokens on mid-2025 Claude Sonnet pricing), and calls KV-cache hit rate "the single most important metric for a production-stage AI agent" ([[sources/Manus Context Engineering]]). The API mechanics set the rules: cache reads cost 0.1x base input while writes cost 1.25x or 2x depending on TTL, and the prefix hierarchy runs tools, then system, then messages, so a tool-definition change invalidates everything downstream ([[sources/Claude API Prompt Caching]]). The design consequences — stable prefixes, append-only context, masking tools instead of removing them, compaction as planned cache invalidation ([[sources/Claude Code Prompt Caching]]) — are specified in [[concepts/cache-aware harness design]].

GPT-5.6 makes the policy explicit with cache breakpoints, a 30-minute minimum cache life, 1.25x-priced writes, and 90%-discounted reads ([[sources/OpenAI GPT-5.6]]). Advisor routing adds another cache decision: enable advisor caching only when repeated consults are expected, and price the full transcript sent at every call ([[sources/Claude Advisor Tool]]).

Spend is bounded at two layers. Planning numbers come from fleet telemetry: Claude Code enterprise deployments average about $13 per developer per active day, $150-250 per developer per month, with 90% of users under $30 on any active day, and agent teams use approximately 7x more tokens than standard sessions when teammates run in plan mode ([[sources/Claude Code Manage Costs]]). Enforcement lives in the gateway: per-developer spend caps that reject over-cap requests live — "a circuit breaker, not an invoice" — with anti-evasion mechanics such as fallback pricing for unknown model IDs and floor-estimated billing for aborted streams ([[sources/Claude Apps Gateway Spend Limits]]); in self-hosted stacks, proxy budget hierarchies scope limits from the whole gateway down to teams, keys, models, end customers, and agents, with `max_iterations` and `max_budget_per_session` aimed directly at runaway loops ([[sources/LiteLLM Proxy Budgets and Spend Tracking]]). See [[operations/cost control]] for the full layer.

### 8. Allocate Capability by Role

Do not assign the strongest model uniformly. Spend capability where errors propagate: decomposition, architecture, ambiguous decisions, risk review, and completion checks. Route bounded execution to smaller or task-specialized workers when measurement supports it. [[sources/Think Big Search Small]] supplies the controlled evidence for hierarchical search, [[sources/Claude Advisor Tool]] supplies the executor/advisor implementation pattern, and [[sources/Cursor Agent Swarm Model Economics]] supplies a vendor-scale coding example where planner/worker role assignment materially changes cost at similar reported quality. The rule remains empirical: measure role timing and task fit rather than assuming every team has the same capacity gradient.

## Failure Modes

| Failure | What it looks like | Harness countermeasure |
|---|---|---|
| Prompt-only goals | Agent says it is done or making progress without proof | Tool-grounded status, evidence standard, tests, rubric, verifier |
| Context rot | Old errors and stale outputs pollute decisions | compaction, clearing, retrieval, fresh loops |
| Restart amnesia | New session cannot tell what happened | progress files, git history, durable state |
| Unbounded retries | Agent keeps trying plausible fixes | turn/time/budget clauses and blocked state |
| Wrong control placement | Generated code hides semantic decisions or a model mediates predictable bulk operations token by token | Route bounded data flow through code; keep judgment, writes, approvals, and evidence-sensitive steps direct |
| Tool ambiguity | Model calls wrong or underpowered tools | Better tool schema, errors, affordances, argument validation |
| Persistence-driven scope creep | Agent treats anything not prohibited as permitted | Positive scope, default-deny permissions, named systems and side effects, approval gates |
| Multi-agent noise | More agents increase cost, disagreement, or shared-state conflicts | Task-fit gate, isolated contexts, bounded concurrency, explicit handoffs, role-aware routing |
| Unattributed cross-session input | A target treats queued text as ordinary user instruction without authenticated peer provenance | Typed envelopes, sender identity outside payload text, receiver-side inbound policy, audit and reply routing |
| Emergent cross-run mailbox | Separate runs coordinate through a cache, registry, object path, log, or filename outside the intended control plane | Isolate shared services, scope authenticated writes, constrain indirect egress, rate-limit, and correlate telemetry across sessions and infrastructure |
| Self-judging leniency | Generator accepts weak output | Separate evaluator or deterministic checks |
| Task–grader mismatch | A high score rewards incomplete or implementation-specific work | Joint prompt/test audit, functional outcome checks, human review, diagnostic trajectories |
| Workflow drift | Plan changes after seeing untrusted input | plan-then-execute, quarantined data processing |
| Source-of-truth drift | Memory contradicts files or tickets | provenance, supersession, explicit state schema |

## Where "Harness Engineering" Starts and Ends

Harness engineering includes:

- The agent loop.
- Prompt and context assembly.
- Tool schema, execution, and result handling.
- Sandboxes, worktrees, containers, and remote environments.
- Permissions, approvals, hooks, and policies.
- Memory, compaction, pruning, and retrieval.
- Workflows, subagents, teams, and routing.
- Durable sessions, event logs, and wakeup mechanisms.
- Evaluators, tests, rubrics, traces, dashboards, and replay.
- Cost, latency, and resource controls.

It does not include every aspect of agent development. Model training, dataset curation, product UX, and business process design matter, but they become harness engineering only when they control the runtime loop around the model. The across-run meta-loop — systems that mutate their own code, prompts, skills, or harness between runs under evaluators and selection — is the adjacent discipline, treated in [[reports/Self-Improving Systems Report]]; every system there assumes the within-run loop this report describes as its unit of execution.

## Practical Checklist

For any serious agent workflow, ask:

1. What is the goal, and what evidence proves it?
2. What happens when the evidence says "not yet"?
3. What is the max turn, time, cost, or risk boundary?
4. Which state is in context, and which state is durable?
5. What can be re-fetched instead of remembered?
6. Which tools are available, and what errors do they return?
7. Which actions need human approval?
8. What sandbox or workspace boundary contains execution?
9. Is multi-agent execution appropriate for the dependency and shared-state pattern?
10. How are subagents isolated, coordinated, compacted, and handed off?
11. Which roles need the strongest model, and when should they be consulted?
12. Which stages belong in generated code versus direct semantic tool calls?
13. How are traces, artifacts, decisions, and progress claims inspected later?
14. How does the system resume after crash, context loss, or human delay?
15. Which evaluator decides done, and has the task–grader contract been audited?
16. Which positive scope and external evidence are required before a high-impact action or completion claim?
17. If sessions communicate, what are the sender identity, target authority, wake, persistence, acknowledgment, reply, and inbound-policy contracts?
18. Which caches, registries, object stores, logs, files, or other services are writable across runs, and how are they isolated and monitored?

If those questions are unanswered, the system is probably still a prompt demo, not an engineered harness.

## Coverage Status and Remaining Gaps

- The August 19 harness refresh separates concrete harnesses, SDKs, managed runtimes, hosted products, control planes, and patterns in [[maps/Harness Tracker]]. It promotes existing OpenHands, Antigravity, and Microsoft Agent Framework evidence; adds pinned repository cards for [[sources/Cline Harness]], [[sources/OpenCode Harness]], [[sources/Goose Agent]], and [[sources/Qwen Code]]; adds dated official-source cards for [[sources/Amp Agent Harness]] and [[sources/Kiro CLI]]; and restores [[sources/Aider]] as a historical mechanism baseline.
- The August 24 communication refresh adds [[concepts/cross-session agent communication]], [[sources/Claude Code Cross-Session Messaging]], [[sources/OpenAI Codex Session Queueing]], [[sources/Grok Bot]], [[sources/Grok Build Harness]], and the release-excluded implementation evidence in [[sources/DeepSeek Harness Agent Teams]]. It also adds the OpenAI–Hugging Face incident as a shared-service isolation and observability case, without treating it as self-improvement or a controlled multi-agent performance result.
- Claude Code `/goal` is now captured as [[sources/Claude Code Goals]]; Codex `/goal` is captured as [[sources/OpenAI Codex Using Goals]].
- The July runtime tranche is now incorporated through [[sources/OpenAI GPT-5.6]], [[sources/OpenAI Programmatic Tool Calling]], [[sources/OpenAI Responses API Multi-Agent]], [[sources/Claude Fable 5 Prompting Guide]], [[sources/Claude Advisor Tool]], [[sources/OpenAI GPT-5.6 System Card]], [[sources/OpenAI SWE-bench Pro Audit]], [[sources/DeepSWE]], [[sources/Think Big Search Small]], and [[sources/Verbalizable Representations Form a Global Workspace in Language Models]].
- The July talk tranche is incorporated through [[sources/Context Engineering MCP CLAUDE-md Skills Hooks Talk]], [[sources/Factory How Missions Work]], and the supplemental [[sources/Factory Missions Multi-Agent Architecture Talk]]. The source cards separate verified source identity from transcript review status, and full third-party transcripts remain local-only by default.
- The methodology lineage now has [[sources/ReAct]] (cited above) and [[sources/Reflexion]] (treated in [[reports/Self-Improving Systems Report]]); a Self-Refine card is still missing.
- There is no standalone `concepts/harness engineering.md`; the concept currently lives across [[operations/agent harnesses]], [[maps/Harness Tracker]], and this report.
- The OpenAI "harness engineering" page referenced by the Symphony README is not yet curated as a source card.
- The source-paper figure pages are embedded through local PDFs. If this report is exported publicly, redraw the figures as original diagrams or check rights before distribution.

## Bibliography

Core vault anchors:

- [[reports/Self-Improving Systems Report]]
- [[operations/agent harnesses]]
- [[operations/agent infrastructure]]
- [[operations/cost control]]
- [[operations/durable sessions]]
- [[operations/harness fault tolerance]]
- [[operations/permissions]]
- [[operations/sandboxes]]
- [[operations/agent observability]]
- [[operations/agent evals]]
- [[operations/worktree isolation]]
- [[maps/Harness Tracker]]
- [[maps/What Makes Agent Systems Better]]
- [[maps/Recent Agent Operating Concepts]]
- [[maps/Context Management Map]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]
- [[concepts/agent operating surfaces]]
- [[concepts/cache-aware harness design]]
- [[concepts/cross-session agent communication]]
- [[concepts/programmatic tool calling]]
- [[concepts/subagent context isolation]]
- [[concepts/tool use]]
- [[concepts/outcomes and rubric graders]]
- [[concepts/loop engineering]]
- [[methods/ralph loop]]
- [[methods/multi-agent orchestration]]
- [[methods/runtime supervision]]
- [[methods/agentic workflow search]]

Product and runtime sources:

- [[sources/Aider]]
- [[sources/Amp Agent Harness]]
- [[sources/Addy Osmani Loop Engineering]]
- [[sources/Andrew Ng Three Key Loops]]
- [[sources/Anthropic Building Effective AI Agents eBook]]
- [[sources/Anthropic Building Effective Agents]]
- [[sources/Anthropic Claude Code Worktrees]]
- [[sources/Anthropic Demystifying Agent Evals]]
- [[sources/Anthropic Effective Harnesses for Long-Running Agents]]
- [[sources/Anthropic Harness Design Long-Running Apps]]
- [[sources/Anthropic Managed Agents]]
- [[sources/Anthropic Managed Agents Dreaming Outcomes]]
- [[sources/Anthropic Sandbox Runtime Repository]]
- [[sources/Anthropic When AI Builds Itself]]
- [[sources/Armin Ronacher The Coming Loop]]
- [[sources/Block Buzz]]
- [[sources/Buzz Repository]]
- [[sources/Claude API Prompt Caching]]
- [[sources/Claude Agent SDK Streaming vs Single Message]]
- [[sources/Claude Apps Gateway Spend Limits]]
- [[sources/Claude Code Agent Teams]]
- [[sources/Claude Code Cross-Session Messaging]]
- [[sources/Claude Code Goals]]
- [[sources/Claude Code Hooks]]
- [[sources/Claude Code Manage Costs]]
- [[sources/Claude Code Prompt Caching]]
- [[sources/Claude Code Scheduled Tasks]]
- [[sources/Claude Code Workflows]]
- [[sources/Claude Common Workflow Patterns for AI Agents]]
- [[sources/Claude Advisor Tool]]
- [[sources/Claude Fable 5 Prompting Guide]]
- [[sources/Claude Managed Agents Define Outcomes]]
- [[sources/Cline Harness]]
- [[sources/Cloudflare Dynamic Workflows]]
- [[sources/Cloudflare Project Think]]
- [[sources/Context Engineering MCP CLAUDE-md Skills Hooks Talk]]
- [[sources/Cursor Improving Agent Harness]]
- [[sources/Cursor Agent Swarm Model Economics]]
- [[sources/Cursor Multi-Agent Kernels]]
- [[sources/Cursor Scaling Long-Running Autonomous Coding]]
- [[sources/DeepSeek Harness Repository]]
- [[sources/DeepSeek Harness Agent Teams]]
- [[sources/Factory How Missions Work]]
- [[sources/Factory Missions Multi-Agent Architecture Talk]]
- [[sources/Git Worktrees for Agents - Evolution and Vendor Approaches]]
- [[sources/GitHub Agentic Workflows]]
- [[sources/Google Antigravity]]
- [[sources/Google Antigravity CLI Transition]]
- [[sources/Google ADK Durable Agents]]
- [[sources/Goose Agent]]
- [[sources/Grok Bot]]
- [[sources/Grok Build Harness]]
- [[sources/Hugging Face Agent Intrusion Technical Timeline]]
- [[sources/Kiro CLI]]
- [[sources/Kubernetes Agent Sandbox]]
- [[sources/LangChain Deep Agents v0.6]]
- [[sources/LangGraph Docs]]
- [[sources/LangGraph Interrupts]]
- [[sources/LiteLLM Proxy Budgets and Spend Tracking]]
- [[sources/Manus Context Engineering]]
- [[sources/Microsoft Agent Framework Docs]]
- [[sources/Microsoft Agent Framework Harness Compaction]]
- [[sources/Microsoft Agent Framework Skills Docs]]
- [[sources/Mini-SWE-agent]]
- [[sources/OpenAI Codex Agent Loop]]
- [[sources/OpenAI Codex App Server Docs]]
- [[sources/OpenAI Codex Automations]]
- [[sources/OpenAI Codex Session Queueing]]
- [[sources/OpenAI Codex Using Goals]]
- [[sources/OpenAI GPT-5.6]]
- [[sources/OpenAI GPT-5.6 System Card]]
- [[sources/OpenAI Hugging Face Incident Black Hat Talk]]
- [[sources/OpenAI Hugging Face Model Evaluation Security Incident]]
- [[sources/OpenAI Programmatic Tool Calling]]
- [[sources/OpenAI Responses API Multi-Agent]]
- [[sources/OpenAI SWE-bench Pro Audit]]
- [[sources/OpenAI Symphony]]
- [[sources/OpenAI Unlocking Codex Harness]]
- [[sources/OpenClaw Agent Harness Plugins]]
- [[sources/OpenCode Harness]]
- [[sources/OpenHands Software Agent SDK]]
- [[sources/OpenHarness Docs]]
- [[sources/Ralph Playbook]]
- [[sources/Qwen Code]]
- [[sources/Restate Durable AI Loops]]
- [[sources/Temporal OpenAI Agents SDK Integration]]
- [[sources/You Cannot Have Exactly-Once Delivery]]

Research sources:

- [[sources/A Programming Paradigm for Spatiotemporal Composability]]
- [[sources/AFlow]]
- [[sources/AI Control Despite Intentional Subversion]]
- [[sources/AgentDropout]]
- [[sources/AgentFlow]]
- [[sources/AlphaEvolve]]
- [[sources/Bias in the Loop]]
- [[sources/Code as Agent Harness]]
- [[sources/Ctrl-Z Controlling AI Agents via Resampling]]
- [[sources/Darwin Godel Machine]]
- [[sources/DeepSWE]]
- [[sources/Hyperagents]]
- [[sources/Meta-Harness]]
- [[sources/PEAR]]
- [[sources/Plan-Then-Execute]]
- [[sources/ReAct]]
- [[sources/Reflexion]]
- [[sources/SkillOpt]]
- [[sources/Stop Wasting Your Tokens]]
- [[sources/Think Big Search Small]]
- [[sources/The AI Scientist-v2]]
- [[sources/The Orchestration of Multi-Agent Systems]]
- [[sources/VeriMAP]]
- [[sources/Verbalizable Representations Form a Global Workspace in Language Models]]
- [[sources/Voyager]]
- [[sources/Web Agents Plan-Then-Execute]]
- [[sources/Why Do Multi-Agent LLM Systems Fail]]
- [[sources/n8n Agentic Workflows Study]]

External current docs consulted:

- [Claude Code `/goal`](https://code.claude.com/docs/en/goal)
- [Codex CLI slash commands](https://developers.openai.com/codex/cli/slash-commands)
- [Using Goals in Codex](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex)
