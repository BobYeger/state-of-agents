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
created: 2026-07-03
updated: 2026-07-03
---

# SWE-bench Pro

## Summary

- 1,865 human-verified problems from 41 actively maintained repositories, three-way split as an anti-overfitting design: public set (731 instances, 11 repos), commercial set (276 instances from 18 proprietary startup codebases under partnership agreements), and a held-out set from 12 repositories reserved for overfitting detection.
- Contamination-resistant by construction: public repos carry strong-copyleft (GPL) licensing as a legal deterrent to training-data inclusion, and the commercial codebases were never published.
- Tasks are enterprise-grade long-horizon problems taking professional engineers hours to days, often multi-file patches; all human-verified and augmented with context to ensure resolvability.
- At launch every frontier model scored below 25% Pass@1 (best: GPT-5 at 23.3%) versus 70%+ on SWE-bench Verified — quantifying how much Verified performance does not transfer to uncontaminated long-horizon tasks.
- v2 revision (2025-11-14) adds failure-mode clustering of agent attempts; as of February 2026 it is OpenAI's officially recommended successor to SWE-bench Verified.

## Connections

- [[benchmarks/agent evaluation]]
- [[benchmarks/long-horizon benchmarks]]
- [[sources/SWE-bench Verified]]
- [[sources/OpenAI Retires SWE-bench Verified]]
- [[sources/SWE-bench Illusion]]
- [[concepts/code factories]]

## Notes

- Canonical URL: https://arxiv.org/abs/2509.16941
- Public leaderboard: labs.scale.com/leaderboard/swe_bench_pro_public — the 23.3% GPT-5 figure is the launch-time public-set score, so check the leaderboard before quoting current numbers.
- Scale AI both sells data services and runs the leaderboard; the held-out and commercial splits are not independently auditable.
