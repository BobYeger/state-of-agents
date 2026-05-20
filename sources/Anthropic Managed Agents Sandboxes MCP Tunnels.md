---
title: "New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels"
aliases:
  - "Claude Managed Agents self-hosted sandboxes"
  - "Claude Managed Agents MCP tunnels"
source_type: "article"
status: "verified"
year: 2026
publication_date: "2026-05-19"
publication_date_basis: "claude_visible_published_date"
source_updated_date: null
source_updated_date_basis: null
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Anthropic"
venue: "Claude"
url: "https://claude.com/blog/claude-managed-agents-updates"
pdf_url: ""
artifacts:
  - "raw/articles/anthropic-managed-agents-sandboxes-mcp-tunnels.md"
  - "raw/docs/anthropic-self-hosted-sandboxes-docs.md"
  - "raw/docs/anthropic-mcp-tunnels-docs.md"
created: 2026-05-20
updated: 2026-05-20
---

# Claude Managed Agents self-hosted sandboxes and MCP tunnels

## Summary

- Describes a managed-harness pattern where the agent loop stays on Anthropic infrastructure while tool execution can move into a customer-controlled sandbox.
- Introduces MCP tunnels as a private network bridge for reaching internal MCP servers without exposing them publicly.
- Important for separating model orchestration, execution boundary, network policy, and private tool access.

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Connections

- [[operations/sandboxes]]
- [[operations/agent infrastructure]]
- [[operations/durable sessions]]
- [[protocols/MCP]]
- [[systems/Cloudflare Agents SDK]]

## Artifacts

- [[raw/articles/anthropic-managed-agents-sandboxes-mcp-tunnels.md]]
- [[raw/docs/anthropic-self-hosted-sandboxes-docs.md]]
- [[raw/docs/anthropic-mcp-tunnels-docs.md]]

## Notes

- Canonical URL: https://claude.com/blog/claude-managed-agents-updates
- This is included for the execution-boundary and private-tool-access architecture, not as generic product coverage.
