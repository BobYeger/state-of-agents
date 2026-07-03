---
title: "Context Engineering for AI Agents: Lessons from Building Manus"
aliases:
  - "Manus Context Engineering"
  - "Stochastic Graduate Descent"
source_type: "article"
kind: "context-engineering"
status: "verified"
year: 2025
publication_date: "2025-07-18"
publication_date_basis: "vendor_blog_page"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Yichao 'Peak' Ji"
venue: "Manus blog"
url: "https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus"
pdf_url: ""
created: 2026-07-03
updated: 2026-07-03
---

# Manus Context Engineering

## Summary

- Declares KV-cache hit rate "the single most important metric for a production-stage AI agent": Manus averages a ~100:1 input-to-output token ratio, a typical task takes ~50 tool calls, and cached input costs $0.30/MTok versus $3.00/MTok uncached on Claude Sonnet — a 10x difference.
- Manages tool availability by masking token logits through a context-aware state machine rather than adding or removing tool definitions mid-loop, which would invalidate the KV cache.
- Uses the file system as "the ultimate context" with restorable compression: page content can be dropped as long as the URL is kept, so truncation never causes irreversible information loss.
- Maintains a continuously rewritten todo.md that recites the global plan into recent attention, countering mid-context "lost in the middle" drift.
- Core fault-tolerance claim: "leave the wrong turns in the context" — erasing failure evidence removes the model's ability to update its beliefs, and error recovery is called a core indicator of true agentic behavior.
- The team rebuilt its agent framework four times, naming the manual architecture-search process "Stochastic Graduate Descent".

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
- [[claims/Claim - Context management is an agent architecture choice]]

## Connections

- [[concepts/context engineering]]
- [[concepts/loop engineering]]
- [[operations/agent harnesses]]
- [[operations/cost control]]
- [[sources/Manus Sandbox]]
- [[sources/Anthropic Effective Context Engineering]]

## Notes

- Canonical URL: https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus
- Single-team practitioner essay, not a controlled study; the cost figures reflect mid-2025 Claude Sonnet pricing and may drift.
