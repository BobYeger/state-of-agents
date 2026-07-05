---
title: "MemGPT: Towards LLMs as Operating Systems"
aliases:
  - "MemGPT"
  - "Virtual Context Management"
source_type: "paper"
kind: "virtual-context-management"
status: "verified"
year: 2023
publication_date: "2023-10-12"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2310.08560"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Charles Packer"
  - "Sarah Wooders"
  - "Kevin Lin"
  - "Vivian Fang"
  - "Shishir G. Patil"
  - "Ion Stoica"
  - "Joseph E. Gonzalez"
venue: "arXiv / UC Berkeley"
url: "https://arxiv.org/abs/2310.08560"
pdf_url: "https://arxiv.org/pdf/2310.08560"
artifacts:
  - "raw/papers/MemGPT - Towards LLMs as Operating Systems.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# MemGPT

## Summary

- Introduces "virtual context management": an OS-inspired memory hierarchy that pages information between the LLM's bounded main context and external context storage, by direct analogy to virtual memory paging.
- The LLM manages its own memory through function calls (self-directed memory edits and retrieval); interrupts manage control flow between system and user, completing the operating-system framing.
- Evaluated in two domains: document analysis over documents far exceeding the native context window, and multi-session chat agents that remember, reflect, and evolve across conversations.
- arXiv v1 2023-10-12, v2 2024-02-12; code and data released. The project evolved into Letta, whose documentation already has vault cards.

## Claims

- [[claims/Claim - Context management is an agent architecture choice]]

## Connections

- [[operations/agent memory]]
- [[concepts/context compaction]]
- [[concepts/context engineering]]
- [[sources/Letta Code Memory Docs]]
- [[sources/Letta Context-Bench]]

## Artifacts

- [[raw/papers/MemGPT - Towards LLMs as Operating Systems.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2310.08560
- Founding paper of the OS-style tiered/paging memory lineage; most later "memory hierarchy" agent designs cite it, and the Letta product line descends from it directly.
