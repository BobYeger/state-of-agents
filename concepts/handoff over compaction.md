# Handoff Over Compaction

Handoff over compaction starts a new thread or session with a deliberately prepared continuation package instead of repeatedly summarizing one long thread.

Amp's 2025 article is the originating product example in this vault, but not its current behavior: the rebuilt 2026 Amp loop uses automatic compaction. The pattern remains useful independently when task boundaries are clearer than one continuously summarized thread.

The goal is to preserve task continuity while encouraging focused work units. It works best when the new session receives a clear goal, relevant files, current decisions, open tasks, and known dead ends.

## Related

- [[concepts/context compaction]]
- [[operations/worktree isolation]]
- [[operations/durable sessions]]
- [[operations/agent harnesses]]
- [[methods/ralph loop]]
- [[maps/Context Management Map]]

## Related Sources

- [[sources/Amp Handoff]]
- [[sources/Amp Agent Harness]]
- [[sources/Anthropic Effective Harnesses for Long-Running Agents]]
- [[sources/OpenAI Codex App Worktrees]]
