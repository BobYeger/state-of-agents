# Context Management Map

This map tracks how agent systems keep long-running work coherent without flooding the model context window.

The organizing distinction is between prompt compression and agent context management. Prompt compression shrinks a prepared input. Agent context management governs an evolving trajectory of goals, messages, tool calls, observations, files, decisions, and memory.

## Methods

| Method | What It Does | Anchor Sources |
|---|---|---|
| Structured summarization | Rewrites earlier history into task-state summaries. | [[concepts/context compaction]], [[sources/Factory Context Compression Evaluation]] |
| Boundary-local compaction evaluation | Compares paired continuations from the same environment state with raw versus compressed history to estimate the marginal execution burden introduced at that transition. | [[concepts/context compaction]], [[sources/Toward Reliable Context Compression for Long-Horizon Agents]] |
| Provider-native compaction | Lets the model/provider emit a compact state representation or compaction item. | [[concepts/context compaction]], [[sources/OpenAI Responses API Computer Environment]] |
| Per-agent context isolation | Gives each delegated worker an independent history and compaction lifecycle, reducing cross-task interference while making handoff design more important. | [[concepts/subagent context isolation]], [[sources/OpenAI Responses API Multi-Agent]], [[sources/Claude Fable 5 Prompting Guide]] |
| Parallel compaction | Splits compaction into blocks to improve latency and make summary volume more predictable. | [[concepts/context compaction]], [[sources/Parallel Context Compaction]] |
| Model-internal compaction | Teaches models to carry compact intermediate state rather than relying only on harness summaries. | [[concepts/context evolution]], [[sources/MEMENTO]] |
| Observation masking | Hides older observations while preserving trajectory structure. | [[concepts/observation masking]], [[sources/The Complexity Trap]] |
| Tool-result clearing | Drops old bulky tool outputs while preserving the tool-call record. | [[concepts/tool-result clearing]], [[sources/Anthropic Context Engineering Cookbook]] |
| Memory offload | Writes durable knowledge outside the active context window. | [[operations/agent memory]], [[sources/Cloudflare Agent Memory]], [[sources/Agent Memory Characterization]], [[sources/Are We Ready For An Agent-Native Memory System]] |
| Virtual context paging | Pages information between bounded main context and external storage, with the model editing its own memory via function calls. | [[sources/MemGPT]], [[sources/Letta Code Memory Docs]] |
| Plan recitation | Continuously rewrites a plan file so the global goal stays in recent attention against mid-context drift. | [[sources/Manus Context Engineering]] |
| Shared memory stores | Governs fleet- or team-level memory: write authority, reconciliation, namespacing, provenance. | [[concepts/shared agent memory]], [[sources/Claude Managed Agents Memory Stores]], [[sources/Governed Shared Memory for Multi-Agent LLM Systems]], [[sources/G-Memory]] |
| Background consolidation | Runs a between-session process that merges, prunes, and generalizes accumulated memory. | [[concepts/dreaming and memory consolidation]], [[sources/Anthropic Managed Agents Dreaming Outcomes]], [[sources/Generative Agents]] |
| Agent-native memory representation | Designs memory as an agent data-management subsystem with storage, extraction, retrieval/routing, and maintenance. | [[sources/Agent Memory Characterization]], [[sources/Are We Ready For An Agent-Native Memory System]], [[sources/Memora]] |
| Execution-state memory | Stores the current task trajectory as structured execution state rather than only semantic facts. | [[sources/MAGE Memory Execution State Management]] |
| Agent-visible context dashboard | Exposes typed working-memory blocks with usage/recency stats and reversible archives so the agent manages its own context. | [[sources/VISTA Latent Context Managers]] |
| Cache-aware context policy | Optimizes compaction and eviction for cache stability, latency, cost, and long-running coding trajectories. | [[sources/TokenPilot]], [[sources/SWE-MeM]] |
| Topic-document memory | Consolidates observations into maintainable topical documents or dual text/code memory. | [[sources/Infini Memory]], [[sources/Metis]], [[sources/Zep Markdown Is Not Agent Memory]] |
| Handoff | Starts a focused new session with a continuation package. | [[concepts/handoff over compaction]], [[sources/Amp Handoff]] |
| Task-aware pruning | Selects lines or evidence according to the current goal. | [[concepts/task-aware context pruning]], [[sources/SWE-Pruner]] |
| Context retrieval | Measures and improves whether the agent finds useful context. | [[concepts/context retrieval]], [[sources/ContextBench]] |
| Memory activation / prospective intention | Surfaces decision-critical memory or a deferred action from query, time, event, state, or always-visible policy. | [[sources/Keep It InMind]], [[sources/PM-Bench]] |
| Source-backed revalidation | Checks a mutable memory against its authoritative live substrate before use. | [[sources/GitHub Copilot Agentic Memory]] |
| Immutable archive + agent search | Preserves full-fidelity history and shifts semantic work from index construction to query-time controlled search. | [[sources/When Your Agent Opens the Chat App]], [[sources/LongMemEval-V2]] |
| Structured boundary filtering | Uses namespaces for tenant/security isolation, then deterministic metadata for consolidation partitions and semantic-search prefilters within the namespace. | [[sources/AWS AgentCore Structured Memory Filtering]] |
| Context evolution | Decides when to retrieve new evidence vs think with existing context. | [[concepts/context evolution]], [[sources/To Retrieve or To Think]] |

## Background

Prompt compression is useful background, but it should not dominate the agent graph. Keep it as a prelude to agent-specific context management.

| Background Thread | Anchor Sources |
|---|---|
| Long-context degradation (why compaction exists) | [[sources/Lost in the Middle]] positional U-shape; [[sources/Context Rot]] length degradation across 18 models |
| Memory architecture lineage | [[sources/MemGPT]] OS-style paging; [[sources/Cognitive Architectures for Language Agents]] memory taxonomy; [[sources/Generative Agents]] retrieval triple and reflection |
| Small-window prompt compression era | [[sources/Prompt Compression Survey]] maps the family, [[sources/LLMLingua]] is the namesake; superseded in agent practice by task-aware pruning ([[sources/SWE-Pruner]]) and learned compaction ([[sources/ACON]]) |

## Benchmarks

- [[benchmarks/agent memory benchmarks]] is the versioned comparison spine for memory abilities, splits, model–harness configurations, judges, runs, latency, and cost.
- [[sources/LOCA-bench]] evaluates agents under controlled context growth.
- [[sources/ContextBench]] evaluates coding-agent context retrieval.
- [[sources/Letta Context-Bench]] evaluates agentic context engineering with file tools.
- [[sources/LoCoMo]] and [[sources/LongMemEval]] evaluate conversational memory; LongMemEval includes knowledge updates and abstention.
- [[sources/BEAM]] stresses ten abilities from 128K to 10M tokens, while [[sources/MemoryAgentBench]] tests incremental retrieval, learning, global understanding, and forgetting.
- [[sources/MemoryArena]] tests whether memory guides later actions across interdependent sessions; [[sources/LongMemEval-V2]] tests retrieval of environment experience and procedural runbooks.

Memory-substrate selection guidance lives in [[operations/agent memory]].

## Synthesis

The core question is not "Should we compact?" It is: what information is lossy, what is re-fetchable, what needs exact preservation, what must activate without a matching query, and where should the state live?

For coding agents, exact files, test results, decisions, and current goals are often more important than broad narrative summaries. For research agents, citations, document provenance, and dead ends may matter more. A maintainable harness should expose the method, trigger, preserved fields, risks, and evaluation criteria.

The August 2026 memory sources sharpen the map: memory is no longer only retrieval. It includes activation before query similarity exists, prospective intentions, construction scheduling, freshness, read-time verification, operational authority, derivation-aware deletion, budget-aware rendering, and operation-level evaluation. The orchestration sources add a second boundary: a multi-agent system also needs an explicit policy for which state stays private to a worker, what crosses handoffs, and whether each worker compacts independently.

## Related

- [[reports/Agent Memory Report]]
- [[reports/Agent Memory Technical Brief]]
- [[benchmarks/agent memory benchmarks]]
- [[concepts/context engineering]]
- [[concepts/context compaction]]
- [[concepts/shared agent memory]]
- [[concepts/dreaming and memory consolidation]]
- [[operations/agent harnesses]]
- [[operations/agent memory]]
- [[maps/Recent Agent Operating Concepts]]
- [[maps/What Makes Agent Systems Better]]
