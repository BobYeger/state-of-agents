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
2. Triage and plan work into durable units with constraints, acceptance criteria, and ownership.
3. Dispatch agents or agent teams into isolated environments.
4. Run implementation, tests, review, security, documentation, and release checks.
5. Record evidence, decisions, failures, and lessons outside the model context.
6. Feed monitoring, incidents, and review outcomes back into the next loop.

## What Makes It Different

- It treats code generation as one stage in a larger control system.
- It requires durable state outside chat: specs, task queues, memories, tickets, traces, and artifacts.
- It needs explicit governance: permission boundaries, risk classification, human gates, audit trails, and rollback.
- It benefits from model routing because different stages optimize for cost, latency, depth, or judgment.
- It is only credible when verification is stronger than generation.

## Current Anchors

- [[sources/Factory 2.0 Software Factory]] frames the software factory as an end-to-end, agent-native, self-improving SDLC loop.
- [[sources/Microsoft Agentic Platform Agent Factory]] frames enterprise agent factories as lifecycle platforms with governance, specs, specialized agents, and operational metrics.
- [[sources/Microsoft Spec-Driven AI-Native Engineering]] supplies the durable-intent layer: specs become the source of truth for agent work and validation.
- [[sources/Addy Osmani Loop Engineering]] connects factory thinking to the loop layer: automations, worktrees, skills, connectors, subagents, and external memory.
- [[sources/Andrew Ng Three Key Loops]] separates fast agentic coding loops from slower developer and external feedback loops.
- [[sources/Armin Ronacher The Coming Loop]] warns that factory-style loops need legibility and human judgment or they produce systems that require machines to understand them.

## Related

- [[concepts/loop engineering]]
- [[operations/agent harnesses]]
- [[operations/agent infrastructure]]
- [[operations/agent observability]]
- [[operations/worktree isolation]]
- [[operations/permissions]]
- [[methods/self-improving code loops]]
- [[concepts/versioned context]]
- [[concepts/human-in-the-loop agents]]
