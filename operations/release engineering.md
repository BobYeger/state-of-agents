# Release Engineering

Release engineering is the set of controls between a merged change and full production exposure: merge serialization, deployment automation, progressive exposure, and rollback. In a code factory it is the backpressure stage — the mechanism that decides how fast agent-generated change volume reaches users, and that pushes failure signal back upstream when stability drops.

This stage matters more, not less, when agents write the code. [[sources/DORA State of AI-assisted Software Development 2025]] reports the first year in which AI adoption correlates positively with delivery throughput — while still correlating with worse stability unless automated testing, small batches, and fast feedback are in place. Generation stages raise volume; release engineering is where that volume is either absorbed safely or converted into change failures.

## Pattern

```text
reviewed PR -> merge queue -> build -> canary population -> progressive rollout -> full exposure
                   |                        |                       |
                requeue                 rollback                flag off
```

## Controls

| Control | Mechanism | What it gives the factory |
|---|---|---|
| Review gate | human, AI, or tiered approval before the queue | the last point where intent is checked, not just behavior |
| Merge queue | PRs grouped and tested against the true post-merge state; failures ejected and the rest retested ([[sources/GitHub Merge Queue Docs]]) | serialized integration with tunable concurrency and batch size |
| Canary release | partial, time-limited deployment evaluated against a control population ([[sources/Google SRE Workbook Canarying Releases]]) | bounded blast radius with explicit error-budget math |
| Feature flags | decouple feature exposure from binary deployment | rollback without redeploy; per-cohort exposure |
| Progressive rollout | staged population growth with metric gates per stage | strict crash/failure gates early, looser gates later |
| Deployment rollback | revert the artifact or flip the flag | recovery time bounded by the pipeline, not by repair speed |

## Design Guidance

**Size the review gate for agent volume, and audit who is reviewing.** The human baseline is narrow: at Google, the median developer reviews about four changes a week, and review scales only because the median change is 24 lines with a single owner-reviewer ([[sources/Modern Code Review at Google]]). Agent PR volume exceeds that ceiling quickly, and the observed failure mode is silent: most agent-authored PRs in open source receive no review activity at all, and when they are reviewed, the reviewer is usually another agent ([[sources/How Humans Review AI-Generated Pull Requests]]). A factory that wants tiered AI approval should copy the deployed shape: decomposed reviewer agents for intent-alignment, safety, and correctness, a hard size gate that refuses large diffs, and every AI approval labelled and queryable — [[sources/Intercom AI Approving Pull Requests]] runs this at 19.2% of PRs auto-approved with a 0.53% revert rate on AI-authored backend code, versus 5.39% for human-authored.

**Treat the merge queue as admission control.** The queue's knobs are the factory's throughput levers: build concurrency (1-100), minimum/maximum batch size, and a wait timeout for quiet periods ([[sources/GitHub Merge Queue Docs]]). Two costs deserve explicit budgeting. A CI failure ejects the failing PR and forces retest of everything behind it, so flaky tests tax the whole queue, not one change — quarantine them before scaling PR volume (see [[methods/automated program repair]] on flaky-test management). And priority interrupts ("jump the queue") force a full rebuild of all in-flight merge groups; frequent expediting makes the queue slower for everyone.

**Canary with population comparison, not before/after.** The canary methodology in [[sources/Google SRE Workbook Canarying Releases]] is directly reusable for agent-produced changes: compare a canary population against a control population running the old version, gate on roughly a dozen metrics that are tied to SLIs and attributable to the change, run one canary at a time to avoid signal contamination, and size the canary with error-budget math — a 20% error-rate change on a 5% canary costs 1% overall, the same change at 100% burns the budget immediately. Time-based before/after comparison confuses the change's effect with everything else that moved.

**Use feature flags to separate deploy risk from launch risk.** The workbook recommends flags to decouple feature launches from binary releases. For a factory this creates two independent rollback surfaces: a bad binary rolls back through the pipeline, a bad feature flips off in seconds. Agent changes should default to landing behind flags when the change is user-visible.

**Read DORA metrics as backpressure, not as a scoreboard.** Throughput metrics (deployment frequency, lead time) measure what the factory's generation stages produce; stability metrics (change failure rate, time to restore) measure what its verification stages catch. When stability degrades, the correct response is to slow intake or raise gates, not to ship faster. [[sources/DORA ROI of AI-assisted Software Development]] names the expected transient: a J-curve where verification overhead and downstream absorption of increased code volume depress delivery metrics before they improve — a factory that panics during the dip and removes gates converts the dip into instability.

## Deployment Rollback Is Not Candidate Rollback

A factory runs more than one kind of revert, and conflating them causes category errors in gate design.

| Rollback type | What is reverted | Trigger evidence | Owner |
|---|---|---|---|
| Deployment rollback | the running artifact or flag state | production telemetry: canary regression, SLO burn | release pipeline |
| Self-improvement-candidate rollback | a change to what future agent runs execute: harness, scaffold, skill, prompt, workflow | evaluation evidence: benchmark or held-out regression | the improvement loop ([[methods/self-improving code loops]]) |
| Capability suspension | access to a model or agent surface | safety or governance finding | vendor or regulator ([[sources/Redeploying Claude Fable 5]]: a government-ordered takedown and restore of a frontier model over an 18-day window) |

The first is about user exposure and is gated on production telemetry. The second is about the factory's own future behavior and is gated on evaluator evidence, which is weaker — evaluator hacking and overfitting to the validation set have no production-telemetry equivalent. [[sources/Harness Updating Is Not Harness Benefit]] adds a subtlety for the second type: the benefit of a harness change depends on which model executes under it, non-monotonically in capability, so a candidate validated under one model needs revalidation when routing changes. Candidate keep/revert decisions should key on the (change, executor) pair, not the change alone.

## Related

- [[concepts/code factories]]
- [[operations/incident response]]
- [[methods/automated program repair]]
- [[concepts/issue tracker control plane]]
- [[methods/self-improving code loops]]
- [[operations/agent observability]]
- [[operations/agent evals]]
- [[concepts/human-in-the-loop agents]]
