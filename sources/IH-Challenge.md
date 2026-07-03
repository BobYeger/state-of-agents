---
title: "IH-Challenge: A Training Dataset to Improve Instruction Hierarchy on Frontier LLMs"
aliases:
  - "IH-Challenge"
source_type: "paper"
kind: "instruction-hierarchy-training"
status: "verified"
year: 2026
publication_date: "2026-03-11"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2603.10521"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Chuan Guo"
  - "Juan Felipe Ceron Uribe"
  - "Sicheng Zhu"
  - "Christopher A. Choquette-Choo"
  - "Steph Lin"
  - "Nikhil Kandpal"
  - "Milad Nasr"
  - "Rai (Michael Pokorny)"
  - "Sam Toyer"
  - "Miles Wang"
  - "Yaodong Yu"
  - "Alex Beutel"
  - "Kai Xiao"
venue: "arXiv / OpenAI"
url: "https://arxiv.org/abs/2603.10521"
pdf_url: "https://arxiv.org/pdf/2603.10521"
created: 2026-07-03
updated: 2026-07-03
---

# IH-Challenge

## Summary

- Direct 2026 successor to the 2024 instruction-hierarchy paper: an RL training dataset covering system/developer/user/tool conflict resolution, released publicly on Hugging Face (openai/ih-challenge).
- Fine-tuning GPT-5-Mini with online adversarial example generation improves instruction-hierarchy robustness by +10.0% on average across 16 in-distribution, out-of-distribution, and human red-teaming benchmarks (84.1% to 94.1%).
- Unsafe behavior drops from 6.6% to 0.7%, and the trained model saturates OpenAI's internal agentic prompt-injection tests.
- Reported with minimal capability loss; also improves safety steerability via system-prompt safety specs.

## Connections

- [[safety/prompt injection]]
- [[benchmarks/agent evaluation]]
- [[sources/The Instruction Hierarchy]]
- [[sources/The Attacker Moves Second]]

## Notes

- Canonical URL: https://arxiv.org/abs/2603.10521
- Full 13-author list verified against the arXiv abs page (2026-07-03); the announcement's abbreviated list had omitted six mid-list authors.
- Saturation of OpenAI's internal injection tests is a vendor-internal measure, not an independent evaluation.
