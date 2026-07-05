Title: Session event stream

URL Source: https://platform.claude.com/docs/en/managed-agents/events-and-streaming

Markdown Content:
Managed Agents Delegate work to your agent

Send events, stream responses, and interrupt or redirect your session mid-execution.

Communication with Claude Managed Agents is event-based. You send user events to the agent, and receive agent and session events back to track status.

All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.

## Event types

Events flow in two directions.

*   **User events** and **system events** are what you send to the agent: `user.*` events kick off a session and steer it as it progresses; `system.message` updates the agent's system prompt between turns.
*   **Session events**, **span events**, and **agent events** are sent to you for observability into your session state and agent progress. Stream connections that opt in also receive [event deltas](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#event-deltas).

Session, span, agent, user, and system event type strings follow a `{domain}.{action}` naming convention. The stream-only delta preview events (`event_start`, `event_delta`) are the exception. See [Event types](https://platform.claude.com/docs/en/managed-agents/reference#event-types) in the reference for the full catalog.

Every persisted event includes a `processed_at` timestamp indicating when the event was recorded server-side. If `processed_at` is null, it means the event has been queued by the harness and is handled after preceding events finish processing.

## Integrating events

Send a `user.message` event to start or continue the agent's work:

Send a `user.interrupt` event to stop the agent mid-execution, then follow up with a `user.message` event to redirect it:

The agent acknowledges the interruption and switches to the new task.

## Event deltas

By default, the agent's response text reaches the stream as buffered `agent.message` events, each emitted only after the model request that produced it finishes. Event deltas let you render that text incrementally, as a live preview, while the model is still generating it. A preview is not the response: previews are a best-effort display aid, and the buffered `agent.message` is always the authoritative record. A client that ignores previews still receives a complete, correct stream.

### Opt in to previews

Previews are opt-in per stream connection. Add the `event_deltas[]` query parameter to `GET /v1/sessions/{session_id}/events/stream`, repeating it once for each event type you want previewed. The accepted values are `agent.message` and `agent.thinking`; any other value returns a 400 error. Only the session-level event stream supports the parameter. [Session thread](https://platform.claude.com/docs/en/managed-agents/multi-agent) event streams reject it.

When a previewed event begins, the stream emits an `event_start` carrying the upcoming event's type and `id`:

For `agent.message`, the start is followed by `event_delta` events carrying incremental text. Each delta names the event it extends in `event_id` and the content block it extends in `delta.index`:

When an `agent.thinking` event is previewed, only the `event_start` is emitted. No `event_delta` events follow, and the content arrives in the buffered `agent.thinking` event as usual.

Unlike persisted events, `event_start` and `event_delta` have no `id` or `processed_at` of their own. The only identifier they carry is the `id` of the event they preview.

Event deltas use a different wire format from [Streaming messages](https://platform.claude.com/docs/en/build-with-claude/streaming), and the difference is intentional. A previewed `agent.message` gets a single `event_start` followed only by `event_delta` events. There are no per-content-block start or stop events and no stop event for the previewed event itself. The delta type is `content_delta`, not `content_block_delta`. Accumulator code written for the Messages API does not carry over unchanged.

### Accumulate and reconcile

The Python, TypeScript, and Go SDKs include an accumulator helper that keys the preview by the event's `id` and handles the `index` bookkeeping for you. The manual pattern works in every language: in the other SDKs, apply it to the generated event types.

In the manual pattern, treat the preview as a scratch buffer and the buffered event as the record. Key the buffer by `(event_id, index)`. Reconcile per model request: a turn opens with a single `session.status_running` event, then on a turn that completes normally each model request produces, in order, `span.model_request_start`, `event_start`, the `event_delta` events, the buffered `agent.message`, and finally [`span.model_request_end`](https://platform.claude.com/docs/en/managed-agents/reference#event-types) (in the Span events tab). Process each event as it arrives:

1.   On `event_start`, note the announced `id`. The identifiers always line up: `event_start.event.id`, every `event_delta.event_id`, and the buffered `agent.message`'s `id` are the same value.
2.   On each `event_delta`, append `delta.content.text` to the entry at `(event_id, delta.index)` and render the running text. The first delta for an `index` creates that entry.
3.   When the buffered `agent.message` arrives, match it by `id`, discard the accumulated preview, and render the message's content instead.
4.   On `span.model_request_end`, close any preview that has not been reconciled by its buffered event. No more deltas are coming for it. If the turn errors or is interrupted, the buffered event may never arrive; `span.model_request_end` still does.

### Limitations

Previews are tuned for responsiveness. Build against these constraints:

*   **Best effort:** Under load, the server may shed deltas for an event. When it does, you receive a contiguous prefix of the text and then no further deltas for that event. The buffered `agent.message` still arrives complete. Never treat an accumulated preview as final.
*   **No replay on reconnect:** Deltas are delivered only to the connection that opted in, while it is open. If the stream drops, follow the [reconnect procedure](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#integrating-events) in the Streaming events tab: reopen the stream and list the event history. The history includes any buffered events emitted while you were disconnected, including the `agent.message` your preview was waiting for. There is no way to re-request missed deltas.
*   **Primary thread, text only:** Previews cover assistant text on the session's primary thread. Tool use, tool results, MCP results, and activity on other [session threads](https://platform.claude.com/docs/en/managed-agents/multi-agent) are never previewed.
*   **Start-only `agent.thinking`:** An `agent.thinking` preview emits only the `event_start` as a signal that a thinking block has started; no `event_delta` events follow it.
*   **Never persisted:**`event_start` and `event_delta` exist only on the live stream. They do not appear in the session's event history (`GET /v1/sessions/{session_id}/events`).

## Additional scenarios

### Handling custom tool calls

When the agent invokes a [custom tool](https://platform.claude.com/docs/en/managed-agents/tools#custom-tools):

1.   The session emits an `agent.custom_tool_use` event containing the tool name and input.
2.   The session pauses with a `session.status_idle` event containing `stop_reason: requires_action`. The blocking event IDs are in the `stop_reason.event_ids` array.
3.   Execute the tool in your system and send a `user.custom_tool_result` event for each, passing the event ID in the `custom_tool_use_id` parameter along with the result content.
4.   Once all blocking events are resolved, the session transitions back to `running`.

### Tool confirmation

When a [permission policy](https://platform.claude.com/docs/en/managed-agents/permission-policies) requires confirmation before a tool executes:

1.   The session emits an `agent.tool_use` or `agent.mcp_tool_use` event.
2.   The session pauses with a `session.status_idle` event containing `stop_reason: requires_action`. The blocking event IDs are in the `stop_reason.event_ids` array.
3.   Send a `user.tool_confirmation` event for each, passing the event ID in the `tool_use_id` parameter. Set `result` to `"allow"` or `"deny"`. Use `deny_message` to explain a denial.
4.   Once all blocking events are resolved, the session transitions back to `running`.

### Resuming an idle session

Sessions persist between interactions. Conversation history is preserved unless the session is explicitly deleted. When a session goes idle, its sandbox is checkpointed, preserving the full sandbox state, including the filesystem, installed packages, and any files the agent created. This allows you to resume cleanly from inactivity.

While session history is persisted until deleted, checkpoints are only preserved for 30 days after the session's last activity. If your workflow requires the full sandbox state (files, installed tools, and so on) to persist beyond 30 days, send periodic `user.message` events to reset the inactivity timer before the checkpoint expires.

To resume a session, send a `user.message` event to it as usual:

### Sending system messages

`system.message` is currently only supported by Claude Opus 4.8. If any model configured on the agent does not support mid-conversation system injection, the event is rejected with a `model_does_not_support_mid_conversation_system` validation error.

Send a `system.message` event to update the agent's system prompt between turns. Unlike the `system` field on the agent definition (which is fixed at session creation), `system.message` lets you change the system prompt as the session progresses. Use it when the agent needs updated system-level guidance mid-session: a different persona, revised constraints, or context fetched at runtime that should shape the model's behavior going forward.

`system.message` cannot be sent while the session is idle with `stop_reason: requires_action`. `content` accepts 1–1000 text items.

### Tracking usage

The session object includes a `usage` field with cumulative token statistics. Fetch the session after it goes idle to read the latest totals, and use them to track costs, enforce budgets, or monitor consumption.

`input_tokens` reports uncached input tokens and `output_tokens` reports total output tokens across all model calls in the session. The `cache_creation_input_tokens` and `cache_read_input_tokens` fields reflect prompt caching activity. Cache entries use a 5-minute TTL, so back-to-back turns within that window benefit from cache reads, which reduce per-token cost.

## Console observability

The Console provides a visual timeline view of your agent sessions. Navigate to the Claude Managed Agents section in the Console to see:

*   **Session list:** All sessions with their status, creation time, and model
*   **Tracing view:** A chronological view of events (content, timestamps, token usage) within a session. Tracing views are only accessible to Developers and Admins.
*   **Tool execution:** Details of each tool call and its result

## Debugging tips

*   **Check session events:** Session errors are conveyed through the `session.error` event
*   **Review tool results:** Tool execution failures often explain unexpected agent behavior
*   **Track token usage:** Monitor token consumption to optimize prompts and reduce costs
*   **Use system prompts:** Add logging instructions to the system prompt to make the agent explain its reasoning

Was this page helpful?
