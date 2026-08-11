---
title: "The 2026-07-28 MCP Specification"
aliases:
  - "MCP 2026-07-28"
  - "MCP stateless specification"
  - "stateless MCP"
source_type: "article"
kind: "protocol-spec-revision"
status: "verified"
year: 2026
publication_date: "2026-07-28"
publication_date_basis: "project_blog_visible_published_date"
source_updated_date: null
source_updated_date_basis: null
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "David Soria Parra"
  - "Den Delimarsky"
venue: "Model Context Protocol blog"
url: "https://blog.modelcontextprotocol.io/posts/2026-07-28/"
pdf_url: ""
artifacts:
  - "raw/articles/mcp-specification-2026-07-28.md"
created: 2026-08-11
updated: 2026-08-11
---

# MCP Specification 2026-07-28

## Summary

- The final `2026-07-28` Model Context Protocol revision replaces the stateful `2025-11-25` transport model with a stateless protocol core. The `initialize`/`notifications/initialized` exchange and `Mcp-Session-Id` are retired. Protocol version and client capabilities are required on every request; client identity is recommended. Servers must implement `server/discover`, while clients may use it for capability discovery before another request.
- Statelessness is an infrastructure change, not a ban on application state. Servers that need continuity return explicit handles that clients or models pass back through ordinary tool arguments, allowing any request to land on any server instance without sticky routing or a shared protocol-session store.
- Multi Round-Trip Requests replace server-initiated requests for elicitation, sampling, and roots. A server returns an input-required result; the client obtains the requested input and retries the original request. Optional `requestState` is opaque to the client and, when present, must be echoed exactly.
- On Streamable HTTP, every request carries `Mcp-Method`; `Mcp-Name` is additionally required for `tools/call`, `resources/read`, and `prompts/get`. `ttlMs` and `cacheScope` apply to `tools/list`, `prompts/list`, `resources/list`, `resources/read`, and `resources/templates/list`; only `tools/list` has an explicit deterministic-order recommendation.
- The extensions framework is now formal. The changelog calls `io.modelcontextprotocol/tasks` an official extension, with poll-based `tasks/get`, `tasks/update`, and an opt-in notification stream; however, the current Tasks repository still labels itself experimental and not official. MCP Apps and Enterprise Managed Authorization are other named extensions.
- Authorization is hardened with RFC 9207 issuer validation and issuer-bound client credentials. Dynamic Client Registration, Roots, Sampling, and Logging enter a minimum 12-month deprecation window; HTTP+SSE was already deprecated since `2025-03-26` and is reclassified under the formal lifecycle policy.
- TypeScript, Python, Go, and C# Tier 1 SDKs shipped support with the specification. Immediate migration work is required for implementations that depend on protocol sessions, the old Tasks lifecycle, the former server-initiated request flow, or SSE stream resumption. Deprecated features remain functional during their offramp.

## Design Consequences

- MCP servers can scale behind ordinary round-robin HTTP load balancers, but application state must become explicit and portable rather than remaining hidden in transport sessions.
- Gateways gain a stable policy surface at the HTTP-header layer; this improves routing and authorization mechanics but does not solve tool-description poisoning, malicious packages, or registry trust.
- MRTR keeps interactive approval and elicitation possible without preserving a bidirectional transport session. If the server supplies `requestState`, the client must echo it unchanged and must not inspect it; the server must treat returned state as attacker-controlled and integrity-protect and verify it when it can affect authorization, resource access, or business logic.
- Clients should treat the revision as a migration target, not assume compatibility merely because the server still speaks MCP. Older SDKs may negotiate an earlier version, and deprecated capabilities remain available during their offramp.

## Connections

- [[protocols/MCP]]
- [[protocols/agent protocols]]
- [[protocols/agent protocol governance]]
- [[sources/MCP Specification 2026-07-28 Release Candidate]]
- [[sources/MCP Specification 2025-11-25]]
- [[operations/agent infrastructure]]
- [[operations/agent observability]]
- [[operations/durable sessions]]
- [[safety/protocol security]]

## Artifacts

- [[raw/articles/mcp-specification-2026-07-28.md]]

## Evidence Boundary

This is the official release announcement written by two MCP lead maintainers and linked to the versioned specification, changelog, migration guidance, and updated SDKs. It is authoritative for release status and first-party migration framing; the versioned specification and schema are normative for implementation requirements. Ecosystem-scale and performance claims in the announcement remain first-party adoption statements and are not independent evidence of production reliability.

## Notes

- Canonical release announcement: https://blog.modelcontextprotocol.io/posts/2026-07-28/
- Versioned specification: https://modelcontextprotocol.io/specification/2026-07-28
- This final release supersedes [[sources/MCP Specification 2026-07-28 Release Candidate]] for normative claims. The RC remains useful as a record of the validation window and working-group release process.
- The protocol no longer owns a session, but a tool or application may still expose explicit state handles. Do not collapse protocol statelessness into a claim that agent applications themselves are stateless.
- Tasks status is inconsistent across official project surfaces as of 2026-08-11: the final changelog calls it an official extension, while https://github.com/modelcontextprotocol/ext-tasks labels it experimental and says it is not an official extension.
