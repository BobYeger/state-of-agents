---
title: "Language Models Need Sleep: Learning to Self-Modify and Consolidate Memories"
aliases:
  - "Language Models Need Sleep"
  - "Google Sleep Framework"
source_type: "paper"
kind: "parametric-continual-learning"
status: "verified"
year: 2026
publication_date: "2026-06-02"
publication_date_basis: "arxiv_v1_submission_date; paper_reports_earlier_openreview_version"
source_updated_date: "2026-07-10"
source_updated_date_basis: "arxiv_v2_revision_date"
source_version: "arxiv_v2"
arxiv_id: "2606.03979"
authors:
  - "Ali Behrouz"
  - "Farnoosh Hashemi"
  - "Adel Javanmard"
  - "Vahab Mirrokni"
venue: "arXiv / Google Research"
url: "https://arxiv.org/abs/2606.03979"
pdf_url: "https://arxiv.org/pdf/2606.03979v2"
evidence_class: "author-run-research-experiments"
metrics_status: "author-reported"
created: 2026-11-09
updated: 2026-11-09
---

# Language Models Need Sleep

## Mechanism and Boundary

Consolidation distills short-term knowledge into expanded parametric capacity; dreaming generates and selects synthetic rehearsal data for numerical weight updates. This requires training infrastructure and differs from rewriting external memory for a frozen task agent.

The paper evaluates knowledge incorporation, reasoning, and long-context retention. Its 10M-token BABILong result uses benchmark-fine-tuned small models; Appendix B.2 reports substantial degradation without fine-tuning. It does not establish a general 10M-token agent memory capability.

The October 27 Google Research article is renewed explanation of earlier work. ArXiv v1 is June 2 and v2 July 10; the paper additionally reports an OpenReview version from September 2025. Do not date the research novelty to the blog.

## Reading

[Full paper, v2](https://arxiv.org/html/2606.03979v2); [submission history](https://arxiv.org/abs/2606.03979); [October research article](https://research.google/blog/the-sleep-framework-a-new-way-for-llms-to-retain-knowledge-in-continual-learning/).

## Connections

- [[concepts/dreaming and memory consolidation]]
- [[concepts/lifelong agent learning]]
- [[sources/Sleep-time Compute]]
- [[sources/Auto-Dreamer]]
- [[reports/Memory and Dreaming Update - 2026-11-09]]
