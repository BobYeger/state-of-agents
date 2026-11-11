---
title: "Scaling Multi-Agent Intelligence with Substrate-Centric Coordination"
aliases: ["ScaleMAS"]
tags: [multi-agent, memory, coordination]
source_type: "paper"
status: "verified"
year: 2026
publication_date: "2026-10-12"
publication_date_basis: "arxiv_v1_submission_date"
source_version: "arxiv_v1"
arxiv_id: "2610.16120"
authors: ["Zhenting Qi", "Zhuokai Zhao", "Rulin Shao", "Kerem Oktar", "Zhiyuan Yao", "Himabindu Lakkaraju", "Wen-tau Yih", "Ansong Ni", "Bhargavi Paranjape", "Yilun Du"]
venue: "arXiv"
url: "https://arxiv.org/abs/2610.16120"
evidence_class: "author-run-controlled-experiments"
review_status: "full-text-methods-results-and-evaluation-appendix-reviewed"
created: 2026-11-09
updated: 2026-11-09
---

# ScaleMAS

Agents publish immutable linked messages and selectively search or visit them. Bounded retrieval replaces broadcasts; relevance and citation counts rank messages. Citation frequency is a quality proxy, not independent verification.

The 128-agent experiment covers FATE-M and synthetic Contradiction Audit with Qwen3.5-9B, not all four benchmarks. FATE largely plateaus after 16 agents. Third-party benchmark scores use pass@N, leaving final-answer selection unresolved; SWE-bench uses its first 100 test instances. Contradiction Audit does not penalize false positives. Private-store ablations separate personal memory from cross-agent sharing.

**Boundary:** author-run benchmark results; retrieval overhead, operational selection, and adversarial citation manipulation require separate evaluation.

Read [v1 §§2–3 and Appendix C.3](https://arxiv.org/html/2610.16120v1).

## Connections

- [[reports/Multi-Agent Research Update - 2026-11-09]]
- [[concepts/shared agent memory]]
- [[benchmarks/multi-agent benchmarks]]
