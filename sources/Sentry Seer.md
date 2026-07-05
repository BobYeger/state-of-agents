---
title: "Seer, Sentry's AI Debugger, is Generally Available"
aliases:
  - "Seer"
source_type: "article"
kind: "triage-and-fix-agent"
status: "verified"
year: 2025
publication_date: "2025-06-17"
publication_date_basis: "vendor_blog_page"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Tillman Elser"
venue: "Sentry Blog"
url: "https://blog.sentry.io/seer-sentrys-ai-debugger-is-generally-available/"
pdf_url: ""
artifacts:
  - "raw/articles/sentry-seer.md"
created: 2026-07-03
updated: 2026-07-05
---

# Sentry Seer

## Summary

- Seer reached GA on 2025-06-17: an agent that aggregates stack traces, commit history, traces, spans, logs, and profiles for root-cause analysis; Sentry claims 94.5% root-cause accuracy.
- 38,000+ issues were analyzed during beta, claimed to save "over 2 years of collective dev time".
- Named triage mechanisms: Automated Issue Scans (every incoming issue is scanned), Actionability Scoring to surface high-priority issues, and an optional Automated Fixes mode that drafts PRs without manual invocation.
- Pricing encodes the pipeline economics: $20/month seat, $1 per fix run, $0.003 per issue scan (with $25/month credits) — the scan/fix cost asymmetry positions triage-scan as the cheap always-on front gate.
- Agent tool surface: grep-like code search, docs parsing, commit-history analysis, and direct file modification; scans can trigger Slack alerts; no merge happens without human approval.

## Connections

- [[concepts/code factories]]
- [[concepts/issue tracker control plane]]
- [[systems/deployed agent products]]
- [[operations/cost control]]
- [[sources/Sentry Issue Noise Reduction]]
- [[sources/Sentry Issue Grouping v2]]

## Artifacts

- [[raw/articles/sentry-seer.md]]

## Notes

- Canonical URL: https://blog.sentry.io/seer-sentrys-ai-debugger-is-generally-available/
- The 94.5% root-cause accuracy and dev-time-saved figures are vendor claims with no published methodology; treat as marketing-adjacent until independently measured.
- The deployed signal-to-fix pipeline shape (scan every issue, score actionability, optionally auto-fix) is the durable takeaway regardless of the accuracy claim.
