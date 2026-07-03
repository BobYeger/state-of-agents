# MCP

Model Context Protocol is an interoperability protocol for connecting agents and models to tools, data sources, and external systems. A client (the agent application) speaks JSON-RPC to servers that expose tools, resources, and prompts; the protocol standardizes discovery, invocation, and authorization so one integration works across vendors.

Launched by Anthropic in November 2024 ([[sources/Anthropic Introducing MCP]]), MCP is now the de facto tool-protocol layer of the agent stack: 10,000+ active public servers and 97M+ monthly SDK downloads at the December 2025 foundation transfer, vendor-reported ([[sources/Anthropic MCP Donation and Agentic AI Foundation]]).

## Spec State as of 2026-07

The current final revision is **2025-11-25** ([[sources/MCP Specification 2025-11-25]]). Relative to the 2025-06-18 revision it made three changes that matter for harness design:

- **Async tasks.** A Tasks primitive for long-running operations: instead of holding a connection open for the duration of a tool call, a server can accept work and let the client poll for completion — the protocol-level answer to tools that run for minutes or hours.
- **Extensions.** A mechanism for optional capabilities negotiated outside the core spec, so vendor and domain features can ship without forking the protocol.
- **Enterprise auth.** Authorization additions aimed at enterprise deployment, extending the OAuth-based model of the 2025-06-18 lineage toward centrally managed identity and client registration.

The next revision string is **2026-07-28**; its release candidate froze on 2026-05-21 with final publication scheduled after a 10-week SDK validation window ([[sources/MCP Specification 2026-07-28 Release Candidate]]). Its headline change is statelessness: the initialize handshake and session header are removed so servers can run behind plain load balancers; the extensions framework becomes official with reverse-DNS identifiers; **MCP Apps** (interactive UI surfaces served over MCP) and a redesigned stateless Tasks ship as the first two extensions; Roots, Sampling, and Logging are deprecated with 12-month removal windows; and authorization is hardened with RFC 9207 issuer validation. Until 2026-07-28 publishes, quote 2025-11-25 as normative.

| Revision | Status as of 2026-07 | Vault source |
|---|---|---|
| 2024-11 (launch) | Historical | [[sources/Anthropic Introducing MCP]] |
| 2025-06-18 | Superseded; auth/security lineage | [[sources/MCP Authorization]], [[sources/MCP Security Best Practices]] |
| 2025-11-25 | Current final revision | [[sources/MCP Specification 2025-11-25]] |
| 2026-07-28 | RC frozen 2026-05-21, final scheduled 2026-07-28 | [[sources/MCP Specification 2026-07-28 Release Candidate]] |

**Supersession note.** The vault's [[sources/MCP Authorization]] and [[sources/MCP Security Best Practices]] cards capture the 2025-06-18 lineage. Their threat framing and patterns remain useful, but the 2025-11-25 revision reworked authorization for enterprise deployment and 2026-07-28 tightens it further — do not quote those cards for current normative auth requirements. Re-verify auth and security claims against the live spec after 2026-07-28 ships.

## Registry and Distribution

The official MCP Registry launched in preview at registry.modelcontextprotocol.io in September 2025 and remains pre-GA as of 2026-07 ([[sources/MCP Registry]]): a central authoritative catalog with standardized server.json metadata, DNS/GitHub-based namespacing, and public or private sub-registries sharing the same API. Its moderation is a reactive denylist — flagged servers are removed after the fact — which makes server distribution a live supply-chain surface: [[sources/Invariant Labs MCP Tool Poisoning]] shows tool descriptions themselves carrying injected instructions, and [[sources/Koi Security Postmark MCP Backdoor]] documents a trojaned server exfiltrating mail in production. Registry presence is discoverability, not vetting.

## Governance

Technical governance runs through the SEP process and a maintainer hierarchy formalized in July 2025, with working groups producing proposals and core maintainers voting ([[sources/MCP Governance and Stewardship]]). In December 2025 Anthropic donated MCP to the Agentic AI Foundation under the Linux Foundation, co-founded with Block and OpenAI; the donation moved IP and funding without changing the maintainer-led technical process ([[sources/Anthropic MCP Donation and Agentic AI Foundation]]). The 2026 roadmap shifted planning from fixed releases to working-group-driven development ([[sources/MCP Specification 2026-07-28 Release Candidate]]). Event-level history is in [[protocols/agent protocol governance]].

Enterprise deployment patterns — gateways, access control, audit, and the "shadow MCP" sprawl problem — are covered by [[sources/Cloudflare Scaling MCP Adoption]].

## Related

- [[protocols/agent protocols]]
- [[protocols/agent protocol governance]]
- [[protocols/A2A]]
- [[concepts/tool use]]
- [[concepts/dynamic tool discovery]]
- [[safety/protocol security]]
- [[operations/agent infrastructure]]

## Related Sources

- [[sources/Anthropic Introducing MCP|Introducing the Model Context Protocol]]
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
