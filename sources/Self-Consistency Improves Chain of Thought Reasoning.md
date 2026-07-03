---
title: "Self-Consistency Improves Chain of Thought Reasoning in Language Models"
aliases:
  - "self-consistency"
source_type: "paper"
kind: "voting-baseline"
status: "verified"
year: 2022
publication_date: "2022-03-21"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2203.11171"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Xuezhi Wang"
  - "Jason Wei"
  - "Dale Schuurmans"
  - "Quoc Le"
  - "Ed Chi"
  - "Sharan Narang"
  - "Aakanksha Chowdhery"
  - "Denny Zhou"
venue: "arXiv / ICLR 2023 (Google)"
url: "https://arxiv.org/abs/2203.11171"
pdf_url: "https://arxiv.org/pdf/2203.11171"
created: 2026-07-03
updated: 2026-07-03
---

# Self-Consistency Improves Chain of Thought Reasoning

## Summary

- The single-model baseline every multi-agent aggregation scheme must beat: sample a diverse set of reasoning paths at nonzero temperature, then marginalize out the paths by majority-voting over final answers.
- Gains over greedy chain-of-thought decoding: GSM8K +17.9%, SVAMP +11.0%, AQuA +12.2%, StrategyQA +6.4%, ARC-challenge +3.9%.
- Rationale: complex problems admit multiple distinct reasoning paths that converge on the same correct answer, so cross-path agreement is a correctness signal.
- Submitted 2022-03-21, final ICLR 2023 version 2023-03-07 — predates all multi-agent debate work and serves as the explicit control condition in Smit et al. and Zhang et al.

## Connections

- [[concepts/scaling with computation]]
- [[concepts/code factories]]
- [[sources/Should We Be Going MAD]]
- [[sources/Stop Overvaluing Multi-Agent Debate]]
- [[sources/More Agents Is All You Need]]

## Notes

- Canonical URL: https://arxiv.org/abs/2203.11171
- Both the origin of answer-voting in LLMs and the baseline that the debate-critique literature shows debate often fails to beat at matched compute.
- Directly applicable to code factories: voting over candidate patches or tests is self-consistency with an execution-grounded equivalence check.
