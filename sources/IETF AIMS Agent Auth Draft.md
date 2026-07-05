---
title: "AI Agent Authentication and Authorization (AIMS) — draft-klrc-aiagent-auth-02"
aliases:
  - "AIMS"
  - "draft-klrc-aiagent-auth"
  - "Agent Identity Management System"
source_type: "spec"
kind: "agent-identity-spec"
status: "verified"
year: 2026
publication_date: "2026-06-01"
publication_date_basis: "ietf_datatracker_version_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Pieter Kasselman"
  - "Jean-Francois Lombardo"
  - "Yaroslav Rosomakho"
  - "Brian Campbell"
  - "Nick Steele"
  - "Aaron Parecki"
venue: "IETF Internet-Draft (individual submission)"
url: "https://datatracker.ietf.org/doc/draft-klrc-aiagent-auth/"
pdf_url: ""
artifacts:
  - "raw/protocols/ietf-aims-agent-auth-draft.md"
created: 2026-07-03
updated: 2026-07-05
---

# IETF AIMS Agent Auth Draft

## Summary

- Defines AIMS (Agent Identity Management System): a layered conceptual stack composing WIMSE/SPIFFE identifiers, short-lived credentials (X.509, JWT-SVID, Workload Identity Tokens), runtime provisioning with posture assessment, authentication (mTLS at the transport layer; WIMSE proof tokens or HTTP Message Signatures at the application layer), OAuth 2.0 authorization, and monitoring via OpenID SSF/CAEP/RISC signals. Deliberately reuses existing standards rather than inventing new protocols.
- Normative rule: an agent MUST be assigned exactly one WIMSE identifier, which MAY be a SPIFFE ID.
- Names OAuth flows per scenario: authorization code + PKCE for user-delegated access, client credentials for autonomous access, JWT bearer grant, token exchange for cross-domain access, and Transaction Tokens for downscoped per-transaction access to reduce lateral movement.
- Explicitly replaces static API keys with short-lived cryptographic bindings as the credential model for agents.
- Cross-vendor authorship spans Defakto Security, AWS, Zscaler, Ping Identity, OpenAI, and Okta — the first unified agent-identity blueprint at IETF. Version history: -00 published 2026-03-02; -01 added Nick Steele (OpenAI); -02 (2026-06-01) added Aaron Parecki (Okta), posture-management terminology, clarified OAuth client authentication, and an Agent Mission section.

## Connections

- [[protocols/agent protocols]]
- [[operations/permissions]]
- [[safety/agent safety and security]]
- [[sources/MCP Authorization]]
- [[sources/Microsoft Entra Agent ID]]

## Artifacts

- [[raw/protocols/ietf-aims-agent-auth-draft.md]]

## Notes

- Canonical URL: https://datatracker.ietf.org/doc/draft-klrc-aiagent-auth/
- Individual submission, not yet working-group adopted; expires 2026-12-03 unless revised.
- Composition/architecture document — the actual mechanisms live in the referenced WIMSE, SPIFFE, OAuth, and SSF specifications.
