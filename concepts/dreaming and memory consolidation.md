# Dreaming and Memory Consolidation

Dreaming is a background memory-maintenance loop: an agent or separate process reviews past sessions, extracts recurring patterns, removes stale or duplicated memory, and writes improved memory for future runs.

The important design move is that learning happens between runs, not only inside the current context window. This makes memory reviewable, schedulable, and separable from task execution. Raw experience accumulates faster than it stays useful; consolidation is the step that turns accumulation into curation.

## Pattern

```text
raw memories / trajectories -> review process -> extract, merge, prune, generalize -> consolidated memory -> future sessions read it
```

## Consolidation Schedules

The main design decision is when consolidation runs, because the schedule determines cost, freshness, and how much unreviewed material future sessions can see.

| Schedule | How it works | Evidence | Tradeoff |
|---|---|---|---|
| On write | Every new memory is processed as it arrives; new entries can restructure existing ones. | [[sources/Mem0]]: salient facts extracted and consolidated inline from conversation; [[sources/A-MEM]]: new notes trigger evolution of linked existing memories | Memory is always current, but consolidation competes with task latency, and retroactive rewriting erases the original record |
| In-session reflection | The agent periodically synthesizes accumulated observations into higher-level inferences during operation. | [[sources/Generative Agents]]: reflection turns the memory stream into abstractions; ablations show removing it critically degrades behavior | Improves reasoning over experience, but consumes task-time context and compute |
| Between sessions | A scheduled background process reviews stores after runs complete. | [[sources/Anthropic Managed Agents Dreaming Outcomes]]: dreaming as a first-class managed-agent operating concept; [[sources/Letta Code Memory Docs]]: reflection-style subagents on durable agents | Zero task-time cost and reviewable output, but memory is stale between dreams |
| Offline trajectory mining | A separate pipeline mines completed trajectories for reusable lessons, skills, or reasoning strategies. | [[sources/Google ReasoningBank]], [[sources/Trajectory-Informed Memory Generation]], [[sources/SkillOpt]] | Strongest generalization per lesson; furthest from real time and needs its own evaluation loop |

## Output Target

Consolidation can rewrite the store in place or write to a fresh target. [[sources/Claude Managed Agents Memory Stores]] takes the second path: a dreaming session reads a fragmented store and consolidates into a new output store, which preserves the original as an audit record and makes the consolidation itself reviewable before anything depends on it. In-place evolution ([[sources/A-MEM]]) buys coherence at the cost of provenance — a reasonable trade for a private store, a poor one for shared memory, where consolidated output is exactly the material being promoted to team-wide trust (see [[concepts/shared agent memory]]).

## Failure Modes

- Consolidating garbage: consolidation generalizes whatever is in the store, including poisoned or overfit entries, and gives it the authority of a curated lesson. A review gate before consolidated memory reaches high-authority use is the control.
- Over-pruning: aggressive deduplication can remove failure evidence that future runs need in order to avoid repeating the mistake.
- Never running: without a schedule, stores degrade into append-only logs and retrieval quality decays — the fragmented-store state the dreaming session exists to fix.

## Related Sources

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

- [[operations/agent memory]]
- [[concepts/shared agent memory]]
- [[concepts/reasoning memory]]
- [[concepts/lifelong agent learning]]
- [[claims/Claim - Agent memory and skills create compounding improvement loops]]
