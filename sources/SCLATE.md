---
title: "SCLATE: A Substrate for Continual-Learning Agent Training and Evaluation"
aliases:
  - "SCLATE"
source_type: "paper"
kind: "agent-lifecycle-training-and-evaluation"
status: "verified"
year: 2026
publication_date: "2026-09-26"
publication_date_basis: "arxiv_v1_submission_history"
source_updated_date: "2026-09-29"
source_updated_date_basis: "arxiv_v2_submission_history"
source_version: "arXiv v2; full text inspected October 5, 2026"
document_date: "2026-10-01"
document_date_basis: "date printed on the archived v2 PDF cover"
arxiv_id: "2609.32391"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "not assessed"
authors:
  - "Youngmok Jung"
  - "Sirajul Salekin"
  - "Henry Tran"
  - "Javier Movellan"
  - "Zhao Huang"
  - "Manjot Bilkhu"
venue: "arXiv / Apple"
url: "https://arxiv.org/abs/2609.32391"
pdf_url: "https://arxiv.org/pdf/2609.32391v2"
license: "CC BY 4.0"
license_url: "https://creativecommons.org/licenses/by/4.0/"
evidence_class: "author-run-systems-and-post-training-preprint"
artifacts:
  - "raw/papers/SCLATE - A Substrate for Continual-Learning Agent Training and Evaluation.pdf"
created: 2026-10-05
updated: 2026-10-05
---

# SCLATE

## Summary

- SCLATE places benchmark events and agent events on one scheduler: tasks, session boundaries, crons, memory consolidation, and state save/restore. A hybrid clock advances with execution and skips idle intervals, allowing long scenarios to run in hours.
- Adapters preserve the existing harness and memory implementation. A proxy captures model-call tokens and log probabilities, with component attribution, so the same execution substrate supports evaluation and model post-training.
- Seven benchmark ports cover software work, assistance, and memory. The MetaClaw comparison crosses ten harness/memory configurations with ten models over 346 rounds and 30 simulated workdays.
- Memory configurations beat their harness's no-memory baseline in that comparison, but adding an external memory system underperforms native memory in 11 of 50 cells. Neither an external store nor one harness wins universally.
- Qwen3.5-4B post-training through unmodified harnesses improves held-out MetaClaw days in all six tested configurations; three gains have nominal p < 0.05, without a reported multiple-comparison correction. The separate SWE-Gym experiment reports a 16.7-point SWE-bench Verified gain and fewer file lines read.

## Architectural Contribution

Treat session boundaries and background maintenance as part of the experimental environment. A memory system that answers isolated recall questions well may behave differently when writes, consolidation, deadlines, and later actions share a timeline. Evaluate the model, harness, and memory together.

SCLATE's post-training updates model parameters. Persistent memory adaptation during a run is a separate state change; neither implies that the harness rewrites itself. [[concepts/harness-aware agent learning]] keeps these mechanisms distinct.

## Evidence Boundary

This is an author-run preprint, not independent production validation. Results depend on the tested adapters, model versions, synthetic timelines, workloads, and memory configurations. The full ten-model grid is MetaClaw-specific, not every combination on all seven benchmarks. The temporal holdout tests later days of the same benchmark; it does not establish transfer to arbitrary users or environments. Large memory gains over no memory do not imply that a separate memory product improves a capable native harness.

## Connections

- [[concepts/harness-aware agent learning]]
- [[concepts/lifelong agent learning]]
- [[concepts/dreaming and memory consolidation]]
- [[operations/agent evals]]
- [[sources/Agent Lightning v1.0]]
- [[sources/MemoryArena]]
- [[sources/MemOps]]
- [[sources/LongMemEval-V2]]
- [[sources/Agent Evaluation Reliability]]

## Source And Archive

- [Versioned full text](https://arxiv.org/html/2609.32391v2), especially sections 3, 4.2, 4.3 and appendix E.
- [Submission history](https://arxiv.org/abs/2609.32391): first submitted September 26; revised September 29, 2026.
- The v2 PDF cover prints October 1, 2026. Publication and revision fields above follow the arXiv history rather than treating that cover date as a new release.
- Unmodified PDF by the authors above, archived under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/): [[raw/papers/SCLATE - A Substrate for Continual-Learning Agent Training and Evaluation.pdf]].
