---
title: "GPT-5.6: Frontier intelligence that scales with your ambition"
aliases:
  - "OpenAI GPT-5.6"
  - "GPT-5.6"
  - "GPT-5.6 Sol"
source_type: "article"
kind: "frontier-model-release"
status: "verified"
year: 2026
publication_date: "2026-07-09"
publication_date_basis: "openai_visible_page_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "OpenAI"
venue: "OpenAI"
url: "https://openai.com/index/gpt-5-6/"
pdf_url: ""
artifacts:
  - "raw/articles/openai-gpt-5.6.md"
created: 2026-07-13
updated: 2026-07-13
---

# OpenAI GPT-5.6

## Summary

- General-availability launch of a three-model family: Sol as the flagship, Terra as the balanced model, and Luna as the lowest-cost model. Sol is priced at $5/M input and $30/M output tokens, Terra at $2.50/$15, and Luna at $1/$6.
- Makes orchestration part of the model and API surface. Programmatic Tool Calling lets the model write JavaScript that coordinates tools, while the Responses API multi-agent beta lets a root agent create isolated subagent contexts and coordinate their work.
- Adds `max` reasoning effort and an `ultra` product mode that coordinates four agents by default. OpenAI's release evaluations show parallel agents improving score-versus-latency frontiers, but these are vendor-run launch measurements rather than independent evaluations.
- Introduces explicit prompt-cache breakpoints and a 30-minute minimum cache life. Cache writes cost 1.25× uncached input while cache reads retain a 90% discount, making prefix and cache policy an explicit harness cost decision.
- The most reusable release finding is architectural rather than a benchmark rank: model-directed parallelism, code-mediated tool orchestration, reasoning effort, and cache control are exposed as separate runtime levers.

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
- [[claims/Claim - Agent teams need explicit organization]]

## Connections

- [[systems/Codex]]
- [[concepts/programmatic tool calling]]
- [[concepts/subagent context isolation]]
- [[operations/agent harnesses]]
- [[operations/cost control]]
- [[sources/OpenAI Responses API Multi-Agent]]
- [[sources/OpenAI Programmatic Tool Calling]]
- [[sources/OpenAI GPT-5.6 System Card]]
- [[sources/OpenAI GPT-5.5]]

## Artifacts

- [[raw/articles/openai-gpt-5.6.md]]

## Notes

- Canonical URL: https://openai.com/index/gpt-5-6/
- Benchmark, latency, and estimated-cost comparisons on the launch page are OpenAI's own measurements and depend on reasoning effort, agent count, harness, and simulated production pricing. Treat them as release evidence, not a stable cross-vendor ranking.
- The launch page was archived through a readable proxy because direct automated extraction returned HTTP 403; the source URL and all claims remain the official OpenAI page.
