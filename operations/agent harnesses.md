# Agent harnesses

A harness is the runtime layer that turns a model into an acting system by managing the loop, context, tool calls, memory, execution environment, approvals, traces, compaction, and resumption.

This is separate from a framework. A framework defines agent structure; a harness executes the agent loop in a concrete environment.

## Improvement Claim

Harnesses improve agent systems by making the loop inspectable and recoverable: context, tools, observations, approvals, state, compaction, and handoff are engineered instead of left implicit.

## Tracker

- [[maps/Harness Tracker]]
- [[reports/Harness Engineering Report]]
- [[maps/Agent Teams and Workforces Map]]
- [[concepts/loop engineering]]
- [[methods/self-improving code loops]]
- [[methods/hook-based control]]
- [[methods/ralph loop]]
- [[methods/deliberative control]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
- [[claims/Claim - Context management is an agent architecture choice]]
- [[maps/What Makes Agent Systems Better]]
- [[maps/Context Management Map]]

## Design Notes

- [[operations/harness fault tolerance]] — what keeps the loop correct when the provider, network, tools, or the harness process itself fails mid-run.
- [[concepts/cache-aware harness design]] — how prefix stability, tool masking, and token budgeting govern the cost and latency of every loop iteration.

## Anchors by Design Question

### How much harness does the model need?

- [[sources/SWE-agent]] — the ACI result: interface design drives coding-agent performance more than prompting, at fixed model capability.
- [[sources/Mini-SWE-agent]] — the control condition: ~100 lines, bash-only, no tool-calling interface, >74% on SWE-bench Verified.
- [[sources/CodeAct]] — executable code as the unified action space, up to 20% over JSON/text tool calls across 17 models.
- [[sources/Code as Agent Harness]] — 42-author survey treating the harness as a first-class research object with a three-layer taxonomy.
- [[sources/Harness Updating Is Not Harness Benefit]] — separates generating harness improvements from executing well under them; benefit is non-monotonic in model capability.
- [[sources/Anthropic Building Effective AI Agents eBook]] — architecture selection across single-agent, multi-agent, and workflow options before harness detail.

### What does the core loop look like in production?

- [[sources/OpenAI Codex Agent Loop]] — deep dive into Codex CLI prompt assembly, tools, context management, and compaction.
- [[sources/OpenAI Unlocking Codex Harness]] — why App Server exists: a stable JSON-RPC control surface over the harness core.
- [[sources/OpenAI Codex App Server Docs]] — the thread/turn/item protocol: start, resume, fork, steer, interrupt, compaction as client-callable operations.
- [[sources/OpenAI Agents SDK Tools]] — the tool surface: hosted tools, hosted MCP, function tools, agents-as-tools.
- [[sources/OpenAI Codex CLI Agents SDK Cookbook]] — one harness nested in another: Codex CLI exposed as an MCP server inside the Agents SDK.
- [[sources/OpenHands Software Agent SDK]] — event-sourced SDK redesign that substantially reduced system-attributable failures in production.
- [[sources/OpenHarness Docs]] — composable harness framework: tool loops, subagent delegation, compaction, streaming, provider abstraction.
- [[sources/Cursor Improving Agent Harness]] — model-specific prompts, tools, and runtime tuning as explicit harness levers.
- [[sources/Cursor 3.2]] — multitask execution, async subagents, and worktrees landing in a shipping harness.
- [[sources/OpenClaw Repository]] — personal-assistant runtime: gateway, channels, skills, always-on framing.
- [[sources/OpenClaw Agent Harness Plugins]] — the cleanest statement of the harness as a low-level executor of prepared agent turns.
- [[sources/Hermes Agent Repository]] — persistent self-improving runtime: memory, skills, toolsets, approvals.
- [[sources/Hermes Agent Docs]] — the documentation view of the same runtime's harness surface.
- [[sources/MiniMax Agent Lessons 2025]] — engineering lessons on tools and sub-agents from complex real-world tasks.

### How should roles and model capacity be allocated?

- [[sources/Think Big Search Small]] — controlled evidence that hierarchical-search accuracy is far more sensitive to delegator capacity than executor capacity; a trained 1.7B executor matches a frontier worker with fewer tokens.
- [[sources/Claude Advisor Tool]] — provider implementation of asymmetric capacity: a cheaper executor consults a stronger advisor at selected checkpoints inside one request.
- [[sources/OpenAI Responses API Multi-Agent]] — provider-native agent trees with isolated contexts, explicit collaboration actions, bounded concurrency, and per-agent compaction.
- [[sources/Claude Fable 5 Prompting Guide]] — operational guidance for long-lived asynchronous subagents, fresh-context verifiers, tool-grounded status, and model-specific failure modes.

### How is context assembled and paid for?

- [[sources/Manus Context Engineering]] — KV-cache hit rate named the dominant production metric; masking over removing tools; restorable truncation; keep failure evidence in context.
- [[sources/Claude API Prompt Caching]] — the mechanics the cache argument rests on: prefix hierarchy, breakpoints, TTL pricing.
- [[sources/Claude API Compaction]] — context overflow recovery moved into the API, with a pause stop-reason and documented cache interaction.
- [[sources/Parallel Context Compaction]] — compaction studied as a serving/runtime problem, not only a semantic one.
- [[sources/Letta Code Memory Docs]] — durable agents whose memory is self-edited rather than transcript-accumulated.
- [[sources/OpenAI GPT-5.6]] — explicit cache breakpoints, cache-write pricing, and minimum cache lifetime make prefix policy a first-class runtime lever.

### How is the loop controlled and steered?

- [[sources/Claude Code Hooks]] — lifecycle interception points; the anchor for [[methods/hook-based control]].
- [[sources/Claude Agent SDK Streaming vs Single Message]] — which capabilities (interrupt, message queueing, injection) exist only on a persistent input stream.
- [[sources/Claude Managed Agents Session Event Stream]] — interrupt-then-redirect, queued events, and reconnect-after-disconnect as a versioned protocol.
- [[sources/LangGraph Interrupts]] — pause/resume with node-restart semantics and the idempotency burden that follows.
- [[sources/Harness-MU]] — multi-principal governance enforced by execution hooks rather than prompts.
- [[sources/Plan-Then-Execute]] — human-agent evidence for separating planning from execution as a control point.
- [[sources/Web Agents Plan-Then-Execute]] — the security case: untrusted content steers ReAct-style control flow unless plans are fixed before execution.
- [[sources/OpenAI Programmatic Tool Calling]] — code-mediated orchestration for bounded stages, with direct calls retained for semantic judgment, evidence validation, and approval-sensitive writes.
- [[sources/OpenAI GPT-5.6 System Card]] — greater persistence can expand scope and fabricate completion, so permission and evidence gates must scale with autonomy.

### How does the loop survive faults and long horizons?

- [[sources/Claude API Errors]] — the provider error taxonomy a retry policy must branch on, including mid-stream errors after a 200.
- [[sources/Temporal OpenAI Agents SDK Integration]] — the reference mapping of durable execution onto an agent loop: workflow plus activities plus deterministic replay.
- [[sources/Restate Durable AI Loops]] — journal-based durability as middleware over existing SDK loops, with first-class suspension.
- [[sources/Atomix]] — transactional semantics for tool side effects: partial effects, losing-branch residue, irreversible sends.
- [[sources/Anthropic Effective Harnesses for Long-Running Agents]] — harness design for work spanning many context windows.
- [[sources/Anthropic Harness Design Long-Running Apps]] — the external harness as first-class for long-running application development.
- [[sources/Google ADK Durable Agents]] — pause, resume, and event-driven wake from explicit durable state rather than replayed chat.
- [[sources/LangChain Delta Channels]] — checkpointing by state deltas instead of full snapshots.
- [[sources/LangChain Deep Agents v0.6]] — the surrounding runtime primitives: harness profiles, typed streaming, context backends.
- [[sources/Cloudflare Dynamic Workflows]] — durable workflow runs routed into tenant- and agent-specific code.
- [[sources/Harness-1]] — a state-externalizing harness as the research contribution, not a better prompt.

### How does the loop keep running without a human?

- [[sources/OpenAI Codex Using Goals]] — Codex-managed objective state that keeps work oriented across turns.
- [[sources/Claude Code Scheduled Tasks]] — recurring prompts: `/loop`, loop files, cron tools.
- [[sources/Claude Code Workflows]] — JavaScript orchestration scripts coordinating subagents in the background.
- [[sources/GitHub Agentic Workflows]] — natural-language workflows compiled into Actions with agent execution.
- [[sources/Addy Osmani Loop Engineering]] — the framing: design systems that prompt, schedule, monitor, retry, and feed state back.
- [[sources/Andrew Ng Three Key Loops]] — nested product-development loops, not only a coding-agent primitive.
- [[sources/Armin Ronacher The Coming Loop]] — the harness-level loop that keeps a task alive after the model would stop, and its legibility cost.
- [[sources/Ralph Playbook]] — the brute-force end of the spectrum: one prompt, one loop, externalized state.

### How do many agents share the harness?

- [[sources/Claude Code Agent Teams]] — coordinating multiple sessions as a team with shared task state.
- [[sources/OpenAI Codex Subagents]] — subagent workflows for parallel exploration, testing, review, summarization.
- [[sources/Cursor 3 Agents Window]] — many agents across repos and environments in one operating surface.
- [[sources/Devin Manages Devins]] — a main session delegating to managed parallel workers.
- [[sources/Anthropic Parallel Claudes C Compiler]] — the large-scale case study: parallel sessions over one compiler project.
- [[sources/MiniMax Agent Team]] — Leader/Worker/Verifier loops with async execution and ROI tradeoffs.
- [[sources/OpenAI Symphony]] — issue-tracker work turned into isolated autonomous coding-agent runs.
- [[sources/Anthropic Claude Code Worktrees]] — Git worktrees isolating parallel CLI sessions.
- [[sources/OpenAI Codex App Worktrees]] — worktrees as background task environments in the Codex app.

### Can the harness improve itself?

- [[sources/Self-Harness]] — the agent improves the harness it operates through.
- [[sources/HarnessFix]] — trace-guided attribution of failures to the responsible harness layer, then repair.
- [[sources/Adaptive Auto-Harness]] — harness optimization extended from fixed benchmarks to open-ended task streams.
- [[sources/Retrospective Harness Optimization]] — self-supervised harness improvement from past trajectories, no labeled validation set.
- [[sources/Meta-Harness]] — automated search over harness code around a fixed base model.
- [[sources/Recursive Agent Harnesses]] — the recursive unit is a full harness, not a model call.
- [[sources/SkillOpt]] — a skill document as trainable external state for a frozen agent.
- [[sources/Darwin Godel Machine]] — self-modifying coding agents under benchmark selection, with reported objective-hacking failures.
- [[sources/Hyperagents]] — task agent and meta agent integrated into one editable program.
- [[sources/AlphaEvolve]] — evolutionary code edits against automated evaluators at discovery scale.
- [[sources/The AI Scientist-v2]] — the harness as an end-to-end autonomous research pipeline.
- [[sources/Anthropic When AI Builds Itself]] — the organizational loop around self-improvement and where its bottlenecks move.

### What outcome is the harness driving toward?

- [[sources/Claude Managed Agents Define Outcomes]] — rubric-defined outcomes as the API-level target of a run.
- [[sources/Anthropic Managed Agents Dreaming Outcomes]] — between-session memory consolidation toward those outcomes.
- [[sources/Factory 2.0 Software Factory]] — the harness embedded in an end-to-end, agent-native SDLC loop.
- [[sources/Microsoft Agentic Platform Agent Factory]] — enterprise factory framing: lifecycle, governance, operational metrics.
- [[sources/Microsoft Spec-Driven AI-Native Engineering]] — durable specs as the source of truth agent work is validated against.

## Related

- [[operations/agent infrastructure]]
- [[operations/durable sessions]]
- [[operations/harness fault tolerance]]
- [[operations/worktree isolation]]
- [[operations/permissions]]
- [[operations/sandboxes]]
- [[operations/agent observability]]
- [[methods/runtime supervision]]
- [[concepts/cache-aware harness design]]
- [[concepts/agent operating surfaces]]
- [[concepts/context compaction]]
- [[maps/Recent Agent Operating Concepts]]
