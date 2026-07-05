---
title: "SWE-RL: Advancing LLM Reasoning via Reinforcement Learning on Open Software Evolution"
aliases:
  - "SWE-RL"
source_type: "paper"
kind: "agentic-rl-training"
status: "verified"
year: 2025
publication_date: "2025-02-25"
publication_date_basis: "arxiv_abs_page"
source_updated_date: "2025-12-01"
source_updated_date_basis: "arxiv_v2_revision_date"
arxiv_id: "2502.18449"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Yuxiang Wei"
  - "Olivier Duchenne"
  - "Gabriel Synnaeve"
  - "Sida I. Wang"
venue: "arXiv / NeurIPS 2025 (main track); Meta FAIR"
url: "https://arxiv.org/abs/2502.18449"
pdf_url: "https://arxiv.org/pdf/2502.18449"
artifacts:
  - "raw/papers/SWE-RL - Advancing LLM Reasoning via Reinforcement Learning on Open Software Evolution.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# SWE-RL

## Summary

- First RL approach trained on open-source software evolution data (GitHub issues, PRs, code diffs) rather than curated executable environments.
- Reward is lightweight and rule-based: a continuous similarity score between the generated patch and the ground-truth oracle patch — no test execution needed at training time.
- Llama3-SWE-RL-70B reaches 41.0% solve rate on SWE-bench Verified — best-in-class among sub-100B models at release, comparable to GPT-4o.
- Despite training only on software engineering data, it improves five out-of-domain tasks (math, general reasoning) — evidence that software-engineering RL generalizes.
- v1 2025-02-25, v2 2025-12-01; accepted to NeurIPS 2025 main track.

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Connections

- [[operations/agent harnesses]]
- [[concepts/code factories]]
- [[sources/SWE-bench Verified]]
- [[sources/Meta Agentic Program Repair]]

## Artifacts

- [[raw/papers/SWE-RL - Advancing LLM Reasoning via Reinforcement Learning on Open Software Evolution.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2502.18449
- Serves as the weights-side data point in the weights-vs-harness comparison: pure RL on software-evolution data reached 41% at release while harness-based systems on the same benchmark reached the 60-70% range — the claim link above is comparative, not an endorsement in the paper itself.
- The similarity-based reward avoids test execution but is also a weaker verification signal than execution-based rewards; keep that distinction when citing.
