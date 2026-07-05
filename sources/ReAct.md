---
title: "ReAct: Synergizing Reasoning and Acting in Language Models"
aliases:
  - "ReAct"
source_type: "paper"
kind: "agent-loop-pattern"
status: "verified"
year: 2022
publication_date: "2022-10-06"
publication_date_basis: "arxiv_abs_page"
source_updated_date: "2023-03-10"
source_updated_date_basis: "arxiv_v3_camera_ready_date"
arxiv_id: "2210.03629"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Shunyu Yao"
  - "Jeffrey Zhao"
  - "Dian Yu"
  - "Nan Du"
  - "Izhak Shafran"
  - "Karthik Narasimhan"
  - "Yuan Cao"
venue: "arXiv / ICLR 2023"
url: "https://arxiv.org/abs/2210.03629"
pdf_url: "https://arxiv.org/pdf/2210.03629"
artifacts:
  - "raw/papers/ReAct - Synergizing Reasoning and Acting in Language Models.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# ReAct

## Summary

- Defines the interleaved reasoning-trace + action loop that every modern agent harness assumes: reasoning traces induce, track, and update plans while actions ground the model in external sources.
- On HotpotQA and Fever, interacting with a simple Wikipedia API overcomes the hallucination and error propagation seen in pure chain-of-thought.
- ALFWorld: +34% absolute success over imitation/RL baselines; WebShop: +10% absolute, with only 1-2 in-context examples.
- v3 camera-ready 2023-03-10 (ICLR 2023); first author Shunyu Yao later co-authored both Reflexion and SWE-agent, giving a clean lineage line from this loop pattern to production coding harnesses.

## Connections

- [[concepts/loop engineering]]
- [[methods/deliberative control]]
- [[concepts/tool use]]
- [[sources/Reflexion]]
- [[sources/SWE-agent]]

## Artifacts

- [[raw/papers/ReAct - Synergizing Reasoning and Acting in Language Models.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2210.03629
- Root node of the agent-loop methodology lineage; the vault's loop-engineering notes referenced it in passing before this card existed.
- Results predate native tool-calling APIs; the contribution is the loop structure, not the specific benchmark numbers.
