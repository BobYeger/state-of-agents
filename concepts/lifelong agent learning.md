# lifelong agent learning

Lifelong agent learning covers memory, reusable experience, learned rules, and post-deployment improvement loops.

The useful design question is how an agent turns experience into reusable, governed capability. Learning loops need memory, skill extraction, evaluation, provenance, and safe update rules; otherwise they can preserve errors as easily as improvements.

## Mechanisms

- Distill successful and failed trajectories into reusable strategies.
- Convert repeated procedures into skills or learned rules.
- Use evals to decide whether a learned behavior should be reused.
- Track provenance, scope, and freshness for learned memory.
- For code-based learning, use sandboxes, rollback, and evaluator-hardening before learned artifacts can affect future runs.

## Evidence Lineage

Four threads run through the sources, and they matured at different rates.

**Experience distilled into text.** [[sources/Reflexion]]: self-reflections stored as text and prepended to retries, with gains that depend on external evaluation signal quality — the foundational citation for every memory-plus-retry pattern. [[sources/Generative Agents]]: the memory stream with retrieval scored by recency, importance, and relevance, plus reflection that synthesizes raw records into higher-level inferences — the template for memory that restructures itself. [[sources/Google ReasoningBank]] carries the modern form: reusable strategies distilled from both successes and failures.

**Memory substrates.** [[sources/MemGPT]]: the agent manages its own memory through function calls, paging between bounded context and external storage. [[sources/A-MEM]]: each memory becomes a structured note with agent-decided links, and new entries can retroactively rewrite old ones. [[sources/Mem0]]: extraction-and-consolidation pipelines beat full-context replay on cost and latency, and its graph variant adds only ~2% — structure is not free improvement. [[sources/Zep Temporal Knowledge Graph Memory]]: bi-temporal facts with automatic invalidation, so the store knows when a fact stopped being true. [[operations/agent memory]] carries the operational treatment; [[sources/Memory in the Age of AI Agents]] is the survey that gives the field its taxonomy (forms, functions, dynamics) and separates agent memory from RAG and context engineering.

**Measurement.** [[sources/LongMemEval]]: five memory abilities including knowledge updates and abstention — a learning loop that cannot supersede stale facts or decline to answer fails here, and commercial assistants drop ~30% accuracy across sustained interactions. It is now the de-facto reporting benchmark for the substrate thread.

**Governance, and what happens without it.** Learning loops preserve errors as easily as improvements, and shared memory makes that collective: [[sources/When Agents Misremember Collectively]] documents false memories reinforcing across agents. [[sources/Governed Shared Memory for Multi-Agent LLM Systems]] supplies the countermeasure primitives — scoped retrieval, temporal supersession, provenance tracking, policy-governed propagation; [[sources/G-Memory]] shows hierarchical memory propagating lessons across trials without flattening per-agent context. See [[concepts/agent failure modes]] for the failure-side treatment and [[concepts/shared agent memory]] for the design note.

**The loop closed in production.** [[sources/LangChain Agent Improvement Loop]]: traces become permanent eval cases and judge/human disagreements become grader tuning examples — the operational form of "use evals to decide whether a learned behavior should be reused." On the code side, the selection-policy and provenance mechanics in [[methods/self-improving code loops]] ([[sources/SICA Self-Improving Coding Agent]], [[sources/Huxley-Godel Machine]]) are the same lifelong-learning question with executable artifacts.

## Related

- [[maps/Self-Improving Systems Map]]
- [[operations/agent memory]]
- [[concepts/shared agent memory]]
- [[concepts/agent failure modes]]
- [[concepts/procedural memory]]
- [[concepts/agent skills]]
- [[methods/multi-agent learning]]
- [[methods/self-improving code loops]]
- [[operations/agent evals]]
- [[claims/Claim - Agent memory and skills create compounding improvement loops]]
- [[maps/What Makes Agent Systems Better]]

## Related Sources

- [[sources/Google ReasoningBank]]
- [[sources/Reflexion]]
- [[sources/Generative Agents]]
- [[sources/MemGPT]]
- [[sources/A-MEM]]
- [[sources/Mem0]]
- [[sources/Zep Temporal Knowledge Graph Memory]]
- [[sources/G-Memory]]
- [[sources/LongMemEval]]
- [[sources/Memory in the Age of AI Agents]]
- [[sources/Governed Shared Memory for Multi-Agent LLM Systems]]
- [[sources/LangChain Agent Improvement Loop]]
- [[sources/Darwin Godel Machine]]
- [[sources/SICA Self-Improving Coding Agent]]
- [[sources/Huxley-Godel Machine]]
- [[sources/Hyperagents]]
- [[sources/Meta-Harness]]
- [[sources/Cursor Bugbot Learned Rules]]
- [[sources/SkillRL]]
- [[sources/SAGE Skill Library]]
- [[sources/SkillOpt]]
- [[sources/SiriuS]]
- [[sources/SkillsBench]]
- [[sources/Agentic Skills in the Wild]]
