# Agent Memory Report: Compaction, Context, and Durable State

Date: 2026-07-05
Scope: local project graph only. Memory here includes persistent agent memory, compaction, retrieval, pruning, clearing, durable runtime state, handoff, skills, and learned procedures. Originally written 2026-06-01; this revision re-grounds every section against the rebuilt 471-source graph. Direct excerpts are intentionally short; longer source passages are summarized to stay within quotation limits. Embedded paper figures are local research crops; redraw or check rights before external distribution.

Shorter technical version: [[reports/Agent Memory Technical Brief]].

## Executive Summary

Agent memory is not one mechanism. The sources in this graph describe a layered architecture in which the model's active context, compacted context, persistent memory, retrieved evidence, durable workflow state, and reusable skills each solve a different part of the same problem: keeping an agent useful over time without flooding the next inference call. That vocabulary has a citable ancestry: [[sources/Cognitive Architectures for Language Agents|CoALA]] fixed the working/episodic/semantic/procedural memory split, and [[sources/MemGPT]] introduced the paged virtual-context design that today's persistent-agent products descend from.

The most consistent finding is that bigger context windows do not remove the need for memory, and the claim is now measured rather than asserted. Models degrade as input length grows even on trivial tasks, mid-context placement alone costs accuracy, and long-context assistants lose accuracy over sustained interactions ([[sources/Context Rot]], [[sources/Lost in the Middle]], [[sources/LongMemEval]]). Even the newest frontier release makes the point from the vendor side: Anthropic reports that Fable 5 stays focused across millions of tokens yet improves further when given persistent file-based memory ([[sources/Claude Fable 5 and Claude Mythos 5]]; vendor-reported). Evaluation of memory systems adds correctives: no single memory architecture dominates, effectiveness follows workload alignment ([[sources/Are We Ready For An Agent-Native Memory System]]), and for LLM-mediated memory the write path, not the read path, dominates lifecycle cost ([[sources/Agent Memory Characterization]]).

On the product side, compaction has moved from harness code into provider APIs: Anthropic and OpenAI both ship a native path, and the live axis between them is inspectability, an opaque encrypted item versus a readable compaction block with a pause hook ([[sources/OpenAI Codex Agent Loop]], [[sources/Claude API Compaction]]). Cloudflare treats compaction as the natural point to ingest session knowledge into a persistent memory profile. Google ADK separates durable workflow state from raw chat history. Cursor's posts emphasize the harness: dynamic context, summarization tradeoffs, learned rules. Manus and the Claude caching docs add the economic constraint underneath all of it: every context mutation has a cache price as well as a semantic effect, so production loops keep a stable prefix and an append-only tail ([[sources/Manus Context Engineering]], [[sources/Claude API Prompt Caching]]). Zep draws the boundary where file-based memory stops sufficing: changing facts, concurrent writers, and compliance regimes ([[sources/Zep Markdown Is Not Agent Memory]]). The newer memory stack also includes dreaming/sleep-time reflection, background jobs that consolidate memories outside the task loop, and shared memory stores with explicit write authority, optimistic concurrency, and versioned audit ([[sources/Claude Managed Agents Memory Stores]]).

Research sources sharpen the toolkit further: observation masking, task-aware pruning, optimized compressors and learned management policies, execution-state tree memory for long-horizon tasks ([[sources/MAGE Memory Execution State Management|MAGE]]), storage decoupled from retrieval ([[sources/Memora]]), agent-visible context dashboards with reversible archives ([[sources/VISTA Latent Context Managers]]), trajectory memory that pays off when grounded in external evaluation signals ([[sources/Reflexion]]), and constructive designs plus governance primitives for memory shared across agents ([[sources/G-Memory]], [[sources/Governed Shared Memory for Multi-Agent LLM Systems]]). Memory also raises the security stakes: a poisoned write outlives the turn that planted it, the attack surface maps onto the same write channels this report recommends, compaction ingestion and skill promotion included ([[sources/Memory Poisoning Attacks in LLM Agents]]), and malicious skills have already appeared at marketplace scale ([[sources/Koi Security ClawHavoc]]).

For a builder, the design rule is simple but demanding: decide what must be exact, what can be summarized, what can be re-fetched, what should persist across sessions, and what should never be written. Memory is a write-manage-read loop, not just a vector database. Compaction is a lossy transition, not a permanent memory strategy. Durable sessions are runtime state, not chat transcript replay. Skills are procedural memory, not just prompt text. And the write path is where both the cost and the risk concentrate, so provenance, review, and rollback belong there first.

## Core Model

The graph's sources converge on this decomposition:

```text
agent input at turn t =
  system/developer instructions
+ current user goal
+ recent high-value interaction history
+ compacted prior trajectory, if any
+ retrieved memory/evidence needed now
+ durable workflow state and artifact pointers
+ relevant skills/procedures

agent action =
  model(agent input at turn t)

memory update =
  filter, verify, classify, deduplicate, store, expire, or forget
  selected facts, decisions, preferences, task state, and lessons
```

In shorthand:

```text
C_t = I + G_t + R_t + K_t + retrieve(M_t, q_t) + compact(H_<t) + S_t
M_{t+1} = manage(M_t, write_candidates(H_t, artifacts_t, feedback_t))
```

`C_t` is the current context window. `M_t` is external memory. `H_t` is interaction history. `K_t` is durable runtime state such as workflow step, events, checkpoints, or artifacts. `S_t` is procedural memory such as skills and playbooks. The point of this formula is not that real systems literally implement this exact algebra; it is the architectural split that appears across the sources.

The type vocabulary in this split is CoALA's: working memory is the active context, while episodic, semantic, and procedural stores persist outside it, and memory operations are internal actions in their own right, the ancestor of the `manage(...)` line ([[sources/Cognitive Architectures for Language Agents|CoALA]]). The pattern of paging `M_t` in and out of a bounded `C_t` under the model's own control traces to [[sources/MemGPT]]. One thing the additive algebra abstracts away is ordering: cache pricing makes a stable prefix plus an append-only tail the cheap physical layout of `C_t`, so production systems order these terms rather than merely summing them ([[sources/Claude API Prompt Caching]], [[sources/Manus Context Engineering]]).

This also answers a recurring confusion: compaction does not store the mathematical representation of the model's intent in the way mechanistic interpretability papers study internal activations. The local sources describe summaries, compacted items, encrypted representations, dense state summaries, or external records. They are artifacts supplied back to later inference calls, not exposed neural hidden states. OpenAI's source is the closest to a latent representation claim because it says the compacted item can preserve prior state in an encrypted representation and Codex receives an opaque compaction item. Even there, the source presents it as an API-level continuation artifact, not as direct access to the model's internal activations, and the opacity is a provider design choice rather than a property of compaction: Anthropic's server-side path emits a readable text block with a pause hook for harness edits ([[sources/Claude API Compaction]]). The genuinely latent techniques sit in the model-internal bucket, which the survey literature now names latent memory ([[sources/Memory in the Age of AI Agents]]).

## Taxonomy of Techniques

Each row names what a technique stores or removes, when it fires, where it fits, and its main failure mode. The table carries citations only; the quantitative evidence behind each row lives in the product and research sections below. The newest rows cover dynamic tool discovery, recitation, agent-visible context dashboards, and execution-state tree memory, drawn from production harness practice and the June 2026 memory-systems wave.

| Technique | What It Stores or Removes | Trigger | Best Use | Main Risk | Key Sources |
|---|---|---|---|---|---|
| Active context | Current instructions, user request, recent messages, tool outputs | Every turn | Immediate reasoning | Context rot, cost, lost-in-middle | [[sources/Anthropic Effective Context Engineering]], [[sources/Cursor Improving Agent Harness]], [[sources/Context Rot]], [[sources/Lost in the Middle]] |
| Just-in-time retrieval | File paths, queries, references, selected source snippets | Need-driven | Large codebases and corpora | Bad query, missing hidden dependency | [[sources/Anthropic Effective Context Engineering]], [[sources/ContextBench]] |
| Dynamic tool discovery / tool-schema retrieval | Tool schemas held outside context, retrieved on demand | Need-driven, per task step | Large MCP tool ecosystems | Wrong tool routing; stale tool index | [[sources/MCP-Zero]], [[sources/ScaleMCP]] |
| Whole-transcript compaction | A summary or typed compaction block replacing older history | Token threshold or manual command | Long dialogue and decisions that cannot be re-fetched | Loss of exact details | [[sources/Anthropic Context Engineering Cookbook]], [[sources/OpenAI Codex Agent Loop]] |
| Provider-native compaction (opaque or inspectable) | API compaction items or blocks; opaque encrypted content (OpenAI) or inspectable text (Anthropic) | Server threshold or `/compact` | Long-running hosted agent loops | Opaque variants resist audit | [[sources/OpenAI Responses API Computer Environment]], [[sources/OpenAI Agents SDK Compaction Sessions]], [[sources/Claude API Compaction]] |
| Tool-result clearing | Drops old re-fetchable tool outputs while preserving call structure and a re-fetch pointer (URL or path) | Tool-result volume threshold | Bulky logs, reads, search results | Re-fetch cost; prefix-cache invalidation | [[sources/Anthropic Context Engineering Cookbook]], [[sources/Microsoft Agent Framework Harness Compaction]], [[sources/Manus Context Engineering]], [[sources/TokenPilot]] |
| Observation masking | Omits older environment observations | Turn/token/cost threshold | Coding agents with verbose outputs | Discards hidden clue | [[sources/The Complexity Trap]] |
| Recitation | A continuously rewritten plan file (todo.md) restated into recent context | Every turn on long tasks | Keeping the global plan in recent attention on long tool loops | Recitation drift | [[sources/Manus Context Engineering]] |
| Task-aware pruning | Keeps selected lines/tokens relevant to the current task | Before model call or compression pass | Code contexts where structure matters | Pruner misses a critical line | [[sources/SWE-Pruner]] |
| Optimized compression and learned management policies | Learned compressors for observations/history; learned policies for when, what, and how to compress | Long-horizon agent traces | Environment and coding tasks with repeated formats | Extra compressor overhead; training-dependent | [[sources/LLMLingua]], [[sources/ACON]], [[sources/SWE-MeM]] |
| Agent-visible context dashboard | Typed, addressable working-memory blocks with a reversible full-fidelity archive | Agent keep/archive decisions informed by per-block usage, recency, and budget stats | Long-horizon tool agents under context pressure | Agent mismanages its own state; dashboard overhead | [[sources/VISTA Latent Context Managers]] |
| Memory offload | Facts, preferences, decisions, events, instructions, tasks; substrates range from files and topic documents to abstraction-keyed entries and graphs | Explicit write, compaction, background ingestion, or self-directed paging | Cross-session persistence | Poisoning, staleness, over-recall | [[sources/MemGPT]], [[sources/Cloudflare Agent Memory]], [[sources/Memory for Autonomous LLM Agents]], [[sources/Memora]], [[sources/Infini Memory]] |
| Dreaming / consolidation | Reorganized memory stores, deduplicated memories, cross-session patterns, failure lessons | Scheduled job, session batch, compaction event, or post-run reflection | Improving memory quality between tasks | Overgeneralized or unreviewed memory updates | [[sources/Anthropic Managed Agents Dreaming Outcomes]], [[sources/Letta Code Memory Docs]], [[sources/Google ReasoningBank]] |
| Durable sessions | Explicit state schema, event history, checkpoints, artifact pointers | Every state transition | Workflows over days/weeks | State/schema drift | [[sources/Google ADK Durable Agents]], [[operations/durable sessions|operations/durable sessions]] |
| Execution-state tree memory | Root-to-current path, subgoal summaries, and branch hints in a hierarchical state tree | Every subgoal transition (Grow, Compress, Maintain, Revise) | Interdependent long-horizon tasks that semantic recall fragments | Wrong revision boundary discards valid work | [[sources/MAGE Memory Execution State Management|MAGE]] |
| Handoff | Fresh thread/agent seeded with extracted goal, files, and state | Thread becomes meandering or too long | Starting a cleaner work unit | Bad handoff omits tacit context | [[sources/Anthropic Effective Harnesses for Long-Running Agents]], [[sources/Amp Handoff]] |
| Procedural memory / skills | Reusable workflows, rules, instructions, examples; text playbooks and crystallized callable tools carry different cost and transfer profiles | Curation, feedback, user command, agent reflection, demonstration recording | Repeated work and organization-specific behavior | Bad rule compounds across runs; malicious skill supply chain | [[claims/Claim - Agent memory and skills create compounding improvement loops]], [[sources/Cognitive Architectures for Language Agents|CoALA]], [[sources/Comprehensive Survey on Agent Skills]], [[sources/Cursor Bugbot Learned Rules]], [[sources/LangSmith Context Hub]], [[sources/Metis]], [[sources/OpenAI Codex Record and Replay]] |
| Trajectory memory | Strategy, recovery, and optimization lessons from prior runs | Post-run analysis | Self-improving agents | False causal attribution; reflections ungrounded in external signals | [[sources/Reflexion]], [[sources/Trajectory-Informed Memory Generation]], [[sources/Agentic Context Engineering]] |
| Model-internal compression | Dense state summaries or soft/latent summaries inside inference | During reasoning/inference | Reducing KV/context cost in reasoning models | Less transparent; training-dependent | [[sources/MEMENTO]], [[sources/Prompt Compression Survey]] |

## What the Product Sources Say

### Anthropic: Separate Compaction, Clearing, and Memory

Anthropic's context engineering sources are the cleanest architectural split in the graph. The cookbook distinguishes three primitives: compaction, tool-result clearing, and memory. Its short version is that each handles a different growth mode: dialogue and reasoning growth, bulky re-fetchable tool outputs, and cross-session persistence.

In the Anthropic framing, compaction summarizes a conversation close to the limit and restarts with that compressed state. It is explicitly lossy. The cookbook calls compaction a whole-transcript operation: user messages, assistant messages, tool calls, tool results, and earlier compaction blocks all become summary material. The effective-context article describes Claude Code preserving architectural decisions, unresolved bugs, and implementation details while dropping redundant outputs. The same article also points to just-in-time context retrieval: Claude Code can put durable project instructions in files such as `CLAUDE.md`, then use glob, grep, shell commands, and file reads to pull only needed context at runtime.

The important builder lesson is that Anthropic does not treat memory as a synonym for compaction. Memory is persistent note-taking outside the context window. Clearing is not summarization; it removes old, re-fetchable tool outputs. Compaction is not exact recall; it preserves substance and continuity.

Since January 2026, compaction is also an Anthropic API feature, not only harness guidance. Server-side compaction (edit type `compact_20260112`) summarizes older conversation content into a compaction block when input tokens reach a configurable trigger, default 150,000 and minimum 50,000, moving compaction from harness-side code into the API itself ([[sources/Claude API Compaction]]). The design keeps developer choice intact: the compaction block is text, `pause_after_compaction: true` returns a `compaction` stop reason so the harness can adjust messages before continuing, and an `instructions` parameter fully replaces the default summarization prompt, the API-native version of compact-with-focus. Billing carries a subtlety: the compaction pass is a sampling iteration reported in `usage.iterations[]`, not in the top-level token counts.

Short source anchors: Anthropic calls context "finite" and recommends the "smallest possible" high-signal set of tokens. The cookbook says the primitives address a "different kind of context growth" and that lossiness is not binary.

Sources: [[sources/Anthropic Effective Context Engineering]], [[sources/Anthropic Context Engineering Cookbook]], [[sources/Claude API Compaction]].

### OpenAI: Codex Uses Native Compaction Items

OpenAI's Codex loop source shows the transition from text summaries to an API-native compaction endpoint. Early Codex compaction used `/compact` with custom summarization instructions and fed the resulting assistant summary back as the next input. The current source says the Responses API returns a compacted list of items and includes a special compaction item with opaque encrypted content that preserves latent understanding of the prior conversation.

The Responses API computer-environment article gives the higher-level version: long-running tool loops fill the context window, so the API can produce a compaction item that preserves key prior state in a token-efficient representation. The Agents SDK docs add a practical framework layer: `OpenAIResponsesCompactionSession` wraps a session backend, can compact automatically after turns, and can also be invoked manually during idle time because compaction can block streaming.

Compaction can be a provider feature, not just a prompt you write, and as of 2026 both major providers ship one. Inspectability changes by mode: a text summary is easy to audit, while an opaque compacted item may perform better or align with model training, but the harness cannot inspect its internal content.

Sources: [[sources/OpenAI Codex Agent Loop]], [[sources/OpenAI Responses API Computer Environment]], [[sources/OpenAI Agents SDK Compaction Sessions]].

### Cursor: Harness Context, Dynamic Retrieval, Learned Rules

Cursor's local sources are less a formal memory design than a harness engineering record. The harness post describes the context window as system prompt, tools, conversation state, and user request. It says Cursor moved from more static upfront context toward dynamic context that the agent fetches while working. It also describes experiments around summarizing at model-switch time, with the caution that summaries can lose important details in deep tasks.

Cursor is also represented by a production memory loop in Bugbot learned rules. Bugbot converts review feedback into learned rules that act as additional instructions in future runs. This is procedural memory: not "remember the whole session," but preserve a rule that changes future behavior. The source gives concrete scale: more than 110,000 repositories enabled learning and more than 44,000 rules had been generated at publication time.

The builder implication is that memory often enters through the harness. A coding assistant's memory may be a context fetcher, model-specific tool shape, learned rule store, summarizer at boundary events, and evaluation instrumentation, not a single memory API.

Sources: [[sources/Cursor Improving Agent Harness]], [[sources/Cursor Bugbot Learned Rules]], [[sources/Cursor Building Better Bugbot]].

### Cloudflare: Managed Memory as Ingestion and Retrieval

Cloudflare's Agent Memory source is the strongest product example of persistent memory as a service. It defines a memory profile with operations to ingest a conversation, remember a specific item, recall needed information, list memories, and forget a memory. The bulk ingest path is typically called when the harness compacts context.

Its ingestion pipeline is not just "embed and store." The article describes extraction, verification, classification, deduplication, provenance tracking, and storage. It classifies memory candidates into facts, events, instructions, and tasks, keeps line provenance, resolves relative dates to absolutes, checks extracted items against the source transcript, and supports supersession. Retrieval combines several channels: full-text search, exact fact-key lookup, raw message search, direct vector search, HyDE vector search, rank fusion, and synthesis.

This is close to a production blueprint. The memory service constrains the tool surface so the primary agent does not spend the task context designing storage queries. Its ingestion path also moves some storage work off the critical path; the asynchronous side is covered under Dreaming and Memory Consolidation.

Short source anchors: Cloudflare says agents should "recall what matters" and that memory should remain useful "as it grows."

Sources: [[sources/Cloudflare Agent Memory]], [[operations/agent memory|operations/agent memory]].

### Google ADK: Durable State Beats Raw Chat Replay

Google ADK's durable-agent source is a useful counterweight to transcript-centric thinking. It argues that long-running workflows fail when raw chat history becomes the state container. Instead, agents should use explicit durable state: current workflow step, progress, events, checkpoints, artifacts, and wakeup conditions.

This is memory in a broader runtime sense. The agent should not infer "where am I?" from a huge transcript after a week. It should read the workflow state. Separately, Google ADK's context compression docs describe sliding-window event compaction over session history, with interval, overlap, and summarizer settings. That makes compaction a workflow-history maintenance primitive, while durable state remains the authoritative operational record.

Sources: [[sources/Google ADK Durable Agents]], [[sources/Google ADK Context Compression]], [[operations/durable sessions|operations/durable sessions]].

### Cache Economics Constrain Memory Design

Every technique in this report mutates context, and every mutation has a cache price as well as a semantic effect. Manus states the metric plainly: KV-cache hit rate is "the single most important metric for a production-stage AI agent." The numbers explain why. Manus averages a roughly 100:1 input-to-output token ratio, a typical task takes about 50 tool calls, and cached input cost $0.30 per million tokens versus $3.00 uncached on Claude Sonnet at the time of writing, a 10x difference ([[sources/Manus Context Engineering]]; a single-team essay at mid-2025 pricing). Its techniques follow from the metric: Manus masks tool logits through a context-aware state machine instead of adding or removing tool definitions mid-loop, because changing the tool set invalidates the cache. It treats the file system as "the ultimate context" with restorable compression, dropping page content as long as the URL is kept so truncation never loses information irreversibly, rewrites a `todo.md` each turn to recite the global plan into recent attention, and leaves failed actions in context so the model can update its beliefs.

Anthropic's prompt-caching pricing generalizes the point beyond one team. Cache reads cost 0.1x base input while 5-minute cache writes cost 1.25x and 1-hour writes 2x, and the prefix hierarchy is tools, then system, then messages, so a tool-definition change invalidates everything downstream ([[sources/Claude API Prompt Caching]]). That pricing makes an append-only tail behind a stable prefix the cheap path and history rewriting the expensive one. The API has grown affordances for exactly this pattern: Opus 4.8 accepts mid-conversation system messages that add instructions without invalidating the cached prefix, and a `max_tokens: 0` request pre-warms a cache without sampling.

Claude Code is the harness-level demonstration. It orders every request as three layers, system prompt, project context (`CLAUDE.md` and auto memory), then conversation, so rarely-changing content comes first, and skills and plan mode deliberately append their instructions as conversation messages rather than editing the prefix ([[sources/Claude Code Prompt Caching]]). Compaction invalidates the conversation layer by design, but the summarization request itself shares the existing prefix and reads the cache, so generating the summary, not a cache miss, is the slow part. Rewinding is cheaper still: `/rewind` truncates back to a prefix that is already cached. The source's own framing is the right builder summary: compaction has runtime cost and cache consequences, not only semantic consequences.

Sources: [[sources/Manus Context Engineering]], [[sources/Claude API Prompt Caching]], [[sources/Claude Code Prompt Caching]].

### LangChain, Letta, and Context Repositories

LangSmith Context Hub turns context into a managed, versioned asset: instructions, policies, examples, skills, domain knowledge, and memories can live in a collaborative repository rather than being scattered through prompts. Deep Agents adds runtime machinery: a code interpreter that preserves state and decides what returns to the model, delta checkpoints to avoid quadratic history storage, and a context hub backend with durable `/memories/`.

Letta Code pushes the persistent-agent idea further. The local docs say the agent has durable identity, memory, configuration, messages, and state across conversations. It can self-edit memory, accept `/remember`, run sleep-time "dream" subagents, and use compaction events as reflection triggers. Its MemFS is a git-backed filesystem where some directories are loaded into the system prompt and others are visible through a tree. Letta descends directly from [[sources/MemGPT]], the 2023 paper that introduced OS-style virtual context management in which the LLM pages information between a bounded main context and external storage through its own function calls; the product's self-editing memory and dream subagents are that paging design carried into production.

These systems treat memory as a filesystem-like substrate and a versioned collaboration problem, not only as retrieval.

Sources: [[sources/LangSmith Context Hub]], [[sources/LangChain Deep Agents v0.6]], [[sources/Letta Code Memory Docs]], [[sources/MemGPT]].

### Zep: File Memory Has a Boundary

Zep supplies the boundary conditions the filesystem pattern needs. Its markdown critique concedes that markdown memory is legitimate, naming Manus's filesystem-as-context, Claude Code, and Letta's MemFS, for a single agent serving a single user with a local source of truth. It then pairs each gap with the capability a fix requires: retrieval at scale needs ranked retrieval that stays fast; changing facts need validity intervals and point-in-time queries; provenance needs each fact linked to its source; concurrent agents need reconciliation against source and timeline; and governance needs isolation, retention, and audit below the memory layer ([[sources/Zep Markdown Is Not Agent Memory]]). Its adoption rubric is four questions: how many agents and users share the memory, do facts change, can facts be re-derived from a local source, and is there a retention or compliance regime. It also punctures a common comfort: the markdown benefit that "a human can review it" is mostly theoretical, because the agent writes its own memory and the files are seldom read. Zep sells the temporal-graph alternative ([[sources/Zep Temporal Knowledge Graph Memory]]), so the boundary is drawn by an interested party, but the failure table stands on its own terms.

Zep's retrieval side is a production example of synthesizing only what the current turn needs. Smart Context Assembly retrieves across six context types (facts, entities, episodes, Observations, thread summaries, and the user summary) and ranks candidates from five of them simultaneously into a fixed 2,500-character budget, replacing fixed per-type quotas, so the block's shape adapts to each query and prompt sizes stay predictable across users and queries ([[sources/Zep Smart Context Assembly]]). Zep publishes the result as a measured exchange rather than a free win: one LoCoMo run traded 54% fewer tokens for about 8 points of accuracy, while a different run gained accuracy on fewer tokens.

Sources: [[sources/Zep Markdown Is Not Agent Memory]], [[sources/Zep Smart Context Assembly]].

### Dreaming and Memory Consolidation

Dreaming is one of the most important memory concepts in the graph because it changes where improvement happens. Ordinary memory writes happen during task execution: the agent notices something and writes it. Compaction happens at a context boundary: the agent or provider compresses prior context so work can continue. Dreaming happens outside the main work loop: a separate process reviews past sessions and memory stores, then produces a cleaner or richer memory state for future sessions.

Anthropic Managed Agents is the clearest product source. Its article describes dreaming as a scheduled process that reviews agent sessions and memory stores, extracts patterns, and curates memories so agents improve over time. The docs are more precise: a dream is an asynchronous job that takes a pre-existing memory store plus 1 to 100 session transcripts, then produces a separate output memory store. The input store is not modified. This makes dreaming reviewable: teams can inspect the output store, attach it to future sessions, or discard it.

The memory stores that dreaming reads and writes are themselves the graph's most concrete shared-memory design. A store is a workspace-scoped collection of documents mounted at `/mnt/memory/<slug>/` in the session sandbox, attached via `resources[]` at session creation only, with `read_write` (the default) or `read_only` access enforced at the filesystem level ([[sources/Claude Managed Agents Memory Stores]]). The limits are explicit: at most 8 stores per session, 2,000 memories per store, 100 kB (about 25k tokens) per memory, and per-store instructions capped at 4,096 characters. Concurrent writers resolve through optimistic concurrency, a `content_sha256` precondition on updates, and every mutation creates an immutable version attributed to the writing session; the audit, redaction, and prompt-injection implications are covered under Safety and Governance.

The practical formula is:

```text
dream(input_memory_store, session_transcripts, instructions)
  -> output_memory_store

output_memory_store =
  merge duplicates
+ replace stale or contradicted entries
+ add new cross-session insights
+ reorganize memory for future retrieval
```

This is not just another compaction prompt. Compaction asks "what should survive into the next context window?" Dreaming asks "what should the agent learn after reviewing many traces?" The answer may include patterns a single session cannot reveal: recurring mistakes, converged workflows, team-level preferences, filetype workarounds, tool-specific patterns, or procedures that should become skills.

Letta Code has a parallel idea under sleep-time reflection. Its docs say Letta launches periodic dream subagents in the background to reflect on recent conversations and edit memory. The recommended MemFS trigger is a compaction event, which is an important pattern: compaction is the moment the system knows a session has generated enough material to justify consolidation.

Google ReasoningBank is the research-side analogue. It runs a closed loop of retrieval, extraction, and consolidation. After an agent acts, it self-assesses the trajectory and extracts success insights or failure reflections into structured reasoning memories. ReasoningBank matters because it emphasizes failures, not only successful workflows: a failed trajectory can become a preventative lesson. The consolidation lineage is older: [[sources/Generative Agents]] introduced reflection, synthesizing a memory stream into higher-level inferences, and the recency/importance/relevance retrieval scoring most agent memory scorers reuse, with the caveat that its evidence is behavioral believability in a social simulation, not task performance. The pattern is reaching procedural memory too: [[sources/SkillOpt]]'s repository previews SkillOpt-Sleep, a nightly offline self-evolution companion for local coding agents. It is an implementation preview rather than an evaluated result, but it applies the same consolidate-outside-the-loop idea to skills.

Cloudflare Agent Memory also points in this direction, though more cautiously. Its current article describes asynchronous vectorization after ingestion and says Cloudflare is testing strategies for memory storage to improve asynchronously, explicitly analogizing the direction to sleep-time consolidation. That makes Cloudflare a near-adjacent source rather than a full dreaming implementation source.

Builder implications:

- Treat dreaming as a background memory-maintenance job, not as online retrieval.
- Keep the input store immutable and produce a new output store so review and rollback are possible.
- Run it on batches of sessions, especially after compaction, task completion, or repeated failures.
- Give it instructions about what to focus on and what to ignore.
- Extract both positive procedures and negative lessons from failures.
- Ground extracted lessons in test results or environment feedback before promotion ([[sources/Reflexion]]).
- Preserve chronological cues during consolidation ([[sources/Are We Ready For An Agent-Native Memory System]]).
- Require provenance back to source sessions before promoted memories affect high-authority actions.
- Promote stable repeated procedures into skills only after evaluation.

Sources: [[sources/Anthropic Managed Agents Dreaming Outcomes]], [[raw/docs/anthropic-managed-agents-dreams-docs|Anthropic Managed Agents dreams docs]], [[sources/Claude Managed Agents Memory Stores]], [[sources/Letta Code Memory Docs]], [[sources/Google ReasoningBank]], [[sources/Generative Agents]], [[sources/Cloudflare Agent Memory]], [[maps/Recent Agent Operating Concepts]], [[maps/Harness Tracker]].

### Procedural Memory and Skills

The skills cluster fills a gap that ordinary memory stores do not: it packages reusable know-how into files, scripts, references, and assets that can be discovered and loaded only when relevant. The local [[maps/Agent Skills Map]] calls skills the reusable procedural-knowledge layer for agents. The academic anchor is [[sources/Comprehensive Survey on Agent Skills]], which treats skills as reusable procedural artifacts and organizes the literature around a four-stage lifecycle of representation, acquisition, retrieval, and evolution; that lifecycle is the write-manage-read loop applied to procedures. This is memory, but not memory as "facts the user said." It is memory as reusable procedure.

The standard/source cards converge on a progressive-disclosure pattern. A skill has a small discoverable description loaded early, while detailed instructions, scripts, references, and assets are loaded only after activation. That makes skills a context-management technique as much as a capability mechanism: the agent can carry a large library of procedures without stuffing all of them into every prompt. The pattern is cross-vendor product status: GitHub Copilot supports skills across its cloud agent, CLI, and VS Code agent mode, and Microsoft Agent Framework ships file-based and code-defined skills with load/read/run tooling and explicit security guidance ([[sources/GitHub Copilot Agent Skills Docs]], [[sources/Microsoft Agent Framework Skills Docs]]).

The research sources add cautions. [[sources/SkillsBench]] treats skill utility as something to benchmark, not assume. [[sources/Agentic Skills in the Wild]] emphasizes realistic skill retrieval from larger collections, where benefits degrade if the agent cannot choose the right skill. [[sources/SAGE Skill Library]], [[sources/SkillRL]], and [[sources/Voyager]] show the more ambitious version: skill libraries become evolving state, generated, validated, reused, and improved across tasks. [[sources/SkillOpt]] is the disciplined-optimizer form of that ambition: it treats the skill document as trainable external state, proposes bounded add/delete/replace edits, and accepts a candidate only when held-out validation improves, keeping rejected edits in a buffer, reporting best or tied-best performance on all 52 evaluated model/benchmark/harness cells, with Codex-trained skills transferring into Claude Code. [[sources/Metis]] adds the controlled study behind the promotion decision: isolating text memory and code memory over an identical set of experiences shows complementary tradeoffs in construction cost, execution efficiency, and transferability, so Metis crystallizes recurring plans into validated callable tools only when repeated reuse justifies the tool-generation cost, improving AppWorld task accuracy by up to 20.6% over ReAct while reducing execution cost by up to 22.8%.

The write paths for procedural memory are also multiplying. Cursor's Bugbot converts review feedback into rules ([[sources/Cursor Bugbot Learned Rules]]); OpenAI's Record & Replay converts a demonstrated macOS workflow into a skill. The user performs the workflow once, and Codex inspects the capture and drafts an inspectable, editable `SKILL.md` that explains when to use the workflow, what inputs it needs, what steps to follow, and how to verify the result ([[sources/OpenAI Codex Record and Replay]]). Demonstration recording fits the governance stance below because the generated skill is reviewable and refinable before reuse.

For builders, skills should be governed like dependencies. They can include executable scripts and injected instructions, so they need review, versioning, tests, provenance, and removal paths; GitHub CLI now ships install, publish, and update workflows for Agent Skills with versioning and provenance, a package-manager-style answer to that requirement ([[sources/GitHub CLI Manage Agent Skills]]). The failure mode is not only "bad memory recall"; it is a stale or unsafe procedure being invoked with authority, a risk that has already appeared at marketplace scale ([[sources/Koi Security ClawHavoc]]).

Sources: [[sources/Anthropic Agent Skills]], [[sources/Agent Skills Specification]], [[sources/OpenAI Skills Docs]], [[sources/OpenAI Codex Record and Replay]], [[maps/Agent Skills Map]], [[sources/Comprehensive Survey on Agent Skills]], [[sources/SkillsBench]], [[sources/Agentic Skills in the Wild]], [[sources/SkillOpt]], [[sources/Metis]].

### Handoff Instead of More Compaction

The graph also includes sources arguing that compaction is not always the right boundary. Amp's handoff article says they removed compaction and replaced it with handoff into a fresh goal/thread. Anthropic's long-running harness source similarly uses an initializer agent, a coding agent, progress files, and git history so a fresh context can resume work from artifacts rather than from a repeatedly summarized thread.

This is an important pattern: sometimes the correct memory artifact is not a smaller chat history. It is a clear new goal plus files, branch state, progress notes, and tests. Cache economics give the boundary choice a cost dimension as well: compaction rebuilds the conversation cache around a new summary, handoff starts a fresh prefix seeded from artifacts ([[sources/Claude Code Prompt Caching]]).

Sources: [[sources/Amp Handoff]], [[sources/Anthropic Effective Harnesses for Long-Running Agents]].

## What the Research Sources Add

### Survey Framing: Memory as Write-Manage-Read

The local survey [[sources/Memory for Autonomous LLM Agents]] formalizes memory as a write-manage-read loop tied to the agent's perception and action cycle. It separates temporal scope, representation substrate, and control policy. The mechanisms it surveys include context-resident compression, retrieval stores, reflective self-improvement, hierarchical virtual context, and learned memory management.

Its most useful warning is that the update step is not append-only. Good memory systems summarize, deduplicate, score priority, resolve contradictions, and delete. This matches Cloudflare's production pipeline and the project's own [[operations/agent memory|agent memory operation note]], which warns about memory poisoning and recommends provenance, write authority, expiration, review gates, and separation between trusted long-term memory and untrusted retrieved content.

The vocabulary's origins, [[sources/Cognitive Architectures for Language Agents|CoALA]]'s memory-type split and [[sources/MemGPT]]'s paged virtual context, are covered in the Core Model and Letta sections. [[sources/Memory in the Age of AI Agents]], a 47-author survey, widens the frame with a taxonomy of forms (token-level, parametric, latent memory), functions (factual, experiential, working memory), and dynamics (formation, evolution, retrieval); the forms axis gives this report's model-internal bucket a citable name, latent memory. It also delineates agent memory from LLM memory, RAG, and context engineering, and names multi-agent memory an emerging research frontier.

Sources: [[sources/Memory for Autonomous LLM Agents]].

### Memory as Measured Infrastructure

[[sources/Agent Memory Characterization]] profiles ten memory systems along four axes (construction, storage, retrieval, mutability). On 1.8M tokens of history and 300 queries, construction wall time runs from under a minute for deterministic indexing (BM25, embedRAG) to about 3.9 hours (SimpleMem) and 13.3 hours (Letta), and end-to-end energy spans more than 26.7x. Normalized by correct answers, LLM-mediated systems such as A-MEM and MIRIX carry a 28-47x energy premium over flat BM25 retrieval, and the per-correct-answer spread across the suite exceeds 47x; the premium must be justified by capabilities flat retrieval cannot provide: mutation, conflict resolution, multi-type routing, or long-range reasoning. Construction energy dominates the lifecycle, and agentic stores scale super-linearly as each ingestion re-reads a growing store. The write path, not the read path, is the expensive half of memory.

[[sources/Are We Ready For An Agent-Native Memory System]] adds multi-workload evaluation: 12 memory systems and two baselines across five workloads spanning 11 datasets, with the caveat that some authors are affiliated with MemTensor, the vendor behind the evaluated MemOS system. No single architecture dominates; effectiveness depends on how well the memory structure aligns with the workload bottleneck, the empirical grounding for the failure-mode-first builder guidance below. Its sharpest caution: on time-dependent queries, raw long-context retrieval still outperforms most memory-backed approaches, because standard semantic consolidation destroys crucial chronological cues.

### Memory Substrates: What Graph Structure Buys

Substrate choice is workload-dependent. [[sources/GraphRAG]] anchors the corpus end: global sensemaking questions over whole corpora in roughly the 1M-token range structurally defeat top-k vector retrieval, because no small set of chunks contains the answer, and an entity graph with community summaries wins on comprehensiveness and diversity, at the price of significant upfront indexing cost and an LLM-judged rather than exact-match evaluation. [[sources/HippoRAG]] shows a graph index can also replace an iterative retrieval loop: single-step graph traversal matches or beats iterative retrieval (IRCoT) on multi-hop QA while 10-30x cheaper and 6-13x faster at query time; combining the two yields further gains, so substrate and control policy compose rather than compete. Its evidence comes from multi-hop QA corpora, not conversational agent memory.

[[sources/A-MEM]] (NeurIPS 2025) holds the midpoint: agent-curated structured notes with dynamic link generation, where the agent rather than a fixed schema decides the graph structure, at the price of retroactive rewriting that erases the original record, a provenance tradeoff taken up in Safety and Governance. [[sources/Zep Temporal Knowledge Graph Memory]] contributes the temporal point: a bi-temporal graph recording when a fact became true and when it stopped being true, with automatic invalidation and episode-level provenance. The counterweight is [[sources/Mem0]]: its graph variant (Mem0-g) adds only about 2% over the base vector configuration on conversational QA, so extraction quality matters more than graph structure for conversational recall. Zep and Mem0 evaluate their own products.

### Memory Representation: Decoupling Storage from Retrieval

[[sources/Memora]] (Microsoft Research; reported as ICML 2026 work) separates what is stored from how it is retrieved. Each entry pairs a primary abstraction, a short phrase of 6-8 words that alone is embedded for similarity search, with a rich memory value never retrieved by its own content, plus cue anchors as alternative access paths; a policy-guided retriever iteratively refines the query, expands through cue anchors, and decides when to stop. It reports 86.3% LLM-judge accuracy on LoCoMo and 87.4% on LongMemEval, outperforming RAG, Mem0, Nemori, Zep, LangMem, and even full-context inference in its own configuration (memory-system scores are not comparable across papers; see Open Questions), with up to 98% fewer context tokens and roughly half the memory entries per conversation that Mem0 stores (344 vs 651). [[sources/Infini Memory]] takes the document-structured position: topic documents as semantic units, buffered writes with periodic consolidation, and agentic retrieval through iterative tool calls (64.7% overall on MemoryAgentBench), avoiding a mandatory dependency on vector or graph databases. It is the research counterpoint to [[sources/Zep Markdown Is Not Agent Memory|Zep's markdown critique]], covered with the product sources.

### Execution-State Memory: The Research Case for Durable State

[[sources/MAGE Memory Execution State Management]] gives Google ADK's durable-state argument a research grounding. Semantic-similarity organization mismatches execution-state dependencies, fragmenting decision trajectories and mixing valid and erroneous traces; the paper cites the counter-intuitive benchmark pattern that memory systems often fail to improve long-horizon performance and sometimes underperform simply retaining the full history in context. MAGE manages a hierarchical state tree instead: the agent's state is the active root-to-current path, maintained by Grow (record new traces), Compress (summarize completed subgoals), Maintain (validate summaries), and Revise, which restores a target boundary and resumes on a new branch, excluding the erroneous segment while keeping valid progress. On MemoryArena it improves average task success by 7.8-20.4 percentage points over long-context and memory baselines while reducing token consumption by 55.1%. Recall-oriented conversation favors extraction systems; interdependent execution favors state trees.

### Length and Position Degrade Performance

The taxonomy names context rot and lost-in-middle as active-context risks; both now carry their canonical citations. [[sources/Context Rot]], the Chroma report that coined the term, tested 18 models across 4 organizations and found all 18 degrade as input length grows, even on trivial tasks. Focused prompts of about 300 tokens of relevant content consistently beat full prompts of about 113k tokens on LongMemEval comparisons across every model family, the direct quantitative case for retrieval and compaction over dumping everything in. One topically similar distractor lowers accuracy and four compound it, and models perform better on shuffled haystacks than logically coherent ones. Chroma sells a retrieval database, so the conclusion favors its business; the cross-vendor dataset is nonetheless the strongest length-degradation evidence available. [[sources/Lost in the Middle]] (TACL 2024) documents the position mechanism: U-shaped performance in which mid-context placement alone drops multi-document QA accuracy by roughly 20 or more points, measured on 2023-era models. Length and position together are the empirical anchor for the "smallest possible" high-signal framing quoted earlier.

[[sources/LongMemEval]] extends the evidence to persistent memory: on its 500 questions over scalable chat histories, commercial chat assistants and long-context LLMs show a 30% accuracy drop across sustained interactions. Its three-stage memory design space of indexing, retrieval, and reading is the research analogue of Cloudflare's multi-channel retrieval pipeline, and its knowledge-update and abstention subtasks make it double as a supersession and forgetting benchmark.

### Observation Masking: Cheap Baseline Before Smart Summaries

The Complexity Trap is a critical corrective for agent memory design. It finds that in software-engineering agents, environment observations dominate context. The paper's figure reports observation tokens at about 84% of an average raw agent turn in its preliminary analysis ([[sources/The Complexity Trap]]). Its experiments compare raw history, observation masking, LLM summarization, and a hybrid strategy.

The practical lesson is not that summarization is bad. It is that many agent traces are bloated by tool observations, not by irreplaceable reasoning. If the old observation can be safely omitted or re-fetched, masking or clearing may match summarization at lower complexity and cost.

![[reports/assets/agent-memory/complexity-observation-token-distribution.png]]

Figure 1. Observation tokens dominate an SE agent trajectory. Source crop from [[sources/The Complexity Trap]].

![[assets/agent-memory-context-figures/complexity_fig2_efficiency_tradeoff.png]]

Figure 2. The Complexity Trap compares solve rate against cost for raw context, observation masking, and LLM-summary strategies. Source crop from [[sources/The Complexity Trap]].

### Parallel Compaction: Compaction as Serving Architecture

[[sources/Parallel Context Compaction]] treats compaction as a runtime bottleneck. Instead of one blocking summarizer over a full accumulated trajectory, it divides the context into target blocks and summarizes them concurrently before merging them. This matters for long-horizon serving because compaction can otherwise become a latency spike at exactly the point where the agent is already near a context boundary.

The broader lesson is that compaction design has systems knobs: block size, overlap, merge policy, summary budget, trigger threshold, prompt-cache continuity, and whether compaction runs during agent idle time. This complements OpenAI's SDK warning that automatic compaction can block streaming.

The cache knob now has direct evidence. [[sources/TokenPilot]] identifies a tradeoff between text sparsity and prompt cache continuity: pruning and eviction that mutate the sequence layout introduce prefix mismatches and cache invalidation. Its answer is ingestion-aware compaction that stabilizes prompt prefixes, plus lifecycle-aware eviction on a conservative batch-turn schedule that offloads segments only when task relevance expires, reporting cost reductions of 61% and 56% in isolated mode and 61% and 87% in continuous mode on PinchBench and Claw-Eval. It ships inside LightMem2.

![[assets/agent-memory-context-figures/parallel_fig1_sequential_parallel_compaction.png]]

Figure 3. Sequential versus parallel context compaction. Source crop from [[sources/Parallel Context Compaction]].

### ACON: Optimize the Compressor Against Agent Failures

[[sources/ACON]] treats context compression as an agent-specific optimization problem. It compresses both environment observations and interaction histories. Its key method is failure-driven guideline optimization: compare trajectories where full context succeeds but compressed context fails, analyze why, and update the natural-language compression guideline. The paper then distills the optimized compressor into smaller models to reduce overhead.

The front-page figure shows a better accuracy and token tradeoff than naive LLM prompting across GPT-4.1, GPT-4.1-mini, and Qwen3-14B distilled settings. The important idea is that "compress this conversation" is too generic; the compressor should be trained or tuned on the actual failure modes of the agent and environment.

[[sources/SWE-MeM]] moves the learning one level up: instead of optimizing the compressor, it trains the memory-management policy itself. A flexible memory tool lets the agent decide when, what, and how to compress from trajectory state, task progress, and remaining context budget, trained with Memory-aware GRPO to jointly optimize memory management and issue resolution. It reports 43.4% and 60.2% resolve rates on SWE-Bench Verified with 4B and 30B models, and its explicit critique target is the fixed token-threshold compaction trigger most harnesses use by default.

![[reports/assets/agent-memory/acon-accuracy-peak-tokens.png]]

Figure 4. ACON improves the accuracy/peak-token tradeoff on AppWorld. Source crop from [[sources/ACON]].

### Where Context Control Lives

Context-management control can sit in harness-side rules (The Complexity Trap's masking), in learned policies (ACON, [[sources/SWE-MeM]]), or in the model itself. [[sources/VISTA Latent Context Managers]] argues the third location needs no training: frontier models are proprioceptively blind to their own context, and the missing piece is an interface exposing that state. Its training-free layer represents working memory as typed, addressable blocks with a dashboard of per-block token usage, recency, access history, and remaining budget, and archives blocks as recoverable full-fidelity payloads rather than one-way summaries. On LOCA-Bench, already in this report's eval matrix, it improves four backbones and lifts Gemini-3-Flash from 22.7 to 50.7%, with the lift growing under context pressure; ablations confirm the dashboard matters beyond the archive and recovery tools. Reversibility is the transferable lesson: a recoverable archive changes what counts as safe eviction.

### SWE-Pruner: Prune Code with Task-Aware Structure

SWE-Pruner addresses a different failure mode: general-purpose token compression can break code semantics. The lineage under critique has a canonical paper: [[sources/LLMLingua]] (EMNLP 2023) pairs a budget controller with token-level iterative compression that models the interdependence between compressed contents, reporting up to 20x compression with little performance loss in single-prompt settings; task-aware pruners like SWE-Pruner and agent-tuned compressors like ACON define themselves against that general-purpose approach. SWE-Pruner instead trains a small neural skimmer to select relevant lines based on the current task and an explicit pruning goal. Its results report substantial token reductions while preserving or improving success rates: 23-38% on SWE-Bench Verified-style agent runs and up to 54% across broader agent-task settings in the paper ([[sources/SWE-Pruner]]).

This belongs in memory architecture because coding agents often use "memory" to mean "what source code and logs should be in the next prompt." For code, exact lines and structural integrity matter. A good pruning system should preserve enough syntax, dependencies, and implementation detail for action, not merely produce a fluent summary.

![[reports/assets/agent-memory/swe-pruner-efficiency.png]]

Figure 5. SWE-Pruner reduces prompt/completion/total tokens and agent rounds in the paper's front-page analysis. Source crop from [[sources/SWE-Pruner]].

### ContextBench: Retrieval Quality Is a Memory Problem

[[sources/ContextBench]] evaluates context retrieval in coding agents at file, block, and line granularity. The related [[sources/Letta Context-Bench]] article frames agentic context engineering as the agent's ability to decide what to retrieve and load. The benchmark's radar plots compare precision, recall, and F1 across coding agents and LLMs.

The lesson for memory design is that recall and precision must be measured at the artifact granularity the agent acts on. A memory system that retrieves the right file but not the right line can still fail. A system that retrieves many loosely related artifacts can create context saturation.

![[reports/assets/agent-memory/contextbench-retrieval-radar.png]]

Figure 6. ContextBench retrieval performance across file, block, and line metrics. Source crop from [[sources/ContextBench]].

### MEMENTO and Soft/Internal Compression

The [[sources/Prompt Compression Survey]] (NAACL 2025) supplies the organizing axis for this bucket: hard-prompt methods filter or paraphrase text, the small-window family of [[sources/LLMLingua]] and kin, superseded in agent practice by task-aware pruning ([[sources/SWE-Pruner]]) and learned compaction ([[sources/ACON]]) covered above, while soft-prompt methods compress into special tokens or embeddings, where MEMENTO sits. Its documented challenges, compressor overfitting and long compression time, are the research-side statement of the training-dependent risk this report's taxonomy lists.

MEMENTO is the main source in the graph for model-internal context management. It trains reasoning models to segment long reasoning traces into blocks, compress each block into a memento, and continue while attending to mementos rather than the full earlier trace. The paper reports about 2.5x peak KV cache reduction and 1.75x throughput improvement in its setup ([[sources/MEMENTO]]). It also notes a dual information stream: text mementos plus corresponding KV states.

This is the closest technique to a "mathematical representation" of prior reasoning, but it is still not the same as a user-level memory entry. It is a trained inference mechanism that changes what the model attends to and retains in KV state. Builders should place it in a separate bucket from external memory stores and chat compaction summaries.

![[reports/assets/agent-memory/memento-overview.png]]

Figure 7. MEMENTO data generation, attention pattern, and efficiency results. Source crop from [[sources/MEMENTO]].

### Trajectory Memory and Evolving Playbooks

The reflection-into-memory pattern begins with [[sources/Reflexion]] (NeurIPS 2023): self-reflections stored as text in an episodic memory buffer and prepended to later attempts, reaching HumanEval pass@1 of 91% versus 80% for base GPT-4. Its ablations carry the load-bearing condition: gains depend on the quality of the external evaluation signal, such as unit tests or environment reward, so reflective memory pays off when grounded in external feedback, not free-floating introspection. ReasoningBank and the sources below are its descendants.

Trajectory-Informed Memory Generation argues that useful memory can be extracted from execution paths, not just facts. It generates strategy tips from clean successes, recovery tips from failure handling, and optimization tips from inefficient successes. It also tracks provenance from each lesson back to the source trajectory. This matches the project's claim that memory and skills create compounding improvement loops.

Agentic Context Engineering treats context as an evolving playbook. Its core warning is "context collapse": repeated rewriting can erase useful details over time. Its alternative is structured incremental updates, reflection, and curation. This is directly relevant to compaction: if every compaction rewrites the whole memory into a shorter document, the system can drift toward a polished but less useful summary.

![[assets/agent-memory-context-figures/trajectory_memory_fig1_overview.png]]

Figure 8. Trajectory-informed memory extracts tips from execution traces, stores and consolidates them, then retrieves them for later tasks. Source crop from [[sources/Trajectory-Informed Memory Generation]].

Sources: [[sources/Trajectory-Informed Memory Generation]], [[sources/Agentic Context Engineering]], [[sources/Reflexion]], [[claims/Claim - Agent memory and skills create compounding improvement loops]].

### Retrieve or Think

To Retrieve or To Think? adds a control-policy point. Retrieval is not always beneficial. The paper frames context evolution as a decision between acquiring external evidence and reasoning over existing context. This matters for memory systems because automatic recall on every turn can saturate the prompt with stale or irrelevant memories. The agent should retrieve when it has an information gap, not as a ritual.

![[assets/agent-memory-context-figures/ace_fig1_retrieve_or_think_loop.png]]

Figure 9. Retrieve-or-think routing: agents vote whether to retrieve external context or reason over the current context. Source crop from [[sources/To Retrieve or To Think]].

Sources: [[sources/To Retrieve or To Think]].

### Shared Memory Across Agents

Multi-agent memory now has constructive designs to set against the shared-false-memory failure mode in [[sources/When Agents Misremember Collectively]]. [[sources/G-Memory]] organizes team memory as a three-tier hierarchy of insight, query, and interaction graphs, propagating cross-trial lessons team-wide while keeping each agent's memory customized. It improves embodied-action success by up to +20.89% and knowledge-QA accuracy by up to +10.12% across five benchmarks, three LLM backbones, and three MAS frameworks with no framework modifications; the gains are on simulated benchmarks, with no production evidence yet.

[[sources/Governed Shared Memory for Multi-Agent LLM Systems]] supplies the governance model: four named failure modes (unauthorized leakage, stale propagation, contradiction persistence, provenance collapse) matched by four primitives (scoped retrieval, temporal supersession, provenance tracking, policy-governed propagation), implemented in MemClaw, a production multi-tenant memory service. Its ArgusFleet harness reconstructed 100% of depth-four derivation chains with correct writer identity at sub-second per-hop latency, showed zero cross-fleet leakage, and surfaced real scope-enforcement and ordering bugs. The evaluation covers only the authors' own service, so treat it as the sharpest available model rather than a validated solution.

### Evaluating Compaction by Continuation, Not Similarity

Factory's context-compression evaluation source argues that summary similarity metrics miss the real issue: can the agent continue the task? It evaluates compressed context through probes about artifacts, continuity, context awareness, accuracy, completeness, and instruction following. It also compares styles: structured persistent summaries, opaque high-compression approaches, and detailed regenerated summaries.

The report's builder lesson is important: compression ratio is not the goal. Good compaction preserves what later action needs. Weak compaction often loses artifact trails, exact decisions, and next steps even if the summary reads well. The small-window compression era (LLMLingua and kin; survey: [[sources/Prompt Compression Survey]]) headlines compression ratio as its success metric; those sources enter this report as baselines and vocabulary, not as evaluation methodology.

Sources: [[sources/Factory Context Compression Evaluation]], [[claims/Claim - Context management is an agent architecture choice]].

## Similarities and Differences Across Providers

| Provider / System | Similarity to Others | Distinctive Move |
|---|---|---|
| Anthropic / Claude Code | Treats context as a finite resource; uses compaction and retrieval | Cleanest public split between compaction, clearing, and memory; emphasizes prompt tuning for compaction |
| OpenAI / Codex | Compacts long-running agent loops near thresholds | Provider-native compacted item; opaque encrypted continuation artifact; Agents SDK session wrapper |
| Cursor | Treats context as harness design and evaluates changes empirically | Dynamic context over static upfront context; learned rules for Bugbot; model-specific harness/tool adaptation |
| Manus | Treats context as harness design and iterates on it in production | KV-cache hit rate as the governing metric; logit masking instead of mid-loop tool removal; filesystem as restorable external context |
| Cloudflare Agent Memory | Uses compaction boundary to preserve session knowledge | Managed memory profile with constrained remember/recall/forget/list API and multi-channel retrieval |
| Zep | Treats memory as a managed ingestion/retrieval service, like Cloudflare | Temporal knowledge graph with validity intervals, fact-level provenance, and point-in-time queries; explicit boundary rubric for when file memory stops sufficing |
| Google ADK | Supports context compression | Separates durable workflow state from raw transcript; state schema is the source of truth |
| Anthropic Managed Agents | Adds memory stores and session traces to a managed runtime | Dreaming jobs consolidate memories between sessions into a reviewable output store; shared workspace-scoped stores with read-only/read-write authority, optimistic concurrency, and versioned audit history |
| LangChain / Letta | Externalizes memory into filesystem/repository abstractions | Versioned context hub, MemFS, dream/reflection workflows, durable agent identity |
| Amp / long-running harnesses | Recognize compaction lossiness | Prefer handoff, artifacts, progress files, and fresh contexts for some work |

Common patterns:

- Every serious source treats context as scarce or at least easily polluted.
- Compaction is lossy and must be tuned or evaluated.
- Compaction is moving from harness code into provider APIs: Anthropic and OpenAI both now ship a native path.
- Retrieval should be selective.
- Durable state should live outside the model context.
- Dreaming/consolidation is a write-side maintenance process, not a replacement for online context retrieval.
- Memory writes need governance: provenance, review, deletion, and contradiction handling.
- Procedural memory is becoming as important as factual memory.

Differences:

- Provider-native compaction no longer distinguishes OpenAI: Anthropic ships a server-side compaction path in the API as well ([[sources/Claude API Compaction]]). The live axis is inspectability. OpenAI's compacted item is opaque and can be encrypted; Anthropic's compaction block is readable text, with a pause-after-compaction hook that lets the harness adjust messages before continuing.
- Anthropic's public materials still emphasize explicit developer choice among compaction, clearing, and memory; the native path adds a managed default without collapsing that choice.
- Zep draws the boundary of the file pattern with an explicit adoption rubric ([[sources/Zep Markdown Is Not Agent Memory]]); its answer past the boundary is a temporal knowledge graph, which Zep sells, so the argument carries a vendor motivation.

## Safety and Governance

Memory raises the stakes of prompt injection because a poisoned write can persist after the malicious content has left the active window. The local [[operations/agent memory]] note is direct: a bad instruction, false fact, poisoned preference, or malicious tool note can silently shape future planning, retrieval, or delegation. In other words, memory turns a one-turn contamination into a durable state problem.

The safety sources split the threat surface into several layers. [[sources/Agent Security Bench]] includes memory poisoning alongside prompt injection, backdoor-style attacks, and mixed attacks. [[sources/AgentDojo]], [[sources/InjecAgent]], and [[sources/BrowseSafe]] focus on indirect prompt injection through tools, external documents, and browser environments. [[sources/Design Patterns for Securing LLM Agents]] connects those attacks to implementable controls around privilege, tool boundaries, and isolation. [[sources/When Agents Misremember Collectively]] adds a multi-agent memory risk: agents can reinforce shared false memories, especially when social influence or shared memory makes wrong claims look corroborated.

[[sources/Memory Poisoning Attacks in LLM Agents]] gives the memory half its systematic treatment. It maps six attack classes onto four memory write channels: explicit instruction-executed write, system prompt-driven write, compaction-driven write, and experience-to-procedure. The last two are the ingestion and skill-promotion paths this report recommends elsewhere. Its MPBench results quantify the capability-security tension: the more aggressive of its two test agents averaged 66.67% attack success versus 34.25% for the more conservative one, so the write and retrieval aggressiveness that makes memory useful is what makes it exploitable. Input-boundary defenses transfer poorly: the best off-the-shelf guardrail detected 84.44% of strong-signal attacks but 42.50% of weak-signal ones, whose payloads are semantically indistinguishable from legitimate content. The paper's defense directions match this report's lifecycle: source isolation, write-path provenance tracking, and compaction filters that separate trusted from untrusted content before summarization.

The design controls are consistent with the memory lifecycle above, and several now have named production mechanisms:

- Separate trusted long-term memory from untrusted retrieved content.
- Track provenance, timestamp, writer identity, write authority, and expiry on every memory.
- Quarantine web/document/tool content before it can become a durable instruction.
- Require review gates before memories affect high-authority actions, permissions, finance, deployment, or security decisions.
- Prefer scoped memories: user-level, project-level, repo-level, team-level, task-level.
- Store contradictions and supersession chains rather than silently overwriting facts. The production mechanism is bi-temporal fact invalidation: record when a fact became true and when it stopped being true, with each fact linked to its source and supporting point-in-time queries ([[sources/Zep Temporal Knowledge Graph Memory]], [[sources/Zep Markdown Is Not Agent Memory]]).
- Audit memory periodically for stale, adversarial, overfit, or low-value entries.
- Support user-visible list, forget, export, and deletion flows.
- For shared/team memory, include conflict resolution and authority rules. [[sources/Governed Shared Memory for Multi-Agent LLM Systems]] formalizes these primitives; see Shared Memory Across Agents.

Provider products have begun shipping this list. Anthropic's Managed Agents memory stores (detailed under Dreaming) separate redaction from deletion so secrets can be scrubbed without destroying the audit trail, and the docs warn that a `read_write` shared store lets injected content become trusted memory in later sessions ([[sources/Claude Managed Agents Memory Stores]]).

The controls also collide with current research practice. Memory-evolution designs such as [[sources/A-MEM]] let new entries retroactively rewrite existing memories; this improves coherence but erases the original record, a provenance and audit tradeoff the paper does not address, so evolution-style stores need versioning underneath, the same reason the dreaming guidance above keeps the input store immutable. Human review is also a weak backstop ([[sources/Zep Markdown Is Not Agent Memory]], discussed above): review gates work as explicit process, not as an assumed benefit of a readable format.

Skills need the same treatment. A skill can inject instructions and run scripts, so it should be reviewed like a dependency. That advice now has incident evidence. [[sources/Koi Security ClawHavoc]] audited ClawHub, OpenClaw's official skill marketplace, and found 341 of 2,857 skills malicious (11.9%) on 2026-02-01; a rescan two weeks later found 824 of more than 10,700 (7.7%), and Antiy Labs later catalogued 1,184 historically, so any single contamination percentage is a point-in-time measurement. Most of the malicious skills belonged to one campaign delivering a macOS credential stealer through fake "Prerequisites" steps inside SKILL.md, with the agent itself surfacing the fake setup step to the user. Skill marketplaces extend the MCP-server supply-chain pattern to procedural memory distribution. [[sources/Comprehensive Survey on Agent Skills]] states the same requirement from the research side, naming quality control, safe updating, and long-term capability management as open challenges of the skill lifecycle. Memory and skills are both compounding layers; that is their value and their risk.

## Builder Guidance

### 1. Split Memory by Failure Mode

Do not start with "add vector memory." Start with the failure:

| Failure | Better First Tool |
|---|---|
| Agent forgets project preferences across sessions | Persistent semantic/procedural memory |
| Agent loses current task state after a pause | Durable session state and checkpoints |
| Agent hits context limit during one long thread | Compaction or handoff |
| Context is bloated by logs/search/file reads | Tool-result clearing or observation masking |
| Context is bloated by tool definitions before work starts | On-demand tool discovery instead of upfront schema injection |
| Agent cannot find relevant code | Context retrieval and line/block/file benchmarks |
| Agent must answer whole-corpus or global questions | Graph index with community summaries, not top-k vector retrieval |
| Agent repeats a bad workflow | Learned rules, skills, trajectory memory |
| Agent needs exact prior artifact | Artifact store and pointers, not summary |
| Agent has irrelevant memories injected | Retrieval gating and memory ranking |

Failure-mode-first design has empirical grounding in the multi-workload evaluation covered above ([[sources/Are We Ready For An Agent-Native Memory System]]). The new rows carry stated tradeoffs. Whole-corpus questions defeat top-k retrieval because no small set of chunks contains the answer; community-summary graph indexes answer them at the price of significant upfront LLM indexing cost ([[sources/GraphRAG]]). Tool definitions are a context load of their own: [[sources/MCP-Zero]] measures the GitHub MCP server at over 4,600 tokens for 26 tools and reports a 98% reduction in token consumption on APIBank when the agent requests tools on demand rather than receiving every schema up front.

### 2. Use a Write-Manage-Read Lifecycle

A robust memory layer should implement:

1. Write candidates: explicit user saves, model `remember` calls, compaction ingestion, post-run reflection, human feedback, and artifact updates.
2. Filtering: reject untrusted instructions, prompt-injection payloads, transient facts, and low-confidence claims.
3. Verification: tie each memory to source lines, artifacts, timestamps, and writer authority.
4. Classification: separate preferences, facts, tasks, events, decisions, procedures, failures, recoveries, and constraints.
5. Conflict handling: supersede stale entries instead of silently accumulating contradictions. Systems that skip this step return stale facts, what one multi-workload evaluation calls "hallucinations of the past"; graph-based stores handle targeted overwrites more reliably than fact-extraction plugins or append-only logs ([[sources/Are We Ready For An Agent-Native Memory System]]). Bi-temporal validity intervals with automatic fact invalidation and episode-level provenance are the production mechanism ([[sources/Zep Temporal Knowledge Graph Memory]]). The same staleness discipline applies to tool indexes: auto-synchronize them against the tool servers as the source of truth ([[sources/ScaleMCP]]).
6. Retrieval: combine exact lookup, keyword search, vector search, raw transcript fallback, and recency/authority scoring. For multi-hop questions, add graph-index traversal as a channel; it replaces iterative retrieval rounds at much lower query cost ([[sources/HippoRAG]], caveats above). Index lightweight abstractions and cue anchors rather than raw memory values, and consider iterative policy-guided retrieval as an alternative to one-shot top-k ([[sources/Memora]]).
7. Context injection: synthesize only what the current turn needs; avoid dumping memory wholesale. Zep's query-adaptive context assembly under a fixed character budget is the production mechanism ([[sources/Zep Smart Context Assembly]]).
8. Forgetting: support deletion, expiry, and user review.

Cloudflare's source is the best production example of this lifecycle. The memory survey gives the general write-manage-read formalization. [[sources/Infini Memory]] names the recurring failure modes the lifecycle guards against: memory fragmentation, memory conflict, compression loss, and retrieval that returns fragments too isolated to support reasoning. For the manage step, the evaluated default is conservative: consolidate cautiously, and prefer localized maintenance over global reorganization ([[sources/Are We Ready For An Agent-Native Memory System]]). The project operation note adds safety concerns: memory poisoning is more damaging than one-turn prompt injection because bad memory can persist across tasks.

### 3. Treat Compaction as a Boundary Event

When compaction fires:

1. Produce the continuation artifact: text summary, provider compaction item, or handoff brief.
2. Preserve exact references: files changed, commands run, test results, artifacts, unresolved decisions, IDs, URLs, and branch state.
3. Trigger memory ingestion or reflection for cross-session knowledge. Filter first: compaction-driven write is a named memory-poisoning channel, so ingestion needs filters that separate trusted from untrusted content ([[sources/Memory Poisoning Attacks in LLM Agents]]).
4. Reset the cache boundary: place a cache breakpoint on the compaction artifact and keep the system prompt cached separately ([[sources/Claude API Compaction]], [[sources/Claude API Prompt Caching]]).

Do not rely on compaction for exact recall. If exactness matters, store an artifact or pointer. If it can be re-fetched, clear it. If it should shape future behavior, write a memory or skill.

Compaction is also not the only boundary event, and it is not the cache-cheapest one. The boundary options are compact, handoff, and rewind: compact when the discarded context is genuinely no longer needed, hand off when a cleaner work unit should start ([[sources/Amp Handoff]]), and rewind when abandoning a path entirely, the cache-cheapest exit ([[sources/Claude Code Prompt Caching]]). Batch context mutations at boundaries; per-turn edits invalidate the prefix cache above the mutated point ([[sources/TokenPilot]]). Prefer reversible eviction when content may be needed later: recoverable full-fidelity archives change what safe eviction means, compared with one-way deletion or summarization ([[sources/VISTA Latent Context Managers]]).

### 4. Evaluate with Action Probes

Use evals that ask whether the agent can continue:

- Can it name the current goal and next step?
- Can it find the relevant file, block, and line?
- Can it recover a decision and the reason for it?
- Can it avoid repeating a failed attempt?
- Can it respect a remembered user or project preference?
- Can it distinguish stale memory from current state?
- Can it cite the artifact or source that supports the memory?
- Can it complete the task with compressed context at lower cost?

Factory's evaluation source is especially useful here because it tests continuation rather than summary similarity. ContextBench adds artifact-level retrieval metrics. The Complexity Trap and SWE-Pruner show cost and task-success measures for coding agents.

Use an eval matrix rather than one metric:

| Capability | Evaluation Source Pattern | What to Measure |
|---|---|---|
| Compaction continuity | [[sources/Factory Context Compression Evaluation]] | Can the agent resume the task, preserve artifacts, and follow prior decisions? |
| Context growth robustness | [[sources/LOCA-bench]], [[sources/Letta Context-Bench]] | Does performance degrade as irrelevant or long context grows? |
| Retrieval quality | [[sources/ContextBench]] | File/block/line precision, recall, and F1 before final task success. |
| Long-term conversational memory and forgetting | [[sources/LongMemEval]] | Accuracy across 500 questions on five abilities; whether the system prefers newer facts over superseded ones (knowledge updates) and declines when memory lacks the answer (abstention). |
| Cost and latency | [[sources/The Complexity Trap]], [[sources/Parallel Context Compaction]], [[sources/Agent Memory Characterization]], [[sources/Manus Context Engineering]], [[sources/TokenPilot]] | Token cost, instance cost, blocking compaction latency, throughput, prompt-cache hit rate, construction (write-path) cost, energy per correct answer, and footprint growth slope. |
| Skill utility | [[sources/SkillsBench]], [[sources/Agentic Skills in the Wild]], [[sources/SkillOpt]], [[sources/OpenAI Eval Skills]] | Does loading the skill improve outcome, can the agent select it from a larger library, does a candidate skill edit improve held-out validation before acceptance, and does the skill ship with evals and regression tests (vendor guidance)? |
| Consolidation quality | [[sources/Anthropic Managed Agents Dreaming Outcomes]], [[sources/Google ReasoningBank]], [[sources/Trajectory-Informed Memory Generation]] | Do background reflections remove duplicates, resolve contradictions, preserve provenance, and improve later task success? |
| Memory safety | [[sources/Agent Security Bench]], [[sources/AgentDojo]], [[sources/InjecAgent]], [[sources/Memory Poisoning Attacks in LLM Agents]] | Can untrusted content poison memory, trigger unsafe tools, or bypass instruction hierarchy? |
| Shared-memory reliability | [[sources/When Agents Misremember Collectively]], [[sources/AgentNet]], [[sources/G-Memory]], [[sources/Governed Shared Memory for Multi-Agent LLM Systems]] | Do agents amplify false memories or resolve conflicting shared state? Does team-level memory improve later task success, and do scope, supersession, provenance, and propagation rules hold under governance testing? |

The cost row now measures the write path as well as the read path: for LLM-mediated memory systems, construction cost rather than query cost dominates the lifecycle, so read-side token savings can hide a front-loaded ingestion bill ([[sources/Agent Memory Characterization]]). Cache-hit rate belongs in the same row because context mutations silently destroy serving-side savings that production teams treat as a first-order cost metric ([[sources/Manus Context Engineering]]).

### 5. Default Architecture for a New Agent

A conservative first implementation:

```text
1. Order the request as a stable prefix (tools, system prompt, durable
   instructions) plus an append-only tail; append new instructions
   rather than editing the prefix.
2. Keep recent turns verbatim within a small window.
3. Store all durable artifacts outside chat: files, patches, logs, test results, links.
4. Add tool-result clearing for bulky re-fetchable outputs.
5. Add text compaction with a structured schema:
   - current objective
   - hard constraints
   - decisions made
   - files/artifacts touched
   - failed attempts
   - next actions
   - open questions
6. Add persistent memory only for cross-session facts/preferences/procedures.
7. Require provenance and timestamps for every memory.
8. Retrieve memory only when the current turn asks for it or a classifier predicts relevance.
9. Promote repeated successful procedures into skills/playbooks after review.
10. Build probes that resume from compacted state and measure task completion.
11. Add dreaming/consolidation only after provenance, review, and rollback are in place.
```

Evidence behind these defaults:

- Stable prefix plus append-only tail is the cheap path ([[sources/Claude API Prompt Caching]]; see Cache Economics). Claude Code orders its prompts this way in production ([[sources/Claude Code Prompt Caching]]).
- The compaction schema keeps failed attempts on purpose: erasing failure evidence removes the model's ability to update its beliefs ([[sources/Manus Context Engineering]]).
- A fixed token-threshold compaction trigger is the right starting point, and it is also the baseline that learned memory-management policies are evaluated against; treat learned compression timing as an upgrade, not a default ([[sources/SWE-MeM]]).
- For cross-session recall, extraction-and-consolidation pipelines drastically cut cost and latency versus full-context replay while staying near-competitive on accuracy, and beat RAG and commercial memory baselines on accuracy, on vendor-reported conversational benchmarks ([[sources/Mem0]]). File-based memory stays proportionate for a single agent and a single user; move to a database-backed store when Zep's four boundary conditions apply ([[sources/Zep Markdown Is Not Agent Memory]]).
- Skill promotion has an evidenced criterion: crystallize a recurring procedure into a callable tool only when repeated reuse justifies the generation cost, and validate the generated tool before exposing it ([[sources/Metis]]). Accept edits to a skill document only when a held-out validation score improves ([[sources/SkillOpt]]).
- Match the construction-versus-query cost split to the workload: heavy LLM-mediated ingestion pipelines pay off only when enough queries amortize each write ([[sources/Agent Memory Characterization]]).

For more mature systems, add multi-channel retrieval, asynchronous memory consolidation, handoff to fresh threads, learned retrieval and compression-timing policies, and task-aware pruning.

Maturity tiers:

- Default: recent verbatim window, artifact store, tool-result clearing, structured text compaction, provenance, selective retrieval, and user-visible memory controls.
- Intermediate: multi-channel retrieval, compaction-triggered ingestion, reviewable dreaming/consolidation jobs, skill libraries, handoff briefs, and continuation probes.
- Advanced: provider-native compaction, parallel block compaction, off-the-shelf budget-controlled compression ([[sources/LLMLingua]]) followed by ACON-style failure-driven optimization, MEMENTO-style model-internal compression, learned retrieval and compression-timing policies ([[sources/SWE-MeM]]), dreaming/consolidation, and self-evolving skill libraries.

## Open Questions and Gaps

- Opaque compaction quality is hard to audit. OpenAI's provider-native path may preserve useful state, but external harnesses cannot inspect it like a text summary. Anthropic's server-side compaction is the existing counter-design ([[sources/Claude API Compaction]], detailed in the Anthropic section). The question narrows to whether opaque continuation artifacts perform well enough to justify losing the audit path.
- Memory ROI is now measured, but inconsistently and mostly by vendors. [[sources/Mem0]] reports 91% lower p95 latency and over 90% token cost savings versus full-context, and [[sources/Zep Temporal Knowledge Graph Memory]] reports up to 18.5% accuracy improvement on LongMemEval with roughly 90% response latency reduction; both evaluate the vendors' own systems. The tradeoff is not free ([[sources/Zep Smart Context Assembly]], see the Zep section). Independent measurement reframes the question rather than settling it: LLM-mediated memory carries a measured energy premium over flat retrieval with construction dominating (see Memory as Measured Infrastructure, [[sources/Agent Memory Characterization]]), and memory systems sometimes underperform full-history retention on long-horizon tasks ([[sources/MAGE Memory Execution State Management]], see Execution-State Memory). The open question is which workloads justify the premium, not whether a premium exists.
- Write timing is a newly named open question. [[sources/Memora]] lists Deferred Memory as a research direction: postpone memory construction until sufficient context, evidence, or future utility is available, instead of committing at ingestion time. With construction the cost-dominant phase for LLM-mediated systems, deferral is a live design lever with no published guidance yet.
- Governance UX is immature. Users need understandable memory review, deletion, provenance, and scope controls.
- Negative transfer is a real risk. Learned rules, trajectory tips, and memories can become stale or overgeneralized. Validation-gated promotion is an emerging countermeasure on the skills side ([[sources/SkillOpt]]); an equivalent gate for fact and trajectory memories remains open.
- Multi-agent shared memory has narrowed from gap to frontier: constructive designs ([[sources/G-Memory]]) and governance primitives ([[sources/Governed Shared Memory for Multi-Agent LLM Systems]]) are covered under Shared Memory Across Agents, and shipped product semantics under Dreaming ([[sources/Claude Managed Agents Memory Stores]]). Microsoft names Group Memory a roadmap direction ([[sources/Memora]]). The remaining gaps are production evidence for the research designs, cross-provider conflict-resolution semantics, and comparative evaluation of shared-memory quality.
- Benchmarks still lag production use, and vendor scores are incomparable. Multi-workload evaluation now exists ([[sources/Are We Ready For An Agent-Native Memory System]], see Memory as Measured Infrastructure), and [[sources/Memory in the Age of AI Agents]] compiles the benchmark and framework landscape. [[sources/LongMemEval]] has become the de-facto reporting benchmark, but configurations vary: Mem0's 2026 algorithm self-reports 94.4, while the multi-workload evaluation measures Zep at 48.0 LLM Judge Accuracy on the same benchmark. Real systems also combine retrieval, context growth, cost, and safety slices that no single benchmark covers together.

## Source Register

Primary local source maps: [[maps/Context Management Map]], [[maps/Agent Skills Map]], and [[maps/Safety Map]]. Supporting local notes: [[operations/agent memory]], [[operations/durable sessions]], [[claims/Claim - Context management is an agent architecture choice|context management claim]], and [[claims/Claim - Agent memory and skills create compounding improvement loops|memory/skills claim]].

Source cards cited in this report:

| Source | Date in Local Graph | Type |
|---|---:|---|
| [[sources/A-MEM]] | 2025-02-17 | paper |
| [[sources/ACON]] | 2025-10-01 | paper |
| [[sources/Agent Memory Characterization]] | 2026-06-04 | paper |
| [[sources/Agent Security Bench]] | 2024-10-03 | paper |
| [[sources/Agent Skills Specification]] | 2025-12-18 | protocol |
| [[sources/AgentDojo]] | 2024-06-19 | paper |
| [[sources/Agentic Context Engineering]] | 2025-10-06 | paper |
| [[sources/Agentic Skills in the Wild]] | 2026-04-06 | paper |
| [[sources/AgentNet]] | 2025-04-01 | paper |
| [[sources/Amp Handoff]] | 2025-10-23 | article |
| [[sources/Anthropic Agent Skills]] | 2025-10-16 | article |
| [[sources/Anthropic Context Engineering Cookbook]] | 2026-05-26 | docs |
| [[sources/Anthropic Effective Context Engineering]] | 2025-09-29 | article |
| [[sources/Anthropic Effective Harnesses for Long-Running Agents]] | 2025-11-26 | article |
| [[sources/Anthropic Managed Agents Dreaming Outcomes]] | 2026-05-06 | article |
| [[sources/Are We Ready For An Agent-Native Memory System]] | 2026-06-23 | paper |
| [[sources/BrowseSafe]] | 2025-11-25 | paper |
| [[sources/Claude API Compaction]] | 2026-01-12 | docs |
| [[sources/Claude API Prompt Caching]] | 2026-02-05 | docs |
| [[sources/Claude Code Prompt Caching]] | 2026-05-26 | docs |
| [[sources/Claude Fable 5 and Claude Mythos 5]] | 2026-06-09 | article |
| [[sources/Claude Managed Agents Memory Stores]] | 2026-04-23 | docs |
| [[sources/Cloudflare Agent Memory]] | 2026-04-17 | article |
| [[sources/Cognitive Architectures for Language Agents]] | 2023-09-05 | paper |
| [[sources/Comprehensive Survey on Agent Skills]] | 2026-05-08 | paper |
| [[sources/Context Rot]] | 2025-07-14 | report |
| [[sources/ContextBench]] | 2026-02-05 | paper |
| [[sources/Cursor Bugbot Learned Rules]] | 2026-04-08 | article |
| [[sources/Cursor Building Better Bugbot]] | 2026-01-15 | article |
| [[sources/Cursor Improving Agent Harness]] | 2026-04-30 | article |
| [[sources/Design Patterns for Securing LLM Agents]] | 2025-06-10 | paper |
| [[sources/Factory Context Compression Evaluation]] | 2025-12-16 | article |
| [[sources/G-Memory]] | 2025-06-09 | paper |
| [[sources/Generative Agents]] | 2023-04-07 | paper |
| [[sources/GitHub CLI Manage Agent Skills]] | 2026-04-16 | article |
| [[sources/GitHub Copilot Agent Skills Docs]] | 2025-12-18 | docs |
| [[sources/Google ADK Context Compression]] | 2026-05-26 | docs |
| [[sources/Google ADK Durable Agents]] | 2026-05-12 | article |
| [[sources/Google ReasoningBank]] | 2026-04-21 | article |
| [[sources/Governed Shared Memory for Multi-Agent LLM Systems]] | 2026-06-23 | paper |
| [[sources/GraphRAG]] | 2024-04-24 | paper |
| [[sources/HippoRAG]] | 2024-05-23 | paper |
| [[sources/Infini Memory]] | 2026-06-09 | paper |
| [[sources/InjecAgent]] | 2024-03-05 | paper |
| [[sources/Koi Security ClawHavoc]] | 2026-02-01 | article |
| [[sources/LangChain Deep Agents v0.6]] | 2026-05-13 | article |
| [[sources/LangSmith Context Hub]] | 2026-05-13 | article |
| [[sources/Letta Code Memory Docs]] | 2026-05-18 | docs |
| [[sources/Letta Context-Bench]] | 2025-10-30 | article |
| [[sources/LLMLingua]] | 2023-12-01 | paper |
| [[sources/LOCA-bench]] | 2026-02-08 | paper |
| [[sources/LongMemEval]] | 2024-10-14 | paper |
| [[sources/Lost in the Middle]] | 2023-07-06 | paper |
| [[sources/MAGE Memory Execution State Management]] | 2026-06-04 | paper |
| [[sources/Manus Context Engineering]] | 2025-07-18 | article |
| [[sources/MCP-Zero]] | 2025-06-01 | paper |
| [[sources/Mem0]] | 2025-04-28 | paper |
| [[sources/MEMENTO]] | 2026-04-10 | paper |
| [[sources/MemGPT]] | 2023-10-12 | paper |
| [[sources/Memora]] | 2026-06-29 | article |
| [[sources/Memory for Autonomous LLM Agents]] | 2026-03-08 | paper |
| [[sources/Memory in the Age of AI Agents]] | 2025-12-15 | paper |
| [[sources/Memory Poisoning Attacks in LLM Agents]] | 2026-06-03 | paper |
| [[sources/Metis]] | 2026-06-23 | paper |
| [[sources/Microsoft Agent Framework Harness Compaction]] | 2026-03-12 | article |
| [[sources/Microsoft Agent Framework Skills Docs]] | 2026-05-18 | docs |
| [[sources/OpenAI Agents SDK Compaction Sessions]] | 2026-05-26 | docs |
| [[sources/OpenAI Codex Agent Loop]] | 2026-01-23 | article |
| [[sources/OpenAI Codex Record and Replay]] | 2026-06-18 | docs |
| [[sources/OpenAI Eval Skills]] | 2026-01-22 | article |
| [[sources/OpenAI Responses API Computer Environment]] | 2026-03-11 | article |
| [[sources/OpenAI Skills Docs]] | 2026-05-18 | docs |
| [[sources/Parallel Context Compaction]] | 2026-05-22 | paper |
| [[sources/Prompt Compression Survey]] | 2025-04-01 | paper |
| [[sources/Reflexion]] | 2023-03-20 | paper |
| [[sources/SAGE Skill Library]] | 2025-12-18 | paper |
| [[sources/ScaleMCP]] | 2025-05-09 | paper |
| [[sources/SkillOpt]] | 2026-05-22 | paper |
| [[sources/SkillRL]] | 2026-02-09 | paper |
| [[sources/SkillsBench]] | 2026-02-13 | paper |
| [[sources/SWE-MeM]] | 2026-06-26 | paper |
| [[sources/SWE-Pruner]] | 2026-01-23 | paper |
| [[sources/The Complexity Trap]] | 2025-08-29 | paper |
| [[sources/To Retrieve or To Think]] | 2026-01-13 | paper |
| [[sources/TokenPilot]] | 2026-06-15 | paper |
| [[sources/Trajectory-Informed Memory Generation]] | 2026-03-11 | paper |
| [[sources/VISTA Latent Context Managers]] | 2026-06-29 | paper |
| [[sources/Voyager]] | 2023-05-25 | paper |
| [[sources/When Agents Misremember Collectively]] | 2026-01-31 | paper |
| [[sources/Zep Markdown Is Not Agent Memory]] | 2026-06-23 | article |
| [[sources/Zep Smart Context Assembly]] | 2026-06-04 | article |
| [[sources/Zep Temporal Knowledge Graph Memory]] | 2025-01-20 | paper |
