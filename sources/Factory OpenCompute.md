---
title: "Introducing OpenCompute"
aliases: ["Factory OpenCompute"]
tags: [sources, code-factories]
source_type: "article"
status: "verified"
evidence_class: "vendor-architecture-report"
publication_date: "2026-10-14"
publication_date_basis: "visible_publication_date"
authors: ["Walker Hildebrand", "Sherry Bai"]
venue: "Factory"
url: "https://factory.com/news/opencompute"
created: 2026-11-09
updated: 2026-11-09
---

# Factory OpenCompute

## Architecture

A customer-hosted service manages agent-computer lifecycles. A Go control plane persists desired/observed state in Postgres and reconciles interrupted operations; standalone gRPC drivers implement provider behavior. Core conformance is mandatory, while suspend, snapshot, and fork are optional profiles tested separately.

Factory reports implementing providers through explicit contracts and conformance tests using Droids under human direction. This is an operational example of spec-bounded agent work, not a productivity experiment.

## Boundaries

The October announcement labels OpenCompute private preview and open sourcing as planned. It distinguishes customer-side compute from inference routing and session storage: local execution alone does not establish local data retention. Provider integrations differ in maturity.

## Connections

- [[concepts/code factories]]
- [[operations/agent infrastructure]]
- [[operations/durable sessions]]
- [[maps/Code Factory Playbook]]

## Primary Link

[Architecture, provider contract, and launch status](https://factory.com/news/opencompute).
