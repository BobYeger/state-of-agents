# Issue Tracker Control Plane

An issue tracker control plane turns tickets into durable agent work units. Each issue can own an isolated workspace, workflow policy, status transitions, retries, evidence, and review.

The important shift is from supervising individual chat sessions to managing work. This makes long-running coding agents easier to coordinate, observe, and govern.

For local coding agents, Git worktrees are the small-scale version of this pattern: one task or agent thread gets a separate checkout, while the harness or issue tracker decides how the result is reviewed and merged.

## Related Sources

- [[sources/OpenAI Symphony]]
- [[sources/OpenAI Codex App Worktrees]]
- [[sources/OpenAI Codex Agent Loop]]
- [[sources/Cursor Scaling Long-Running Autonomous Coding]]

## Related

- [[operations/agent harnesses]]
- [[operations/worktree isolation]]
- [[operations/durable sessions]]
- [[operations/agent observability]]
- [[systems/Codex]]
