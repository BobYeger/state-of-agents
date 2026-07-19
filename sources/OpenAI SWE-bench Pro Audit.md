---
title: "Separating signal from noise in coding evaluations"
aliases:
  - "OpenAI SWE-bench Pro Audit"
  - "SWE-bench Pro audit"
source_type: "article"
kind: "benchmark-audit"
status: "verified"
year: 2026
publication_date: "2026-07-08"
publication_date_basis: "openai_visible_page_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "OpenAI"
venue: "OpenAI"
url: "https://openai.com/index/separating-signal-from-noise-coding-evaluations/"
pdf_url: ""
artifacts:
  - "raw/articles/openai-swe-bench-pro-audit.md"
created: 2026-07-13
updated: 2026-07-13
---

# Separating signal from noise in coding evaluations

## Summary

- Audits the 731-task public SWE-Bench Pro split after frontier-model pass rates rose from 23.3% to 80.3% in eight months. OpenAI's automated datapoint analysis flagged 200 tasks (27.4%) as broken; five-engineer human review identified 249 (34.1%).
- Finds four main validity failures: tests that enforce unstated implementation details, prompts that omit hidden requirements, tests with insufficient coverage that pass incomplete work, and misleading prompts that contradict the expected behavior.
- The pipeline first reviewed prompts, metadata, attempts, and failure traces, then used multiple Codex investigator passes inside task environments and a final researcher judgment. A parallel human campaign gave every flagged task to five experienced engineers.
- Human reviewers were more likely than the investigator agents to identify multiple overlapping faults. Their category judgments overlapped the agent pipeline in 74% of cases, suggesting the agent-assisted route was useful but conservative rather than a replacement for human review.
- OpenAI retracts its earlier recommendation to adopt SWE-Bench Pro and argues that difficult coding benchmarks should be authored and validated specifically as evaluations rather than reconstructed from pull requests whose prompts, patches, and tests served a different purpose.

## Claims

- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[sources/SWE-bench Pro]]
- [[sources/DeepSWE]]
- [[concepts/evaluator reliability]]
- [[operations/agent evals]]
- [[benchmarks/coding agent benchmarks]]
- [[sources/Rigorous Agentic Benchmarks]]

## Artifacts

- [[raw/articles/openai-swe-bench-pro-audit.md]]

## Notes

- Canonical URL: https://openai.com/index/separating-signal-from-noise-coding-evaluations/
- OpenAI both evaluated models on SWE-Bench Pro and performed this audit. The article publishes aggregate counts and methodology but not a replacement corrected leaderboard.
- The page was archived through a readable proxy because direct automated extraction returned HTTP 403; the source URL and claims remain the official OpenAI article.
