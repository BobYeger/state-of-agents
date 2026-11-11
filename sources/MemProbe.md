---
title: "Probing Stability–Plasticity Tradeoffs in Agent Memory through Cognitive Experimental Paradigms"
aliases:
  - "MemProbe"
source_type: "paper"
kind: "memory-maintenance-diagnostics"
status: "verified"
year: 2026
publication_date: "2026-10"
publication_date_basis: "acl_proceedings_month; exact_day_unreported"
source_version: "emnlp_2026_proceedings"
authors:
  - "Jiaqi Ding"
  - "Guorong Wu"
venue: "EMNLP 2026"
url: "https://aclanthology.org/2026.emnlp-main.2473/"
pdf_url: "https://aclanthology.org/2026.emnlp-main.2473.pdf"
evidence_class: "author-run-controlled-diagnostic-evaluation"
metrics_status: "author-reported"
created: 2026-11-09
updated: 2026-11-09
---

# MemProbe

## Contribution and Evidence

Tests interference, misleading evidence, consolidation strength, and reactivation timing through 56 controlled episodes. Six incremental memory systems share a Gemini-3-Flash reader; probes distinguish current values, prior values, source attribution, conflicts, and timing.

Similar aggregate accuracy hides different maintenance behavior. Graphiti preserves previous values better than LangMem (96.4% versus 67.9%), while their current-value comparison reverses direction (66.1% versus 80.4%). A second 40-episode suite tests the construction protocol with new fact types and another reader.

## Boundaries

The controlled, LLM-assisted English text suite is a diagnostic instrument, not a broad production ranking. Reader sensitivity and source-attribution failures remain important. Use its interventions to evaluate whether consolidation preserves justified uncertainty and history.

## Reading

[Proceedings metadata](https://aclanthology.org/2026.emnlp-main.2473/); [full paper, section 5.2 and Appendices A/F/G](https://aclanthology.org/2026.emnlp-main.2473.pdf).

## Connections

- [[concepts/dreaming and memory consolidation]]
- [[concepts/memory use calibration]]
- [[benchmarks/agent memory benchmarks]]
- [[reports/Memory and Dreaming Update - 2026-11-09]]
