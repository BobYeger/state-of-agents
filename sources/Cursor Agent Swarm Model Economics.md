---
title: "Agent swarms and the new model economics"
aliases:
  - "Cursor agent swarm model economics"
  - "Cursor SQLite swarm experiment"
  - "Cursor planner-worker model routing"
source_type: "article"
kind: "vendor-operator-report"
status: "verified"
year: 2026
publication_date: "2026-07-20"
publication_date_basis: "json_ld_date_published"
source_updated_date: "2026-07-22"
source_updated_date_basis: "capture_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Wilson Lin"
venue: "Cursor"
url: "https://cursor.com/blog/agent-swarm-model-economics"
pdf_url: ""
evidence_class: "vendor-operator-report"
metrics_status: "vendor-reported-single-study"
artifacts:
  - "raw/articles/cursor-agent-swarm-model-economics.md"
created: 2026-07-22
updated: 2026-07-22
---

# Agent swarms and the new model economics

## Summary

- Cursor compares an older and newer agent swarm on the same hard task: rebuilding SQLite in Rust from its 835-page manual, without source code, tests, the SQLite binary, or internet access. Both systems use the same model configurations and time budget; progress is measured against the held-out `sqllogictest` suite.
- The new harness outperforms the old in every tested model configuration. At the four-hour cutoff, new runs score roughly 73–85% of the suite while old runs range from 11–77%; every new run eventually reaches 100% in the reported experiment. These are vendor-reported results from one study, not an independently reproduced benchmark.
- The swarm has two main roles: frontier-capability planners recursively decompose the goal, while faster workers execute narrow leaves. Cursor argues that context specialization—not parallelism alone—is the main scaling mechanism: planners avoid low-level implementation detail and workers avoid carrying the whole plan.
- The model economics are highly role-sensitive. Cursor reports similar quality across mixes but total costs from $1,339 for an Opus 4.8 planner with Composer 2.5 workers to $10,565 for GPT-5.5 used throughout. Workers consume most tokens, but expensive planner tokens can dominate dollars; reported worker spend was $9,373 in the all-GPT-5.5 run and $411 in the Opus/Composer run.
- At swarm scale, Git is replaced by a purpose-built VCS. Cursor reports throughput rising from roughly 1,000 commits per hour in the earlier browser swarm to about 1,000 commits per second in the new system, with coordination mechanisms for split-brain design, planner contention, merge conflicts, megafiles, and architectural ossification.
- The system also uses decorrelated review lenses and an agent-owned Field Guide: a line-budgeted shared context folder that captures surprising lessons for successor agents. This is within-run adaptive context, not evidence that the harness improves itself across runs; the article does not provide an ablation isolating the Field Guide's effect.

## SQLite Comparison

| Measure | Cursor-reported result |
|---|---|
| Task | Rebuild SQLite in Rust from documentation only |
| Specification | 835-page SQLite manual |
| Held-out evaluator | `sqllogictest`, millions of known-answer queries |
| New vs old harness | New swarm wins in every tested model configuration |
| Four-hour new-run range | Approximately 73–85% |
| Four-hour old-run range | Approximately 11–77% |
| New-run endpoint | Every new configuration passed 100% of the suite |
| Old Grok 4.5 run | Paused before two hours after runaway coordination |

Cursor says it manually reviewed the code and run for cheating, shortcuts, and uneven implementation. That is a useful integrity check, but it is not an independent audit and the article does not publish a full protocol or raw run artifacts.

## Coordination Diagnostics

The strongest evidence for the harness change is not only the final grade but the reduction in coordination churn and architectural sprawl:

| Diagnostic | Old harness | New harness |
|---|---:|---:|
| Grok 4.5 commits | 68,000 in the first two hours | Roughly 70x lower pace over the comparison window |
| Grok 4.5 merge conflicts | More than 70,000 before the run was paused | Fewer than 1,000 over four hours |
| Conflicts in the hottest file | 7,771, with 1,173 agents touching it | 47 |
| Rust crates in the Grok 4.5 codebase | 54, including three SQL packages | Nine, stable from early in the run |
| Fable 5 engine code at 100% | 64,305 lines | 9,908 lines |
| Opus-mix engine code and grade | 19,013 lines at 97% | 4,645 lines at 100% |

These diagnostics support Cursor's interpretation that the old harness was producing thrash rather than useful throughput. They remain first-party measurements from one task, and the article does not ablate the contribution of the VCS, planner rules, conflict agent, megafile policy, review lenses, or Field Guide.

## Planner–Worker Economics

The tested configurations were GPT-5.5 throughout, Grok 4.5 throughout, Opus 4.8 as planner with Composer 2.5 as worker, and Fable 5 as planner with Composer 2.5 as worker. Cursor reports similar quality across the mixes but very different spend:

- Opus 4.8 planner plus Composer 2.5 workers: approximately $1,339 total.
- GPT-5.5 throughout: approximately $10,565 total; workers alone account for approximately $9,373.
- The Opus/Composer hybrid's workers cost approximately $411.
- Workers carry at least 69% of tokens and more than 90% in most runs, while the planner can still account for roughly two-thirds of dollars because its tokens are more expensive.
- The Fable 5 planner used fewer planning tokens than Opus 4.8 despite a higher per-token price, but its workers consumed several times as many tokens and the total run was more expensive.

The design implication is conditional model routing: spend frontier capability on decomposition, architecture, and ambiguous decisions; route bounded execution to cheaper workers when the handoff is explicit enough. The article's claim is an operator hypothesis backed by one study, not a general cost law.

## Coordination Mechanisms

- **Split-brain design:** planners make design decisions themselves and must ensure delegated subtrees do not decide the same question.
- **Planner contention:** shared design documents carry decisions, and code references those decisions so a reconciler can propagate a resolution.
- **Merge conflicts:** a neutral third-party agent resolves collisions instead of asking workers to absorb each other's context and merge directly.
- **Megafiles:** bloated files are flagged, new commits are blocked, and an outside agent decomposes the file into modules.
- **Ossification:** agents may make narrowly scoped intentional breakage with an explanatory comment so dependent agents follow the new design through compiler errors.
- **Review lenses:** reviewers vary by transcript visibility, output visibility, model family, and personality; Cursor argues that decorrelated lenses stack better than one perfect reviewer.
- **Field Guide:** agents curate a line-budgeted shared context folder whose index is injected into new agent sessions, turning surprising encounters into reusable procedural knowledge.

## Model and Harness Boundary

This article is best read alongside [[sources/Cursor Self-Driving Codebases]] and [[sources/Cursor Scaling Long-Running Autonomous Coding]], not as proof that more agents always help. It supports a narrower thesis: at sufficient task scale, role-specific context, explicit design artifacts, conflict-resolution machinery, and review diversity can make a swarm more stable, while role-aware model routing can reduce cost relative to uniform frontier execution.

The footnote also records a negative result: Cursor attempted to include GPT-5.6 Sol as the frontier configuration but saw sensitivity to literal/emphasized wording and runaway spirals, without time to tune that model. That is an anecdote about prompt/harness fit, not a model capability ranking.

## Claims

- [[claims/Claim - Coordination is a cost the task must justify]]
- [[claims/Claim - Agent systems improve when structure matches the task]]
- [[claims/Claim - Agent teams need explicit organization]]
- [[claims/Claim - Context management is an agent architecture choice]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[sources/Cursor Self-Driving Codebases]]
- [[sources/Cursor Scaling Long-Running Autonomous Coding]]
- [[sources/Cursor Improving Agent Harness]]
- [[sources/Cursor Multi-Agent Kernels]]
- [[sources/Factory How Missions Work]]
- [[sources/Cognition Multi-Agents Whats Actually Working]]
- [[systems/Cursor agents]]
- [[concepts/code factories]]
- [[concepts/context engineering]]
- [[concepts/subagent context isolation]]
- [[methods/multi-agent orchestration]]
- [[methods/runtime routing]]
- [[operations/agent observability]]
- [[maps/MAS Orchestration and Architecture]]
- [[maps/Harness Design Playbook]]
- [[maps/Code Factory Playbook]]

## Artifacts

- [[raw/articles/cursor-agent-swarm-model-economics]]

## Evidence Boundary

This is a detailed first-party Cursor operator report with a same-task old-versus-new comparison and unusually concrete cost, token, commit, conflict, and code-size figures. The experiment remains vendor-run: the article does not provide raw traces, a preregistered protocol, independent replication, a full model-cost ledger, or an ablation for each coordination mechanism. The manual review for cheating and uneven implementation is valuable but not independent evaluation.

## Notes

- Canonical URL: https://cursor.com/blog/agent-swarm-model-economics
- Author: Wilson Lin.
- Visible JSON-LD publication date: 2026-07-20.
- Public code: https://github.com/cursor/minisqlite. Cursor identifies this as the output of a solo Opus 4.8 run and says it had not deeply reviewed it; it is not a release of the swarm runs or raw experimental traces.
- The structured raw capture preserves metadata, section structure, quantitative facts, and caveats without republishing the article verbatim.
