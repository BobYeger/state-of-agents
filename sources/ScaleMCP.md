---
title: "ScaleMCP: Dynamic and Auto-Synchronizing Model Context Protocol Tools for LLM Agents"
aliases:
  - "ScaleMCP"
source_type: "paper"
status: "verified"
year: 2025
publication_date: "2025-05-09"
publication_date_basis: "arxiv_published"
source_updated_date: "2025-05-09"
source_updated_date_basis: "arxiv_updated"
arxiv_id: "2505.06416"
citation_count: 0
citation_source: "OpenAlex"
citation_snapshot_date: "2026-05-20"
citation_lookup: "doi:10.48550/arxiv.2505.06416"
authors:
  - "Elias Lumer"
  - "Anmol Gulati"
  - "Vamse Kumar Subbiah"
  - "Pradeep Honaganahalli Basavaraju"
  - "James A. Burke"
venue: "arXiv"
url: "https://arxiv.org/abs/2505.06416"
pdf_url: "https://arxiv.org/pdf/2505.06416"
artifacts:
  - "raw/papers/scalemcp.pdf"
created: 2026-05-20
updated: 2026-10-05
---

# ScaleMCP

## Summary

- Dynamic MCP tool selection system with auto-synchronizing tool storage that treats MCP servers as the source of truth.
- Important because it addresses MCP-scale duplication, stale local tool repositories, and limited autonomy from pre-invocation retrieval.
- Connects dynamic tool discovery with tool memory and cost-aware tool exposure.

## Evidence and Limits

- The 5,000-server evaluation uses five deterministic financial-tool templates for each Fortune 1000 company, backed by yfinance. It is a constructed domain-specific workload, not 5,000 independently designed tool services.
- Sections 5.2–5.3 separate retrieval, correct tool invocation, and judged task completion. Table 3 reports o3 at 94.4% Task Completion but 36.1% Tool Correctness; plausible answers can conceal incorrect calls.
- Weighted tool-document embeddings do not uniformly beat concatenation. The authors note keyword-heavy tools and similarly generated synthetic queries as possible bias, and call for human-query testing.
- Automatic registry synchronization addresses freshness. It does not itself provide per-session version pinning or execution-time authorization. Full paper rechecked October 5, 2026.

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Connections

- [[concepts/dynamic tool discovery]]
- [[concepts/tool use]]
- [[protocols/MCP]]
- [[operations/cost control]]
- [[sources/Gorilla]]
- [[sources/Claude Mid-Conversation Tool Definitions]]

## Artifacts

- [[raw/papers/scalemcp.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2505.06416
- PDF URL: https://arxiv.org/pdf/2505.06416
