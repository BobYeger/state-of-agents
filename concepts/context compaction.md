# Context Compaction

Context compaction is the practice of reducing or rewriting an agent's accumulated interaction history so a long-running task can continue within a finite context window.

For agents, compaction is not just summarization. It is an architecture choice about what state stays in the active model context, what is replaced by summaries or placeholders, what is moved to memory, and what remains recoverable outside the context window.

## Evaluation at the Compaction Boundary

Compaction quality should be measured by what the agent can do next, not by whether a summary resembles the text it replaced. [[sources/Toward Reliable Context Compression for Long-Horizon Agents]] operationalizes this with TRACE: paired closed-loop continuations start from the same environment state with either the raw interaction update or its replacement summary, estimating the marginal blocked/error and repeated-call burden introduced at that boundary.

This boundary-local design complements end-to-end task scores, which cannot identify which transition introduced extra execution burden. A plausible-looking summary can still make a recent constraint or completed action less usable. The evidence is preliminary and AppWorld lets agents re-query much of the environment, so the reported gains do not establish a universal compression policy; the durable method is the paired continuation test around each lossy boundary.

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
- [[sources/Toward Reliable Context Compression for Long-Horizon Agents]]
