---
title: "Gorilla: Large Language Model Connected with Massive APIs"
aliases:
  - "Gorilla"
source_type: "paper"
kind: "retrieval-aware-tool-use"
status: "verified"
year: 2023
publication_date: "2023-05-24"
publication_date_basis: "arxiv_v1_submission_history"
source_updated_date: "2023-05-24"
source_updated_date_basis: "arxiv_v1"
arxiv_id: "2305.15334"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Shishir G. Patil"
  - "Tianjun Zhang"
  - "Xin Wang"
  - "Joseph E. Gonzalez"
venue: "arXiv"
url: "https://arxiv.org/abs/2305.15334"
pdf_url: "https://arxiv.org/pdf/2305.15334v1"
artifacts: []
created: 2026-10-05
updated: 2026-10-05
---

# Gorilla

## Summary

- Combines API-call fine-tuning with retrieved documentation; APIBench evaluates calls to HuggingFace, Torch Hub, and TensorFlow Hub APIs.
- Retrieval-aware training tests whether a model can follow changed documentation at inference time. Figure 6 demonstrates changed model backbones and registry locations.

## Evidence and Limits

- Tables 1–2 distinguish call accuracy, hallucination, training with retrieval, and the quality of the runtime retriever. Retrieval is not uniformly beneficial: weak retrieved context can perform worse than the model's no-retrieval baseline.
- APIBench focuses on ML APIs and evaluates generated calls using AST-based matching. This does not establish successful execution of arbitrary workflows, safe side effects, or permission enforcement.
- Documentation adaptation is different from updating a runtime's executable tool registry or pinning its version during replay.
- Read v1 for this note; use its versioned PDF when comparing results. [Project and releases](https://gorilla.cs.berkeley.edu/).

## Connections

- [[concepts/dynamic tool discovery]]
- [[concepts/tool-use contracts]]
- [[sources/Toolformer]]
- [[sources/AnyTool]]
- [[sources/ScaleMCP]]
- [[sources/Claude Mid-Conversation Tool Definitions]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
