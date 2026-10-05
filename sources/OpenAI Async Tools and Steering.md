---
title: "OpenAI asynchronous tools and mid-turn steering"
aliases: []
source_type: "docs"
kind: "agent-loop-runtime-contract"
status: "verified"
year: 2026
publication_date: "2026-09-03"
publication_date_basis: "official_API_changelog_feature_date"
source_updated_date: "2026-10-05"
source_updated_date_basis: "documentation_access_date_not_release_date"
authors:
  - "OpenAI"
venue: "OpenAI API documentation"
url: "https://developers.openai.com/api/docs/guides/async-tool-calling"
evidence_class: "official-runtime-documentation"
artifacts: []
created: 2026-10-05
updated: 2026-10-05
---

# OpenAI Async Tools and Steering

Async function/custom calls let the model continue while application-owned work runs; later outputs retain the original call identifier. This does not move job execution or recovery into the provider. Support starts with GPT-6 Astra. It applies to application function/custom tools, not hosted tools or programmatic tool calling; in multi-agent mode, it must not be combined with parallel tool calls. Background response generation is a separate feature.

[Mid-turn steering](https://developers.openai.com/api/docs/guides/steering) queues new user input over a WebSocket. Acceptance does not mean application. Steering neither undoes effects nor cancels started tools; queued steering is connection-local and requires explicit recovery after a disconnect.

The [September 3 changelog](https://developers.openai.com/api/docs/changelog) establishes release timing. These are interface contracts, not comparative reliability measurements.

## Connections

- [[concepts/agent loop]]
- [[concepts/background agents]]
- [[concepts/event-driven agents]]
- [[operations/durable sessions]]
- [[sources/LLMCompiler]]
