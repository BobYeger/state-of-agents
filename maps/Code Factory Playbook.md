# Code Factory Playbook

This playbook walks the [[concepts/code factories]] lifecycle stage by stage. For each stage it names the design note that covers it, the anchor evidence, and how mature that evidence is — because factory stages differ enormously in how much of their guidance is measured production result versus vendor framing.

Maturity labels used below:

| Label | Meaning |
|---|---|
| Production-measured | Deployed at scale with published accuracy, acceptance, or revert numbers |
| Deployed, thin measurement | Shipped and in use; little published quantitative evidence |
| Framework | A scoring or process framework with internal validation only |
| Research | Benchmark or lab evidence; not yet demonstrated in a production factory |

## Stage 0: Score Readiness Before Autonomy

The factory's ceiling is set by the repository environment, not the agent. [[sources/Factory Agent Readiness]] scores eight pillars (build, testing, docs, observability, governance, and others) across five maturity levels and recommends Level 3 "Standardized" as the production-ready target for routine agent maintenance. **Maturity: framework.** Use it as a checklist, not a benchmark; its strongest idea is inverting the question from "is the agent trustworthy" to "is the environment ready."

## Stage 1: Intake, Grouping, Triage

Note: [[concepts/issue tracker control plane]]. The work-unit boundary is decided here: an overgrouped issue hands an agent two faults under one acceptance criterion; an undergrouped one spawns duplicate investigations.

- [[sources/Sentry Issue Grouping v2]]: grouping quality made a queryable metric, overgrouping halved. **Production-measured.**
- [[sources/Sentry Issue Noise Reduction]]: noise filtering ahead of triage. **Deployed, thin measurement.**
- [[sources/JetBrains Cutting Through the Noise]]: the same problem from the IDE-telemetry side. **Deployed, thin measurement.**

## Stage 2: Specs and Planning

Durable intent is what agent work gets validated against. [[sources/Microsoft Spec-Driven AI-Native Engineering]] makes specs the source of truth; [[sources/Factory 2.0 Software Factory]] frames the end-to-end agent-native SDLC. **Maturity: deployed, thin measurement** — this is the stage with the largest gap between vendor conviction and published evidence. Treat spec-first as a sound default inherited from pre-agent practice rather than a proven agent-specific result.

## Stage 3: Dispatch and Isolation

Notes: [[concepts/issue tracker control plane]], [[operations/worktree isolation]], [[operations/durable sessions]].

- [[sources/OpenAI Symphony]]: one isolated workspace per ticket, workflow policy, bounded concurrency, proof-of-work before review. **Deployed, thin measurement.**
- [[sources/Anthropic Claude Code Worktrees]] and [[sources/OpenAI Codex App Worktrees]]: worktree isolation as a shipped harness feature. **Deployed, thin measurement.**

## Stage 4: Implementation and Repair

Note: [[methods/automated program repair]]. This is the best-evidenced stage in the factory.

- [[sources/Passerine]]: machine-reported bugs are ~3x more tractable than human reports (73% vs 25.6% plausible-patch rate); reproduction tests raise fix rates from 57% to 74%. **Production-measured.**
- [[sources/Meta Agentic Program Repair]]: LLM-judge gate before humans; 25.5% of published diffs landed over three months — the sober throughput baseline. **Production-measured.**
- [[sources/Agentless]] and [[sources/Mini-SWE-agent]]: the pipeline-versus-agent and minimal-scaffold control conditions. **Research**, but the strongest research in the vault for calibrating scaffold complexity.
- Benchmark caveat: [[sources/SWE-bench Illusion]] shows memorization inflates SWE-bench headline rates; calibrate on your own failure stream.

## Stage 5: Verification and Test Generation

Notes: [[methods/automated program repair]] (test-generation half), [[operations/agent evals]], [[concepts/evaluator reliability]].

- [[sources/TestGen-LLM]]: filter cascade — build, repeated-run reliability, coverage gain — with 73% of surviving recommendations accepted by engineers. **Production-measured.**
- [[sources/ACH Mutation-Guided Test Generation]]: mutation killing as the stronger adequacy criterion, hardening the repair loop against overfitted patches. **Production-measured.**
- [[sources/ImpossibleBench]] and [[sources/METR Recent Reward Hacking]]: verification will be gamed where the task is scored by an optimizable metric — repair agents should not have write access to the tests that validate them. **Research**, directly actionable.

## Stage 6: Review Gate

Note: [[operations/release engineering]] (review-gate sizing); failure evidence in [[concepts/agent failure modes]].

- [[sources/Intercom AI Approving Pull Requests]]: tiered AI approval — 19.2% of PRs auto-approved, 0.53% revert rate on AI-authored backend code versus 5.39% human-authored. **Production-measured**, single deployment.
- [[sources/Modern Code Review at Google]]: the human-capacity baseline — median reviewer handles ~4 changes a week because the median change is 24 lines. **Production-measured**, pre-agent.
- [[sources/How Humans Review AI-Generated Pull Requests]]: most agent-authored PRs in open source get no human review; "reviewed" increasingly means reviewed by another agent. **Production-measured**, the erosion warning.
- [[sources/Bias in the Loop]]: correction friction drives rubber-stamping — rejection must be as cheap as approval. **Research** (randomized experiment, n=2,784).

## Stage 7: Merge and Release

Note: [[operations/release engineering]].

- [[sources/GitHub Merge Queue Docs]]: serialized integration against the true post-merge state; flaky tests tax the whole queue. **Deployed, thin measurement** as agent evidence; mature pre-agent practice.
- [[sources/Google SRE Workbook Canarying Releases]]: population-comparison canarying with error-budget sizing, directly reusable for agent-produced changes. **Production-measured**, pre-agent.
- [[sources/DORA State of AI-assisted Software Development 2025]]: AI adoption correlates with throughput and with worse stability unless testing, small batches, and fast feedback exist. [[sources/DORA ROI of AI-assisted Software Development]]: expect the J-curve; do not remove gates during the dip. **Production-measured** (survey scale).

## Stage 8: Monitoring and Incident Response

Note: [[operations/incident response]]. Second-best-evidenced stage, with published accuracy ceilings.

- [[sources/RCACopilot]]: 0.766 root-cause accuracy on a year of real cloud incidents, with deterministic collection preceding the model. **Production-measured.**
- [[sources/Meta AI Incident Response]]: 42% top-5 root-cause accuracy at investigation creation — design the human workflow around the 58% case. **Production-measured.**
- [[sources/Azure SRE Agent Docs]]: permission-gated mitigation and the first public per-task cost model. **Deployed, thin measurement.**
- [[sources/Datadog Bits AI Eval Platform]] and [[sources/AIOpsLab]]: replayed-reality and injected-fault evaluation for investigation agents. **Production-measured** / **research** respectively.

## Stage 9: Learning Loop

Notes: [[methods/self-improving code loops]], [[concepts/lifelong agent learning]], [[maps/Self-Improving Systems Map]].

- [[sources/LangChain Agent Improvement Loop]]: traces to eval cases to judge alignment as an operational loop. **Deployed, thin measurement.**
- [[sources/Cursor Bugbot Learned Rules]]: learned review rules in a shipped product. **Deployed, thin measurement.**
- Closed-loop factory self-improvement — the factory improving its own stages under evidence — remains **research**; the harness-optimization cluster in [[maps/Self-Improving Systems Map]] is where that evidence is accumulating.

## Sequencing Adoption

Adopt where evidence is strongest and blast radius is bounded: repair on machine-filed bugs with reproduction tests (Stage 4), test generation with filter cascades (Stage 5), and merge/canary controls (Stage 7) have production-measured playbooks. Review-gate automation (Stage 6) has one strong deployment and strong erosion warnings — instrument who reviews what before scaling volume. Spec tooling (Stage 2) and learning loops (Stage 9) are where conviction currently outruns measurement; run them behind explicit evaluation rather than assuming the vendor claim.

## Related

- [[concepts/code factories]]
- [[maps/Self-Improving Systems Map]]
- [[maps/Harness Design Playbook]]
- [[methods/automated program repair]]
- [[operations/release engineering]]
- [[operations/incident response]]
- [[concepts/issue tracker control plane]]
- [[concepts/evaluator reliability]]
- [[concepts/agent failure modes]]
