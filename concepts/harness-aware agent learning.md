---
title: "Harness-aware agent learning"
aliases:
  - "harness-aware learning"
tags:
  - agents/learning
  - agents/harnesses
created: 2026-10-05
updated: 2026-10-05
---

# Harness-aware agent learning

An agent learns through a system that selects observations, builds context, executes tools, manages sessions, and evaluates outcomes. Those choices determine the experience available for improvement. Track what changes and how it is validated before calling a system self-improving.

## Three Different Update Targets

| Target | What persists | Representative evidence | Evaluation question |
| --- | --- | --- | --- |
| Memory and skills | Reflections, facts, procedures, executable skills | [[sources/Reflexion]], [[sources/Voyager]], [[sources/Google ReasoningBank]] | Does experience improve later tasks without preserving stale or misleading guidance? |
| Harness | Prompts, routing, context policy, search strategy, executable control code | [[sources/Meta-Harness]], [[sources/Darwin Godel Machine]], [[sources/AIDE2 Recursive Self-Improvement]] | Do selected code changes generalize beyond the selection tasks under matched budgets? |
| Model parameters | Updated weights or adapters | [[sources/SWE-RL]], [[sources/Agent Lightning v1.0]], [[sources/SCLATE]] | Does the trained policy work in the deployment harness and transfer beyond training? |

These mechanisms can coexist. Recording a memory is not a weight update; training inside a harness does not establish harness self-modification. Likewise, offline harness optimization and post-deployment adaptation differ in when feedback arrives and when accepted changes affect users.

## Research Lineage

Reflexion (2023) establishes feedback stored as language across retries; Voyager (2023) retains executable skills across tasks. They are research antecedents for persistent experience, preceding current vendor memory and skill surfaces. Their environments and storage mechanisms differ from today's products.

SWE-RL (2025) provides a parameter-training branch; SICA and Darwin Gödel Machine (2025) provide executable self-modification branches. Meta-Harness (2026) makes the harness an explicit optimization object. The distinction remains useful when reading [[sources/AIDE2 Recursive Self-Improvement]]: improved research performance does not establish a better recursive self-improver.

[[sources/Agent Lightning v1.0]] keeps the deployed harness in charge while training the model through recorded calls. [[sources/SCLATE]] extends the experimental unit across session boundaries, scheduled events, and memory maintenance. A vendor release can make an existing mechanism accessible without originating its research idea; chronology or similarity alone does not establish direct influence.

## Experimental Contract

Record the initial and updated model, harness version, memory state, environment, task order, budget, acceptance rule, and held-out population. Keep selection data separate from evaluation, and compare against simpler or native-memory baselines. [[sources/SCLATE]] shows why adding an external memory system is not an automatic gain.

Choose whether a score describes a complete system or an underlying component. [[sources/Agent Evaluation Reliability]] shows that additional tasks do not remove uncertainty from limited harness coverage. [[concepts/memory use calibration]] adds a separate check on how the model applies the experience it receives.

## Related

- [[concepts/lifelong agent learning]]
- [[concepts/reasoning memory]]
- [[concepts/procedural memory]]
- [[methods/self-improving code loops]]
- [[methods/multi-agent learning]]
- [[operations/agent evals]]
- [[sources/SICA Self-Improving Coding Agent]]
- [[sources/Adaptive Auto-Harness]]
