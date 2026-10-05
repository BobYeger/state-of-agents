---
title: Agent Runtime Selection
created: 2026-10-05
updated: 2026-10-05
---

# Agent Runtime Selection

Choose how much of the [[concepts/agent loop|agent loop]] to own, independently of where its tools execute. A packaged harness can remove substantial runtime work while leaving the application's task definition, domain tools, authority, business state, and evaluation with its builder. Frameworks remain useful where their control and integration points solve a concrete problem. The recommendations below are an engineering synthesis; the primary documentation establishes product contracts, not a universal performance ranking.

## Five Starting Points

These are overlapping integration choices, not successive maturity levels. A framework can supply a harness, and a durable workflow can call a managed agent as one worker.

| Starting point | What the builder owns | Good starting condition | Main reason to choose another layer |
| --- | --- | --- | --- |
| **Hosted product or packaged app** — use an existing agent interface, configured with instructions, skills, tools, and plugins | Task configuration, access, review, and acceptance | The existing user experience already fits the work | A distinct customer interface, deployment contract, or control point is essential |
| **Managed harness API** — e.g. [[sources/OpenAI Agents API]] or [[sources/Anthropic Managed Agents]] | Application, domain tools, permissions, outcome checks, and the integration with hosted sessions | The supplied loop fits, and running it is not a differentiator | A required model, hook, state policy, or execution contract is unavailable |
| **Embedded/customizable harness SDK** — e.g. Claude Agent SDK, [[sources/LangChain Deep Agents Docs]], [[sources/OpenHands Software Agent SDK]] | Harness configuration and extensions, plus the process and deployment it runs in | Reuse planning, context management, and tools while controlling application integration | The supplied behavior is too restrictive, or deployment operations are unnecessary overhead |
| **Agent framework or orchestration runtime** — e.g. [[sources/OpenAI Agents SDK Docs]], LangChain, [[sources/LangGraph Docs]] | Agent composition, policies, tool implementations, state configuration, and deployment | Explicit workflows, handoffs, middleware, or mixed deterministic and agentic steps matter | The abstractions add more complexity than the workload needs |
| **Custom runtime or small direct API loop** | Model/tool protocol, context, stopping, budgets, errors, tracing, and any required recovery | The flow is genuinely small, or a measured requirement cannot be expressed through available extensions | Repeatedly rebuilding standard capabilities costs more than adopting them |

The boundaries are visible in current primary docs. [OpenAI's runtime comparison](https://developers.openai.com/api/docs/guides/agents#compare-agent-runtimes) separates its hosted Agents API, application-run Agents SDK, and lower-level Responses API. The [SDK guide](https://developers.openai.com/api/docs/guides/agents/sdk) still positions the SDK for custom storage, approval decisions, tools, and product logic. [Claude's SDK overview](https://code.claude.com/docs/en/agent-sdk/overview) offers the Claude Code loop and tools inside an application-controlled process. A builder can reuse an existing harness without adopting its interactive product interface.

[LangChain's own comparison](https://docs.langchain.com/oss/python/langchain/overview) spans three of these choices: Deep Agents supplies a fuller harness, `create_agent` supplies a configurable loop with middleware, and LangGraph supplies lower-level orchestration. Calling all three “a framework” obscures the actual decision.

## Hosting and Control Are Separate

Select three things explicitly: **who operates the loop, who operates the execution environment, and who owns the application's authoritative state**. In [OpenAI's architecture](https://developers.openai.com/api/docs/guides/agents-api/architecture), a managed harness can use OpenAI-hosted compute, self-hosted compute, or no execution environment. Bringing your sandbox does not move the harness or its session state into your infrastructure. The application still operates custom function tools and, when applicable, its environment's provisioning and shutdown.

Moving to a service also changes the integration rather than simply deleting responsibilities. [Anthropic's migration guide](https://platform.claude.com/docs/en/managed-agents/migration) moves history and built-in execution into managed sessions, but custom tools still run in the client. Some SDK features become client logic: tool-event handling, turn counting, and parts of hook behavior. Permission-policy semantics must be rechecked during migration. A session becoming idle indicates that the agent has no further work at that moment; the application must still validate the requested outcome.

## Keep Business State Distinct From Agent State

A resumable conversation, a graph checkpoint, a sandbox filesystem, and a completed business operation are different records. Persist the authoritative task ID, authorization, accepted artifacts, external-operation IDs, and outcome status in the application's existing system of record where they must survive a runtime replacement. Associate provider session IDs with that task rather than making the transcript the sole record of completion.

For example, an invoice may have been submitted even if the process dies before storing the tool result. Recovery needs an idempotency key or reconciliation against the invoicing system; replaying the agent's last message is insufficient. A managed service's internal recovery does not establish exactly-once effects in an external application. See [[operations/harness fault tolerance]].

Framework persistence also has configuration boundaries. [LangGraph distinguishes thread checkpoints from cross-thread stores](https://docs.langchain.com/oss/python/langgraph/persistence); an in-memory saver loses state on restart. Its [durability modes](https://docs.langchain.com/oss/python/langgraph/checkpointers#durability-modes) trade checkpoint timing against overhead. [Interrupt recovery restarts a node](https://docs.langchain.com/oss/python/langgraph/interrupts#side-effects-called-before-interrupt-must-be-idempotent), so preceding effects can repeat. Select and test the recovery contract instead of inferring it from “persistent,” “background,” or “managed.”

## Evaluate the Same Work Before Migrating

1. **Specify the required outcome and hard constraints.** Include permitted actions, latency, deployment, model availability, data handling, observability, and recovery. Reject candidates that cannot satisfy a necessary contract before optimizing their scores.
2. **Run a small representative suite through two or three candidates.** Keep tasks, tool access, environment, acceptance checks, and budgets comparable. Where possible, hold the model fixed to test the harness effect; separately compare each candidate's best complete system. Those answer different questions.
3. **Measure accepted outcomes and total operating cost.** Track artifact correctness, successful autonomous completion, human intervention, tail latency, and spend per accepted task. Include retries, background work, sandbox time, integration maintenance, and incident recovery. Reconcile cached-token and other usage semantics rather than comparing unadjusted dashboard totals.
4. **Exercise the failure boundaries.** Stop a process after an external write but before acknowledgement; duplicate an event; resume an old session; revoke tool authority; fail a tool handler; cancel a run with pending work. Check both business effects and resource cleanup.
5. **Keep the incumbent unless the gain justifies switching.** Reuse a managed or embedded harness where it passes the suite. Retain a working framework when its policies and state integration are valuable. A fashionable abstraction is not a migration benefit.

[[sources/Harness or Model]] illustrates why the fixed-model comparison matters: its selected coding suite did not resolve an average solve-rate advantage between the tested native and neutral harnesses, and incomplete cost telemetry limited the cost ordering. This is neither equivalence nor evidence that harness choice is irrelevant. [[sources/Agent Evaluation Reliability]] further motivates evaluating the deployed system with a reliable grader, not extrapolating from a model leaderboard.

## Example Paths and Custom-Loop Exit Criteria

| Workload | Plausible first experiment |
| --- | --- |
| An internal analyst already works in an agent app | Configure its tools and instructions; test accepted reports before building another interface |
| A customer-facing research or document workflow needs its own UI | Try a managed harness API behind the application; keep domain records and acceptance checks in the app |
| A workspace agent needs process-local hooks and tailored approvals | Embed a harness SDK, then test its permission and deployment boundaries |
| A multiday business process mixes approvals, deterministic updates, and agent research | Put the workflow and recovery in an orchestration layer; call a packaged or managed agent for bounded reasoning work |
| A bounded tool interaction or novel planner requires direct control | Use a small custom loop; add only the runtime obligations the workload actually needs |

Continue investing in a custom runtime when a required capability cannot be implemented through an extension, or when repeated matched evaluations show a meaningful quality, latency, isolation, or economic advantage. Record that requirement and a threshold before expanding the runtime. Exit toward a reusable harness when it meets those requirements and maintenance of context handling, scheduling, retries, or compatibility exceeds the benefit of owning them. A short direct loop need not grow into a general agent platform.

Portability is strongest when task contracts, tool implementations, permissions, artifacts, and evals remain understandable outside one runtime. Standard tool schemas and MCP help connectivity, but session lifecycle, streaming, approvals, errors, and model behavior still require adapters and regression tests. Preserve the option to change a layer without assuming integrations are behaviorally interchangeable.

## Related

- [[systems/agent frameworks and orchestration libraries]]
- [[operations/agent harnesses]]
- [[operations/agent evals]]
- [[operations/harness fault tolerance]]
- [[operations/cost control]]
- [[methods/runtime routing]] — choosing models and execution paths during a run, rather than choosing the runtime itself

Primary documentation checked October 5, 2026. Product capabilities and migration details are dated observations; the ownership and evaluation method is intended to remain useful as those contracts change.
