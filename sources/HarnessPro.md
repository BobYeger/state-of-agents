---
title: "HarnessPro: Recursive Harness Self-Improvement with Pareto Optimization for Performance-Cost Trade-offs"
aliases: ["HarnessPro"]
source_type: "paper"
kind: "self-improving-harness"
status: "verified"
year: 2026
publication_date: "2026-10-19"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: "2026-10-20"
source_updated_date_basis: "arxiv_v2_revision_date"
source_version: "arxiv_v2"
arxiv_id: "2610.26770"
authors: ["Zhuoshi Pan", "ZhiYuan Feng", "Yukuo Cen", "Honglin Lin", "Junru Lu", "Zhongxia Chen", "Shuo Yang", "H. Vicky Zhao", "Jie Tang"]
venue: "arXiv; under review"
url: "https://arxiv.org/abs/2610.26770"
pdf_url: "https://arxiv.org/pdf/2610.26770v2"
created: 2026-11-09
updated: 2026-11-09
tags: [research, harness, self-improvement]
---

# HarnessPro

## Contribution

Analyzes trajectories, edits harnesses, and selects lite/medium/heavy operating points using performance and token cost. Generated tests guide evolution; official tests are withheld until final evaluation. Tests are generated once, limiting moving-target evaluation.

## Evidence and Limits

Terminal-Bench 2, SWE-Bench Pro, and ProgramBench use separate held-out sets of 59/100/100 tasks. Table 2's GPT-5.5/Codex heavy mode averages +2.0 percentage points and 26.1% lower per-task execution cost versus RHO.

That average combines binary task success on the first two benchmarks with mean test-case fraction on ProgramBench. Cost prices cached/input/output tokens; it is execution cost, not amortized optimization cost. Generated-test selection can still favor an imperfect proxy. Main HarnessPro results use three runs on the first two benchmarks and two on ProgramBench.

## Connections

- [[sources/Retrospective Harness Optimization]]
- [[sources/Harmony Harness]]
- [[methods/self-improving code loops]]
- [[reports/Harness Self-Improvement Update - 2026-11-09]]

## Primary Links

- [Metadata](https://arxiv.org/abs/2610.26770)
- [Full text v2, Sections 3–5](https://arxiv.org/html/2610.26770v2)
- [Author repository](https://github.com/pzs19/HarnessPro)
