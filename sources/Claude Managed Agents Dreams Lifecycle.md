---
title: "Dreams — Claude Managed Agents lifecycle"
aliases:
  - "Claude Managed Agents Dreams Lifecycle"
source_type: "docs"
kind: "memory-consolidation-runtime"
status: "verified"
year: 2026
publication_date: null
publication_date_basis: "undated_living_documentation"
accessed: 2026-11-09
authors:
  - "Anthropic"
venue: "Claude Platform Docs"
url: "https://platform.claude.com/docs/en/managed-agents/dreams"
evidence_class: "documented-product-contract"
created: 2026-11-09
updated: 2026-11-09
---

# Claude Managed Agents Dreams Lifecycle

## Current Contract

A dream asynchronously processes one existing memory store and 1–100 session transcripts into a separate store, preserving the inputs. Documentation still labels access research preview on the review date.

An output ID can appear while the job is running. Failed or canceled jobs retain partial output; successful completion, review, and attachment to future sessions are distinct steps. Archiving the job leaves its output store intact. The underlying session transcript remains inspectable after termination.

Instructions steer synthesis; precise line edits belong in the Memory Stores API. Billing uses the chosen model's token rates, with recorded usage; moving work into the background does not remove its cost.

## Evidence Boundary

This documents lifecycle semantics, not demonstrated memory quality. It refreshes the operational detail behind [[sources/Anthropic Managed Agents Dreaming Outcomes]] and [[sources/Claude Managed Agents Memory Stores]], without implying those older snapshots are current API references.

## Reading

[Dreams documentation](https://platform.claude.com/docs/en/managed-agents/dreams).

## Connections

- [[concepts/dreaming and memory consolidation]]
- [[operations/agent memory]]
- [[reports/Memory and Dreaming Update - 2026-11-09]]
