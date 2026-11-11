---
title: "PHP2Shell: A tale of two PHP remote vulnerabilities"
aliases: ["Calif PHP2Shell Research"]
tags: [sources, cybersecurity, skills]
source_type: "technical-report"
status: "verified"
evidence_class: "researcher-disclosure"
publication_date: "2026-10-21"
publication_date_basis: "article_published_time_and_jsonld"
source_updated_date: "2026-10-22"
source_version: "page_retrieved_2026-11-09"
authors: ["Ryan Austin"]
venue: "Calif Research"
url: "https://calif.io/php2shell/"
created: 2026-11-09
updated: 2026-11-09
---

# Calif PHP2Shell Research

## Mechanism

A researcher familiar with historical PHP vulnerabilities directed an LLM toward neglected failure paths. After an initial finding, the researcher had the model generalize the failure pattern into a reusable `SKILL.md`; this produced another finding. The account describes iterative human direction, model source analysis, and experimental validation. Initial discovery used publicly available models without a special harness; the report does not identify a precise model/version or supply a controlled baseline.

## Evidence

Audit began July 30; initial remote-code-execution paths were found August 1. Calif reported the first issue August 11, shared its proof August 14, and records PHP confirmation August 15. The second report followed August 21; patches shipped October 21. Researchers demonstrated unauthenticated execution against multiple applications and deployment configurations.

## Boundaries

Application-independent paths and application-dependent paths differ across PHP server interfaces. This is evidence of expert-guided capability and reusable research knowledge, not autonomous discovery of every bug or demonstrated attacker deployment. Exact effort, compute cost, success denominator, and skill ablations are absent.

## Connections

- [[sources/PHP Foundation October Security Release]]
- [[sources/Wiz PHP2Shell Research]]
- [[methods/self-improving code loops]]

[Primary disclosure](https://calif.io/php2shell/).
