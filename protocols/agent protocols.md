# Agent Protocols

Agent protocols define how agents discover capabilities, call tools, exchange tasks, share state, authenticate, and coordinate across systems.

The useful distinction is between tool protocols and agent-to-agent protocols. Tool protocols expose external capabilities to an agent; agent-to-agent protocols let independently implemented agents advertise skills, exchange tasks, stream progress, and coordinate work.

## Protocol Questions

- How does an agent discover another agent or tool?
- What is the unit of work: a tool call, message, task, artifact, or stream?
- How are identity, authorization, and delegation represented?
- What prevents prompt injection, impersonation, confused-deputy behavior, or over-broad authorization?
- Which parts are interoperability standards versus framework-specific conventions?

## Protocol Surfaces

- [[protocols/MCP]]: agent to tools, data, and context.
- [[protocols/A2A]]: agent to agent.
- [[protocols/ACP]]: coding agent to editor or client.
- [[protocols/AG-UI]] and [[protocols/A2UI]]: agent to user interface.
- [[protocols/AP2]] and [[protocols/UCP]]: agent-mediated payments and commerce.

## Related Sources

- [[sources/A2A Specification|Agent2Agent Protocol Specification]]
- [[sources/A2A GitHub Repository|A2A GitHub Repository]]
- [[sources/MCP Specification 2025-11-25|MCP Specification 2025-11-25]]
- [[sources/Google Developer Guide to AI Agent Protocols|Developer's Guide to AI Agent Protocols]]
- [[sources/The Orchestration of Multi-Agent Systems|The Orchestration of Multi-Agent Systems: Architectures, Protocols, and Enterprise Adoption]]
- [[sources/Multi-Agent Collaboration Mechanisms - A Survey of LLMs|Multi-Agent Collaboration Mechanisms: A Survey of LLMs]]
