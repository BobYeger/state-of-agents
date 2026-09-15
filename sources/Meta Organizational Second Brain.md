---
title: "An Organizational Second Brain: Building an AI That Learns From Experts"
aliases:
  - "Meta Organizational Second Brain"
source_type: "article"
kind: "organizational-knowledge-maintenance-architecture"
status: "verified"
year: 2026
publication_date: "2026-09-02"
publication_date_basis: "visible_article_date"
source_updated_date: "2026-09-02"
source_updated_date_basis: "article_publication_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Shaurya Sengar"
  - "Jason Nawrocki"
  - "Jay Shah"
  - "Prashant Kommireddi"
venue: "Engineering at Meta"
url: "https://engineering.fb.com/2026/09/02/ml-applications/organizational-second-brain-ai-learns-from-experts/"
pdf_url: ""
evidence_class: "first-party-production-architecture"
metrics_status: "vendor-reported-without-controlled-comparison"
artifacts: []
created: 2026-09-15
updated: 2026-09-15
---

# Meta Organizational Second Brain

## Summary

- Meta describes a compliance-domain agent built from curated knowledge files, composable reasoning procedures, evaluation, and an expert-feedback improvement loop. Frequently reused positions enter the wiki; occasional supporting material stays in retrieval.
- Knowledge and procedures remain separate, with explicit dependencies and staged loading. Feedback diagnosis checks whether available evidence contained the answer, distinguishing missing knowledge, faulty procedure, and unresolved expert disagreement.
- Proposed edits receive independent review, structural checks, replay of the failing case, regression evaluation, and expert approval. Accepted cases expand the test suite; model weights remain unchanged.

## Evidence Boundary

This is an internal engineering account, not an independently evaluated release. Meta reports about 80% fewer tokens per turn after restructuring and no regressions in its improvement cycles, but publishes no controlled comparison, test-set denominator, or judge-error analysis. Regression results only cover the measured cases.

## Report Implication

Knowledge maintenance needs an explicit acceptance contract: locate the failure, bound the edit, retain provenance, and test affected behavior before promotion. The design connects organizational memory to loop engineering; its reported benefits do not establish autonomous improvement without expert supervision.

## Connections

- [[concepts/organizational knowledge systems]]
- [[concepts/LLM-maintained knowledge bases]]
- [[concepts/procedural memory]]
- [[concepts/loop engineering]]
- [[reports/Agent Memory Report]]
- [[reports/Self-Improving Systems Report]]
- [[sources/Cerebras How We Built Our Knowledge Base]]
- [[sources/WikiSkill]]
