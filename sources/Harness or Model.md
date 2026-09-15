---
title: "Harness or Model? Isolating the Harness Effect in Agentic Coding with a Contamination-Controlled Private Suite"
aliases:
  - "Harness or Model"
source_type: "paper"
kind: "paired-coding-harness-evaluation"
status: "verified"
year: 2026
publication_date: "2026-09-08"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: "2026-09-08"
source_updated_date_basis: "revised_manuscript_and_arxiv_v1_date"
arxiv_id: "2609.11987"
arxiv_version: "v1"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Mohsen Arjmandi"
venue: "arXiv / evolutionID GmbH"
url: "https://arxiv.org/abs/2609.11987"
pdf_url: "https://arxiv.org/pdf/2609.11987v1"
evidence_class: "single-author-private-suite-paired-empirical-study"
metrics_status: "task-bootstrap-estimates-with-selection-and-cost-telemetry-limitations"
artifacts: []
created: 2026-09-15
updated: 2026-09-15
---

# Harness or Model?

## Summary

- Holds the model fixed while comparing vendor-native harnesses against DeepAgents: Claude Agent SDK versus DeepAgents on Opus 4.8, and Codex SDK versus DeepAgents on GPT-5.5. The study builds a private 256-task suite, then runs paired comparisons on 80 selected tasks; 792 of 800 planned runs across the study were graded.
- Neither average comparison resolves a solve-rate advantage: native minus neutral is −1.25 percentage points for Opus, with task-bootstrap 95% interval [−10.0, +7.5], and +1.25 for GPT-5.5, [−4.4, +6.9]. This is uncertainty about these comparisons, not equivalence or evidence that harness design never matters.
- The Opus average combines opposite repository and contest patterns, discovered after inspecting the data. Completion also differs from correctness: 22 of 81 runs cancelled at the wall-clock limit already contained passing patches. Record both validated artifact quality and whether the agent autonomously finishes.
- The September revision corrects an August manuscript's cache-token accounting error. Repricing observed usage suggests higher neutral-harness cost per solution, but 58 Anthropic runs lack usage records and plausible allocation of that spend can reverse the billed ordering. The durable lesson is to reconcile each SDK's token semantics, raw events, aggregate ledger, and invoice before comparing agent economics.

## Evidence Boundary

The 80-task pool partly selects for harness disagreement: 24 discordant tasks plus two groups of 28 selected by hash. It is not an unselected representative sample of software work. Repository tasks come from four proprietary codebases, the workload interaction is post hoc, repeats are limited, and configuration differences remain, including VM memory. Conclusions are conditional on these models, snapshots, tasks, and budgets.

Contamination controls use private provenance and documented cutoffs, but the canary emission probe was not run. The revised paper corrects its earlier preregistration claim: plans were committed before execution and documents deposited in a private OSF project, but no formal OSF registration was created.

Tasks, gold patches, and hidden tests remain private. Although the abstract says code and aggregates are released, the availability section describes a replication package obtainable from the corresponding author, with a persistent archival deposit deferred. Public end-to-end replication has not been established. This is a useful new preprint and measurement case, not a settled comparison of native and neutral harnesses.

## Connections

- [[reports/Harness Engineering Report]]
- [[maps/Harness Design Playbook]]
- [[benchmarks/agent evaluation]]
- [[operations/agent evals]]
- [[operations/cost control]]
- [[concepts/cache-aware harness design]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Notes

- [arXiv abstract and submission record](https://arxiv.org/abs/2609.11987); [full text v1](https://arxiv.org/html/2609.11987v1), especially study design, telemetry correction, limitations, and data availability. Checked September 15, 2026.
- The September 8 telemetry correction is already included in arXiv v1; it is not an arXiv v2 release. No paper or private dataset is archived here.
