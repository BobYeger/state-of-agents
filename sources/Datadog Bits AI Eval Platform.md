---
title: "How We Built a Real-World Evaluation Platform for Autonomous SRE Agents at Scale"
aliases:
  - "Bits AI eval platform"
source_type: "article"
kind: "agent-eval-platform"
status: "verified"
year: 2026
publication_date: "2026-04-07"
publication_date_basis: "vendor_blog_page"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Benjamin Barton"
venue: "Datadog Engineering Blog"
url: "https://www.datadoghq.com/blog/engineering/bits-ai-eval-platform/"
pdf_url: ""
created: 2026-07-03
updated: 2026-07-03
---

# Datadog Bits AI Eval Platform

## Summary

- Eval labels pair a ground-truth root cause with a "world snapshot" — archived signal queries available at the time of the original incident — so triage/investigation agents replay against realistic state rather than curated fixtures.
- Agentic validation pipeline: Bits itself aggregates feedback signals and derives causal chains to validate candidate labels; validation time per label dropped over 95% in one week, and label creation rate rose an order of magnitude.
- Weekly evaluations run Bits against tens of thousands of scenarios, segmented by technology, problem category, monitor type, and difficulty; scoring covers conclusion correctness plus trajectory, depth, and proximity.
- Noise is deliberately injected (tangentially-related components alongside root-cause signals); the realistic-noise dataset cut pass rate 11% and label count 35% versus the simplified version but predicted production performance better.
- The platform work is credited with a ~30% increase in root-cause quality, and it caught a regression where expanding service names into context degraded unrelated scenarios.

## Connections

- [[operations/agent evals]]
- [[benchmarks/agent evaluation]]
- [[concepts/code factories]]
- [[sources/AIOpsLab]]
- [[sources/Anthropic Demystifying Agent Evals]]

## Notes

- Canonical URL: https://www.datadoghq.com/blog/engineering/bits-ai-eval-platform/
- The replayable world-snapshot pattern, agent-assisted label validation, and noise-realism finding generalize to evaluating any investigation-style agent, not just SRE.
- Quality-improvement figures are Datadog-internal; no external benchmark comparison is published.
