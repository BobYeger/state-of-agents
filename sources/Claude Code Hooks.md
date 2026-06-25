---
title: "Claude Code Hooks"
aliases:
  - "Claude Code hooks"
  - "Hooks reference"
  - "Automate actions with hooks"
source_type: "docs"
kind: "harness-docs"
status: "verified"
year: 2026
publication_date: "2026-06-21"
publication_date_basis: "accessed_living_docs_no_visible_publication_date"
source_updated_date: "2026-06-21"
source_updated_date_basis: "snapshot_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Anthropic"
venue: "Claude Code Docs"
url: "https://code.claude.com/docs/en/hooks"
pdf_url: ""
artifacts:
  - "raw/docs/claude-code-hooks-reference.md"
  - "raw/docs/claude-code-hooks-guide.md"
created: 2026-06-21
updated: 2026-06-21
---

# Claude Code Hooks

## Summary

- Official Claude Code docs for lifecycle hooks: user-defined commands, HTTP endpoints, MCP tools, LLM prompts, or agents that run at specific points in a Claude Code session.
- Key source for [[methods/hook-based control]] because it turns agent behavior from "Claude should remember" into deterministic harness control at session, turn, tool, subagent, compaction, file, worktree, and notification boundaries.
- Hooks can observe, inject context, block actions, request approval, run validators, continue a session, enforce teammate quality gates, emit telemetry, or integrate with external systems.
- Important bridge between [[concepts/loop engineering]] and [[methods/runtime supervision]]: Claude Code documents `/goal` as a built-in shortcut for a session-scoped prompt-based `Stop` hook.

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[methods/hook-based control]]
- [[methods/runtime supervision]]
- [[concepts/loop engineering]]
- [[operations/agent harnesses]]
- [[operations/agent observability]]
- [[operations/cost control]]
- [[systems/Claude Code]]
- [[sources/Claude Code Agent Teams]]
- [[sources/Claude Code Skills Docs]]
- [[sources/Anthropic Claude Code Worktrees]]

## Hook Taxonomy

- Session hooks: initialize, end, configure, or restore context around a session.
- Prompt hooks: inspect or augment user prompts before the model processes them.
- Tool hooks: validate, block, approve, observe, or post-process tool calls.
- Completion hooks: block premature stopping or return additional context for continuation.
- Subagent and team hooks: enforce task creation, task completion, subagent stop, and teammate idle quality gates.
- Runtime hooks: react to compaction, file changes, current working directory changes, worktree lifecycle, config changes, notifications, and displayed messages.

## Harness Reading

Hooks are a method for moving behavioral constraints out of probabilistic model memory and into deterministic lifecycle control. Prompts and skills can tell an agent what to prefer; hooks decide what happens at a specific point in the loop.

Use them when the system needs a reliable side effect, policy gate, context injection, external validator, audit trail, or continuation check. Avoid treating hooks as a full policy engine: hard security still needs permissions, sandboxing, and managed settings.

## Artifacts

- [[raw/docs/claude-code-hooks-reference.md]]
- [[raw/docs/claude-code-hooks-guide.md]]

## Notes

- Hooks reference: https://code.claude.com/docs/en/hooks
- Hooks guide: https://code.claude.com/docs/en/hooks-guide
- Settings for managed hooks and HTTP hook allowlists: https://code.claude.com/docs/en/settings
- Monitoring hook telemetry: https://code.claude.com/docs/en/monitoring-usage
- Agent SDK hook usage: https://code.claude.com/docs/en/agent-sdk/python
