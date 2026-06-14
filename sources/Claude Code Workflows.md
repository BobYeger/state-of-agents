---
title: "Orchestrate subagents at scale with dynamic workflows"
aliases:
  - "Claude Code Workflows"
  - "Claude Code Dynamic Workflows"
source_type: "docs"
kind: "harness-docs"
status: "verified"
year: 2026
publication_date: "2026-06-14"
publication_date_basis: "accessed_living_docs_no_visible_publication_date"
source_updated_date: "2026-06-14"
source_updated_date_basis: "snapshot_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Anthropic"
venue: "Claude Code Docs"
url: "https://code.claude.com/docs/en/workflows"
pdf_url: ""
artifacts:
  - "raw/docs/claude-code-workflows.md"
created: 2026-06-01
updated: 2026-06-14
---

# Orchestrate subagents at scale with dynamic workflows

## Summary

- Official Claude Code docs for dynamic workflows: JavaScript orchestration scripts that coordinate many subagents in the background while the main session stays responsive.
- Important because it separates orchestration state from the conversation context: intermediate results live in script variables, while agents do the file, shell, and web work.
- The current docs compare workflows against subagents, skills, and agent teams; workflows are the option where the script, not Claude turn-by-turn, holds the plan.
- Defines practical limits and controls: bundled `/deep-research`, `ultracode` workflow opt-in, workflow approval prompts, saved workflow commands with `args`, scripts under `~/.claude/projects/`, up to 16 concurrent agents, up to 1,000 agents per run, pause/resume within a session, and explicit cost warnings.

## Claims

- [[claims/Claim - Agent teams need explicit organization]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Connections

- [[systems/Claude Code]]
- [[operations/agent harnesses]]
- [[methods/multi-agent orchestration]]
- [[operations/permissions]]
- [[operations/cost control]]
- [[concepts/subagent context isolation]]
- [[concepts/loop engineering]]

## Artifacts

- [[raw/docs/claude-code-workflows.md]]

## Notes

- Canonical URL: https://code.claude.com/docs/en/workflows
- Publication date is the access date because the living docs page did not expose a stable publication date in this pass.
- Distinction to preserve: subagents, skills, and agent teams leave Claude or a lead agent as the turn-by-turn orchestrator, while workflows move the orchestration plan into executable code.
- Trigger detail as of the 2026-06-14 snapshot: direct workflow requests and the `ultracode` keyword trigger a workflow; before v2.1.160 the literal trigger keyword was `workflow`.
