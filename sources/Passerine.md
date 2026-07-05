---
title: "Evaluating Agent-based Program Repair at Google"
aliases:
  - "Passerine"
source_type: "paper"
kind: "program-repair"
status: "verified"
year: 2025
publication_date: "2025-01-13"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2501.07531"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Pat Rondon"
  - "Renyao Wei"
  - "José Cambronero"
  - "Jürgen Cito"
  - "Aaron Sun"
  - "Siddhant Sanyam"
  - "Michele Tufano"
  - "Satish Chandra"
venue: "arXiv / ICSE 2025 SEIP (Google)"
url: "https://arxiv.org/abs/2501.07531"
pdf_url: "https://arxiv.org/pdf/2501.07531"
artifacts:
  - "raw/papers/Evaluating Agent-based Program Repair at Google.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# Passerine

## Summary

- Evaluated on 178 bugs from Google's internal issue tracker — 78 human-reported, 100 machine-reported — deliberately not SWE-bench; the paper shows enterprise bugs differ from SWE-bench in language diversity, size, and change spread.
- With 20 trajectory samples and Gemini 1.5 Pro: plausible (test-passing) patches for 73% of machine-reported and 25.6% of human-reported bugs; semantically equivalent to ground truth for 43% and 17.9% respectively.
- Pipeline is bug abstention, then patch generation, then patch validation and selection, with at most one patch per bug forwarded to human review — an explicit acceptance-gate architecture.
- Passerine is "an agent similar in spirit to SWE-Agent" operating inside Google's internal development environment.
- Google follow-up BRT Agent (arXiv 2502.01821, Feb 2025): feeding an auto-generated bug-reproduction test as initial input raises Passerine's plausible-fix rate from 57% to 74%.

## Connections

- [[concepts/code factories]]
- [[sources/SWE-bench]]
- [[sources/Agentless]]
- [[sources/Meta Agentic Program Repair]]

## Artifacts

- [[raw/papers/Evaluating Agent-based Program Repair at Google.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2501.07531
- The machine-reported vs human-reported split matters for factory design: sanitizer/fuzzer-style machine-reported bugs are far more tractable than human bug reports.
- Strongest available evidence that SWE-bench underrepresents enterprise bug distributions; "plausible" means test-passing, not necessarily correct.
