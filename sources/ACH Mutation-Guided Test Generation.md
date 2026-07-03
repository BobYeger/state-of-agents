---
title: "Mutation-Guided LLM-based Test Generation at Meta"
aliases:
  - "ACH"
source_type: "paper"
kind: "test-generation"
status: "verified"
year: 2025
publication_date: "2025-01-22"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2501.12862"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Christopher Foster"
  - "Abhishek Gulati"
  - "Mark Harman"
  - "Inna Harper"
  - "Ke Mao"
  - "Jillian Ritchey"
  - "Hervé Robert"
  - "Shubho Sengupta"
venue: "arXiv / FSE 2025 industry track (Meta)"
url: "https://arxiv.org/abs/2501.12862"
pdf_url: "https://arxiv.org/pdf/2501.12862"
created: 2026-07-03
updated: 2026-07-03
---

# ACH Mutation-Guided Test Generation

## Summary

- Inverts test generation: the LLM first generates faults (mutants) simulating a stated concern (e.g., a privacy fault such as messages shared to the wrong audience), then generates tests proven to kill those mutants — adequacy is defined by fault detection, not coverage.
- Applied to 10,795 Android Kotlin classes across 7 Meta platforms: 9,095 mutants generated, 571 privacy-hardening tests produced.
- Messenger/WhatsApp engineers accepted 73% of generated tests; 36% were judged privacy-relevant.
- An LLM-based equivalent-mutant detection agent reached precision 0.79 / recall 0.47, rising to 0.95 / 0.96 with simple preprocessing.
- A follow-up Meta engineering blog post (2025-09-30, engineering.fb.com) reports Oct-Dec 2024 trials across Facebook, Instagram, WhatsApp, and wearables (Quest, Ray-Ban glasses), and launches the community "Catching JiTTest Challenge".

## Claims

- [[claims/Claim - Runtime control and verification improve agent reliability]] — adequacy by proven mutant-killing is a stronger verification standard than coverage, tightening the tests-as-backpressure gate.

## Connections

- [[concepts/code factories]]
- [[sources/TestGen-LLM]]
- [[sources/Meta Agentic Program Repair]]

## Notes

- Canonical URL: https://arxiv.org/abs/2501.12862
- Successor to TestGen-LLM in Meta's test-generation line; the mutation-first framing targets a specific concern class (privacy) rather than general adequacy.
- Acceptance and relevance percentages are Meta-internal engineer judgments.
