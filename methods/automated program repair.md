# Automated Program Repair

Automated program repair (APR) is the pipeline that turns a failure signal — a failing test, a crash, a machine-filed bug, a production error group — into a validated candidate patch. In a code factory it is the maintain-and-debug stage: the factory generates change volume, change volume generates failures, and APR is what keeps that feedback from landing on human queues.

The method predates LLMs. Facebook's SapFix and Getafix (2018-2019) mined fix templates from history and attached them to crash signals. The current generation replaces templates with models but keeps the same economic structure: cheap candidate generation, expensive validation, and a hard gate before anything reaches a human.

## Pattern

```text
failure signal -> abstain or accept -> reproduce -> localize -> generate patches -> validate -> select one -> human review
```

## Approaches

| Approach | Mechanism | Evidence |
|---|---|---|
| Fixed pipeline | Staged localization, repair, validation; no autonomous action decisions | [[sources/Agentless]]: a three-phase pipeline beat all open-source agent scaffolds on SWE-bench Lite at $0.70 per issue |
| Agentic repair | Tool-using agent iterates on execution feedback | [[sources/SWE-agent]]: interface design drives repair performance more than prompting; [[sources/Passerine]]: SWE-agent-style repair inside Google's issue tracker; [[sources/Meta Agentic Program Repair]]: ReAct loop over static-analysis and test-execution feedback in production CI |
| Minimal harness | Bash-only loop, linear history | [[sources/Mini-SWE-agent]]: ~100 lines scoring over 74% on SWE-bench Verified — the control condition for scaffold complexity |
| Trained repair models | RL or fine-tuning on software-evolution data | [[sources/SWE-RL]]: patch-similarity reward on GitHub history reaches 41% SWE-bench Verified at 70B; [[sources/Meta Agentic Program Repair]]: a fine-tuned 70B was highly competitive with the much larger vanilla 405B |
| Triage-and-fix products | Error monitor scans, scores, and drafts fixes | [[sources/Sentry Seer]]: scan every issue, score actionability, optionally draft PRs |

The pipeline-versus-agent choice is a real design decision, not a maturity ladder. [[sources/Agentless]] shows that removing the model's freedom to choose actions can beat elaborate scaffolds when the task shape is known; [[sources/Mini-SWE-agent]] shows that as models improve, much of the remaining scaffold value is in the validation gates, not the interface machinery.

## Design Guidance

**Select targets by signal quality, not by backlog order.** [[sources/Passerine]] found machine-reported bugs (sanitizers, fuzzers) nearly three times more tractable than human bug reports — 73% versus 25.6% plausible-patch rate. A factory should point APR at its machine-generated failure stream first and treat human reports as a harder, later tier.

**Reproduce before repairing.** Google's BRT Agent follow-up ([[sources/Passerine]]) raised the plausible-fix rate from 57% to 74% just by feeding an auto-generated bug-reproduction test as the starting input. A failing test is both the localization signal and the validation oracle; without one, "fixed" is unfalsifiable.

**Budget for abstention and single-candidate review.** [[sources/Passerine]] forwards at most one patch per bug to review, after explicit bug abstention. Sending humans a ranked list of candidate patches converts a review gate into a triage task and burns the scarcest resource in the loop.

**Treat "plausible" as a claim about tests, not correctness.** In [[sources/Passerine]], only 43% of machine-reported bugs got a patch semantically equivalent to ground truth despite 73% passing tests. The gap between test-passing and correct is where patch overfitting lives, and it is exploitable: [[sources/ImpossibleBench]] measures how readily agents modify or game tests that contradict the spec, and [[sources/METR Recent Reward Hacking]] documents evaluator-gaming in the wild. Repair agents should not have write access to the tests that validate them.

**Gate with a judge before humans, but calibrate expectations.** [[sources/Meta Agentic Program Repair]] runs an LLM-as-judge against human-review standards before a diff reaches engineers; even so, only 25.5% of published diffs landed over a three-month production trial. That number is the sober baseline for CI-repair throughput, not the 40-70% benchmark solve rates.

## Test Generation Is the Other Half

Repair is only as strong as the suite that validates it, so factories that deploy APR usually deploy test generation alongside it.

- [[sources/TestGen-LLM]] defines the filter-cascade pattern: a generated test reaches humans only if it builds, passes reliably on repeated runs, and measurably increases coverage — 73% of surviving recommendations were accepted by Meta engineers.
- [[sources/ACH Mutation-Guided Test Generation]] replaces coverage with fault detection: generate mutants that simulate a stated concern, then generate tests proven to kill them. Mutation gating is the stronger adequacy criterion, and it also hardens the repair loop — a suite that kills mutants is harder for an overfitted patch to slip through.

## Flaky-Test Management

Flaky tests poison every stage of this loop: they generate false repair targets, they invalidate the "passed reliably" gate, and they eject innocent changes from merge queues ([[sources/GitHub Merge Queue Docs]]: a CI failure removes the PR and forces retest of everything behind it). The repeated-run reliability filter in [[sources/TestGen-LLM]] is the minimum defense — a test that does not pass deterministically never enters the suite. For existing suites, quarantine flaky tests before enabling CI-failure repair; an agent iterating on nondeterministic signal ([[sources/Meta Agentic Program Repair]] averaged 11.8 feedback iterations per fix) wastes its budget chasing phantom failures and erodes reviewer trust in the diffs it does publish.

## Benchmark Caveats

SWE-bench-family scores transfer poorly to factory planning. [[sources/SWE-bench Illusion]] shows frontier models locate buggy files from issue text alone at up to 76% on SWE-bench versus 53% elsewhere — memorization inflates headline rates. [[sources/Passerine]] shows enterprise bug distributions differ from SWE-bench in language, size, and change spread. Calibrate on your own failure stream; the Meta and Google production numbers above are better priors than leaderboard scores.

## Related

- [[concepts/code factories]]
- [[operations/release engineering]]
- [[operations/incident response]]
- [[concepts/issue tracker control plane]]
- [[methods/self-improving code loops]]
- [[operations/agent evals]]
- [[concepts/outcomes and rubric graders]]
