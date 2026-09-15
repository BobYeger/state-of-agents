---
title: "What Does an LLM-Agent Leaderboard Rank Actually Compare?"
aliases:
  - "What Does an LLM-Agent Leaderboard Rank Actually Compare"
source_type: "paper"
kind: "agent-evaluation-methodology"
status: "verified"
year: 2026
publication_date: "2026-09-07"
publication_date_basis: "arxiv_v1_submission_history"
source_updated_date: "2026-09-07"
source_updated_date_basis: "arxiv_v1_submission_history"
source_version: "arXiv v1; inspected September 15, 2026"
arxiv_id: "2609.07785"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "not assessed"
authors:
  - "Wei-Jung Huang"
venue: "IEEE DSAA 2026 (acceptance reported on arXiv)"
url: "https://arxiv.org/abs/2609.07785"
pdf_url: "https://arxiv.org/pdf/2609.07785v1"
evidence_class: "conference-accepted-public-log-reanalysis-and-statistical-method"
artifacts: []
created: 2026-09-15
updated: 2026-09-15
---

# What Does an LLM-Agent Leaderboard Rank Actually Compare?

## Summary

- Defines an estimand-aware pairwise procedure: state what quantity a comparison estimates, identify the evaluated configuration and label source, check shared task coverage, then apply an uncertainty rule and practical margin.
- Reanalyzes SWE-bench, AgentRewardBench, and tau2-bench; coarser DataAgentBench/Open Agent records illustrate conclusions that public data cannot support. This is a method for interpreting scores, not a technique that improves agent performance.
- Among 45 comparisons within the observed SWE-bench top ten, descriptive pointwise intervals with a two-percentage-point margin classified 39 as underpowered; simultaneous intervals resolved none. This result is conditional on those submissions, data, and decision rules.
- On AgentRewardBench, expert labels selected Claude 3.7 Sonnet while a GPT-4o-mini judge selected GPT-4o. On comparable tau2-bench runs, allowing four attempts increased success by 17.7–20.4 points; cost-aware rules could change the selected system.

## Comparison Contract

The paper makes six fields explicit before a ranking is interpreted:

1. **Configuration:** model, harness, tools, prompts, stopping policy, and resources.
2. **Target:** observed benchmark mix or a stated deployment-relevant population.
3. **Labels:** execution tests, experts, or a specified automatic grader.
4. **Coverage:** which task groups have results for every compared configuration.
5. **Uncertainty:** sampling unit and interval, including repeated or clustered observations.
6. **Decision:** meaningful gap and whether the claim names one pair or an entire family of comparisons.

The practical addition to [[sources/Adding Error Bars to Evals]] is that a precise estimate of the wrong population or label source does not answer the desired comparison. Shared coverage and a declared target come before significance testing.

## Connections

- [[sources/AI Agents That Matter]]
- [[sources/Holistic Agent Leaderboard]]
- [[sources/Adding Error Bars to Evals]]
- [[sources/On Randomness in Agentic Evals]]
- [[sources/Tau-Bench]]
- [[concepts/evaluator reliability]]
- [[benchmarks/agent evaluation]]
- [[operations/agent evals]]
- [[operations/cost control]]

## Evidence Limits

- Public releases determine what is identifiable. The analysis does not establish causal effects of changing models, harnesses, repositories, or graders.
- Equal-repository weighting and a two-point margin are stated analysis choices, not universally correct deployment policies. A named-pair interval and a leaderboard-wide winner claim require different treatment of multiple comparisons.
- “Unresolved” means insufficient support for the specified superiority claim; it does not prove the systems are equivalent.
- Acceptance is reported in the arXiv record. Broad adoption, citation influence, and independent reproduction were not established in this review.
- [Versioned full text](https://arxiv.org/html/2609.07785v1); [submission history](https://arxiv.org/abs/2609.07785).
