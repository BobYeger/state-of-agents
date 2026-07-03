---
title: "Azure SRE Agent Documentation (Overview, Extensibility Primitives, AAU Pricing)"
aliases:
  - "Azure SRE Agent"
source_type: "docs"
kind: "sre-agent"
status: "verified"
year: 2026
publication_date: "2026-06-16"
publication_date_basis: "ms_learn_docs_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Microsoft (Azure docs)"
venue: "Microsoft Learn"
url: "https://learn.microsoft.com/en-us/azure/sre-agent/overview"
pdf_url: ""
created: 2026-07-03
updated: 2026-07-03
---

# Azure SRE Agent Docs

## Summary

- The agent is assembled from five extension primitives plus a permission gate: skills (marketplace runbooks/CLI scripts), five built-in subagents (architecture, logs+metrics, source code, root-cause analysis, scanning), Python tools, MCP servers (40+ connectors including Datadog, Prometheus, Grafana, Splunk, AWS CloudWatch, GCP Stackdriver), and agent hooks with two executor types — command hooks (deterministic CLI) and prompt hooks (LLM-evaluated, structured JSON output).
- The permission gate is a pre-execution safety layer that evaluates every proposed tool call (require human approval, enforce policy, or block); audit telemetry routes to the customer's own Application Insights; the docs state no change deploys without human sign-off.
- Incident flow: receive an alert from PagerDuty/ServiceNow/Azure Monitor, query the observability stack, generate a root-cause hypothesis plus proposed mitigations, and file a prefilled ticket. A worked example resolves a payment-service memory-leak page in 7 minutes by correlating an App Insights memory trend with a GitHub deployment commit two hours earlier.
- Billing is token-metered in Azure Agent Units (AAUs): always-on flow costs 4 AAUs/agent-hour; active flow is priced per model — Claude Opus 4.6 at 100/500/10/125 AAUs per 1M input/output/cache-read/cache-write tokens, GPT 5.3 Codex at 35/280/3.5/0 (pricing page ms.date 2026-05-12).
- Published task-shape economics: a quick question costs ~3.8 AAUs, an automated incident investigation ~35.3 AAUs (~200K input / 15K output tokens), a full diagnose-and-fix remediation ~86.5 AAUs on Opus 4.6 versus 30.1 on GPT 5.3 Codex; a monthly active-flow cap is settable from 500 to 1,000,000 AAUs and the agent goes unavailable when the cap is hit.
- Model provider is set per agent (Anthropic or OpenAI); the docs note Opus "often reaches a conclusion in fewer tool calls," offsetting higher per-token rates — an explicit cost-versus-depth model-routing guideline.

## Claims

- [[claims/Claim - Runtime control and verification improve agent reliability]] — the permission gate evaluates every proposed tool call before execution, and no change deploys without human sign-off.

## Connections

- [[operations/agent harnesses]]
- [[operations/permissions]]
- [[operations/cost control]]
- [[methods/hook-based control]]
- [[protocols/MCP]]
- [[concepts/code factories]]

## Notes

- Canonical URL: https://learn.microsoft.com/en-us/azure/sre-agent/overview
- Living documentation; publication date reflects the overview page's ms.date (2026-06-16). The AAU pricing figures come from the separate pricing-billing page (ms.date 2026-05-12) and may change.
- Per-task AAU figures and the 7-minute worked example are vendor-published; not independently verified.
