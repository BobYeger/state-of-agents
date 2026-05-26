# Recent Agent Operating Concepts

This map tracks the operating substrate that is forming around capable agents: memory consolidation, explicit outcomes, versioned context, dynamic tools, durable runtimes, subagents, observability, and control planes.

The point is not to collect every vendor feature. A source belongs here when it names or demonstrates a reusable operating concept that can transfer across systems.

## Concept Threads

| Concept | What It Adds | Anchor Sources |
|---|---|---|
| Dreaming and memory consolidation | Agents improve between sessions by reviewing trajectories and curating memory. | [[sources/Anthropic Managed Agents Dreaming Outcomes]], [[sources/Letta Code Memory Docs]], [[sources/Trajectory-Informed Memory Generation]] |
| Outcomes and rubric graders | A separate evaluator checks artifacts against a rubric and sends repair feedback. | [[sources/Anthropic Managed Agents Dreaming Outcomes]], [[sources/OpenAI Eval Skills]], [[sources/Anthropic Demystifying Agent Evals]] |
| Agent skills as procedural packages | Reusable procedures are loaded selectively rather than stuffed into every prompt. | [[maps/Agent Skills Map]] |
| Versioned context | Context becomes a versioned operational artifact, not a one-off prompt. | [[sources/Agentic Context Engineering]], [[sources/LangSmith Context Hub]], [[sources/Anthropic Effective Context Engineering]] |
| Dynamic tool discovery | Agents retrieve or request tools when needed instead of seeing every schema up front. | [[sources/MCP-Zero]], [[sources/ScaleMCP]], [[sources/Anthropic Advanced Tool Use]] |
| Programmatic tool calling | Agents write code to call tools, filter results, and keep intermediates outside model context. | [[sources/Anthropic Code Execution with MCP]], [[sources/Cloudflare Code Mode MCP]], [[sources/Cloudflare Code Mode MCP API]], [[sources/LangChain Deep Agents v0.6]] |
| Agent operating surfaces | APIs, MCP, CLIs, SDKs, docs, schemas, skills, and code execution become a designed capability surface for agents. | [[concepts/agent operating surfaces]], [[sources/Cloudflare CLI for All Cloudflare]], [[sources/OpenAI Agents SDK Tools]] |
| Subagent context isolation | Subagents isolate context, tools, and role prompts as much as they provide parallelism. | [[sources/Anthropic Managed Agents Dreaming Outcomes]], [[sources/LangChain Deep Agents Docs]], [[sources/MiniMax Agent Team]] |
| Worktree isolation | Parallel coding-agent tasks get separate Git checkouts so edits, branches, and review state do not collide. | [[sources/Anthropic Claude Code Worktrees]], [[sources/OpenAI Codex App Worktrees]], [[sources/Cursor 2.0]] |
| Issue-tracker control planes | Tickets become durable work units and agent workspaces rather than ad hoc chat sessions. | [[sources/OpenAI Symphony]] |
| Durable dormant agents | Agents pause, wake on events, and resume from explicit state machines. | [[sources/Google ADK Durable Agents]], [[operations/durable sessions]] |
| Runtime scaling primitives | Long-running agent state, streams, and checkpoints become runtime cost centers. | [[sources/LangChain Delta Channels]], [[sources/LangChain Deep Agents v0.6]], [[sources/Cloudflare Think Docs]] |
| Managed sandboxes and private tools | Agent harnesses and execution environments are separated by policy and network boundary. | [[sources/Anthropic Managed Agents Sandboxes MCP Tunnels]], [[sources/OpenAI Running Codex Safely]], [[operations/sandboxes]] |
| Reasoning and trajectory memory | Memory stores lessons, recovery strategies, and reasoning patterns with provenance. | [[sources/Google ReasoningBank]], [[sources/Memory for Autonomous LLM Agents]], [[sources/Trajectory-Informed Memory Generation]] |
| Observability and event streams | Agent runs expose traces, events, artifacts, state updates, and subagent progress. | [[operations/agent observability]], [[sources/LangChain Deep Agents v0.6]], [[sources/OpenAI Symphony]] |

## Synthesis

The old agent stack was prompt plus tools plus loop.

The newer stack is versioned context plus skills plus dynamic tools plus memory consolidation plus evaluators plus durable runtime plus subagents plus observability plus governance.

This map should stay compact. If three sources explain the same vendor implementation, keep the original architecture source, the strongest empirical paper, and one implementation example only when it introduces a distinct mechanism.

## Related

- [[maps/What Makes Agent Systems Better]]
- [[maps/Production Infrastructure Map]]
- [[maps/MAS Orchestration and Architecture]]
- [[maps/Agent Skills Map]]
- [[operations/agent harnesses]]
- [[operations/worktree isolation]]
- [[concepts/agent operating surfaces]]
