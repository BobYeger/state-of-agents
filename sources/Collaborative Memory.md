---
title: "Collaborative Memory: Multi-User Memory Sharing in LLM Agents with Dynamic Access Control"
aliases:
  - "Collaborative Memory"
source_type: "paper"
kind: "memory-access-control"
status: "verified"
year: 2025
publication_date: "2025-05-23"
publication_date_basis: "arxiv_v1_submission_date"
arxiv_id: "2505.18279"
authors:
  - "Alireza Rezazadeh"
  - "Zichao Li"
  - "Ange Lou"
  - "Yuying Zhao"
  - "Wei Wei"
  - "Yujia Bao"
venue: "arXiv / Accenture Center for Advanced AI"
url: "https://arxiv.org/abs/2505.18279"
pdf_url: "https://arxiv.org/pdf/2505.18279v1"
evidence_class: "author-run-framework-and-experiments"
metrics_status: "author-reported"
artifacts: []
created: 2026-10-05
updated: 2026-10-05
---

# Collaborative Memory

## Contribution

Private and shared memory tiers carry provenance and are filtered through changing user–agent–resource access graphs. Read and write policies are separate. This anticipates identity-scoped memory as an architectural concern.

## What Was Tested

Experiments include overlapping multi-user queries, asymmetric permissions, and evolving access. They compare sharing with isolation and include synthetic business scenarios. The formal policy guarantees assume the specified access graph and enforcement; they do not prove that LLM transformations remove every secret or that revoked information disappears from prior outputs.

## Reading

[Full text](https://arxiv.org/html/2505.18279v1), especially policy definitions and experimental appendices C–E.

## Connections

- [[concepts/shared agent memory]]
- [[operations/agent identity]]
- [[sources/LangChain Identity-Scoped Agent Memory]]
- [[sources/Governed Shared Memory for Multi-Agent LLM Systems]]
