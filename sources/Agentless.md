---
title: "Agentless: Demystifying LLM-based Software Engineering Agents"
aliases:
  - "Agentless"
source_type: "paper"
kind: "program-repair"
status: "verified"
year: 2024
publication_date: "2024-07-01"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2407.01489"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Chunqiu Steven Xia"
  - "Yinlin Deng"
  - "Soren Dunn"
  - "Lingming Zhang"
venue: "arXiv / FSE 2025 (UIUC)"
url: "https://arxiv.org/abs/2407.01489"
pdf_url: "https://arxiv.org/pdf/2407.01489"
artifacts:
  - "raw/papers/Agentless - Demystifying LLM-based Software Engineering Agents.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# Agentless

## Summary

- Scaffold-free counterargument to tool-using SWE agents: a fixed three-phase pipeline (hierarchical fault localization, repair, patch validation) with no autonomous action decisions and no complex tool operation.
- 32.00% solve rate (96 correct fixes) on SWE-bench Lite at $0.70 average cost per issue — outperforming all open-source agent scaffolds at time of publication.
- Constructed SWE-bench Lite-S by removing issues whose descriptions leak the exact ground-truth patch or are insufficient/misleading — an early benchmark-contamination critique.
- Core claim for harness designers: preventing the LLM from deciding next actions or operating complex tools can beat elaborate agent scaffolds on repair tasks.

## Claims

- [[claims/Claim - Agent systems improve when structure matches the task]] — a fixed pipeline shaped to the repair task outperformed general-purpose autonomous scaffolds on the same benchmark.

## Connections

- [[operations/agent harnesses]]
- [[concepts/code factories]]
- [[sources/SWE-bench]]
- [[sources/Passerine]]

## Artifacts

- [[raw/papers/Agentless - Demystifying LLM-based Software Engineering Agents.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2407.01489
- The result is from mid-2024 on SWE-bench Lite; later frontier agents surpassed it in absolute terms, but the pipeline-vs-agent design tension it names remains load-bearing.
- The SWE-bench Lite-S filtering is a useful caveat on any solve-rate comparison across scaffolds.
