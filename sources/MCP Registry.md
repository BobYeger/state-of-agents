---
title: "Introducing the MCP Registry"
aliases:
  - "MCP Registry"
  - "registry.modelcontextprotocol.io"
source_type: "article"
kind: "tool-discovery-infrastructure"
status: "verified"
year: 2025
publication_date: "2025-09-08"
publication_date_basis: "project_blog_page"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "David Soria Parra"
  - "Adam Jones"
  - "Tadas Antanavicius"
  - "Toby Padilla"
  - "Theodora Chu"
venue: "Model Context Protocol blog"
url: "https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/"
pdf_url: ""
created: 2026-07-03
updated: 2026-07-03
---

# MCP Registry

## Summary

- September 8, 2025: official MCP Registry launched in preview at registry.modelcontextprotocol.io as an open catalog and API for public MCP servers.
- Architecture: a central authoritative registry with an OpenAPI spec feeds public sub-registries (client marketplaces that augment upstream data) and private enterprise sub-registries sharing the same API schemas.
- Server metadata is standardized via server.json; namespacing ties server names to DNS or GitHub identity.
- Moderation is community-driven: flagged servers (spam, malicious code, impersonation) are denylisted and retroactively removed by maintainers.
- Began as a grassroots effort in February 2025 with contributors from PulseMCP, Goose, and others (16 individuals, 9+ companies); the preview explicitly carried no durability guarantees and allowed breaking changes before GA. Still not GA as of July 2026.

## Connections

- [[protocols/MCP]]
- [[concepts/dynamic tool discovery]]
- [[operations/agent infrastructure]]
- [[safety/protocol security]]
- [[sources/MCP Specification 2025-11-25]]

## Notes

- Canonical URL: https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/
- Preview-status caveat: API surface and durability guarantees may have changed since the announcement; the registry remained pre-GA as of July 2026.
- Denylist moderation is reactive (retroactive removal after community flagging), which matters for supply-chain threat modeling of MCP server distribution.
