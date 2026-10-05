---
title: "Persistent Personal Agents"
aliases:
  - "Persistent personal assistants"
  - "Persistent personal assistant agents"
tags:
  - agents/personal
  - agents/long-horizon
created: 2026-10-05
updated: 2026-10-05
---

# Persistent Personal Agents

A persistent personal agent is a continuing delegate for a person: it retains relevant context, carries responsibilities across conversations, and acts through connected tools or environments. The enduring unit is the relationship and its open commitments. Individual tasks, model calls, and execution environments can start and stop within it.

This is an analytical category for the vault, not a standardized industry label. [[systems/personal assistant agents]] compares current products. A role shared by a team is an adjacent form of persistent delegate; record who owns the role and whose authority applies to each action.

## Separate the Dimensions

| Dimension | What it establishes | What it does not establish |
|---|---|---|
| Personal continuity | Context, preferences, and corrections associated with a person | Complete, current, or correctly scoped memory |
| Persistent responsibility | An obligation can survive an individual conversation | A continuously running model or an indefinitely valid instruction |
| Background execution | Work can progress outside the foreground exchange | Useful initiative or recovery after a crash |
| Proactivity | A policy decides whether to initiate useful help | Permission to take every suggested action |
| Context awareness | Connected observations inform assistance | A need to observe everything or share it across channels |
| Mixed initiative | Person and agent can redirect, ask, act, or take over | That approval of one action grants continuing authority |

These are independent axes. An assistant can run a fixed schedule without inferring a new need. An ambient interface can observe context while taking no actions. A task-specific agent can run overnight without maintaining a continuing personal relationship. See [[concepts/background agents]], [[concepts/event-driven agents]], and [[operations/durable sessions]].

## Research Questions Before Product Packaging

| Question | Research trail | Remaining distinction |
|---|---|---|
| When should the assistant act, ask, or wait? | [[sources/Principles of Mixed-Initiative User Interfaces]] (1999); [[sources/Proactive Agent]] (2024) | A decision framework and an assistance benchmark offer different evidence |
| When is an interruption worth its cost? | [[sources/Learning and Reasoning about Interruption]] (2003); [[sources/ProAgentBench]] (2026) | Predicting a convenient moment differs from causing a useful outcome |
| Which proposed goals become commitments? | [[sources/A Cognitive Framework for Delegation to an Assistive User Agent]] (2005); [[sources/PM-Bench]] (2026) | Retaining a fact differs from carrying out, revising, or canceling an intention |
| How should understanding of the person change? | [[sources/Generative Agents]] (2023); [[sources/LongMemEval]]; [[sources/HorizonBench]] (2026) | Recall, simulated behavior, and adaptation to changed preferences are separate tests |
| Can an intention become a correct external result? | [[sources/Mind2Web]] (2023); [[sources/OSWorld]] (2024) | Offline action prediction differs from execution and long-term service quality |

This is a research lineage by problem, not a claim of implementation ancestry. Product-specific citations and disclosed architecture belong in source cards. [[sources/Meta Muse Security Architecture]], for example, explicitly references [[sources/Willison Lethal Trifecta]]; the general resemblance of another product to a paper does not demonstrate adoption.

## Design and Evaluate the Continuing Relationship

Treat remembered facts, inferred preferences, accepted responsibilities, current permissions, and pending actions as different state. A preference may help rank options without authorizing a purchase. A canceled responsibility must stop future wakeups and obsolete delegated work, even if its history remains useful context.

Evaluate repeated use with changing priorities, quiet periods, revoked access, delayed results, and corrected assumptions. Measure completed useful obligations, missed and unnecessary interventions, stale actions, duplicate effects, correction uptake, total cost, and human time spent supervising or repairing results. A strong isolated-task benchmark does not establish that the assistant reduces work over weeks.

For a builder, this relationship layer can sit above an existing harness. [[methods/agent runtime selection]] separates the execution machinery one can reuse from product responsibilities one still owns. A portable record of commitments, source references, authorization, and results is more durable than depending on a provider's transcript format alone.

## Related

- [[systems/personal assistant agents]]
- [[concepts/agent loop]]
- [[concepts/memory use calibration]]
- [[concepts/shared agent memory]]
- [[concepts/human-in-the-loop agents]]
- [[maps/Agent Capability Research Lineage]]
