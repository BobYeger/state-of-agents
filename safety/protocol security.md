# Protocol Security

Protocol security for agents concerns authentication, authorization, identity, impersonation, capability discovery, delegated action, and malicious or compromised peers. Two surfaces dominate in practice: the supply chain of tools and skills an agent installs, and the identity fabric that says which agent is acting for whom.

## MCP Supply-Chain Attack Classes

The MCP ecosystem inherits package-registry threats and adds a new one: tool metadata is model-readable instruction space. [[sources/Invariant Labs MCP Tool Poisoning]] is the canonical disclosure and named the classes.

| Attack class | Mechanism | Status |
|---|---|---|
| Tool poisoning | Malicious instructions in tool or parameter descriptions, invisible to the user but trusted by the model | Demonstrated against Anthropic, OpenAI, Zapier, and Cursor clients at disclosure ([[sources/Invariant Labs MCP Tool Poisoning]]) |
| Rug pull | A server or package builds trust with clean releases, then ships a malicious update the client re-trusts silently | In the wild: [[sources/Koi Security Postmark MCP Backdoor]] — 15 clean npm releases, then one line BCC-ing every outbound email to an attacker; ~300 organizations estimated affected |
| Cross-server shadowing | A malicious server's instructions redirect a co-connected trusted server's behavior (e.g. rerouting `send_email`) | Demonstrated ([[sources/Invariant Labs MCP Tool Poisoning]], WhatsApp exfiltration follow-up) |
| Skill-marketplace campaigns | Malicious agent skills distributed through official marketplaces, with the agent itself surfacing the fake install step to the user | In the wild at scale: [[sources/Koi Security ClawHavoc]] — 341 of 2,857 ClawHub skills malicious at first scan (7.7–11.9% across snapshots), 335 in one macOS-stealer campaign |
| Client-config execution | Repository- or project-provided configuration executes on open: lifecycle hooks, auto-enabled MCP servers, redirected API endpoints | Disclosed and patched: [[sources/Check Point Claude Code Project Files RCE]] (CVE-2025-59536, CVSS 8.7), plus 30+ MCP-ecosystem CVEs tallied in early 2026 |

Distribution-side mitigation is thin: [[sources/MCP Registry]] namespaces servers to DNS/GitHub identity but moderates by reactive community denylisting, which the Postmark incident postdates trust decisions by construction. Client-side scanning (Invariant's mcp-scan), pinned tool descriptions, and treating minor version bumps of agent-invoked packages as trust events are the current practical controls. [[sources/MCP Specification 2026-07-28 Release Candidate]] hardens authorization (RFC 9207 issuer validation) but does not address tool-description trust. Offense already uses the same plumbing: [[sources/Anthropic Disrupting AI Espionage]] documents a state-sponsored campaign running Claude Code with off-the-shelf MCP tools at 80–90% autonomy.

## Agent Identity and Delegation

The 2026 identity stack is converging on short-lived, workload-style credentials instead of static API keys:

- [[sources/IETF AIMS Agent Auth Draft]] is the cross-vendor blueprint: one WIMSE/SPIFFE identifier per agent, short-lived credentials, mTLS plus proof tokens, per-scenario OAuth flows, and transaction tokens to limit lateral movement.
- [[sources/Identity Assertion JWT Authorization Grant]] standardizes cross-domain delegation: the enterprise IdP becomes the policy decision point for agent-to-app access instead of N-by-M pairwise consents.
- [[sources/Microsoft Entra Agent ID]] is the largest deployment: directory-visible identities for every Foundry/Copilot Studio agent, blueprint inheritance for fleets, conditional access, and audit logging — GA as of June 2026.
- [[sources/Cloudflare Signed Agents]] covers the web-facing leg: RFC 9421 message signatures replacing IP and user-agent heuristics for agent traffic at third-party origins.
- [[sources/Infisical Agent Vault]] handles the credential-exposure half: a brokering proxy injects real credentials below the application layer so a prompt-injected agent cannot sweep secrets it never held.

Design rule of thumb: identity answers "which agent, for whom, with what standing"; supply-chain controls answer "is what the agent is about to execute the thing that was reviewed." Both are required — a perfectly authenticated agent running a rug-pulled server is still compromised.

## Related

- [[protocols/A2A]]
- [[protocols/MCP]]
- [[protocols/agent protocol governance]]
- [[safety/prompt injection]]
- [[safety/sandbox escape and credential exposure]]
- [[safety/agent safety and security]]
- [[operations/permissions]]
- [[concepts/agent skills]]

## Related Sources

- [[sources/A2ASecBench|A2ASecBench: A Protocol-Aware Security Benchmark for Agent-to-Agent Multi-Agent Systems]]
- [[sources/A2A Specification|Agent2Agent Protocol Specification]]
- [[sources/Anthropic Disrupting AI Espionage|Disrupting the First Reported AI-Orchestrated Cyber Espionage Campaign]]
- [[sources/Building A Secure Agentic AI Application Leveraging A2A Protocol|Building A Secure Agentic AI Application Leveraging A2A Protocol]]
- [[sources/Check Point Claude Code Project Files RCE|RCE and API Token Exfiltration Through Claude Code Project Files]]
- [[sources/Cloudflare Signed Agents|Cryptographically Recognizing Agent Traffic (Signed Agents)]]
- [[sources/IETF AIMS Agent Auth Draft|AI Agent Authentication and Authorization (AIMS)]]
- [[sources/Identity Assertion JWT Authorization Grant|Identity Assertion JWT Authorization Grant (ID-JAG)]]
- [[sources/Infisical Agent Vault|Agent Vault: The Open Source Credential Proxy and Vault for Agents]]
- [[sources/Invariant Labs MCP Tool Poisoning|MCP Security Notification: Tool Poisoning Attacks]]
- [[sources/Koi Security ClawHavoc|ClawHavoc: 341 Malicious ClawHub Skills]]
- [[sources/Koi Security Postmark MCP Backdoor|First Malicious MCP in the Wild: The Postmark Backdoor]]
- [[sources/MCP Authorization|MCP Authorization]]
- [[sources/MCP Registry|Introducing the MCP Registry]]
- [[sources/MCP Security Best Practices|MCP Security Best Practices]]
- [[sources/MCP Specification 2026-07-28 Release Candidate|The 2026-07-28 MCP Specification Release Candidate]]
- [[sources/Microsoft Entra Agent ID|What is Microsoft Entra Agent ID?]]
- [[sources/TAMAS|TAMAS: Benchmarking Adversarial Risks in Multi-Agent LLM Systems]]
