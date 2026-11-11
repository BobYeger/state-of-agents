---
title: "MemCode: Discrete Semantic Representations for Long-Term Agent Memory"
aliases:
  - "MemCode"
source_type: "paper"
kind: "associative-memory-and-consolidation"
status: "verified"
year: 2026
publication_date: "2026-10-14"
publication_date_basis: "arxiv_v1_submission_date"
source_version: "arxiv_v1"
arxiv_id: "2610.19472"
authors:
  - "Xin Li"
  - "Liang Hu"
  - "Duoqian Miao"
  - "Ming Peng"
  - "Qi Zhang"
venue: "arXiv; NeurIPS 2026 acceptance stated by authors"
url: "https://arxiv.org/abs/2610.19472"
pdf_url: "https://arxiv.org/pdf/2610.19472v1"
evidence_class: "author-run-research-experiments"
metrics_status: "author-reported"
created: 2026-11-09
updated: 2026-11-09
---

# MemCode

## Mechanism and Evidence

Atomic conversational memories support dense retrieval plus a learned discrete-code association path. Offline consolidation gates sensitive clusters, archives superseded facts, and retains forwarding pointers and original-span provenance.

On LongMemEval-S with GPT-4o-mini, Table 1 reports 77.2% accuracy before consolidation and 78.4% after it; construction runtime rises from 74.05 to 82.98 seconds per dialogue. Temporal accuracy falls from 69.92% to 67.67% despite the aggregate gain. MemCode uses substantially more construction tokens than LightMem in this comparison despite lower measured runtime.

## Boundaries

Conversational retrieval experiments do not test a complete planning/tool-use agent. The learned codebook adds training requirements. Aggregate accuracy and wall-clock speed do not establish better temporal retention or lower total cost.

## Reading

[Full text, section 3.5, Table 1, Appendix A](https://arxiv.org/html/2610.19472v1); [metadata](https://arxiv.org/abs/2610.19472).

## Connections

- [[concepts/dreaming and memory consolidation]]
- [[operations/agent memory]]
- [[benchmarks/agent memory benchmarks]]
- [[reports/Memory and Dreaming Update - 2026-11-09]]
