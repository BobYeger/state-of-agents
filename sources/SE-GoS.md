---
title: "SE-GoS: Self-Evolving Graph-of-Skills for Skill Library at Scale"
aliases:
  - "SE-GoS"
source_type: "paper"
kind: "skill-retrieval-evolution"
status: "verified"
year: 2026
publication_date: "2026-09-08"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: "2026-09-08"
source_updated_date_basis: "arxiv_v1_submission_date"
source_version: "arxiv_v1"
arxiv_id: "2609.08228"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Dawei Fu"
  - "Cheng Jiang"
  - "Sitian Qian"
  - "Huainan Wang"
  - "Zhongkai Hao"
venue: "arXiv"
url: "https://arxiv.org/abs/2609.08228"
pdf_url: "https://arxiv.org/pdf/2609.08228"
created: 2026-09-15
updated: 2026-09-15
---

# SE-GoS

## Contribution

Execution traces update a skill graph's edges, weights, and retrieval descriptions while skill bodies and retrieval code remain fixed.

## Evidence and Limits

On 87 SkillsBench tasks with two attempts each and a 1,000-skill library, the representative DeepSeek row rises from static GoS's 52.4% to 59.4%. This remeasures tasks used for evolution. A separate 50/37 train/test split rises from 52.9% to 58.3% on held-out tasks, within the paper's estimated noise band.

Repeated evolution yields 59.4%, 59.8%, then 54.0%, alongside graph growth. Cross-model rows include imported baselines; broader scale and convergence remain untested. This is bounded evidence for graph adaptation and a stopping rule, not sustained compounding improvement.

## Connections

- [[maps/Agent Skills Map]]
- [[maps/Self-Improving Systems Map]]
- [[concepts/procedural memory]]
- [[sources/SkillAdam]]
- [[sources/Adaptive Auto-Harness]]

## Primary Links

- [Paper and submission history](https://arxiv.org/abs/2609.08228)
- [Full text, v1](https://arxiv.org/html/2609.08228v1)
