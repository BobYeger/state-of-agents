---
title: "The components of agent memory"
aliases:
  - "Anthropic Components of Agent Memory"
source_type: "article"
kind: "memory-consolidation-evaluation"
status: "verified"
year: 2026
publication_date: "2026-11-06"
publication_date_basis: "visible_publication_date"
authors:
  - "Anthropic"
venue: "Anthropic Engineering"
url: "https://www.anthropic.com/research/components-of-agent-memory"
evidence_class: "vendor-run-experiments"
metrics_status: "vendor-reported"
created: 2026-11-09
updated: 2026-11-09
---

# Anthropic Components of Agent Memory

## Contribution and Evidence

Separates transcripts, notes, linked representations, and injected context. Dreaming can correct notes against transcripts and construct a wiki; these interventions do not update model weights.

On 25 questions over an internal corpus of approximately 420M tokens, Opus 5 wiki construction scales from 2 to 128 sessions. Search plus wiki reaches 61% of graded criteria, versus 53% for search alone; wiki alone reaches 48%. Figure 10 shows up to 128M dreaming tokens. Reported savings of about 20,000 answering tokens per question exclude that preparation cost.

The Pokémon correction is a case study. The small internal question set and vendor-run evaluation do not establish a general production effect or cost break-even.

## Reading

[Primary article, especially Figures 8–10](https://www.anthropic.com/research/components-of-agent-memory).

## Connections

- [[concepts/dreaming and memory consolidation]]
- [[concepts/LLM-maintained knowledge bases]]
- [[sources/Sleep-time Compute]]
- [[sources/Claude Managed Agents Dreams Lifecycle]]
- [[reports/Memory and Dreaming Update - 2026-11-09]]
