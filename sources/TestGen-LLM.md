---
title: "Automated Unit Test Improvement using Large Language Models at Meta"
aliases:
  - "TestGen-LLM"
  - "Assured LLMSE"
source_type: "paper"
kind: "test-generation"
status: "verified"
year: 2024
publication_date: "2024-02-14"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2402.09171"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Nadia Alshahwan"
  - "Jubin Chheda"
  - "Anastasia Finegenova"
  - "Beliz Gokkaya"
  - "Mark Harman"
  - "Inna Harper"
  - "Alexandru Marginean"
  - "Shubho Sengupta"
  - "Eddy Wang"
venue: "arXiv / FSE 2024 industry track (Meta)"
url: "https://arxiv.org/abs/2402.09171"
pdf_url: "https://arxiv.org/pdf/2402.09171"
artifacts:
  - "raw/papers/Automated Unit Test Improvement using Large Language Models at Meta.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# TestGen-LLM

## Summary

- Filter-cascade acceptance gate ("Assured LLMSE"): a generated test is only surfaced to humans if it builds, passes reliably, and measurably increases coverage over the existing suite — 75% of generated tests built, 57% passed reliably, 25% increased coverage.
- 73% of TestGen-LLM recommendations were accepted for deployment by Meta engineers during Instagram/Facebook test-a-thons.
- Improved 11.5% of all classes it was applied to, evaluated on Reels and Stories.
- The design explicitly counters hallucination by requiring empirical validation instead of trusting LLM output — the canonical "tests must clear filters before humans see them" pattern.

## Claims

- [[claims/Claim - Runtime control and verification improve agent reliability]] — the filter cascade ensures only empirically validated tests reach human review, which is what made the 73% acceptance rate possible.

## Connections

- [[concepts/code factories]]
- [[sources/ACH Mutation-Guided Test Generation]]
- [[sources/Meta Agentic Program Repair]]

## Artifacts

- [[raw/papers/Automated Unit Test Improvement using Large Language Models at Meta.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2402.09171
- First at-scale industrial deployment of LLM test improvement; adequacy criterion is coverage increase, which the follow-up ACH work replaces with mutant-killing.
- Acceptance numbers come from test-a-thon settings, not steady-state usage.
