# Codex Thread Orchestration

Codex thread orchestration is the pattern of using one Codex thread as a coordinator that manages other top-level Codex threads as durable workers.

The key distinction is that workers are not merely subagents hidden inside one conversation. Each worker is a real thread with its own context, status, and usually its own worktree. The coordinator relays instructions through the thread control plane and aggregates results through explicit artifacts.

## Pattern

```text
coordinator thread
  -> create / find worker threads
  -> assign scoped work by sending turns to worker thread ids
  -> read worker state and reports
  -> steer, stop, archive, or rename workers
  -> aggregate verified outputs

worker thread
  -> owns one scoped task and usually one worktree
  -> may spawn helper subagents for read-heavy investigation or review
  -> reports status, changed files, verification, blockers, and final recommendation
```

## Public Primitives

The public foundation is the Codex App Server thread/turn protocol:

| Primitive | Role in orchestration |
|---|---|
| `thread/start` | Create a new worker conversation. |
| `thread/resume` | Reopen an existing worker by id. |
| `thread/fork` | Branch an existing conversation into a new worker. |
| `turn/start` | Send an assignment or follow-up to a worker thread. |
| `turn/steer` | Add steering input to an active worker turn. |
| `thread/queue/add` | Persist a future user turn in the experimental queue API. |
| `thread/name/set` | Give worker threads readable names. |
| `thread/archive` | Clean up completed or irrelevant worker threads. |

## Keep The Surfaces Separate

Codex now exposes related thread controls through several contracts that should not be collapsed into one generic "agent messaging" feature:

- **Public thread/turn control plane:** an App Server client calls methods such as `thread/start`, `thread/read`, and `turn/start` to operate durable threads.
- **Released session queue:** Codex CLI v0.149 added `codex queue`, which calls experimental `thread/queue/add` to persist a future user turn. The queue is durable, but its record does not identify a sender or supply a reply address.
- **Agent-callable task controls:** current desktop bindings can expose tools such as `create_thread`, `send_message_to_thread`, `read_thread`, and `wait_threads`. A 2026-08-24 main-branch TUI implementation added a similar `codex_tui` namespace, wrapping a source thread ID into delegated prompts. That implementation postdated the latest formal release at this snapshot.

The desktop names and the main-branch TUI names are environment-specific tool bindings, not public App Server method names. Likewise, `codex queue` is not evidence that released Codex sessions have Claude-style named peer messaging.

## Worker Ledger

The coordinator should keep a small ledger rather than relying on memory:

```text
Worker: auth-audit
threadId: ...
scope: auth routes and session middleware
environment: worktree
branch/PR: ...
status: running / blocked / complete
expected output: worker report, diff, tests, risks
last checked: ...
```

Good worker reports include:

- assigned scope
- changed files
- helper subagents used
- tests and commands run
- findings or decisions with file references
- blockers and unresolved risks
- final recommendation

## When To Use

Use this pattern when work decomposes into independent or loosely coupled tasks:

- independent issue backlog items
- codebase-wide audits split by directory or concern
- parallel migration slices
- competing implementation approaches
- review, verification, or test-generation passes that should not pollute the coordinator context

Use ordinary subagents instead when the worker does not need durable user access, separate thread history, or a long-running worktree.

## Operating Rules

- Give each worker a narrow scope and a non-overlapping file boundary when possible.
- Prefer one worktree or branch per write-capable worker.
- Let workers spawn helper subagents for investigation and review, but keep helper outputs summarized inside the worker thread.
- Keep durable state in files, branches, PRs, issues, or a coordinator ledger, not only in chat history.
- Require verification output before aggregation.
- Aggregate in the coordinator; do not let multiple workers merge into the same branch blindly.

## Failure Modes

- Overlapping edits create merge conflicts and incoherent behavior.
- The coordinator can drift if it does not maintain a worker ledger.
- Workers can finish locally but fail to report enough evidence for aggregation.
- Thread fanout can increase token spend, runtime, and approval noise.
- A queued turn has no protocol-level sender identity or reply address, so request-response workflows need an explicit envelope or coordinator ledger.
- Agent-callable task controls are host- and version-dependent; an orchestration design should not assume that a local desktop binding, a released CLI, and the public App Server expose identical behavior.
- Worktrees isolate files and Git state, but not ports, databases, credentials, host processes, or security policy.
- Helper subagents can create extra context and cost inside workers if not bounded.

## Related

- [[sources/OpenAI Codex App Server Docs]]
- [[sources/OpenAI Codex Session Queueing]]
- [[sources/OpenAI Unlocking Codex Harness]]
- [[sources/OpenAI Codex App]]
- [[sources/OpenAI Codex App Worktrees]]
- [[sources/OpenAI Codex Subagents]]
- [[sources/OpenAI Codex Automations]]
- [[methods/multi-agent orchestration]]
- [[operations/worktree isolation]]
- [[operations/agent infrastructure]]
- [[operations/agent observability]]
- [[concepts/agent teams]]
- [[maps/Agent Teams and Workforces Map]]
