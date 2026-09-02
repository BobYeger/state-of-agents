# Self-Improving Code Loops

Self-improving code loops are agent loops where the mutable artifact is executable code or an executable procedure, and the loop keeps changes only after external evidence improves.

This is a narrower pattern than [[concepts/loop engineering]]. A scheduled loop can simply rerun a prompt. A self-improving code loop mutates something that future runs will execute: an agent scaffold, harness, tool, workflow, algorithm, skill, or research codebase.

## Pattern

```text
candidate code/procedure -> run evaluator -> score/trace -> keep, branch, or revert -> next candidate
```

## Required Harness Pieces

- Editable code or procedure with a bounded action surface.
- Objective metric, test, benchmark, rubric, or reviewer.
- Sandboxed execution for generated code.
- Trace and provenance for every candidate.
- Selection, rollback, archive, or branching policy.
- Budget and stop policy.
- Guardrails against evaluator hacking and fake tool-use evidence.

## Subtypes

| Subtype | Artifact that improves | Examples |
|---|---|---|
| Self-editing agent scaffold | The agent's own tools, prompts, memory, workflow, or code | [[sources/Darwin Godel Machine]], [[sources/SICA Self-Improving Coding Agent]], [[sources/Huxley-Godel Machine]], [[sources/Hyperagents]], [[sources/Meta-Harness]] |
| Harness optimization | Context, retrieval, tools, completion checks, and model wrapper code | [[sources/Meta-Harness]], [[sources/AFlow]], [[sources/ADAS]], [[sources/Self-Harness]], [[sources/HarnessFix]], [[sources/Adaptive Auto-Harness]], [[sources/Retrospective Harness Optimization]], [[sources/Evo-Bench]] |
| Algorithm evolution | Candidate algorithms or programs | [[sources/AlphaEvolve]], [[sources/LoongFlow]] |
| Autonomous research code | Experimental code, hypotheses, figures, and papers | [[sources/The AI Scientist-v2]], [[sources/Karpathy Autoresearch]] |
| Skill/procedure evolution | Reusable skills, rules, or trajectory memories | [[sources/SkillOpt]], [[sources/WikiSkill]], [[sources/Metis]], [[sources/Voyager]], [[sources/SAGE Skill Library]], [[sources/SkillRL]], [[sources/Cursor Bugbot Learned Rules]] |
| Co-evolving evaluators | Agent and evaluator improve together under explicit epoch or utility controls | [[sources/Red Queen Godel Machine]] |

## Selection Policy

The keep/branch/revert decision is where these loops differ most, and the lineage of results reads as successive corrections to the previous policy.

| Policy | Mechanism | Evidence | Known failure |
|---|---|---|---|
| Greedy hill-climb over an archive | Each iteration resumes from the highest-utility archived version | [[sources/SICA Self-Improving Coding Agent]]: 17% to 53% on a SWE-bench Verified subset with utility combining score, cost, and runtime | Converges on local optima; discards stepping stones that score poorly but parent well |
| Open-ended archive (quality-diversity) | Keep a growing archive of all viable agents; branch from any member, not only the best | [[sources/Darwin Godel Machine]]: 20% to 50% on SWE-bench, explicitly outperforming its own greedy ablation | Compute-hungry — the archive multiplies evaluation cost; still selects parents by their own score |
| Clade-based (metaproductivity) | Expand the self-modification tree by descendants' aggregated performance, not the candidate's own score | [[sources/Huxley-Godel Machine]]: names the Metaproductivity-Performance Mismatch — an agent's own benchmark score is a poor signal for whether it is a good parent — and reaches better agents at 2.38x fewer CPU-hours than DGM | Needs enough descendants per node to estimate clade quality; cold-start is greedy anyway |
| Pareto frontier per instance | Sample candidates from the Pareto frontier of per-instance scores, preserving complementary strengths instead of one global best | [[sources/GEPA Reflective Prompt Evolution]]: frontier sampling avoids premature convergence and beats single-best iteration and MIPROv2 | Frontier can bloat on noisy evaluators; per-instance scores must be trustworthy |

The design reading: aggregate score alone is a bad parent-selection signal, so keep per-instance results, and budget for an archive rather than a single champion. All four policies inherit the measurement problem in [[concepts/evaluator reliability]] — a selection policy applied to a noisy evaluator selects for noise.

## Evaluating Harness Evolution

[[sources/Evo-Bench]] turns harness evolution itself into a benchmark: an evolver edits a shared executable policy harness using 160 visible validation tasks and up to 20 formal evaluations, then one frozen revision is evaluated on 448 held-out tasks across Search, Office, and General-agent domains. Keeping the policy model fixed within a run separates gains in the surrounding procedure from gains due to swapping the worker model.

The best reported evolver improves the seed harness by 16.6 points and approaches a composite human-engineered baseline. Separate evolution reruns under two evolvers and three policy models improve each policy's own CodeAct baseline; they do not transplant one frozen harness between models. The result also exposes the control problem: improvement varies sharply by domain, can saturate early, and does not increase monotonically with additional iterations. Because main configurations have one run, some grading is model-based, and task construction deliberately selects for harness sensitivity, the benchmark supports “harness evolution is measurable and robust to these policy-model changes,” not a general claim that autonomous evolution matches human harness engineering.

## Provenance and Lineage

Selection policies beyond greedy are only implementable if the archive is a lineage tree, not a best-snapshot. Every candidate needs:

- A parent pointer and the mutation diff that produced it.
- The evaluator version and per-instance scores it was judged with.
- Full execution traces of its evaluation runs.

Each element is load-bearing somewhere in the evidence. Clade selection in [[sources/Huxley-Godel Machine]] requires aggregating scores over descendants, which requires the tree. Failure attribution in [[sources/HarnessFix]] works by tracing a failure to the responsible harness layer before proposing a repair. The objective-hacking cases in [[sources/Darwin Godel Machine]] were caught by reviewing traces of anomalously scored candidates — without traces, a hacked evaluator is indistinguishable from an improvement. And rollback after a bad keep decision requires knowing exactly which diff to revert. [[sources/Retrospective Harness Optimization]] extends the same discipline backward: past trajectories become the validation set, which only works if they were recorded with enough fidelity to re-score.

## Scaffold vs Weights

The same improvement loop can mutate text and code around a fixed model, or mutate the model itself with RL. The boundary is a design decision with direct evidence on both sides:

- [[sources/GEPA Reflective Prompt Evolution]]: reflective prompt evolution outperforms GRPO-based RL by 6% on average with up to 35x fewer rollouts — when the feedback is legible in language, text-space search is drastically more sample-efficient than gradient updates.
- [[sources/SWE-RL]]: rule-based rewards over software-evolution data train a 70B model to 41% on SWE-bench Verified and improve out-of-domain reasoning — weight updates capture capability that transfers beyond the training task, which no scaffold edit does.
- [[sources/SkillRL]]: the hybrid — agent weights and a hierarchical skill bank co-evolve, making skills trainable state rather than documentation.
- [[sources/Harness Updating Is Not Harness Benefit]]: the caution for the scaffold side — generating harness updates and benefiting from them are separate capabilities, and benefit is non-monotonic in model tier.

Decision criteria: scaffold-side improvement is inspectable (a diff), revertible (rollback), cheap per iteration, and portable across models — [[sources/Huxley-Godel Machine]]'s discovered agents transfer from GPT-5-mini to GPT-5 with performance intact. Weights-side improvement is warranted when the deficit is capability rather than procedure, and when rollout volume is affordable. The reward-hacking exposure differs in kind, not presence: scaffold loops hack the evaluator at run time and the hack is visible in traces; RL bakes the hack into the policy — [[sources/METR Recent Reward Hacking]] attributes measured hack rates to outcome-graded RL itself.

## Boundary Case: AI R&D Acceleration

[[sources/Anthropic When AI Builds Itself]] should sit next to this method without being collapsed into it. The article is not a paper about an agent directly editing its own scaffold under benchmark selection. Its value is showing the surrounding organizational loop: humans set goals and rubrics, Claude writes code, runs experiments, reviews defects, suggests next steps, and increases the amount of work that must be evaluated.

That is still important for self-improving-code research because it names the likely bottleneck shift. As code and experiment execution get cheaper, the hard harness problems become goal selection, evaluator quality, review throughput, provenance, permission boundaries, and governance.

## Why It Matters

This is the strongest emerging form of harness engineering because the harness is no longer only executing work. It is also exposing itself or adjacent executable artifacts to search.

The key safety distinction is evidence quality. A self-improving code loop is only as trustworthy as its evaluator, sandbox, provenance, and rollback policy. [[sources/Darwin Godel Machine]] is especially useful here because it reports both capability gains and objective-hacking failures.

The June 2026 harness-optimization papers push this method from research curiosity toward an engineering loop: mine failed trajectories, attribute failures to harness layers, propose bounded repairs, and validate against held-out or retrospective evidence before the change becomes reusable.

## Related

- [[maps/Self-Improving Systems Map]]
- [[concepts/loop engineering]]
- [[concepts/evaluator reliability]]
- [[safety/reward hacking]]
- [[operations/agent harnesses]]
- [[methods/agentic workflow search]]
- [[methods/runtime supervision]]
- [[operations/agent evals]]
- [[operations/sandboxes]]
- [[concepts/lifelong agent learning]]
- [[concepts/procedural memory]]
- [[sources/Anthropic When AI Builds Itself]]
- [[sources/Evo-Bench]]
