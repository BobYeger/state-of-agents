---
title: "Rethinking Multi-Agent Collaboration: When More Is Less"
aliases: ["SAIGE", "Semantic-Aware Incremental Graph Evolution"]
tags: [multi-agent, context, orchestration]
source_type: "paper"
status: "verified"
year: 2026
publication_date: "2026-09-17"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: "2026-09-18"
source_updated_date_basis: "arxiv_v2_submission_date"
source_version: "arxiv_v2"
arxiv_id: "2609.19759"
authors: ["Yishuo Yuan", "Yibo Wu", "Yihan Zhang", "Minyuan Sun", "Shenliang Li", "Xinkai Ma", "Yifan Li", "Jiaheng Liu"]
venue: "arXiv"
url: "https://arxiv.org/abs/2609.19759"
evidence_class: "author-run-controlled-experiments"
review_status: "full-text-methods-results-and-ablations-reviewed"
created: 2026-11-09
updated: 2026-11-09
---

# SAIGE

Grows a task graph during execution and retrieves dependencies when needed. Its target is useful context separation without prematurely fixing all communication edges.

All compared systems use Codex CLI and DeepSeek-V4-Pro; default teams have at most four agents and one delegation level. SAIGE scores 71.80 versus single-agent 53.57 on AgentIF-OneDay, but 75.50 versus 76.71 on Terminal Bench 2.1. More agents or recursion do not consistently help. Input-token savings do not imply equal savings in output tokens or dollars.

**Boundary:** one backbone and four workloads; mathematical dependency assumptions are not a runtime guarantee of correct decomposition.

Read [v2 §§3–5 and Appendix B](https://arxiv.org/html/2609.19759v2).

## Connections

- [[reports/Multi-Agent Research Update - 2026-11-09]]
- [[methods/multi-agent orchestration]]
- [[concepts/subagent context isolation]]
