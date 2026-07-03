# OpenHands

OpenHands is an open platform for software-development agents that can write code, use shells, browse, and run benchmarks inside realistic development environments.

It matters because it is not only a benchmark paper; it is an agent runtime and research substrate. It gives agent researchers a shared interface for sandboxed code execution, browser interaction, task state, and evaluation across software engineering and web tasks.

## Two Generations

The project should now be read as two architectures, not one:

| Generation | Canonical reference | What it is |
|---|---|---|
| V0 (2024 platform) | [[sources/OpenHands]] | Open platform: agent runtime, sandboxed environments, benchmark harness for comparing software agents. |
| V1 (Software Agent SDK) | [[sources/OpenHands Software Agent SDK]] | Complete redesign of the agent components as a composable SDK; supersedes the platform paper as the architecture reference. |

The V1 SDK integrates sandboxed execution, agent lifecycle control, model-agnostic multi-LLM routing, and built-in security analysis in one package, with local-to-remote execution portability via REST/WebSocket services and interfaces spanning VSCode, VNC, browser, CLI, and APIs. A default agent takes a few lines of code. The redesign is argued from production data: V1 substantially reduces system-attributable failures versus V0 with negligible event-sourcing overhead ([[sources/OpenHands Software Agent SDK]]: vendor-reported deployment figures, accepted at MLSys 2026).

The design lesson in the V0-to-V1 arc is that a research platform and a production SDK want different decompositions: the platform optimized for shared evaluation across agents, while the SDK optimizes for lifecycle control, portability, and failure attribution in deployment.

## Design Pattern

- Put the agent in a tool-rich developer environment instead of a prompt-only task.
- Make shells, files, browsers, and execution feedback first-class parts of the loop.
- Use the same harness to compare agents, benchmark tasks, and inspect failures.
- Treat the agent layer as a composable SDK so execution can move between local and remote sandboxes without rewriting the agent (V1).

## Related

- [[concepts/long-horizon agents]]
- [[concepts/tool use]]
- [[operations/sandboxes]]
- [[operations/agent infrastructure]]
- [[benchmarks/agent evaluation]]

## Related Sources

- [[sources/OpenHands|OpenHands: An Open Platform for AI Software Developers as Generalist Agents]] (V0 platform)
- [[sources/OpenHands Software Agent SDK|The OpenHands Software Agent SDK]] (V1 architecture reference)
