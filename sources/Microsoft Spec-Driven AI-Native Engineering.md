---
title: "Spec-Driven Development: A Spec-First Approach to AI-Native Engineering"
aliases:
  - "Microsoft Spec-Driven Development"
  - "Spec-first AI-native engineering"
  - "GitHub Spec Kit AI-native engineering"
source_type: "article"
kind: "methodology"
status: "verified"
year: 2026
publication_date: "2026-06-10"
publication_date_basis: "visible_page_date"
source_updated_date: "2026-07-01"
source_updated_date_basis: "snapshot_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Apoorv Gupta"
venue: "Microsoft for Developers"
url: "https://developer.microsoft.com/blog/spec-driven-development-ai-native-engineering"
pdf_url: ""
artifacts:
  - "raw/articles/microsoft-spec-driven-ai-native-engineering.md"
created: 2026-07-01
updated: 2026-07-01
---

# Spec-Driven Development: A Spec-First Approach to AI-Native Engineering

## Summary

- Microsoft argues that prompt-first workflows break down as AI-native work grows because intent, constraints, and edge cases need a durable source of truth.
- Spec-Driven Development makes structured specs the shared artifact that links requirements, architecture, implementation, tests, and validation.
- The GitHub Spec Kit lifecycle is: Constitution, Specify, Clarify, Plan, Tasks, Implement, Validate.
- This source matters for [[concepts/code factories]] because a factory needs machine-readable intent and acceptance criteria, not just faster code generation.
- Practical lesson: spec quality becomes output quality when AI-generated implementation is downstream of the spec.

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
- [[claims/Claim - Context management is an agent architecture choice]]

## Connections

- [[concepts/code factories]]
- [[concepts/versioned context]]
- [[operations/agent harnesses]]
- [[operations/agent evals]]
- [[operations/permissions]]
- [[sources/Microsoft Agentic Platform Agent Factory]]
- [[sources/OpenAI Codex Using Goals]]

## Artifacts

- [[raw/articles/microsoft-spec-driven-ai-native-engineering.md]]

## Notes

- Canonical URL: https://developer.microsoft.com/blog/spec-driven-development-ai-native-engineering
- The article is a methodology source rather than a loop/factory source, but it supplies the durable-intent layer that factory-style coding loops need.
