# Codex App Server

Source URLs:

- https://developers.openai.com/codex/app-server
- https://github.com/openai/codex/blob/main/codex-rs/app-server/README.md

Snapshot date: 2026-07-01

## Position

Codex App Server is the local integration surface that exposes the Codex harness to rich clients. It is a long-running process plus a JSON-RPC-like protocol over JSONL. The docs position it as the right surface when a client needs authentication, conversation history, approvals, streamed events, and the full agent loop. The Codex SDK is the higher-level wrapper for simpler programmatic automation.

## Core Primitives

- Thread: durable conversation between a user and the Codex agent. A thread contains turns and can be started, resumed, forked, archived, named, compacted, or deleted.
- Turn: one unit of user-requested work inside a thread. A turn starts from user input and ends when Codex completes, is interrupted, or fails.
- Item: typed unit of input or output inside a turn, such as user messages, agent messages, command execution, tool calls, diffs, approval requests, and progress events.

## Lifecycle

Typical lifecycle:

1. Initialize the app-server connection.
2. Start, resume, or fork a thread.
3. Start a turn with user input against that thread.
4. Stream turn and item notifications while Codex works.
5. Resolve any approval requests from the client.
6. Receive final turn completion.
7. Continue the same thread with another turn, steer an active turn, archive/name the thread, or resume it later.

Important methods:

| App Server method | Role |
|---|---|
| `thread/start` | Open a fresh conversation and return a thread id. |
| `thread/resume` | Continue an existing persisted thread. |
| `thread/fork` | Branch an existing conversation into a new thread id. |
| `turn/start` | Add user input to a target thread and begin Codex work. |
| `turn/steer` | Add input to an active turn without starting a new turn. |
| `turn/interrupt` | Request cancellation of an in-flight turn. |
| `thread/name/set` | Set or update a thread's user-facing name. |
| `thread/archive` / `thread/unarchive` | Move a thread in or out of archived state. |
| `thread/compact/start` | Trigger manual compaction for a thread. |

## Coordinator Pattern

The app-server model makes coordinator/worker thread orchestration possible:

- A coordinator creates worker threads with `thread/start`.
- It relays assignments by starting turns on worker `threadId`s with `turn/start`.
- It can steer an active worker turn with `turn/steer`.
- It organizes workers with thread names, archive state, and status events.
- Worker threads remain durable sessions that can be reopened, inspected, resumed, or moved across worktree/local contexts through the Codex app surface.

The current Codex desktop tool binding exposed inside Codex sessions can map this into tools such as `codex_app.create_thread`, `codex_app.send_message_to_thread`, `codex_app.read_thread`, `codex_app.list_threads`, and thread title/pin/archive operations. Those names are not the public API names; the public primitive is the app-server thread/turn protocol.

## Worktrees and Worker State

App Server controls conversations. Git worktrees isolate file state. For coordinator/worker coding work, use one worker thread per task and usually one Codex-managed worktree per worker. The durable state should not live only in chat history; keep a worker ledger plus branch, worktree, report file, PR, or issue comment.

## Approvals and Safety

When a turn asks to run commands or modify files, app-server can drive client approval flows. Approval requests include the relevant thread and turn ids, so clients can scope the decision to the active worker. Coordinator thread orchestration does not remove the need for sandboxing, permissions, worktree isolation, reviews, and tests.
