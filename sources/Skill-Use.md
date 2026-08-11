---
title: "Skill-Use: Can LLMs Actually Use Skills in Agentic Harnesses?"
aliases:
  - "Skill-Use"
  - "Skill-Use Benchmark"
source_type: "paper"
kind: "skill-use-benchmark"
status: "verified"
year: 2026
publication_date: "2026-08-05"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: null
source_updated_date_basis: null
arxiv_id: "2608.04828"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Jinyi Han"
  - "Yuanjian Xu"
  - "Ying Liao"
  - "Xinyi Wang"
  - "Zishang Jiang"
  - "Zixiang Di"
  - "Fanyang Lu"
  - "Zhichao Hu"
  - "Yanghua Xiao"
venue: "arXiv"
url: "https://arxiv.org/abs/2608.04828"
pdf_url: "https://arxiv.org/pdf/2608.04828"
license: "CC BY 4.0"
license_url: "https://creativecommons.org/licenses/by/4.0/"
artifacts:
  - "raw/papers/Skill-Use - Can LLMs Actually Use Skills in Agentic Harnesses.pdf"
created: 2026-08-11
updated: 2026-08-11
---

# Skill-Use: Can LLMs Actually Use Skills in Agentic Harnesses?

## Summary

- Skill-Use evaluates whether an agent can use an existing skill under progressive disclosure. Initially the agent sees only the skill name, description, and path; it must recognize relevance, retrieve the full document, and execute its procedure.
- The score separates **Trigger** (retrieve the target skill), **Compliance** (follow required steps), and **Boundary** (avoid prohibited operations). Task completion is measured separately. The aggregate is gated by Trigger and weights Compliance 0.7 and Boundary 0.3.
- The benchmark pairs 79 public skills with 177 executable tasks in nine domains and grades trajectories and artifacts against 1,314 rubric items. Tasks run in isolated Ubuntu containers with real files and tools.
- Eight models are evaluated under Claude Code and Codex. The best configuration, GPT-5.5 under Claude Code, reaches 0.613 aggregate Skill-Use; the best conditional Compliance among triggered traces is 0.638.
- Skill use is harness-conditioned. GPT-5.5 leads under Claude Code, Claude Opus 4.8 leads under Codex, and several open-weight models move sharply between harnesses. Trigger and Compliance remain distinct bottlenecks.
- Concrete file-processing, database, and data-science procedures are followed more reliably than open-ended business-analysis and architecture guidance. Strong in-scope skill use also does not guarantee restraint on adjacent tasks.

## Scoped Ablations

These secondary findings do not all cover both harnesses:

- **Preloading is Codex-only.** Pairing native metadata-only discovery with the full skill preloaded mainly raises Trigger; among runs that trigger in both modes, execution quality changes little.
- **Library scaling is Claude Code-only.** Expanding from one to ten installed skills produces the largest selection drop; failures are mostly no-skill outcomes rather than wrong-skill choices.
- **Out-of-scope restraint is Claude Code-only.** On 53 topically adjacent tasks across six models, within-scope Skill-Use does not predict avoiding unnecessary invocation.
- **Task-completion pairing is Claude Code-only.** Across 779 triggered skill-enabled runs paired with no-library baselines, task completion turns from negative to positive near a Skill-Use score of 0.5. This is an association within the selected triggered traces, not evidence that skills create improvement across runs.

## Evidence Boundary

This is an author-built arXiv v1 benchmark, not an independent audit of production skill systems. The public skills improve realism, but tasks and hidden rubrics are deliberately constructed for skill-exclusive, observable procedures. GUI-, GPU-, and paid-API-heavy skills are de-emphasized.

Claude Code and Codex have different turn limits, and no ordinary repeated seed is reported per task–model–harness cell. The aggregate score embeds a normative weighting. Semantic scoring is imperfect: rescoring preserves broad tiers, while reported single-score agreement is moderate. The 53-task negative set tests over-invocation in one harness and is not a safety certification.

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[maps/Agent Skills Map]]
- [[concepts/agent skills]]
- [[operations/agent evals]]
- [[sources/SkillsBench]]
- [[sources/SkillOpt]]

## Artifacts

- [[raw/papers/Skill-Use - Can LLMs Actually Use Skills in Agentic Harnesses.pdf]]

## Notes

- Canonical arXiv URL: https://arxiv.org/abs/2608.04828
- Repository: https://github.com/JinyiHan99/Skill-Use-Bench
- arXiv lists only v1 at capture time.
- The paper and preserved PDF are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
