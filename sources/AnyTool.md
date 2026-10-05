---
title: "AnyTool: Self-Reflective, Hierarchical Agents for Large-Scale API Calls"
aliases:
  - "AnyTool"
source_type: "paper"
kind: "hierarchical-tool-discovery"
status: "verified"
year: 2024
publication_date: "2024-02-06"
publication_date_basis: "arxiv_v1_submission_history"
source_updated_date: "2024-02-06"
source_updated_date_basis: "arxiv_v1"
arxiv_id: "2402.04253"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Yu Du"
  - "Fangyun Wei"
  - "Hongyang Zhang"
venue: "arXiv"
url: "https://arxiv.org/abs/2402.04253"
pdf_url: "https://arxiv.org/pdf/2402.04253v1"
artifacts: []
created: 2026-10-05
updated: 2026-10-05
---

# AnyTool

## Summary

- Uses GPT-4 agents arranged by category and tool to discover candidates from 16K+ RapidAPI APIs. A separate solver attempts execution; failure reactivates discovery and solving rather than accepting the original candidate set.

## Evidence and Limits

- Table 2 reports 73.8% pass rate on AnyToolBench, versus 36.6% for ToolLLM retrieval with a GPT-4 solver. Table 3 ablates hierarchy and reflection; both matter in the tested subsets.
- The authors identify an evaluation failure: treating queries judged unsolvable with retrieved tools as passes rewards poor retrieval. Their revised protocol counts solved requests directly and filters infeasible queries.
- Results depend on API availability, GPT-4 judging, benchmark construction, and repeated calls. Table 12 reports approximately 136,000 tokens and 43.3 calls per query on average; discovery quality is not evidence of cheap execution.
- Read v1, including Tables 2–3 and 12. [Author repository](https://github.com/dyabel/AnyTool).

## Connections

- [[concepts/dynamic tool discovery]]
- [[methods/multi-agent orchestration]]
- [[operations/agent evals]]
- [[sources/Gorilla]]
- [[sources/MCP-Zero]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
