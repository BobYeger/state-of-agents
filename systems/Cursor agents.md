# Cursor Agents

Cursor's local and cloud coding-agent systems, including long-running and multi-agent research harnesses.

Cursor is useful here less as a single product and more as a corpus of production experiments: cloud agents with their own development environments, long-running autonomous coding, multi-agent coordination, code review agents, and harness iteration.

## The 3.x Command-Center Turn

Cursor 3.x moved the center of gravity from a single agent in an editor to the IDE as an agent command center. The Agents Window runs many agents across repos and environments — local sessions, worktrees, cloud, and remote SSH — with `/worktree` and `/best-of-n` style isolated parallel runs whose outcomes can be compared ([[sources/Cursor 3 Agents Window]]: the 3.0 changelog introducing this surface). Cursor 3.2 added the operational mechanics: multitask execution, async subagents, improved worktrees, and multi-root workspaces ([[sources/Cursor 3.2]]: the stronger source for how parallel background work actually runs).

Two design commitments carry through from the 2.x era into 3.x: isolation as the default for parallel attempts (worktrees or remote machines), and comparison of outcomes rather than trust in any single attempt (best-of-n over parallel runs).

## Design Pattern

- Run many coding agents in parallel when the work can be decomposed.
- Use worktrees or remote machines to keep parallel agent attempts from interfering with one another.
- Use shared project state, tests, screenshots, logs, and review artifacts as coordination surfaces.
- Treat harness design and evaluation as the durable product, not only the model choice.

## Related

- [[concepts/long-horizon agents]]
- [[concepts/multi-agent systems]]
- [[methods/multi-agent orchestration]]
- [[operations/agent infrastructure]]
- [[operations/worktree isolation]]
- [[operations/sandboxes]]

## Related Sources

- [[sources/Cursor Agent Computer Use|Cursor agents can now control their own computers]]
- [[sources/Cursor 2.0|Introducing Cursor 2.0 and Composer]]
- [[sources/Cursor 3 Agents Window|Cursor 3.0 Agents Window]]
- [[sources/Cursor 3.2|Multitask, Worktrees, and Multi-root Workspaces]]
- [[sources/Cursor Improving Agent Harness|Continually improving our agent harness]]
- [[sources/Cursor Scaling Long-Running Autonomous Coding|Scaling long-running autonomous coding]]
- [[sources/Cursor Multi-Agent Kernels|Speeding up GPU kernels by 38% with a multi-agent system]]
- [[sources/Cursor Self-Driving Codebases|Towards self-driving codebases]]
- [[sources/Cursor Building Better Bugbot|Building a better Bugbot]]
- [[sources/Cursor Bugbot Learned Rules|Bugbot now self-improves with learned rules]]
