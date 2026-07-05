---
title: "Debating with More Persuasive LLMs Leads to More Truthful Answers"
aliases:
  - "persuasive debate oversight"
source_type: "paper"
kind: "adversarial-debate-oversight"
status: "verified"
year: 2024
publication_date: "2024-02-09"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2402.06782"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Akbir Khan"
  - "John Hughes"
  - "Dan Valentine"
  - "Laura Ruis"
  - "Kshitij Sachan"
  - "Ansh Radhakrishnan"
  - "Edward Grefenstette"
  - "Samuel R. Bowman"
  - "Tim Rocktäschel"
  - "Ethan Perez"
venue: "arXiv / ICML 2024 Best Paper (UCL / Anthropic / Speechmatics)"
url: "https://arxiv.org/abs/2402.06782"
pdf_url: "https://arxiv.org/pdf/2402.06782"
artifacts:
  - "raw/papers/Debating with More Persuasive LLMs Leads to More Truthful Answers.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# Debating with More Persuasive LLMs

## Summary

- Adversarial debate as judge aggregation: two LLM experts argue for different answers on QuALITY reading comprehension, and a non-expert judge (without access to the passage) picks the winner.
- Non-expert LLM judges reach 76% accuracy with debate vs 48% naive baseline; human judges reach 88% vs 60% baseline.
- Optimizing expert debaters for persuasiveness in an unsupervised manner (no ground-truth labels) improves the non-expert judge's ability to identify truth — persuasion pressure helps rather than corrupts in this asymmetric-information setup.
- Won a Best Paper Award at ICML 2024; core empirical evidence that weak-judge/strong-debater oversight can work without ground truth.
- Latest arXiv revision 2024-07-25.

## Claims

- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[methods/deliberative control]]
- [[operations/agent evals]]
- [[sources/Judging LLM-as-a-Judge with MT-Bench]]
- [[sources/Multiagent Debate Improves Factuality and Reasoning]]

## Artifacts

- [[raw/papers/Debating with More Persuasive LLMs Leads to More Truthful Answers.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2402.06782
- The crucial contrast case in the debate literature: adversarial assigned-position debate with a separate judge works where free-form consensus debate entrenches — this anchors the majority-voting vs judge-aggregation distinction.
- Results are on a reading-comprehension task with an information asymmetry by construction; the setup differs from open-ended agent task debate.
