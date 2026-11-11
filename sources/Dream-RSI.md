---
title: "Dream-RSI: Recursive Self-Improvement through Evolving Worlds"
aliases: ["Dream-RSI"]
source_type: "paper"
kind: "self-improving-exploration"
status: "verified"
year: 2026
publication_date: "2026-09-14"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: "2026-10-06"
source_updated_date_basis: "arxiv_v2_revision_date"
source_version: "arxiv_v2"
arxiv_id: "2609.14858"
authors: ["Tong Zheng", "Xidong Wu", "Zheng Zhang", "Zhankui He", "Chaoyi Zhang", "Benjamin Coleman", "Ruoqiao Wei", "Di Bai", "Haolin Liu", "Rui Liu", "Xue Wang", "Yue Zhuan", "Wang-Cheng Kang", "Renkai Xiang", "Heng Huang", "Xinwu Cheng", "Yunsong Guo"]
venue: "arXiv"
url: "https://arxiv.org/abs/2609.14858"
pdf_url: "https://arxiv.org/pdf/2609.14858v2"
created: 2026-11-09
updated: 2026-11-09
tags: [research, dreaming, self-improvement]
---

# Dream-RSI

## Contribution

Replays historical discovery trees to optimize executable exploration policies: branching, parallel allocation, refinement, and stopping. The discovery agent, evaluator, and interfaces remain fixed. This meaning of dreaming is controller search over stored outcomes, distinct from memory summarization.

## Evidence and Limits

Version 2 covers nine tasks in four domains, including harness optimization. Replay produces no outcomes outside recorded trees; an improved replay score does not guarantee better online discovery. Reported discovery cost counts discovery-agent calls, not complete dollar expenditure.

The harness experiment evaluates candidates on the full 89-task Terminal-Bench 2.1 suite. Its final full-suite result is therefore not held-out transfer. It omits the fixed-policy control because authors estimate another search would exceed $100,000. Scientific-discovery comparisons provide the cleaner controlled evidence for the exploration-policy contribution.

## Connections

- [[concepts/dreaming and memory consolidation]]
- [[sources/Meta-Harness]]
- [[methods/self-improving code loops]]
- [[reports/Harness Self-Improvement Update - 2026-11-09]]

## Primary Links

- [Metadata and revisions](https://arxiv.org/abs/2609.14858)
- [Full text v2, Sections 3–4](https://arxiv.org/html/2609.14858v2)
- [Author repository](https://github.com/google-research/dream-rsi)
