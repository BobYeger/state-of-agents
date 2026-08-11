# The 2026-07-28 MCP Specification — structured capture

- Canonical URL: https://blog.modelcontextprotocol.io/posts/2026-07-28/
- Versioned specification: https://modelcontextprotocol.io/specification/2026-07-28
- Authors: David Soria Parra and Den Delimarsky, MCP lead maintainers
- Publisher: Model Context Protocol project
- Publication date: 2026-07-28
- Captured: 2026-08-11
- Capture mode: metadata, release structure, protocol facts, and migration boundary; not a verbatim republication

## Release State

- The project officially published specification revision `2026-07-28` and matching Tier 1 SDK support on July 28, 2026.
- The TypeScript, Python, Go, and C# SDKs support the revision; Rust support was described as beta at publication.
- The release contains breaking changes, particularly for implementations that relied on transport sessions, the earlier Tasks API, the former server-initiated request flow, or SSE stream resumption.

## Protocol-Core Changes

- `initialize`/`notifications/initialized` and `Mcp-Session-Id` are retired.
- Every request carries its protocol version and client capabilities in `_meta`; clients SHOULD also identify themselves with `clientInfo`.
- Servers MUST implement `server/discover`; calling it before another operation is optional for clients.
- Requests can land on any stateless server instance. Stateful applications use explicit handles returned by tools and passed back as ordinary arguments.
- Multi Round-Trip Requests replace server-initiated requests for elicitation, sampling, and roots. The server returns an input-required result and may attach opaque `requestState`; if present, the client retries the original operation with collected inputs and echoes that state unchanged.

## Gateway, Cache, and Trace Changes

- Streamable HTTP requires `Mcp-Method` on every request and `Mcp-Name` on `tools/call`, `resources/read`, and `prompts/get`, giving gateways a header-level routing, authorization, metering, and filtering surface.
- `tools/list`, `prompts/list`, `resources/list`, `resources/read`, and `resources/templates/list` results carry `ttlMs` and `cacheScope`; `server/discover` is also cacheable. Only `tools/list` has an explicit recommendation for deterministic ordering.
- W3C Trace Context propagation is documented in `_meta`, standardizing `traceparent`, `tracestate`, and `baggage` names for distributed tracing.

## Extensions and Tasks

- Extensions use formal identifiers, delegated maintenance, and independent versioning.
- The final changelog describes Tasks as moving from the experimental core to the official `io.modelcontextprotocol/tasks` extension. At capture time, the extension repository still labels itself experimental and says it is not an official extension, so its maturity status is internally inconsistent across official project surfaces.
- The revised lifecycle includes `tasks/get` and `tasks/update`; notification delivery uses an opt-in `subscriptions/listen` stream.
- MCP Apps and Enterprise Managed Authorization are also named within the extensions ecosystem.

## Authorization and Deprecation

- Authorization servers SHOULD return `iss` under RFC 9207, and clients MUST validate any present value against the recorded issuer before code redemption.
- Client credentials are bound to the issuer that created them.
- Dynamic Client Registration is deprecated in favor of Client ID Metadata Documents.
- Roots, Sampling, and Logging are newly deprecated, with a minimum 12-month offramp before removal. HTTP+SSE had already been deprecated since `2025-03-26` and is formally reclassified under the same lifecycle policy.

## Capture Boundary

- This capture preserves protocol changes and migration implications from the official announcement.
- Partner quotations, adoption totals, and vendor performance statements are omitted because they are not needed to summarize the release mechanics and are not independent validation.
- Use the canonical specification and changelog for exact schemas, required fields, error semantics, and conformance decisions.
