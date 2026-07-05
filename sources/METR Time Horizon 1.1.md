---
title: "Time Horizon 1.1"
aliases:
  - "TH1.1"
source_type: "report"
kind: "capability-measurement"
status: "verified"
year: 2026
publication_date: "2026-01-29"
publication_date_basis: "metr_blog_page"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "METR"
venue: "METR blog"
url: "https://metr.org/blog/2026-1-29-time-horizon-1-1/"
pdf_url: ""
artifacts:
  - "raw/reports/metr-time-horizon-1.1.md"
created: 2026-07-03
updated: 2026-07-05
---

# Time Horizon 1.1

## Summary

- Updated 50%-time-horizon methodology: task suite expanded 34% from 170 to 228 tasks (73 added, 15 removed, 53 updated); 8+ hour tasks doubled from 14 to 31.
- Infrastructure migrated from METR's in-house Vivaria to the UK AI Security Institute's open-source Inspect framework; 14 of 33 original models were re-estimated under the new setup.
- Revised doubling estimates: ~131 days since 2023 (vs 165 in the original paper, ~20% faster) and ~89 days since 2024; the full-period 2019-2026 trend is ~196.5 days — the original "7-month doubling" is now the conservative long-run figure.
- TH1.1 frontier 50% horizons: Claude Opus 4.5 at 320 min [CI 170-729], GPT-5 at 214 min [117-480], o3 at 121 min [74-201], Claude Opus 4 at 101 min [58-170].
- Caveat from METR itself: only 5 of 31 long tasks have measured human baseline times (the rest use estimates), so confidence intervals on long-horizon claims remain wide.

## Connections

- [[sources/METR Measuring Long Task Completion]]
- [[concepts/long-horizon agents]]
- [[benchmarks/long-horizon benchmarks]]
- [[benchmarks/agent evaluation]]
- [[sources/Anthropic Measuring Agent Autonomy]]

## Artifacts

- [[raw/reports/metr-time-horizon-1.1.md]]

## Notes

- Canonical URL: https://metr.org/blog/2026-1-29-time-horizon-1-1/
- Supersedes the 2025 paper's since-2023 doubling estimate; the vault should quote TH1.1 numbers for post-2023 trend claims.
- Wide CIs on frontier-model horizons (e.g. Opus 4.5's 170-729 min) mean point estimates should be reported with intervals.
