# Hook-Based Control

Hook-based control is the use of lifecycle interception points around an agent loop to run deterministic code, external services, MCP tools, prompts, or subagents before the agent continues.

It is an agentic method at the harness layer. The model still reasons and proposes actions, but the harness can observe, block, validate, inject context, continue, or escalate at specific moments.

## Pattern

```text
agent event -> matcher -> hook handler -> decision / side effect / context -> agent continues
```

## Common Hook Roles

| Role | Lifecycle point | Typical action |
|---|---|---|
| Gate | before tool, permission, task creation | block dangerous commands, protected file edits, unsupported tasks, or unsafe MCP tools |
| Feedback | after tool, failed tool, batch result | run formatter, lint, tests, scanner, or validator and feed findings back |
| Continuation | stop, subagent stop, teammate idle, task complete | prevent premature completion until tests, artifacts, or quality gates pass |
| Context | session start, prompt submit, pre/post compaction, cwd/file change | inject project state, reload environment, preserve compaction context, add focused evidence |
| Observability | hook execution, tool use, config change, stop failure | log actions, costs, latency, policy decisions, and failures |
| Integration | HTTP hooks, MCP hooks, external event hooks | connect the agent loop to CI, ticket systems, review systems, and org policy services |

## Why It Matters

Prompts and skills can influence what an agent tries to do. Hooks make selected behavior operational: the system runs a check or side effect at the moment where it matters.

This is especially useful for:

- enforcing project rules that should not rely on model memory
- making tool use safer before execution
- making completion criteria executable
- keeping context fresh after compaction or environment changes
- turning tests, linters, scanners, and cost filters into runtime feedback
- making subagent and teammate work auditable

## Claude Code Anchor

[[sources/Claude Code Hooks]] is the current strongest source. It documents `PreToolUse`, `PostToolUse`, `UserPromptSubmit`, `Stop`, `SubagentStop`, `TaskCreated`, `TaskCompleted`, `TeammateIdle`, `PreCompact`, `PostCompact`, `WorktreeCreate`, `WorktreeRemove`, HTTP hooks, MCP tool hooks, prompt hooks, agent hooks, async hooks, and hook telemetry.

The important design link is that Claude Code describes `/goal` as a built-in shortcut for a session-scoped prompt-based `Stop` hook. Goal-oriented agents, loop engineering, and hook-based control are therefore part of the same harness control family.

## Boundaries

Hooks are not a substitute for permissions, sandboxing, or managed policy. They are also not just webhooks. A webhook wakes or notifies a system from the outside; a hook is a lifecycle interception point inside the agent runtime.

Use hooks when the behavior should be reliable and localized to a lifecycle event. Use workflows or state machines when the whole control path needs explicit durable orchestration.

## Related

- [[operations/agent harnesses]]
- [[methods/runtime supervision]]
- [[concepts/loop engineering]]
- [[concepts/outcomes and rubric graders]]
- [[operations/agent observability]]
- [[operations/cost control]]
- [[operations/permissions]]
- [[operations/sandboxes]]
