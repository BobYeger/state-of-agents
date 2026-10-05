---
title: "Personal Assistant Agents"
tags:
  - agents/personal
  - systems/categories
created: 2026-10-05
updated: 2026-10-05
---

# Personal Assistant Agents

This category tracks user-facing agents that maintain a continuing relationship, context, and delegated responsibilities. The durable concept is [[concepts/persistent personal agents]]. Personal describes whose priorities and context organize the work; it does not restrict the category to household tasks.

These are products built on harnesses. Their application category is separate from the implementation classes in [[maps/Harness Tracker]]: a hosted personal assistant does not become a reusable harness or framework merely because it exposes tools, skills, and scheduled work.

## Current Product Comparison

Snapshot: October 5, 2026. These are documented or marketed capabilities, not a comparative performance ranking.

| Product | Center of the experience | Execution and continuity | Evidence boundary |
|---|---|---|---|
| [[sources/OpenAI Dots]] | A continuing assistant that can delegate work | Cloud computer, saved context, background tasks, and continuity across contact methods | Official living documentation; gradual rollout, exact initial release date unverified |
| [[sources/Grok Bot]] | A roster of durable specialist teammates, including personal and team modes | Persistent computer use, role memory, coordination, skills, and routines | August 11 launch; later team contracts differ from personal-roster sharing; no comparative longitudinal evaluation |
| [[sources/Instinct Personal Assistant]] | A personal assistant reached through text and voice | Markets connected personal context, device actions, and proactive follow-up | Public product claims; model, harness, memory implementation, launch date, and current access restrictions unverified |
| [[sources/Meta Muse]] | A personal agent for tasks and continuing goals | Per-user cloud computer, saved memory, background work, and explicit permission architecture | September 8 launch; architecture disclosed, but base-model benchmarks do not measure the whole personal-agent experience |

Grok's shared Team Bots are adjacent to the personal-assistant subtype: the relevant principal and memory scope can be a team as well as a person. Avoid forcing both into an identical ownership model. Similarly, a product claiming to know the user does not disclose how preferences are learned, corrected, or enforced.

## What Research Supports the Category?

The most useful reading order starts with human–agent interaction, then adds memory and execution:

1. [[sources/Principles of Mixed-Initiative User Interfaces]] and [[sources/Learning and Reasoning about Interruption]] frame initiative and attention as decisions with costs.
2. [[sources/A Cognitive Framework for Delegation to an Assistive User Agent]] addresses negotiated delegation and continuing commitments.
3. [[sources/Proactive Agent]], [[sources/ProAgentBench]], [[sources/PM-Bench]], and [[sources/HorizonBench]] test initiative, intentions, and synthetic preference tracking under different protocols.
4. [[sources/LongMemEval]], [[sources/MemCalib]], and [[sources/Collaborative Memory]] separate remembering, appropriate use, and permission to share.
5. [[sources/OSWorld]] evaluates external computer-task results; [[sources/ReAct]] and [[sources/Cognitive Architectures for Language Agents]] supply broader loop and architecture foundations.

No reviewed evidence establishes that all four products implement these papers. Their relevance is to the mechanisms and failure modes. The Muse security account supplies an explicit practitioner citation and a concrete architecture; Instinct's reviewed pages leave implementation largely unspecified. Preserve that difference.

## Connection to Custom Agent Builders

The application still needs user identity, domain integrations, current permissions, open commitments, correction handling, and evidence that the outcome was achieved. A managed or embedded harness can supply the worker loop underneath it. Frameworks can connect such workers to explicit workflows and durable application state. The custom development question is which of these boundaries the product needs to own, evaluated on its actual workload. See [[methods/agent runtime selection]].

## Related

- [[systems/deployed agent products]]
- [[systems/agent frameworks and orchestration libraries]]
- [[maps/Builder Ecosystem Map]]
- [[maps/Agent Capability Research Lineage]]
- [[maps/Evaluation Map]]
