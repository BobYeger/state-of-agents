---
title: "Enabling Agent 3 to Self-Test at Scale with REPL-Based Verification"
aliases:
  - "Replit Agent 3 automated self-testing"
source_type: "article"
kind: "self-testing-loop"
status: "verified"
year: 2025
publication_date: "2025-12-15"
publication_date_basis: "vendor_blog_page"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Replit"
venue: "Replit Blog"
url: "https://replit.com/blog/automated-self-testing"
pdf_url: ""
artifacts:
  - "raw/articles/replit-agent-3-self-testing.md"
created: 2026-07-03
updated: 2026-07-05
---

# Replit Agent 3 Self-Testing

## Summary

- Testing runs as a separate subagent: the main agent hands it high-level action plans; it runs observe-act-repeat cycles and returns summarized pass/fail results, keeping test detail out of the main agent's context (which runs at 80k-100k tokens).
- Mechanism: the agent writes JavaScript executed in a sandboxed notebook REPL with injected Playwright helpers; variables and browser sessions persist across executions, enabling iterative page exploration.
- Test context is augmented with DOM representations including ARIA labels, database query utilities, and client/server logs.
- Cost/speed claims: ~$0.20 per session for complex multi-hundred-step testing, versus ~$0.50 and 30-90s per 5-field form for pixel-based computer-use agents (Replit claims 3x faster, 10x cheaper).
- Replit credits this self-testing loop with pushing Agent 3 from ~20 minutes to 200+ minutes of continuous autonomous runtime (Agent 3 announced 2025-09-10 alongside a $250M raise at a $3B valuation).

## Claims

- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[concepts/loop engineering]]
- [[concepts/subagent context isolation]]
- [[concepts/long-horizon agents]]
- [[operations/agent harnesses]]
- [[concepts/computer use]]
- [[systems/deployed agent products]]

## Artifacts

- [[raw/articles/replit-agent-3-self-testing.md]]

## Notes

- Canonical URL: https://replit.com/blog/automated-self-testing (blog.replit.com URLs 301-redirect to replit.com/blog)
- Cost and speed comparisons are vendor-reported and unaudited; the 3x/10x framing compares against Replit's own prior pixel-based approach.
- Most mechanism-rich public account of a production self-testing/verification loop; core evidence for self-healing code factories.
