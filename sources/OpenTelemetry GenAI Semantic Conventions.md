---
title: "OpenTelemetry GenAI Semantic Conventions (dedicated repository)"
aliases:
  - "OTel GenAI semconv"
  - "gen_ai semantic conventions"
source_type: "spec"
kind: "telemetry-spec"
status: "verified"
year: 2026
publication_date: "2026-05-05"
publication_date_basis: "github_repo_created_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "OpenTelemetry GenAI SIG (CNCF)"
venue: "GitHub (open-telemetry/semantic-conventions-genai)"
url: "https://github.com/open-telemetry/semantic-conventions-genai"
pdf_url: ""
created: 2026-07-03
updated: 2026-07-03
---

# OpenTelemetry GenAI Semantic Conventions

## Summary

- The GenAI semantic conventions were split out of the main open-telemetry/semantic-conventions repo into a dedicated repository created 2026-05-05; the opentelemetry.io pages under /docs/specs/semconv/gen-ai/ are now deprecation stubs pointing here.
- Defines spans, metrics, and events for GenAI client inference, agents, tool execution, evaluation, and MCP operations — doc files include gen-ai-spans.md, gen-ai-agent-spans.md, gen-ai-events.md, gen-ai-metrics.md, gen-ai-exceptions.md, and mcp.md.
- Provider-specific convention docs exist for Anthropic, AWS Bedrock, Azure AI Inference, and OpenAI; the auto-generated registry covers the `gen_ai.*`, `mcp.*`, and `openai.*` attribute namespaces.
- Status is still "Development" (not stable). Transition mechanism: existing instrumentations default to the old attribute format, and users opt into the new one via `OTEL_SEMCONV_STABILITY_OPT_IN=gen_ai_latest_experimental`, with semconv v1.36 as the transition baseline.
- Key attributes already adopted by vendors: `gen_ai.operation.name`, `gen_ai.provider.name`, `gen_ai.request.model`, `gen_ai.usage.input_tokens`/`output_tokens`.
- Uses the Weaver tool to manage dependencies on core OTel semantic conventions; 565 commits and no tagged releases as of 2026-07.

## Connections

- [[operations/agent observability]]
- [[operations/agent infrastructure]]
- [[protocols/MCP]]
- [[sources/MCP Specification 2025-11-25]]

## Notes

- Canonical URL: https://github.com/open-telemetry/semantic-conventions-genai
- This is the wire-format anchor for agent/LLM telemetry: vendor tracing platforms (Langfuse, Braintrust, Arize, etc.) map to or emit these attributes.
- Spec is explicitly pre-stable; attribute names may still change before a tagged release, so pin the semconv version when instrumenting.
