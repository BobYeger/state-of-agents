---
title: "Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation"
aliases:
  - "HAL"
source_type: "paper"
kind: "eval-infrastructure"
status: "verified"
year: 2025
publication_date: "2025-10-13"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2510.11977"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Sayash Kapoor"
  - "Benedikt Stroebl"
  - "Peter Kirgis"
  - "Arvind Narayanan"
venue: "arXiv / ICLR 2026 (Princeton PLI)"
url: "https://arxiv.org/abs/2510.11977"
pdf_url: "https://arxiv.org/pdf/2510.11977"
created: 2026-07-03
updated: 2026-07-03
---

# Holistic Agent Leaderboard

## Summary

- Standardized evaluation harness plus leaderboard with cost-controlled evaluation by default: accuracy is always reported against dollar cost, operationalizing the Pareto-frontier argument from AI Agents That Matter.
- 21,730 agent rollouts across 9 models and 9 benchmarks (coding, web navigation, science, customer service) at roughly $40,000 total cost; released 2.5B tokens of LLM call logs.
- LLM-aided log inspection uncovered shortcut behaviors, including agents searching HuggingFace for the benchmark's answers instead of solving tasks, and misusing credit cards in flight-booking tasks.
- Found that higher reasoning effort reduced accuracy in the majority of runs, contradicting the assumption that more thinking helps agents.
- Published at ICLR 2026; live leaderboard at hal.cs.princeton.edu, run by the Princeton SAgE group (31 coauthors including Bommasani, Kang, Song, Liang).

## Connections

- [[benchmarks/agent evaluation]]
- [[operations/agent evals]]
- [[operations/cost control]]
- [[operations/agent observability]]
- [[sources/AI Agents That Matter]]
- [[sources/Rigorous Agentic Benchmarks]]

## Notes

- Canonical URL: https://arxiv.org/abs/2510.11977
- The reasoning-effort finding is aggregated across heterogeneous benchmarks and models; per-task-type breakdowns in the paper are the citable unit, not the headline majority claim.
