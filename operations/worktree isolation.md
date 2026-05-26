# Worktree Isolation for Coding Agents

Worktree isolation is a coding-agent operating pattern: each agent session gets a separate Git worktree so file edits, branches, dependencies, build artifacts, and review state do not collide with the user's foreground checkout or with other agents.

This is not a security sandbox. A worktree is a filesystem and Git isolation primitive. It helps separate code changes and agent context, but it does not by itself restrict network access, credential access, command execution, or filesystem reads outside the checkout.

## Why It Matters

- Multiple coding agents can work on the same repository in parallel without editing the same working tree.
- Each task can keep its own branch, thread, conversation history, tests, logs, and review surface.
- A human can compare competing patches, keep one, discard another, or hand a task back into the local checkout for manual inspection.
- Agent subteams can use worktrees as context and file isolation while coordination happens through a harness, issue tracker, or lead agent.

## Failure Modes

- Worktrees can accumulate disk usage through duplicate dependencies, build caches, and generated artifacts.
- Gitignored files such as `.env` or local config do not automatically exist in each worktree unless copied deliberately.
- Ports, databases, caches, and external services can still collide unless the harness assigns separate runtime resources.
- Worktrees reduce edit collisions; they do not replace reviews, tests, permission gates, or sandbox policy.

## Related Sources

- [[sources/Anthropic Claude Code Worktrees]]
- [[sources/OpenAI Codex App Worktrees]]
- [[sources/Cursor 2.0]]
- [[sources/OpenAI Codex App]]
- [[sources/Nate Ross Claude Code Worktrees]]

## Related

- [[operations/agent harnesses]]
- [[operations/sandboxes]]
- [[concepts/subagent context isolation]]
- [[concepts/issue tracker control plane]]
- [[systems/Claude Code]]
- [[systems/Codex]]
- [[systems/Cursor agents]]
