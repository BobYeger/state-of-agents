---
title: "WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution"
aliases:
  - "WikiSkill"
source_type: "paper"
kind: "skill-evolution"
status: "verified"
year: 2026
publication_date: "2026-08-27"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: null
source_updated_date_basis: null
arxiv_id: "2608.27454"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Liyan Tang"
  - "Cyrus Rashtchian"
  - "Chun-Sung Ferng"
  - "Andrew Tomkins"
  - "Da-Cheng Juan"
  - "Tu Vu"
venue: "arXiv"
url: "https://arxiv.org/abs/2608.27454"
pdf_url: "https://arxiv.org/pdf/2608.27454"
license: "CC BY 4.0"
license_url: "https://creativecommons.org/licenses/by/4.0/"
evidence_class: "research-with-evals"
metrics_status: "three-run-benchmark-transfer-and-ablation-results"
artifacts:
  - "raw/papers/WikiSkill - Compiling Agent Experience into Persistent Knowledge for Skill Evolution.pdf"
created: 2026-09-02
updated: 2026-09-02
---

# WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution

## Summary

- Google Research framework for evolving agent skills while preserving optimization knowledge outside the deployed skill set.
- WikiSkill separates three layers: immutable execution traces in `raw/`; a persistent optimizer-facing `wiki/` with pattern pages, an evolution log, and a skill-impact log; and active skill directories in `skills/`, each containing `SKILL.md` and `PURPOSE.md`.
- Each iteration runs the current skills, consolidates sampled success and failure traces through a Wiki Maintainer, and lets a tool-using Skill Proposer make one atomic create-or-patch proposal to one skill. Held-out validation accepts only an improvement; rejected skill changes roll back while their history and the wiki persist.
- The task-running Inference Agent receives the active skills but not the wiki by default. The wiki is therefore optimizer memory, not an organizational knowledge base or a task-runtime retrieval layer.
- Across five benchmarks and five inference models, WikiSkill has the highest model-level average point estimate in all five rows. Its gaps over the strongest competing method range from 3.3 to 12.0 points; the Qwen-3.5-4B average is statistically tied with SkillOpt, while WikiSkill is the sole top average for the other four models.
- Cross-model transfer is useful but unsafe to assume. Qwen-3.6-27B skills raise Qwen-3.5-9B ALFWorld performance to 70.2, above its 63.4 self-evolved result, while a Qwen-3.5-4B spreadsheet skill drops Gemini-3.5-Flash from 50.5 without a skill to 18.1, versus 76.6 with its own skill.

## Relationship to SkillOpt

WikiSkill is a separate later method and direct comparator to [[sources/SkillOpt]], not a replacement or revision. SkillOpt already retains rejected edits and an epoch-level meta skill as optimizer memory. WikiSkill instead represents optimizer history as an explicit, inspectable, multi-file knowledge base maintained separately from the skills that the task agent executes.

The shared discipline is strict held-out promotion of textual procedure changes. The architectural addition is a write-maintain-compile boundary: raw experience remains immutable, accumulated patterns and proposal outcomes survive in the wiki, and only validated procedures enter the active skill set.

## Evidence

- The evaluation covers LiveMath, SealQA, SpreadsheetBench, OfficeQA, and ALFWorld with five models: Qwen-3.5-4B, Qwen-3.5-9B, Qwen-3.6-27B, Gemma-4-31B, and Gemini-3.5-Flash. Baselines are no skill, Trace2Skill, EvoSkill, and SkillOpt.
- WikiSkill improves over the no-skill condition in 23 of 25 model-benchmark cells, ties one, and hurts one. Qwen-3.5-9B with WikiSkill averages 47.4, above Qwen-3.6-27B without skills at 39.4.
- In the four-benchmark Gemini ablation, enabling wiki access for the Skill Proposer while denying it to the Inference Agent raises the average from 48.7 to 63.7. Giving the Inference Agent wiki access as well reduces the result to 60.9, evidence that optimization knowledge and runtime context should be evaluated as separate surfaces.

## Evidence Boundary

- The ablation does not isolate persistence alone: disabling proposer wiki access also removes the Wiki Maintainer. WikiSkill also differs from SkillOpt in its proposer, batching, multi-skill representation, and trace-access strategy.
- Skills are fully injected into the Inference Agent, so retrieval, triggering, and performance with a large skill library are not tested.
- Validation sets contain 10 to 40 tasks. Results average three complete evolution runs, while the paired bootstrap resamples test tasks rather than optimizer runs.
- Strict improvement gating cannot keep neutral stepping stones. The wiki itself is neither validation-gated nor automatically pruned: pattern pages remain regardless of the later skill gate, while rejected proposal diffs and outcomes are deliberately retained in the impact log.
- The paper does not evaluate production or very-long-horizon operation and does not report budget-matched token, latency, or dollar cost. The v1 record links no official implementation, generated wiki, evolved skills, or dataset repository.

## Claims

- [[claims/Claim - Agent memory and skills create compounding improvement loops]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Connections

- [[sources/SkillOpt]]
- [[maps/Agent Skills Map]]
- [[maps/Self-Improving Systems Map]]
- [[concepts/agent skills]]
- [[concepts/procedural memory]]
- [[concepts/LLM-maintained knowledge bases]]
- [[concepts/lifelong agent learning]]
- [[methods/self-improving code loops]]
- [[operations/agent evals]]

## Artifacts

- [[raw/papers/WikiSkill - Compiling Agent Experience into Persistent Knowledge for Skill Evolution.pdf]]

## Notes

- arXiv v1 was submitted August 27, 2026. The PDF is dated August 28; vault publication metadata uses the arXiv v1 submission timestamp.
- The arXiv record licenses the paper under CC BY 4.0.
- This card describes the v1 snapshot; no later revision was listed when archived on 2026-09-02.
