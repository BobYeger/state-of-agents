---
title: "Executable Code Actions Elicit Better LLM Agents (CodeAct)"
aliases:
  - "CodeAct"
source_type: "paper"
kind: "code-action-space"
status: "verified"
year: 2024
publication_date: "2024-02-01"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2402.01030"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Xingyao Wang"
  - "Yangyi Chen"
  - "Lifan Yuan"
  - "Yizhe Zhang"
  - "Yunzhu Li"
  - "Hao Peng"
  - "Heng Ji"
venue: "arXiv / ICML 2024"
url: "https://arxiv.org/abs/2402.01030"
pdf_url: "https://arxiv.org/pdf/2402.01030"
created: 2026-07-03
updated: 2026-07-03
---

# CodeAct

## Summary

- Proposes executable Python code as the unified agent action space, replacing JSON/text tool calls; enables tool composition, control flow, and dynamic revision of prior actions in multi-turn interaction.
- Up to 20% higher success rate than JSON/text action formats, evaluated across 17 LLMs on API-Bank and a new M3ToolEval benchmark.
- Releases CodeActInstruct (7k multi-turn interactions) and CodeActAgent (Llama2/Mistral fine-tunes) with an integrated Python interpreter capable of self-debugging.
- ICML 2024; first author Xingyao Wang went on to build OpenHands — a direct lineage from this paper to a production harness.

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Connections

- [[concepts/programmatic tool calling]]
- [[concepts/tool use]]
- [[systems/OpenHands]]
- [[sources/Cloudflare Code Mode MCP]]
- [[sources/Anthropic Code Execution with MCP]]

## Notes

- Canonical URL: https://arxiv.org/abs/2402.01030
- The intellectual ancestor of the "code mode" pattern: the vault's Cloudflare and Anthropic code-execution cards assume this result without citing the original evidence.
- The 20% figure is the maximum across models/benchmarks, not the average; check Table results before quoting.
