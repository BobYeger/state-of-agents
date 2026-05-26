# Subagent Context Isolation

Subagents are useful not only for parallelism, but for context isolation. A lead agent can delegate a bounded task to a specialist with its own prompt, tools, memory, and trace, then receive a distilled result.

This reduces contamination of the lead context and makes specialization auditable. It also introduces coordination costs, so subagents need task-fit, handoff contracts, and observability.

## Related Sources

- [[sources/Anthropic Managed Agents Dreaming Outcomes]]
- [[sources/Anthropic Claude Code Worktrees]]
- [[sources/Cursor 2.0]]
- [[sources/Anthropic Multi-Agent Research System]]
- [[sources/LangChain Deep Agents Docs]]
- [[sources/MiniMax Agent Team]]

## Related

- [[concepts/multi-agent systems]]
- [[methods/multi-agent orchestration]]
- [[operations/worktree isolation]]
- [[operations/agent observability]]
- [[maps/MAS Orchestration and Architecture]]
