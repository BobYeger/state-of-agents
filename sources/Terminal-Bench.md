---
title: "Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces"
aliases:
  - "Terminal-Bench 2.0"
  - "T-Bench"
source_type: "paper"
kind: "benchmark"
status: "verified"
year: 2026
publication_date: "2026-01-17"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2601.11868"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Mike A. Merrill"
  - "Stanford x Laude Institute (85 authors)"
venue: "arXiv (Terminal-Bench 2.0 released 2025-11-07)"
url: "https://arxiv.org/abs/2601.11868"
pdf_url: "https://arxiv.org/pdf/2601.11868"
created: 2026-07-03
updated: 2026-07-03
---

# Terminal-Bench

## Summary

- Terminal-Bench 2.0 (released 2025-11-07): 89 human-verified terminal tasks across 16 categories and 3 difficulty tiers, each in a unique Docker container with a human-written oracle solution and tests verifying final container state; each task received several hours of human and LM-assisted validation.
- At launch, frontier models and agents scored under 65%; by 2026-05-14 the TB2.0 leaderboard top reached 84.7% (NexAU-AHE + GPT-5.5).
- Ships with Harbor (harborframework.com), an eval harness rewritten for agentic evals and RL rollouts: it parallelizes containerized rollouts horizontally across thousands of cloud containers and works with any agent installable in a container, regardless of framework.
- Harbor exposes rollout interfaces for RL and SFT training pipelines; the team used it internally to generate tens of thousands of rollouts during benchmark creation.
- Terminal-Bench 2.1 (2026-05-06) fixed 28 of 89 tasks (9 external-dependency breaks, 8 hardware-budget mismatches, 11 misspecifications) and introduced continuous validation for agentic benchmarks; the largest agent gain from fixes was +12.1% (Claude Code + Opus 4.6).
- TB2.1 leaderboard top is 79.1% (Codex CLI + GPT-5.3-Codex), with no task left unsolved by all agents — evidence that benchmark tasks decay and need ongoing maintenance, not one-time curation.

## Connections

- [[benchmarks/agent evaluation]]
- [[benchmarks/long-horizon benchmarks]]
- [[operations/agent evals]]
- [[operations/agent harnesses]]
- [[operations/sandboxes]]
- [[sources/TheAgentCompany]]

## Notes

- Canonical URL: https://arxiv.org/abs/2601.11868
- The task-decay findings (2.0 vs 2.1) mean scores across versions are not directly comparable; check which version a reported number uses.
- Citation count pending vault backfill.
