---
title: "Loop Engineering"
aliases:
  - "Addy Osmani Loop Engineering"
  - "Loop Engineering"
source_type: "article"
kind: "harness-analysis"
status: "verified"
year: 2026
publication_date: null
publication_date_basis: "not_visible_in_defuddle_snapshot"
source_updated_date: "2026-06-14"
source_updated_date_basis: "snapshot_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Addy Osmani"
venue: "AddyOsmani.com"
url: "https://addyosmani.com/blog/loop-engineering/"
pdf_url: ""
artifacts:
  - "raw/articles/addy-osmani-loop-engineering.md"
created: 2026-06-14
updated: 2026-06-14
---

# Loop Engineering

## Summary

- Article framing loop engineering as the next abstraction above manual prompting: developers design systems that prompt, schedule, monitor, retry, and feed state back into agents.
- Important because it names the layer above harness engineering: harnesses provide the tool/context/runtime scaffold, while loops add cadence, repeated prompts, external state, and verification gates.
- Maps the pattern across Claude Code and Codex-style systems: scheduled tasks, `/loop`, `/goal`, hooks, workflows, worktrees, skills, connectors, subagents, and memory outside the conversation.

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[concepts/loop engineering]]
- [[operations/agent harnesses]]
- [[methods/ralph loop]]
- [[operations/worktree isolation]]
- [[operations/durable sessions]]
- [[operations/agent observability]]
- [[concepts/agent skills]]
- [[concepts/subagent context isolation]]
- [[sources/Claude Code Scheduled Tasks]]
- [[sources/Claude Code Workflows]]
- [[sources/OpenAI Codex Agent Loop]]

## Artifacts

- [[raw/articles/addy-osmani-loop-engineering.md]]

## Notes

- Canonical URL: https://addyosmani.com/blog/loop-engineering/
- The local raw artifact is intentionally a partial research snapshot, not a full article copy.
- Treat this as a live industry term source rather than a formal research paper.
