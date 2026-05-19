---
title: "autoresearch"
aliases:
  - "karpathy/autoresearch"
source_type: "repository"
status: "verified"
year: 2026
publication_date: "2026-03-06"
publication_date_basis: "github_created_at"
source_updated_date: "2026-03-26"
source_updated_date_basis: "github_pushed_at"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Andrej Karpathy"
venue: "GitHub"
url: "https://github.com/karpathy/autoresearch"
pdf_url: ""
artifacts:
  - "raw/articles/karpathy-autoresearch_README.md"
  - "raw/articles/karpathy-autoresearch_program.md"
created: 2026-05-18
updated: 2026-05-18
---

# autoresearch

## Summary

- Repository for autonomous AI research over a small but real single-GPU LLM training setup derived from nanochat.
- The agent edits only `train.py`, runs fixed five-minute experiments, evaluates `val_bpb`, keeps improvements, discards regressions, and repeats.
- The human-facing control surface is `program.md`, which acts like lightweight research-organization code for the agent loop.
- Useful concrete example of long-horizon coding/research agents operating through a tight experiment-evaluate-commit/revert loop.

## Connections

- [[systems/autoresearch]]
- [[methods/agentic workflow search]]
- [[concepts/long-horizon agents]]

## Artifacts

- [[raw/articles/karpathy-autoresearch_README.md]]
- [[raw/articles/karpathy-autoresearch_program.md]]

## Notes

- Canonical URL: https://github.com/karpathy/autoresearch
- Publication date basis: GitHub repository `created_at`.
- Source updated date basis: GitHub repository `pushed_at`.
- GitHub snapshot on 2026-05-18: 81,661 stars, 11,864 forks, 181 open issues; default branch `master`.
- Latest observed commit on `master`: `228791fb499afffb54b46200aca536f79142f117`.
- GitHub API license field was null, while the README states MIT.
