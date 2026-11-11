---
title: "Prime Agent: A Self-Improving RLM Harness"
aliases: ["Prime Agent"]
source_type: "paper"
kind: "persistent-recursive-harness"
status: "verified"
year: 2026
publication_date: "2026-08-24"
publication_date_basis: "arxiv_v1_submission_date"
first_publication_date: "2026-08-05"
first_publication_date_basis: "manuscript_statement"
source_version: "arxiv_v1"
companion_artifact_version: "prime-agent_v0.3.3"
arxiv_id: "2608.23552"
authors: ["Seth Karten", "Alex L. Zhang", "Kevin Thomas", "Sebastian Müller", "Elie Bakouch", "Daniel Auras", "Mika Senghaas", "Fares Obeid", "Konstantin Dunas", "Johannes Hagemann", "Sami Jaghouar"]
venue: "arXiv"
url: "https://arxiv.org/abs/2608.23552"
pdf_url: "https://arxiv.org/pdf/2608.23552v1"
discovery_url: "https://academy.dair.ai/papers/collections/harness-engineering"
created: 2026-11-09
updated: 2026-11-09
tags: [research, harness, self-improvement, multi-agent, memory]
---

# Prime Agent

## Mechanism

Persistent IPython kernels hold intermediate data outside active context. Asynchronous recursive subagents retain separate contexts and kernels, communicating through daemon queues. Continual Harness versions prompt notes, factual memories, executable skills, and subagent specifications. Direct edits or `/refine` update supplemental state at turn boundaries; explicit global entries survive across sessions. Model weights and the base prompt stay fixed. See [Sections 2.2–2.5](https://arxiv.org/html/2608.23552v1).

## Evidence and Limits

The [companion results](https://github.com/PrimeIntellect-ai/arc-agi-3-prime-agent/blob/main/README.md), checked November 9, specify v0.3.3, Opus 5 `xhigh`, 25 public ARC-AGI-3 games/183 levels, fresh sessions, 500 actions/game, and at most 20 actions/call. Three runs score 94.99%, 95.24%, and 95.5% RHAE; the median completes 178/183 levels and 24/25 games, costing an estimated $1,059. [RHAE](https://docs.arcprize.org/methodology) combines completion and human-relative action efficiency; it is not a solve percentage.

The paper's 95.5% Best@1 headline matches the highest companion run, not its median. Its roughly 30% baseline uses external official results; Section 3.1 explicitly disclaims causal isolation. These are historical public-set results, not a current private leaderboard claim. Component gains remain entangled; nanoGPT final records show little harness effect relative to noise. A Factorio trace retains an exploit as a skill, illustrating that persistence can preserve bad behavior. See [Sections 3.1–3.5](https://arxiv.org/html/2608.23552v1).

## Connections

- [[sources/Harness2]]
- [[concepts/procedural memory]]
- [[methods/multi-agent orchestration]]
- [[reports/Harness Self-Improvement Update - 2026-11-09]]

## Primary Links

- [Metadata and version](https://arxiv.org/abs/2608.23552)
- [Author implementation](https://github.com/PrimeIntellect-ai/prime-agent)
