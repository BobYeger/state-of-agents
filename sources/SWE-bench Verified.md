---
title: "Introducing SWE-bench Verified"
aliases:
  - "SWE-bench Verified"
source_type: "article"
kind: "benchmark-curation"
status: "partial"
year: 2024
publication_date: "2024-08-13"
publication_date_basis: "vendor_blog_page"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "OpenAI"
venue: "OpenAI blog"
url: "https://openai.com/index/introducing-swe-bench-verified/"
pdf_url: ""
artifacts:
  - "raw/articles/swe-bench-verified.md"
created: 2026-07-03
updated: 2026-07-05
---

# Introducing SWE-bench Verified

## Summary

- 93 experienced Python developers annotated 1,699 random samples from the SWE-bench test set, producing a 500-sample human-validated subset (Hugging Face dataset: princeton-nlp/SWE-bench_Verified).
- Filtering targeted underspecified issue descriptions and overly specific unit tests that unfairly rejected valid solutions — the original SWE-bench systematically underestimated model capability.
- Annotators checked that problem statements are clear, test patches are correct, and tasks are solvable from the available information (per swebench.com/verified.html).
- Became the industry-standard reported coding metric from mid-2024 until OpenAI itself retired it in February 2026.
- Documents the "human-verify your benchmark" pattern: even a widely used eval needed expert annotation to separate model failure from task defects.

## Connections

- [[benchmarks/agent evaluation]]
- [[operations/agent evals]]
- [[sources/SWE-bench]]
- [[sources/OpenAI Retires SWE-bench Verified]]
- [[sources/Anthropic Demystifying Agent Evals]]

## Artifacts

- [[raw/articles/swe-bench-verified.md]]

## Notes

- Canonical URL: https://openai.com/index/introducing-swe-bench-verified/
- openai.com returns HTTP 403 to automated fetch; content verified via the Hugging Face dataset card and swebench.com/verified.html plus secondary coverage — hence status "partial".
