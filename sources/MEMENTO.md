---
title: "MEMENTO: Teaching LLMs to Manage Their Own Context"
aliases:
  - "MEMENTO"
source_type: "paper"
status: "verified"
year: 2026
publication_date: "2026-04-10"
publication_date_basis: "arxiv_published"
source_updated_date: "2026-04-10"
source_updated_date_basis: "arxiv_updated"
arxiv_id: "2604.09852"
citation_count: 0
citation_source: "OpenAlex"
citation_snapshot_date: "2026-05-26"
citation_lookup: "doi:10.48550/arxiv.2604.09852"
authors:
  - "Vasilis Kontonis"
  - "Yuchen Zeng"
  - "Shivam Garg"
  - "Lingjiao Chen"
  - "Hao Tang"
  - "Ziyan Wang"
  - "Ahmed Awadallah"
  - "Eric Horvitz"
  - "John Langford"
  - "Dimitris Papailiopoulos"
venue: "arXiv / Microsoft Research"
url: "https://arxiv.org/abs/2604.09852"
pdf_url: "https://arxiv.org/pdf/2604.09852"
artifacts:
  - "raw/papers/MEMENTO - Teaching LLMs to Manage Their Own Context.pdf"
created: 2026-05-26
updated: 2026-05-26
---

# MEMENTO

## Summary

- Microsoft Research paper on teaching reasoning models to segment reasoning into blocks and compress each block into a dense state summary called a memento.
- Important because it moves context management partly inside the model/inference method instead of relying only on an external harness compaction prompt.
- Connects context management, KV-cache reduction, throughput, and learned memory summaries.

## Claims

- [[claims/Claim - Context management is an agent architecture choice]]

## Connections

- [[concepts/context compaction]]
- [[concepts/context evolution]]
- [[concepts/scaling with computation]]
- [[operations/agent infrastructure]]
- [[maps/Context Management Map]]

## Artifacts

- [[raw/papers/MEMENTO - Teaching LLMs to Manage Their Own Context.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2604.09852
- PDF URL: https://arxiv.org/pdf/2604.09852
- Microsoft Research article URL: https://www.microsoft.com/en-us/research/articles/memento-teaching-llms-to-manage-their-own-context/
- Citation count is an OpenAlex snapshot, not a live count.
