# MCP

Model Context Protocol is an interoperability protocol for connecting agents and models to tools, data sources, and external systems. A client (the agent application) speaks JSON-RPC to servers that expose tools, resources, and prompts; the protocol standardizes discovery, invocation, and authorization so one integration works across vendors.

Launched by Anthropic in November 2024 ([[sources/Anthropic Introducing MCP]]), MCP is now the de facto tool-protocol layer of the agent stack: 10,000+ active public servers and 97M+ monthly SDK downloads at the December 2025 foundation transfer, vendor-reported ([[sources/Anthropic MCP Donation and Agentic AI Foundation]]).

## Spec State as of 2026-08

The current final revision is **2026-07-28** ([[sources/MCP Specification 2026-07-28]]). It is a breaking revision whose central change is a stateless protocol core:

- **No protocol handshake or session.** `initialize`/`notifications/initialized` and `Mcp-Session-Id` are retired. Protocol version and client capabilities are required on every request; client identity is recommended. Servers must implement `server/discover`, but calling it is optional for clients. Applications may still expose explicit state handles as tool arguments rather than relying on transport-hidden state.
- **Stateless interaction.** Multi Round-Trip Requests replace server-initiated elicitation, sampling, and roots requests with an input-required result and a retry of the original operation. If a server supplies opaque `requestState`, the client echoes it unchanged; the server validates it when it affects security-sensitive logic.
- **Gateway and cache surfaces.** Streamable HTTP requires `Mcp-Method` on every request and `Mcp-Name` on `tools/call`, `resources/read`, and `prompts/get`. Cache metadata applies to `tools/list`, `prompts/list`, `resources/list`, `resources/read`, and `resources/templates/list`; only `tools/list` has an explicit deterministic-order recommendation.
- **Extensions and Tasks.** The extensions framework becomes formal. The final changelog calls `io.modelcontextprotocol/tasks` an official extension, but the current Tasks repository still labels itself experimental and not official; treat maturity as unresolved. MCP Apps and Enterprise Managed Authorization are other named extensions.
- **Authorization and deprecation.** RFC 9207 issuer validation and issuer-bound credentials harden OAuth flows; Dynamic Client Registration, Roots, Sampling, and Logging are deprecated under a minimum 12-month window. HTTP+SSE had already been deprecated since `2025-03-26` and is now classified under that lifecycle policy. Deprecated features remain functional during the window but should not be adopted by new implementations.

The TypeScript, Python, Go, and C# Tier 1 SDKs shipped support with the revision. Compatibility must still be negotiated: implementations built around the 2025-11-25 session model, experimental Tasks API, former server-initiated request flow, or SSE stream resumption need explicit migration.

| Revision | Status as of 2026-08 | Vault source |
|---|---|---|
| 2024-11 (launch) | Historical | [[sources/Anthropic Introducing MCP]] |
| 2025-06-18 | Superseded; auth/security lineage | [[sources/MCP Authorization]], [[sources/MCP Security Best Practices]] |
| 2025-11-25 | Superseded final revision | [[sources/MCP Specification 2025-11-25]] |
| 2026-07-28 | Current final revision; published 2026-07-28 | [[sources/MCP Specification 2026-07-28]] |

**Supersession note.** The vault's [[sources/MCP Authorization]] and [[sources/MCP Security Best Practices]] cards capture the 2025-06-18 lineage, while [[sources/MCP Specification 2026-07-28 Release Candidate]] records the pre-release design and validation window. Their threat framing and history remain useful, but quote [[sources/MCP Specification 2026-07-28]] and the versioned live specification for current normative requirements.

## Registry and Distribution

The official MCP Registry launched in preview at registry.modelcontextprotocol.io in September 2025 and remains pre-GA as of 2026-07 ([[sources/MCP Registry]]): a central authoritative catalog with standardized server.json metadata, DNS/GitHub-based namespacing, and public or private sub-registries sharing the same API. Its moderation is a reactive denylist — flagged servers are removed after the fact — which makes server distribution a live supply-chain surface: [[sources/Invariant Labs MCP Tool Poisoning]] shows tool descriptions themselves carrying injected instructions, and [[sources/Koi Security Postmark MCP Backdoor]] documents a trojaned server exfiltrating mail in production. Registry presence is discoverability, not vetting.

[[concepts/agent plugins|Agent Plugins 1.0]] adds a portable package configuration above MCP: an optional root `mcp.json` can carry client connection definitions, and a package may also carry Agent Skills ([[sources/Agent Plugins Specification]]). It does not change MCP's wire, lifecycle, or authorization semantics and should not be confused with the MCP Registry's server-authored `server.json` metadata.

## Governance

Technical governance runs through the SEP process and a maintainer hierarchy formalized in July 2025, with working groups producing proposals and core maintainers voting ([[sources/MCP Governance and Stewardship]]). In December 2025 Anthropic donated MCP to the Agentic AI Foundation under the Linux Foundation, co-founded with Block and OpenAI; the donation moved IP and funding without changing the maintainer-led technical process ([[sources/Anthropic MCP Donation and Agentic AI Foundation]]). The 2026 roadmap shifted planning from fixed releases to working-group-driven development, and the 2026-07-28 revision completed the first 10-week SDK validation cycle under that process ([[sources/MCP Specification 2026-07-28 Release Candidate]], [[sources/MCP Specification 2026-07-28]]). Event-level history is in [[protocols/agent protocol governance]].

Enterprise deployment patterns — gateways, access control, audit, and the "shadow MCP" sprawl problem — are covered by [[sources/Cloudflare Scaling MCP Adoption]].

## Related

- [[protocols/agent protocols]]
- [[protocols/agent protocol governance]]
- [[protocols/A2A]]
- [[concepts/tool use]]
- [[concepts/dynamic tool discovery]]
- [[concepts/agent plugins]]
- [[safety/protocol security]]
- [[operations/agent infrastructure]]

## Related Sources

- [[sources/Anthropic Introducing MCP|Introducing the Model Context Protocol]]
- [[sources/Agent Plugins Specification]]
- [[sources/MCP Specification 2026-07-28|MCP Specification 2026-07-28]]
- [[sources/MCP Specification 2025-11-25|MCP Specification 2025-11-25]]
- [[sources/MCP Specification 2026-07-28 Release Candidate]]
- [[sources/MCP Registry]]
- [[sources/MCP Governance and Stewardship]]
- [[sources/Anthropic MCP Donation and Agentic AI Foundation]]
- [[sources/MCP Authorization|MCP Authorization]]
- [[sources/MCP Security Best Practices|MCP Security Best Practices]]
- [[sources/Cloudflare Scaling MCP Adoption]]
- [[sources/Cloudflare MCP Auth Durable Objects|Piecing together the Agent puzzle: MCP, authentication & authorization, and Durable Objects free tier]]
- [[sources/Cloudflare Code Mode MCP]]
- [[sources/Cloudflare Code Mode MCP API]]
- [[sources/OpenAI Codex CLI Agents SDK Cookbook]]
- [[sources/MCP-Zero]]
- [[sources/ScaleMCP]]
- [[sources/Invariant Labs MCP Tool Poisoning]]
- [[sources/Koi Security Postmark MCP Backdoor]]
- [[sources/Anthropic Managed Agents Sandboxes MCP Tunnels]]
- [[sources/Anthropic Managed Agents|Scaling Managed Agents: Decoupling the brain from the hands]]
