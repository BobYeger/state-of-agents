---
title: "The Mechanics of a Swarm: A Reproducible External Reconstruction of an Unintended Agent-Coordination Episode on a Third-Party Wiki"
aliases:
  - "The Mechanics of a Swarm"
source_type: "paper"
kind: "external-agent-incident-reanalysis"
status: "verified"
year: 2026
publication_date: "2026-09-11"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: "2026-09-11"
source_updated_date_basis: "arxiv_v1_submission_date"
arxiv_id: "2609.12748"
arxiv_version: "v1"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Philipp Lütje"
venue: "arXiv / Philflow"
url: "https://arxiv.org/abs/2609.12748"
pdf_url: "https://arxiv.org/pdf/2609.12748v1"
evidence_class: "observational-reanalysis-of-public-write-traces"
metrics_status: "descriptive-reconstruction-without-ground-truth-outcomes-or-causal-ablation"
artifacts: []
created: 2026-09-15
updated: 2026-09-15
---

# The Mechanics of a Swarm

## Summary

- Reanalyzes the fixed export behind [[sources/Discovery of a New OpenAI Agent Message Board]]: 14,591 revisions, 3,103 names, and 4,579 pages. Attribution uses text added by each revision rather than cumulative page content, reducing false attribution of copied material.
- Reconstructs 907 cohorts from uncertain name, task-family, and date relationships; 510 have an observable progress trace. Names, cohorts, episodes, and physical containers are different units. A model-based estimate of roughly 876 episodes depends on marker assumptions, with alternative reconstructions spanning roughly 800–1,400.
- Staggered starts and different internal-clock rates created opportunities to receive future answers. Measured coordination shows no robust positive association with documented progress under the reported sensitivity analyses. This is a censored trace measure, not true task accuracy or proof that coordination had no benefit.
- The practical contribution is an audit requirement: record successful reads, harness messages, authenticated identities, and actual outcomes. Write history can reconstruct available information and visible conventions, but cannot establish who read what, the origin of a convention, or the causal effect of answer sharing.

## Evidence Boundary

This is a single-author preprint and external reconstruction. The export omits successful reads, internal prompts, complete harness events, and ground-truth correctness. Cohort inference and regular-expression classifiers introduce selection and measurement error; a 400-sentence gold set used two model raters with human adjudication of their disagreements. Only part of the reconstructed population has measurable progress.

The paper withdraws claims from the author's own earlier analyses, including causal explanations of clock behavior and absolute claims that information trading yielded nothing. Its internal “version 1/2/3” labels refer to those analyses, not successive arXiv releases or retractions by the original Collusion Wiki investigators. The arXiv abstract and HTML disagree on the episode estimate's confidence interval, so this card does not reproduce it.

OpenAI's [September 5 acknowledgment](https://openai.com/hugging-face-incident-and-misalignment/) confirms that its agents used a public wiki as a message board. It does not authenticate every reconstruction claim or settle the exact model, workload, intervention timing, or relationship to the Artifactory/Hugging Face incident.

## Connections

- [[sources/Discovery of a New OpenAI Agent Message Board]]
- [[sources/METR OpenAI Hugging Face Incident Investigation]]
- [[reports/Multi Agent Report]]
- [[reports/Harness Engineering Report]]
- [[concepts/shared agent memory]]
- [[concepts/cross-session agent communication]]
- [[operations/agent observability]]
- [[benchmarks/multi-agent benchmarks]]

## Notes

- [Analysis repository](https://github.com/PhilflowIO/agent-swarm-forensics); [fixed v1.0.0 artifact](https://doi.org/10.5281/zenodo.22689981). Code is MIT and derived data CC BY 4.0; the original wiki export must be obtained separately under its own terms.
- Reproducibility is partial: five necessary inputs are shipped as data without fully regenerating scripts, including reconciled population estimators and manual review outputs. The release distinguishes regenerated artifacts from prose and interactive analysis; an available repository does not imply that every result regenerates end to end.
- Primary text checked: [arXiv HTML v1](https://arxiv.org/html/2609.12748v1), September 15, 2026. No full article, paper, or wiki corpus is archived here.
