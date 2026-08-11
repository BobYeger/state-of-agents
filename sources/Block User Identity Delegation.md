---
title: "Who's Asking? Identity Delegation for AI Agents and Service Meshes"
aliases:
  - "Block User Identity Delegation"
  - "Subject actor consent delegation"
source_type: "article"
kind: "agent-identity-and-authorization-architecture"
status: "verified"
year: 2026
publication_date: "2026-07-06"
publication_date_basis: "block_engineering_visible_date"
source_updated_date: "2026-08-02"
source_updated_date_basis: "capture_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Franco Sola"
  - "Brett Caley"
  - "Cea Stapleton Cordasco"
venue: "Block Engineering"
url: "https://engineering.block.xyz/blog/whos-asking-identity-delegation-for-ai-agents-and-service-meshes"
pdf_url: ""
evidence_class: "vendor-architecture-report"
metrics_status: "architecture-description-no-outcome-evaluation"
artifacts:
  - "raw/articles/block-user-identity-delegation.md"
created: 2026-08-02
updated: 2026-08-02
---

# Who's Asking? Identity Delegation for AI Agents and Service Meshes

## Summary

- Block's internal delegation architecture preserves both the human **subject** and the software **actor** instead of using a broad shared service identity or letting software impersonate the human.
- An edge issuer supplies signed user context; token exchange supports work beyond the original request; a consent control plane records what the subject delegated to that actor; an authorization data plane resolves current authority at the downstream decision point.
- Effective delegated capabilities are the intersection of the user's current grants and the capabilities explicitly consented for that actor. Consent can narrow existing authority but cannot create it.
- The downstream service retains the final resource/action policy, and revocation is checked at decision time rather than treated as a property of an old token alone.
- This is a strong general model for long-running agent authority and audit, but it is **not evidence that Buzz implements the same OAuth/JWT consent plane**. Buzz's Nostr owner-attestation design has different scope and revocation semantics.

## Connections

- [[operations/agent identity]]
- [[operations/permissions]]
- [[sources/Block Buzz]]

## Artifacts

- [[raw/articles/block-user-identity-delegation]]

## Evidence Boundary

This is a first-party architecture description with no comparative outcome evaluation. It describes Block infrastructure adjacent to Buzz; the two systems should be compared conceptually, not conflated as one implementation.

## Notes

- Canonical URL: https://engineering.block.xyz/blog/whos-asking-identity-delegation-for-ai-agents-and-service-meshes
- Publication date: 2026-07-06.
