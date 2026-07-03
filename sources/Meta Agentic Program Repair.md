---
title: "Agentic Program Repair from Test Failures at Scale: A Neuro-symbolic Approach with Static Analysis and Test Execution Feedback"
aliases:
  - "Meta Engineering Agent"
source_type: "paper"
kind: "ci-repair"
status: "verified"
year: 2025
publication_date: "2025-07-24"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2507.18755"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Chandra Maddila"
venue: "arXiv (Meta Platforms)"
url: "https://arxiv.org/abs/2507.18755"
pdf_url: "https://arxiv.org/pdf/2507.18755"
created: 2026-07-03
updated: 2026-07-03
---

# Meta Agentic Program Repair

## Summary

- Production CI-failure repair: the agent fixes failing tests across two Meta monorepos spanning 15 programming languages.
- ReAct harness on Llama with 15 actions (file reading through patch generation), iterating on static-analysis signals and test execution traces; offline solve rate 42.3% at an average of 11.8 feedback iterations.
- Three-month production trial (2025-02-01 to 2025-04-30): 1,589 diffs published, 80% received engineer review, 405 landed — 25.5% of published and 31.5% of reviewed diffs accepted.
- An LLM-as-a-Judge gate validates patches against human-review standards before they reach engineers.
- A fine-tuned Llama 70B was "highly competitive with the much larger but vanilla Llama-405B" — specialization beat scale for this repair task.

## Claims

- [[claims/Claim - Runtime control and verification improve agent reliability]] — static-analysis and test-execution feedback loops plus an LLM-as-judge gate are what let agent-authored diffs enter a production review pipeline at all.

## Connections

- [[concepts/code factories]]
- [[concepts/loop engineering]]
- [[sources/TestGen-LLM]]
- [[sources/Passerine]]

## Notes

- Canonical URL: https://arxiv.org/abs/2507.18755
- Paper lists Chandra Maddila plus 23 co-authors; largest published production deployment of an agentic test-failure fixer to date, with real acceptance-rate telemetry.
- Acceptance rates (25.5% of published diffs landing) set a sober baseline for CI-repair throughput expectations.
