# Claude Code Hooks Reference

Source URL: https://code.claude.com/docs/en/hooks

Capture date: 2026-06-21

Capture note: concise local research snapshot from the official Claude Code Hooks reference. Cite the canonical URL for the full event schemas and examples.

## Core framing

Claude Code hooks are lifecycle handlers that run automatically when configured events fire. A hook handler can be a shell command, HTTP endpoint, MCP tool, LLM prompt, or agent. Claude Code passes JSON event context to the handler; the handler can inspect the input, take action, and sometimes return a decision.

The reference separates hook cadence into:

| Cadence | Examples | Method relevance |
|---|---|---|
| Session-level | `SessionStart`, `SessionEnd`, `Setup` | Initialize, restore, or clean up durable context. |
| Turn-level | `UserPromptSubmit`, `Stop`, `StopFailure` | Inject context, validate completion, continue or log failures. |
| Tool-loop-level | `PreToolUse`, `PermissionRequest`, `PostToolUse`, `PostToolUseFailure`, `PostToolBatch` | Gate tool calls, observe results, run validation, or feed back errors. |
| Subagent/team-level | `SubagentStart`, `SubagentStop`, `TaskCreated`, `TaskCompleted`, `TeammateIdle` | Enforce delegation, task quality gates, and teammate completion checks. |
| Runtime/UI | `PreCompact`, `PostCompact`, `FileChanged`, `CwdChanged`, `WorktreeCreate`, `WorktreeRemove`, `Notification`, `ConfigChange`, `MessageDisplay` | Preserve context, update environment, customize worktree behavior, notify, or monitor. |

## Decision control

- `PreToolUse` can allow, deny, ask, or defer tool calls after Claude has produced parameters but before the tool executes.
- `PostToolUse` and related events can feed validation results back after execution.
- `Stop` and `SubagentStop` can prevent stopping and return a reason or additional context.
- `TaskCreated`, `TaskCompleted`, and `TeammateIdle` can block task state changes and return feedback to the model or teammate.
- Some events are observational only; blocking behavior depends on event type.

## Advanced hook forms

- Command hooks read JSON from stdin and communicate through exit code, stdout, and stderr.
- HTTP hooks receive the event input as POST body.
- MCP tool hooks call tools on already connected MCP servers.
- Prompt hooks use a Claude model as a single-turn evaluator.
- Agent hooks use a configured agent as the hook handler.
- Async hooks can run in the background for non-blocking side effects such as tests after file changes.

## Method reading

The hook reference makes lifecycle points explicit. This matters because a harness can enforce behavior at the exact moment where failure matters: before a dangerous command, after a file edit, before compaction, when a subagent stops, or when the main agent claims it is done.

Claude Code also documents `/goal` as a built-in shortcut for a session-scoped prompt-based `Stop` hook. That connects goal commands directly to hook-based continuation control.

## Related official docs

- Hooks guide: https://code.claude.com/docs/en/hooks-guide
- Settings: https://code.claude.com/docs/en/settings
- Monitoring: https://code.claude.com/docs/en/monitoring-usage
- Agent SDK Python: https://code.claude.com/docs/en/agent-sdk/python
- Subagents: https://code.claude.com/docs/en/sub-agents
- Costs: https://code.claude.com/docs/en/costs
