---
title: "Recursive self-improvement of AI research agents"
aliases:
  - "AIDE2"
  - "AIDE²"
  - "Recursive Self-Improvement of AI Research Agents"
source_type: "paper"
kind: "research-agent-harness-self-improvement"
status: "verified"
year: 2026
publication_date: "2026-09-22"
publication_date_basis: "arxiv_v1_submission_history"
source_updated_date: null
source_updated_date_basis: null
source_version: "arXiv v1; full text inspected October 5, 2026"
arxiv_id: "2609.26457"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "not assessed"
authors:
  - "Dhruv Srikanth"
  - "Bingchen Zhao"
  - "Dixing Xu"
  - "Yuxiang Wu"
  - "Zhengyao Jiang"
venue: "arXiv / Weco AI"
url: "https://arxiv.org/abs/2609.26457"
pdf_url: "https://arxiv.org/pdf/2609.26457v1"
license: "arXiv non-exclusive distribution"
license_url: "https://arxiv.org/licenses/nonexclusive-distrib/1.0/"
evidence_class: "author-run-recursive-harness-optimization-preprint"
artifacts: []
created: 2026-10-05
updated: 2026-10-05
---

# AIDE² Recursive Self-Improvement

## Summary

- An outer research agent rewrites an inner research agent's harness, selecting candidates using private evaluations under fixed budgets. Model weights remain fixed within each loop.
- The eight-day main run accepts seven rewrites; changes include search diversification, bounded history, and robustness checks. Gains transfer to four external benchmarks; two additional optimization runs also find improvements.
- This extends research on executable self-modification toward research efficiency itself. Related antecedents include [[sources/Darwin Godel Machine]], [[sources/SICA Self-Improving Coding Agent]], and [[sources/Meta-Harness]].

## Evidence Boundary

Author-run preprint. Hidden selection scores do not establish external generalization; separate held-out tasks supply that evidence. The weather result uses one task with three seeds.

The **ignition test is inconclusive**: with three seeds per arm, the discovered agent is not established as a better or more sample-efficient self-improver than its human-engineered comparator. Evaluation noise, compute cost, and difficult-to-interpret evolved code limit the conclusion. This supports measured harness improvement, not demonstrated accelerating recursive improvement.

## Connections

- [[concepts/harness-aware agent learning]]
- [[concepts/lifelong agent learning]]
- [[methods/self-improving code loops]]
- [[sources/Adaptive Auto-Harness]]
- [[sources/Red Queen Godel Machine]]
- [[safety/reward hacking]]

## Sources

- [Versioned full text](https://arxiv.org/html/2609.26457v1), sections 2, 3.3, 3.5, 3.6 and 5.
- [Submission history](https://arxiv.org/abs/2609.26457).
- No public PDF copy: arXiv's distribution license does not grant general redistribution rights.
