---
title: "Orchestrate teams of Claude Code sessions"
aliases:
  - "Claude Code Agent Teams"
source_type: "docs"
kind: "harness-docs"
status: "verified"
year: 2026
publication_date: "2026-05-26"
publication_date_basis: "accessed_living_docs_no_visible_publication_date"
source_updated_date: "2026-08-24"
source_updated_date_basis: "snapshot_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Anthropic"
venue: "Claude Code Docs"
url: "https://code.claude.com/docs/en/agent-teams"
pdf_url: ""
artifacts:
  - "raw/docs/claude-code-agent-teams.md"
created: 2026-05-26
updated: 2026-08-24
---

# Claude Code Agent Teams

## Summary

- Official Claude Code docs for coordinating multiple Claude Code sessions as a team.
- Cleanly distinguishes agent teams from subagents: teammates are independent sessions with their own context windows and can communicate directly.
- Agent Teams are experimental and disabled by default. They make a lead, shared task list, teammate context, direct messaging, and display modes first-class harness concepts.
- Separate, independently started sessions can now communicate through [[sources/Claude Code Cross-Session Messaging]], but that peer channel does not create an Agent Team or shared task list.

## Claims

- [[claims/Claim - Agent teams need explicit organization]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Connections

- [[concepts/agent teams]]
- [[concepts/subagent context isolation]]
- [[operations/agent harnesses]]
- [[operations/worktree isolation]]
- [[methods/hook-based control]]
- [[maps/Agent Teams and Workforces Map]]
- [[sources/Claude Code Hooks]]
- [[sources/Claude Code Cross-Session Messaging]]

## Artifacts

- [[raw/docs/claude-code-agent-teams.md]]

## Notes

- Canonical URL: https://code.claude.com/docs/en/agent-teams
- Publication date basis: accessed_living_docs_no_visible_publication_date.
- The living docs describe Agent Teams as of Claude Code v2.1.178 and explicitly route independent-session messaging to the separate cross-session feature.
