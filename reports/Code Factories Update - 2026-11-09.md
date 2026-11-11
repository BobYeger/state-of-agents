---
title: "Code Factories Update — 2026-11-09"
aliases: ["November 2026 Code Factory Research Update"]
tags: [reports, code-factories]
created: 2026-11-09
updated: 2026-11-09
research_as_of: 2026-11-09
---

# Code Factories Update — 2026-11-09

The main change since the vault's earlier synthesis is better evidence about operating the whole factory: continuous work intake, persistent coordination, infrastructure capacity, review convergence, and measuring whether merged work actually helps. This review adds September–October primary sources; it does not establish comprehensive coverage of all releases through November 9.

## What Changed

| Development | New evidence | Strength and boundary |
|---|---|---|
| Persistent project coordination | [[sources/Cursor Projects and Agent SDK]] connects long-lived project state with event-driven agents defined as code. | Shipped mechanisms and vendor use reports; no independent delivery-quality estimate. |
| Fleet provisioning becomes a separate layer | [[sources/Factory OpenCompute]] supplies a reconciled lifecycle and capability-tested provider contracts. | Private-preview architecture; hosting locality and data locality remain different. |
| Review is an optimization loop | [[sources/Claude Code Review at Agent Volume]] tracks human effort, defects, false positives, and rounds to convergence. | Production observations, not a controlled attribution of gains. |
| Source control becomes a throughput constraint | [[sources/Anthropic Scion Source Control]] documents a specialized service for an unusually busy monorepo. | Concrete deployed architecture; narrow transferability. |
| Verification extends into production | [[sources/Cursor Rollouts and Security Reviewer]] turns a diff into a monitoring plan. | Product mechanism; published detection/rollback accuracy remains absent. |
| Factory progress can become self-referential | [[sources/Instant Software Factories]] distinguishes activity from lasting delivery when agents also alter tasks and checks. | Short industrial observations; automated bootstrap still untested. |
| Orchestration becomes inspectable | [[sources/HumanLayer Open Source Agent Orchestration]] exposes the application, daemon, API, and staged workflow implementation. | Repository evidence, not measured delivery gains; self-hosting guidance remains incomplete. |

The existing [[maps/Code Factory Playbook]] remains the lifecycle spine. These sources sharpen its measurement requirements rather than proving that an entire autonomous SDLC is solved.

## Integration Is Its Own Evaluation Target

Three new benchmarks inspect different failure surfaces:

| Source | What should be measured |
|---|---|
| [[sources/AsynCodeBench]] | Whether producer–consumer dependencies hold, and when they first hold. |
| [[sources/Passes Alone Fails Together]] | Whether a shared test suite reveals failures introduced specifically by composing patches. |
| [[sources/ParallACT]] | Whether work from separate principals satisfies their requirements jointly. |

These are diagnostic tests, not production failure-rate estimates. They should inform local evaluation design, not be combined into one multi-agent leaderboard.

**Design inference:** task assignment should record affected interfaces and the owner of a disputed requirement. A clean textual merge, plausible message exchange, and high test-pass fraction are distinct observations. Check the combined behavior before calling a team successful.

## Two Different Integration Regimes

The Anthropic sources must not be conflated. Its exceptional monorepo tolerates a window of post-merge repair; the separate Claude Code repository retains checks against combined main before landing. These are different operating envelopes, not contradictory descriptions of one queue. See [[sources/Anthropic Scion Source Control]] and [[sources/Claude Code Review at Agent Volume]].

**Design inference:** ordinary factory adoption should keep the existing integration gate unless measured queue pressure justifies another design. If checks move after merge, record how long main can remain broken, which deployments are blocked, and who restores it. Volume alone does not justify importing an exceptional operator's policy.

## DAIR Follow-up: Verification and Runtime Adaptation

[[sources/Rethinking Verification in Agent Harnesses]] motivates testing a separate critic before acceptance, while retaining executable acceptance tests. [[sources/Exo]] motivates separating editable runtime policies from protected state and activation authority. **Design inference:** evaluate both changes against held-out work and complete lifecycle cost before extending factory autonomy.

## Measurements to Add

The [[reports/Cyber Swarms and Attacker Findings - 2026-11-09|cyber follow-up]] extends these measurements to vulnerability pipelines. [[sources/OpenAI Linux Vulnerability Pipeline]] and [[sources/PHP Foundation October Security Release]] make validation, attribution, maintainer capacity, and deployed remediation explicit parts of the delivery path.

For a local pilot, record a stable work identifier through intake, accepted patch, integrated state, deployment, and delayed outcome. Track:

- Useful changes still correct after a fixed observation window.
- Human minutes across review, clarification, repair, and incidents.
- Dependency failures and semantic conflicts, including failures hidden by partial test progress.
- Agent, CI, environment, and integration costs per surviving change.
- Reviewer recall, harmful false positives, and repeated review rounds.
- Who changed the acceptance criteria or CI while the work was underway.

This is a proposed evaluation design derived from the sources, not a validated universal factory score. Preserve earlier baselines and compare equivalent work cohorts before attributing improvement.

## Priority Follow-ups

1. **Independent factory replication:** replay the same incoming work with a fixed external acceptance suite, reporting delayed defects and complete human/compute costs.
2. **Communication that changes execution:** compare actual online interface updates and ownership agreements with oracle messages and sequential handoff.
3. **Review-learning generalization:** evaluate held-out incident classes after edits to reviewer instructions; measure noise-induced code churn.
4. **Infrastructure maturity:** verify current OpenCompute release status and failure recovery contracts before treating preview architecture as an available general solution.
5. **Formal verification lead:** [Modern Software Engineering with Verification Agents](https://arxiv.org/html/2611.02285v1), submitted November 1, proposes a formal-specification-centered architecture. Its proposed components should be assessed separately from its cited existing systems; it is not promoted here as deployed factory evidence.

## Review Method

Read the primary article bodies and paper methods/results/limitations. Source cards record publication-date basis and paper version. Metrics retain their denominator, model/protocol, and operator-versus-research status. No experiments were reproduced, and source identity verification does not validate the authors' claims.

Related: [[maps/Code Factory Playbook]], [[concepts/code factories]], [[maps/Self-Improving Systems Map]], [[reports/Multi Agent Report]].
