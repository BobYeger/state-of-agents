# Incident Response

Incident response is the factory stage that runs when release gates were not enough: detection, triage, diagnosis, mitigation, and learning after a fault reaches production. It closes the factory's outer loop — incidents become tickets, tickets become agent work, postmortems become the next cycle's constraints.

It is also the best-documented deployment surface for investigation agents. Unlike coding agents, whose public evidence is dominated by benchmarks, incident-response agents have published production numbers from Microsoft, Meta, Azure, Sentry, and Datadog, including accuracy ceilings and cost shapes.

## Pattern

```text
alert -> dedup/group -> route -> collect diagnostics -> root-cause hypothesis -> gated mitigation -> ticket -> postmortem -> backlog
```

## Deployed Systems

| System | Output | Mechanism | Reported result |
|---|---|---|---|
| [[sources/RCACopilot]] (Microsoft) | root-cause category + narrative | alert-type routing to a handler, deterministic diagnostic aggregation, then LLM classification | 0.766 accuracy on a year of real cloud incidents |
| [[sources/Meta AI Incident Response]] | ranked root-cause changes | heuristic retrieval narrows thousands of candidate changes to hundreds; a fine-tuned 7B ranker elects a top 5 | 42% accuracy at investigation creation time |
| [[sources/Azure SRE Agent Docs]] | RCA hypothesis, proposed mitigations, prefilled ticket | subagents, 40+ MCP connectors, command and prompt hooks, pre-execution permission gate | worked example: memory-leak page resolved in 7 minutes |
| [[sources/Sentry Seer]] | scored issues, optional drafted fix PRs | scan every incoming issue, actionability scoring, agentic RCA over traces and commits | vendor-claimed 94.5% root-cause accuracy, no published methodology |

## Design Guidance

**Deterministic collection precedes the model.** RCACopilot's diagnostic-collection component ran in production for four years before the LLM layer existed; the model classifies and narrates over aggregated evidence, it does not decide what to gather ([[sources/RCACopilot]]). The Azure agent follows the same split: fixed connectors query the observability stack, the model forms the hypothesis. Building the LLM layer first inverts this and produces an agent that hallucinates its evidence base.

**Choose the RCA decomposition by your incident distribution.** Meta treats root-cause candidates as code changes, because in a monorepo most incidents are change-induced; the payoff is that RCA output plugs directly into rollback and into [[methods/automated program repair]] as a repair target ([[sources/Meta AI Incident Response]]). RCACopilot classifies into predefined root-cause categories over telemetry, which fits incident streams dominated by environment and dependency faults. Ranking the change stream is the better default for a factory, since the factory itself is the main source of changes.

**Gate for precision, not reach.** A wrong root-cause suggestion during an incident actively misleads responders, which is worse than silence. Meta's ranker uses explicit confidence gating so low-confidence answers are never surfaced, and pairs recommendations with explainability so engineers can independently validate ([[sources/Meta AI Incident Response]]). Its 42% accuracy is the honest current ceiling for change-ranking at scale; design the human workflow around the 58% case.

**Keep mitigation behind a permission gate.** The Azure agent evaluates every proposed tool call pre-execution (approve, enforce policy, or block) and deploys no change without human sign-off ([[sources/Azure SRE Agent Docs]]). Incident time is the worst time for unsupervised writes: responders are stressed, telemetry is abnormal, and the blast radius is already nonzero. Diagnosis can be autonomous; mutation should route through [[methods/hook-based control]]-style gates and [[operations/permissions]].

**Budget by task shape, and decide what happens at the cap.** Azure's published economics give the first public cost model for this stage: a quick question costs ~3.8 agent units, an automated investigation ~35, a full diagnose-and-fix ~86.5 on Opus 4.6 versus 30.1 on GPT 5.3 Codex — with the note that the more expensive model often concludes in fewer tool calls ([[sources/Azure SRE Agent Docs]]). Two consequences: model routing per task shape is worth it here, and a monthly spend cap that makes the agent unavailable when hit is a deliberate availability-versus-cost decision that should not be discovered during an outage.

**Evaluate on replayed reality, not fixtures.** Datadog pairs each ground-truth label with a world snapshot — the signal queries as they looked at incident time — and runs weekly evaluations over tens of thousands of scenarios; deliberately injecting realistic noise cut pass rates 11% but predicted production performance better ([[sources/Datadog Bits AI Eval Platform]]). [[sources/AIOpsLab]] is the complementary approach: injected faults in live Kubernetes environments give controlled difficulty where replay gives realism. An investigation agent evaluated only on clean fixtures will overreport its production accuracy.

## From Alert to Backlog

The durable output of an incident is work, and the quality of that work is set upstream at grouping time.

- Grouping decides the work-unit boundary: [[sources/Sentry Issue Grouping v2]] halved overgrouping and made it a queryable metric — an overgrouped issue hands an agent two faults under one acceptance criterion, an undergrouped one spawns duplicate investigations. [[concepts/issue tracker control plane]] covers the intake-gate design in full.
- Alert-to-ticket is now agent-written: the Azure agent files prefilled tickets with hypothesis and evidence attached; Seer drafts fix PRs. Both write into the same control plane the factory dispatches from, so incident output re-enters at triage with provenance intact.
- Postmortems feed two loops. Action items are stage-1 signals for the next factory cycle ([[concepts/code factories]]). And incident traces become permanent evaluation cases: reviewer-labeled traces turn into offline eval datasets and grader-calibration examples ([[sources/LangChain Agent Improvement Loop]]), which is how Datadog's platform caught a context-change regression before production. The incidents an agent handled badly are the regression suite for its next version.

## Related

- [[concepts/code factories]]
- [[operations/release engineering]]
- [[methods/automated program repair]]
- [[concepts/issue tracker control plane]]
- [[operations/agent observability]]
- [[operations/agent evals]]
- [[operations/permissions]]
- [[methods/hook-based control]]
- [[operations/cost control]]
