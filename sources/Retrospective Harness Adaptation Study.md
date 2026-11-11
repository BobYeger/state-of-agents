---
title: "How Do Coding-Agent Harnesses Self-Evolve? An Empirical Study of Retrospective Adaptation"
aliases: ["Retrospective Harness Adaptation Study"]
source_type: "paper"
kind: "self-improving-harness-analysis"
status: "verified"
year: 2026
publication_date: "2026-10-26"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: "2026-10-26"
source_version: "arxiv_v1"
arxiv_id: "2610.34938"
authors: ["Christoph Treude", "Sebastian Baltes"]
venue: "arXiv"
url: "https://arxiv.org/abs/2610.34938"
pdf_url: "https://arxiv.org/pdf/2610.34938v1"
created: 2026-11-09
updated: 2026-11-09
tags: [research, harness, self-improvement]
---

# Retrospective Harness Adaptation Study

## Contribution

Tests whether individual retrospective changes affect later issues in the same repository. Thirty Claude Code sessions yield 125 proposals; 24 are implemented, and 12 adaptations undergo transfer evaluation. Selection and labeling involve humans: this is not an autonomous improvement experiment.

## Evidence and Limits

Of seven informative transfer events, two eliminate the targeted action, one reduces it, and four show no reduction. No consistent task-success benefit appears. Avoiding a failed command can coexist with longer sessions when bundled instructions add checks.

Five sessions per harness and targeted issue selection limit generalization. “Repeated work” is a behavioral measure; preventing a baseline comparison does not inherently improve verification. Two model coders plus author resolution are not human inter-rater reliability. The key diagnostic is whether the later problem occurs, the adaptation covers it, and the agent acts differently.

## Connections

- [[sources/Harness Updating Is Not Harness Benefit]]
- [[concepts/procedural memory]]
- [[methods/self-improving code loops]]
- [[reports/Harness Self-Improvement Update - 2026-11-09]]

## Primary Links

- [Metadata](https://arxiv.org/abs/2610.34938)
- [Full text v1](https://arxiv.org/html/2610.34938v1)
- [Research artifact](https://doi.org/10.5281/zenodo.23653700)
