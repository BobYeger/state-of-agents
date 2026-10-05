---
title: "Agent Lightning v1.0: Towards Harnessed Agentic RL"
aliases:
  - "Agent Lightning v1.0"
  - "Harnessed Agentic RL"
source_type: "paper"
kind: "harness-aware-agent-post-training"
status: "verified"
year: 2026
publication_date: "2026-08-18"
publication_date_basis: "arxiv_v1_submission_history"
source_updated_date: null
source_updated_date_basis: null
source_version: "arXiv v1; full text inspected October 5, 2026"
arxiv_id: "2608.17528"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "not assessed"
authors:
  - "Zhiyuan He"
  - "Siwei Zhang"
  - "Zhiwen Zhou"
  - "Yuqing Yang"
  - "Yu Kang"
  - "Yuge Zhang"
  - "Luna K. Qiu"
  - "Tin Yan Tsui"
  - "Jiahang Xu"
  - "Chong Luo"
venue: "arXiv / Microsoft, Fudan, Zhejiang, Edinburgh"
url: "https://arxiv.org/abs/2608.17528"
pdf_url: "https://arxiv.org/pdf/2608.17528v1"
license: "arXiv non-exclusive distribution"
license_url: "https://arxiv.org/licenses/nonexclusive-distrib/1.0/"
evidence_class: "author-run-agent-training-systems-preprint"
artifacts: []
created: 2026-10-05
updated: 2026-10-05
---

# Agent Lightning v1.0

## Summary

- Trains models through the deployment harness. The harness owns tools, context, and control flow; an endpoint proxy exposes model calls to the trainer.
- Compaction, subagents, and retokenization disrupt assumptions about one continuous training trajectory. The paper studies sample assembly, advantage assignment, loss normalization, and scheduling with variable sample counts.
- Rollout-level accounting avoids overweighting trajectories merely because they produce more samples. The reported Qwen3.5-9B coding experiment improves SWE-bench Verified from 41.8% to 56.4% using roughly 6,000 training examples.

## Evidence Boundary

Author-run preprint with search, instruction-following, and coding experiments. Results establish specific configurations, not universal compatibility or gains across arbitrary harnesses. Training needed safeguards against obtaining reference code through Git history and network access. These are parameter updates using an existing harness, not autonomous modification of that harness or proof of continual learning after deployment.

## Connections

- [[concepts/harness-aware agent learning]]
- [[operations/agent harnesses]]
- [[sources/SWE-RL]]
- [[sources/Meta-Harness]]
- [[sources/SCLATE]]
- [[safety/reward hacking]]

## Sources

- [Versioned full text](https://arxiv.org/html/2608.17528v1), sections 2–4.
- [Submission history](https://arxiv.org/abs/2608.17528).
- [Authors' repository](https://github.com/microsoft/agent-lightning).
- No public PDF copy: arXiv's distribution license does not grant general redistribution rights.
