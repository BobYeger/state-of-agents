# Sandboxes

Sandboxes isolate agent-executed code, file edits, browser actions, and external tool calls from sensitive host systems and credentials.

## Security Boundary

Sandboxes should prevent generated code, untrusted inputs, and prompt-injected actions from reaching credentials, internal networks, or privileged host resources.

Worktrees are useful for file and branch isolation, but they are not sandboxes. A coding agent in a worktree can still need separate policy for commands, network access, credentials, secrets, local services, and host filesystem boundaries.

The risk is not only a classical sandbox escape. A model can also be tricked into reading credentials, exfiltrating logs, modifying configuration, authorizing unintended actions, or using one tool's authority to affect another system.

Useful control points:

- Separate working directories from sensitive user files.
- Use explicit network policies for coding and browsing agents.
- Store secrets outside the agent-readable context whenever possible.
- Require confirmation for payments, credential entry, account changes, deletes, and external messages.
- Log tool calls and filesystem or network effects for later audit.

## Related

- [[operations/permissions]]
- [[operations/agent infrastructure]]
- [[operations/worktree isolation]]
- [[safety/prompt injection]]
- [[safety/agent safety and security]]

## Related Sources

- [[sources/Cursor Agent Computer Use|Cursor agents can now control their own computers]]
- [[sources/OpenAI Responses API Computer Environment|From model to agent: Equipping the Responses API with a computer environment]]
- [[sources/Anthropic Managed Agents Sandboxes MCP Tunnels|New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels]]
- [[sources/OpenHands|OpenHands: An Open Platform for AI Software Developers as Generalist Agents]]
- [[sources/Cloudflare Project Think|Project Think: building the next generation of AI agents on Cloudflare]]
- [[sources/Cloudflare Sandboxing AI Agents|Sandboxing AI agents, 100x faster]]
- [[sources/Cloudflare Code Mode MCP API|Code Mode: give agents an entire API in 1,000 tokens]]
- [[sources/Cursor Scaling Long-Running Autonomous Coding|Scaling long-running autonomous coding]]
- [[sources/Anthropic Managed Agents|Scaling Managed Agents: Decoupling the brain from the hands]]
- [[sources/Manus Sandbox|Understanding Manus sandbox - your cloud computer]]
- [[sources/OpenAI Codex App]]
