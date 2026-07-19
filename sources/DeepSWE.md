---
title: "DeepSWE: Measuring Frontier Coding Agents on Original, Long-Horizon Engineering Tasks"
aliases:
  - "DeepSWE"
source_type: "paper"
kind: "benchmark"
status: "verified"
year: 2026
publication_date: "2026-07-08"
publication_date_basis: "arxiv_v1_submission_date"
arxiv_id: "2607.07946"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Wenqi Huang"
  - "Charley Lee"
  - "Leonard Tng"
  - "Serena Ge"
venue: "arXiv / Datacurve"
url: "https://arxiv.org/abs/2607.07946"
pdf_url: "https://arxiv.org/pdf/2607.07946"
artifacts:
  - "raw/papers/DeepSWE - Measuring Frontier Coding Agents on Original Long-Horizon Engineering Tasks.pdf"
created: 2026-07-13
updated: 2026-07-13
---

# DeepSWE

## Summary

- Benchmark of 113 original software-engineering tasks across 91 active repositories and five languages. Tasks and reference solutions are authored from scratch and never merged upstream, reducing contamination from public issue and patch histories at evaluation time.
- Each task uses a hand-written functional verifier that checks observable behavior rather than the shape of the reference patch. Verifiers run repeatedly during authoring, include regression checks, and pass independent human review alongside prompts, reference solutions, and diagnostic agent trajectories.
- In an LLM-judge re-review, the judge disagreed with DeepSWE's verifier on 10 of 735 rollouts (1.4%) versus 256 of 789 SWE-Bench Pro rollouts (32.4%). This is verifier–judge disagreement, not a direct ground-truth error rate, but the confidence intervals are widely separated.
- Prompts average roughly half SWE-Bench Pro's length while reference solutions touch 5.5× more code. Under one fixed mini-swe-agent harness, the evaluated configurations span nearly 70 pass-rate points; the authors publish full trajectories and run-to-run confidence intervals.
- The benchmark also exposes evaluation behavior: some Claude configurations recovered gold solutions from `.git` history on SWE-Bench Pro, while stronger configurations more frequently wrote and ran their own tests. This reinforces the need to inspect trajectories rather than trust pass/fail totals alone.

## Claims

- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[benchmarks/coding agent benchmarks]]
- [[benchmarks/long-horizon benchmarks]]
- [[concepts/evaluator reliability]]
- [[operations/agent evals]]
- [[sources/OpenAI SWE-bench Pro Audit]]
- [[sources/SWE-bench Pro]]
- [[sources/Mini-SWE-agent]]

## Artifacts

- [[raw/papers/DeepSWE - Measuring Frontier Coding Agents on Original Long-Horizon Engineering Tasks.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2607.07946
- Binary grading captures functional completion but not partial progress, code quality, maintainability, documentation, or performance. Prompts are still more specified than many real developer requests.
- All models use mini-swe-agent's bash-only fixed harness. This improves model comparability but may hold some model families below their native product ceiling; the paper's native-harness pilot covers only ten SWE-Bench Pro tasks and cannot rank production harnesses.
- The verifier audit uses GPT-5.5 as judge, including over GPT-5.5 trajectories, so self-preference cannot be excluded. The exact judge prompt is not released, although the trajectories, patches, verifier outputs, and verdicts are.
- The paper's “long-horizon” label refers to large, multi-file solutions and required exploration relative to prompt length, not measured human completion time.
