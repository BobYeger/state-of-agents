---
title: "PM-Bench: Evaluating Prospective Memory in LLM Agents"
aliases:
  - "PM-Bench"
  - "Prospective Memory Benchmark"
source_type: "paper"
kind: "prospective-memory-benchmark"
status: "verified"
year: 2026
publication_date: "2026-07-14"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: null
source_updated_date_basis: null
arxiv_id: "2607.12385"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Genglin Liu"
  - "Saadia Gabriel"
venue: "COLM 2026"
url: "https://arxiv.org/abs/2607.12385"
pdf_url: "https://arxiv.org/pdf/2607.12385"
license: "CC BY 4.0"
license_url: "https://creativecommons.org/licenses/by/4.0/"
created: 2026-08-16
updated: 2026-08-16
---

# PM-Bench

## Summary

- PM-Bench treats **prospective memory** as executing a deferred intention when a future time, event, or latent environment state makes it due, while continuing unrelated work. This is distinct from answering a later question about the intention.
- Its cognitive-science-inspired Virtual Week simulation spans seven days and 80 decision steps. It defines 83 intentions—57 event-based and 26 time-based—of which 81 are executable and scored, including 15 channel-triggered tasks, seven cross-day tasks, 11 cancel/override/reschedule events, 11 queryable state channels, and 74 lure actions.
- At each step the agent must choose an ongoing activity and the exact set of prospective actions currently due. It may first query hidden channels such as a clock, inbox, or status tracker. Set-F1 therefore penalizes both missed intentions and premature or spammed actions.
- The study runs eight backbones under eight configurations: an unassisted agent, a todo ledger, optional and fixed heartbeats, and a hierarchical monitoring team plus voting replays. The optional-heartbeat setup has the best macro Set-F1 across models at 65.1%; the todo ledger follows at 62.8% and has fewer false positives.
- The strongest individual model–setup cell is GPT-5.4 with optional heartbeat at 79.1% Set-F1. The abstract's 65.1% headline is the scaffold's macro score across eight models, not that individual cell.
- Monitoring more is not sufficient. The automatic 30-minute heartbeat reaches the best hidden-channel hit rate among fresh-inference configurations, 15.8%, but produces 489 false positives and only 57.8% macro Set-F1. The hierarchical setup issues 1,661 state queries yet reaches 45.2% macro Set-F1.
- No setup exceeds 50% hit rate on either cross-day or update-sensitive tasks. Different backbones prefer different scaffolds, exposing a control-policy problem rather than one universal reminder strategy.

## Report Implications

Prospective memory should be a separate memory class and evaluation axis. A useful schema needs an activation mode (`time`, `event`, or `state`), trigger predicate, status (`active`, `completed`, `canceled`, or `superseded`), monitoring policy, and the evidence that changed an intention.

Evaluation must measure activation precision as well as recall. “Always remind” can appear attentive while causing premature or duplicated actions; cancellation, rescheduling, cross-day retention, hidden-state monitoring, and stopping conditions all need explicit probes.

## Evidence Boundary

PM-Bench is a peer-reviewed COLM 2026 paper, but the released evaluation is one synthetic, author-reviewed week. Each of the 64 model–configuration cells is one run on the same scenario, so the study does not estimate scenario-sampling or ordinary run-to-run variance.

Opaque action handles and a controlled text simulation make scoring clean but do not capture real tool costs or consequences. The benchmark establishes prospective-memory failure modes and precision–recall trade-offs under its protocol; it does not show that heartbeat intervals or hierarchical monitoring will transfer unchanged to production agents.

## Claims

- [[claims/Claim - Context management is an agent architecture choice]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[operations/agent memory]]
- [[operations/agent evals]]
- [[concepts/durable dormant agents]]
- [[concepts/long-horizon agents]]
- [[maps/Context Management Map]]

## Notes

- Canonical arXiv URL: https://arxiv.org/abs/2607.12385
- Repository: https://github.com/genglinliu/PMBench
- arXiv identifies the work as a conference paper at COLM 2026.
- arXiv lists only v1 at capture time.
- The paper is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
