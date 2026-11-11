---
title: "State of Agents Research Update — November 9, 2026"
aliases: ["November 2026 Research Update"]
tags: [research-update, harness, code-factories, multi-agent, memory, cyber]
created: 2026-11-09
updated: 2026-11-09
---

# State of Agents Research Update — November 9, 2026

The most useful change since the vault's earlier synthesis is the growing ability to **modify the machinery around an agent while it works, then carry selected improvements into later work**. Harness code, optimizer experience, memory representations, coordination stores, and factory workflows are now distinct objects of experimentation. Evidence also increasingly measures what those changes break or cost.

This is a targeted catch-up across five areas, prioritizing September–November 2026. It combines three delegated review tracks with cross-cutting literature and incident review. Earlier omissions are dated explicitly; discovery in this sweep does not make an older paper new. Primary texts and technical documentation were read, but experiments were not independently reproduced. The existing September reports remain dated baselines with links to these extensions.

The update adds **53 source cards and five topic reports**, with links into the existing maps, concepts, methods, and benchmark notes. This includes seven papers from the user-supplied DAIR catalog, documented in [[reports/DAIR Paper Review - 2026-11-09]], 14 sources in the October cyber follow-up, and the inspectable [[systems/HumanLayer]] implementation. Unreviewed leads remain separate from incorporated findings.

## Five Reading Paths

| Area | Start here | Main change to the research project |
|---|---|---|
| Harness self-improvement | [[reports/Harness Self-Improvement Update - 2026-11-09]] | Separate active-task changes, retained improvement experience, and evidence of transfer. |
| Code factories | [[reports/Code Factories Update - 2026-11-09]] | Study integration, delivered value, and evaluation ownership alongside code production. |
| Multi-agent research | [[reports/Multi-Agent Research Update - 2026-11-09]] | Compare discovery sharing and selective retrieval with independent search and simpler architectures. |
| Memory and dreaming | [[reports/Memory and Dreaming Update - 2026-11-09]] | Treat consolidation as a separately evaluated transformation with a deployment lifecycle. |
| Cyber swarms and attacker findings | [[reports/Cyber Swarms and Attacker Findings - 2026-11-09]] | Separate observed deployments, authorization failures, research capabilities, and delivered remediation. |

## What Is Newly Possible or Better Specified

**Harness changes during execution.** [[sources/BOXBOX]] exposes executable hot reload; [[sources/Harness2]] separates current-task adaptation from reusable improvement experience. These are concrete mechanisms, with different persistence boundaries. Neither alone demonstrates indefinite improvement. Read alongside [[sources/Beneath the Surface Agent Evolution]] for preservation-aware evaluation.

**A factory can generate its own work and alter its own measurement process.** [[sources/Instant Software Factories]] makes that feedback loop explicit. The resulting research question is how to measure independently valuable, validated delivery when issue creation and CI changes are themselves agent outputs. This strengthens the need to inspect integration and delayed failures, not merely count merged changes.

**Collaboration can reuse discoveries while exploration is still underway.** [[sources/Scaling Discovery through Test-Time Communication]] supplies controlled evidence beyond simple task division. [[sources/ScaleMAS]] instead changes what shared work each agent retrieves. Both expand the architecture space; their evaluation protocols still need careful interpretation.

**Dreaming has concrete representations and lifecycle semantics.** [[sources/Anthropic Components of Agent Memory]] studies transcript correction and wiki construction. [[sources/Claude Managed Agents Dreams Lifecycle]] documents a separate candidate output store, which can exist before successful completion. This makes review and promotion distinct from the background computation itself.

**Improvement and preservation are separate outcomes.** [[sources/MemCode]] and [[sources/Complementary Memory Curation and Consolidation]] expose memory trade-offs; [[sources/Retrospective Harness Adaptation Study]] checks later behavior rather than accepting plausible advice. Aggregate scores need a record of lost capabilities and newly introduced errors.

**The same mechanisms now appear in adversarial deployments.** [[sources/Google ARTEX Offensive Frameworks in the Wild]] supplies incident-response evidence for delegated cyber operations; [[sources/Calif PHP2Shell Research]] connects reusable skills to vulnerability research. The cyber update distinguishes these from rogue-agent incidents and evaluates the full path from a reported finding to deployed remediation.

## A Shared Research Model

This cycle is the project's proposed research model; individual sources implement different subsets.

| Step | Research artifact | Decision |
|---|---|---|
| Observe | Execution traces and independently checked outcomes | Which recurring problem merits a change? |
| Propose | Candidate harness, memory, skill, or coordination revision | What changes, and for how long? |
| Evaluate | Gains, regressions, and complete cost | Does the candidate improve the intended outcome? |
| Promote or reject | Versioned candidate or retained prior version | Which evidence supports the choice? |
| Recheck | Later-task results and retained failure history | Does the change remain useful as tasks evolve? |

For every claimed improvement, record **what changed, what persisted, what evaluated it, and what remained outside its control**. Add the reuse horizon: a change can pay on the current task, amortize only after many tasks, or improve the optimizer without improving the deployed agent. The topic reports contain the supporting distinctions and narrower experiments.

The same accounting applies across areas. Candidate-generation cost belongs to harness search; wiki construction belongs to memory; selection and communication belong to teams; integration, review, and escaped defects belong to factories. Report foreground latency separately from total resource use.

## Next Research Priorities

These are proposed investigations, not results from the source papers.

1. **Retention and transfer:** compare a frozen baseline, memory-only adaptation, harness-only adaptation, and both, on later tasks held out from improvement. Count new successes and lost successes separately.
2. **Dreaming economics:** hold raw history and retrieval tools fixed; compare unconsolidated notes with candidate memory revisions over different numbers of future queries. Include temporal accuracy, source attribution, and revision cost.
3. **Communication value:** compare one agent, independent parallel agents, and communicating agents under declared budgets. Score the answer actually selected for delivery, not only the best candidate produced.
4. **Factory outcome measurement:** track independently chosen work through implementation, integration, release, and a follow-up failure window. Separate agent-created backlog and changes to the evaluator.
5. **Simplification after model changes:** repeat the same tests after removing obsolete instructions, subagents, or stored procedures. Retain complexity only when the comparison supports it.
6. **Cyber outcome attribution:** distinguish intended-task success, unauthorized effects, and verified repair. Measure the operator's contribution and the persistence of campaign state across runs.

## Evidence Discipline and Remaining Coverage

- **Research experiments** establish results under the reported model, task split, budget, and scorer. Most new papers are preprints.
- **Vendor experiments and operator reports** establish documented observations and implementation choices, with limited independent validation.
- **Living documentation** establishes the contract checked on November 9, not the historical release date or measured effectiveness.
- **Queued leads** have verified primary metadata but incomplete full-text review. They remain outside the source-card evidence base until reviewed.

The sweep does not establish broad production return on investment, reliable autonomous research across domains, or unbounded self-improvement. Its strongest contribution is a more testable map of the mechanisms now available and the evidence needed to retain them.

Continue at [[maps/Frontier Reading Queue]] for the remaining November leads; use [[maps/Self-Improving Systems Map]], [[maps/Code Factory Playbook]], [[maps/MAS Orchestration and Architecture]], and [[maps/Context Management Map]] for durable navigation.
