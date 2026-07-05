---
title: "LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code"
source_type: "paper"
kind: "benchmark"
status: "verified"
year: 2024
publication_date: "2024-03-12"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2403.07974"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Naman Jain"
  - "King Han"
  - "Alex Gu"
  - "Ion Stoica"
venue: "arXiv / UC Berkeley, MIT, Cornell"
url: "https://arxiv.org/abs/2403.07974"
pdf_url: "https://arxiv.org/pdf/2403.07974"
artifacts:
  - "raw/papers/LiveCodeBench - Holistic and Contamination Free Evaluation of Large Language Models for Code.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# LiveCodeBench

## Summary

- Refresh-by-design benchmark: continuously collects new problems from LeetCode, AtCoder, and Codeforces contests, tagging each with its release date so evaluation can be restricted to problems published after a model's training cutoff.
- Detects contamination empirically by comparing performance on problems released before versus after the model's cutoff — performance cliffs at the cutoff date expose train-set leakage.
- Initial release hosted 400 problems published May 2023 – May 2024 and evaluated 18 base and 34 instruction-tuned LLMs; documented overfitting to HumanEval in existing models.
- Measures holistic code capabilities beyond generation: self-repair, code execution, and test-output prediction.
- v1 2024-03-12, v2 2024-06-06; the live rolling benchmark at livecodebench.github.io continues adding problem batches.

## Connections

- [[benchmarks/agent evaluation]]
- [[operations/agent evals]]
- [[concepts/code factories]]
- [[sources/SWE-bench Illusion]]
- [[sources/SWE-bench Pro]]

## Artifacts

- [[raw/papers/LiveCodeBench - Holistic and Contamination Free Evaluation of Large Language Models for Code.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2403.07974
- Problems are self-contained competitive-programming tasks, not repository-level agentic tasks; the rolling-refresh and cutoff-comparison designs transfer to agent evals, the task distribution does not.
