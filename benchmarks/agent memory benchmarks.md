# Agent Memory Benchmarks

This is the comparison spine for agent-memory evaluation, not a leaderboard. The benchmark determines which memory ability is under test; the model, harness, memory implementation, context and retrieval budgets, judge, runs, and cost basis determine what a reported score means. Builder guidance and system design live in [[operations/agent memory]], with fuller synthesis in [[reports/Agent Memory Report]] and [[reports/Agent Memory Technical Brief]].

## Capability Registry

| Ability family | Current anchor and split | Scale | Task form | Primary outputs |
|---|---|---|---|---|
| Conversational recall and narrative continuity | [[sources/LoCoMo]]; current public `locomo10` release | 10 conversations; 5,882 turns; 1,986 QA annotations; 19–32 sessions | QA, event-graph summarization, multimodal continuation over human-edited synthetic conversations | QA partial-match F1; retrieval accuracy for RAG analyses; atomic-fact summary F1; separate generation metrics |
| Multi-session extraction, reasoning, updates, and abstention | [[sources/LongMemEval]]; Standard 500-question reference, with S/M history scales | 500 questions; histories designed to scale from roughly 115K to 1.5M tokens | QA over timestamped multi-session user–assistant histories | Accuracy under the pinned judge and prompt; ability slices for extraction, multi-session reasoning, temporal reasoning, update, and abstention |
| Extreme-scale conversational memory | [[sources/BEAM]]; arXiv v2 / ICLR 2026 release | 100 conversations; 2,000 probes; release bands 128K, 500K, 1M, and 10M (result tables label the first band 100K) | Two probes for each of ten memory abilities per conversation | Nugget score for nine abilities; Kendall tau-b for event ordering |
| Incremental memory operations | [[sources/MemoryAgentBench]]; arXiv v4 / ICLR 2026 release | 2,071 questions; average histories 103K–1.44M tokens | Chunk-by-chunk ingestion followed by repeated probes of retrieval, test-time learning, global understanding, and selective forgetting | Accuracy, F1, Recall@5, and task-specific LLM-judge scores; macro competency averages |
| Interdependent memory-guided action | [[sources/MemoryArena]]; arXiv v1 paper and HF test@`da1a37c` | Paper v1: 766 claimed in Table 1, 736 implied by Table 2; pinned HF test: 701 rows (150/270/221/40/20). Paper Table 1 reports 6.9 subtasks and 57 steps on average | Shopping, group travel, progressive search, and formal reasoning in fresh but causally linked sessions | Task success, progress, soft progress, success at dependency depth, and latency |
| Environment experience and procedural runbooks | [[sources/LongMemEval-V2]]; work-in-progress public release | 451 manually curated questions; up to 500 trajectories and 115M tokens per history | QA over prior environment interactions: state, dynamics, workflows, gotchas, and premise awareness | Context-gathering accuracy plus query latency; task and domain slices |

These rows are complementary. LoCoMo or LongMemEval success does not establish test-time learning, prospective activation, or correct action. MemoryAgentBench makes construction and updating incremental but still ends in probes. MemoryArena tests whether memory changes later behavior. LongMemEval-V2 tests whether an agent can recover operational experience from its environment rather than only user facts.

## Configuration Registry

“Not standardized” means the benchmark can be—and routinely is—run under different configurations. It is a required field for a result record, not permission to omit it.

| Benchmark | Model and harness in anchor paper | Judge or metric | Ordinary run count | Cost basis |
|---|---|---|---|---|
| LoCoMo | Multiple 2024 base, long-context, and RAG configurations; no single benchmark harness | Original QA uses partial-match F1; event summaries use atomic-fact scoring; later system papers often substitute their own LLM judge | Not standardized; original repeated-run count not reported | Not standardized; original paper does not report end-to-end cost |
| LongMemEval | Benchmark paper spans commercial assistants, long-context readers, and retrieval pipelines | Prompt-engineered LLM judge plus ability slices; pin judge model and prompt for comparison | Not standardized | Not standardized |
| BEAM | Long context, full-corpus RAG, and LIGHT across four readers. At 10M, vanilla uses the largest supported recent tail; RAG uses a full turn-pair index plus top-5 retrieval into a 32K reader; LIGHT uses a full-history index and scratchpad plus recent working memory in a 32K reader | LLM-scored nuggets; event ordering uses an LLM equivalence detector plus Kendall tau-b; judge identity not reported | Not reported | Not reported |
| MemoryAgentBench | Standard incremental wrapper; most RAG and external-memory rows use GPT-4o-mini, while long-context backbones vary | Mostly exact task metrics; GPT-4o judge for LongMemEval and summarization subsets | Not reported | Partial estimated per-query table only; assumes November 2025 OpenAI prices/caching and excludes indexing |
| MemoryArena | Unified memory adapter and environment loop; main memory comparison uses GPT-5.1-mini as task agent | Task-specific environment checks; SR, PS, sPS, SR@depth, and latency; no single judge | Not reported | Retrieval frequency is specified, but monetary ingest/retrieval/answer cost is not reported |
| LongMemEval-V2 | Agent-controlled file/search baselines and author systems; model, controller, and search policy are coupled | Task-specific answer checking plus latency | Not standardized; use the release's per-system disclosure | Query latency reported; monetary ingest/search/answer cost not standardized |

## Result Intake Contract

Every score added to this vault should carry the fields below. If a paper omits one, record `not_reported`; do not infer it from a model or provider default.

```yaml
benchmark: ""
benchmark_version: ""
artifact_revision: ""
split: ""
ability_slice: ""
history_scale: ""
model: ""
harness: ""
memory_system: ""
context_budget: ""
retrieval_budget: ""
judge_or_verifier: ""
metric: ""
run_count: ""
ingest_cost: ""
retrieval_cost: ""
answer_cost: ""
latency: ""
result_owner: "author | vendor | independent"
source: ""
```

Do not compare headline scores unless benchmark version and split, task subset, model, harness, context budget, retrieval budget, judge, and run count match. Report cost as ingest + retrieval + answering under a dated price basis; token savings alone are not economic evidence.

## Adjacent Evaluation Axes

The core registry above does not cover every memory failure. Use [[sources/Toward Reliable Context Compression for Long-Horizon Agents|TRACE]] for boundary-local compaction continuity; [[sources/Keep It InMind]] for indirect application after successful storage; [[sources/PM-Bench]] for prospective activation; [[sources/MemOps]] for operation-level state trajectories; [[sources/Skill-Use]] for procedural Trigger, Compliance, and Boundary; [[sources/When Memory Becomes Authority]] for authority preservation; [[sources/HarnessSafe]] for delayed carrier reactivation; and [[sources/Deployment-Time Memorization in Foundation-Model Agents]] for deletion residue across derived tiers. Serving economics belongs on a separate configuration-specific curve anchored by [[sources/Total Recall at What Cost]], not inside an accuracy leaderboard.

## Related

- [[benchmarks/agent evaluation]]
- [[benchmarks/long-horizon benchmarks]]
- [[operations/agent evals]]
- [[operations/agent memory]]
- [[maps/Context Management Map]]
- [[reports/Agent Memory Report]]
- [[reports/Agent Memory Technical Brief]]
