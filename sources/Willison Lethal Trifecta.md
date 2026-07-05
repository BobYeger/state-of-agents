---
title: "The lethal trifecta for AI agents: private data, untrusted content, and external communication"
aliases:
  - "Lethal trifecta"
source_type: "article"
kind: "threat-model"
status: "verified"
year: 2025
publication_date: "2025-06-16"
publication_date_basis: "blog_post_date"
authors:
  - "Simon Willison"
venue: "simonwillison.net (blog)"
url: "https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/"
artifacts:
  - "raw/articles/willison-lethal-trifecta.md"
created: 2026-07-03
updated: 2026-07-05
---

# The Lethal Trifecta for AI Agents

## Summary

- Names the trifecta: access to private data, exposure to untrusted content, and ability to communicate externally; any agent combining all three is exfiltration-vulnerable regardless of model quality.
- Backed by documented production exploits: Microsoft 365 Copilot (June 2025), GitHub's official MCP server (May 2025), GitLab Duo (May 2025), plus earlier cases in ChatGPT, Bard, Amazon Q, NotebookLM, Slack, Grok, and the Claude iOS app.
- Argues against probabilistic guardrails: vendors claiming to catch "95% of attacks" fail the security bar — "in web application security 95% is very much a failing grade".
- Endorses exactly two mitigation directions: the Design Patterns paper's constrained-input patterns and DeepMind's CaMeL.
- Design rule: once an agent ingests untrusted input it must be constrained so that input cannot trigger consequential actions; end users composing third-party MCP tools must avoid assembling the trifecta themselves.

## Connections

- [[safety/prompt injection]]
- [[safety/agent safety and security]]
- [[safety/sandbox escape and credential exposure]]
- [[sources/MCP Security Best Practices]]
- [[sources/CaMeL]]
- [[sources/Design Patterns for Securing LLM Agents]]

## Artifacts

- [[raw/articles/willison-lethal-trifecta.md]]

## Notes

- Canonical URL: https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
- Practitioner heuristic, not a formal result; it is the threat-model shorthand much of the 2025-26 defense literature (including Meta's "Rule of Two") is written against.
- The exploit list is as-reported by Willison from vendor disclosures; individual incidents should be verified against the linked advisories before quoting.
