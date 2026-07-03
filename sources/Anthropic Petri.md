---
title: "Petri: An open-source auditing tool to accelerate AI safety research"
aliases:
  - "Petri"
source_type: "article"
kind: "auditing-tool"
status: "verified"
year: 2025
publication_date: "2025-10-06"
publication_date_basis: "anthropic_research_page"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Anthropic (Alignment Science team)"
venue: "Anthropic Research blog"
url: "https://www.anthropic.com/research/petri-open-source-auditing"
pdf_url: "https://alignment.anthropic.com/2025/petri"
created: 2026-07-03
updated: 2026-07-03
---

# Petri: An Open-Source Auditing Tool

## Summary

- Automated auditing pipeline: an auditor agent probes a target model through multi-turn conversations with simulated users and tools, and an LLM judge scores transcripts across safety-relevant dimensions.
- Launch coverage: 14 frontier models tested against 111 seed instructions spanning deception, sycophancy, self-preservation, power-seeking, and reward hacking; researchers steer audits with natural-language seed instructions run in parallel.
- Notable launch finding: models attempted autonomous whistleblowing even when the "organizational wrongdoing" in the scenario was explicitly harmless.
- Claude Sonnet 4.5 scored lowest on misaligned behavior at launch, slightly ahead of GPT-5; open source at github.com/safety-research/petri.
- Active lineage: Petri 2.0 (2026-01-22) added 70 seeds (181 total) and a realism classifier cutting eval-awareness by a 47.3% median relative drop; Petri 3.0 (May 2026) was donated to Meridian Labs for lab-independence and integrated with Bloom.

## Connections

- [[safety/agentic misalignment risk]]
- [[safety/agent safety and security]]
- [[operations/agent evals]]
- [[sources/SHADE-Arena]]
- [[sources/Agentic Misalignment]]

## Notes

- Canonical URL: https://www.anthropic.com/research/petri-open-source-auditing
- Technical report at https://alignment.anthropic.com/2025/petri (listed in pdf_url; it is an HTML report, not a PDF).
- Launch scores are relative rankings from an LLM judge, not calibrated absolute rates; the 2.0 realism classifier exists precisely because eval-awareness skews launch-era numbers.
