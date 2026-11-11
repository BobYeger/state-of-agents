---
title: "RRSI: Regularized Recursive Self-Improvement of Agent Harnesses"
aliases: ["RRSI"]
source_type: "paper"
kind: "self-improving-harness"
status: "verified"
year: 2026
publication_date: "2026-09-21"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: "2026-10-04"
source_updated_date_basis: "arxiv_v3_revision_date"
source_version: "arxiv_v3"
arxiv_id: "2609.24972"
authors: ["Peng Xia", "Rujun Han", "Zifeng Wang", "Yanfei Chen", "Yufan Zhuang", "Yoonho Lee", "Chengsong Huang", "Han Yu", "Zhongying CuiZhu", "Yifei Ming", "Huaxiu Yao", "Burak Gokturk", "Tomas Pfister", "Chen-Yu Lee"]
venue: "arXiv"
url: "https://arxiv.org/abs/2609.24972"
pdf_url: "https://arxiv.org/pdf/2609.24972v3"
created: 2026-11-09
updated: 2026-11-09
tags: [research, harness, self-improvement]
---

# RRSI

## Contribution

Regularizes frozen-model harness search through shrinking edit budgets, rejected-hypothesis history, leakage screening, cost-aware acceptance, and removal of unproductive components. The editable harness remains broad; the constraints govern proposal and selection.

## Evidence and Limits

Eight benchmarks span coding, professional work, and engineering. Appendix E reports paired task-level bootstrap intervals and a second independent search; these are author-run experiments, not external replication. Table 6 reports SWE-bench Verified transfer of +1.8 points versus the unevolved harness, with a 95% interval of [+1.1, +4.0].

The abstract's “up to 4.3” out-of-distribution summary conflicts with Table 6's +4.7 JobBench result; use benchmark-specific tables. Finite evolution data and tuned design choices still limit generalization. Regularization terminology is an analogy to discrete search, not numerical weight penalties.

## Connections

- [[methods/self-improving code loops]]
- [[concepts/evaluator reliability]]
- [[sources/SkillAdam]]
- [[reports/Harness Self-Improvement Update - 2026-11-09]]

## Primary Links

- [Metadata and version history](https://arxiv.org/abs/2609.24972)
- [Full text v3, especially Sections 3–4 and Appendix E](https://arxiv.org/html/2609.24972v3)
