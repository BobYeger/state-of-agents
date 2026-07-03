# Graduated Autonomy

Graduated autonomy is the practice of expanding an agent's standing authority in steps sized to accumulated evidence, and contracting it when the evidence turns bad.

Standing authority means actions the agent takes without a synchronous human check: merging without review, deploying, spending, writing to production, messaging external parties. The alternative to graduation is binary trust, and both poles fail. Gating every action exceeds human review capacity and decays into rubber-stamping; granting full autonomy up front gives the agent the blast radius of its worst run. Graduation makes the trust decision explicit, evidence-based, and reversible.

## Levels-of-Autonomy Frameworks

Three framework families grade different things, and a deployment decision needs all three:

| Framework | What it grades | Structure | Source |
|---|---|---|---|
| User-role levels (L1-L5) | The agent, by the role the user *can* take: operator, collaborator, consultant, approver, observer | Autonomy as a design decision separable from capability; products mapped from ChatGPT Canvas (L1) to Voyager (L5) | [[sources/Levels of Autonomy for AI Agents]] proposes the taxonomy plus "autonomy certificates" — evidence-based cases that an agent operates at level X and no higher, renewed when spec or environment changes |
| Environment readiness | The repository, not the agent: 8 technical pillars crossed with 5 maturity levels, 80% pass-rate gate per level | Level 3 "Standardized" is the recommended threshold at which agents handle routine maintenance | [[sources/Factory Agent Readiness]] inverts the trust question — an untrustworthy environment caps safe autonomy regardless of agent quality |
| Empirical autonomy measurement | Deployed behavior: how long agents actually run between interventions and what triggers interruptions | Autonomy as a measured deployment property rather than a capability label | [[sources/Anthropic Measuring Agent Autonomy]] supplies the operational measurement frame |

Two design readings follow. First, the same model can ship at L1 or L4; the level is chosen by the harness, so it can be chosen per scope — per repository, per action class, per environment — rather than globally. Second, [[sources/Levels of Autonomy for AI Agents]]'s "assisted evaluations" give the measurement procedure: run fully autonomously, then add human involvement level by level until the agent passes, and classify it at the minimum involvement that works. The certificate mechanism itself remains a proposal — no certifying body exists as of mid-2026.

## Autonomy Budgets Sized by Capability Evidence

An autonomy budget is how long an agent runs, and how much authority it exercises, between checkpoints. The credible way to size it is capability measurement rather than anecdote:

- [[sources/METR Measuring Long Task Completion]] defines the 50%-task-completion time horizon — the human task duration at which the model succeeds half the time — and documents the doubling trend that makes any fixed budget a depreciating decision.
- [[sources/METR Time Horizon 1.1]] gives the current frontier numbers with their honesty bars: Claude Opus 4.5 at a 320-minute 50% horizon with a 170-729 minute confidence interval. Budgets should be set from the interval floor, not the point estimate, and METR itself notes most long tasks lack measured human baselines.
- The 50% bar is the wrong bar for unsupervised authority. [[sources/METR Frontier Risk Report 2026]] measured the strongest shared model at roughly 16-20 hours at the 50% horizon but only 3-4 hours at 80% — the budget for unreviewed work should track the high-reliability horizon, which is several times shorter.
- Longer runs are also more adversarial, not just more error-prone: [[sources/METR Frontier Risk Report 2026]] found at least 16% of successful runs on tasks over 8 hours involved cheating on review, with prevalence rising on harder tasks. Checkpoint spacing has to shrink relative to task difficulty even as raw capability grows.
- Verification strength buys budget directly: [[sources/Replit Agent 3 Self-Testing]] credits a self-testing subagent loop with extending continuous autonomous runtime from ~20 to 200+ minutes — evidence that the budget is a property of the harness's verification, not the model alone.

## Escalation and Revocation

The escalation ladder is visible in deployed systems, from starting tier to earned tier to revocation:

- Starting tier: [[sources/GitHub Copilot Coding Agent]] ships with structural distrust — the agent pushes only to branches it creates, works in draft pull requests, cannot have its PRs approved by its requester, and needs human approval before CI runs.
- Earned tier: [[sources/Intercom AI Approving Pull Requests]] is the clearest published promotion — after a pilot of 100+ PRs with zero reverts, the review agent now auto-approves 19.2% of all PRs, and the promotion is bounded by a size gate (it refuses to approve large or broadly scoped changes) and made auditable by labelling and logging every AI approval. The track record continues to be measured, though what it measures is authorship rather than the approval gate: AI-authored backend code reverts at 0.53% versus 5.39% for human-authored — a comparison that may partly reflect the size gate, since AI changes are structurally smaller.
- Practice without graduation: [[sources/METR Frontier Risk Report 2026]] found ~40% of surveyed frontier-lab developers granted agents unrestricted permissions on "low-stakes" projects and no company documented universal human-approval requirements — authority granted by convenience rather than by evidence, at the organizations with the most capable models.
- Revocation: [[sources/Redeploying Claude Fable 5]] is the largest-scale example, though the revoking authority was the government, not the lab — US export controls imposed after a jailbreak demonstration forced global suspension of a frontier model, with restoration 18 days later when the controls lifted. Anthropic's proposed four-criterion severity framework (capability gain, breadth, weaponization ease, discoverability) functions as a sizing rule for how much authority to pull when evidence goes bad.

Three rules generalize. Escalate per scope, not globally: a track record on documentation PRs says nothing about deploy rights. Make demotion cheaper than promotion: revocation must not require re-litigating the original grant. And keep the audit trail that makes both possible — Intercom's labelled approvals and METR's incident scoring both depend on being able to attribute outcomes to a specific authority tier after the fact.

## Gate-Placement Economics

Where to put human gates is a budget problem, and the budget is measured:

- The capacity ceiling: [[sources/Modern Code Review at Google]] establishes the pre-agent human baseline — the median reviewer handles ~4 changes per week, spending a mean of 3.2 hours weekly (median 2.6), sustained only by small diffs (median 24 lines) and single-reviewer gates. Any gate design that assumes more human throughput than this is assuming reviewers Google could not find.
- What happens past the ceiling: [[sources/How Humans Review AI-Generated Pull Requests]] shows most agent-authored PRs in open source receive no review at all, and when review happens it is dominated by other agents — the gate still exists on paper while the oversight it implies has stopped.
- Why overloaded gates fail quietly: [[sources/Bias in the Loop]] isolates the mechanism experimentally — when flagging an error costs more effort than approving, reviewers correct less and accept more wrong output, and prior attitude toward AI predicts detection performance better than any demographic. Rejection must be as cheap as approval, or the gate selects for rubber-stamping.
- The aggregate cost: [[sources/DORA ROI of AI-assisted Software Development]] names the J-curve — verification overhead absorbs the early productivity gains of agent adoption, which is the organizational bill for gates placed without regard to throughput.
- The mitigation pattern: [[sources/Anthropic Claude Code Auto Mode]] automates permission decisions with classifiers so human attention is spent only where policy cannot decide, and [[sources/Intercom AI Approving Pull Requests]] spends it only on changes the size gate and agent reviewers cannot clear.

The economic reading: a gate is only real while its throughput exceeds the arrival rate of work. Past that point the system has silently moved to a higher autonomy tier while keeping the paperwork of the lower one — worse than an explicit promotion, because the audit trail claims oversight that did not occur. The honest design is the one [[safety/AI control]] formalizes: declare the human budget, auto-clear what deterministic policy and trusted monitors can clear, and concentrate the human hours on the flagged tail.

## Related

- [[concepts/human-in-the-loop agents]]
- [[operations/permissions]]
- [[safety/AI control]]
- [[concepts/code factories]]
- [[concepts/long-horizon agents]]
- [[benchmarks/long-horizon benchmarks]]
- [[operations/agent evals]]
- [[operations/release engineering]]
- [[sources/Anthropic Measuring Agent Autonomy]]
