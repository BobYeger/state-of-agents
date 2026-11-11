---
title: "Building agents: When to fold subagents into your main agent loop"
aliases: []
tags: [multi-agent, skills, harness]
source_type: "article"
status: "verified"
year: 2026
publication_date: "2026-10-22"
publication_date_basis: "visible_published_date"
authors: ["Diane Sarkis"]
venue: "Claude by Anthropic"
url: "https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop"
evidence_class: "vendor-practice-report"
review_status: "full-article-reviewed"
created: 2026-11-09
updated: 2026-11-09
---

# Anthropic Folding Subagents into the Main Loop

Moves tightly coupled domain agents into one loop with progressively loaded skills and tools. Retains subagents for measurable context problems, independent parallel work, and useful tool or instruction separation.

The migration procedure compares one change at a time on end-to-end tasks, inspects which cases regress, and repeats stochastic runs. An example reduces latency while bypassing a required shipping-specialist step, demonstrating why aggregate quality is insufficient.

**Boundary:** practitioner guidance and selected customer observations; no complete comparative dataset or general effect estimate. Organizational ownership can move to skills without requiring one autonomous agent per team.

Primary text: [October 22 article](https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop).

## Connections

- [[reports/Multi-Agent Research Update - 2026-11-09]]
- [[maps/MAS Orchestration and Architecture]]
- [[maps/Agent Skills Map]]
