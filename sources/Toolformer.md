---
title: "Toolformer: Language Models Can Teach Themselves to Use Tools"
aliases:
  - "Toolformer"
source_type: "paper"
kind: "learned-tool-use"
status: "verified"
year: 2023
publication_date: "2023-02-09"
publication_date_basis: "arxiv_v1_submission_history"
source_updated_date: "2023-02-09"
source_updated_date_basis: "arxiv_v1"
arxiv_id: "2302.04761"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Timo Schick"
  - "Jane Dwivedi-Yu"
  - "Roberto Dessì"
  - "Roberta Raileanu"
  - "Maria Lomeli"
  - "Luke Zettlemoyer"
  - "Nicola Cancedda"
  - "Thomas Scialom"
venue: "arXiv"
url: "https://arxiv.org/abs/2302.04761"
pdf_url: "https://arxiv.org/pdf/2302.04761v1"
artifacts: []
created: 2026-10-05
updated: 2026-10-05
---

# Toolformer

## Summary

- Learns when to call an API, its arguments, and how to use its result. Candidate calls are sampled, executed, and retained when their results reduce subsequent token-prediction loss; the model is then fine-tuned on the augmented text.
- Uses a few demonstrations per predefined tool and a 6.7B GPT-J base model. This is training a tool-use policy, rather than discovering an unknown tool catalog at inference time.

## Evidence and Limits

- Section 4 tests factual lookup, arithmetic, question answering, translation-related tasks, and language modeling. Results support the usefulness of learned calls within these settings; they do not establish general agent autonomy.
- Section 7 explicitly identifies missing chained and interactive tool use, sensitivity to prompt wording, sample inefficiency, and the absence of tool-specific execution cost in call decisions.
- Read the v1 paper for this note. The PDF is linked rather than redistributed in the vault.

## Connections

- [[concepts/tool use]]
- [[concepts/dynamic tool discovery]]
- [[concepts/programmatic tool calling]]
- [[sources/Gorilla]]
- [[sources/CodeAct]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
