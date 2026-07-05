---
title: "Leveraging AI for Efficient Incident Response"
aliases:
  - "Meta incident response ranker"
source_type: "article"
kind: "incident-rca"
status: "verified"
year: 2024
publication_date: "2024-06-24"
publication_date_basis: "vendor_blog_page"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Meta (Engineering at Meta blog)"
venue: "Engineering at Meta blog"
url: "https://engineering.fb.com/2024/06/24/data-infrastructure/leveraging-ai-for-efficient-incident-response/"
pdf_url: ""
artifacts:
  - "raw/articles/meta-ai-incident-response.md"
created: 2026-07-03
updated: 2026-07-05
---

# Meta AI Incident Response

## Summary

- Two-stage root-cause-change identification: heuristic retrieval (code/directory ownership plus runtime code graphs) narrows thousands of candidate changes to hundreds, then an LLM ranker reduces them to a top-5 list.
- The ranker is a fine-tuned Llama 2 7B that scores changes in batches of 20 and aggregates picks "election"-style to produce the final five.
- Achieves 42% accuracy at identifying the root-cause change at investigation creation time for Meta's web monorepo.
- Training recipe: continued pre-training on internal wikis and code, then supervised fine-tuning on ~5,000 instruction examples, each containing 2-20 candidate changes with a known root cause.
- Explicit risk posture: confidence gating so low-confidence answers are not recommended (precision over reach), plus closed feedback loops and explainability so engineers can independently validate results.

## Connections

- [[concepts/code factories]]
- [[sources/RCACopilot]]
- [[sources/Sentry Seer]]
- [[sources/Meta Agentic Program Repair]]

## Artifacts

- [[raw/articles/meta-ai-incident-response.md]]

## Notes

- Canonical URL: https://engineering.fb.com/2024/06/24/data-infrastructure/leveraging-ai-for-efficient-incident-response/
- Connects incident response directly to the change stream of a monorepo: root-cause candidates are code changes, not telemetry categories — a different decomposition than RCACopilot.
- 42% accuracy is at investigation creation time on Meta's internal distribution; vendor-reported, no external replication.
