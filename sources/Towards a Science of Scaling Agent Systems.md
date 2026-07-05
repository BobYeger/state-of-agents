---
title: "Towards a Science of Scaling Agent Systems"
aliases:
  - "Scaling Agent Systems (paper)"
source_type: "paper"
kind: "agent-scaling-study"
status: "verified"
year: 2025
publication_date: "2025-12-09"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2512.08296"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Yubin Kim"
  - "Ken Gu"
  - "Chanwoo Park"
  - "Samuel Schmidgall"
  - "Paul Pu Liang"
  - "Yilun Du"
  - "Shwetak Patel"
  - "Tim Althoff"
  - "Daniel McDuff"
  - "Xin Liu"
venue: "arXiv (Google Research / MIT)"
url: "https://arxiv.org/abs/2512.08296"
pdf_url: "https://arxiv.org/pdf/2512.08296"
artifacts:
  - "raw/papers/Towards a Science of Scaling Agent Systems.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# Towards a Science of Scaling Agent Systems

## Summary

- Defines five canonical agent architectures (Single, Independent, Centralized, Decentralized, Hybrid) and evaluates them across 3 LLM families (OpenAI, Google, Anthropic; 9 models); v3 (2026-04-08) covers 260 configurations across 6 benchmarks: BrowseComp-Plus, Finance Agent, PlanCraft, Workbench, SWE-bench Verified, Terminal-Bench.
- Topology-dependent error amplification: independent agents amplify trace-level errors 17.2x through unchecked propagation; centralized coordination contains amplification to 4.4x.
- Capability-saturation effect: coordination yields diminishing or negative returns once the single-agent baseline exceeds roughly 0.45 accuracy (v3: beta = -0.236, p = 0.004; v1 reported beta = -0.408, p < 0.001).
- A predictive model built from empirical coordination metrics (efficiency, overhead, error amplification, redundancy) achieves cross-validated R^2 = 0.373 (Intelligence Index spec) / 0.413 (task-grounded ACI spec) and selects the best architecture for 87% of held-out configurations, transferring to unseen frontier models.
- Relative performance vs single-agent baseline spans +80.8% (decomposable financial reasoning under centralized coordination) to -70.0% (sequential planning under independent coordination).
- Tool-coordination trade-off: tool-heavy tasks suffer disproportionately from multi-agent overhead — a direct coordination-cost consideration for harness designers.

## Claims

- [[claims/Claim - Coordination is a cost the task must justify]]
- [[claims/Claim - Agent systems improve when structure matches the task]]

## Connections

- [[concepts/multi-agent systems]]
- [[methods/multi-agent orchestration]]
- [[methods/topology optimization]]
- [[operations/cost control]]
- [[sources/Google Scaling Agent Systems]]
- [[sources/Do More Agents Help]]

## Artifacts

- [[raw/papers/Towards a Science of Scaling Agent Systems.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2512.08296
- This is the underlying arXiv paper behind the already-carded Google Research blog post ([[sources/Google Scaling Agent Systems]]); the paper carries the formulas, R^2 values, and architecture predictor the blog omits.
- Headline coefficients shifted between v1 (2025-12-09) and v3 (2026-04-08); cite the version explicitly when quoting the capability-saturation beta.
