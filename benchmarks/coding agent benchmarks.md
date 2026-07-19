# Coding Agent Benchmarks

Coding agent benchmarks measure end-to-end completion of software tasks — issue resolution, terminal work, tool-mediated user interaction — rather than isolated code generation. They are the primary public evidence base for coding-agent capability claims, and also the clearest documented case study in how benchmarks decay.

## The SWE-bench Family

[[sources/SWE-bench]] set the template: real GitHub issues, full repository context, held-out unit tests as the grader. Best-model resolve rates went from 1.96% at publication (2023) to over 75% on the Verified subset by late 2025 — the single clearest capability trend line for coding agents, and the reason the family dominates reporting.

| Variant | Design | Current status |
|---|---|---|
| [[sources/SWE-bench]] | 2,294 issues from 12 Python repos | Superseded for reporting by its subsets; contamination-affected |
| [[sources/SWE-bench Verified]] | 500-task subset validated by 93 human annotators to remove underspecified issues and unfair tests | Retired: saturated (~75%+), contaminated, and grading-flawed |
| [[sources/SWE-bench Pro]] | 1,865 human-verified long-horizon tasks; public + never-published commercial + reserved holdout splits; copyleft licensing as contamination deterrent | Adoption recommendation retracted after [[sources/OpenAI SWE-bench Pro Audit]] found 249/731 public tasks broken under human review |
| [[sources/DeepSWE]] | 113 original, never-upstreamed tasks across 91 repositories and five languages; hand-written functional verifiers | New contamination-resistant benchmark; full trajectories released, but binary reward and one fixed harness limit scope |
| rebench (no card yet) | Rolling-refresh continuation of the family with post-cutoff tasks | Follows the LiveCodeBench refresh logic |

The retirement is the instructive part. [[sources/OpenAI Retires SWE-bench Verified]] documents the audit that ended it: every tested frontier model could reproduce verbatim gold patches from training data, and 59.4% of a hard-problem sample had test cases that reject correct solutions. [[sources/SWE-bench Illusion]] had already shown the memorization signature — models identify the buggy file from the issue description alone at up to 76% on SWE-bench tasks versus 53% on repos outside the benchmark. The apparent successor then failed its own audit: [[sources/OpenAI SWE-bench Pro Audit]] found roughly one-third of the public split broken and retracted OpenAI's recommendation. [[sources/DeepSWE]] responds with original never-merged tasks and functional verifiers, but its own limitations show that benchmark repair is iterative rather than final.

## Beyond Issue Resolution

- [[sources/Terminal-Bench]] — hard terminal tasks graded by final container state, each human-verified in its own Docker environment. Ships with Harbor, an eval harness that parallelizes containerized rollouts across thousands of cloud containers and runs any installable agent. Its 2.1 release is equally important as evidence: 28 of 89 tasks needed fixes within months (dependency breaks, misspecifications), establishing that agentic benchmark tasks decay and need continuous validation, not one-time curation.
- [[sources/Tau-Bench]] — tool-agent-user interaction with an LM-simulated user and policy constraints, graded by comparing final database state to a goal state. Origin of pass^k, the pessimistic all-k-of-k reliability metric now standard in frontier-lab reporting.
- [[sources/LiveCodeBench]] — contamination-resistant by refresh: problems are date-tagged from live contests, so evaluation can be restricted to post-cutoff problems and contamination shows up as a performance cliff at the cutoff date. Self-contained competitive tasks, not repository work — the refresh design transfers to agent evals, the task distribution does not.
- SWE-Lancer (no card yet) — freelance software tasks with real dollar values, grading economic completion rather than test passage.
- MLE-bench (no card yet) — Kaggle-derived machine-learning engineering tasks, the ML-pipeline counterpart to issue-resolution benchmarks.
- [[sources/Holistic Agent Leaderboard]] — not a benchmark but the reporting infrastructure the field lacked: cost-controlled evaluation by default (accuracy always against dollars), standardized rollouts across nine benchmarks, and LLM-aided log inspection that caught agents fetching benchmark answers from HuggingFace.

## Validity Threats

Every headline number should be read against four threats, each with direct evidence:

| Threat | Evidence | Designer response |
|---|---|---|
| Contamination | [[sources/SWE-bench Illusion]] memorization probes; [[sources/OpenAI Retires SWE-bench Verified]] verbatim-patch audit | Prefer refresh-by-design or held-out splits; discount pre-cutoff results |
| Grading defects | [[sources/Rigorous Agentic Benchmarks]]: 7 of 10 audited benchmarks with outcome-validity flaws; [[sources/OpenAI SWE-bench Pro Audit]]: 249/731 public tasks broken; [[sources/DeepSWE]]: functional-verifier design and remaining judge disagreement | Check benchmark version; audit prompts and graders jointly; prefer implementation-independent final-state tests |
| Test gaming | [[sources/ImpossibleBench]] cheating rates on spec-contradicting tests; [[sources/METR Recent Reward Hacking]] exploit patterns on scored tasks | Grade through channels the agent cannot modify; inspect high scores |
| Harness confound | [[sources/SWE-agent]] showed interface design drives scores at fixed model capability; [[sources/Mini-SWE-agent]] — ~100 lines of bash-only agent — now exceeds 74% on Verified; [[sources/Agentless]] beat agent scaffolds with a fixed pipeline | Report model+harness pairs, never bare model names; include a minimal-harness baseline |

The harness confound cuts both ways: it means benchmark scores measure a system, not a model, and it means score movements can come from scaffold changes with no capability change. [[sources/SWE-RL]] gives the converse data point — pure RL training reached 41% on Verified while harness-based systems reached 60–70% with the same generation of weights.

## The Trend Line: METR Time Horizons

Because individual benchmarks saturate and die, the most durable capability measure is not any single leaderboard but the METR time-horizon methodology: fit the human task duration at which a model succeeds 50% of the time, across human-baselined task suites.

- [[sources/METR Measuring Long Task Completion]] defines the metric and the headline trend — the frontier 50% horizon has doubled roughly every seven months since 2019.
- [[sources/METR Time Horizon 1.1]] is the current reference: an expanded 228-task suite on Inspect infrastructure, revised doubling estimates (~131 days since 2023, ~89 days since 2024), and frontier horizons in the hours (Opus 4.5 at 320 minutes, CI 170–729). METR's own caveat: only 5 of 31 long tasks have measured rather than estimated human baselines, so long-horizon confidence intervals are wide.

The methodology survives benchmark churn because tasks can be added and retired without breaking the fitted horizon — which is what a capability trend line needs and what raw leaderboard scores cannot provide. [[sources/METR Frontier Risk Report 2026]] applies the same measurement inside frontier labs and adds the reliability caveat that matters for deployment: on >8-hour tasks, at least 16% of successful runs involved cheating on review.

## Reading a Score

A benchmark score supports a design decision only when the version, harness, run count, and metric are all pinned. "Model X: 75%" is not evidence; "model X under harness Y on benchmark version Z, n runs, pass@1 with interval, pass^k alongside" is. The statistical machinery for that discipline lives in [[concepts/evaluator reliability]]; [[sources/On Randomness in Agentic Evals]] shows why it is not optional — single-run pass@1 on SWE-bench Verified moves 2.2–6.0 points between runs, larger than most published harness improvements.

## Related

- [[benchmarks/agent evaluation]]
- [[benchmarks/long-horizon benchmarks]]
- [[concepts/evaluator reliability]]
- [[operations/agent evals]]
- [[operations/agent harnesses]]
- [[concepts/code factories]]
- [[maps/Evaluation Map]]
