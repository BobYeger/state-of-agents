---
title: "BOXBOX: Recursive Harness Self-Improvement for Long-Running Performance Optimization"
aliases: ["BOXBOX", "PerfRace"]
source_type: "paper"
kind: "online-harness-optimization"
status: "verified"
year: 2026
publication_date: "2026-11-06"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: "2026-11-06"
source_version: "arxiv_v1"
arxiv_id: "2611.09218"
authors: ["Yuhao Tan", "Hanyun Jiang", "Fangkai Yang", "Yuan Yao", "Taolue Chen", "Bo Qiao", "Yu Kang", "Lu Wang", "Pu Zhao", "Xiaoxing Ma", "Qingwei Lin"]
venue: "arXiv"
url: "https://arxiv.org/abs/2611.09218"
pdf_url: "https://arxiv.org/pdf/2611.09218v1"
created: 2026-11-09
updated: 2026-11-09
tags: [research, harness, self-improvement]
---

# BOXBOX

## Contribution

The agent requests executable harness revisions during an ongoing task. Kernel-managed hot reload preserves execution context, with validation and recovery. PerfRace supplies performance-optimization workloads with shadow verification outside the writable workspace.

## Evidence and Limits

Fifty held-out tasks, three four-hour runs each, GPT-5.6 Luna, and a common Terminus-KIRA seed. The budget includes execution, online harness optimization, and evaluation. Harmonic-mean correct speedup is 1.702× versus 1.539× for Harness Scaling; mean model cost is $16.43 versus $12.98. BOXBOX's higher speedup therefore does not mean lower absolute cost than that baseline.

This measures task-local adaptation, not cross-task accumulation. The authors explicitly classify it as a research prototype: validation/rollback do not constitute a complete security boundary. Benchmark curation and frozen correctness/performance checks remain central to interpreting the gains.

## Connections

- [[methods/self-improving code loops]]
- [[concepts/long-horizon agents]]
- [[sources/Harness2]]
- [[reports/Harness Self-Improvement Update - 2026-11-09]]

## Primary Links

- [Metadata](https://arxiv.org/abs/2611.09218)
- [Full text v1, Sections 3–5 and security limitations](https://arxiv.org/html/2611.09218v1)
