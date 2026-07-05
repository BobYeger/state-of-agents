---
title: "Agent Vault: The Open Source Credential Proxy and Vault for Agents"
aliases:
  - "agent-vault"
source_type: "article"
kind: "credential-broker"
status: "verified"
year: 2026
publication_date: "2026-04-22"
publication_date_basis: "vendor_blog_page"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Tony Dang"
venue: "Infisical blog"
url: "https://infisical.com/blog/agent-vault-the-open-source-credential-proxy-and-vault-for-agents"
pdf_url: ""
artifacts:
  - "raw/articles/infisical-agent-vault.md"
created: 2026-07-03
updated: 2026-07-05
---

# Agent Vault: Open Source Credential Proxy for Agents

## Summary

- TLS-terminating forward proxy purpose-built for agent workloads: the agent sets `HTTPS_PROXY=<agent_credential>:vault@<url>` and trusts a local CA; the vault intercepts CONNECT tunnels, strips any credential the agent attached, injects the real credential from its encrypted store, then opens a separate verified TLS connection upstream.
- Threat model is prompt-injection-driven credential exfiltration — an attacker telling the agent to "sweep and return the secrets available in the agent's environment"; with brokering the agent never sees, stores, or logs the secret in any form.
- Allowlisting, rate limiting, audit logging, and per-agent credential scoping are enforced uniformly at the proxy layer, below the application layer, so the same control covers APIs, CLIs, SDKs, and MCP tools generically.
- Works with Claude Code, OpenClaw, Hermes, and custom harnesses; released as an open-source research preview at github.com/Infisical/agent-vault (announced 2026-04-22).

## Connections

- [[safety/sandbox escape and credential exposure]]
- [[safety/prompt injection]]
- [[operations/agent infrastructure]]
- [[operations/sandboxes]]
- [[sources/Anthropic Sandbox Runtime Repository]]

## Artifacts

- [[raw/articles/infisical-agent-vault.md]]

## Notes

- Canonical URL: https://infisical.com/blog/agent-vault-the-open-source-credential-proxy-and-vault-for-agents
- Repository: https://github.com/Infisical/agent-vault
- Generalizes the proxy-injected-credential pattern from Anthropic's git-proxy design into a vendor-neutral drop-in for any harness; research preview status, so maturity claims should be re-checked before recommending for production.
