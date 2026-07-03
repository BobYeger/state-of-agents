# Agent Evals

Agent evals are the operational evaluation strategy of a deployed agent system: what gets measured, when a change must be re-measured, and what evidence a ship-or-revert decision requires. The benchmark notes ([[benchmarks/agent evaluation]], [[benchmarks/coding agent benchmarks]]) cover the public capability record; this note covers running an evaluation pipeline for a system you own.

The operating premise comes from [[sources/Anthropic Demystifying Agent Evals]]: tool use, state changes, autonomy, and multi-turn recovery make agent evaluation categorically harder than static model evaluation, so the pipeline has to grade trajectories and end states, not single completions.

## Offline and Online Halves

A production eval strategy has two halves that share graders but differ in everything else. [[sources/LangSmith Evaluation Concepts]] draws the split explicitly and it generalizes past any one platform:

| Half | Runs against | Reference outputs | Answers the question |
|---|---|---|---|
| Offline | Curated datasets (golden sets, regression suites, benchmarks) as pre-deployment batch jobs | Yes — labeled expected outputs or acceptance criteria | Did this change make the system better or worse than the baseline? |
| Online | Live production traces, sampled or exhaustive, in near real time | No — reference-free checks: safety, format, heuristics, reference-free judges | Is the deployed system degrading, and on which traffic? |

The offline half needs three patterns for a promotion pipeline: regression testing against a pinned baseline, backtesting a new version against historical production inputs, and pairwise comparison when direct scoring is hard ([[sources/LangSmith Evaluation Concepts]] names all three). [[sources/Inspect Framework]] is the reference pattern library for this half — datasets, solvers, and scorers composed so that every run emits a full transcript that scorers can grade end to end, with sandbox backends for untrusted agent code; it deliberately has no online half.

Neither half substitutes for the other. Offline evals catch regressions before exposure but only on the distribution you thought to curate; online telemetry catches drift on real traffic but cannot compare against references. The bridge between them is the trace-to-dataset loop below.

## Trace-Derived Regression Suites

The most valuable eval cases are not authored — they are harvested. A production failure that gets labeled and added to the golden set becomes a permanent regression test: that failure mode can never silently return.

- Sampling triggers: negative user feedback, heuristic flags (latency spikes, errors), and LLM-detected significant conversations are the three standard triggers for routing a production trace into a dataset ([[sources/LangSmith Evaluation Concepts]]).
- Conversion paths: reviewers either label a ground-truth correct output, or — for open-ended tasks with no exact answer — label the quality criteria the output should satisfy, enabling criteria-based grading ([[sources/LangChain Agent Improvement Loop]] formalizes both inside a seven-stage improvement loop).
- Growth policy: golden sets are append-mostly and grow as production reveals edge cases, which is what makes the regression gate strengthen over time rather than staying frozen at launch coverage ([[sources/Braintrust Eval-Driven Development]]).

Fidelity of the replayed case is a design decision of its own. [[sources/Datadog Bits AI Eval Platform]] pairs each ground-truth label with a "world snapshot" — the archived signal state available at the time of the original incident — so the agent replays against realistic conditions rather than curated fixtures, and deliberately injects tangentially-related noise: the noisy dataset scored 11% lower but predicted production performance better. The complementary approach is curated fault injection — [[sources/AIOpsLab]] deploys live Kubernetes microservices and injects controlled faults, buying difficulty control at the cost of sampling from a synthetic rather than production incident distribution. Choose replay when the goal is predicting production behavior, injection when the goal is coverage of failure classes production has not yet produced.

## Eval Gating of Harness Changes

Prompts, tools, context policy, and model routing all change agent behavior, so every harness change is a candidate that must pass gates before exposure — the same discipline [[methods/self-improving code loops]] applies to agent-proposed changes applies to human-proposed ones.

[[sources/Braintrust Eval-Driven Development]] gives the staged shape: development runs a fast subset for iteration speed, staging requires the full suite on the complete golden set, production adds safety and compliance evals, and CI blocks automatically when any metric falls below threshold at any gate. The final gate is a canary that routes partial live traffic to the new version and scores it with the same criteria used offline — the agent-era instance of the methodology in [[sources/Google SRE Workbook Canarying Releases]], which supplies the pre-LLM discipline: population-isolated (not before/after) comparison, roughly a dozen SLI-tied metrics, strict metrics gating small early stages.

This works in practice: the Datadog platform caught a change that expanded service names into context and degraded unrelated scenarios — exactly the class of regression no code review would flag ([[sources/Datadog Bits AI Eval Platform]]).

Two maintenance obligations come with the gate:

- The suite itself decays. [[sources/Terminal-Bench]] had to fix 28 of 89 tasks within months of release — dependency breaks, hardware mismatches, misspecifications — and one agent gained +12.1% purely from task fixes. Internal suites rot the same way; schedule validation passes and pin suite versions so scores stay comparable.
- Graders are code and need audits. [[sources/Rigorous Agentic Benchmarks]] found outcome-validity flaws in 7 of 10 audited agentic benchmarks, with grading bugs misestimating performance by up to 100% relative — a gate built on a buggy grader blocks the wrong changes and passes the wrong ones.

## Judge Calibration

Wherever a gate's grader is an LLM judge, the judge is a measurement instrument with its own bias and variance; [[concepts/evaluator reliability]] is the full treatment. The operational minimum:

- Calibrate against human labels on a schedule, not once. Route sampled traces to annotation queues and treat judge/human disagreements as tuning examples until the grader tracks human judgment ([[sources/LangChain Agent Improvement Loop]]). [[sources/Braintrust Eval-Driven Development]] makes this calibration one of the four defining properties of eval-driven development.
- Raise the ceiling with tools before adding judges. [[sources/Agent-as-a-Judge]] reports 90% alignment with human consensus when the judge can inspect code and execute tools, versus 60% for a bare LLM judge on the same outputs, at about 2% of human-evaluation cost.
- Keep at least one verification channel that is not an LLM opinion — tests, execution, final-state checks — because judge errors correlate with worker errors ([[concepts/evaluator reliability]] has the evidence).

## Statistics Discipline

Agentic evals are high-variance, and most reported deltas live inside the noise band.

- [[sources/On Randomness in Agentic Evals]] quantifies it: across 60,000 SWE-bench Verified trajectories, single-run pass@1 varies by 2.2–6.0 points between runs, with standard deviations above 1.5 points even at temperature 0 — so a typical 2–3 point harness improvement measured with one run is not evidence.
- [[sources/Adding Error Bars to Evals]] supplies the machinery: standard errors on eval scores, paired-difference tests for comparing two variants on the same cases, and power analysis to set run counts before the experiment rather than after.
- Report both reliability bounds. pass@k (at least one success in k) is the optimistic capability bound; pass^k (all k of k) is the pessimistic reliability bound a deployment decision needs — [[sources/Tau-Bench]] originated pass^k and showed agents near 50% average success falling below 25% at pass^8.
- [[sources/METR Time Horizon 1.1]] models the reporting standard: point estimates always shipped with confidence intervals, and explicit flags on which measurements rest on estimated rather than measured baselines.

The gate decision is a two-sample hypothesis test whether or not it is treated as one. Set run counts by power analysis, compare paired on the same cases, and report intervals — otherwise the gate ratifies noise.

## Cost and Transcript Inspection

Two disciplines from public benchmarking transfer directly to internal pipelines:

- Grade cost with accuracy. [[sources/AI Agents That Matter]] showed accuracy-only evaluation produces needlessly complex, costly agents and made the cost-accuracy Pareto frontier the correct target; [[sources/Holistic Agent Leaderboard]] operationalizes it by reporting accuracy against dollars by default — and found that higher reasoning effort reduced accuracy in the majority of its 21,730 rollouts, a result invisible to accuracy-only dashboards. That finding aggregates heterogeneous benchmarks and models, so the paper's per-task-type breakdowns are the citable unit, not the headline majority.
- Read transcripts before believing scores. HAL's LLM-aided log inspection caught agents fetching benchmark answers from HuggingFace instead of solving tasks ([[sources/Holistic Agent Leaderboard]]). Anomalously high scores are incidents to investigate, not wins to report — the gaming evidence lives in [[concepts/evaluator reliability]].

## Adjacent Eval Trails

Specialized evaluation lines that hang off this note rather than in it: skill evaluation ([[sources/OpenAI Eval Skills]] on evals as reusable skills, [[sources/SkillsBench]], [[sources/SkillOpt]], [[sources/Agentic Skills in the Wild]] — navigate via [[maps/Agent Skills Map]]); multi-agent evaluation ([[sources/MultiAgentBench]], [[sources/OpenRouter Fusion Beats Frontier]] on ensemble-vs-frontier comparisons); simulated-workplace tasks ([[sources/TheAgentCompany]]); and the academic survey baseline ([[sources/Evaluation and Benchmarking of LLM Agents - A Survey]]).

## Related

- [[maps/Evaluation Map]]
- [[concepts/evaluator reliability]]
- [[benchmarks/agent evaluation]]
- [[benchmarks/coding agent benchmarks]]
- [[benchmarks/long-horizon benchmarks]]
- [[concepts/outcomes and rubric graders]]
- [[methods/self-improving code loops]]
- [[operations/agent observability]]
- [[operations/cost control]]
- [[operations/release engineering]]
- [[concepts/code factories]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]
