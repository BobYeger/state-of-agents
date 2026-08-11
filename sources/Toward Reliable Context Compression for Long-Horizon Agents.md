---
title: "Toward Reliable Context Compression for Long-Horizon Agents: An Empirical Study of Execution Instability"
aliases:
  - "Toward Reliable Context Compression"
  - "TRACE"
  - "Trajectory-Relative Agent Context Compression"
source_type: "paper"
kind: "context-compression"
status: "verified"
year: 2026
publication_date: "2026-08-06"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: null
source_updated_date_basis: null
arxiv_id: "2608.06503"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Guanghui Min"
  - "Liang Wu"
  - "Mayank Darbari"
  - "Chen Chen"
  - "Liangjie Hong"
venue: "arXiv"
url: "https://arxiv.org/abs/2608.06503"
pdf_url: "https://arxiv.org/pdf/2608.06503"
license: "CC BY 4.0"
license_url: "https://creativecommons.org/licenses/by/4.0/"
artifacts:
  - "raw/papers/Toward Reliable Context Compression for Long-Horizon Agents.pdf"
created: 2026-08-11
updated: 2026-08-11
---

# Toward Reliable Context Compression for Long-Horizon Agents

## Summary

- The paper argues that compression must preserve an agent's position in an unfolding execution, not just salient facts. A declarative summary can retain entities and plans while weakening recognition of completed actions, current constraints, or when to stop.
- In a 147-task AppWorld train/development study with MiniMax-M3 and an OpenClaw-derived loop, summary compression beats FIFO clearly only at the tightest 2K budget: 72.8% mean pass rate versus 42.2%. Both remain below full context.
- Matched next-action probes show partial attenuation after summarization: divergence from full-history behavior is 0.149 when recent interactions remain raw, 0.233 when compressed, and 0.289 when omitted.
- At 590 compaction boundaries, 4,640 short closed-loop rollouts compare two renderings from the same environment state. PRE retains the raw interaction update; POST replaces it with the candidate summary plus the retained raw turn. At the first post-boundary action, POST produces 0.108 more blocked/error actions and 0.031 more re-fetch/replay actions.
- These POST-minus-PRE differences estimate the immediate execution burden introduced when raw history is replaced at the boundary. PRE is a paired control for the frozen agent's variability, not a gold trajectory, and the experiment does not attribute broader run-level instability solely to information lost in compaction.
- TRACE uses this boundary-local signal to optimize a natural-language compression template while freezing the compressor, downstream agent, tools, parser, system prompt, and decoding. It samples three summaries at 12 selected error-producing boundaries, proposes five templates, and selects with two-run Pass2 on development tasks.
- On 168 AppWorld test tasks at a 4,096-token window, MiniMax-M3 with TRACE reaches 77.1% mean accuracy and 67.3% Pass2 versus 71.4% and 59.5% for the strongest compressed baseline; full context remains higher at 85.7% and 77.4%.
- The MiniMax-optimized template transfers once to Kimi-K2.7-Code, reaching 84.5% accuracy and 79.2% Pass2 versus 82.7% and 73.8% for full context, but lower Pass@2 and worse hard-task results limit the claim.

## Evidence Boundary

The authors call this a preliminary empirical study. It covers one stateful API benchmark, one optimization model, and one transfer model. AppWorld state can often be queried again, so the setup measures recoverable execution burden better than irreversible evidence loss.

Optimization uses only 12 selected boundaries, and the verifier observes blocked/error actions plus repeated canonicalized tool calls. It can miss silent state corruption, wrong plans, security failures, and nonrepetitive waste; repetition can also be legitimate. Main results use two runs per condition, limiting precision. The durable contribution is the paired boundary-local evaluation design, not a universal compression policy.

## Claims

- [[claims/Claim - Context management is an agent architecture choice]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Connections

- [[concepts/context compaction]]
- [[operations/agent evals]]
- [[maps/Context Management Map]]
- [[sources/Factory Context Compression Evaluation]]
- [[sources/Parallel Context Compaction]]

## Artifacts

- [[raw/papers/Toward Reliable Context Compression for Long-Horizon Agents.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2608.06503
- Code: https://github.com/nokia-applied-research/Trace
- arXiv lists only v1 at capture time.
- TRACE expands to Trajectory-Relative Agent Context ComprEssion.
- The paper and preserved PDF are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
