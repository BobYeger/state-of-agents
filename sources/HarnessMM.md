---
title: "HarnessMM: Recursive Self-Improvement for Harness Token Efficiency"
aliases: ["HarnessMM", "HarnessMinusMinus"]
source_type: "paper"
kind: "harness-token-efficiency"
status: "verified"
year: 2026
publication_date: "2026-10-23"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: "2026-11-06"
source_updated_date_basis: "arxiv_v2_revision_date"
source_version: "arxiv_v2"
source_version_title: "HarnessMinusMinus: A Technical Report on Efficient Agent Harnesses Minus Overhead, Minus Cost"
arxiv_id: "2610.32813"
authors: ["Yuhua Jiang", "Chang Xu", "Feifei Gao", "Li Zhao"]
venue: "arXiv"
url: "https://arxiv.org/abs/2610.32813"
pdf_url: "https://arxiv.org/pdf/2610.32813v2"
discovery_url: "https://academy.dair.ai/papers/harnessmm-recursive-self-improvement-for-harness-token-efficiency-2610.32813"
created: 2026-11-09
updated: 2026-11-09
tags: [research, harness, self-improvement]
---

# HarnessMM

## Mechanism

RSI revises prompts/context/adapters; retained settings generate next-round feedback and freeze before testing. Actor weights stay fixed. Runtime graphs reuse resolved actions across tool receipts, bypassing model callbacks.

## Evidence and Limits

HumanEval uses a custom 33/33/98 training/validation/test partition, one attempt per task. With Qwen3.5-4B, Codex preserves 90.82% success while tokens/task fall 66.72k→47.02k (29.54%). DeepSeek Harness improves 71.43%→85.71%, with 96.28k→11.62k tokens (87.93%).

Totals include input/output, cached tokens, authorship, fallback, and failures across all test tasks; optimization costs remain separate. Token savings are not dollar or latency savings.

These integrated comparisons do not isolate RSI or callback removal. The historical textual RSI pilot accepts no edits; visual RSI curves report training progress. Certificates verify omitted calls, not semantic correctness. Codex's MBPP comparison loses success despite saving tokens. This is author-run evidence.

## Connections

- [[sources/HarnessPro]]
- [[methods/self-improving code loops]]
- [[reports/Harness Self-Improvement Update - 2026-11-09]]

## Primary Links

- [Metadata and revisions](https://arxiv.org/abs/2610.32813)
- [Full text v2, Sections 4–5 and Appendices B, F, L, V](https://arxiv.org/html/2610.32813v2)
- [Author repository](https://github.com/YuhuaJiang2002/HarnessMM)
