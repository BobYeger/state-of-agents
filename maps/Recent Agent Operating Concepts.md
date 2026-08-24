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
| Agent-native memory systems | Memory becomes a maintained operating subsystem with construction, retrieval/routing, freshness, provenance, and poisoning defenses. | [[sources/Agent Memory Characterization]], [[sources/Are We Ready For An Agent-Native Memory System]], [[sources/Memory Poisoning Attacks in LLM Agents]] |
| Dynamic tool discovery | Agents retrieve or request tools when needed instead of seeing every schema up front. | [[concepts/dynamic tool discovery]], [[sources/MCP-Zero]] |
| Agentic resource discovery | Agents discover and verify tools, skills, agents, and catalogs across organizational boundaries. | [[sources/Google Agentic Resource Discovery]], [[concepts/agent operating surfaces]] |
| Programmatic tool calling | Agents write code to call tools, filter results, and keep intermediates outside model context, while direct calls preserve semantic judgment and approval boundaries. | [[concepts/programmatic tool calling]], [[sources/Anthropic Code Execution with MCP]], [[sources/OpenAI Programmatic Tool Calling]] |
| Agent operating surfaces | APIs, MCP, CLIs, SDKs, docs, schemas, skills, and code execution become a designed capability surface for agents. | [[concepts/agent operating surfaces]], [[sources/OpenAI Agents SDK Tools]] |
| Subagent context isolation | Subagents isolate context, tools, and role prompts as much as they provide parallelism; provider APIs now compact each agent independently. | [[concepts/subagent context isolation]], [[sources/OpenAI Codex Subagents]], [[sources/OpenAI Responses API Multi-Agent]] |
| Cross-session communication contracts | Peer messages, queued turns, team mailboxes, control-plane commands, and protocol tasks differ in identity, authority, wake, persistence, acknowledgment, and reply semantics. | [[concepts/cross-session agent communication]], [[sources/Claude Code Cross-Session Messaging]], [[sources/OpenAI Codex Session Queueing]], [[sources/DeepSeek Harness Agent Teams]] |
| Role-aware capacity allocation | Strong models concentrate on decomposition or advice while compact workers execute bounded subtasks. | [[methods/runtime routing]], [[sources/Think Big Search Small]], [[sources/Claude Advisor Tool]] |
| Workflow scripts as orchestration state | A generated script or CI workflow holds the plan, spawns workers, tracks intermediate results, and reports back. | [[sources/Claude Code Workflows]], [[sources/Recursive Agent Harnesses]], [[sources/GitHub Agentic Workflows]] |
| Loop engineering | Outer loops wake, prompt, monitor, verify, retry, and stop agents over time. | [[concepts/loop engineering]], [[sources/Claude Code Scheduled Tasks]], [[sources/Addy Osmani Loop Engineering]], [[sources/Andrew Ng Three Key Loops]], [[sources/Armin Ronacher The Coming Loop]], [[sources/GitHub Agentic Workflows]] |
| Code/software factories | Agent work becomes an SDLC control plane that links signals, specs, agent execution, verification, release, monitoring, and organizational learning. | [[concepts/code factories]], [[sources/Factory 2.0 Software Factory]], [[sources/Microsoft Agentic Platform Agent Factory]], [[sources/Microsoft Spec-Driven AI-Native Engineering]] |
| Self-improving code loops | Agents mutate code, harnesses, workflows, algorithms, or skills and keep changes only when evidence improves. | [[methods/self-improving code loops]], [[sources/Darwin Godel Machine]], [[sources/Self-Harness]], [[sources/HarnessFix]], [[sources/Adaptive Auto-Harness]] |
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

July 2026 adds model-native agent trees, generated tool-control programs, asymmetric advisor/executor routing, and independently compacted subagent contexts. August adds direct session messaging, durable queued turns, explicit team-mailbox recovery semantics, and a production incident in which shared infrastructure became an unauthorized cross-run blackboard. The shared move is still to make control explicit and inspectable outside a single chat context, but some of that control surface is now part of the model API—and some can emerge outside the designed harness entirely.

This map should stay compact. If three sources explain the same vendor implementation, keep the original architecture source, the strongest empirical paper, and one implementation example only when it introduces a distinct mechanism.

## Related

- [[maps/What Makes Agent Systems Better]]
- [[maps/Production Infrastructure Map]]
- [[maps/MAS Orchestration and Architecture]]
- [[maps/Agent Skills Map]]
- [[maps/Context Management Map]]
- [[operations/agent harnesses]]
- [[concepts/loop engineering]]
- [[concepts/code factories]]
- [[methods/self-improving code loops]]
- [[operations/worktree isolation]]
- [[concepts/agent operating surfaces]]
- [[concepts/cross-session agent communication]]
