# Harness Tracker

An agent harness is the execution scaffold around a model: prompt assembly, the agent loop, tool dispatch, context management, state and memory, sandboxing, permissions, streaming, event logs, compaction, subagents, skills, and resumability.

The practical question for every harness is how the loop closes: what the agent observes, where state lives, what can execute, when humans intervene, how memory and skills enter context, and what makes the run auditable or resumable.

## Schema

| Field | Meaning |
|---|---|
| Name | Harness, product, runtime, or framework being tracked. |
| Kind | Local coding harness, hosted agent, multi-agent team runtime, managed runtime, personal-agent harness, framework harness, etc. |
| Evidence level | Official architecture article, official docs, open-source code/docs, product-level only, or third-party/reverse-engineering. |
| Loop pattern | Plan-act-observe, tool loop, graph loop, leader-worker-verifier, plan/act modes, background async PR loop, etc. |
| State / context | Transcript, compaction, files, git history, durable session log, memory store, tree session, project artifacts. |
| Tools / runtime | Shell, filesystem, browser, MCP, code execution, sandbox, VM, GitHub Actions, Durable Objects, container. |
| Control layer | Approvals, permissions, path protection, sandbox, network policy, human-in-loop, PR review. |
| Multi-agent support | Subagents, handoffs, leader/worker/verifier, swarms, teams, none/extension-only. |
| Skills / memory | Agent Skills, AGENTS.md, project rules, long-term memory, procedural skill library. |
| Observability | Traces, logs, session replay, PR diffs, event stream, telemetry, checkpoints. |
| Primary sources | Official article/docs/repo links. |

## Harness Patterns

| Pattern | Examples | What to look for |
|---|---|---|
| Simple tool loop | OpenAI Agents SDK, Responses API | Model calls tool, observes output, repeats until done. |
| Coding-agent loop | Codex, Claude Code, Pi, OpenCode, Cline, Cascade | Read repo, plan, edit files, run shell/tests, observe, patch, summarize. |
| Plan/Act split | Cline, OpenCode, Windsurf Cascade | Read-only planning separated from write/execute mode. |
| Deliberative control | Three-layer architectures, plan-then-execute, planner-executor-verifier | Planning, execution, observation, and verification have explicit boundaries and authority. |
| Durable session + sandbox | Anthropic Managed Agents, Cloudflare Agents, Manus, Jules, Copilot cloud agent | Long-task state persists outside model context; execution happens in an isolated environment. |
| Initializer + worker handoff | Anthropic long-running harness | First agent creates artifacts; later agents resume from them. |
| Planner/generator/evaluator | Anthropic app-development harness | Generation and evaluation are separate agents and context resets are explicit. |
| Leader/Worker/Verifier | MiniMax Agent Team | Leader decomposes; workers execute; verifiers challenge and force revisions. |
| Memory-first agent | Letta, Hermes | Agent persists identity, preferences, lessons, and self-edits memory. |
| Extensible minimal core | Pi, OpenClaw, OpenHarness | Keep core small; add tools, skills, subagents, policies, and UI through extensions. |
| PR-producing async agent | Devin, Copilot cloud agent, Jules, Codex Cloud | Agent works in background and produces branch/diff/PR for review. |

## Profiles

| Name | Kind | Evidence | Loop Pattern | State / Context | Tools / Runtime | Control Layer | Multi-Agent | Skills / Memory | Observability | Primary Sources |
|---|---|---|---|---|---|---|---|---|---|---|
| OpenAI Codex harness | local + cloud software-engineering harness | official architecture article | Responses API inference -> tool calls -> observations -> updated context -> next call -> final response | prompt items, tool definitions, conversation input, compaction, local/cloud task context | shell, filesystem, web/search, MCP tools, Responses API, cloud/container primitives | sandbox modes, approvals, network policy, telemetry | parallel cloud tasks; not primarily a MAS framework | AGENTS.md, skills through container/runtime surfaces | event stream, logs, diffs, plans | [[sources/OpenAI Codex Agent Loop]]<br>[[sources/OpenAI Responses API Computer Environment]]<br>[[sources/OpenAI Running Codex Safely]] |
| OpenAI Agents SDK | framework harness / production agent SDK | official docs | built-in agent loop repeats tool invocation and LLM calls until complete | sessions, context management, memory layer | function tools, MCP servers, sandbox agents | guardrails, human-in-the-loop, tracing | handoffs, agents-as-tools, sandboxed specialists | skills through OpenAI platform/runtime adoption | tracing and eval integration | [[sources/OpenAI Agents SDK Docs]] |
| Claude Code / Claude Agent SDK | coding harness + long-running agent harness | Anthropic harness and safety articles | tool-using coding loop plus long-running handoff patterns across context windows | progress files, git history, feature lists, context artifacts, compaction | bash, file tools, web/MCP tools, Claude Agent SDK | permissions, sandboxing, tests, git commits, structured handoff | initializer/coding agents; planner/generator/evaluator patterns; subagents through SDK/task surfaces | Agent Skills, project instructions, Claude Code skills | logs, commits, progress artifacts | [[sources/Anthropic Effective Harnesses for Long-Running Agents]]<br>[[sources/Anthropic Harness Design Long-Running Apps]]<br>[[sources/Anthropic Claude Code Sandboxing]] |
| Anthropic Managed Agents | managed runtime / meta-harness | official architecture article | stateless harness over durable session logs and external sandboxes | append-only session event log separate from model context | sandbox hands, MCP proxy, vault-backed credentials | credential isolation, sandbox separation, resumable sessions | many brains / many hands architecture | future harness-compatible skill loading | durable session log | [[sources/Anthropic Managed Agents]] |
| Cursor Agent | IDE coding-agent harness | official harness/research articles | model-specific coding loop with context, tools, eval-driven tuning, model switching | conversation state, context management, summaries during model switches | editor, file edits, terminal, codebase context, background agents | harness-level mitigation of model quirks | emerging harness-level orchestration | rules, skills, project context | agent state, diffs, logs, eval feedback | [[sources/Cursor Improving Agent Harness]]<br>[[sources/Cursor Scaling Long-Running Autonomous Coding]] |
| Pi Coding Agent | minimal terminal coding harness | open-source repo/docs | interactive terminal coding loop with four-tool core and extensible sessions | tree sessions, branchable history, compaction, AGENTS.md, SYSTEM.md | read/write/edit/bash, TypeScript extensions, skills, prompt templates, packages | minimal core; permission gates, sandboxing, subagents, MCP via extensions/packages | not built in by default; extensible through packages or spawned Pi instances | on-demand skills, AGENTS.md, prompt templates | session tree, export/share, JSON/RPC streams | [[sources/Pi Agent Harness Repository]] |
| Hermes Agent | persistent self-improving personal agent runtime | official docs/repo | long-running memory + skills + tool execution loop with scheduled automations | cross-session memory, skills, session history, learning loop | web control, MCP, code execution, multiple execution backends | command approval and runtime isolation depending on backend | isolated subagents for parallel workstreams | open-standard skills and memory entries | trajectory export, batch processing, session records | [[sources/Hermes Agent Docs]] |
| OpenClaw | agent runtime with pluggable harness layer | official docs | prepared agent turn executed by a harness plugin | gateway/session files outside low-level harness | plugins, channels, memory providers, tool registry, bundled Codex harness | gateway handles high-level delivery/approval; harness executes the turn | depends on configured harness/plugins | via configured harness/runtime | gateway/session traces | [[sources/OpenClaw Agent Harness Plugins]] |
| OpenHarness | composable harness framework | official docs | multi-step tool loops as programmable primitives | stateless agents by default; middleware adds persistence, compaction, retry, hooks | filesystem tools, bash tools, providers, MCP | permissions and middleware as composable runtime pieces | subagent delegation with nesting/background execution | developer-defined capabilities through code/middleware | streaming UI integration and event streams | [[sources/OpenHarness Docs]] |
| Letta Code | stateful coding agent / memory-first harness | official memory docs | persistent agent across many conversations with self-editing memory | agent identity, memories, model config, messages, state; conversations as threads | CLI, desktop app, subagents, memory commands | /remember, /doctor, /init, memory auditing | subagents for memory initialization/reflection | procedural memory and shared memory blocks | memory inspection and command history | [[sources/Letta Code Memory Docs]] |
| LangGraph | low-level orchestration framework / framework harness | official docs/repo | explicit graph state machine | durable graph state, short-term memory, long-term memory | nodes, edges, tools, LangSmith, deployment infra | interrupts, pause/resume, human state inspection/modification | supervisor graphs, swarms, subagents through graph composition | application-defined | LangSmith traces/debugging | [[sources/LangGraph Docs]] |
| CrewAI | role-based multi-agent framework | official docs | crews execute tasks through sequential or hierarchical process; flows add event-driven control | crew memory, cache, flow state | agents, tasks, crews, flows, tools, hooks | process choice, manager LLM, hooks, telemetry | native crews plus flows connecting crews/tasks | agents and tasks as reusable role/process artifacts | telemetry and logs | [[sources/CrewAI Docs]] |
| Cloudflare Agents SDK / Project Think | serverless managed runtime | official architecture posts | stateful Durable Object agent wakes, reads state, does work, hibernates | Durable Object SQL database, key-value state, WebSockets, scheduling | Workers, Workflows, browser tools, MCP, subagents, email, voice, webhooks | human-in-the-loop, retries, durable execution, MCP governance | subagents and workflow orchestration | tools and memory primitives; skills possible through runtime | logs, state, workflows | [[sources/Cloudflare Project Think]]<br>[[sources/Cloudflare Agent Memory]] |
| MiniMax Agent Team | multi-agent team runtime | official engineering article | Leader -> Worker(s) -> Verifier -> retry/revise -> done | session logs, task state, file artifacts, decision records, memory, skills | IM async execution, coding harness, research pipeline, document pipeline | verifiers, retries, Leader decisions, human sign-off for high-risk actions | native Leader / Worker / Verifier team runtime | experience distilled into memory and skills | Team Engine states, status updates, artifacts | [[sources/MiniMax Agent Team]]<br>[[sources/MiniMax Agent Lessons 2025]] |

## Related

- [[operations/agent harnesses]]
- [[maps/Builder Ecosystem Map]]
- [[operations/agent infrastructure]]
- [[methods/deliberative control]]
- [[operations/agent memory]]
- [[operations/sandboxes]]
- [[operations/permissions]]
- [[protocols/agent protocols]]
