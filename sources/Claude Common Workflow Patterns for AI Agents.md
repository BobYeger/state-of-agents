---
title: "Common workflow patterns for AI agents—and when to use them"
aliases:
  - "Claude Common Workflow Patterns"
  - "Common workflow patterns for AI agents"
  - "Common workflow patterns for AI agents and when to use them"
source_type: "article"
kind: "workflow-pattern-guide"
status: "verified"
year: 2026
publication_date: "2026-03-05"
publication_date_basis: "article_visible_date"
source_updated_date: null
source_updated_date_basis: null
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Anthropic"
venue: "Claude Blog"
url: "https://claude.com/blog/common-workflow-patterns-for-ai-agents-and-when-to-use-them"
pdf_url: ""
artifacts:
  - "raw/articles/claude-common-workflow-patterns-ai-agents.md"
created: 2026-06-17
updated: 2026-06-17
---

# Common workflow patterns for AI agents—and when to use them

## Summary

- Claude Blog guide for choosing between three production workflow patterns: sequential, parallel, and evaluator-optimizer.
- The core distinction is that workflows do not remove agent autonomy; they constrain where autonomy happens by defining flow, checkpoints, boundaries, and handoffs.
- Strong practical heuristic: try a single agent first, use sequential workflows for dependency chains, parallel workflows for independent subtasks and latency bottlenecks, and evaluator-optimizer loops only when quality gains are measurable.
- Important complement to [[sources/Anthropic Building Effective Agents]] because it narrows the broad workflow taxonomy into a deployer-facing decision guide.
- [[sources/Anthropic Building Effective AI Agents eBook]] repeats the same workflow-family decision in a broader enterprise architecture guide.

## Claims

- [[claims/Claim - Agent systems improve when structure matches the task]]
- [[claims/Claim - Coordination is a cost the task must justify]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Connections

- [[methods/multi-agent orchestration]]
- [[methods/deliberative control]]
- [[concepts/loop engineering]]
- [[concepts/outcomes and rubric graders]]
- [[maps/Harness Tracker]]
- [[maps/MAS Orchestration and Architecture]]
- [[reports/Harness Engineering Report]]

## Harness Reading

This is harness engineering because the workflow is the control surface around the agent: it sets the phase order, concurrency model, aggregation strategy, evaluator role, stopping criteria, fallback behavior, and cost/latency budget.

The article's strongest local contribution is pattern discipline. Parallelism and evaluator loops are not assumed improvements; they are justified only when the task structure, aggregation strategy, and measurement surface support them.

## Artifacts

- [[raw/articles/claude-common-workflow-patterns-ai-agents.md]]

## Notes

- Canonical URL: https://claude.com/blog/common-workflow-patterns-for-ai-agents-and-when-to-use-them
