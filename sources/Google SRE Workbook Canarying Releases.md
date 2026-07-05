---
title: "The Site Reliability Workbook, Ch. 16: Canarying Releases"
aliases:
  - "Canarying Releases"
  - "SRE Workbook Ch. 16"
source_type: "docs"
kind: "release-engineering"
status: "verified"
year: 2018
publication_date: "2018-07"
publication_date_basis: "oreilly_book_publication"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Alec Warner"
  - "Štěpán Davidovič"
venue: "Google SRE Workbook (O'Reilly, free online)"
url: "https://sre.google/workbook/canarying-releases/"
pdf_url: ""
artifacts:
  - "raw/docs/google-sre-workbook-canarying-releases.md"
created: 2026-07-03
updated: 2026-07-05
---

# Google SRE Workbook Canarying Releases

## Summary

- Defines canarying as "a partial and time-limited deployment of a change in a service and its evaluation": a canary population receives the change while a control population runs the old version.
- Error-budget math for canary sizing: a change with a 20% error rate deployed to 100% of traffic burns the budget immediately, while the same change on a 5% canary produces only a 1% overall error rate.
- Canary metric selection discipline: metrics must indicate real problems (tied to SLIs), be attributable to the change, and number roughly a dozen at most — monitoring everything erodes trust and creates maintenance burden.
- Rejects before/after comparison (time-based noise); instead isolates metrics by population (canary versus control) in the monitoring system.
- Multi-stage gradual rollouts: strict metrics (crashes, request failures) gate small early stages, looser metrics gate later larger stages; only one canary should run at a time to avoid signal contamination.
- Recommends feature flags to decouple feature launches from binary releases; for data pipelines, canary duration must span complete work-unit processing.

## Claims

- [[claims/Claim - Runtime control and verification improve agent reliability]] — canarying is the release-layer instance of verification gating change exposure.

## Connections

- [[concepts/code factories]]
- [[concepts/loop engineering]]
- [[operations/agent observability]]

## Artifacts

- [[raw/docs/google-sre-workbook-canarying-releases.md]]

## Notes

- Canonical URL: https://sre.google/workbook/canarying-releases/
- Pre-LLM (2018) and agent-agnostic; included as the canonical methodology for evaluating any change on partial traffic — the evaluation loop a code factory must automate when agent-produced changes ship at volume.
