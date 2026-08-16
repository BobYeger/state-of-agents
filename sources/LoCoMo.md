---
title: "Evaluating Very Long-Term Conversational Memory of LLM Agents"
aliases:
  - "LoCoMo"
  - "LoCoMo benchmark"
source_type: "paper"
kind: "agent-memory-benchmark"
status: "verified"
year: 2024
publication_date: "2024-02-27"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: null
source_updated_date_basis: null
arxiv_id: "2402.17753"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Adyasha Maharana"
  - "Dong-Ho Lee"
  - "Sergey Tulyakov"
  - "Mohit Bansal"
  - "Francesco Barbieri"
  - "Yuwei Fang"
venue: "ACL 2024"
url: "https://aclanthology.org/2024.acl-long.747/"
pdf_url: "https://aclanthology.org/2024.acl-long.747.pdf"
license: "CC BY 4.0"
license_url: "https://creativecommons.org/licenses/by/4.0/"
created: 2026-08-16
updated: 2026-08-16
---

# LoCoMo

## Summary

- LoCoMo is the canonical conversational-memory benchmark behind many later memory-system comparisons. It evaluates question answering, event-graph summarization, and multimodal dialogue generation over months-long conversations grounded in personas and temporal event graphs.
- The current public `locomo10` release contains ten human-edited conversations, 5,882 dialogue turns, and 1,986 question-answer annotations. Conversations span 19–32 sessions. The final ACL paper describes roughly 600 turns and 16K tokens per conversation on average.
- Question answering separates single-hop, multi-hop, temporal, open-domain, and adversarial questions. Answers carry evidence turn IDs when available; the original evaluation reports partial-match F1, with retrieval accuracy used for RAG analyses, rather than one universal LLM-judge score.
- Event summarization tests causal and temporal structure with atomic-fact precision, recall, and F1. Multimodal dialogue generation is a separate generation task, not interchangeable with the QA subset used by most later memory papers.
- Long-context and RAG baselines improved QA in the original study but remained far below human performance, especially on temporal reasoning. Transforming dialogue into speaker-level observations was a strong RAG representation in that setup.

## Evidence Boundary

The conversations are machine-generated and then human-edited, not naturally occurring longitudinal user histories. The current ten-conversation release was sampled from the 50-conversation collection described in the first arXiv release; the final ACL paper itself reports the ten-conversation benchmark. Results must identify the release and task subset.

The arXiv v1 abstract and repository README retain earlier statistics of roughly 300 turns and 9K tokens, while the final ACL paper reports roughly 600 turns and 16K tokens. Downstream papers also use different QA subsets, readers, prompts, retrieval budgets, and judges. A bare “LoCoMo score” is therefore not comparable across systems.

## Claims

- [[claims/Claim - Context management is an agent architecture choice]]

## Connections

- [[benchmarks/agent memory benchmarks]]
- [[operations/agent memory]]
- [[maps/Context Management Map]]
- [[sources/LongMemEval]]
- [[sources/Mem0]]

## Notes

- Authoritative proceedings page: https://aclanthology.org/2024.acl-long.747/
- arXiv: https://arxiv.org/abs/2402.17753
- Project: https://snap-research.github.io/locomo/
- Code and current public data: https://github.com/snap-research/locomo
- The ACL paper is CC BY 4.0. The repository's code and data are separately licensed CC BY-NC 4.0; no dataset files are vendored here.
- Public-release counts above are computed from the repository's `data/locomo10.json`; they should be rechecked if the release changes.
