# Long-Horizon Agents

Long-horizon agents work across many steps, tool calls, context transitions, and state changes. They require infrastructure beyond a prompt: durable sessions, recovery, memory, sandboxing, evals, and progress tracking.

## Operating Patterns

- [[concepts/durable dormant agents]] for pause, wake, and resume workflows.
- [[operations/durable sessions]] for state and event persistence.
- [[concepts/versioned context]] for keeping instructions, memories, and policies reusable across runs.

## Related

- [[operations/durable sessions]]
- [[operations/sandboxes]]
- [[concepts/context engineering]]
- [[benchmarks/long-horizon benchmarks]]

## Related Sources

- [[sources/Anthropic Effective Context Engineering|Effective context engineering for AI agents]]
- [[sources/Anthropic Effective Harnesses for Long-Running Agents|Effective harnesses for long-running agents]]
- [[sources/Karpathy Autoresearch|autoresearch]]
- [[sources/OpenHands|OpenHands: An Open Platform for AI Software Developers as Generalist Agents]]
- [[sources/Cursor Scaling Long-Running Autonomous Coding|Scaling long-running autonomous coding]]
- [[sources/TheAgentCompany|TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks]]
