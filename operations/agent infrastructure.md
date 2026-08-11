# Agent Infrastructure

Agent infrastructure includes the runtime components that let agents act reliably: harnesses, sessions, sandboxes, tools, memory, permissions, queues, observability, and recovery.

The infrastructure layer is where many agent improvements become real: the same model can behave differently depending on its tools, state, sandbox, traces, memory, and recovery path.

## Durable Execution

Durable execution is a neutral infrastructure category — not one vendor's product — for making agent loops survive crashes, rate limits, and long waits without re-running completed steps or re-spending tokens. The shared mechanism is a persisted record of completed steps that a restarted process replays to resume where it stopped. The category currently spans two architectural stances:

- Workflow-engine style: [[sources/Temporal OpenAI Agents SDK Integration]] runs the agent loop as a workflow with every LLM call and tool call as a retryable activity; event history replays deterministically after a crash, and the integration targets three named failure classes (rate-limited LLMs, network faults, process crashes).
- Journal-middleware style: [[sources/Restate Durable AI Loops]] records step results in a per-invocation journal over an unmodified SDK loop ("agents are just code"), with first-class suspension so an agent can await human approval indefinitely at zero compute cost.

The stances trade restructuring cost against runtime guarantees; both vendors' comparisons are adversarial positioning, so evaluate against your own loop shape. Two neutral results anchor the category. [[sources/You Cannot Have Exactly-Once Delivery]] is the classic constraint: task pickup across queues and agent fleets must be designed at-least-once plus idempotent, because exactly-once delivery is impossible at the delivery layer. [[sources/Atomix]] names what replay alone does not solve — partial tool side effects, losing-branch residue, stale writes, irreversible sends — and prototypes transactional tool use that gates irreversible effects until conflicting work settles. Durable execution recovers the loop; effect semantics for the tools remain the designer's problem. See [[operations/durable sessions]] and [[operations/harness fault tolerance]] for the session- and harness-level views.

## Kubernetes-Native Runtimes

A parallel track makes the agent a first-class cluster workload rather than a process inside someone's cloud:

- [[sources/kagent]]: agents, model configs, and tool servers as Kubernetes CRDs — versioned in Git, reviewed in PRs, deployed by GitOps — with A2A for delegation, OTel tracing built in, and CNCF Sandbox status. The durable idea is that agent definitions become declarative, reviewable infrastructure.
- [[sources/Kubernetes Agent Sandbox]]: upstream Kubernetes (SIG Apps) standardizing a Sandbox CRD for isolated, stateful, mostly-idle singleton agents, with gVisor/Kata isolation, warm pools against cold starts, and scale-to-zero with preserved state — the argument being that StatefulSets and Services mismatch agent workload shape.

Gateways are becoming the corresponding data plane: [[sources/agentgateway]] (Linux Foundation/AAIF) proxies LLM, MCP, and A2A traffic with per-tool policies and CEL authorization; [[sources/Envoy AI Gateway 1.0]] adds token-aware quotas and a full MCP gateway on Envoy. Protocol design is converging on this deployment model from the other side: [[sources/MCP Specification 2026-07-28]] removes protocol-level session state, permitting compatible servers to run behind plain load balancers when application state is explicit. Streamable HTTP mirrors the method and, for tool calls, resource reads, and prompt gets, the relevant name or URI into headers for gateway routing and policy.

## Self-Hosted vs Managed

| Consideration | Self-hosted (K8s runtimes, gateways, durable-execution clusters) | Managed (vendor agent clouds and sandboxes) |
|---|---|---|
| Control and audit | Full: definitions in Git, traffic through your gateway, traces in your stack | Bounded by the vendor's event stream and export surface |
| Cost attribution | Requires your own gateway/metering ([[operations/cost control]]) | Built in, but on the vendor's granularity |
| Operational burden | You run the control plane, upgrades, and warm pools | Vendor's problem; you inherit their incidents |
| Data boundaries | Workloads and credentials stay in-tenant | Depends on sandbox and tunnel architecture |
| Maturity risk | Pre-GA CRDs and pre-stable conventions churn under you | Beta-versioned APIs churn on the vendor's schedule |

The practical middle is hybrid: managed model access behind a self-hosted gateway, or vendor harnesses scheduled onto cluster-owned sandboxes. The deciding questions are where credentials must live ([[operations/permissions]], [[operations/agent identity]]) and who needs the traces ([[operations/agent observability]]).

## Related

- [[operations/durable sessions]]
- [[operations/harness fault tolerance]]
- [[operations/sandboxes]]
- [[operations/worktree isolation]]
- [[operations/agent memory]]
- [[operations/agent observability]]
- [[operations/permissions]]
- [[operations/agent identity]]
- [[operations/cost control]]
- [[operations/agent harnesses]]
- [[operations/agent evals]]
- [[concepts/agent operating surfaces]]
- [[methods/codex thread orchestration]]
- [[maps/What Makes Agent Systems Better]]
- [[maps/Recent Agent Operating Concepts]]

## Related Sources

- [[sources/Anthropic Effective Harnesses for Long-Running Agents|Effective harnesses for long-running agents]]
- [[sources/OpenAI Responses API Computer Environment|From model to agent: Equipping the Responses API with a computer environment]]
- [[sources/llm-wiki - Karpathy|llm-wiki]]
- [[sources/MasRouter|MasRouter: Learning to Route LLMs for Multi-Agent Systems]]
- [[sources/Cloudflare Project Think|Project Think: building the next generation of AI agents on Cloudflare]]
- [[sources/Cloudflare Dynamic Workflows|Introducing Dynamic Workflows]]
- [[sources/Cloudflare Think Docs|Cloudflare Think docs]]
- [[sources/LangChain Deep Agents v0.6|New in Deep Agents v0.6]]
- [[sources/Anthropic Managed Agents Sandboxes MCP Tunnels|New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels]]
- [[sources/The Orchestration of Multi-Agent Systems|The Orchestration of Multi-Agent Systems: Architectures, Protocols, and Enterprise Adoption]]
- [[sources/Cloudflare Sandboxing AI Agents|Sandboxing AI agents, 100x faster]]
- [[sources/Cloudflare Scaling MCP Adoption|Scaling MCP adoption: reference architecture]]
- [[sources/Cloudflare Code Mode MCP API|Code Mode: give agents an entire API in 1,000 tokens]]
- [[sources/Cloudflare CLI for All Cloudflare|Building a CLI for all of Cloudflare]]
- [[sources/Anthropic Managed Agents|Scaling Managed Agents: Decoupling the brain from the hands]]
- [[sources/The 2025 AI Agent Index|The 2025 AI Agent Index: Documenting Technical and Safety Features of Deployed Agentic AI Systems]]
- [[sources/Understanding Multi-Agent LLM Frameworks|Understanding Multi-Agent LLM Frameworks: A Unified Benchmark and Experimental Analysis]]
- [[sources/OpenAI Codex Agent Loop|Unrolling the Codex agent loop]]
- [[sources/OpenAI Codex App Server Docs]]
- [[sources/OpenAI Codex App Worktrees|Worktrees]]
- [[sources/Anthropic Claude Code Worktrees|Run parallel sessions with worktrees]]
- [[sources/Temporal OpenAI Agents SDK Integration]]
- [[sources/Restate Durable AI Loops]]
- [[sources/You Cannot Have Exactly-Once Delivery]]
- [[sources/Atomix]]
- [[sources/kagent]]
- [[sources/Kubernetes Agent Sandbox]]
- [[sources/agentgateway]]
- [[sources/Envoy AI Gateway 1.0]]
- [[sources/MCP Specification 2026-07-28]]
