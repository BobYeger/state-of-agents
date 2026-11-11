# Dreaming and Memory Consolidation

Dreaming, in this note, is a background memory-maintenance loop: an agent or separate process reviews past sessions, extracts recurring patterns, removes stale or duplicated memory, and writes candidate memory for future runs. Improvement must be measured; rewriting is not itself evidence of learning.

The important design move is that adaptation happens between runs, not only inside the current context window. This makes memory reviewable, schedulable, and separable from task execution. Raw experience can accumulate faster than it stays useful; consolidation attempts to turn accumulation into curation.

The November evidence update is [[reports/Memory and Dreaming Update - 2026-11-09]]. Keep external-store rewriting distinct from training a consolidator ([[sources/Auto-Dreamer]]) and from updating the task model's weights ([[sources/Language Models Need Sleep]]). They require different artifacts, costs, and retention tests.

## Pattern

```text
raw memories / trajectories -> review process -> extract, merge, prune, generalize -> consolidated memory -> future sessions read it
```

## Consolidation Schedules

The main design decision is when consolidation runs, because the schedule determines cost, freshness, and how much unreviewed material future sessions can see.

| Schedule | How it works | Evidence | Tradeoff |
|---|---|---|---|
| On write | Every new memory is processed as it arrives; new entries can restructure existing ones. | [[sources/Mem0]]: salient facts extracted and consolidated inline from conversation; [[sources/A-MEM]]: new notes trigger evolution of linked existing memories | Reduces write-to-use delay, but competes with task latency; preserve the original record separately if edits overwrite it |
| In-session reflection | The agent periodically synthesizes accumulated observations into higher-level inferences during operation. | [[sources/Generative Agents]]: reflection turns the memory stream into abstractions; ablations show removing it critically degrades behavior | Improves reasoning over experience, but consumes task-time context and compute |
| Between sessions | A scheduled background process reviews stores after runs complete. | [[sources/Anthropic Managed Agents Dreaming Outcomes]]: dreaming as a first-class managed-agent operating concept; [[sources/Letta Code Memory Docs]]: reflection-style subagents on durable agents | Moves work off the foreground path and produces reviewable output, but still consumes compute and shared resources; memory can be stale between runs |
| Offline trajectory mining | A separate pipeline mines completed trajectories for reusable lessons, skills, or reasoning strategies. | [[sources/Google ReasoningBank]], [[sources/Trajectory-Informed Memory Generation]], [[sources/SkillOpt]] | Can generalize across sessions; further from real time and needs its own evaluation loop |

## Research Before Managed Services

[[sources/Generative Agents]] (2023) tests reflection over accumulated observations. [[sources/Sleep-time Compute]] (2025) tests a related but different mechanism: preparing persistent context before the next query. Its gains depend on the task, model, budget, and predictability of future questions; lower query-time computation does not establish lower total computation. The associated Letta blog explains the same research, not an independent replication.

[[sources/SCLATE]] (2026) extends evaluation to multi-session lifecycles, including scheduled memory work. [[concepts/harness-aware agent learning]] connects that lifecycle to training, while [[concepts/memory use calibration]] asks whether the resulting memories improve later decisions.

## Output Target

Consolidation can rewrite the store in place or write to a fresh target. [[sources/Claude Managed Agents Dreams Lifecycle]] documents the second path and the need to distinguish partial output from successful completion. In-place evolution ([[sources/A-MEM]]) needs explicit versioning if the original record must survive. Store layout alone does not guarantee provenance or safe promotion to [[concepts/shared agent memory]].

[[sources/MemCode]] supplies another design: archived records forward to replacement records while retaining source-span links. [[sources/Anthropic Components of Agent Memory]] treats representations and injected context as different maintenance targets. Retaining an archive and deciding what future sessions see are separate responsibilities.

## Measure the Rewrite

[[sources/Complementary Memory Curation and Consolidation]] measures an accuracy–compression trade-off, not a universal consolidation gain. [[sources/MemProbe]] motivates testing historical facts and source attribution separately from current-value accuracy. For a candidate rewrite, compare the same agent and future tasks against the original bank; record regressions, total compute, and the procedure for reverting the active revision.

## Failure Modes

- Consolidating garbage: consolidation generalizes whatever is in the store, including poisoned or overfit entries, and gives it the authority of a curated lesson. A review gate before consolidated memory reaches high-authority use is the control.
- Over-pruning: aggressive deduplication can remove failure evidence that future runs need in order to avoid repeating the mistake.
- Never reviewing: an append-only store can accumulate duplicates and stale entries; measure retrieval and task degradation before choosing a maintenance cadence.
- Partial-output promotion: a created output store may still be incomplete or belong to a failed job; gate promotion on completion and validation.
- Misleading cost claims: fewer active memory tokens or lower foreground latency need not offset construction and consolidation work.

## Related Sources

- [[sources/Anthropic Components of Agent Memory]]
- [[sources/Claude Managed Agents Dreams Lifecycle]]
- [[sources/Auto-Dreamer]]
- [[sources/MemCode]]
- [[sources/Complementary Memory Curation and Consolidation]]
- [[sources/MemProbe]]
- [[sources/Language Models Need Sleep]]
- [[sources/Anthropic Managed Agents Dreaming Outcomes]]
- [[sources/Claude Managed Agents Memory Stores]]
- [[sources/Generative Agents]]
- [[sources/Letta Code Memory Docs]]
- [[sources/SkillOpt]]
- [[sources/Trajectory-Informed Memory Generation]]
- [[sources/Google ReasoningBank]]
- [[sources/A-MEM]]
- [[sources/Mem0]]

## Related

- [[concepts/background agents]]
- [[concepts/harness-aware agent learning]]
- [[operations/agent memory]]
- [[concepts/shared agent memory]]
- [[concepts/reasoning memory]]
- [[concepts/lifelong agent learning]]
- [[claims/Claim - Agent memory and skills create compounding improvement loops]]
