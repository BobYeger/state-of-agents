---
title: "Background Agents"
aliases:
  - "Asynchronous agents"
  - "Observer agents"
  - "Proactive agent initiation"
created: 2026-10-05
updated: 2026-10-05
---

# Background Agents

Background agents run outside the foreground interaction's blocking path. The user or parent can continue while they work, wait, or observe. This describes scheduling and interaction; it does not establish initiative, persistent responsibility, or recovery after a crash.

## Different Lifecycles

| Pattern | Trigger and lifetime | Result contract |
|---|---|---|
| Asynchronous delegated worker | A parent assigns work; child ends when it finishes | Return a result or artifact to the parent |
| Independent observer or monitor | Subscribes to relevant events during another run | Report a finding or invoke an explicitly granted intervention |
| Scheduled work | Timer creates a bounded run | Produce an outcome or remain quiet according to policy |
| Event-triggered wakeup | New message, state change, approval, or webhook wakes dormant work | Resume the relevant obligation; handle duplicate or stale events |
| Proactive assistant | Observations suggest a possible user need | Decide whether and how to offer assistance |
| Persistent responsibility | A standing objective survives individual turns and idle periods | Keep explicit ownership, escalation, and stopping conditions |

These can combine. A standing responsibility can sleep between events; an observer can propose work for a separate worker. A scheduled task can remain entirely reactive to a fixed instruction. [[concepts/event-driven agents]] covers wakeup and dispatch; [[operations/durable sessions]] covers what survives interruption.

## Research and Implementation Evidence

**Asynchrony is an execution mechanism.** [[sources/AgentScope 1.0]], [[sources/Claude Code Workflows]], and [[concepts/cross-session agent communication]] provide implementations and delivery contracts. Parallel work needs explicit result integration, cancellation, and shared-state ownership. Starting a child is not completion, and separate contexts do not imply separate filesystems or credentials.

**Proactivity is a decision under uncertainty.** [[sources/Proactive Agent]] evaluates whether to propose assistance from observations, including remaining silent. Its false-alarm results make restraint part of capability. [[sources/ProAgentBench]] separates intervention timing from assistance content on real workflow records. Both are evidence about initiative; neither establishes safe unattended execution.

**Observation is a different role from delegated work.** Earlier control and trace-monitoring research already evaluates an actor and an observer separately ([[sources/AI Control Despite Intentional Subversion]]; [[sources/Monitoring Reasoning Models for Misbehavior]]). The October 2026 [[sources/Claude Code Mods and You Should Know]] release makes a side observer a user-facing harness feature. That chronology identifies related ideas, not a demonstrated influence or an effectiveness result for the product.

**Idle time can do useful preparation.** [[sources/Sleep-time Compute]] explores computation before a future query. This adds another objective for background work: prepare reusable context. It should be evaluated against wasted preparation and whether the anticipated need occurs, rather than equated with persistent autonomy.

## Operational Contract

A useful background-agent description answers five questions:

1. **Activation:** what wakes it, and what events are ignored or coalesced?
2. **Observation:** what can it see, how fresh is that view, and what remains outside its view?
3. **Authority:** can it only notify, propose a patch, block an action, or execute changes?
4. **Ownership:** who integrates the result, handles conflict, and cancels obsolete work?
5. **Persistence:** which queued inputs, cursors, obligations, and effects survive restart?

Notification and action are distinct outcomes. An observer that emits a warning after a side effect has happened is not an action gate. A reminder that fires repeatedly is not evidence that an obligation was resolved. Evaluate duplicate notifications, missed events, stale results, interruption burden, and completed outcomes alongside token and latency costs.

Background execution alone promises no crash safety. Durable history, restart-safe execution, and correct external side effects are separate guarantees; see [[operations/harness fault tolerance]]. Persistent responsibility is an application contract requiring identity, retained state, and explicit termination, even if individual model invocations are stateless.

## Related

- [[concepts/persistent personal agents]]
- [[concepts/agent loop]]
- [[concepts/advisor agents]]
- [[concepts/loop engineering]]
- [[concepts/durable dormant agents]]
- [[concepts/long-horizon agents]]
- [[methods/runtime supervision]]
- [[operations/agent observability]]
- [[operations/worktree isolation]]
