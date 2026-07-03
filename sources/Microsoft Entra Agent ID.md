---
title: "What is Microsoft Entra Agent ID?"
aliases:
  - "Entra Agent ID"
  - "Agent identity blueprints"
source_type: "docs"
kind: "agent-identity-platform"
status: "verified"
year: 2026
publication_date: "2026-04-14"
publication_date_basis: "microsoft_learn_page_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Microsoft"
venue: "Microsoft Learn docs"
url: "https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id"
pdf_url: ""
created: 2026-07-03
updated: 2026-07-03
---

# Microsoft Entra Agent ID

## Summary

- Announced in public preview at Build (May 2025); every agent created in Azure AI Foundry and Copilot Studio automatically receives a directory-visible identity via a new "Agent ID" application type in the Entra admin center.
- "Agent identity blueprints" are templates with parent-child relationships so one security policy propagates across large fleets of derived agent identities.
- Third-party agents (e.g. AWS Bedrock, n8n) onboard via the Microsoft Entra Auth SDK sidecar or workload identity federation.
- Platform supports OAuth 2.0, MCP, and A2A for agent authentication and agent-to-agent communication.
- The full Entra security stack extends to agents: Conditional Access (Entra ID P1), Identity Protection risky-agent detection (P2), Identity Governance, network controls via Secure Web AI Gateway, and complete sign-in/audit logging. Requires a per-user Microsoft Agent 365 license (bundled in Microsoft 365 E7).
- Generally available to all Entra customers as of the June 2026 docs update — no longer preview.

## Connections

- [[operations/agent infrastructure]]
- [[operations/permissions]]
- [[safety/agent safety and security]]
- [[protocols/A2A]]
- [[protocols/MCP]]

## Notes

- Canonical URL: https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id
- Living docs page (dated 2026-04-14, last updated 2026-06-24); details like licensing bundles may shift between snapshots.
- The largest deployed system granting agents first-class enterprise directory identities; complements the IETF standards track ([[sources/IETF AIMS Agent Auth Draft]]) rather than implementing it.
