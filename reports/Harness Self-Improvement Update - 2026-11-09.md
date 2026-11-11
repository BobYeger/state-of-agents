---
title: "Harness Self-Improvement Update — November 9, 2026"
date: 2026-11-09
created: 2026-11-09
updated: 2026-11-09
tags: [research, harness, self-improvement]
---

# Harness Self-Improvement Update — November 9, 2026

The new contribution since the vault's summer cluster is a more precise account of **what survives an improvement loop**: reusable mechanisms, task-specific adaptations, executable exploration policies, and the memory that guides future edits. A second change is stronger attention to cost, distribution shift, and the gap between proposing a sensible edit and demonstrating its benefit.

This is a focused September–November update checked November 9, not an exhaustive survey or independent reproduction. Source cards contain publication/version dates, checked metrics, and methodological limits. Existing foundations remain in [[reports/Self-Improving Systems Report]] and [[maps/Self-Improving Systems Map]].

## Evidence Added

| Source | Date / reviewed revision | Delta from existing coverage | Evidence class |
|---|---|---|---|
| [[sources/Dream-RSI]] | September 14 / October 6 | Historical trajectories become a replay evaluator for exploration policies | Research preprint |
| [[sources/RRSI]] | September 21 / October 4 | Acceptance and pruning explicitly address overfitting | Research preprint |
| [[sources/Harness2]] | October 9 / v1 | Current-task refinement and future improvement memory have separate lifecycles | Research preprint |
| [[sources/Harmony Harness]] | October 10 / v1 | Security/functionality objectives coexist with modular composition | Research preprint |
| [[sources/HarnessPro]] | October 19 / October 20 | Select several operating costs instead of one champion | Research preprint |
| [[sources/Retrospective Harness Adaptation Study]] | October 26 / v1 | Later-task behavioral checks challenge plausible retrospective advice | Empirical preprint |
| [[sources/Factory Droid 1.0 Frontier Harness]] | October 29 | A production operator describes its agent-assisted harness development loop | Vendor operator report |
| [[sources/Beneath the Surface Agent Evolution]] | November 5 / v1 | Gains and regressions must be tracked per task | Empirical preprint |
| [[sources/BOXBOX]] | November 6 / v1 | Executable harness changes can take effect during ongoing work | Research prototype |
| [[sources/HarnessMM]] | October 23 / November 6 | Guarded action reuse removes redundant reasoning callbacks | Research technical report |
| [[sources/Prime Agent]] | August 24 / v1; earlier omission | Persistent REPLs and recursive agents combine with versioned continual refinement | Research technical report |

### DAIR Discovery Follow-Up

[[sources/HarnessMM]] was discovered through [DAIR's paper catalog](https://academy.dair.ai/papers/harnessmm-recursive-self-improvement-for-harness-token-efficiency-2610.32813) and checked against primary v2. Its useful distinction is between optimizing reusable settings and reusing decisions during execution; the evidence card preserves separate attribution and cost scopes.

[[sources/Prime Agent]], found through [DAIR's harness collection](https://academy.dair.ai/papers/collections/harness-engineering), fills an August omission. Its integration of recursive execution and retained state merits study. The card distinguishes public-set headline scores from the companion protocol and records a case where persistent skills retain an exploit. Component contributions remain entangled.

## Implications for the Research Project

The evidence should be organized around the object that changes and the evidence used to retain it. “Self-improvement” alone is now too broad to identify an architecture. A candidate can be useful on the current task, useful across future tasks, useful only for the optimizer, or simply better at the measurement procedure.

For future comparisons, use the following research record. This is a synthesis recommendation, not a protocol validated by any single paper:

1. **Mutable state:** exact files, policy, library, or model parameters; what stays fixed.
2. **Feedback:** official tests, generated tests, replayed outcomes, model preferences, or human judgments.
3. **Admission:** how the candidate is selected; whether the old version can win; whether a separate final evaluation exists.
4. **Transfer and preservation:** same task, later tasks in the same repository, unseen benchmark, another model, or another harness; previously successful tasks lost along the way.
5. **Economics:** proposal, candidate evaluation, deployment execution, latency, and human review measured separately.
6. **Maintenance:** expiration, rejected-edit history, regression checks, and removal of once-useful components.

These axes connect the harness branch to [[concepts/dreaming and memory consolidation]], [[concepts/procedural memory]], and [[concepts/code factories]] without collapsing them into the same mechanism. The question for a factory is whether validated improvements reach subsequent work at acceptable total cost. The question for memory is whether retained experience activates in the correct situation and remains valid.

## Next Investigations, Ranked

1. **Transfer after retention.** Compare reviewed retrospective changes with an unchanged harness on later, unselected issues. Record task outcome as well as activation and behavioral change.
2. **Total cost of evolution.** Compare a static harness, task-only retries, memory reuse, and harness search under the same complete budget. Include unsuccessful candidates and review.
3. **Optimizer memory lifecycle.** Test whether rejected-change history and pruning help after the task distribution shifts; distinguish library growth from useful learning.
4. **Replay validity.** Test controller improvements on fresh online discovery runs, beyond the histories used for dreaming.
5. **Production replication.** Seek independent reproduction of operator claims and long-running evidence showing that gains survive new models and environments.

No result in this tranche establishes indefinite autonomous improvement. The strongest practical conclusion is that persistence should carry an explicit reason to retain a change and a future opportunity to remove it.

## Cyber Follow-Up

For applied cyber evidence, see [[reports/Cyber Swarms and Attacker Findings - 2026-11-09]]. Its research pipelines sharpen two requirements for harness evaluation: verify that success concerns the assigned issue, and measure what happens after a candidate repair passes its initial test.

## Abstract-Verified Follow-Up Leads

These primary metadata/abstract pages were opened, but their full texts have not been reviewed in this sweep; they are leads, not incorporated findings.

- [Meta², November 3](https://arxiv.org/abs/2611.05139): prioritize its separation of reusable evolution guidance from task-local online edits, alongside Harness² and BOXBOX.
- [Flex-RSI, November 6](https://arxiv.org/abs/2611.08946): examine the claimed paired harness-editing comparison and hidden-test protocol for vision/robotics tasks.
