# Claude Code

Anthropic's coding-agent product and harness surface for terminal-centered software engineering workflows.

## Design Pattern

- Use worktrees to isolate parallel Claude Code sessions so concurrent file edits do not collide.
- Combine worktrees with subagents when a task needs both separate context and separate filesystem state.
- Treat `.worktreeinclude`, cleanup policy, and base-branch choice as part of the harness rather than incidental Git setup.

## Related Sources

- [[sources/Anthropic Claude Code Worktrees]]
- [[sources/Claude Code Skills Docs]]
- [[sources/Anthropic Effective Harnesses for Long-Running Agents]]
- [[sources/Anthropic Harness Design Long-Running Apps]]
- [[sources/Anthropic Claude Code Sandboxing]]
- [[sources/Anthropic Claude Code Auto Mode]]
- [[sources/Anthropic Parallel Claudes C Compiler]]
