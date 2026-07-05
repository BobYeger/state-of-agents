---
title: "The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions"
aliases:
  - "Instruction Hierarchy"
source_type: "paper"
kind: "model-layer-defense"
status: "verified"
year: 2024
publication_date: "2024-04-19"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2404.13208"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Eric Wallace"
  - "Kai Xiao"
  - "Reimar Leike"
  - "Lilian Weng"
  - "Johannes Heidecke"
  - "Alex Beutel"
venue: "arXiv / OpenAI"
url: "https://arxiv.org/abs/2404.13208"
pdf_url: "https://arxiv.org/pdf/2404.13208"
artifacts:
  - "raw/papers/The Instruction Hierarchy - Training LLMs to Prioritize Privileged Instructions.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# The Instruction Hierarchy

## Summary

- Defines an explicit privilege ordering — system prompt > developer > user > tool outputs — and specifies model behavior when instructions at different levels conflict.
- Training data is generated automatically: aligned lower-privilege instructions are demonstrated as followed, misaligned or injected ones as selectively ignored.
- Applied to GPT-3.5, the method substantially increases robustness, including against attack types never seen during training, with minimal degradation of standard capabilities.
- The canonical model-layer defense that OpenAI later operationalized in GPT-4o-class models and the Model Spec chain of command.

## Connections

- [[safety/prompt injection]]
- [[safety/agent safety and security]]
- [[concepts/tool use]]
- [[sources/IH-Challenge]]
- [[sources/SecAlign]]

## Artifacts

- [[raw/papers/The Instruction Hierarchy - Training LLMs to Prioritize Privileged Instructions.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2404.13208
- Model-layer (weights-level) defense, complementary to harness-level architectures like CaMeL; The Attacker Moves Second shows this class of defense degrades under adaptive attack, so treat robustness numbers as against-the-tested-attacks only.
