---
title: "The Dual LLM pattern for building AI assistants that can resist prompt injection"
aliases:
  - "Dual LLM pattern"
source_type: "article"
kind: "injection-defense-pattern"
status: "verified"
year: 2023
publication_date: "2023-04-25"
publication_date_basis: "blog_post_date"
authors:
  - "Simon Willison"
venue: "simonwillison.net (blog)"
url: "https://simonwillison.net/2023/Apr/25/dual-llm-pattern/"
artifacts:
  - "raw/articles/willison-dual-llm-pattern.md"
created: 2026-07-03
updated: 2026-07-05
---

# The Dual LLM Pattern

## Summary

- Origin (April 2023) of the quarantined-LLM pattern: a Privileged LLM takes input only from trusted sources and holds all tool access; a Quarantined LLM processes potentially malicious content, is "expected to go rogue at any moment", and has no tools.
- A non-LLM Controller passes untrusted content by reference as variables ($VAR1, $VAR2); the Privileged LLM never sees the raw text, only placeholders.
- Core rule: unfiltered content output by the Quarantined LLM is never forwarded to the Privileged LLM.
- Willison states the costs upfront: implementation complexity, degraded UX, and residual attacks via social engineering and dialog fatigue.
- The page carries a 2025 update noting that CaMeL identified flaws in the proposal (exfiltration via data dependencies) and improved on it — making this the documented ancestor of the 2025-26 provable-defense line.

## Connections

- [[safety/prompt injection]]
- [[concepts/tool use]]
- [[sources/CaMeL]]
- [[sources/Design Patterns for Securing LLM Agents]]
- [[sources/Willison Lethal Trifecta]]

## Artifacts

- [[raw/articles/willison-dual-llm-pattern.md]]

## Notes

- Canonical URL: https://simonwillison.net/2023/Apr/25/dual-llm-pattern/
- Blog post, not peer-reviewed; its historical value is as the source of the privileged/quarantined split that CaMeL, FIDES, and the Design Patterns paper refine.
