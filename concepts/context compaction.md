# Context Compaction

Context compaction is the practice of reducing or rewriting an agent's accumulated interaction history so a long-running task can continue within a finite context window.

For agents, compaction is not just summarization. It is an architecture choice about what state stays in the active model context, what is replaced by summaries or placeholders, what is moved to memory, and what remains recoverable outside the context window.

## Related

- [[concepts/context engineering]]
- [[concepts/observation masking]]
- [[concepts/tool-result clearing]]
- [[concepts/handoff over compaction]]
- [[concepts/task-aware context pruning]]
- [[operations/agent harnesses]]
- [[operations/agent memory]]
- [[maps/Context Management Map]]

## Related Sources

- [[sources/Anthropic Context Engineering Cookbook]]
- [[sources/OpenAI Responses API Computer Environment]]
- [[sources/OpenAI Agents SDK Compaction Sessions]]
- [[sources/The Complexity Trap]]
- [[sources/ACON]]
- [[sources/Parallel Context Compaction]]
- [[sources/MEMENTO]]
- [[sources/Factory Context Compression Evaluation]]
- [[sources/Google ADK Context Compression]]
- [[sources/Microsoft Agent Framework Harness Compaction]]
- [[sources/Claude Code Prompt Caching]]
