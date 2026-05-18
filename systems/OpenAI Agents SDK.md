# OpenAI Agents SDK

OpenAI's Agents SDK is a developer framework for orchestrating single-agent and multi-agent workflows around model calls, tool calls, handoffs, tracing, and evaluations.

It matters as a production abstraction layer: it packages common agent control-flow into a framework while exposing enough runtime state to debug and evaluate the system. This makes it a useful comparison point against more environment-heavy systems such as [[systems/Codex]] and [[systems/OpenHands]].

## Design Pattern

- Express agents, tools, handoffs, and traces as explicit application objects.
- Keep evals and observability near the orchestration layer.
- Use framework structure when it clarifies routing, delegation, or tool boundaries.

## Related

- [[concepts/agentic systems]]
- [[concepts/tool use]]
- [[concepts/multi-agent systems]]
- [[operations/agent infrastructure]]

## Related Sources

- [[sources/OpenAI Agents SDK Docs|OpenAI Agents SDK Documentation]]
