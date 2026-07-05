---
title: "An important update: Transitioning Gemini CLI to Antigravity CLI"
aliases:
  - "Antigravity CLI"
  - "Gemini CLI retirement"
source_type: "article"
kind: "harness-consolidation"
status: "verified"
year: 2026
publication_date: "2026-05-19"
publication_date_basis: "google_developers_blog_page"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Google"
venue: "Google Developers Blog"
url: "https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/"
pdf_url: ""
artifacts:
  - "raw/articles/google-antigravity-cli-transition.md"
created: 2026-07-03
updated: 2026-07-05
---

# Google Antigravity CLI Transition

## Summary

- 2026-05-19: Antigravity CLI available to all; 2026-06-18: Gemini CLI and the Gemini Code Assist IDE extensions stop serving requests for free-tier and Google AI Pro/Ultra users (paid Gemini Code Assist Standard/Enterprise/Cloud licenses keep unchanged access).
- One of the fastest kill-and-replace cycles for a major vendor harness: Gemini CLI, open-sourced mid-2025, retired within roughly a year.
- Migration preserves the Gemini CLI feature set — Agent Skills, Hooks, and Subagents carry over; Extensions are renamed "plugins" — evidence that the skills/hooks/subagents surface has become the cross-vendor harness baseline.
- The new CLI is Go-based (faster), supports asynchronous background multi-agent orchestration, and shares the same agent harness as the Antigravity 2.0 desktop app.
- Google's stated rationale: workflows "outgrew" the single-agent CLI era — users need "multiple agents communicating with each other," so Google consolidated into "a single product built for today's multi-agent reality," under Antigravity as "our premier agent-first development platform."

## Connections

- [[operations/agent harnesses]]
- [[concepts/agent skills]]
- [[methods/hook-based control]]
- [[methods/multi-agent orchestration]]
- [[sources/Google Antigravity]]

## Artifacts

- [[raw/articles/google-antigravity-cli-transition.md]]

## Notes

- Canonical URL: https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/
- The "multi-agent reality" rationale is vendor framing for a deprecation; the load-bearing facts are the dates, the preserved feature set, and the shared-harness architecture.
