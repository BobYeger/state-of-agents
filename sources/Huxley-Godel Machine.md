---
title: "Huxley-Godel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine"
aliases:
  - "HGM"
  - "Huxley-Gödel Machine"
source_type: "paper"
kind: "self-improving-coding-agent"
status: "verified"
year: 2025
publication_date: "2025-10-24"
publication_date_basis: "arxiv_abs_page"
source_updated_date: "2025-10-29"
source_updated_date_basis: "arxiv_v3_revision_date"
arxiv_id: "2510.21614"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Wenyi Wang"
  - "Piotr Piękos"
  - "Jürgen Schmidhuber"
venue: "arXiv / KAUST"
url: "https://arxiv.org/abs/2510.21614"
pdf_url: "https://arxiv.org/pdf/2510.21614"
created: 2026-07-03
updated: 2026-07-03
---

# Huxley-Godel Machine

## Summary

- Names the Metaproductivity-Performance Mismatch: an agent's own benchmark score is a poor signal for whether it is a good parent for further self-modification — a direct critique of the score-greedy selection policies in DGM and SICA.
- Selection policy expands the self-modification tree by estimated clade metaproductivity (CMP) — the aggregated benchmark performance of an agent's descendants — rather than the agent's own score.
- Compute efficiency: 2.38x fewer CPU-hours than DGM on SWE-Verified-60 (517 vs 1,231); 6.86x faster than DGM and 1.65x faster than SICA on Polyglot (347 vs 572 hours).
- Best discovered agent with GPT-5-mini scores 61.4% on SWE-bench Verified — the top result for that backbone; discovered agents lift Polyglot from 20.3% to 30.5%.
- Transfers across models and datasets: the agent optimized on SWE-Verified with GPT-5-mini reaches 49.0% on SWE-bench Lite when run with GPT-5, matching the best human-engineered coding agents.
- v1 2025-10-24, v3 2025-10-29.

## Connections

- [[methods/self-improving code loops]]
- [[operations/agent evals]]
- [[sources/Darwin Godel Machine]]
- [[sources/Red Queen Godel Machine]]
- [[sources/SICA Self-Improving Coding Agent]]
- [[sources/SWE-bench Verified]]

## Notes

- Canonical URL: https://arxiv.org/abs/2510.21614
- The core contribution is a selection signal, not a new agent design: which node to iterate from is treated as the bottleneck in self-improvement loops.
- SWE-Verified-60 and Polyglot comparisons use subsets; check the paper before quoting them as full-benchmark results.
