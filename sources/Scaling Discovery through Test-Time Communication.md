---
title: "Scaling Discovery through Test-Time Communication"
aliases: []
tags: [multi-agent, research, verification]
source_type: "paper"
status: "verified"
year: 2026
publication_date: "2026-09-17"
publication_date_basis: "arxiv_v1_submission_date"
source_version: "arxiv_v1"
arxiv_id: "2609.21032"
authors: ["Jongho Park", "Vasilis Kontonis", "Shivam Garg", "Akshay Krishnamurthy", "Dimitris Papailiopoulos"]
venue: "arXiv"
url: "https://arxiv.org/abs/2609.21032"
evidence_class: "author-run-controlled-experiments"
review_status: "full-text-methods-results-and-accounting-reviewed"
created: 2026-11-09
updated: 2026-11-09
---

# Scaling Discovery through Test-Time Communication

Identical agents share measured intermediate discoveries through logs and artifacts, with atomic ownership and serialized artifact writes. The mechanism is cumulative reuse, beyond independent parallel attempts.

On 25 public ARC-AGI-3 games with Sonnet 4.6, five communicating agents achieve 8.0% full-game success versus 2.2% for best-of-five independent attempts. There are 64 solo trials per game and 20 trials per team size. Per-agent action budgets match; total inference spending need not. Terminal-Bench 2.0 communication fails to beat independent pass@2.

**Boundary:** author-run experiments, task-specific verifiers, small teams, and finite solo pools. This does not establish a universal scaling law or production research productivity.

Read [v1 §§2–3 and Appendix A](https://arxiv.org/html/2609.21032v1) for protocol and accounting.

## Connections

- [[reports/Multi-Agent Research Update - 2026-11-09]]
- [[methods/multi-agent orchestration]]
- [[concepts/shared agent memory]]
