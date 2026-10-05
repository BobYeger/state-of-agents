---
title: "Memory use calibration"
aliases:
  - "calibrated memory use"
  - "memory overuse and underuse"
tags:
  - agents/memory
  - agents/evaluation
created: 2026-10-05
updated: 2026-10-05
---

# Memory use calibration

Memory use calibration concerns how strongly recalled information should affect the current decision. A correct fact can be irrelevant; a relevant preference may be advisory; a current constraint may govern the answer. Retrieval quality alone cannot distinguish these cases.

[[sources/MemCalib]] operationalizes this as Ignore, Bound, or Control for individual propositions and evaluates overuse and underuse separately. Its training method changes model weights; it does not itself provide a persistent memory store.

## Distinctions To Preserve

| Question | Failure if omitted | Related evidence |
| --- | --- | --- |
| Was the right evidence retrieved? | Relevant context never reaches the model | [[sources/LongMemEval]], [[sources/LongMemEval-V2]] |
| Is it still current? | Superseded or forgotten facts affect the decision | [[sources/MemOps]], [[concepts/versioned context]] |
| How much should it influence this task? | Irrelevant details dominate, or governing constraints are ignored | [[sources/MemCalib]] |
| Does it authorize the action? | A remembered observation becomes a standing instruction | [[sources/When Memory Becomes Authority]], [[operations/permissions]] |

For example, remembering that someone prefers short meetings can help schedule a routine discussion. It should not silently truncate the explicit duration of a workshop they have just requested. Whether the agent may send an invitation is a separate authorization question.

## Research Lineage And Evaluation

[[sources/Reflexion]] and [[sources/Google ReasoningBank]] ask how experience becomes reusable guidance. [[sources/LongMemEval]] adds update and abstention tests; [[sources/MemOps]] distinguishes memory-state operations; [[sources/When Memory Becomes Authority]] tests permitted use after consolidation. These are related research problems, not interchangeable benchmark scores or evidence that later products adopted a particular paper.

When evaluating a memory pipeline, test retrieval and downstream behavior separately. Include outdated, irrelevant, weakly supported, and currently controlling propositions in the same context. Check both unnecessary influence and missed constraints, and preserve provenance through compression. An apparent improvement obtained by ignoring all memory can fail authorized or useful personalization; indiscriminate retention can fail freshness and scope.

## Related

- [[concepts/harness-aware agent learning]]
- [[concepts/lifelong agent learning]]
- [[concepts/reasoning memory]]
- [[concepts/context retrieval]]
- [[operations/agent memory]]
- [[benchmarks/agent memory benchmarks]]
- [[sources/SCLATE]]
