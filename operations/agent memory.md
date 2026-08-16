# Agent Memory

Agent memory stores reusable knowledge, preferences, and experience outside the current context window. Adjacent durable workflow state holds task progress and pending intentions. The harness surfaces either when a query, time, event, state, or policy makes it relevant.

Two surveys now anchor the field. [[sources/Memory for Autonomous LLM Agents]] (2026-03-08) is the narrower, single-author map of mechanisms and evaluation. [[sources/Memory in the Age of AI Agents]] (2025-12-15) is the larger 47-author survey: a three-axis taxonomy (forms, functions, dynamics) that also draws the boundary between agent memory, RAG, LLM memory, and context engineering — a boundary worth keeping when reading vendor material that blurs them.

## Lineage

Three papers supply the vocabulary the rest of the field reuses:

- [[sources/Generative Agents]] introduced the memory stream with retrieval scored by recency, importance, and relevance, plus reflection as a consolidation step — the retrieval triple most later scorers reuse, though its evidence is social-simulation believability, not task performance.
- [[sources/MemGPT]] introduced OS-style virtual context management: paging between bounded main context and external storage, with the model editing its own memory through function calls. The Letta product line descends from it directly ([[sources/Letta Code Memory Docs]]).
- [[sources/Cognitive Architectures for Language Agents]] is the citable origin of the working/episodic/semantic/procedural memory split this vault's memory notes use implicitly.

## Memory Risks

Memory poisoning attacks corrupt an agent's stored facts, preferences, procedures, or learned experience so future behavior is manipulated.

It matters more for agents than for chatbots because agents reuse state. A bad instruction, false fact, poisoned preference, or malicious tool note can persist across tasks and silently influence future planning, retrieval, or delegation.

The risk continues after ingestion. [[sources/HarnessSafe]] shows persistent carriers can be transformed through summaries, skills, delegation, and artifacts before a later benign task reactivates them. [[sources/When Memory Becomes Authority]] shows consolidation can preserve a claim while erasing whether it was authorized to drive action. [[sources/Deployment-Time Memorization in Foundation-Model Agents]] shows deleting a raw item can leave its derived summary recoverable. Treat entry, transformation, re-consumption, action, and whole-lineage deletion as one lifecycle.

## Improvement Claim

Memory improves agents when it stores reusable procedures and experience with provenance, scope, and evaluation. Unchecked memory can make agents worse; curated memory and skills can compound capability.

Useful control points:

- Separate trusted long-term memory from untrusted retrieved content.
- Separate provenance, writer, epistemic support, operational authority, and permitted uses.
- Track validity, expiry, version/hash, derivation lineage, review state, and last verification.
- Avoid turning user-visible documents or web pages directly into durable instructions.
- Revalidate mutable facts against their cited source when possible; [[sources/GitHub Copilot Agentic Memory]] is the production code-memory example.
- Reinspect persistent carriers at re-consumption and add an action-time authority gate before high-impact operations.
- Purge or tombstone derived summaries, indexes, and promoted skills when the originating memory is deleted.
- Periodically audit memory for stale, adversarial, or overfit entries.

The August 2026 memory cluster pushes this from "what should we remember?" toward "what memory subsystem should the harness operate?": activation before a matching query exists, prospective intentions, construction scheduling, source-backed validation, authority preservation, lifecycle deletion, cache-aware compaction, and operation-level evaluation.

## Substrate Selection

The substrate question — where memory physically lives — is separable from the policy questions above, and the evidence supports different substrates for different query shapes rather than one winner.

| Substrate | Best for | Evidence | Cost of choosing it wrongly |
|---|---|---|---|
| Markdown / plain files | Single agent, single user, low write volume, human-auditable state (`CLAUDE.md`, progress files) | [[sources/Zep Markdown Is Not Agent Memory]]: works at small scale, breaks under contradiction, supersession, and concurrency; [[sources/Letta Code Memory Docs]]: file-backed self-editing memory as a harness profile | No answer to "which version is current"; concurrent writers clobber each other |
| Immutable raw archive + agent search | Exact evidence over chat or trajectory histories; cheap construction | [[sources/When Your Agent Opens the Chat App]]: turn-level lexical index plus agent-controlled search reaches 58.2 mean on roughly 2,800 matched MemoryAgentBench questions, above the strongest compared graph/tree system at 53.2; baseline values are reused from MemoryAgentBench rather than rerun locally | Higher query-time model/tool cost; does not solve implicit activation, low-latency personalization, or prospective action |
| Vector store + extraction | Conversational recall; salient-fact QA | [[sources/Mem0]]: 26% relative improvement over OpenAI memory on LoCoMo; 91% lower p95 latency and >90% token savings versus full-context replay; its graph variant adds only ~2%, so extraction quality dominates structure here | Multi-hop and corpus-level questions fail: no small set of chunks contains the answer |
| Knowledge graph | Multi-hop reasoning; corpus-level sensemaking | [[sources/HippoRAG]]: KG index + PageRank matches iterative retrieval at 10-30x lower cost; [[sources/GraphRAG]]: community summaries answer global questions top-k vector RAG structurally cannot | Significant upfront indexing cost; wasted if queries are single-hop |
| Temporal knowledge graph | Facts that change; provenance and supersession requirements | [[sources/Zep Temporal Knowledge Graph Memory]]: bi-temporal records with automatic fact invalidation, up to +18.5% on LongMemEval (vendor-reported) | Same indexing cost, plus schema commitment; overkill for static reference material |
| Agent-curated notes | An agent maintaining its own evolving understanding | [[sources/A-MEM]]: Zettelkasten-style notes with agent-decided links and retroactive evolution, gains across six models | Retroactive rewriting erases the original record — a provenance loss shared stores cannot afford |
| Relational / structured store | Typed facts with fixed schema, tenant/compliance boundaries, exact filters, joins, aggregation | [[sources/AWS AgentCore Structured Memory Filtering]]: namespaces provide tenant/security isolation; within them, deterministic metadata partitions consolidation and pre-filters before similarity search; vendor test reports 40%→64% overall QA on 151 questions | Schema rigidity fights open-ended experience capture; vendor test is small and protocol details are undisclosed |

Three decision rules fall out. First, benchmark an immutable raw-record search baseline before paying to construct semantic structure. Second, match substrate to query shape: single-hop recall tolerates vectors, multi-hop and global questions need structure, changing facts need time, tenant/security isolation needs namespaces, and application-known business boundaries need deterministic fields before similarity. Third, substrate does not solve activation or governance—time/event/state triggers, provenance, authority, and supersession policy sit above it (see [[concepts/shared agent memory]]).

## Benchmarks

- [[benchmarks/agent memory benchmarks]] is the comparison registry. It pins the benchmark version and split, memory ability, scale, model, harness, context and retrieval budgets, judge, run count, latency, and cost basis required to interpret a score.
- Conversational recall: [[sources/LoCoMo]] tests QA, temporal and causal event summarization, and multimodal continuation; [[sources/LongMemEval]] adds multi-session extraction, temporal reasoning, knowledge updates, and abstention.
- Extreme scale: [[sources/BEAM]] spans released 128K, 500K, 1M, and 10M bands and ten memory abilities. At 10M, vanilla long-context readers use only their largest supported recent tail; RAG and LIGHT process or index the full conversation but answer from bounded retrieved or condensed context, so no reported arm is a direct full-context 10M read.
- Incremental operations: [[sources/MemoryAgentBench]] separates accurate retrieval, test-time learning, long-range understanding, and selective forgetting after chunk-by-chunk ingestion.
- Memory-guided action: [[sources/MemoryArena]] runs causally dependent subtasks in fresh sessions and measures success, partial progress, degradation with dependency depth, and latency.
- Environment experience: [[sources/LongMemEval-V2]] tests whether agents recover state, workflows, dynamics, and recurring gotchas from prior environment trajectories rather than only facts about a user.
- Adjacent axes: [[sources/Keep It InMind]] tests indirect application after successful storage, [[sources/PM-Bench]] tests prospective triggering, [[sources/MemOps]] tests operation-level state trajectories, and [[sources/HarnessSafe]] tests delayed reactivation through persistent carriers.

These benchmarks are complementary, not successive replacements. A conversational QA score does not establish implicit activation, test-time learning, or correct downstream action. Author and vendor results also use different readers, harnesses, judges, and budgets; compare configurations before quoting deltas.

## Related

- [[reports/Agent Memory Report]]
- [[reports/Agent Memory Technical Brief]]
- [[benchmarks/agent memory benchmarks]]
- [[concepts/context engineering]]
- [[concepts/context compaction]]
- [[concepts/shared agent memory]]
- [[concepts/dreaming and memory consolidation]]
- [[concepts/reasoning memory]]
- [[claims/Claim - Agent memory and skills create compounding improvement loops]]
- [[maps/Context Management Map]]
- [[maps/What Makes Agent Systems Better]]
- [[safety/prompt injection]]
- [[operations/durable sessions]]

## Related Sources

- [[sources/Agent Security Bench|Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents]]
- [[sources/AgentNet|AgentNet: Decentralized Evolutionary Coordination for LLM-based Multi-Agent Systems]]
- [[sources/Cloudflare Agent Memory|Agents that remember: introducing Agent Memory]]
- [[sources/Agent Memory Characterization|Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads]]
- [[sources/Are We Ready For An Agent-Native Memory System]]
- [[sources/Memory Poisoning Attacks in LLM Agents]]
- [[sources/SWE-MeM]]
- [[sources/TokenPilot]]
- [[sources/Memora]]
- [[sources/Metis]]
- [[sources/Zep Smart Context Assembly]]
- [[sources/Zep Markdown Is Not Agent Memory]]
- [[sources/Anthropic Context Engineering Cookbook|Context Engineering for AI Agents: Memory vs. Compaction vs. Tool Clearing]]
- [[sources/Anthropic Managed Agents Dreaming Outcomes|New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration]]
- [[sources/Anthropic Effective Context Engineering|Effective context engineering for AI agents]]
- [[sources/Memory for Autonomous LLM Agents|Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers]]
- [[sources/Trajectory-Informed Memory Generation|Trajectory-Informed Memory Generation for Self-Improving Agent Systems]]
- [[sources/Google ReasoningBank|ReasoningBank: Enabling agents to learn from experience]]
- [[sources/SiriuS|SiriuS: Self-improving Multi-agent Systems via Bootstrapped Reasoning]]
- [[sources/When Agents Misremember Collectively|When Agents Misremember Collectively: Exploring the Mandela Effect in LLM-based Multi-Agent Systems]]
- [[sources/Memory in the Age of AI Agents|Memory in the Age of AI Agents: A Survey]]
- [[sources/Claude Managed Agents Memory Stores|Using agent memory (Claude Managed Agents memory stores)]]
- [[sources/G-Memory|G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems]]
- [[sources/Governed Shared Memory for Multi-Agent LLM Systems]]
- [[sources/Keep It InMind]]
- [[sources/PM-Bench]]
- [[sources/When Memory Becomes Authority]]
- [[sources/GitHub Copilot Agentic Memory]]
- [[sources/AWS AgentCore Structured Memory Filtering]]
- [[sources/Toward Reliable Context Compression for Long-Horizon Agents]]
- [[sources/HarnessSafe]]
- [[sources/Deployment-Time Memorization in Foundation-Model Agents]]
- [[sources/MemOps]]
- [[sources/LongMemEval-V2]]
- [[sources/When Your Agent Opens the Chat App]]
- [[sources/Total Recall at What Cost]]

## Skills and Procedural Memory

- [[concepts/procedural memory]]
- [[sources/SAGE Skill Library]]
- [[sources/SkillRL]]
- [[sources/Voyager]]
