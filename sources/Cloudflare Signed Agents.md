---
title: "The age of agents: cryptographically recognizing agent traffic (Signed Agents)"
aliases:
  - "Signed Agents"
  - "Web Bot Auth"
source_type: "article"
kind: "agent-traffic-identity"
status: "verified"
year: 2025
publication_date: "2025-08-28"
publication_date_basis: "vendor_blog_page"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Jin-Hee Lee"
venue: "Cloudflare blog"
url: "https://blog.cloudflare.com/signed-agents/"
pdf_url: ""
created: 2026-07-03
updated: 2026-07-03
---

# Cloudflare Signed Agents

## Summary

- Defines "signed agents" as a traffic category distinct from verified bots: user-controlled agents whose HTTP requests are cryptographically signed via Web Bot Auth, with Cloudflare validating message signatures at the edge.
- Built on RFC 9421 HTTP Message Signatures, following the draft-meunier-web-bot-auth-architecture Internet-Draft.
- Initial signed-agent cohort at launch: OpenAI ChatGPT agent, Block's Goose, Browserbase, Anchor Browser, and Cloudflare Browser Rendering.
- Agents register through the Cloudflare dashboard bot submission form and elect signed-agent versus verified-bot classification.
- Replaces IP-range and user-agent heuristics with per-request cryptographic attribution — the web-facing leg of agent identity, addressed to third-party origins rather than the agent's own enterprise IdP.

## Connections

- [[operations/agent infrastructure]]
- [[safety/agent safety and security]]
- [[sources/IETF AIMS Agent Auth Draft]]
- [[sources/Microsoft Entra Agent ID]]
- [[systems/ChatGPT agent]]

## Notes

- Canonical URL: https://blog.cloudflare.com/signed-agents/
- Vendor blog post announcing a Cloudflare product feature; the classification categories and edge-validation behavior are Cloudflare-specific even though the signature mechanism (RFC 9421) is a standard.
- Complements enterprise-IdP identity (Entra Agent ID, AIMS): this covers how agents identify themselves to arbitrary web origins, not how they authenticate inside an organization.
