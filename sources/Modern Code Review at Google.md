---
title: "Modern Code Review: A Case Study at Google"
aliases:
  - "Google code review study"
source_type: "paper"
kind: "code-review-study"
status: "verified"
year: 2018
publication_date: "2018-05"
publication_date_basis: "icse_seip_2018_proceedings"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Caitlin Sadowski"
  - "Emma Söderberg"
  - "Luke Church"
  - "Michal Sipko"
  - "Alberto Bacchelli"
venue: "ICSE-SEIP 2018 (DOI 10.1145/3183519.3183525)"
url: "https://sback.it/publications/icse2018seip.pdf"
pdf_url: "https://sback.it/publications/icse2018seip.pdf"
created: 2026-07-03
updated: 2026-07-03
---

# Modern Code Review at Google

## Summary

- Baseline human throughput at Google: roughly 20,000 code changes committed per workday; the study analyzed 9M reviewed changes (Jan 2014 - Jul 2016) from over 25,000 authors/reviewers plus 13M review comments.
- Reviewer capacity: the median developer authors ~3 changes/week (80% author fewer than 7) and the median reviewer reviews 4 changes/week (80% review fewer than 10); developers spend a mean of 3.2 h/week (median 2.6 h) reviewing.
- Latency: median time to first feedback is under 1 h for small changes, ~5 h for very large; overall median review latency is under 4 h vs 14.7-24 h reported at Microsoft, AMD, and Chrome OS; 70% of changes commit less than 24 h after mail-out.
- Gate design that enables this: the median change is 24 lines, over 35% touch one file, ~90% touch fewer than 10 files; one reviewer is sufficient (fewer than 25% of changes have more than 1 reviewer, median 1); 80% of changes need at most one comment-resolution iteration.
- Structural gates: ownership (per-directory owner approval) plus per-language readability certification; Tricorder static analysis (110 analyzers, over 30 languages) surfaces findings inside the review UI, and analyzers with high "Not useful" click rates are fixed or disabled — a feedback loop that preserves reviewer trust.
- Comments per change grow with diff size, peaking near 12.5 comments at ~1250 lines — quantifying why small changes are the unit that keeps review scalable.

## Connections

- [[concepts/code factories]]
- [[concepts/human-in-the-loop agents]]
- [[sources/GitHub Merge Queue Docs]]
- [[sources/DORA State of AI-assisted Software Development 2025]]
- [[sources/How Humans Review AI-Generated Pull Requests]]

## Notes

- Canonical URL: https://sback.it/publications/icse2018seip.pdf (author-hosted copy; ACM DOI 10.1145/3183519.3183525)
- The canonical pre-agents reviewer-capacity baseline: any "agents produce 10x more PRs" claim should be read against Google's measured human ceiling (3-4 changes reviewed per person per week, ~3 h/week) and the gate design (small diffs, single owner-reviewer, analyzer pre-filtering) that made human review scale.
- Data ends mid-2016; numbers describe Google's monorepo culture and tooling, not industry averages.
