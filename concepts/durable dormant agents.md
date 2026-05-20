# Durable Dormant Agents

Durable dormant agents pause when work is blocked, persist explicit state outside the context window, and wake on events such as webhooks, approvals, document signatures, or scheduled checks.

This pattern replaces raw transcript replay with explicit state machines and durable session storage. It is essential for workflows that span days or weeks.

## Related Sources

- [[sources/Google ADK Durable Agents]]
- [[sources/Cloudflare Project Think]]
- [[sources/Anthropic Managed Agents]]
- [[sources/LangChain Delta Channels]]

## Related

- [[operations/durable sessions]]
- [[operations/agent harnesses]]
- [[concepts/long-horizon agents]]
- [[concepts/context engineering]]
