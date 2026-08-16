---
title: "LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues"
aliases:
  - "LongMemEval-V2"
  - "LME-V2"
  - "LongMemEval V2"
source_type: "paper"
kind: "agent-experience-memory-benchmark"
status: "verified"
year: 2026
publication_date: "2026-05-12"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: null
source_updated_date_basis: null
arxiv_id: "2605.12493"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Di Wu"
  - "Zixiang Ji"
  - "Asmi Kawatkar"
  - "Bryan Kwan"
  - "Jia-Chen Gu"
  - "Nanyun Peng"
  - "Kai-Wei Chang"
venue: "arXiv (work in progress)"
url: "https://arxiv.org/abs/2605.12493"
pdf_url: "https://arxiv.org/pdf/2605.12493"
license: "CC BY 4.0"
license_url: "https://creativecommons.org/licenses/by/4.0/"
created: 2026-08-16
updated: 2026-08-16
---

# LongMemEval-V2

## Summary

- LongMemEval-V2 evaluates whether memory turns accumulated web-agent trajectories into environment-specific experience: static interface state, dynamic state transitions, workflows, recurring gotchas, and awareness that a question's premise may be wrong in the current environment.
- Its 451 manually curated questions draw from multimodal WebArena, WorkArena, and WorkArena++ trajectories. Small haystacks contain 100 trajectories and about 25.6 million tokens; question-specific medium haystacks average 498 trajectories and about 114.8 million tokens.
- Memory is evaluated as context gathering. A system incrementally inserts an ordered trajectory history and returns bounded evidence for a fixed Qwen3.5-9B reader; accuracy and query latency are measured separately. This isolates evidence gathering from end-to-end tool execution.
- Simple query-to-slice RAG reaches 42.8% on the small tier and 38.1% on medium. Adding trajectory notes reaches 51.0% and 45.9%. AgentRunbook-R separates raw state slices, state-transition events, and procedure/gotcha notes and reaches 58.6% and 57.0% at roughly 26 seconds per query.
- An off-the-shelf Codex file-search baseline reaches 69.9%/68.7%. AgentRunbook-C stores trajectories as files and adds a memory workflow, query-time manifests, and inspection helpers; it reaches 74.9%/70.1%, or 72.5% averaged across tiers, while taking 108–140 seconds per query.
- AgentRunbook-C is about 32% faster than the Codex baseline in the reported configuration, but remains much slower than RAG. The result supports coding agents as high-accuracy memory controllers and makes the accuracy–latency trade-off explicit.

## Report Implications

The benchmark spine should include **environment experience** separately from conversational personalization. A coding agent may need memory of interface affordances, world-state transitions, procedures, failure modes, and invalid assumptions rather than only facts about a user.

The report should compare memory systems using a fixed-reader context-gathering protocol as well as downstream task success. File-based agent search is an important baseline, but its high query latency means it should be paired with cheaper retrieval paths or reserved for difficult questions.

## Evidence Boundary

The arXiv record labels this v1 paper “Work in Progress.” It covers customized browser environments and pre-collected trajectories, not online learning as an agent's own policy changes. Questions are manually written and checked, but some answer-trajectory mapping begins with Codex proposals before human verification.

The context-gathering setup fixes a Qwen3.5-9B reader and truncates returned evidence to 200K tokens; it does not measure live planning, tool use, or task completion. Coding-agent results depend on GPT-5.4-mini, Codex v0.117.0, prompts, and sandbox helpers and appear to be one run per question, with bootstrap significance over questions rather than independent system replications. The benchmark is strong evidence for a missing evaluation category, not a production memory ranking.

## Claims

- [[claims/Claim - Agent memory and skills create compounding improvement loops]]
- [[claims/Claim - Context management is an agent architecture choice]]

## Connections

- [[operations/agent memory]]
- [[operations/agent evals]]
- [[concepts/procedural memory]]
- [[concepts/lifelong agent learning]]
- [[concepts/context retrieval]]
- [[maps/Context Management Map]]
- [[sources/LongMemEval]]
- [[sources/Trajectory-Informed Memory Generation]]

## Notes

- Canonical arXiv URL: https://arxiv.org/abs/2605.12493
- Project: https://xiaowu0162.github.io/longmemeval-v2/
- Repository: https://github.com/xiaowu0162/LongMemEval-V2
- arXiv lists only v1 and labels the paper “Work in Progress” at capture time.
- The paper is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
