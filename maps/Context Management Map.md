# Context Management Map

This map tracks how agent systems keep long-running work coherent without flooding the model context window.

The organizing distinction is between prompt compression and agent context management. Prompt compression shrinks a prepared input. Agent context management governs an evolving trajectory of goals, messages, tool calls, observations, files, decisions, and memory.

## Methods

| Method | What It Does | Anchor Sources |
|---|---|---|
| Structured summarization | Rewrites earlier history into task-state summaries. | [[concepts/context compaction]], [[sources/Factory Context Compression Evaluation]] |
| Provider-native compaction | Lets the model/provider emit a compact state representation or compaction item. | [[concepts/context compaction]], [[sources/OpenAI Responses API Computer Environment]] |
| Parallel compaction | Splits compaction into blocks to improve latency and make summary volume more predictable. | [[concepts/context compaction]], [[sources/Parallel Context Compaction]] |
| Model-internal compaction | Teaches models to carry compact intermediate state rather than relying only on harness summaries. | [[concepts/context evolution]], [[sources/MEMENTO]] |
| Observation masking | Hides older observations while preserving trajectory structure. | [[concepts/observation masking]], [[sources/The Complexity Trap]] |
| Tool-result clearing | Drops old bulky tool outputs while preserving the tool-call record. | [[concepts/tool-result clearing]], [[sources/Anthropic Context Engineering Cookbook]] |
| Memory offload | Writes durable knowledge outside the active context window. | [[operations/agent memory]], [[sources/Cloudflare Agent Memory]] |
| Handoff | Starts a focused new session with a continuation package. | [[concepts/handoff over compaction]], [[sources/Amp Handoff]] |
| Task-aware pruning | Selects lines or evidence according to the current goal. | [[concepts/task-aware context pruning]], [[sources/SWE-Pruner]] |
| Context retrieval | Measures and improves whether the agent finds useful context. | [[concepts/context retrieval]], [[sources/ContextBench]] |
| Context evolution | Decides when to retrieve new evidence vs think with existing context. | [[concepts/context evolution]], [[sources/To Retrieve or To Think]] |

## Background

Prompt compression is useful background, but it should not dominate the agent graph. Keep it as a prelude to agent-specific context management.

| Background Thread | Anchor Sources |
|---|---|
| Prompt compression survey | [[concepts/prompt compression]], [[sources/Prompt Compression Survey]] |
| Token pruning | [[concepts/prompt compression]], [[sources/LLMLingua]] |
| Retrieval compression | [[sources/RECOMP]] |
| Soft-prompt / embedding compression | [[sources/AutoCompressors]], [[sources/Pretraining Context Compressor]] |

## Benchmarks

- [[sources/LOCA-bench]] evaluates agents under controlled context growth.
- [[sources/ContextBench]] evaluates coding-agent context retrieval.
- [[sources/Letta Context-Bench]] evaluates agentic context engineering with file tools.

## Synthesis

The core question is not "Should we compact?" It is: what information is lossy, what is re-fetchable, what needs exact preservation, and where should the state live?

For coding agents, exact files, test results, decisions, and current goals are often more important than broad narrative summaries. For research agents, citations, document provenance, and dead ends may matter more. A maintainable harness should expose the method, trigger, preserved fields, risks, and evaluation criteria.

## Related

- [[concepts/context engineering]]
- [[concepts/context compaction]]
- [[operations/agent harnesses]]
- [[operations/agent memory]]
- [[maps/Recent Agent Operating Concepts]]
- [[maps/What Makes Agent Systems Better]]
