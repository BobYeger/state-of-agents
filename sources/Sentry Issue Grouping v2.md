---
title: "Issue Grouping: Smarter, Faster, Half as Wrong"
aliases:
  - "Sentry grouping v2"
source_type: "article"
kind: "signal-dedup"
status: "verified"
year: 2026
publication_date: "2026-06-12"
publication_date_basis: "vendor_blog_page"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Kush Dubey"
  - "Yuval Mandelboum"
venue: "Sentry Blog (engineering)"
url: "https://blog.sentry.io/enhancing-issue-grouping/"
pdf_url: ""
artifacts:
  - "raw/articles/sentry-issue-grouping-v2.md"
created: 2026-07-03
updated: 2026-07-05
---

# Sentry Issue Grouping v2

## Summary

- Grouping v2 (rolled out 2026-04-22) prevents 70% of would-be new issues from being created, up from 50% with v1.
- Overgrouping — merging distinct root causes into one issue — halved from 8% to 4% globally; the worst-hit platforms improved from 30-60% overgrouping to 2-15%.
- Training pipeline: Claude Sonnet 3.5 with 1,024-token thinking budgets labeled hundreds of thousands of stacktrace pairs (10-8,192 tokens), validated against internal expert "grouping czars"; a lightweight ModernBERT model was trained on the result; training code published at getsentry/grouping-trainer.
- The model is calibrated to err toward separation when ambiguous — a named design stance on the dedup precision/recall tradeoff.
- Triage-quality measurement made continuous: batch-labeling pipelines over merged issues turned overgrouping from a "silent but deadly failure mode" into a SQL-queryable metric.
- Inference is 6x faster than v1; p50 HNSW lookup dropped 52ms to 12ms, insertion 270ms to 13ms.

## Connections

- [[concepts/code factories]]
- [[operations/agent evals]]
- [[sources/Sentry Issue Noise Reduction]]
- [[sources/Sentry Seer]]

## Artifacts

- [[raw/articles/sentry-issue-grouping-v2.md]]

## Notes

- Canonical URL: https://blog.sentry.io/enhancing-issue-grouping/
- The best available public source on measuring triage quality: overgrouping rate as a first-class metric plus LLM-labeled evaluation pipelines (frontier-model labeler distilled into a small production model).
- All figures are Sentry-internal measurements on Sentry's own traffic.
