---
title: "The 2026-07-28 MCP Specification Release Candidate"
aliases:
  - "MCP 2026-07-28 RC"
  - "stateless MCP"
source_type: "article"
kind: "protocol-spec-revision"
status: "verified"
year: 2026
publication_date: "2026-05-21"
publication_date_basis: "project_blog_page"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Model Context Protocol core maintainers"
venue: "Model Context Protocol blog"
url: "https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/"
pdf_url: ""
artifacts:
  - "raw/articles/mcp-specification-2026-07-28-release-candidate.md"
created: 2026-07-03
updated: 2026-07-05
---

# MCP Specification 2026-07-28 Release Candidate

## Summary

- Next MCP spec revision string is 2026-07-28; the release candidate froze on May 21, 2026, with final publication scheduled July 28, 2026 after a 10-week SDK validation window. No final revision shipped after 2025-11-25 as of early July 2026.
- Headline change is statelessness: the initialize/initialized handshake and Mcp-Session-Id header are removed, so servers can run behind a plain round-robin load balancer with no sticky routing or shared session store.
- New Mcp-Method and Mcp-Name HTTP headers enable routing without body inspection; client metadata moves to _meta on each request; Multi-Round-Trip Requests replace SSE streams for elicitation.
- Extensions framework becomes official with reverse-DNS identifiers and independent versioning; MCP Apps and a redesigned stateless Tasks ship as the first two extensions.
- Roots, Sampling, and Logging are deprecated with 12-month minimum removal windows; authorization is hardened with RFC 9207 iss validation.
- Companion context: the 2026 MCP Roadmap (blog, March 9, 2026) shifted planning from fixed releases to working-group-driven development, with a contributor ladder and SEP authority delegated to working groups.

## Connections

- [[protocols/MCP]]
- [[protocols/agent protocol governance]]
- [[sources/MCP Specification 2025-11-25]]
- [[sources/MCP Governance and Stewardship]]
- [[operations/agent infrastructure]]
- [[operations/durable sessions]]

## Artifacts

- [[raw/articles/mcp-specification-2026-07-28-release-candidate.md]]

## Notes

- Canonical URL: https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
- Release-candidate caveat: details may change before final publication on 2026-07-28; re-verify against the published spec revision after that date.
- Supersedes the 2025-11-25 revision carded in this vault ([[sources/MCP Specification 2025-11-25]]) once final.
