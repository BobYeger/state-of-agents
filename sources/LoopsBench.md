---
title: "LoopsBench: From Harness Engineering to Loop Engineering in Coding Agent Evaluation"
aliases:
  - "LoopsBench"
  - "Loop engineering benchmark"
source_type: "paper"
kind: "benchmark"
status: "verified"
year: 2026
publication_date: "2026-07-31"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: "2026-08-10"
source_updated_date_basis: "arxiv_v2_submission_date"
arxiv_id: "2608.00267"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Han Li"
  - "Zhemin Fang"
  - "Rili Feng"
  - "Yingqi Zhao"
  - "Jiaheng Liu"
  - "Pengfei Gao"
  - "He Ye"
  - "Dayi Lin"
  - "Qingwei Lin"
  - "Saravan Rajmohan"
  - "Dongmei Zhang"
venue: "arXiv"
url: "https://arxiv.org/abs/2608.00267"
pdf_url: "https://arxiv.org/pdf/2608.00267"
created: 2026-08-11
updated: 2026-08-11
---

# LoopsBench

## Summary

- LoopsBench evaluates a model–loop configuration over sustained coding work rather than grading only a final patch. Each task is a dependency DAG whose nodes are separately testable development units and whose edges encode source-evidenced prerequisites.
- The released benchmark contains 112 tasks, more than 5,300 units, eight languages, and nine domains. It draws from 29 pull-request sequences, 57 course labs, and 26 research evolutions with auditable public development evidence.
- Unit manifests, declared parents, attached tests, project-native tests, and the writable repository are visible from the start. The evaluator alone tracks the active ready frontier and activates test obligations for scoring as their prerequisites become satisfied. The agent may edit anywhere and is not told which unit is currently ready.
- Once a released obligation passes, its tests remain active at later checkpoints. This evaluator-side state distinguishes forward progress from regressions without pretending to constrain the agent's implementation order.
- The best reported configuration, Opus 4.7 with Claude Code and outer continuation, resolves 25.00% of tasks versus 16.96% without continuation. Under fixed GPT-5.4, resolve rates range from 18.75% for Codex and 17.86% for Claude Code to 7.14% for mini-swe-agent.
- Plans recover only part of the reference prerequisite structure. Closed-source loops report edge F1 of 0.58–0.71; evaluated open-source loops report 0.27–0.39 and tend toward near-linear plans. Reference DAGs are conservative lower bounds, not complete or uniquely correct development plans.
- Patches are longer than the gold references, agent-authored tests are sparse, and all four workflow profiles in one analysis record regressions. Low regression counts can simply reflect that a loop reached fewer obligations eligible to regress.

## Evidence Boundary

This is an author-reported arXiv preprint. Main model–loop cells use one trial; pass@3 checks support within-family model-generation ordering but do not establish the robustness of small differences in the fixed-model loop comparison.

The benchmark favors projects with auditable prerequisite evidence and containerizable tests. Mobile, frontend-heavy, hardware-adjacent, and less instrumentable development are absent. Claude Code and Opus 4.7 assist instruction recovery, environment construction, and test synthesis, creating possible wording and test bias; public source histories also leave contamination risk.

Resolve rate and regression measure the released executable obligations. They do not establish semantic equivalence, maintainability, security, deployment readiness, or general software-engineering quality. The local PDF is intentionally not linked as a redistributable artifact because arXiv lists only its non-exclusive distribution license; use the canonical paper URL.

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
- [[claims/Claim - Agent systems improve when structure matches the task]]

## Connections

- [[concepts/loop engineering]]
- [[benchmarks/long-horizon benchmarks]]
- [[operations/agent evals]]
- [[maps/Evaluation Map]]
- [[sources/On Randomness in Agentic Evals]]

## Notes

- Canonical URL: https://arxiv.org/abs/2608.00267
- First submitted July 31, 2026; current paper is arXiv v2, revised August 10, 2026.
- Project: https://loopsbench.ai/
- Code and benchmark artifacts: https://github.com/microsoft/Loopsbench
