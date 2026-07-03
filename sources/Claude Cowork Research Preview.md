---
title: "Claude Cowork (research preview)"
aliases:
  - "Claude Cowork"
  - "Cowork"
source_type: "article"
kind: "computer-agent-product"
status: "verified"
year: 2026
publication_date: "2026-01-12"
publication_date_basis: "claude_blog_page"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Anthropic"
venue: "Claude Blog"
url: "https://claude.com/blog/cowork-research-preview"
pdf_url: ""
created: 2026-07-03
updated: 2026-07-03
---

# Claude Cowork Research Preview

## Summary

- Announced 2026-01-12 as a research preview "computer agent" for non-technical knowledge workers — "Claude Code for the rest of your work" — built into Claude Desktop (macOS first, Windows later with full feature parity).
- Architecture (per Simon Willison's same-day teardown): the Claude Code harness wrapped in a friendlier UI, running in a containerized VM via Apple's VZVirtualMachine; user-granted folders are mounted at `/sessions/[session-id]/mnt/[folder-name]`, with no host access outside the sandbox perimeter.
- Flow: the user states an outcome; Claude plans, then executes code, terminal, and file operations autonomously in the background with approval gates before significant actions, and returns a finished deliverable. Supports scheduled recurring tasks, plugins, and MCP connectors.
- Rollout: initially Max-only ($100-200/mo); extended to $20/mo Pro subscribers by 2026-01-16; GA 2026-04-09 with six enterprise features (admin-managed access and spend).
- Anthropic states the product was built primarily by Claude Code itself in about 1.5 weeks.

## Connections

- [[operations/agent harnesses]]
- [[operations/sandboxes]]
- [[systems/Claude Code]]
- [[concepts/agent operating surfaces]]
- [[sources/Anthropic When AI Builds Itself]]
- [[sources/TheAgentCompany]]

## Notes

- Canonical URL: https://claude.com/blog/cowork-research-preview
- The harness-reuse architecture details come from Willison's external teardown, not the announcement itself; treat mount-path specifics as observed-at-launch, subject to change.
- The "built by Claude Code in ~1.5 weeks" figure is a vendor claim with no published methodology.
