# Code Factories

Code factories, software factories, and agent factories are organization-level harnesses that turn the software lifecycle into an instrumented loop.

The factory is bigger than a coding agent. It connects incoming signals, triage, specs, planning, implementation, tests, review, security, release, monitoring, and incident feedback into a repeatable system.

## Relationship to Harness Engineering

| Layer | Main question | Typical artifacts |
|---|---|---|
| Harness engineering | What scaffold makes one or more agent runs reliable, inspectable, and recoverable? | tools, permissions, sandbox, context, hooks, skills, logs, worktrees, evals |
| Loop engineering | How does the harness wake, continue, verify, retry, and stop over time? | schedules, goals, workflow scripts, queues, state files, stop conditions |
| Code factory | How does the organization turn work signals into shipped and monitored software through agent-mediated loops? | issue queues, specs, policies, model routing, agent workspaces, review gates, telemetry, learning loops |

## Operating Pattern

1. Capture external and internal signals: customer feedback, bugs, incidents, security findings, roadmap work, CI failures.
2. Triage and plan work into durable units with constraints, acceptance criteria, and ownership. Deduplication and grouping gate this stage: [[sources/Sentry Issue Grouping v2]] shows triage quality can be a measured metric, not a vibe (see [[concepts/issue tracker control plane]]).
3. Dispatch agents or agent teams into isolated environments.
4. Run implementation, tests, review, security, and documentation checks. Pointed at the factory's own failure stream — CI breaks, crashes, machine-filed bugs — this stage is [[methods/automated program repair]], and its test-generation and mutation-gating half is what keeps verification stronger than generation.
5. Record evidence, decisions, failures, and lessons outside the model context.
6. Gate merges with review sized for agent volume: tiered AI approval with human escalation and audit ([[sources/Intercom AI Approving Pull Requests]]), against the human-capacity baseline in [[sources/Modern Code Review at Google]].
7. Serialize integration through merge queues so checks pass against the true post-merge state ([[sources/GitHub Merge Queue Docs]]).
8. Release behind canaries, feature flags, and progressive rollout, with rollback as a pipeline property ([[operations/release engineering]]).
9. Feed monitoring, incidents, and review outcomes back into the next loop ([[operations/incident response]]).

## What Makes It Different

- It treats code generation as one stage in a larger control system.
- It requires durable state outside chat: specs, task queues, memories, tickets, traces, and artifacts.
- It needs explicit governance: permission boundaries, risk classification, human gates, audit trails, and rollback.
- It benefits from model routing because different stages optimize for cost, latency, depth, or judgment.
- It is only credible when verification is stronger than generation.

## Current Anchors

- [[sources/Factory 2.0 Software Factory]] frames the software factory as an end-to-end, agent-native, self-improving SDLC loop.
- [[sources/Claude AI-Native SDLC Playbook]] turns the factory idea into a concrete artifact-triggered lifecycle: versioned intent, specification, plan, code, review, and incident records connect the stages, while skills, hooks, evals, and human gates carry policy and verification through the loop.
- [[sources/Microsoft Agentic Platform Agent Factory]] frames enterprise agent factories as lifecycle platforms with governance, specs, specialized agents, and operational metrics.
- [[sources/Microsoft Spec-Driven AI-Native Engineering]] supplies the durable-intent layer: specs become the source of truth for agent work and validation.
- [[sources/Addy Osmani Loop Engineering]] connects factory thinking to the loop layer: automations, worktrees, skills, connectors, subagents, and external memory.
- [[sources/Andrew Ng Three Key Loops]] separates fast agentic coding loops from slower developer and external feedback loops.
- [[sources/Armin Ronacher The Coming Loop]] warns that factory-style loops need legibility and human judgment or they produce systems that require machines to understand them.
- [[sources/DORA State of AI-assisted Software Development 2025]] is the largest quantitative baseline: AI adoption now correlates with delivery throughput, but with worse stability unless automated testing, small batches, and fast feedback are in place — "AI is an amplifier."
- [[sources/DORA ROI of AI-assisted Software Development]] names the J-curve: verification overhead and downstream absorption of increased code volume depress delivery metrics before they improve.
- [[sources/Factory Agent Readiness]] inverts the autonomy question: it scores whether the repository environment — build, tests, docs, observability, governance — is ready for agents, rather than whether the agent is trustworthy.
- [[sources/How Humans Review AI-Generated Pull Requests]] is the oversight-erosion warning: most agent-authored PRs in open source get no human review, and "reviewed" increasingly means reviewed by another agent.

## Related

- [[concepts/loop engineering]]
- [[methods/automated program repair]]
- [[operations/release engineering]]
- [[operations/incident response]]
- [[concepts/issue tracker control plane]]
- [[operations/agent harnesses]]
- [[operations/agent infrastructure]]
- [[operations/agent observability]]
- [[operations/worktree isolation]]
- [[operations/permissions]]
- [[methods/self-improving code loops]]
- [[concepts/versioned context]]
- [[concepts/human-in-the-loop agents]]
