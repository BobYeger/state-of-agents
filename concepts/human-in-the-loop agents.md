# human-in-the-loop agents

Human-in-the-loop agent design decides when a system should keep acting autonomously and when it should pause, ask, route, or escalate.

The useful pattern is calibrated intervention. Humans should not be asked for every trivial step, but they should be brought in for ambiguity, irreversible actions, high-authority tool calls, policy-sensitive work, and cases where the agent lacks confidence or grounding.

Human-in-the-loop agents explicitly involve users in planning, approval, correction, monitoring, or handoff. How much authority the agent holds between those touchpoints — and how that authority grows or shrinks with track record — is the subject of [[concepts/graduated autonomy]].

## Improvement Levers

- Ask humans at planning boundaries, not only after failure.
- Require approval for purchases, credentials, production writes, and external messages.
- Use human feedback to update evals, rules, memories, or skills.
- Keep human decisions visible in traces for audit and future training.

## Review Throughput Is the Binding Constraint

A human gate is a queue with a measured service rate, and the rate is low. [[sources/Modern Code Review at Google]] gives the pre-agent baseline: the median reviewer handles ~4 changes per week in ~3.2 hours, and the whole system depends on small diffs (median 24 lines) and single-reviewer gates to stay that fast. Agent-scale volume breaks this arithmetic before it breaks anything else.

The break is already observable. [[sources/How Humans Review AI-Generated Pull Requests]] finds that most agent-authored PRs in open source receive no review activity at all, and that when agentic PRs are reviewed, the reviewer is usually another agent — so "reviewed" in the metrics no longer means human oversight occurred. [[sources/DORA ROI of AI-assisted Software Development]] shows the organizational cost of ignoring this: verification overhead absorbs early agent productivity gains, the down-slope of its J-curve.

The design consequence is to spend human review as a budget rather than a default: auto-clear what deterministic policy can clear ([[sources/Anthropic Claude Code Auto Mode]] uses classifier-based permission automation to cut approval fatigue without dropping the gate), let vetted agent reviewers clear the routine tier with humans on escalation ([[sources/Intercom AI Approving Pull Requests]] auto-approves 19.2% of PRs behind a size gate, with every AI approval labelled and queryable), and reserve synchronous human attention for the flagged tail — the same budgeted-audit structure formalized in [[safety/AI control]].

## Automation Bias at the Gate

A human in the loop only adds safety if the human actually disagrees sometimes. [[sources/Bias in the Loop]] measures when they stop: in a 2,784-participant randomized experiment, raising the cost of rejecting an AI suggestion (typing a correction instead of clicking accept) made participants accept more incorrect suggestions, and pre-existing attitude toward AI predicted error detection better than any demographic. Two rules follow directly:

- Rejection must be as cheap as approval in the interface, or the gate selects for rubber-stamping.
- Gate quality must be measured with correction-activity metrics (undercorrection, overcorrection, accuracy), not with approval counts — an approver who never rejects is indistinguishable from no gate.

Interruption mechanics matter for the same reason: gates that are slow or lossy get bypassed. [[sources/LangGraph Interrupts]] documents the production pattern — pause via exception, persist exact state through a checkpointer, resume by re-executing the node — and why pre-interrupt code must be idempotent for approval flows to be reliable.

## Related

- [[concepts/graduated autonomy]]
- [[operations/permissions]]
- [[operations/agent observability]]
- [[methods/runtime supervision]]
- [[safety/AI control]]
- [[concepts/code factories]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]
- [[maps/What Makes Agent Systems Better]]

## Related Sources

- [[sources/Anthropic Trustworthy Agents]]
- [[sources/Anthropic Claude Code Auto Mode]]
- [[sources/OpenAI Running Codex Safely]]
- [[sources/Google ADK Multi-Agent Patterns]]
- [[sources/Anthropic Measuring Agent Autonomy]]
- [[sources/Magentic-UI]]
- [[sources/Bias in the Loop]]
- [[sources/How Humans Review AI-Generated Pull Requests]]
- [[sources/Modern Code Review at Google]]
- [[sources/Intercom AI Approving Pull Requests]]
- [[sources/LangGraph Interrupts]]
