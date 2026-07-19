---
title: "Prompting Claude Fable 5"
aliases:
  - "Claude Fable 5 Prompting Guide"
  - "Fable 5 prompting"
source_type: "docs"
kind: "model-prompting-guide"
status: "verified"
year: 2026
publication_date: "2026-07-13"
publication_date_basis: "accessed_living_docs_no_visible_publication_date"
source_updated_date: "2026-07-13"
source_updated_date_basis: "snapshot_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Anthropic"
venue: "Claude Platform Docs"
url: "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5"
pdf_url: ""
artifacts:
  - "raw/docs/claude-fable-5-prompting-guide.md"
created: 2026-07-13
updated: 2026-07-13
---

# Prompting Claude Fable 5

## Summary

- Treats longer model turns as a harness migration issue: hard requests can run for many minutes and autonomous work for hours, so clients need longer timeouts, streaming, progress surfaces, and asynchronous checks rather than a blocking request loop.
- Anthropic says instructing Fable to audit progress claims against tool results nearly eliminated fabricated status reports in its tests. The recommended contract is to label unverified work, report failed tests faithfully, and claim completion only with evidence.
- Recommends frequent asynchronous delegation and long-lived subagents whose contexts persist across subtasks, both to avoid waiting on the slowest worker and to retain prompt-cache benefits. Fresh-context verifier subagents are preferred over self-critique for periodic checks.
- Recommends simple external memory, even one Markdown lesson per file, recording corrections and confirmed approaches without duplicating repository or chat history; wrong lessons should be deleted rather than accumulated.
- Documents model-specific failure edges: rare text-only promises without the corresponding tool call, premature handoff when a harness exposes a context countdown, unrequested tidying at high effort, and reasoning-extraction refusals when old prompts demand visible internal reasoning. Anthropic warns that overly prescriptive skills written for earlier models can degrade Fable.

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]
- [[claims/Claim - Context management is an agent architecture choice]]

## Connections

- [[sources/Claude Fable 5 and Claude Mythos 5]]
- [[operations/agent harnesses]]
- [[operations/agent memory]]
- [[concepts/subagent context isolation]]
- [[concepts/long-horizon agents]]
- [[maps/Agent Skills Map]]
- [[sources/Anthropic Effective Harnesses for Long-Running Agents]]

## Artifacts

- [[raw/docs/claude-fable-5-prompting-guide.md]]

## Notes

- Canonical URL: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5
- Living documentation snapshot from 2026-07-13. Behavioral observations and intervention effects are Anthropic's internal tests; most sample sizes and benchmark definitions are not supplied.
- The guide is model-specific operational evidence, not a general instruction to add more scaffolding. Its migration advice explicitly includes removing legacy instructions when the stronger model performs better without them.
