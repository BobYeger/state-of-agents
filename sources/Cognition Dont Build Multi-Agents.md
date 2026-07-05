---
title: "Don't Build Multi-Agents"
aliases:
  - "Don't Build Multi-Agents"
source_type: "article"
kind: "position-essay"
status: "verified"
year: 2025
publication_date: "2025-06-12"
publication_date_basis: "cognition_blog_page"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Walden Yan"
venue: "Cognition blog"
url: "https://cognition.com/blog/dont-build-multi-agents"
pdf_url: ""
artifacts:
  - "raw/articles/cognition-dont-build-multi-agents.md"
created: 2026-07-03
updated: 2026-07-05
---

# Cognition Dont Build Multi-Agents

## Summary

- The canonical industry counter-position on multi-agent design. Two stated principles: (1) share context as full agent traces, not just individual messages; (2) actions carry implicit decisions, and conflicting decisions produce bad results.
- Concludes (as of mid-2025) that a single-threaded linear agent plus context compression is more reliable than parallel subagents, because parallel writers make conflicting implicit decisions.
- Coins/elevates "context engineering" as the successor to prompt engineering and "the #1 job of engineers building AI agents."
- Uses Claude Code subagents as supporting evidence: subagents only answer questions (no parallel writing), keeping investigative context out of the main history.
- Cites the decline of edit-apply models (a big model writes a markdown diff, a small model applies it) as an example of why splitting decision-making across models fails; explicitly critiques OpenAI Swarm and Microsoft AutoGen-style frameworks as tempting but flawed abstractions.

## Claims

- [[claims/Claim - Coordination is a cost the task must justify]]
- [[claims/Claim - Context management is an agent architecture choice]]

## Connections

- [[methods/multi-agent orchestration]]
- [[concepts/context engineering]]
- [[concepts/subagent context isolation]]
- [[concepts/multi-agent systems]]
- [[sources/Why Do Multi-Agent LLM Systems Fail]]
- [[sources/Cognition Multi-Agents Whats Actually Working]]

## Artifacts

- [[raw/articles/cognition-dont-build-multi-agents.md]]

## Notes

- Canonical URL: https://cognition.com/blog/dont-build-multi-agents
- A 2025 position piece from a vendor whose product (Devin) was single-threaded at the time; read alongside the 2026 follow-up ([[sources/Cognition Multi-Agents Whats Actually Working]]), which narrows rather than retracts it.
