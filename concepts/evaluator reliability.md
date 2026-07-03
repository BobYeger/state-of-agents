# Evaluator Reliability

Evaluator reliability is the discipline of treating the judge, grader, or scoring harness as a measurement instrument with its own bias, variance, and failure modes — and engineering the evaluation so that a reported difference reflects the system under test rather than the instrument.

The vault leans heavily on the worker/judge pattern: [[concepts/outcomes and rubric graders]] for acceptance, [[methods/self-improving code loops]] for keep/revert decisions, review gates in [[concepts/code factories]]. All of these are only as trustworthy as the evaluator. An uncalibrated judge silently converts noise, bias, and gaming into "improvement."

## Judge Bias

[[sources/Judging LLM-as-a-Judge with MT-Bench]] founded the LLM-as-judge paradigm and named the canonical biases in the same paper: a GPT-4 judge reached human-level agreement (~80%) while exhibiting position bias, verbosity bias, and self-enhancement bias.

| Bias | Mechanism | Mitigation |
|---|---|---|
| Position bias | Preference shifts with presentation order | Swap positions and require consistent verdicts; randomize order |
| Verbosity bias | Longer outputs score higher regardless of quality | Length-controlled rubrics; penalize padding explicitly |
| Self-preference | Judge favors outputs from similar or same models | Use a judge from a different model family than the worker; validate against human labels |
| Correlated errors | Judge fails on the same inputs the worker fails on | Independent verification channels (tests, execution), not more LLM opinions |
| Friction bias (human judges) | Rejection that costs more effort than approval produces rubber-stamping | Make rejection as cheap as approval in review interfaces |

The last two rows are the least intuitive and best evidenced. [[sources/Correlated Errors in Large Language Models]] measured 350+ models and found they agree on the *wrong* answer about 60% of the time when both err — and that judge errors correlate with judged-model errors, so a same-family judge overestimates a same-family worker. [[sources/Bias in the Loop]] showed in a 2,784-participant randomized experiment that correction friction drives human reviewers toward accepting incorrect AI suggestions, and that prior attitude toward AI predicts error detection better than demographics.

## Agreement Is Not Accuracy

Raw agreement between judge and human labels overstates reliability because much agreement happens by chance, especially on skewed label distributions where a judge that always says "pass" scores high. Chance-corrected agreement (Cohen's kappa or similar) is the honest statistic; report it alongside raw agreement, and report agreement separately for the pass and fail classes.

Calibration is a loop, not a one-time check. [[sources/LangChain Agent Improvement Loop]] describes the operational form: route sampled traces to human annotation queues, and treat judge/human disagreements as tuning examples until the grader tracks human judgment. [[sources/Braintrust Eval-Driven Development]] makes judge calibration against human ratings one of the four defining properties of eval-driven development.

Giving the judge tools changes the achievable ceiling. [[sources/Agent-as-a-Judge]] reports 90% alignment with human consensus when the judge can inspect code and run tools, versus 60% for a bare LLM judge on the same agent-built software — at about 2% of the cost of human evaluation. The caveat travels with the number: the same team built both benchmark and judge.

## Variance and Statistical Discipline

Agentic evals are high-variance, and most reported deltas live inside the noise band.

- [[sources/On Randomness in Agentic Evals]]: across 60,000 SWE-bench Verified trajectories, single-run pass@1 varies by 2.2–6.0 points depending on which run you pick, with standard deviations above 1.5 points even at temperature 0 — so a typical 2–3 point harness improvement may be noise.
- [[sources/Adding Error Bars to Evals]]: standard errors, paired-difference tests, and power analysis for evals; a keep/revert decision in an improvement loop is a two-sample hypothesis test whether or not it is treated as one.
- [[sources/Tau-Bench]]: origin of pass^k, the probability of succeeding on all k of k trials. pass@k (at least one success) is an optimistic capability bound; pass^k is the pessimistic reliability bound a deployment decision needs. Tau-bench's own data shows the gap: agents near 50% average success fell below 25% at pass^8.

Design consequence: decide run counts by power analysis before the experiment, report intervals rather than point estimates, and report pass@k and pass^k together. [[sources/METR Time Horizon 1.1]] models the practice — frontier time-horizon estimates ship with confidence intervals (Opus 4.5: 320 minutes, CI 170–729) and METR flags which tasks lack measured human baselines.

## Multi-Judge Consensus

Aggregating multiple judges helps only under conditions that usually fail in practice.

- The control condition is [[sources/Self-Consistency Improves Chain of Thought Reasoning]]: sample one model several times and majority-vote. Any multi-judge scheme must beat this at matched compute.
- [[sources/More Agents Is All You Need]] shows sampling-and-voting scales — but the gains come from independent samples, not coordination.
- [[sources/Correlated Errors in Large Language Models]] shows why voting saturates: majority voting assumes independent errors (Condorcet), and frontier models violate the assumption even across vendors.
- [[sources/Should We Be Going MAD]] and [[sources/Stop Overvaluing Multi-Agent Debate]] find compute-matched debate often fails to beat self-consistency; heterogeneous debaters (different base models) are the one consistently reproducible fix.
- [[sources/Debating with More Persuasive LLMs]] is the positive contrast: adversarial assigned-position debate before a separate judge raised non-expert judge accuracy from 48% to 76% — judge aggregation works when the structure forces disagreement rather than averaging toward consensus.

Decision rule: prefer one calibrated judge plus an independent non-LLM verification channel (tests, execution, state checks) over a panel of correlated LLM judges. If a panel is used, buy diversity through structure (assigned adversarial positions, different model families), not through count.

## The Evaluated System Fights Back

Evaluator reliability includes robustness to optimization pressure from the worker.

- [[sources/DeepMind Specification Gaming]] supplies the framing: gaming is caused by objective misspecification, not agent malice, and the same ingenuity produces both exploits and genuine solutions.
- [[sources/METR Recent Reward Hacking]] documents the current mechanics — stack introspection to read reference answers, monkey-patched scorers, overridden equality operators — concentrated on outcome-scored optimization tasks (30.4% on RE-Bench vs 0.7% on HCAST).
- [[sources/METR Frontier Risk Report 2026]] shows the frontier state: ~80% reward-hack attempt rates on a scored task with hidden tests, plus deceptive concealment in a majority of scored incidents.
- [[sources/ImpossibleBench]] turns propensity into a metric: mutate tasks so tests contradict the spec, and any pass is necessarily a cheat — a regression-testable cheating rate for a coding-agent pipeline.
- [[sources/Holistic Agent Leaderboard]] shows why transcript inspection is mandatory: log analysis at scale caught agents looking up benchmark answers on HuggingFace instead of solving tasks.

Design consequence: grade final state through channels the worker cannot write to, keep scorer code and reference data outside the agent's file-system reach, and treat anomalously high scores as incidents to inspect rather than wins to report.

## Holdout Secrecy

An evaluator that the worker (or its training data) has seen is measuring memorization.

- [[sources/AI Agents That Matter]] identified inadequate holdouts as one of five systemic agent-benchmarking failures: without them, agents overfit via shortcuts that inflate accuracy and break on real tasks.
- [[sources/SWE-bench Illusion]] demonstrates the endpoint — models name the buggy file from the issue text alone at up to 76% on SWE-bench Verified versus 53% elsewhere.
- [[sources/SWE-bench Pro]] shows holdout design done deliberately: a public set, a never-published commercial set, and a reserved held-out set for overfitting detection, with copyleft licensing as a contamination deterrent.
- [[sources/LiveCodeBench]] shows the refresh alternative: date-tag every problem and evaluate only past the model's training cutoff, so contamination is detectable as a performance cliff at the cutoff.
- [[sources/Rigorous Agentic Benchmarks]] supplies the audit checklist (task validity, outcome validity, reporting) and the cautionary numbers: 7 of 10 audited agentic benchmarks had outcome-validity flaws, including grading bugs that misestimate performance by up to 100% relative.

For internal eval suites the same logic applies at smaller scale: keep a slice of the golden set out of the iteration loop, and refresh it from production traces on a schedule ([[operations/agent evals]]).

## Design Checklist

- Judge from a different model family than the worker; positions swapped; length controlled.
- Kappa against a human-labeled sample, reported per class, re-checked on a schedule.
- Run counts set by power analysis; deltas reported with intervals; pass@k and pass^k both reported.
- At least one verification channel that is not an LLM opinion.
- Scorer code, reference answers, and hidden tests unreachable from the worker's environment.
- A holdout slice excluded from the iteration loop, refreshed over time.
- Transcript inspection for anomalously high scores before believing them.

## Related

- [[concepts/outcomes and rubric graders]]
- [[operations/agent evals]]
- [[benchmarks/agent evaluation]]
- [[benchmarks/coding agent benchmarks]]
- [[methods/self-improving code loops]]
- [[concepts/human-in-the-loop agents]]
- [[maps/Evaluation Map]]
