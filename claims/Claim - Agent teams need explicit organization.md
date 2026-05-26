# Claim - Agent teams need explicit organization

Agent teams improve systems only when team structure is explicit: roles, task ownership, communication, shared state, verification, stopping conditions, and human supervision.

## Evidence

- [[sources/Claude Code Agent Teams]] distinguishes agent teams from subagents by independent context windows, shared task lists, direct teammate communication, and team-lead coordination.
- [[sources/Anthropic Multi-Agent Coordination Patterns]] says agent teams fit sustained, parallel, independent work, but struggle when dependencies require tight coordination.
- [[sources/MiniMax Agent Team]] uses a Leader / Worker / Verifier loop with explicit task states and adversarial quality gates.
- [[sources/Agyn]] models autonomous software engineering as an organizational process with coordination, research, implementation, review, structured communication, and isolated sandboxes.
- [[sources/Multi-Agent Teams Hold Experts Back]] shows self-organizing teams can underuse their strongest member, so team interaction is not automatically beneficial.

## Implications

- Prefer agent teams when subtasks are independent enough to run in parallel and benefit from sustained worker context.
- Avoid agent teams for tightly coupled same-file or sequential work unless the control layer handles conflicts and dependencies.
- Add verification and conflict resolution before adding more teammates.
- Treat team observability as part of the product, not an afterthought.

## Related

- [[concepts/agent teams]]
- [[methods/multi-agent orchestration]]
- [[maps/Agent Teams and Workforces Map]]
- [[claims/Claim - More agents are not automatically better]]
- [[claims/Claim - Agent systems improve when structure matches the task]]
