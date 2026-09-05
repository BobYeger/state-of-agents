# Claim - Agent teams need explicit organization

Agent teams improve systems only when team structure is explicit: roles, task ownership, communication, shared state, verification, stopping conditions, and human supervision.

## Evidence

- [[sources/Claude Code Agent Teams]] distinguishes agent teams from subagents by independent context windows, shared task lists, direct teammate communication, and team-lead coordination.
- [[sources/Claude Code Cross-Session Messaging]] shows the lower layer: already-running sessions can exchange identified peer messages with reply and inbound-policy semantics without acquiring a shared task list or team lead.
- [[sources/OpenAI Codex Session Queueing]] supplies the contrasting control-plane primitive: durable queued input can wake an idle loaded session or wait for an unloaded session to be resumed, without carrying peer identity in the v0.149 envelope.
- [[sources/DeepSeek Harness Agent Teams]] makes the organizational delta explicit in implementation: Lead, roster, durable mailbox acknowledgments, and a CAS task DAG, bounded by private experimental packaging and shared-checkout limitations.
- [[sources/Grok Bot]] combines named persistent agents, direct and group messaging, and shared files on one user computer; the shared machine helps coordination but does not isolate teammates from one another.
- [[sources/Anthropic Multi-Agent Coordination Patterns]] says agent teams fit sustained, parallel, independent work, but struggle when dependencies require tight coordination.
- [[sources/MiniMax Agent Team]] uses a Leader / Worker / Verifier loop with explicit task states and adversarial quality gates.
- [[sources/Agyn]] models autonomous software engineering as an organizational process with coordination, research, implementation, review, structured communication, and isolated sandboxes.
- [[sources/Multi-Agent Teams Hold Experts Back]] shows self-organizing teams can underuse their strongest member, so team interaction is not automatically beneficial.
- [[sources/OpenAI Responses API Multi-Agent]] defines the useful/poor-fit boundary for provider-native subagents and makes concurrency, agent trees, collaboration actions, and per-agent context explicit runtime controls.
- [[sources/Think Big Search Small]] shows that role design includes capacity allocation: delegation was more than four times as sensitive to model scale as execution on controlled hierarchical-search tasks.
- [[sources/Claude Advisor Tool]] implements a narrow executor/advisor organization in which the stronger model is consulted at selected decision points rather than generating every token.
- [[sources/Factory How Missions Work]] gives a vendor-operated orchestrator/worker/validator system with explicit role authority, externalized state, milestone gates, and a predeclared validation contract; its outcome telemetry is a single vendor-reported run.
- [[sources/MasDrift]] shows that task organization and authorization organization are separate: deeper centralized hierarchies improve completion while increasing reserved actions; Source re-anchoring reduces but does not eliminate those actions, while Chain prevents them at a large utility cost.

## Implications

- Prefer agent teams when subtasks are independent enough to run in parallel and benefit from sustained worker context.
- Avoid agent teams for tightly coupled same-file or sequential work unless the control layer handles conflicts and dependencies.
- Add verification and conflict resolution before adding more teammates.
- Treat team observability as part of the product, not an afterthought.
- Allocate model capacity by role and information bottleneck, not uniformly across teammates.
- Keep delegated task state separate from authoritative permission state; re-evaluate effective authority at the action boundary.
- Do not infer team organization from a communication edge. Specify roles, ownership, shared state, verification, and stopping policy above the transport.
- Audit shared writable infrastructure as an undeclared coordination plane. Emergent roles, signatures, and peer approval can make an improvised channel usable without supplying platform-backed identity or authorization ([[sources/OpenAI Hugging Face Incident Technical Report]], [[sources/METR OpenAI Hugging Face Incident Investigation]]).

## Related

- [[concepts/agent teams]]
- [[concepts/cross-session agent communication]]
- [[methods/multi-agent orchestration]]
- [[maps/Agent Teams and Workforces Map]]
- [[claims/Claim - Coordination is a cost the task must justify]]
- [[claims/Claim - Agent systems improve when structure matches the task]]
