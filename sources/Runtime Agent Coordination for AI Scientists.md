---
title: "Can AI Scientists Coordinate at Runtime?"
aliases: ["Runtime Agent Coordination", "RAC"]
tags: [multi-agent, research, evaluation]
source_type: "paper"
status: "verified"
year: 2026
publication_date: "2026-10-01"
publication_date_basis: "arxiv_v1_submission_date"
source_version: "arxiv_v1"
arxiv_id: "2610.00980"
authors: ["Zijian Liu", "Yangzhixin Luo", "Junyu Lu", "Yi Li", "Yu Chen", "David Xu", "William F. Shen", "Xinchi Qiu", "Xisen Wang"]
venue: "arXiv"
url: "https://arxiv.org/abs/2610.00980"
evidence_class: "exploratory-single-seed-experiments"
review_status: "full-text-methods-results-and-controls-reviewed"
created: 2026-11-09
updated: 2026-11-09
---

# Runtime Agent Coordination for AI Scientists

Adds communication, then state-dependent selection, then contracts plus verification to three existing research-agent hosts. Host models, tools, and permissions stay fixed; cross-run memory resets.

On ResearchClawBench, runtime selection has the highest mean for every host; adding contracts and verification reduces each mean. Verification supplies feedback without blocking transitions, rejecting artifacts, or rolling back work.

**Boundary:** one seed, ten tasks each for Agent Laboratory and EvoScientist, five for ARK. Matched ceilings do not mean equal realized spending. Contracts and verification are added together, so their separate causal effects are unknown. These results do not show verification is generally harmful.

Read [v1 §§3–5](https://arxiv.org/html/2610.00980v1).

## Connections

- [[reports/Multi-Agent Research Update - 2026-11-09]]
- [[methods/runtime routing]]
- [[methods/deliberative control]]
