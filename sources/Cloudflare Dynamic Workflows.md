---
title: "Introducing Dynamic Workflows: durable execution that follows the tenant"
aliases:
  - "Cloudflare Dynamic Workflows"
  - "@cloudflare/dynamic-workflows"
source_type: "article"
status: "verified"
year: 2026
publication_date: "2026-05-01"
publication_date_basis: "cloudflare_visible_published_date"
source_updated_date: null
source_updated_date_basis: null
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Dan Lapid"
  - "Luís Duarte"
venue: "Cloudflare"
url: "https://blog.cloudflare.com/dynamic-workflows/"
pdf_url: ""
artifacts:
  - "raw/articles/cloudflare-dynamic-workflows.md"
created: 2026-06-01
updated: 2026-06-01
---

# Introducing Dynamic Workflows: durable execution that follows the tenant

## Summary

- Cloudflare article introducing `@cloudflare/dynamic-workflows`, a library that routes durable Workflow runs back into tenant-, repo-, request-, or agent-specific Dynamic Worker code.
- Important because it combines dynamic code loading with durable execution: agent-written plans can become retryable, hibernating, resumable Cloudflare Workflows instead of transient tool-call sequences.
- Connects Cloudflare's agent stack across Dynamic Workers, Durable Object Facets, Artifacts, Workflows, Project Think, and sandboxed execution.

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[systems/Cloudflare Agents SDK]]
- [[operations/agent harnesses]]
- [[operations/agent infrastructure]]
- [[operations/durable sessions]]
- [[operations/sandboxes]]
- [[operations/agent observability]]
- [[concepts/durable dormant agents]]
- [[methods/agentic workflow search]]

## Artifacts

- [[raw/articles/cloudflare-dynamic-workflows.md]]

## Notes

- Canonical URL: https://blog.cloudflare.com/dynamic-workflows/
- Publication date basis: visible Cloudflare blog date.
- Main design idea: wrap the Workflow binding so `create()` stores routing metadata, then dispatch the later `run(event, step)` call back into the right Dynamic Worker.
