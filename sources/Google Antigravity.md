---
title: "Build with Google Antigravity, our new agentic development platform"
aliases:
  - "Antigravity"
  - "Google Antigravity platform"
source_type: "article"
kind: "agent-manager-ide"
status: "verified"
year: 2025
publication_date: "2025-11-18"
publication_date_basis: "google_developers_blog_page"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Google Antigravity team"
venue: "Google Developers Blog"
url: "https://developers.googleblog.com/build-with-google-antigravity-our-new-agentic-development-platform/"
pdf_url: ""
artifacts:
  - "raw/articles/google-antigravity.md"
created: 2026-07-03
updated: 2026-07-05
---

# Google Antigravity

## Summary

- Two-surface design: an Editor view (VS Code-fork IDE with tab completion and inline commands) plus a Manager surface, "a dedicated interface where you can spawn, orchestrate, and observe multiple agents working asynchronously" across workspaces — the strongest published example of a dedicated agent-manager surface.
- Agents emit Artifacts — task lists, implementation plans, screenshots, browser recordings — as verifiable deliverables; users comment on Artifacts like a document and the agent incorporates the feedback.
- Agents autonomously drive a browser to test and verify their own changes, without synchronous human intervention.
- Model-pluralist: Gemini 3 Pro with generous rate limits, plus full support for Anthropic Claude Sonnet 4.5 and OpenAI GPT-OSS.
- Launched alongside Gemini 3 in November 2025 (announced Nov 18; page dated Nov 20); public preview free for individuals on macOS, Windows, and Linux.

## Claims

- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[concepts/agent teams]]
- [[methods/multi-agent orchestration]]
- [[concepts/human-in-the-loop agents]]
- [[operations/agent observability]]
- [[concepts/computer use]]
- [[sources/Google Antigravity CLI Transition]]

## Artifacts

- [[raw/articles/google-antigravity.md]]

## Notes

- Canonical URL: https://developers.googleblog.com/build-with-google-antigravity-our-new-agentic-development-platform/
- Announcement/date discrepancy: announced Nov 18, 2025 but the page itself is dated Nov 20; card uses the announcement date.
- Antigravity later absorbed Google's terminal harness — see [[sources/Google Antigravity CLI Transition]].
