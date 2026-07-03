---
title: "Introducing Agent Readiness"
aliases:
  - "Agent Readiness"
  - "Factory readiness report"
source_type: "article"
kind: "agent-readiness-framework"
status: "verified"
year: 2026
publication_date: "2026-01-20"
publication_date_basis: "vendor_blog_page"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Factory.ai"
venue: "Factory.ai blog"
url: "https://factory.ai/news/agent-readiness"
pdf_url: ""
created: 2026-07-03
updated: 2026-07-03
---

# Introducing Agent Readiness

## Summary

- Framework scoring how well a repository supports autonomous development: 8 technical pillars (Style & Validation, Build System, Testing, Documentation, Dev Environment, Code Quality, Observability, Security & Governance) crossed with 5 maturity levels (Functional, Documented, Standardized, Optimized, Autonomous).
- Progression gate: a repo must pass 80% of criteria at a level plus all previous levels to advance. Run via /readiness-report in Droid; criteria are applied at repository level and per-app in monorepos.
- Level 3 "Standardized" is the recommended target and defined as "production-ready for agents": agents handle routine maintenance (bug fixes, tests, docs, dependency upgrades). Level 5 means full autonomous development.
- Evaluation variance dropped from 7% average to 0.6% across benchmark repos after grounding improvements; example public score: CockroachDB 74% (Level 4).
- Recommended organizational metric is the percentage of active repos reaching Level 3+, not average scores; public per-repo reports exist (e.g. factory.ai/agent-readiness/expressjs_express).
- Inverts the usual graduated-autonomy question: it grades the readiness of the environment for agents rather than the trustworthiness of the agent.

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Connections

- [[concepts/code factories]]
- [[operations/agent harnesses]]
- [[sources/Factory 2.0 Software Factory]]
- [[sources/Factory Context Compression Evaluation]]

## Notes

- Canonical URL: https://factory.ai/news/agent-readiness
- Vendor framework tied to the Droid product; the 80% gate and level definitions are Factory's own choices, not an industry standard.
- Variance figures (7% to 0.6%) are Factory's self-reported numbers on their own benchmark repos.
