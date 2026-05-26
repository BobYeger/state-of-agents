# Cursor Agents

Cursor's local and cloud coding-agent systems, including long-running and multi-agent research harnesses.

Cursor is useful here less as a single product and more as a corpus of production experiments: cloud agents with their own development environments, long-running autonomous coding, multi-agent coordination, code review agents, and harness iteration.

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
- [[sources/Cursor Improving Agent Harness|Continually improving our agent harness]]
- [[sources/Cursor Scaling Long-Running Autonomous Coding|Scaling long-running autonomous coding]]
- [[sources/Cursor Multi-Agent Kernels|Speeding up GPU kernels by 38% with a multi-agent system]]
- [[sources/Cursor Self-Driving Codebases|Towards self-driving codebases]]
- [[sources/Cursor Building Better Bugbot|Building a better Bugbot]]
- [[sources/Cursor Bugbot Learned Rules|Bugbot now self-improves with learned rules]]
