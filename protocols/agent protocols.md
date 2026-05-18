# Agent Protocols

Agent protocols define how agents discover capabilities, call tools, exchange tasks, share state, authenticate, and coordinate across systems.

The useful distinction is between tool protocols and agent-to-agent protocols. Tool protocols expose external capabilities to an agent; agent-to-agent protocols let independently implemented agents advertise skills, exchange tasks, stream progress, and coordinate work.

## Protocol Questions

- How does an agent discover another agent or tool?
- What is the unit of work: a tool call, message, task, artifact, or stream?
- How are identity, authorization, and delegation represented?
- What prevents prompt injection, impersonation, confused-deputy behavior, or over-broad authorization?
- Which parts are interoperability standards versus framework-specific conventions?

## Key Protocols

- [[protocols/MCP]]
- [[protocols/A2A]]

## Related Sources

- [[sources/A2A Specification|Agent2Agent Protocol Specification]]
- [[sources/A2A Specification|Agent2Agent Protocol Specification]]
- [[sources/Multi-Agent Collaboration Mechanisms - A Survey of LLMs|Multi-Agent Collaboration Mechanisms: A Survey of LLMs]]
