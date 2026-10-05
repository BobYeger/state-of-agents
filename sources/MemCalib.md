---
title: "MemCalib: Benchmarking and Optimizing Memory Use in LLM Agents"
aliases:
  - "MemCalib"
  - "MemCalib-RL"
source_type: "paper"
kind: "memory-use-calibration-benchmark"
status: "verified"
year: 2026
publication_date: "2026-09-21"
publication_date_basis: "arxiv_v1_submission_history"
source_updated_date: "2026-09-22"
source_updated_date_basis: "arxiv_v2_submission_history"
source_version: "arXiv v2; full text inspected October 5, 2026"
arxiv_id: "2609.24259"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "not assessed"
authors:
  - "Ruike Cao"
  - "Fanyu Zhao"
  - "Fugen Yao"
  - "Liang Dong"
  - "Jian Xu"
  - "Guanjun Jiang"
  - "Yifei Zhao"
  - "Han Zhang"
  - "Li Xiao"
venue: "arXiv / USTC, Alibaba Qwen, Fudan"
url: "https://arxiv.org/abs/2609.24259"
pdf_url: "https://arxiv.org/pdf/2609.24259v2"
license: "arXiv non-exclusive distribution"
license_url: "https://arxiv.org/licenses/nonexclusive-distrib/1.0/"
evidence_class: "author-run-memory-calibration-benchmark-and-rl-preprint"
artifacts: []
created: 2026-10-05
updated: 2026-10-05
---

# MemCalib

## Summary

- Evaluates the influence of individual supplied memory propositions using three target levels: Ignore, Bound, and Control. Retrieving relevant material does not establish appropriate use.
- The constructed dataset has 15,000 examples, including 1,500 test examples. Metrics separate overuse, underuse, and exact calibration.
- MemCalib-RL updates model parameters using distinct directional error signals and counterfactual credit assignment. Reported experiments cover three model families/scales and external transfer; some conventional training methods improve one error direction while worsening the other.

## Evidence Boundary

Author-run preprint using constructed memory/query examples and an LLM judge, not a live storage-and-retrieval system. Human agreement is 96.7% on 150 naturally sampled response/atom pairs but 74.0% on 150 stress-stratified pairs; Bound/Control distinctions remain difficult. Counterfactual token attribution is approximate. Keep calibration, retrieval quality, and operational authorization separate.

## Connections

- [[concepts/memory use calibration]]
- [[concepts/harness-aware agent learning]]
- [[operations/agent memory]]
- [[sources/LongMemEval]]
- [[sources/MemOps]]
- [[sources/When Memory Becomes Authority]]

## Sources

- [Versioned full text](https://arxiv.org/html/2609.24259v2), sections 2–5 and appendix C.
- [Submission history](https://arxiv.org/abs/2609.24259).
- [Authors' code and data repository](https://github.com/Quark-Medical/memcalib).
- No public PDF copy: arXiv's distribution license does not grant general redistribution rights.
