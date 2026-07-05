---
title: "GitHub Copilot: Meet the new coding agent"
aliases:
  - "Copilot coding agent"
source_type: "article"
kind: "async-coding-agent"
status: "verified"
year: 2025
publication_date: "2025-05-19"
publication_date_basis: "github_blog_page"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Thomas Dohmke"
venue: "GitHub Blog"
url: "https://github.blog/news-insights/product-news/github-copilot-meet-the-new-coding-agent/"
pdf_url: ""
artifacts:
  - "raw/articles/github-copilot-coding-agent.md"
created: 2026-07-03
updated: 2026-07-05
---

# GitHub Copilot Coding Agent

## Summary

- The agent's compute environment is GitHub Actions: it boots a VM, clones the repo, analyzes the codebase, and pushes commits to a draft pull request, with session logs streaming its reasoning — the clearest published example of CI infrastructure reused as an agent sandbox.
- Security model: the agent can only push to branches it creates; the requester cannot approve the agent's own PR; internet access is restricted to a trusted allowlist; CI/CD workflows require human approval before running.
- Uses RAG via GitHub code search and MCP to pull external context; vision model support lets it read screenshots and mockups attached to issues.
- Triggered by assigning a GitHub issue to Copilot on github.com, GitHub Mobile, or the CLI, or by prompting from VS Code — the issue tracker acts as the control plane.
- Launched 2025-05-19 (Microsoft Build) for Copilot Enterprise and Pro+; from 2025-06-04 each model request costs one premium request.

## Connections

- [[operations/sandboxes]]
- [[concepts/issue tracker control plane]]
- [[operations/permissions]]
- [[protocols/MCP]]
- [[systems/deployed agent products]]
- [[sources/GitHub Agent HQ]]

## Artifacts

- [[raw/articles/github-copilot-coding-agent.md]]

## Notes

- Canonical URL: https://github.blog/news-insights/product-news/github-copilot-meet-the-new-coding-agent/
- Launch-era description; the agent was later folded into the Agent HQ multi-vendor surface (see [[sources/GitHub Agent HQ]]), so operational details may have shifted since.
