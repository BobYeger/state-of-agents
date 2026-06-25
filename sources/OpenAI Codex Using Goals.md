---
title: "Using Goals in Codex"
aliases:
  - "OpenAI Codex Goals"
  - "Codex Goals"
  - "Codex /goal"
  - "Codex Goal mode"
source_type: "docs"
kind: "cookbook"
status: "verified"
year: 2026
publication_date: "2026-05-09"
publication_date_basis: "openai_cookbook_visible_published_date"
source_updated_date: "2026-06-16"
source_updated_date_basis: "snapshot_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Raj Pathak"
  - "Stefano Fabbri"
venue: "OpenAI Cookbook"
url: "https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex"
pdf_url: ""
artifacts:
  - "raw/docs/openai-codex-using-goals.md"
created: 2026-06-16
updated: 2026-06-16
---

# Using Goals in Codex

## Summary

- Official OpenAI Cookbook guide for Codex Goals, a Codex-managed objective state that keeps Codex working toward a defined outcome across turns.
- Important because it makes a slash command into a harness primitive: objective persistence, lifecycle controls, continuation policy, budget handling, and evidence-based completion.
- Defines strong goals as compact contracts with an outcome, verification surface, constraints, boundaries, iteration policy, and blocked stop condition.
- Positions Goals as useful for uncertain multi-step work such as profiling, flaky-test investigation, migrations, benchmark-driven tuning, and research audits, while normal prompts remain better for one-off tasks.

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[systems/Codex]]
- [[operations/agent harnesses]]
- [[operations/durable sessions]]
- [[operations/agent observability]]
- [[operations/cost control]]
- [[concepts/loop engineering]]
- [[concepts/outcomes and rubric graders]]
- [[methods/hook-based control]]
- [[methods/ralph loop]]
- [[reports/Harness Engineering Report]]

## Artifacts

- [[raw/docs/openai-codex-using-goals.md]]

## Notes

- Canonical URL: https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex
- Codex manual Goal mode URL: https://developers.openai.com/codex/prompting#goal-mode
- Raw notebook URL: https://raw.githubusercontent.com/openai/openai-cookbook/main/examples/codex/using_goals_in_codex.ipynb
- Publication date basis: visible OpenAI Cookbook date, May 9, 2026.
- The key architecture claim is that a Goal is persisted task objective state, not global memory or project-level instruction.
- The page says Goals are available starting in Codex 0.128.0.
