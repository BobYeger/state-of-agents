---
title: "DAIR Paper Review — November 9, 2026"
aliases: ["DAIR Research Follow-up"]
tags: [research-update, literature-review, harness, multi-agent, memory]
created: 2026-11-09
updated: 2026-11-09
---

# DAIR Paper Review — November 9, 2026

The user-supplied [DAIR paper catalog](https://academy.dair.ai/papers) surfaced seven papers missing from the initial [[reports/Research Update - 2026-11-09|November update]]. Three delegated investigations and a separate routing review checked their primary texts. The additions sharpen three questions: what persists, what admits a change, and what the reported cost includes.

Discovery covered the displayed weekly issue, the [harness-engineering collection](https://academy.dair.ai/papers/collections/harness-engineering), the [self-improving-agents reading list](https://academy.dair.ai/papers/collections/self-improving-agents), and selected entries in its [latest-paper view](https://academy.dair.ai/papers/collections/self-improving-agents?view=latest). This is a targeted review, not an exhaustive archive survey. Each source card preserves its discovery URL and reviewed version; claims below come from primary papers. Experiments were not reproduced.

## Seven Reviewed Additions

| Paper and primary text | What it adds | Reading caution |
|---|---|---|
| [HarnessMM](../sources/HarnessMM.md) · [v2](https://arxiv.org/html/2610.32813v2) | Reusable harness settings plus runtime decision reuse. | Integrated savings do not isolate the recursive optimizer. |
| [Prime Agent](../sources/Prime%20Agent.md) · [v1](https://arxiv.org/html/2608.23552v1) | Recursive execution and persistent refinement. | Public-game results and external baselines need protocol-level comparison. |
| [EMMA](../sources/EMMA.md) · [v1](https://arxiv.org/html/2610.35966v1) | Workflow configuration serves as retained experience. | An admissible edit can persist after a failed rerun. |
| [Continual AutoResearch](../sources/Continual%20AutoResearch.md) · [v1](https://arxiv.org/html/2611.05108v1) | Tests persistence across research tasks. | Earlier useful candidates need not improve final outcomes. |
| [Verification placement](../sources/Rethinking%20Verification%20in%20Agent%20Harnesses.md) · [v1](https://arxiv.org/html/2610.34577v1) | Compares verification placement and independent critics. | Completion self-check prompts are distinct from executable CI gates. |
| [Exo](../sources/Exo.md) · [v1 PDF](https://arxiv.org/pdf/2611.00463v1) | Separates mutable execution policy from state and activation mechanisms. | Default admission checks build success; protection depends on configuration. |
| [AgentBaton](../sources/AgentBaton.md) · [v1](https://arxiv.org/html/2610.35959v1) | Learns when to hand a task to a cheaper model. | API savings exclude local inference cost. |

Prime Agent is an August omission, not a November release. HarnessMM's November revision has a different technical-report title from the catalog entry; its source card records both. Exo's incomplete HTML required the PDF for the full evaluation and implementation limits.

## How This Changes the Project

These are synthesis recommendations from the reviewed designs:

1. **Describe admission precisely.** Structural validity, successful execution, benchmark improvement, and preservation of previous capabilities are different tests. Record which ones a system actually performs.
2. **Treat persistence as an experimental variable.** Separate retained sessions, workspace artifacts, insight notes, workflow configuration, and rewritten runtime code. Test irrelevant or stale state alongside useful state.
3. **Measure the outcome at the intended horizon.** Early progress, final selection, recurring-task efficiency, and generalization answer different questions. A useful optimization on repeated tasks may not pay on novel work.
4. **Complete the cost boundary.** Include optimization, failed candidates, critics, detector serving, local inference, and downstream repair when relevant. Keep token counts, API charges, latency, and total compute distinct.

The detailed additions are integrated into [[reports/Harness Self-Improvement Update - 2026-11-09]], [[reports/Code Factories Update - 2026-11-09]], [[reports/Multi-Agent Research Update - 2026-11-09]], and [[reports/Memory and Dreaming Update - 2026-11-09]].

## Next Papers: Abstracts Checked, Full Review Pending

These are discovery leads, not incorporated effectiveness findings. Dates are first arXiv submission dates.

| Lead | Date | Question for the next review |
|---|---|---|
| [AutoRefine](https://arxiv.org/abs/2611.09291) | Nov 6 | How much can noisy merge/abandon outcomes teach a code judge, and how well does calibration transfer? |
| [Masked Erosion](https://arxiv.org/abs/2610.38392) | Oct 28 | Can a gate preserve redundant safeguards when measured task success rewards their removal? |
| [When the Critic Falls Behind / RuHarness](https://arxiv.org/abs/2610.36826) | Oct 27 | How are evolving rubrics evaluated while the underlying task objective stays fixed? |
| [OpenJarvis](https://arxiv.org/abs/2605.17172) | May 16 | What transfers from cloud-assisted specification search into entirely local execution, at what complete cost? |
| [Continual Harness](https://arxiv.org/abs/2605.09998) | May 11 | How does reset-free online adaptation differ from offline harness search and model co-learning? Already present in the older queue. |

Continue at [[maps/Frontier Reading Queue]]. Use DAIR for discovery, then inspect the primary version, evaluation split, mutable artifact, acceptance rule, cost scope, and negative results before promoting a lead to a source card.
