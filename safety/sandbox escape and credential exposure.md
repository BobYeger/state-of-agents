# sandbox escape and credential exposure

Sandbox escape and credential exposure are production-agent risks where an agent or compromised tool crosses intended execution boundaries or leaks privileged secrets.

This risk is most acute for coding agents, browser agents, and MCP/tool-using agents that can execute code, access files, call external services, or hold credentials. The design question is not only whether a sandbox exists, but whether credentials, network access, filesystem scope, approval policy, and logs are separated from compromised tool output.

## Related

- [[operations/sandboxes]]
- [[operations/permissions]]
- [[safety/agent safety and security]]
- [[safety/prompt injection]]

## Related Sources

- [[sources/OpenAI Running Codex Safely]]
- [[sources/Anthropic Claude Code Sandboxing]]
- [[sources/Cloudflare Sandboxing AI Agents]]
- [[sources/MCP Security Best Practices]]
