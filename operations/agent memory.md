# Agent Memory

Agent memory stores reusable knowledge, preferences, task state, or experience outside the current context window.

Two surveys now anchor the field. [[sources/Memory for Autonomous LLM Agents]] is the earlier, narrower map of mechanisms and evaluation. [[sources/Memory in the Age of AI Agents]] is the larger successor: a three-axis taxonomy (forms, functions, dynamics) that also draws the boundary between agent memory, RAG, LLM memory, and context engineering — a boundary worth keeping when reading vendor material that blurs them.

## Lineage

Three papers supply the vocabulary the rest of the field reuses:

- [[sources/Generative Agents]] introduced the memory stream with retrieval scored by recency, importance, and relevance, plus reflection as a consolidation step — the retrieval triple most later scorers reuse, though its evidence is social-simulation believability, not task performance.
- [[sources/MemGPT]] introduced OS-style virtual context management: paging between bounded main context and external storage, with the model editing its own memory through function calls. The Letta product line descends from it directly ([[sources/Letta Code Memory Docs]]).
- [[sources/Cognitive Architectures for Language Agents]] is the citable origin of the working/episodic/semantic/procedural memory split this vault's memory notes use implicitly.

## Memory Risks

Memory poisoning attacks corrupt an agent's stored facts, preferences, procedures, or learned experience so future behavior is manipulated.

It matters more for agents than for chatbots because agents reuse state. A bad instruction, false fact, poisoned preference, or malicious tool note can persist across tasks and silently influence future planning, retrieval, or delegation.

## Improvement Claim

Memory improves agents when it stores reusable procedures and experience with provenance, scope, and evaluation. Unchecked memory can make agents worse; curated memory and skills can compound capability.

Useful control points:

- Separate trusted long-term memory from untrusted retrieved content.
- Track provenance, write authority, and expiration for memory items.
- Avoid turning user-visible documents or web pages directly into durable instructions.
- Add review gates before memories affect high-authority actions.
- Periodically audit memory for stale, adversarial, or overfit entries.

The June 2026 memory cluster pushes this from "what should we remember?" toward "what memory subsystem should the harness operate?": construction scheduling, retrieval/routing, freshness, cache-aware compaction, visible context state, topic maintenance, and poisoning resistance.

## Substrate Selection

The substrate question — where memory physically lives — is separable from the policy questions above, and the evidence supports different substrates for different query shapes rather than one winner.

| Substrate | Best for | Evidence | Cost of choosing it wrongly |
|---|---|---|---|
| Markdown / plain files | Single agent, single user, low write volume, human-auditable state (`CLAUDE.md`, progress files) | [[sources/Zep Markdown Is Not Agent Memory]]: works at small scale, breaks under contradiction, supersession, and concurrency; [[sources/Letta Code Memory Docs]]: file-backed self-editing memory as a harness profile | No answer to "which version is current"; concurrent writers clobber each other |
| Vector store + extraction | Conversational recall; salient-fact QA | [[sources/Mem0]]: 26% relative improvement over OpenAI memory on LoCoMo with 91% lower p95 latency; its graph variant adds only ~2%, so extraction quality dominates structure here | Multi-hop and corpus-level questions fail: no small set of chunks contains the answer |
| Knowledge graph | Multi-hop reasoning; corpus-level sensemaking | [[sources/HippoRAG]]: KG index + PageRank matches iterative retrieval at 10-30x lower cost; [[sources/GraphRAG]]: community summaries answer global questions top-k vector RAG structurally cannot | Significant upfront indexing cost; wasted if queries are single-hop |
| Temporal knowledge graph | Facts that change; provenance and supersession requirements | [[sources/Zep Temporal Knowledge Graph Memory]]: bi-temporal records with automatic fact invalidation, up to +18.5% on LongMemEval (vendor-reported) | Same indexing cost, plus schema commitment; overkill for static reference material |
| Agent-curated notes | An agent maintaining its own evolving understanding | [[sources/A-MEM]]: Zettelkasten-style notes with agent-decided links and retroactive evolution, gains across six models | Retroactive rewriting erases the original record — a provenance loss shared stores cannot afford |
| Relational / structured store | Typed facts with fixed schema needing exact filters, joins, aggregation | Thin in this vault; [[sources/Zep Temporal Knowledge Graph Memory]] integrating structured business data is the nearest evidence | Schema rigidity fights open-ended experience capture |

Two decision rules fall out. First, match substrate to query shape: single-hop recall tolerates vectors, multi-hop and global questions need structure, changing facts need time. Second, the substrate does not solve governance — provenance, write authority, and supersession policy sit above it (see [[concepts/shared agent memory]]).

## Benchmarks

- [[sources/LongMemEval]] is the de-facto reporting benchmark: 500 questions over scalable chat histories testing extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention. The update/abstention subtasks are the best available evidence for forgetting and supersession behavior; commercial assistants drop ~30% accuracy on sustained interactions.
- LoCoMo tests very long conversational memory across single-hop, temporal, multi-hop, and open-domain questions; no dedicated card yet, but [[sources/Mem0]] carries its headline results.
- BEAM stresses much longer conversational horizons (into the millions of tokens); no card yet.

Vendor scores on all of these come from vendors evaluating their own systems under differing setups — compare configurations before quoting deltas.

## Related

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

## Skills and Procedural Memory

- [[concepts/procedural memory]]
- [[sources/SAGE Skill Library]]
- [[sources/SkillRL]]
- [[sources/Voyager]]
