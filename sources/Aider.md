---
title: "Aider"
aliases:
  - "Aider coding agent"
source_type: "repository"
kind: "coding-agent-harness-repository"
status: "verified"
year: 2023
publication_date: "2023-05-09"
publication_date_basis: "github_repository_created_at"
source_updated_date: "2026-05-22"
source_updated_date_basis: "pinned_main_commit_author_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Aider maintainers"
venue: "GitHub"
url: "https://github.com/Aider-AI/aider"
pdf_url: ""
license: "Apache-2.0"
license_url: "https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/LICENSE.txt"
artifacts: []
evidence_class: "open-source-implementation-maintainer-documentation-and-project-benchmark"
metrics_status: "project-run-polyglot-benchmark-not-comparable-to-swe-bench"
created: 2026-08-19
updated: 2026-08-19
---

# Aider

## Summary

- Aider is an open-source terminal pair-programming harness whose durable design contributions predate the current autonomous-agent wave: explicit edit formats, git-native checkpoints, automated lint/test feedback, and token-budgeted repository maps.
- The loop assembles selected files plus a repository map, asks a model for edits in a declared format, applies them, optionally runs lint/tests, and feeds failures back for repair. Automatic commits make changes diffable and undoable, but Git rollback does not reverse shell, network, or external-service side effects.
- Its repository map extracts key symbols with tree-sitter, builds a dependency/reference graph, ranks relevant definitions, and selects the highest-value lines that fit the active token budget. This is a concrete early example of harness-managed context selection rather than whole-repository stuffing.
- Architect mode separates solution reasoning from edit production: one model proposes the change and a possibly different editor model converts it into a valid patch format. Historical gains were measured on Aider's own code-editing benchmark, so they show a within-harness mechanism effect rather than cross-harness superiority.

## Evaluation Boundary

- The repository includes a Dockerized Polyglot benchmark derived from Exercism tasks. Reports record model, edit format, commit hash, cost, malformed responses, and pass-at-try statistics, which makes harness changes reproducible within that suite.
- The benchmark evaluates the model-plus-Aider editing pipeline and is not SWE-bench; its scores should not be compared directly with SWE-bench Verified or used as present-day evidence that Aider outperforms current coding harnesses.
- Latest formal release `v0.86.0` was published August 9, 2025; audited main commit `5dc9490bb35f9729ef2c95d00a19ccd30c26339c` is dated May 22, 2026. Treat Aider as an active historical/mechanism baseline, not a current multi-agent or durable-runtime reference.

## Connections

- [[maps/Harness Tracker]]
- [[operations/agent harnesses]]
- [[concepts/task-aware context pruning]]
- [[methods/deliberative control]]
- [[sources/SWE-agent]]
- [[sources/Mini-SWE-agent]]

## Notes

- Canonical repository: https://github.com/Aider-AI/aider
- Audited main snapshot: https://github.com/Aider-AI/aider/tree/5dc9490bb35f9729ef2c95d00a19ccd30c26339c
- Latest formal release at this snapshot: https://github.com/Aider-AI/aider/releases/tag/v0.86.0
- Repository map: https://aider.chat/docs/repomap.html
- Architect/Editor mechanism and historical project-benchmark results: https://aider.chat/2024/09/26/architect.html
- Benchmark harness: https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/benchmark/README.md
- Lint/test loop: https://aider.chat/docs/usage/lint-test.html
- Git integration and undo: https://aider.chat/docs/git.html
- License: https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/LICENSE.txt
- No repository content was copied into the vault.
