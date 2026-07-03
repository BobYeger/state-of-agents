---
title: "The OpenHands Software Agent SDK: A Composable and Extensible Foundation for Production Agents"
aliases:
  - "OpenHands V1"
source_type: "paper"
kind: "agent-sdk"
status: "verified"
year: 2025
publication_date: "2025-11-05"
publication_date_basis: "arxiv_abs_page"
source_updated_date: "2026-04-22"
source_updated_date_basis: "arxiv_v2_date"
arxiv_id: "2511.03690"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Xingyao Wang"
  - "Simon Rosenberg"
  - "Juan Michelini"
  - "Calvin Smith"
  - "Hoang Tran"
  - "Engel Nyst"
  - "Rohit Malhotra"
  - "Xuhui Zhou"
  - "Valerie Chen"
  - "Robert Brennan"
  - "Graham Neubig"
venue: "arXiv / MLSys 2026 (All Hands AI / CMU)"
url: "https://arxiv.org/abs/2511.03690"
pdf_url: "https://arxiv.org/pdf/2511.03690"
created: 2026-07-03
updated: 2026-07-03
---

# OpenHands Software Agent SDK

## Summary

- Complete architectural redesign of the agent components of the OpenHands framework (V1), superseding the ICLR 2025 platform paper (arXiv 2407.16741) as the canonical OpenHands architecture reference.
- Integrates native sandboxed execution, agent lifecycle control, model-agnostic multi-LLM routing, and built-in security analysis in a single SDK.
- Seamless local-to-remote execution portability via integrated REST/WebSocket services; interfaces include VSCode, VNC, browser, CLI, and APIs; a default agent needs only a few lines of code.
- Production deployment data: V1 substantially reduces system-attributable failures versus V0, with negligible event-sourcing overhead.
- v1 2025-11-05, v2 2026-04-22; accepted at MLSys 2026.

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Connections

- [[systems/OpenHands]]
- [[operations/agent harnesses]]
- [[operations/agent infrastructure]]
- [[operations/sandboxes]]
- [[sources/OpenHands]]

## Notes

- Canonical URL: https://arxiv.org/abs/2511.03690
- Refreshes the two-generation-old [[sources/OpenHands]] card (2024 platform paper); the two cards should be read as V0 platform vs V1 SDK.
- Failure-reduction figures come from the vendor's own production deployment data.
