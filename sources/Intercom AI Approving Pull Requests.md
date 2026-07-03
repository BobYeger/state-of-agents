---
title: "AI is approving our pull requests: Here's how we made it safe"
aliases:
  - "Intercom AI PR approval"
source_type: "article"
kind: "ai-review-gate"
status: "verified"
year: 2026
publication_date: "2026-04-21"
publication_date_basis: "vendor_blog_page"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Kesha Mykhailov"
  - "Niamh Young"
venue: "Intercom Blog"
url: "https://www.intercom.com/blog/ai-is-approving-our-pull-requests-heres-how-we-made-it-safe/"
pdf_url: ""
created: 2026-07-03
updated: 2026-07-03
---

# Intercom AI Approving Pull Requests

## Summary

- Production deployment numbers: 19.2% of all PRs auto-approved by the review agent, 93% of PRs across main codebases AI-evaluated; approval is 6-16x faster at the 75th percentile.
- Quality outcome: AI-authored backend code revert rate 0.53% vs 5.39% for human-authored; frontend 0.22% vs 2.00%; a pilot of 100+ PRs had zero reverts; 497 fully autonomous PRs shipped in the first 4 weeks of broader rollout.
- Gate architecture is multi-agent decomposition, not one monolithic reviewer: separate agents assess problem-statement quality, diff-to-intent alignment, safety concerns, logical correctness, and best practices/anti-patterns.
- Size gate: the agent refuses to approve PRs that are too big, complex, or broadly scoped — structurally enforcing small incremental changes; human review stays optional and requestable at any time.
- Review goes beyond the visible diff: the agent traces execution paths through the codebase, and reviews are grounded in Intercom-specific engineering guidance that is continuously refined.
- Auditability as compliance surface: every AI-approved PR is labelled, logged, and queryable, mapped to SOC 2, HIPAA, ISO 27001, ISO 42001, and AIUC-1.

## Claims

- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[concepts/code factories]]
- [[concepts/human-in-the-loop agents]]
- [[sources/Modern Code Review at Google]]
- [[sources/GitHub Merge Queue Docs]]
- [[sources/Cursor Building Better Bugbot]]

## Notes

- Canonical URL: https://www.intercom.com/blog/ai-is-approving-our-pull-requests-heres-how-we-made-it-safe/
- The strongest practitioner evidence for tiered gate design at factory scale: a real company removed the human from a fifth of its merge gates and published throughput, revert-rate, and audit-design numbers.
- Vendor self-report on its own deployment; revert rate is the only quality metric given, and the AI-vs-human revert comparison may partly reflect the size gate (AI-approved changes are structurally smaller).
