---
title: Event-Driven Agents
aliases:
  - Event-triggered agents
created: 2026-10-05
updated: 2026-10-05
---

# Event-Driven Agents

An event-driven agent can begin or resume work when relevant state changes: a tool finishes, a teammate replies, a document changes, a timer expires, or an approval arrives. The design separates receipt of an event from deciding whether it warrants action.

[[concepts/background agents]] describes execution lifetimes. [[concepts/durable dormant agents]] adds persisted waiting and recovery. Proactivity asks whether help is appropriate without a fresh request. An event-triggered workflow can be fully predefined and need no proactive judgment.

## Research Lineage

[[sources/Hearsay-II]] (1980) is a historical implementation of knowledge sources becoming eligible after shared-state changes, with a scheduler deciding which to run. It is a coordination antecedent, not an LLM benchmark.

[[sources/Generative Agents]] (2023) studies memory, reflection, planning, and reactions in a social simulation. Its behavioral-believability evidence does not establish workplace usefulness. The empirical proactivity literature in [[concepts/background agents]] asks when intervention helps. [[sources/SCLATE]] (2026) brings agent-side events and benchmark events onto a common evaluation timeline.

## Separate the Policies

| Policy | Decision | What to record |
|---|---|---|
| Subscription | Which changes may this principal observe? | Resource scope, filters, expiry, revocation |
| Admission | Is the event new, relevant, and still current? | Event identity, occurrence time, prior processing |
| Wakeup | Run immediately, batch, wait, or ignore? | Deadline, cost, information needed, reason for waking |
| Execution | What work is authorized now? | Task revision, current permissions, action ownership |
| Notification | Does the user need an update or decision? | Actionability, urgency, delivery and acknowledgment |

These are architecture questions derived from the combined evidence. A helpful wakeup policy can still produce annoying notifications; a reliable webhook can still trigger the wrong work.

## Current Implementations

[[sources/OpenAI MCP Events]] documents webhook-triggered work using a draft extension. [[sources/OpenAI Dots]] documents ongoing responsibilities that can wake and delegate. Both are implementation evidence; neither supplies a controlled measure of whether the intervention policy improves outcomes.

Event content is evidence about the world, not a new authority source. An external comment may satisfy a subscription filter while still containing untrusted instructions. The existing task and current access policy determine what may be done with it.

## Evaluation Questions

Test duplicate and reordered events, revoked access, stale deadlines, missed-event recovery, user steering during a run, and bursts that should be batched. Add no-action cases and score unnecessary interventions alongside missed useful ones. Measure delay from the underlying event to a useful result, not only model latency.

For feedback loops, tag effects produced by the agent and determine whether their resulting events should wake it again. A task that watches comments and writes comments needs a termination policy. For restart behavior, use the stronger guarantees in [[operations/harness fault tolerance]]; transport acknowledgment alone is insufficient.

## Related

- [[concepts/persistent personal agents]]
- [[concepts/agent loop]]
- [[concepts/cross-session agent communication]]
- [[concepts/shared agent memory]]
- [[concepts/loop engineering]]
- [[operations/durable sessions]]
- [[maps/Agent Capability Research Lineage]]
