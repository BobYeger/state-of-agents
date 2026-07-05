# Agent Memory Technical Brief

Date: 2026-07-05
Scope: local graph only. Condensed from [[reports/Agent Memory Report]] as revised 2026-07-05. This is the shorter technical version of that report; it uses source terminology as labels and keeps direct excerpts short because verbatim quotation is limited. Text-only: figures live in the full report.

## 0. Core Finding

The sources do not describe one thing called "memory." They describe a stack, and the stack has a citable ancestry: [[sources/Cognitive Architectures for Language Agents|CoALA]] fixed the working/episodic/semantic/procedural memory split, and [[sources/MemGPT]] introduced the paged virtual-context design that today's persistent-agent products descend from.

```text
online context management
  = just-in-time retrieval + retrieval compression + dynamic tool discovery
  + compaction / compacted items        # provider-native on both major APIs
  + tool-result clearing / observation masking / pruning / recitation
  + handoff / rewind

external memory
  = memory stores / profiles / MemFS / ContextHub / shared stores
  + substrates: files, topic documents, abstraction-keyed entries, entity and temporal graphs
  + remember / recall / list / forget
  + provenance / supersession / expiry

background consolidation
  = dreams / sleep-time reflection / trajectory memory
  + deduplication / contradiction repair / pattern extraction

procedural memory
  = Agent Skills / learned rules / skill libraries / crystallized tools

durable runtime state
  = event logs / checkpoints / workflow state / artifacts / execution-state trees
```

The need for this stack is measured, not asserted. All 18 tested models degrade as input length grows even on trivial tasks, and focused prompts of about 300 tokens of relevant content consistently beat full prompts of about 113k tokens ([[sources/Context Rot]]). Mid-context placement alone drops multi-document QA accuracy by roughly 20 or more points ([[sources/Lost in the Middle]]). Commercial assistants and long-context LLMs show a 30% accuracy drop across sustained interactions on [[sources/LongMemEval]]'s 500 questions. Two correctives bound the design space: no single memory architecture dominates, effectiveness follows workload alignment ([[sources/Are We Ready For An Agent-Native Memory System]]), and for LLM-mediated memory the write path, not the read path, dominates lifecycle cost ([[sources/Agent Memory Characterization]]).

These are artifacts passed back into future model calls — text summaries, compaction items, memory stores, retrieved notes, durable state, skills — not the internal activation state studied by mechanistic interpretability. The genuinely latent techniques sit in a separate model-internal bucket that the survey literature names latent memory ([[sources/Memory in the Age of AI Agents]]).

## 1. Minimal Architecture

```text
model_input_t =
  stable_prefix              # tools + system + durable instructions, cached
+ current_goal
+ recent_verbatim_turns
+ compacted_history          # summary or provider compaction block/item
+ retrieved_memory           # recall/search result, not full store
+ durable_state_pointer      # workflow step, artifacts, checkpoints
+ selected_skills            # loaded by progressive disclosure

write_side =
  memory_ingest(conversation)           # filter untrusted content first
+ remember(item)
+ dream(memory_store, sessions)
+ skill_promotion(repeated_procedure)   # validation-gated

read_side =
  recall(query)                         # only on information gap
+ retrieve_files_or_blocks(task)
+ load_skill(skill_description_match)
+ read_durable_state(workflow_id)
```

Ordering is load-bearing, not cosmetic. Cache reads cost 0.1x base input while 5-minute cache writes cost 1.25x and 1-hour writes 2x, and the prefix hierarchy is tools, then system, then messages, so a stable prefix plus an append-only tail is the cheap physical layout ([[sources/Claude API Prompt Caching]]). Manus calls KV-cache hit rate "the single most important metric for a production-stage AI agent" ([[sources/Manus Context Engineering]]).

Builder rule from the sources: decide what must be exact, what can be summarized, what can be re-fetched, what should persist across sessions, and what should never be written.

## 2. Mechanism Groups

| Group | Mechanism | State Transform | Trigger | Inspectability | Source Anchors |
|---|---|---|---|---|---|
| Online context | Whole-transcript compaction | transcript -> summary / `compaction` block | token threshold, manual `/compact` | high if text | [[sources/Anthropic Context Engineering Cookbook]], [[sources/OpenAI Codex Agent Loop]] |
| Online context | Provider-native compaction | prior input -> opaque encrypted item (OpenAI) or readable compaction block with pause hook (Anthropic) | server threshold or `/compact` | opaque vs inspectable text; the live axis | [[sources/OpenAI Responses API Computer Environment]], [[sources/OpenAI Agents SDK Compaction Sessions]], [[sources/Claude API Compaction]] |
| Online context | Parallel compaction | context blocks -> concurrent localized summaries -> merged compact context | serving/runtime compaction | text summaries, block-level knobs | [[sources/Parallel Context Compaction]] |
| Online context | Tool-result clearing | old re-fetchable tool outputs -> placeholders with re-fetch pointer | tool-result volume threshold | high | [[sources/Anthropic Context Engineering Cookbook]], [[sources/Microsoft Agent Framework Harness Compaction]], [[sources/Manus Context Engineering]], [[sources/TokenPilot]] |
| Online context | Observation masking | old observations omitted | turn/token/cost threshold | high, but lossy by omission | [[sources/The Complexity Trap]] |
| Online context | Recitation | rewritten plan file (todo.md) restated into recent context | every turn on long tasks | high | [[sources/Manus Context Engineering]] |
| Online context | Task-aware pruning | long code context -> selected relevant lines | before model call / middleware | high if lines retained | [[sources/SWE-Pruner]] |
| Online context | Optimized compression / learned policies | learned compressors; learned when/what/how-to-compress policies | long-horizon agent traces | training-dependent | [[sources/LLMLingua]], [[sources/ACON]], [[sources/SWE-MeM]] |
| Online context | Retrieval compression | retrieved documents -> trained summaries, possibly an empty string | post-retrieval, before injection | medium; trained compressor | [[sources/RECOMP]] |
| Online context | Dynamic tool discovery | tool schemas held outside context, retrieved on demand | need-driven, per task step | high if index audited | [[sources/MCP-Zero]], [[sources/ScaleMCP]] |
| Online context | Context retrieval | file/block/line search -> selected evidence | information gap | high if source linked | [[sources/ContextBench]], [[sources/Letta Context-Bench]] |
| Online context | Agent-visible context dashboard | typed, addressable blocks + reversible full-fidelity archive | agent keep/archive decisions under budget stats | high | [[sources/VISTA Latent Context Managers]] |
| External memory | Memory profile/store | sessions -> facts/events/instructions/tasks | compaction ingest, `remember` call, self-directed paging | high if provenance stored | [[sources/MemGPT]], [[sources/Cloudflare Agent Memory]], [[sources/Memory for Autonomous LLM Agents]] |
| External memory | Substrate variants | files/topic documents, abstraction-keyed entries, entity graphs, bi-temporal graphs | workload-dependent | varies; see 3.2 | [[sources/GraphRAG]], [[sources/HippoRAG]], [[sources/A-MEM]], [[sources/Zep Temporal Knowledge Graph Memory]], [[sources/Memora]], [[sources/Infini Memory]] |
| External memory | MemFS / ContextHub | memories and context files -> versioned filesystem/repository | agent/user edits | high | [[sources/Letta Code Memory Docs]], [[sources/LangSmith Context Hub]] |
| External memory | Shared memory stores | workspace-scoped stores with write authority, concurrency control, versioned audit | attach at session creation | high; every mutation versioned | [[sources/Claude Managed Agents Memory Stores]], [[sources/Governed Shared Memory for Multi-Agent LLM Systems]] |
| Background memory | Dreaming | input memory store + sessions -> new output memory store | scheduled, batch, compaction event | high if output store reviewed | [[sources/Anthropic Managed Agents Dreaming Outcomes]], [[sources/Letta Code Memory Docs]] |
| Background memory | Trajectory memory | execution traces -> strategy/recovery/optimization tips | post-run reflection | medium/high with provenance | [[sources/Reflexion]], [[sources/Trajectory-Informed Memory Generation]], [[sources/Google ReasoningBank]] |
| Procedural memory | Agent Skills | skill description -> loaded instructions/scripts/references/assets | skill match / explicit invocation | high if reviewed | [[sources/Agent Skills Specification]], [[sources/Anthropic Agent Skills]], [[sources/OpenAI Skills Docs]] |
| Procedural memory | Learned rules / skill libraries / crystallized tools | feedback, demonstration, or reflection -> future rule, instruction, or callable tool | review feedback, RL, validation-gated edits, demonstration recording | varies | [[sources/Cursor Bugbot Learned Rules]], [[sources/SkillOpt]], [[sources/Metis]], [[sources/OpenAI Codex Record and Replay]], [[sources/SAGE Skill Library]], [[sources/SkillRL]], [[sources/Voyager]] |
| Durable runtime | Durable state | workflow event -> explicit state/checkpoint/artifact pointer | every workflow transition | high | [[sources/Google ADK Durable Agents]], [[operations/durable sessions|operations/durable sessions]] |
| Durable runtime | Execution-state tree memory | subgoal transitions -> hierarchical state tree (Grow, Compress, Maintain, Revise) | every subgoal transition | high | [[sources/MAGE Memory Execution State Management|MAGE]] |
| Boundary reset | Handoff | current thread -> new goal + relevant files + prompt draft | thread becomes too long/meandering | high if editable | [[sources/Amp Handoff]], [[sources/Anthropic Effective Harnesses for Long-Running Agents]] |
| Model/inference | Mementos / soft compression | reasoning blocks -> dense state summaries / soft prompts | during inference or trained compression | lower | [[sources/MEMENTO]], [[sources/AutoCompressors]], [[sources/Prompt Compression Survey]] |

## 3. Implementation Contracts

### 3.1 Compaction Contract

Source terms: compaction, `compaction` content block, `compact_20260112`, compacted item list, `encrypted_content`, `pause_after_compaction`, sliding-window compaction, parallel block compaction.

```text
input:
  transcript_items
  tool_calls_and_results
  prior_compaction_blocks
  compaction_instructions

output:
  continuation_artifact =
    text_summary
    OR typed compaction block (Anthropic, readable)
    OR provider compacted item list (OpenAI, opaque/encrypted)

must preserve:
  objective / constraints / decisions / unresolved questions
  files and artifacts touched / failed attempts / next actions

must not pretend to preserve:
  verbatim tool outputs; exact table cells / logs / IDs unless explicitly retained
  cross-session memory
```

Compaction is now a provider feature on both major APIs; the live axis between them is inspectability. Anthropic's server-side path (edit type `compact_20260112`) fires at a configurable input-token trigger, default 150,000 and minimum 50,000; the block is text, `pause_after_compaction: true` returns a `compaction` stop reason so the harness can adjust messages before continuing, and an `instructions` parameter fully replaces the default summarization prompt. Billing subtlety: the compaction pass is a sampling iteration reported in `usage.iterations[]`, not in the top-level token counts ([[sources/Claude API Compaction]]). OpenAI's compacted item is opaque and can be encrypted; the Agents SDK wraps it in `OpenAIResponsesCompactionSession` and warns that automatic compaction can block streaming ([[sources/OpenAI Codex Agent Loop]], [[sources/OpenAI Agents SDK Compaction Sessions]]).

Use compaction for dialogue, reasoning, and decisions that cannot be re-fetched. Use clearing/masking for bulky re-fetchable outputs. The boundary options are compact, handoff, and rewind; rewind truncates back to an already-cached prefix and is the cache-cheapest exit ([[sources/Amp Handoff]], [[sources/Claude Code Prompt Caching]]). Batch context mutations at boundaries: per-turn edits invalidate the prefix cache above the mutated point, and ingestion-aware compaction plus lifecycle-aware eviction reports cost reductions of 61% and 56% in isolated mode and 61% and 87% in continuous mode on PinchBench and Claw-Eval ([[sources/TokenPilot]]). Repeated whole-rewrite compaction risks context collapse; prefer structured incremental updates ([[sources/Agentic Context Engineering]]). Evaluate by continuation probes, not summary similarity ([[sources/Factory Context Compression Evaluation]]).

### 3.2 Memory Store Contract

Source terms: memory profile, memory store, ingest, remember, recall, list, forget, facts/events/instructions/tasks, provenance, supersession, validity intervals.

```text
memory_item:
  id
  type: fact | event | instruction | task | preference | procedure | failure_lesson
  content
  source: session_id | transcript_lines | artifact_id | user_write | feedback_event
  authority: user | system | tool | web | inferred
  created_at / observed_at / expires_at
  supersedes: [memory_id]
  confidence
  scope: user | project | repo | team | task
```

Cloudflare's architecture is the most explicit production pattern: ingestion extracts, verifies, classifies, deduplicates, tracks provenance, and stores, then retrieval combines channels such as full-text, exact fact-key lookup, raw message search, vector search, HyDE vector search, rank fusion, and synthesis ([[sources/Cloudflare Agent Memory]]).

Substrate choice is workload-dependent. Global sensemaking over roughly 1M-token corpora structurally defeats top-k vector retrieval; an entity graph with community summaries wins on comprehensiveness and diversity at significant upfront indexing cost ([[sources/GraphRAG]]). Single-step graph traversal matches or beats iterative retrieval on multi-hop QA while 10-30x cheaper and 6-13x faster at query time, and the two compose ([[sources/HippoRAG]]). Agent-curated notes with dynamic link generation buy coherence at the price of retroactive rewriting that erases the original record ([[sources/A-MEM]]). Bi-temporal graphs record when a fact became true and when it stopped being true, with automatic invalidation and episode-level provenance ([[sources/Zep Temporal Knowledge Graph Memory]]). The counterweight: Mem0's graph variant adds only about 2% over its base vector configuration on conversational QA, so extraction quality matters more than graph structure for conversational recall ([[sources/Mem0]]). Decoupling storage from retrieval is its own lever: Memora embeds only a 6-8 word primary abstraction per entry, reports 86.3% LLM-judge accuracy on LoCoMo and 87.4% on LongMemEval with up to 98% fewer context tokens and roughly half the entries per conversation that Mem0 stores (344 vs 651) ([[sources/Memora]]). Topic documents with buffered writes and agentic retrieval reach 64.7% overall on MemoryAgentBench without a mandatory vector or graph database ([[sources/Infini Memory]]).

File-based memory has a boundary rubric: how many agents and users share the memory, do facts change, can facts be re-derived from a local source, and is there a retention or compliance regime ([[sources/Zep Markdown Is Not Agent Memory]]). Past the boundary, shared stores need explicit semantics; the shipped example mounts workspace-scoped stores at `/mnt/memory/<slug>/`, attached via `resources[]` at session creation only, with `read_write` (default) or `read_only` enforced at the filesystem level, at most 8 stores per session, 2,000 memories per store, 100 kB (about 25k tokens) per memory, per-store instructions capped at 4,096 characters, optimistic concurrency via a `content_sha256` precondition, and an immutable version per mutation attributed to the writing session ([[sources/Claude Managed Agents Memory Stores]]).

On the read side, synthesize only what the current turn needs. Trained retrieval compressors reach compression rates as low as 6% and can return an empty string when documents are unhelpful ([[sources/RECOMP]]). Zep's Smart Context Assembly ranks candidates from five of six context types simultaneously into a fixed 2,500-character budget; one LoCoMo run traded 54% fewer tokens for about 8 points of accuracy, while a different run gained accuracy on fewer tokens ([[sources/Zep Smart Context Assembly]]).

### 3.3 Dreaming / Consolidation Contract

Source terms: dream, input memory store, sessions, output memory store, sleep-time dream subagents, reflection, ReasoningBank, closed loop of retrieval/extraction/consolidation.

```text
dream_job:
  inputs:
    memory_store_id
    session_ids[1..100]
    instructions
  output:
    new_memory_store_id
  invariants:
    input store is not modified
    output store can be reviewed, used, archived, or discarded

dream_output:
  merged duplicates; replaced stale/contradicted entries
  surfaced cross-session insights; extracted recurring mistakes
  extracted converged workflows and team-shared preferences
```

Dreaming is write-side maintenance, not online retrieval. Compaction asks what survives into the next context window. Dreaming asks what the agent should learn after reviewing many traces ([[sources/Anthropic Managed Agents Dreaming Outcomes]], [[sources/Letta Code Memory Docs]]).

The lineage is citable. [[sources/Generative Agents]] introduced reflection and the recency/importance/relevance retrieval scoring most agent memory scorers reuse, with the caveat that its evidence is behavioral believability, not task performance. [[sources/Reflexion]] carries the load-bearing condition: reflective memory pays off when grounded in external evaluation signals such as unit tests or environment reward (HumanEval pass@1 of 91% versus 80% for base GPT-4). [[sources/Google ReasoningBank]] and [[sources/Trajectory-Informed Memory Generation]] extract structured memories from successful and failed trajectories, including strategy tips, recovery tips, optimization tips, and preventative lessons, with provenance back to source trajectories.

Operating rules: keep the input store immutable and the output store reviewable; run on session batches, especially after compaction; preserve chronological cues during consolidation, since standard semantic consolidation destroys them ([[sources/Are We Ready For An Agent-Native Memory System]]); require provenance before promoted memories affect high-authority actions; promote stable repeated procedures into skills only after evaluation.

### 3.4 Skill Contract

Source terms: Agent Skills, `SKILL.md`, progressive disclosure, instructions, scripts, references, assets, learned rules, skill library, crystallized tools.

```text
skill:
  name
  description             # discoverable at startup / routing time
  instructions            # loaded only when relevant
  scripts/
  references/
  assets/
  tests/evals
  version
  owner
  trust_level
```

Skills are procedural memory organized by a four-stage lifecycle: representation, acquisition, retrieval, evolution — the write-manage-read loop applied to procedures ([[sources/Comprehensive Survey on Agent Skills]]). Progressive disclosure makes them a context-management technique: a large library carried without stuffing every procedure into every prompt.

The write paths are multiplying. Cursor's Bugbot converts review feedback into learned rules, with more than 110,000 repositories enabled and more than 44,000 rules generated at publication time ([[sources/Cursor Bugbot Learned Rules]]). OpenAI's Record & Replay converts one demonstrated macOS workflow into an inspectable, editable `SKILL.md` ([[sources/OpenAI Codex Record and Replay]]). [[sources/SkillOpt]] treats the skill document as trainable external state and accepts an edit only when held-out validation improves, reporting best or tied-best performance on all 52 evaluated model/benchmark/harness cells, with Codex-trained skills transferring into Claude Code. [[sources/Metis]] crystallizes recurring plans into validated callable tools only when repeated reuse justifies the tool-generation cost, improving AppWorld task accuracy by up to 20.6% over ReAct while reducing execution cost by up to 22.8%.

Govern skills like dependencies: review, versioning, tests, provenance, removal paths; GitHub CLI ships install, publish, and update workflows with versioning and provenance ([[sources/GitHub CLI Manage Agent Skills]]). The risk is incident-proven: an audit of ClawHub found 341 of 2,857 skills malicious (11.9%) on 2026-02-01, a rescan two weeks later found 824 of more than 10,700 (7.7%), and 1,184 were later catalogued historically, most delivering a macOS credential stealer through fake "Prerequisites" steps inside SKILL.md ([[sources/Koi Security ClawHavoc]]).

### 3.5 Durable State Contract

Source terms: durable state, event history, checkpoint/resume, artifacts, explicit state schema, execution-state tree.

```text
workflow_state:
  workflow_id / current_step / status
  pending_events
  artifact_refs / checkpoint_refs
  wakeup_conditions
  last_validated_at
```

Durable state is not chat memory. Google ADK's pattern: the agent reads the current workflow state instead of reconstructing progress from raw transcript history; sliding-window event compaction maintains the session history while the state schema stays authoritative ([[sources/Google ADK Durable Agents]], [[sources/Google ADK Context Compression]]).

The research grounding is [[sources/MAGE Memory Execution State Management|MAGE]]: semantic-similarity organization mismatches execution-state dependencies, and memory systems often fail to improve long-horizon performance versus simply retaining full history. MAGE manages a hierarchical state tree via Grow, Compress, Maintain, and Revise, improving average task success on MemoryArena by 7.8-20.4 percentage points over long-context and memory baselines while reducing token consumption by 55.1%. Recall-oriented conversation favors extraction systems; interdependent execution favors state trees.

### 3.6 Cache Economics Constraint

Every technique above mutates context, and every mutation has a cache price as well as a semantic effect. Manus averages a roughly 100:1 input-to-output token ratio, a typical task takes about 50 tool calls, and cached input cost $0.30 per million tokens versus $3.00 uncached at the time of writing, a 10x difference; its responses are logit masking instead of mid-loop tool-set changes, the filesystem as restorable compression (drop page content, keep the URL), todo.md recitation, and failed actions left in context ([[sources/Manus Context Engineering]]; single-team essay at mid-2025 pricing).

Claude Code is the harness-level demonstration: requests ordered as system prompt, project context, then conversation; skills and plan mode append instructions rather than editing the prefix; the compaction summarization request itself reads the existing cache, so generation, not a cache miss, is the slow part; `/rewind` is cheaper still ([[sources/Claude Code Prompt Caching]]). API affordances match the pattern: Opus 4.8 accepts mid-conversation system messages without invalidating the cached prefix, and a `max_tokens: 0` request pre-warms a cache without sampling ([[sources/Claude API Prompt Caching]]).

## 4. Decision Table

| Observed Failure | Use First | Do Not Use First |
|---|---|---|
| Agent forgets a user/project preference next session | memory store with provenance and scope | larger prompt |
| Agent loses current workflow step after pause | durable state/checkpoint | transcript replay |
| Agent hits context limit in one thread | compaction or handoff | vector memory |
| Old file reads/logs dominate context | tool-result clearing, observation masking | whole-transcript summary |
| Tool definitions bloat context before work starts | on-demand tool discovery | upfront schema injection |
| Agent needs exact artifact | artifact store + pointer | summary |
| Agent cannot find relevant code | file/block/line retrieval evals | memory writes |
| Whole-corpus or global questions | graph index with community summaries | top-k vector retrieval |
| Agent repeats bad workflow | learned rule, skill, trajectory memory | more raw history |
| Memory store accumulates duplicates/stale facts | dream/consolidation job | more recall |
| Many reusable procedures exist | Agent Skills / skill library | one huge system prompt |
| Irrelevant memories injected every turn | retrieval gating and memory ranking | bigger recall budget |
| Untrusted web/doc content asks to persist instructions | quarantine + review gate | direct memory write |

Failure-mode-first design has empirical grounding in multi-workload evaluation ([[sources/Are We Ready For An Agent-Native Memory System]]). The tool-discovery row is quantified: the GitHub MCP server costs over 4,600 tokens for 26 tools, and on-demand tool requests cut token consumption 98% on APIBank ([[sources/MCP-Zero]], [[sources/ScaleMCP]]).

## 5. Provider / System Patterns

| System | Pattern | Technical Distinction |
|---|---|---|
| Anthropic / Claude Code | compaction + clearing + memory + JIT retrieval | cleanest split by context-growth type; API-native compaction is readable text with a pause hook; cache-ordered three-layer prompts |
| Anthropic Managed Agents | memory stores + dreams + multiagent orchestration | dreams produce a separate reviewable output store; shared stores with read-only/read-write authority, optimistic concurrency, versioned audit |
| OpenAI / Codex | stateless loop + provider-native compacted items | `type=compaction` item can include opaque encrypted content; SDK session wrapper; compaction can block streaming |
| Cursor | harness-level dynamic context + learned rules | context strategy evaluated per model/harness; Bugbot rules at production scale |
| Manus | cache-first harness engineering | KV-cache hit rate as the governing metric; logit masking over mid-loop tool removal; filesystem as restorable external context; recitation |
| Cloudflare Agent Memory | managed memory profile | constrained remember/recall/list/forget API; multi-channel retrieval; asynchronous post-ingestion improvement |
| Zep | managed ingestion/retrieval service | bi-temporal knowledge graph with validity intervals and point-in-time queries; explicit boundary rubric for file memory; query-adaptive context assembly under a fixed budget |
| Google ADK | durable workflow state + context compression | state schema is authoritative; sliding-window compaction maintains event history |
| LangChain / ContextHub | versioned context repository | context, skills, policies, examples, memories as collaborative assets; delta checkpoints |
| Letta Code | durable agent identity + MemFS + dream subagents | memory-first harness descending from MemGPT; compaction event triggers reflection |
| Amp | handoff over repeated compaction | new focused thread with goal, prompt draft, and relevant files |

## 6. Evaluation Matrix

| Capability | Evaluation Question | Source Pattern |
|---|---|---|
| Compaction continuity | Can the agent continue the task, preserve the artifact trail, and follow prior decisions? | [[sources/Factory Context Compression Evaluation]] |
| Context growth | Does performance degrade as irrelevant/long context grows? | [[sources/LOCA-bench]], [[sources/Letta Context-Bench]] |
| Retrieval | Does the agent retrieve the right file, block, and line? | [[sources/ContextBench]] |
| Long-term memory and forgetting | Accuracy over sustained histories; preference for newer facts over superseded ones; abstention when memory lacks the answer | [[sources/LongMemEval]] |
| Cost / latency | Token cost, blocking compaction latency, throughput, prompt-cache hit rate, construction (write-path) cost, energy per correct answer, footprint growth slope | [[sources/The Complexity Trap]], [[sources/Parallel Context Compaction]], [[sources/Agent Memory Characterization]], [[sources/Manus Context Engineering]], [[sources/TokenPilot]] |
| Dreaming / consolidation | Do background reflections remove duplicates, resolve contradictions, preserve provenance, and improve later success? | [[sources/Anthropic Managed Agents Dreaming Outcomes]], [[sources/Google ReasoningBank]], [[sources/Trajectory-Informed Memory Generation]] |
| Skills | Does skill loading improve outcome, can the agent select the right skill from a library, and does a candidate edit improve held-out validation before acceptance? | [[sources/SkillsBench]], [[sources/Agentic Skills in the Wild]], [[sources/SkillOpt]], [[sources/OpenAI Eval Skills]] |
| Memory safety | Can untrusted content poison memory, trigger unsafe tools, or bypass authority boundaries? | [[sources/Agent Security Bench]], [[sources/AgentDojo]], [[sources/InjecAgent]], [[sources/Memory Poisoning Attacks in LLM Agents]] |
| Shared memory | Do agents amplify false memories or resolve conflicting shared state? Do scope, supersession, provenance, and propagation rules hold under governance testing? | [[sources/When Agents Misremember Collectively]], [[sources/AgentNet]], [[sources/G-Memory]], [[sources/Governed Shared Memory for Multi-Agent LLM Systems]] |

The cost row measures the write path as well as the read path. On 1.8M tokens of history and 300 queries, construction wall time runs from under a minute for deterministic indexing to about 3.9 hours (SimpleMem) and 13.3 hours (Letta); LLM-mediated systems carry a 28-47x energy premium per correct answer over flat BM25 retrieval, and agentic stores scale super-linearly as each ingestion re-reads a growing store ([[sources/Agent Memory Characterization]]).

## 7. Practical Build Order

```text
P0:
  stable_prefix + append-only tail ordering
  event_log + artifact_store + durable_workflow_state
  recent_verbatim_window
  structured_text_compaction         # schema keeps failed attempts
  tool-result clearing for bulky outputs

P1:
  memory_store with provenance/scope/expiry/supersession
  recall gated by task need
  compaction-triggered memory ingestion with poisoning filters
  cache breakpoint on the compaction artifact
  continuation probes + user-visible list/forget/export

P2:
  dream/consolidation job producing reviewable output store
  Agent Skills registry with progressive disclosure
  validation-gated skill/tool promotion
  file/block/line retrieval evals
  trajectory memory grounded in external evaluation signals

P3:
  provider-native and parallel compaction
  budget-controlled compression, then failure-driven compressor optimization
  learned compression-timing policies + model-internal compression
  graph and temporal substrates; abstraction-keyed retrieval
  reversible full-fidelity archives
  multi-agent shared-memory governance and conflict resolution
```

Evidence behind the defaults: stable prefix plus append-only tail is the cheap path ([[sources/Claude API Prompt Caching]]); erasing failure evidence removes the model's ability to update its beliefs ([[sources/Manus Context Engineering]]); a fixed token-threshold trigger is the right starting point and the baseline learned policies are evaluated against ([[sources/SWE-MeM]]: 43.4% and 60.2% resolve rates on SWE-Bench Verified with 4B and 30B models); extraction-and-consolidation pipelines drastically cut cost versus full-context replay on vendor-reported benchmarks ([[sources/Mem0]]); heavy LLM-mediated ingestion pays off only when enough queries amortize each write ([[sources/Agent Memory Characterization]]); reversible archives change what counts as safe eviction ([[sources/VISTA Latent Context Managers]]: Gemini-3-Flash lifted from 22.7 to 50.7% on LOCA-Bench).

## 8. Safety Controls

Memory turns a one-turn contamination into a durable state problem: a poisoned write outlives the turn that planted it ([[operations/agent memory]], [[sources/Memory Poisoning Attacks in LLM Agents]]).

The attack surface maps onto the recommended write channels. [[sources/Memory Poisoning Attacks in LLM Agents]] maps six attack classes onto four write channels — explicit instruction-executed write, system prompt-driven write, compaction-driven write, and experience-to-procedure — the last two being the ingestion and skill-promotion paths above. Its MPBench numbers quantify the capability-security tension: the more aggressive test agent averaged 66.67% attack success versus 34.25% for the conservative one, and the best off-the-shelf guardrail detected 84.44% of strong-signal attacks but only 42.50% of weak-signal ones.

Controls from the graph, several with named production mechanisms:

- Separate trusted long-term memory from untrusted retrieved content; add compaction filters that separate them before summarization.
- Track provenance, timestamp, writer identity, write authority, expiry, and scope (user, project, repo, team, task) on every memory.
- Quarantine web/tool/document content before durable instruction writes.
- Require review gates before memories affect high-authority actions, permissions, finance, deployment, or security decisions; review works as explicit process, not as an assumed benefit of a readable format ([[sources/Zep Markdown Is Not Agent Memory]]).
- Use supersession chains instead of silent overwrite; the production mechanism is bi-temporal fact invalidation with point-in-time queries ([[sources/Zep Temporal Knowledge Graph Memory]]).
- Audit for stale, adversarial, overfit, and low-value entries; evolution-style stores that retroactively rewrite entries ([[sources/A-MEM]]) need versioning underneath.
- Support list, forget, export, archive, and delete; separate redaction from deletion so secrets can be scrubbed without destroying the audit trail ([[sources/Claude Managed Agents Memory Stores]]).
- For shared/team memory, apply scoped retrieval, temporal supersession, provenance tracking, and policy-governed propagation ([[sources/Governed Shared Memory for Multi-Agent LLM Systems]]); a `read_write` shared store lets injected content become trusted memory in later sessions ([[sources/Claude Managed Agents Memory Stores]]).
- Treat skills like dependencies: review scripts, references, instructions, versions; the ClawHavoc marketplace incident is the evidence ([[sources/Koi Security ClawHavoc]]).
- For dreams, keep input stores immutable and make output stores reviewable before attachment.

## 9. Open Questions

- Opaque compaction quality is hard to audit; Anthropic's readable server-side block is the existing counter-design. The question narrows to whether opaque continuation artifacts perform well enough to justify losing the audit path ([[sources/Claude API Compaction]]).
- Memory ROI is measured but mostly by vendors: Mem0 reports 91% lower p95 latency and over 90% token cost savings versus full-context; Zep reports up to 18.5% accuracy improvement on LongMemEval with roughly 90% response latency reduction. Independent measurement reframes the question: a measured energy premium with construction dominating, and memory systems sometimes underperforming full-history retention on long-horizon tasks. Which workloads justify the premium is open ([[sources/Mem0]], [[sources/Zep Temporal Knowledge Graph Memory]], [[sources/Agent Memory Characterization]], [[sources/MAGE Memory Execution State Management|MAGE]]).
- Write timing: Deferred Memory — postponing construction until sufficient context, evidence, or future utility exists — is a named research direction with no published guidance yet ([[sources/Memora]]).
- Governance UX is immature: understandable review, deletion, provenance, and scope controls.
- Negative transfer: learned rules, tips, and memories go stale or overgeneralize; validation-gated promotion exists on the skills side ([[sources/SkillOpt]]), an equivalent gate for fact and trajectory memories remains open.
- Multi-agent shared memory has narrowed from gap to frontier: constructive designs and governance primitives exist, production evidence and cross-provider conflict-resolution semantics do not ([[sources/G-Memory]], [[sources/Governed Shared Memory for Multi-Agent LLM Systems]]).
- Vendor benchmark scores are incomparable: on LongMemEval, Mem0's 2026 algorithm self-reports 94.4 while multi-workload evaluation measures Zep at 48.0 LLM Judge Accuracy ([[sources/Are We Ready For An Agent-Native Memory System]]).

## 10. Source Spine

Primary maps: [[maps/Context Management Map]], [[maps/Agent Skills Map]], [[maps/Recent Agent Operating Concepts]], [[maps/Safety Map]]. Supporting local notes: [[operations/agent memory]], [[operations/durable sessions]].

High-weight source cards:

- [[sources/Cognitive Architectures for Language Agents]]
- [[sources/MemGPT]]
- [[sources/Anthropic Context Engineering Cookbook]]
- [[sources/Claude API Compaction]]
- [[sources/Claude API Prompt Caching]]
- [[sources/OpenAI Codex Agent Loop]]
- [[sources/Manus Context Engineering]]
- [[sources/Cloudflare Agent Memory]]
- [[sources/Zep Markdown Is Not Agent Memory]]
- [[sources/Zep Temporal Knowledge Graph Memory]]
- [[sources/Mem0]]
- [[sources/Memora]]
- [[sources/HippoRAG]]
- [[sources/Claude Managed Agents Memory Stores]]
- [[sources/Anthropic Managed Agents Dreaming Outcomes]]
- [[sources/Google ReasoningBank]]
- [[sources/Google ADK Durable Agents]]
- [[sources/MAGE Memory Execution State Management]]
- [[sources/Letta Code Memory Docs]]
- [[sources/Agent Skills Specification]]
- [[sources/Comprehensive Survey on Agent Skills]]
- [[sources/Context Rot]]
- [[sources/LongMemEval]]
- [[sources/Agent Memory Characterization]]
- [[sources/Are We Ready For An Agent-Native Memory System]]
- [[sources/The Complexity Trap]]
- [[sources/Factory Context Compression Evaluation]]
- [[sources/Memory Poisoning Attacks in LLM Agents]]
- [[sources/Koi Security ClawHavoc]]
- [[sources/Memory in the Age of AI Agents]]
