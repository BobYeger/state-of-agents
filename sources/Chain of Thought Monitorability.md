---
title: "Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety"
aliases:
  - "CoT Monitorability"
source_type: "paper"
kind: "cot-monitoring"
status: "verified"
year: 2025
publication_date: "2025-07-15"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2507.11473"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Tomek Korbak"
  - "Mikita Balesni"
  - "Elizabeth Barnes"
  - "Yoshua Bengio"
venue: "arXiv (cross-lab position paper)"
url: "https://arxiv.org/abs/2507.11473"
pdf_url: "https://arxiv.org/pdf/2507.11473"
artifacts:
  - "raw/papers/Chain of Thought Monitorability - A New and Fragile Opportunity for AI Safety.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# Chain of Thought Monitorability

## Summary

- Cross-lab position paper (41 authors spanning OpenAI, Anthropic, Google DeepMind, METR, and academia; v1 2025-07-15, v2 2025-12-07) arguing that CoT monitoring is a usable but fragile safety layer.
- Core claim: models that "think" in natural language allow monitoring the CoT for intent to misbehave — but scaled-up RL, process supervision, and latent-reasoning architectures could silently erode this visibility.
- Recommends frontier developers treat monitorability as a first-class property: run standardized monitorability evaluations, report them (e.g., in system cards), and weigh monitorability impact when making training and architecture decisions.
- Positions CoT monitoring explicitly as complementary to, not a replacement for, other oversight layers — it "allows some misbehavior to go unnoticed."

## Connections

- [[operations/agent observability]]
- [[safety/agent safety and security]]
- [[methods/runtime supervision]]
- [[sources/Monitoring Reasoning Models for Misbehavior]]
- [[sources/METR Frontier Risk Report 2026]]

## Artifacts

- [[raw/papers/Chain of Thought Monitorability - A New and Fragile Opportunity for AI Safety.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2507.11473
- A consensus/position paper, not an empirical result — its evidence base is largely the Baker et al. obfuscation findings; cite those for the underlying experiments.
- The rare-signature aspect is the author list: rival labs co-signing a preservation requirement for trace legibility.
