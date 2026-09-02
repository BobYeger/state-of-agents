---
title: "SkillOpt: Executive Strategy for Self-Evolving Agent Skills"
aliases:
  - "SkillOpt"
source_type: "paper"
kind: "skill-optimization"
status: "verified"
year: 2026
publication_date: "2026-05-22"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: "2026-05-25"
source_updated_date_basis: "arxiv_v2_revision_date"
arxiv_id: "2605.23904"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Yifan Yang"
  - "Ziyang Gong"
  - "Weiquan Huang"
  - "Qihao Yang"
  - "Ziwei Zhou"
  - "Zisu Huang"
  - "Yan Li"
  - "Xuemei Gao"
  - "Qi Dai"
  - "Bei Liu"
  - "Kai Qiu"
  - "Yuqing Yang"
  - "Dongdong Chen"
  - "Xue Yang"
  - "Chong Luo"
venue: "arXiv"
url: "https://arxiv.org/abs/2605.23904"
pdf_url: "https://arxiv.org/pdf/2605.23904"
artifacts:
  - "raw/papers/SkillOpt - Executive Strategy for Self-Evolving Agent Skills.pdf"
  - "raw/docs/skillopt-site.md"
  - "raw/repositories/skillopt-readme.md"
created: 2026-06-16
updated: 2026-09-02
---

# SkillOpt: Executive Strategy for Self-Evolving Agent Skills

## Summary

- Microsoft Research paper and repository for treating a natural-language skill document as trainable external state for a frozen language agent.
- SkillOpt runs scored rollouts, reflects over success/failure minibatches, proposes bounded add/delete/replace edits, and accepts a candidate skill only when held-out validation improves.
- Important because it makes procedural memory optimization look like a real training loop without weight updates: rollout evidence, textual learning rate, rejected-edit buffer, slow/meta update, validation gate, and exported `best_skill.md`.
- The paper reports gains across six benchmarks, seven target models, and three execution harnesses: direct chat, Codex, and Claude Code. The arXiv abstract reports best or tied-best performance on all 52 evaluated model/benchmark/harness cells.
- Project/repo updates also introduce SkillOpt-Sleep as a nightly offline self-evolution companion for local coding agents; treat that as an implementation preview rather than the core paper result.

## Claims

- [[claims/Claim - Agent memory and skills create compounding improvement loops]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Connections

- [[sources/WikiSkill]]
- [[maps/Agent Skills Map]]
- [[concepts/agent skills]]
- [[concepts/procedural memory]]
- [[concepts/dreaming and memory consolidation]]
- [[concepts/lifelong agent learning]]
- [[methods/self-improving code loops]]
- [[operations/agent evals]]
- [[operations/agent harnesses]]
- [[systems/Codex]]
- [[systems/Claude Code]]

## Artifacts

- [[raw/papers/SkillOpt - Executive Strategy for Self-Evolving Agent Skills.pdf]]
- [[raw/docs/skillopt-site.md]]
- [[raw/repositories/skillopt-readme.md]]

## Notes

- Canonical arXiv URL: https://arxiv.org/abs/2605.23904
- Project page: https://microsoft.github.io/SkillOpt/
- Repository: https://github.com/microsoft/SkillOpt
- arXiv metadata: submitted May 22, 2026; revised May 25, 2026.
- The source is especially relevant to cross-harness skill transfer because the project page reports Codex-trained SpreadsheetBench skills transferring into Claude Code.
