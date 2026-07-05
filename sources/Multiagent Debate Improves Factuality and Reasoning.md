---
title: "Improving Factuality and Reasoning in Language Models through Multiagent Debate"
aliases:
  - "society of minds debate"
  - "Du et al. multiagent debate"
source_type: "paper"
kind: "multi-agent-debate"
status: "verified"
year: 2023
publication_date: "2023-05-23"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2305.14325"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Yilun Du"
  - "Shuang Li"
  - "Antonio Torralba"
  - "Joshua B. Tenenbaum"
  - "Igor Mordatch"
venue: "arXiv / ICML 2024 (MIT / Google Brain)"
url: "https://arxiv.org/abs/2305.14325"
pdf_url: "https://arxiv.org/pdf/2305.14325"
artifacts:
  - "raw/papers/Improving Factuality and Reasoning in Language Models through Multiagent Debate.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# Multiagent Debate Improves Factuality and Reasoning

## Summary

- Canonical "society of minds" pattern: multiple instances of the same LLM propose answers, read each other's responses, and revise over multiple rounds to converge on a common final answer.
- Default configuration is 3 agents debating for 2 rounds (chosen for computational cost); performance scales with both more agents and more rounds per the project page (composable-models.github.io/llm_debate).
- Evaluated on six tasks spanning arithmetic expressions, GSM8K, chess move optimality, MMLU, and biography factuality; the same procedure is applied across all tasks with no task-specific tuning.
- Works on black-box commercial models with no retraining, and is explicitly positioned as complementary to self-consistency and verification.
- Reports that debate "improves the factual validity of generated content, reducing fallacious answers and hallucinations."

## Connections

- [[methods/multi-agent orchestration]]
- [[methods/deliberative control]]
- [[concepts/multi-agent systems]]
- [[sources/Self-Consistency Improves Chain of Thought Reasoning]]
- [[sources/Stop Overvaluing Multi-Agent Debate]]
- [[sources/Should We Be Going MAD]]

## Artifacts

- [[raw/papers/Improving Factuality and Reasoning in Language Models through Multiagent Debate.pdf]]

## Notes

- Era note (2026-07-05): the 2023 "society of minds" origin paper; retained as lineage. Cost-matched evaluations found debate rarely beats self-consistency ([[sources/Should We Be Going MAD]], [[sources/Stop Overvaluing Multi-Agent Debate]]). Live guidance: [[methods/debate and aggregation]].
- Canonical URL: https://arxiv.org/abs/2305.14325
- Origin point of the LLM multi-agent debate literature; the 2024-2026 critique papers ([[sources/Should We Be Going MAD]], [[sources/Stop Overvaluing Multi-Agent Debate]]) argue against this paper's free-form consensus setup specifically.
- The headline gains predate compute-matched comparisons; later controlled evaluations find debate often fails to beat self-consistency at equal cost.
