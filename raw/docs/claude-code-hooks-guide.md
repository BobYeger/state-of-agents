# Claude Code Hooks Guide

Source URL: https://code.claude.com/docs/en/hooks-guide

Capture date: 2026-06-21

Capture note: concise local research snapshot from the official Claude Code guide "Automate actions with hooks." Cite the canonical URL for the full setup examples.

## Core framing

The guide presents hooks as deterministic control over Claude Code behavior: certain actions should happen because the harness runs them at lifecycle points, not because the model remembers to choose them.

The guide's main examples include:

- notify when Claude needs input
- format code after edits
- block protected file edits
- re-inject context after compaction
- audit configuration changes
- reload environment when the current directory or files change
- auto-approve narrow permission prompts

## Configuration shape

Hooks are configured under a `hooks` object in Claude Code settings. Each event contains matcher groups, and each matcher group contains one or more handlers.

Typical pattern:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          { "type": "command", "command": "prettier --write ..." }
        ]
      }
    ]
  }
}
```

Matchers narrow when a hook fires. Tool events match on tool name, session events match on session source, notification events match on notification type, subagent events match on agent type, and compaction events match on compaction trigger.

## Output and control

- Exit `0`: no objection; for some events stdout can add context.
- Exit `2`: block where the event supports blocking; stderr becomes feedback to Claude or the user.
- JSON output: supports structured decisions, reasons, additional context, approval behavior, or event-specific control.

The guide distinguishes deterministic command hooks from prompt-based or agent-based hooks. Command hooks are appropriate for exact rules; prompt or agent hooks are useful when the hook needs judgement.

## Method reading

The guide is useful because it turns "rules in prompt" into "rules in runtime." Hooks are best treated as a harness method for policy gates, context injection, validation, and integration. They are especially important when the desired behavior should be reliable across sessions, compaction, subagents, and repeated tool calls.
