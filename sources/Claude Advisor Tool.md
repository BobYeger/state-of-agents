---
title: "Advisor tool"
aliases:
  - "Claude Advisor Tool"
  - "Anthropic Advisor Tool"
source_type: "docs"
kind: "runtime-routing"
status: "verified"
year: 2026
publication_date: "2026-07-13"
publication_date_basis: "accessed_living_docs_no_visible_publication_date"
source_updated_date: "2026-07-13"
source_updated_date_basis: "snapshot_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Anthropic"
venue: "Claude Platform Docs"
url: "https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool"
pdf_url: ""
artifacts:
  - "raw/docs/claude-advisor-tool.md"
created: 2026-07-13
updated: 2026-07-13
---

# Claude Advisor Tool

## Summary

- Beta server tool that lets a faster or cheaper executor consult a more capable advisor during one Messages request. The advisor receives the executor's full transcript, returns a plan or course correction, and the executor continues doing the work.
- Operationalizes asymmetric capacity without a full multi-agent application: expensive reasoning is concentrated at planning, architecture, risk, and completion checkpoints while most tool use and token generation remain with the executor.
- The advisor has no tools or context-management features of its own. Fable 5 and Mythos 5 advice is returned as an encrypted `advisor_redacted_result` that the client cannot inspect but the server feeds back to the executor; other supported advisors can return plaintext.
- Cost and reliability remain application responsibilities: cap calls per request with `max_uses`, cap advisor output, count conversation-level calls client-side, and enable advisor caching only when roughly three or more calls are expected.
- Anthropic's internal prompting results are sharply workload- and model-dependent: nudges can increase helpful consults, but early or forced calls can reduce performance when the executor lacks context or the work is a simple lookup. The docs repeatedly recommend measuring baseline call timing before adding routing prompts.

## Claims

- [[claims/Claim - Agent teams need explicit organization]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Connections

- [[methods/runtime routing]]
- [[methods/multi-agent orchestration]]
- [[operations/cost control]]
- [[operations/agent harnesses]]
- [[sources/Think Big Search Small]]
- [[sources/Claude Fable 5 Prompting Guide]]

## Artifacts

- [[raw/docs/claude-advisor-tool.md]]

## Notes

- Canonical URL: https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool
- Living beta documentation snapshot from 2026-07-13. The feature was not available on Amazon Bedrock, Google Cloud, or Microsoft Foundry at snapshot time.
- The advisor receives the whole transcript as quoted context, including system prompt, tools, prior turns, tool results, and current-turn text. This makes transcript length and sensitive context part of the routing decision.
