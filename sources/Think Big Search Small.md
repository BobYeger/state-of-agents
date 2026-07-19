---
title: "Think Big, Search Small: Where Capacity Matters in Hierarchical Search Agents?"
aliases:
  - "Think Big Search Small"
  - "Role-aware capacity allocation"
source_type: "paper"
kind: "multi-agent-architecture"
status: "verified"
year: 2026
publication_date: "2026-07-08"
publication_date_basis: "arxiv_v1_submission_date"
arxiv_id: "2607.07548"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Qinnan Cai"
  - "Yibo Zhao"
  - "Xiang Li"
venue: "arXiv"
url: "https://arxiv.org/abs/2607.07548"
pdf_url: "https://arxiv.org/pdf/2607.07548"
artifacts:
  - "raw/papers/Think Big Search Small - Where Capacity Matters in Hierarchical Search Agents.pdf"
created: 2026-07-13
updated: 2026-07-13
---

# Think Big, Search Small

## Summary

- Factorizes hierarchical search into delegation, execution, and answer generation, then holds the answerer fixed while independently sweeping the model capacity assigned to the first two roles across 3,869 questions from five multi-hop QA benchmarks.
- Using the same model for both roles, the factored main/subagent architecture improves exact match over a single shared-context agent by 4.52–8.63 points across six model scales. Gains are smallest for the frontier model but remain positive.
- Capacity sensitivity is strongly asymmetric: scaling the delegator from 1.7B to frontier scale improves exact match by 11.3 points, while scaling the executor across the same range improves it by about 2.6. A correct executor cannot recover when the delegator decomposes the wrong relation or entity.
- A 1.7B executor trained through quality-filtered trajectory distillation matches or slightly exceeds a frontier executor under two different backbones while using 37% fewer subagent tokens. An off-the-shelf search model trained to plan and answer whole questions transfers poorly into the narrower executor role.
- Supports a role-aware routing rule for hierarchical search: spend capacity on decomposition, keep execution compact and task-specialized, and evaluate role training against the distribution of subtasks the delegator actually produces.

## Claims

- [[claims/Claim - Agent teams need explicit organization]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Connections

- [[methods/multi-agent orchestration]]
- [[methods/runtime routing]]
- [[concepts/subagent context isolation]]
- [[operations/cost control]]
- [[sources/Claude Advisor Tool]]
- [[sources/Multi-Agent Design - MASS]]
- [[sources/Stop Wasting Your Tokens]]

## Artifacts

- [[raw/papers/Think Big Search Small - Where Capacity Matters in Hierarchical Search Agents.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2607.07548
- Results are limited to English multi-hop QA over a fixed retrieval corpus. The paper does not establish that the same capacity asymmetry holds for open-web research, coding, computer use, multilingual work, or shared-state collaboration.
- The compact executor is supervised-fine-tuned on 2,168 filtered records from 1,591 training questions. The answerer is fixed to Qwen3-32B, and questions answerable without search are removed to reduce parametric-memory confounding.
