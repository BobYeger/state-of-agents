---
title: "Introducing LangSmith Context Hub"
aliases:
  - "Context Hub"
  - "LangSmith Context Hub"
source_type: "article"
status: "verified"
year: 2026
publication_date: "2026-05-13"
publication_date_basis: "langchain_visible_published_date"
source_updated_date: null
source_updated_date_basis: null
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Harrison Chase"
venue: "LangChain Blog"
url: "https://www.langchain.com/blog/introducing-context-hub"
pdf_url: ""
artifacts:
  - "raw/articles/langsmith-context-hub.md"
created: 2026-05-20
updated: 2026-05-20
---

# LangSmith Context Hub

## Summary

- Product/architecture article arguing that agent context deserves a versioned, collaborative home separate from harness code.
- Important because it treats `AGENTS.md`, skills, policies, memories, and examples as versioned operational artifacts.
- Directly relevant to the vault design question: agent-readable context can live in a structured layer without overwhelming the human-facing graph.

## Claims

- [[claims/Claim - Agent memory and skills create compounding improvement loops]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Connections

- [[concepts/versioned context]]
- [[concepts/context engineering]]
- [[concepts/LLM-maintained knowledge bases]]
- [[operations/agent memory]]
- [[operations/agent harnesses]]

## Artifacts

- [[raw/articles/langsmith-context-hub.md]]

## Notes

- Canonical URL: https://www.langchain.com/blog/introducing-context-hub
- Included for the context-repository pattern, not for generic vendor implementation coverage.
