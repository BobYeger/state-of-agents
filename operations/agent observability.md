# Agent Observability

Agent observability captures traces, plans, tool calls, state changes, costs, latencies, errors, and interventions so behavior can be evaluated and debugged.

## Improvement Claim

Observability improves agent systems by making hidden coordination and tool behavior visible enough to debug, evaluate, and supervise.

## What to Instrument

The minimum viable trace for an agent system covers five things per turn: the model request (model, prompt layers, token counts split by input/output/cached/reasoning), every tool call with arguments and results, subagent spawns with parent-child linkage, permission and policy decisions (what was allowed, blocked, or escalated), and human interventions (interrupts, approvals, steering messages). Cost and latency attach to each of these rather than to the session as a whole — per-session totals cannot answer "which subagent or tool is burning the budget," which is the question that matters in practice ([[operations/cost control]]).

Two less obvious signals earn their place. First, queued and interrupted events: [[sources/Claude Managed Agents Session Event Stream]] specifies a session event protocol where every inbound steering message, interrupt, and custom-tool pause is a typed event with explicit processed/unprocessed state — the event stream is simultaneously the control surface and the audit log. Second, identity per request rather than per session, so a misbehaving agent in a fleet can be isolated after the fact ([[operations/agent identity]]).

## Standardization

Telemetry schemas for agents are converging on OpenTelemetry. [[sources/OpenTelemetry GenAI Semantic Conventions]] defines spans, metrics, and events for inference, agents, tool execution, evaluation, and MCP operations (`gen_ai.*`, `mcp.*` attribute namespaces), with provider-specific conventions for Anthropic, Bedrock, Azure, and OpenAI. Two instrumentation-library lineages feed it: OpenLLMetry (Traceloop) emits OTel-native spans from framework hooks, and OpenInference (Arize) defines its own convention that platforms increasingly map onto the OTel attributes. Gateways emit the same vocabulary from the network layer — [[sources/Envoy AI Gateway 1.0]] ships Prometheus GenAI token metrics, time-to-first-token and inter-token latency, and OTel tracing with OpenInference compatibility, which gives fleet-wide coverage without touching application code.

The caveat for designers: the GenAI semconv is explicitly pre-stable, with opt-in migration flags and no tagged release, so pin the semconv version in instrumentation and expect attribute renames.

## From Traces to Evaluation

Observability pays for itself when traces feed evaluation rather than just dashboards. [[sources/LangSmith Evaluation Concepts]] draws the operational split: offline evals run against curated datasets pre-deployment, online evaluators run reference-free over live traces (safety checks, format validation, LLM-as-judge), and production traces flagged by negative feedback, latency, or errors are sampled back into datasets. [[sources/Braintrust Eval-Driven Development]] closes the loop with regression gates: the same eval criteria run offline in CI and online against canary traffic. [[sources/Datadog Bits AI Eval Platform]] shows the mature end — archived "world snapshots" of production signal state make agent investigations replayable, and the trace-derived eval suite caught a context-change regression that dashboards would have missed. The design implication: choose trace schemas so that a trace is sufficient to re-run or judge the episode, not merely to read it.

## Related

- [[methods/runtime supervision]]
- [[concepts/outcomes and rubric graders]]
- [[operations/cost control]]
- [[operations/agent identity]]
- [[operations/agent evals]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]
- [[maps/What Makes Agent Systems Better]]
- [[benchmarks/agent evaluation]]

## Related Sources

- [[sources/MegaAgent|MegaAgent: A Large-Scale Autonomous LLM-based Multi-Agent System Without Predefined SOPs]]
- [[sources/OpenAI Agents SDK Docs|OpenAI Agents SDK Documentation]]
- [[sources/OpenAI Codex CLI Agents SDK Cookbook|Building Consistent Workflows with Codex CLI & Agents SDK]]
- [[sources/Anthropic Managed Agents Dreaming Outcomes|New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration]]
- [[sources/LangChain Deep Agents v0.6|New in Deep Agents v0.6]]
- [[sources/LangChain Delta Channels|Delta Channels: Evolving our Runtime for Long-Running Agents]]
- [[sources/OpenAI Symphony|OpenAI Symphony]]
- [[sources/OpenAI Codex Using Goals]]
- [[sources/Claude Code Hooks]]
- [[sources/Anthropic Building Effective AI Agents eBook]]
- [[sources/OpenRouter Fusion Beats Frontier]]
- [[sources/Cloudflare Think Docs|Cloudflare Think docs]]
- [[sources/Cloudflare Dynamic Workflows|Introducing Dynamic Workflows]]
- [[sources/SHADE-Arena|SHADE-Arena: Evaluating Sabotage and Monitoring in LLM Agents]]
- [[sources/Stop Wasting Your Tokens|Stop Wasting Your Tokens: Towards Efficient Runtime Multi-Agent Systems]]
- [[sources/Cursor Self-Driving Codebases|Towards self-driving codebases]]
- [[sources/OpenTelemetry GenAI Semantic Conventions]]
- [[sources/Envoy AI Gateway 1.0]]
- [[sources/LangSmith Evaluation Concepts]]
- [[sources/Braintrust Eval-Driven Development]]
- [[sources/Datadog Bits AI Eval Platform]]
- [[sources/Claude Managed Agents Session Event Stream]]
