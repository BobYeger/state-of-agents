---
title: "Meta-Harness: End-to-End Optimization of Model Harnesses"
aliases:
  - "Meta-Harness"
source_type: "paper"
kind: "harness-optimization"
status: "verified"
year: 2026
publication_date: "2026-03-30"
publication_date_basis: "openalex_arxiv_publication_date"
source_updated_date: "2026-03-30"
source_updated_date_basis: "arxiv_v1_date"
arxiv_id: "2603.28052"
citation_count: 3
citation_source: "OpenAlex"
citation_snapshot_date: "2026-06-14"
citation_lookup: "doi:10.48550/arxiv.2603.28052"
authors:
  - "Yoonho Lee"
  - "Roshen Nair"
  - "Qizheng Zhang"
  - "Kangwook Lee"
  - "Omar Khattab"
  - "Chelsea Finn"
venue: "arXiv"
url: "https://arxiv.org/abs/2603.28052"
pdf_url: "https://arxiv.org/pdf/2603.28052"
artifacts:
  - "raw/papers/Meta-Harness - End-to-End Optimization of Model Harnesses.pdf"
created: 2026-06-14
updated: 2026-06-14
---

# Meta-Harness

## Summary

- Introduces automated search over model harness code: what information to store, retrieve, and present to a fixed base model.
- Important because it directly operationalizes [[operations/agent harnesses]] as an optimization target rather than a hand-designed wrapper.
- Uses an agentic proposer with access to candidate source code, scores, and execution traces through a filesystem.
- Reports gains on online text classification, retrieval-augmented math reasoning, and TerminalBench-2 agentic coding.

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[methods/self-improving code loops]]
- [[methods/agentic workflow search]]
- [[operations/agent harnesses]]
- [[concepts/loop engineering]]
- [[concepts/context engineering]]

## Artifacts

- [[raw/papers/Meta-Harness - End-to-End Optimization of Model Harnesses.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2603.28052
- Repository: https://github.com/stanford-iris-lab/meta-harness
- OpenAlex citation snapshot on 2026-06-14: 3 citations.
