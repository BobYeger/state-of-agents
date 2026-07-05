---
title: "Multi-Agents: What's Actually Working"
aliases:
  - "Multi-Agents: What's Actually Working"
source_type: "article"
kind: "position-essay"
status: "verified"
year: 2026
publication_date: "2026-04-22"
publication_date_basis: "cognition_blog_page"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Walden Yan"
venue: "Cognition blog"
url: "https://cognition.com/blog/multi-agents-working"
pdf_url: ""
artifacts:
  - "raw/articles/cognition-multi-agents-whats-actually-working.md"
created: 2026-07-03
updated: 2026-07-05
---

# Cognition Multi-Agents Whats Actually Working

## Summary

- Ten-month follow-up to "Don't Build Multi-Agents" that narrows rather than retracts the 2025 position: multiple agents may contribute intelligence, but writes stay single-threaded (the single-writer principle).
- Devin + Devin Review code-review loop catches ~2 bugs per PR, 58% of them severe; reviewers perform best with completely clean context rather than shared context.
- Three named production patterns: the code-review loop; "smart friend" escalation from a weaker primary model to a stronger model; and manager-child delegation coordinated over internal MCP.
- Production scale-signals: enterprise Devin usage grew ~8x over six months; SWE-1.6 is described as "Opus-4.5 level"; cross-frontier Claude+GPT pairings run in production via capability routing.
- Attributes the gains to context-length reduction (combating "context rot"/attention limits) and dedicated communication-bridge prompting between agents.

## Claims

- [[claims/Claim - Agent teams need explicit organization]]
- [[claims/Claim - Coordination is a cost the task must justify]]

## Connections

- [[methods/multi-agent orchestration]]
- [[concepts/agent teams]]
- [[concepts/subagent context isolation]]
- [[methods/runtime routing]]
- [[sources/Cognition Dont Build Multi-Agents]]
- [[sources/Devin Manages Devins]]

## Artifacts

- [[raw/articles/cognition-multi-agents-whats-actually-working.md]]

## Notes

- Canonical URL: https://cognition.com/blog/multi-agents-working
- All production numbers (bugs per PR, severity share, 8x growth) are Cognition's own telemetry, not independently audited.
- Pairing this with the 2025 essay gives the full arc of the single-writer vs parallel-agents debate from one vendor.
