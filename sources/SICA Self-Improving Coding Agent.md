---
title: "A Self-Improving Coding Agent (SICA)"
aliases:
  - "SICA"
source_type: "paper"
kind: "self-improving-coding-agent"
status: "verified"
year: 2025
publication_date: "2025-04-21"
publication_date_basis: "arxiv_abs_page"
source_updated_date: "2025-05-16"
source_updated_date_basis: "arxiv_v2_revision_date"
arxiv_id: "2504.15228"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Maxime Robeyns"
  - "Martin Szummer"
  - "Laurence Aitchison"
venue: "arXiv (ICLR 2025 SSI-FM workshop)"
url: "https://arxiv.org/abs/2504.15228"
pdf_url: "https://arxiv.org/pdf/2504.15228"
created: 2026-07-03
updated: 2026-07-03
---

# SICA Self-Improving Coding Agent

## Summary

- A single agent edits its own codebase directly, collapsing the meta-agent/target-agent split used by ADAS and the Darwin Godel Machine.
- Selection policy is a greedy hill-climb over an archive: each iteration resumes from the highest-utility archived version, where utility combines benchmark score with cost and runtime penalties.
- Performance rose from 17% to 53% on a random 50-problem subset of SWE-bench Verified, with additional gains on LiveCodeBench and synthetic agent benchmarks.
- Improvement is purely non-gradient: driven by LLM reflection and code edits, with no weight updates.
- Runs inside a Docker sandbox with an asynchronous overseer LLM that monitors the event stream and can cancel runaway runs.
- v1 2025-04-21, v2 2025-05-16; code released at MaximeRobeyns/self_improving_coding_agent.

## Claims

- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[methods/self-improving code loops]]
- [[methods/runtime supervision]]
- [[operations/sandboxes]]
- [[sources/Darwin Godel Machine]]
- [[sources/ADAS]]
- [[sources/SWE-bench Verified]]

## Notes

- Canonical URL: https://arxiv.org/abs/2504.15228
- The utility function (score minus cost/runtime penalties) is the simplest concrete selection policy in the self-improving-agent lineage; HGM and later selection-policy work benchmark against it.
- SWE-bench Verified numbers are on a 50-problem random subset, not the full benchmark — not directly comparable to full-set scores.
