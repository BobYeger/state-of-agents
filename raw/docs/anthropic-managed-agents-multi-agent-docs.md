Multi-agent orchestration lets one agent coordinate with others to complete complex work. Agents can act in parallel with their own isolated context, which helps improve output quality and can also improve time to completion.

All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets this beta header automatically.

## How it works

All agents share the same container and filesystem, but each agent runs in its own **session thread**, a context-isolated event stream with its own conversation history. The coordinator reports activity in the **primary thread** (which is the same as the session-level [event stream](https://platform.claude.com/docs/en/managed-agents/events-and-streaming)); additional threads are spawned at runtime when the coordinator decides to delegate.

Threads are persistent: the coordinator can send a follow-up to an agent it called earlier, and that agent retains everything from its previous turns.

Each agent uses its own configuration (model, system prompt, tools, MCP servers, and skills) as defined when that agent was created. Tools and context are not shared.

### What to delegate

Multiagent coordination is best-suited for complex tasks that either require work across a variety of surfaces, or where multiple well-scoped tasks contribute to an overall goal.

Patterns that work well:

- **Parallelization:** Fan out independent subtasks simultaneously (searching multiple sources, analyzing separate files) and have the coordinator synthesize the results.
- **Specialization:** Route to agents with domain-focused system prompts and tools, such as a security agent or a documentation agent, rather than loading a single agent with every capability.
- **Escalation:** Consult a more capable agent / model for a subset of complex subtasks.

## Configure the coordinator

When [defining your agent](https://platform.claude.com/docs/en/managed-agents/agent-setup), set `multiagent` to declare the roster of agents the coordinator can delegate to:

```
ant beta:agents create <<YAML
name: Engineering Lead
model: claude-opus-4-7
system: You coordinate engineering work. Delegate code review to the reviewer agent and test writing to the test agent.
tools:
  - type: agent_toolset_20260401
multiagent:
  type: coordinator
  agents:
    - type: agent
      id: $REVIEWER_AGENT_ID
    - type: agent
      id: $TEST_WRITER_AGENT_ID
YAML
```

`multiagent.agents` can accept any of the following:

- `{"type": "agent", "id": agent.id}` references a previously created `agent` by ID. Defaults to pinning the latest agent version if no `version` is specified.
- `{"type": "agent", "id": agent.id, "version": agent.version}` pins a specific agent version.
- `{"type": "self"}`: allows the coordinator to spawn copies of itself.

The coordinator can only delegate to one level of agents; depth > 1 is ignored. A maximum of 20 unique agents can be listed in `multiagent.agents`, but the coordinator can call multiple copies of each agent.

## Create the session

Create a session referencing the coordinator. The coordinator will delegate to the agents in its roster as needed.

```
session = client.beta.sessions.create(
    agent=coordinator.id,
    environment_id=environment.id,
)
```

## Threads

The **session-level event stream** (`/v1/sessions/:id/events/stream`) is considered the **primary thread**, containing a condensed view of all activity across all threads. You won't see the full activity from non-coordinator agents, but you will see the start and end of their work, as well as blocking events like tool permission requests.

**Session threads** are where you drill into a specific agent's activity.

The session `status` is an aggregation of all agent activity; if at least one thread is `running`, then the overall session status will be `running` as well.

A maximum of 25 concurrent threads are supported. The coordinator can call multiple copies of a single agent in the roster, creating multiple threads associated with one `agent`.

These events surface multiagent activity on the primary thread at `/v1/sessions/:id/events/stream`.

| Type | Description |
| --- | --- |
| `session.thread_created` | A thread was created. Includes `session_thread_id` and `agent_name`. |
| `session.thread_status_running` | A thread started activity. |
| `session.thread_status_idle` | The agent associated with the thread is awaiting input. Includes a `stop_reason` indicating why the agent stopped. |
| `session.thread_status_terminated` | A thread was archived or encountered a terminal error. |
| `agent.thread_message_received` | An agent delivered its result to the coordinator. Includes `from_session_thread_id`, `from_agent_name`, and `content`. |
| `agent.thread_message_sent` | The coordinator sent a follow-up to another agent. Includes `to_session_thread_id`, `to_agent_name`, and `content`. |

Critical events are proxied to the primary thread. However, you may still want to investigate a specific agent's reasoning and tool calls. To do so, stream or list the events from the associated session thread.

### Tool permissions and custom tools

If a non-coordinator agent needs something from your client, such as [permission](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#tool-confirmation) to run an `always_ask` tool, or the [result of a custom tool](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#handling-custom-tool-calls), the event is cross-posted to the **primary thread** with `session_thread_id` identifying the originating session thread.

```
{
  "type": "session.thread_status_idle",
  "id": "sevt_01ABC...",
  "session_thread_id": "sth_01DEF...",
  "agent_name": "code-reviewer",
  "stop_reason": {
    "type": "requires_action",
    "event_ids": ["toolu_01XYZ..."]
  }
}
```

Post `user.tool_confirmation` (with `tool_use_id`) or `user.custom_tool_result` (with `custom_tool_use_id`); the server routes the response to the correct thread automatically.

The example below extends the [tool confirmation handler](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#tool-confirmation) to route replies. The same pattern applies to `user.custom_tool_result`.

```
for event_id in stop.event_ids:
    client.beta.sessions.events.send(
        session.id,
        events=[
            {
                "type": "user.tool_confirmation",
                "tool_use_id": event_id,
                "result": "allow",
            }
        ],
    )
```

Was this page helpful?