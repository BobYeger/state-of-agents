# Claude Code

Anthropic's coding-agent product and harness surface for terminal-centered software engineering workflows.

## Design Pattern

- Use worktrees to isolate parallel Claude Code sessions so concurrent file edits do not collide.
- Combine worktrees with subagents when a task needs both separate context and separate filesystem state.
- Treat `.worktreeinclude`, cleanup policy, and base-branch choice as part of the harness rather than incidental Git setup.
- Use cross-session messaging for live, independently started sessions that need to exchange a finding, status, or decision. Use Agent Teams when the work also needs a lead and shared task state.
- Treat inbound session messages as peer-authored text rather than user authority: configure `accept`/`hold`/`refuse`, preserve the receiving session's permission boundary, and do not assume an offline durable inbox.

## Related Sources

- [[sources/Anthropic Claude Code Worktrees]]
- [[sources/Claude Code Cross-Session Messaging]]
- [[sources/Claude Code Agent Teams]]
- [[sources/Claude Code Hooks]]
- [[sources/Claude Code Skills Docs]]
- [[sources/Claude Code Scheduled Tasks]]
- [[sources/Claude Code Workflows]]
- [[sources/Anthropic Effective Harnesses for Long-Running Agents]]
- [[sources/Anthropic Harness Design Long-Running Apps]]
- [[sources/Anthropic Claude Code Sandboxing]]
- [[sources/Anthropic Claude Code Auto Mode]]
- [[sources/Anthropic Parallel Claudes C Compiler]]
- [[sources/SkillOpt]]
