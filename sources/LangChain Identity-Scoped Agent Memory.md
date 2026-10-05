---
title: "Managed Deep Agents v0.8: new auth, memory, and channels"
aliases: []
source_type: "article"
kind: "identity-scoped-memory-runtime"
status: "verified"
year: 2026
publication_date: "2026-09-24"
publication_date_basis: "visible_author_blog_date"
authors:
  - "Nathan Drezner"
  - "Karthic Subramanian"
venue: "LangChain blog"
url: "https://www.langchain.com/blog/langsmith-managed-deep-agents-whats-new"
evidence_class: "vendor-implementation-report"
artifacts: []
created: 2026-10-05
updated: 2026-10-05
---

# LangChain Identity-Scoped Agent Memory

Adds authenticated-user memory alongside shared deployment memory and user-owned credentials. Default personal-memory access is denied in Slack group/channel conversations and HTTP runs. This makes caller identity and communication surface part of memory policy.

The announcement documents mechanisms and defaults, not an adversarial isolation evaluation. Its customer testimonials are not controlled evidence. Compare the earlier [[sources/Collaborative Memory]] research for a model of provenance and changing access rights; no direct product influence is established.

## Connections

- [[concepts/shared agent memory]]
- [[operations/agent identity]]
- [[concepts/background agents]]
- [[maps/Agent Capability Research Lineage]]
