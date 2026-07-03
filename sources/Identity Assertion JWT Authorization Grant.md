---
title: "Identity Assertion JWT Authorization Grant (ID-JAG) — draft-ietf-oauth-identity-assertion-authz-grant-04"
aliases:
  - "ID-JAG"
  - "Cross App Access spec"
source_type: "spec"
kind: "delegation-spec"
status: "verified"
year: 2026
publication_date: "2026-05-21"
publication_date_basis: "ietf_datatracker_version_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Aaron Parecki"
  - "Karl McGuinness"
  - "Brian Campbell"
venue: "IETF OAuth Working Group Internet-Draft"
url: "https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-assertion-authz-grant/"
pdf_url: ""
created: 2026-07-03
updated: 2026-07-03
---

# Identity Assertion JWT Authorization Grant

## Summary

- Profile of the JWT Authorization Grant that gives a client delegated access to a resource in another trust domain on behalf of a user, without a direct user-approval step per app pair.
- Three-step flow: (1) client obtains an identity assertion from the IdP via standard SSO, (2) exchanges it at the IdP for an ID-JAG using OAuth 2.0 Token Exchange, (3) presents the ID-JAG at the resource authorization server's token endpoint to obtain an access token.
- Makes the enterprise IdP the central policy decision point for cross-domain agent-to-app access, replacing N-by-M pairwise app consents.
- WG-adopted by the IETF OAuth Working Group (replacing individual draft-parecki-oauth-identity-assertion-authz-grant); v04 dated 2026-05-21.
- This is the spec productized as Okta Cross App Access (XAA).

## Connections

- [[protocols/agent protocols]]
- [[operations/permissions]]
- [[sources/IETF AIMS Agent Auth Draft]]
- [[sources/MCP Authorization]]

## Notes

- Canonical URL: https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-assertion-authz-grant/
- Standards-track but still a draft; token-exchange semantics may change before RFC.
- Not agent-specific in its mechanics — it standardizes cross-domain delegation generally, with agents as the motivating client class.
