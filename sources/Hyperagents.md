---
title: "Hyperagents"
aliases: []
source_type: "paper"
kind: "self-improving-agents"
status: "verified"
year: 2026
publication_date: "2026-03-19"
publication_date_basis: "openalex_arxiv_publication_date"
source_updated_date: "2026-03-19"
source_updated_date_basis: "arxiv_v1_date"
arxiv_id: "2603.19461"
citation_count: 0
citation_source: "OpenAlex"
citation_snapshot_date: "2026-06-14"
citation_lookup: "doi:10.48550/arxiv.2603.19461"
authors:
  - "Jenny Zhang"
  - "Bingchen Zhao"
  - "Wannan Yang"
  - "Jakob Foerster"
  - "Jeff Clune"
  - "Minqi Jiang"
  - "Sam Devlin"
  - "Tatiana Shavrina"
venue: "arXiv"
url: "https://arxiv.org/abs/2603.19461"
pdf_url: "https://arxiv.org/pdf/2603.19461"
artifacts:
  - "raw/papers/Hyperagents.pdf"
created: 2026-06-14
updated: 2026-06-14
---

# Hyperagents

## Summary

- Extends the self-improvement line beyond coding-only DGM by integrating a task agent and a meta agent into one editable program.
- Important because it targets metacognitive self-improvement: improving the process that improves future task behavior.
- The repository exposes separate `task_agent.py`, `meta_agent.py`, and `generate_loop.py` components, with explicit warning about executing untrusted model-generated code.

## Claims

- [[claims/Claim - Agent memory and skills create compounding improvement loops]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[methods/self-improving code loops]]
- [[methods/agentic workflow search]]
- [[concepts/loop engineering]]
- [[operations/sandboxes]]
- [[sources/Darwin Godel Machine]]

## Artifacts

- [[raw/papers/Hyperagents.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2603.19461
- Repository: https://github.com/facebookresearch/Hyperagents
- OpenAlex citation snapshot on 2026-06-14: 0 citations.
