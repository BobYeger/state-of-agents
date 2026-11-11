---
title: "Harness²: Recursive Agent Harnessing for an Open World"
aliases: ["Harness2", "Harness Squared"]
source_type: "paper"
kind: "self-improving-harness"
status: "verified"
year: 2026
publication_date: "2026-10-09"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: "2026-10-09"
source_version: "arxiv_v1"
arxiv_id: "2610.14224"
authors: ["Ruiyao Xu", "Yanfei Chen", "Zhongying CuiZhu", "Bhavana Dalvi Mishra", "Yifei Ming", "Han Yu", "Rujun Han", "Chen-Yu Lee", "Tomas Pfister"]
venue: "arXiv"
url: "https://arxiv.org/abs/2610.14224"
pdf_url: "https://arxiv.org/pdf/2610.14224v1"
created: 2026-11-09
updated: 2026-11-09
tags: [research, harness, self-improvement]
---

# Harness²

## Contribution

Propose–Probe–Compose compares candidate executions on the current task without ground-truth feedback. A separate improvement library retains adopted harnesses and evidence-linked experience. Each subsequent task restarts from the common base harness; useful components are selectively reused rather than automatically inherited.

## Evidence and Limits

Three professional benchmarks, four model–harness combinations, and three shuffled-order runs per main configuration. The paper reports single-step gains up to 11.5 points on WorkBuddy-Bench, 4.5 on JobBench, and 11.8 percentage points on LAB's per-criterion pass rate.

Behavioral contrasts do not certify correctness. More recursion spends additional executions; shared model biases remain. Stage instructions and decision rules stay fixed: the persistent library improves, not every part of the optimizer. Appendix F explicitly limits transfer claims.

## Connections

- [[methods/self-improving code loops]]
- [[concepts/procedural memory]]
- [[sources/Adaptive Auto-Harness]]
- [[reports/Harness Self-Improvement Update - 2026-11-09]]

## Primary Links

- [Metadata](https://arxiv.org/abs/2610.14224)
- [Full text v1](https://arxiv.org/html/2610.14224v1)
- [Author repository](https://github.com/google-research/harness2)
