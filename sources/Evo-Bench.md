---
title: "Evo-Bench: Can Language Models Improve Agent Harness?"
aliases:
  - "Evo-Bench"
  - "Evo-Bench Harness Evolution Benchmark"
source_type: "paper"
kind: "harness-evolution-benchmark"
status: "verified"
year: 2026
publication_date: "2026-08-10"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: null
source_updated_date_basis: null
arxiv_id: "2608.09096"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Lisheng Huang"
  - "Chen Yang"
  - "Hao Zhou"
  - "Huatong Song"
  - "Zongchao Chen"
  - "Ran Le"
  - "Yang Song"
  - "Wayne Xin Zhao"
  - "Tao Zhang"
venue: "arXiv"
url: "https://arxiv.org/abs/2608.09096"
pdf_url: "https://arxiv.org/pdf/2608.09096"
license: "CC BY 4.0"
license_url: "https://creativecommons.org/licenses/by/4.0/"
artifacts:
  - "raw/papers/Evo-Bench - Can Language Models Improve Agent Harness.pdf"
created: 2026-08-11
updated: 2026-08-11
---

# Evo-Bench: Can Language Models Improve Agent Harness?

## Summary

- Evo-Bench evaluates whether an evolver model can improve executable policy-harness code around a fixed task model. Editable surfaces include prompts, tools, control flow, context, memory, verification, recovery, routing, and multi-agent behavior.
- The main protocol starts from a minimal CodeAct seed with DeepSeek-V4-Flash fixed as the policy model. An evolver receives 160 visible validation tasks and up to 20 formal evaluations, 1,000 agent steps, and 48 hours before one revision is frozen for 448 disjoint held-out tasks across Search, Office, and General domains.
- All nine evolvers beat the 29.7-point seed on held-out evaluation. GPT-5.6 Sol leads at 46.3 (+16.6), Claude Opus 4.8 reaches 45.8 (+16.1), and a composite of three domain-specific human systems scores 47.5.
- Gains are domain-dependent: Search improves by as much as 34.8 points as evolvers add missing retrieval and web-processing tools, while Office changes are small or negative because its workflows require specialized document and data operations.
- Later changes can erase earlier gains. Several runs saturate early, bundle edits without isolating causes, omit smoke tests, or fail to restore their best snapshot. Main configurations run once, so the paper does not estimate how reliably an evolver finds and retains a strong harness.
- The policy-model ablation reruns evolution separately for Qwen3.6-35B-A3B, DeepSeek-V4-Flash, and GLM-5.2 policies using Qwen3.7-Max and GLM-5.2 as evolvers. Every rerun improves its own CodeAct baseline, showing that the evolution protocol is not tied to one policy model. It does **not** test whether one frozen evolved harness transfers unchanged across policy models.

## Evaluation Design

| Component | Design |
|---|---|
| Validation / held out | 160 visible tasks / 448 disjoint tasks |
| Domains | 320 Search, 192 Office, 96 General tasks |
| Main policy | Fixed DeepSeek-V4-Flash |
| Evolution cap | 20 formal evaluations, 1,000 steps, 48 hours |
| Rollout cap | 300 steps and one hour |
| Selection | One frozen revision receives held-out evaluation |

Policy rollouts use immutable harness snapshots in fresh workspaces and cannot access answers, scorers, evolver notes, sibling workspaces, or held-out data. Because evolvers can inspect validation answers and trajectories, the benchmark also scans code and trajectories for leakage and zeroes confirmed violations.

## Evidence Boundary

This is an author-run arXiv v1 benchmark, not an independent replication. Tasks are deliberately selected for sensitivity to a set of auxiliary harnesses, so the sample is useful for discriminating harness quality but is not an unbiased estimate of benefit on arbitrary workloads. Some auxiliary Office data comes from anonymized enterprise workflows or internal corpora.

The human comparator is a composite of MiroFlow, Stirrup, and the Claw-Eval harness rather than one general-purpose system built under the evolvers' budget. Scoring mixes source-native metrics with Qwen3.7-Plus judging, and General tasks receive three trials while Search and Office receive one. Reported evolver costs exclude policy and judge calls. The results support held-out evaluation of executable harness search under this protocol, not recursive self-improvement or a claim that more budget always helps.

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
- [[claims/Claim - Agent systems improve when structure matches the task]]

## Connections

- [[maps/Self-Improving Systems Map]]
- [[methods/self-improving code loops]]
- [[concepts/loop engineering]]
- [[operations/agent evals]]
- [[sources/Meta-Harness]]
- [[sources/Self-Harness]]

## Artifacts

- [[raw/papers/Evo-Bench - Can Language Models Improve Agent Harness.pdf]]

## Notes

- Canonical arXiv URL: https://arxiv.org/abs/2608.09096
- Project and leaderboard: https://evobench.org/
- Repository: https://github.com/RUCAIBox/Evo-Bench
- arXiv lists only v1 at capture time.
- The paper and preserved PDF are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
