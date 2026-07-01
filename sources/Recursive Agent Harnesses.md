---
title: "Recursive Agent Harnesses"
aliases:
  - "RAH"
source_type: "paper"
kind: "multi-agent-orchestration"
status: "verified"
year: 2026
publication_date: "2026-06-11"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: null
source_updated_date_basis: null
arxiv_id: "2606.13643"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Elias Lumer"
  - "Sahil Sen"
  - "Kevin Paul"
  - "Vamse Kumar Subbiah"
venue: "arXiv"
url: "https://arxiv.org/abs/2606.13643"
pdf_url: "https://arxiv.org/pdf/2606.13643"
artifacts:
  - "raw/papers/Recursive Agent Harnesses.pdf"
created: 2026-07-01
updated: 2026-07-01
---

# Recursive Agent Harnesses

## Summary

- Names the pattern where the recursive unit is a full agent harness with tools, filesystem access, code execution, and planning, not merely a model call.
- A parent agent generates and runs executable scripts that spawn subagent harnesses in parallel for fine-grained workloads.
- Directly relevant to Claude Code Workflows: the execution plan lives in generated code that coordinates many subagents outside the main conversation context.
- Useful for explaining workflow scripts as real multi-agent architecture rather than "a prompt that asks for subagents."

## Claims

- [[claims/Claim - Agent teams need explicit organization]]
- [[claims/Claim - Agent systems improve when structure matches the task]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Connections

- [[sources/Claude Code Workflows]]
- [[methods/multi-agent orchestration]]
- [[maps/MAS Orchestration and Architecture]]
- [[maps/Harness Tracker]]
- [[concepts/subagent context isolation]]
- [[concepts/loop engineering]]

## Artifacts

- [[raw/papers/Recursive Agent Harnesses.pdf]]

## Notes

- Canonical arXiv URL: https://arxiv.org/abs/2606.13643
- arXiv metadata: submitted June 11, 2026.
