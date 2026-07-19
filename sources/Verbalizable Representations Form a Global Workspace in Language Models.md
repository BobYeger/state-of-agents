---
title: "Verbalizable Representations Form a Global Workspace in Language Models"
aliases:
  - "J-space"
  - "Jacobian lens"
  - "Anthropic Global Workspace"
source_type: "paper"
kind: "interpretability"
status: "verified"
year: 2026
publication_date: "2026-07-06"
publication_date_basis: "transformer_circuits_visible_published_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Wes Gurnee"
  - "Nicholas Sofroniew"
  - "Adam Pearce"
  - "Mateusz Piotrowski"
  - "Isaac Kauvar"
  - "Runjin Chen"
  - "Anna Soligo"
  - "Paul Bogdan"
  - "Euan Ong"
  - "Rowan Wang"
  - "T. Ben Thompson"
  - "David Abrahams"
  - "Subhash Kantamneni"
  - "Emmanuel Ameisen"
  - "Joshua Batson"
  - "Jack Lindsey"
venue: "Transformer Circuits Thread / Anthropic"
url: "https://transformer-circuits.pub/2026/workspace/index.html"
pdf_url: ""
artifacts:
  - "raw/articles/anthropic-global-workspace.md"
created: 2026-07-13
updated: 2026-07-13
---

# Verbalizable Representations Form a Global Workspace in Language Models

## Summary

- Introduces the Jacobian lens, an averaged causal map from intermediate residual-stream activations to present and future output tokens, and defines J-space as sparse nonnegative combinations of the resulting token-indexed vectors. The authors typically cap the active set at 25 concepts.
- J-space is small but mechanistically privileged: its component carries a median 6–7% of a concept vector's variance, yet swapping or ablating that component redirects verbal reports and multi-step answers much more strongly than perturbing the remaining representation.
- Heavy J-space ablation drives controlled multi-hop reasoning close to zero while leaving routine classification, factual recall, grammatical fluency, and much ordinary text prediction largely intact. Writing intermediate reasoning steps externally makes some tasks more robust to ablation.
- The readout surfaces internal recognition of prompt injections, evaluation awareness, hidden goals, strategic deliberation, and misreported tool calls that may not appear in the model's visible output, making it a candidate signal for alignment auditing.
- Counterfactual-reflection training teaches a model to articulate ethical principles in hypothetical future continuations; those principles then populate J-space during ordinary inference and improve behavior, while ablating the implanted representations largely reverses the improvement.

## Connections

- [[safety/agentic misalignment risk]]
- [[sources/Monitoring Reasoning Models for Misbehavior]]
- [[concepts/evaluator reliability]]
- [[operations/agent observability]]

## Artifacts

- [[raw/articles/anthropic-global-workspace.md]]

## Notes

- Canonical paper: https://transformer-circuits.pub/2026/workspace/index.html
- Accessible Anthropic summary: https://www.anthropic.com/research/global-workspace
- Main experiments use Claude Sonnet 4.5, with selected corroboration on Haiku 4.5, Opus 4.5, and Opus 4.6. The method is restricted mostly to concepts expressible as vocabulary tokens, although the appendices explore phrase-level extensions.
- The authors claim a functional analogy to access consciousness, not evidence of phenomenal consciousness, and explicitly note that a transformer lacks several architectural features posited by biological global-workspace theories.
