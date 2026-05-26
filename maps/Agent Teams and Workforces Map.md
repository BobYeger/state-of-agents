# Agent Teams and Workforces Map

This map tracks agent teams as an organizational pattern inside multi-agent systems.

The core distinction is:

- Multi-agent system: multiple agents interact.
- Agent team: agents have roles, responsibilities, shared objectives, team-state, coordination, observability, and a definition of done.

## Patterns

| Pattern | What It Adds | Anchor Sources |
|---|---|---|
| Agent teams vs subagents | Independent teammates keep their own context, communicate directly, and coordinate through a shared task list. | [[sources/Claude Code Agent Teams]], [[sources/OpenAI Codex Subagents]] |
| Coordination-pattern taxonomy | Chooses between generator-verifier, orchestrator-subagent, agent teams, message bus, and shared state. | [[sources/Anthropic Multi-Agent Coordination Patterns]] |
| Leader / Worker / Verifier | Lead decomposes, workers execute, verifiers challenge or reject. | [[sources/MiniMax Agent Team]], [[sources/Agyn]] |
| Orchestrator-specialist team | A lead plans and directs specialists across web, files, code, and terminal tools. | [[sources/Magentic-One]], [[sources/Magentic-UI]] |
| Software-company prelude | Software engineering is encoded as roles, phases, SOPs, and communicative workflows. | [[sources/ChatDev]], [[sources/MetaGPT]] |
| Team learning | Teams reuse experience from prior trajectories instead of solving every task from scratch. | [[sources/Experiential Co-Learning]], [[operations/agent memory]] |
| Cross-team orchestration | Multiple teams explore solution paths and exchange insights. | [[sources/Croto]] |
| Human-agent team management | A manager agent allocates work between human and AI workers while monitoring constraints and progress. | [[sources/Orchestrating Human-AI Teams]], [[sources/Developing Guidelines for Human-LLM Agent Teams]], [[concepts/human-in-the-loop agents]] |
| Team composition optimization | Model/role assignments are optimized for accuracy and cost. | [[sources/MALBO]], [[sources/MasRouter]] |
| Team failure modes | Teams can dilute expertise, compromise incorrectly, or add coordination overhead. | [[sources/Multi-Agent Teams Hold Experts Back]], [[sources/Why Do Multi-Agent LLM Systems Fail]], [[sources/Google Scaling Agent Systems]] |
| Product command centers | Human operators supervise many agent sessions across repos, worktrees, and environments. These are product-evidence examples, not core conceptual anchors. | [[sources/OpenAI Codex App]], [[sources/Cursor 3.2]], [[sources/Devin Manages Devins]] |
| Framework team patterns | Frameworks expose teams through crews, group chat, supervisor graphs, and ADK patterns. | [[sources/CrewAI Docs]], [[sources/AutoGen SelectorGroupChat]], [[sources/Google ADK Multi-Agent Patterns]] |

## Heuristics

- Use teams when the work decomposes into independent or loosely coupled assignments.
- Give each teammate an owned scope and a clean context.
- Keep shared task state explicit: task board, issue tracker, shared filesystem, event log, or worktree set.
- Prefer direct communication only when intermediate findings matter across teammates.
- Add verification, conflict handling, and stopping conditions before scaling team size.
- Preserve team-level observability: status, task ownership, artifacts, diffs, traces, and final review.

## Related

- [[concepts/agent teams]]
- [[maps/MAS Orchestration and Architecture]]
- [[maps/Harness Tracker]]
- [[maps/What Makes Agent Systems Better]]
- [[methods/multi-agent orchestration]]
- [[operations/worktree isolation]]
- [[operations/agent observability]]
