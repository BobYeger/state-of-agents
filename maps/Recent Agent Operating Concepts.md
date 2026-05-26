# Recent Agent Operating Concepts

This map tracks the operating substrate that is forming around capable agents: memory consolidation, explicit outcomes, versioned context, dynamic tools, durable runtimes, subagents, observability, and control planes.

The point is not to collect every vendor feature. A source belongs here when it names or demonstrates a reusable operating concept that can transfer across systems.

## Concept Threads

| Concept | What It Adds | Anchor Sources |
|---|---|---|
| Dreaming and memory consolidation | Agents improve between sessions by reviewing trajectories and curating memory. | [[concepts/dreaming and memory consolidation]], [[sources/Anthropic Managed Agents Dreaming Outcomes]] |
| Outcomes and rubric graders | A separate evaluator checks artifacts against a rubric and sends repair feedback. | [[concepts/outcomes and rubric graders]], [[sources/Claude Managed Agents Define Outcomes]] |
| Agent skills as procedural packages | Reusable procedures are loaded selectively rather than stuffed into every prompt. | [[maps/Agent Skills Map]] |
| Versioned context | Context becomes a versioned operational artifact, not a one-off prompt. | [[concepts/versioned context]], [[sources/Agentic Context Engineering]] |
| Context compaction and pruning | Long-running agents must decide what to summarize, mask, clear, retrieve, offload, or hand off. | [[maps/Context Management Map]], [[sources/Parallel Context Compaction]] |
| Dynamic tool discovery | Agents retrieve or request tools when needed instead of seeing every schema up front. | [[concepts/dynamic tool discovery]], [[sources/MCP-Zero]] |
| Programmatic tool calling | Agents write code to call tools, filter results, and keep intermediates outside model context. | [[concepts/programmatic tool calling]], [[sources/Anthropic Code Execution with MCP]] |
| Agent operating surfaces | APIs, MCP, CLIs, SDKs, docs, schemas, skills, and code execution become a designed capability surface for agents. | [[concepts/agent operating surfaces]], [[sources/OpenAI Agents SDK Tools]] |
| Subagent context isolation | Subagents isolate context, tools, and role prompts as much as they provide parallelism. | [[concepts/subagent context isolation]], [[sources/OpenAI Codex Subagents]] |
| Ralph loops | Fresh-context coding iterations use files, tests, plans, and commits as the durable agent state. | [[sources/Ralph Playbook]], [[methods/ralph loop]] |
| Worktree isolation | Parallel coding-agent tasks get separate Git checkouts so edits, branches, and review state do not collide. | [[operations/worktree isolation]], [[sources/Cursor 3.2]] |
| Issue-tracker control planes | Tickets become durable work units and agent workspaces rather than ad hoc chat sessions. | [[sources/OpenAI Symphony]] |
| Durable dormant agents | Agents pause, wake on events, and resume from explicit state machines. | [[concepts/durable dormant agents]], [[sources/Google ADK Durable Agents]] |
| Runtime scaling primitives | Long-running agent state, streams, and checkpoints become runtime cost centers. | [[sources/LangChain Delta Channels]], [[sources/Parallel Context Compaction]] |
| Managed sandboxes and private tools | Agent harnesses and execution environments are separated by policy and network boundary. | [[operations/sandboxes]], [[sources/Anthropic Managed Agents Sandboxes MCP Tunnels]] |
| Reasoning and trajectory memory | Memory stores lessons, recovery strategies, and reasoning patterns with provenance. | [[concepts/reasoning memory]], [[sources/Google ReasoningBank]] |
| Observability and event streams | Agent runs expose traces, events, artifacts, state updates, and subagent progress. | [[operations/agent observability]], [[sources/OpenAI Symphony]] |

## Synthesis

The old agent stack was prompt plus tools plus loop.

The newer stack is versioned context plus skills plus dynamic tools plus memory consolidation plus evaluators plus durable runtime plus subagents plus observability plus governance.

This map should stay compact. If three sources explain the same vendor implementation, keep the original architecture source, the strongest empirical paper, and one implementation example only when it introduces a distinct mechanism.

## Related

- [[maps/What Makes Agent Systems Better]]
- [[maps/Production Infrastructure Map]]
- [[maps/MAS Orchestration and Architecture]]
- [[maps/Agent Skills Map]]
- [[maps/Context Management Map]]
- [[operations/agent harnesses]]
- [[operations/worktree isolation]]
- [[concepts/agent operating surfaces]]
