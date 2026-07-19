---
title: "SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?"
aliases:
  - "SWE-Bench Pro"
source_type: "paper"
kind: "benchmark"
status: "verified"
year: 2025
publication_date: "2025-09-21"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2509.16941"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Xiang Deng"
venue: "arXiv / Scale AI"
url: "https://arxiv.org/abs/2509.16941"
pdf_url: "https://arxiv.org/pdf/2509.16941"
artifacts:
  - "raw/papers/SWE-Bench Pro - Can AI Agents Solve Long-Horizon Software Engineering Tasks.pdf"
created: 2026-07-03
updated: 2026-07-13
---

# SWE-bench Pro

## Summary

- 1,865 human-verified problems from 41 actively maintained repositories, three-way split as an anti-overfitting design: public set (731 instances, 11 repos), commercial set (276 instances from 18 proprietary startup codebases under partnership agreements), and a held-out set from 12 repositories reserved for overfitting detection.
- Contamination-resistant by construction: public repos carry strong-copyleft (GPL) licensing as a legal deterrent to training-data inclusion, and the commercial codebases were never published.
- Tasks are enterprise-grade long-horizon problems taking professional engineers hours to days, often multi-file patches; all human-verified and augmented with context to ensure resolvability.
- At launch every frontier model scored below 25% Pass@1 (best: GPT-5 at 23.3%) versus 70%+ on SWE-bench Verified — quantifying how much Verified performance does not transfer to uncontaminated long-horizon tasks.
- v2 revision (2025-11-14) adds failure-mode clustering of agent attempts. OpenAI recommended it as the successor to SWE-bench Verified in February 2026, then retracted that recommendation on 2026-07-08 after an audit found breaking issues in roughly one-third of the 731-task public split.

## Connections

- [[benchmarks/agent evaluation]]
- [[benchmarks/long-horizon benchmarks]]
- [[sources/SWE-bench Verified]]
- [[sources/OpenAI Retires SWE-bench Verified]]
- [[sources/SWE-bench Illusion]]
- [[sources/OpenAI SWE-bench Pro Audit]]
- [[sources/DeepSWE]]
- [[concepts/code factories]]

## Artifacts

- [[raw/papers/SWE-Bench Pro - Can AI Agents Solve Long-Horizon Software Engineering Tasks.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2509.16941
- Public leaderboard: labs.scale.com/leaderboard/swe_bench_pro_public — the 23.3% GPT-5 figure is the launch-time public-set score, so check the leaderboard before quoting current numbers.
- Scale AI both sells data services and runs the leaderboard; the held-out and commercial splits are not independently auditable.
- Current validity warning: [[sources/OpenAI SWE-bench Pro Audit]] reports 249 of 731 public tasks (34.1%) were judged broken by a five-engineer review. Historical scores remain evidence about a model+harness under that benchmark version, but should not be treated as clean estimates of coding capability.
