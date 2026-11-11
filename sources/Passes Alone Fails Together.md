---
title: "Passes Alone, Fails Together: Benchmarking Semantic Coordination in Parallel LLM-Agent Development"
aliases: ["stale semantic coordination benchmark", "Passes Alone, Fails Together"]
tags: [sources, multi-agent, code-factories]
source_type: "paper"
status: "verified"
evidence_class: "research-benchmark"
publication_date: "2026-09-21"
publication_date_basis: "arxiv_v1_submission_date"
source_version: "arxiv_v1"
arxiv_id: "2609.25396"
authors: ["Haocheng Xia", "Eugene Wu", "Yongjoo Park"]
venue: "EXPRESS 2026"
url: "https://arxiv.org/abs/2609.25396"
doi: "10.1145/3842650.3843171"
created: 2026-11-09
updated: 2026-11-09
---

# Passes Alone, Fails Together

## Contribution

The `stale` benchmark tests identical suites against each patch separately and their combination, attributing interference only to newly failing combined behavior. Removing agent test edits and correcting unequal grading reduced observed interference to one of 834 runs on 417 mined Django PR pairs.

## Evidence and Boundaries

On deliberately constructed tasks using 12 Django helpers, GPT-5.5 caused interference in 105/108 blind runs. An oracle message describing a finalized concurrent change recovered 89/108 runs. One patch is scripted; the agent must use selected helpers.

These results establish a failure mechanism, not its real-world prevalence. Reviewed repository history and constructed breaking changes sample different conditions. Complete oracle messages do not demonstrate a working online communication protocol.

## Connections

- [[operations/worktree isolation]]
- [[operations/release engineering]]
- [[concepts/evaluator reliability]]
- [[sources/ParallACT]]

## Primary Link

[Full text v1, Sections 2–5](https://arxiv.org/html/2609.25396v1).
