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
source_updated_date: "2024-06-07"
source_updated_date_basis: "arxiv_v4_submission_history"
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
artifacts:
  - "raw/papers/Executable Code Actions Elicit Better LLM Agents (CodeAct).pdf"
created: 2026-07-03
updated: 2026-10-05
---

# CodeAct

## Summary

- Proposes executable Python code as the unified agent action space, replacing JSON/text tool calls; enables tool composition, control flow, and dynamic revision of prior actions in multi-turn interaction.
- Evaluates code versus JSON/text action formats across 17 LLMs on API-Bank and M3ToolEval; reports up to 20 percentage points of success-rate improvement in the tested settings.
- Releases CodeActInstruct (7k multi-turn interactions) and CodeActAgent (Llama2/Mistral fine-tunes) with an integrated Python interpreter capable of self-debugging.
- ICML 2024 research evidence for changing the action representation, distinct from adopting a particular hosted code-execution service.

## Evidence and Limits

- The maximum improvement is not the average or a guarantee for newer models. Interpreter feedback supports correction, but the paper notes hallucinated variable contents as a remaining failure mode.
- Code composition does not establish sandbox isolation, permission enforcement, or safe concurrent side effects. Compare [[sources/LLMCompiler]] for explicit dependency scheduling and [[sources/Atomix]] for transactional effects.

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Connections

- [[concepts/programmatic tool calling]]
- [[concepts/tool use]]
- [[systems/OpenHands]]
- [[sources/Cloudflare Code Mode MCP]]
- [[sources/Anthropic Code Execution with MCP]]

## Artifacts

- [[raw/papers/Executable Code Actions Elicit Better LLM Agents (CodeAct).pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2402.01030
- This paper predates the linked Cloudflare and Anthropic implementations and tests a related mechanism. Chronology and similarity do not establish that either implementation derives from this paper.
