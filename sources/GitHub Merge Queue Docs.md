---
title: "Managing a merge queue (GitHub Docs)"
aliases:
  - "GitHub merge queue"
source_type: "docs"
kind: "merge-queue"
status: "verified"
year: 2026
publication_date: "2026"
publication_date_basis: "living_doc_current_version"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "GitHub"
venue: "docs.github.com"
url: "https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue"
pdf_url: ""
created: 2026-07-03
updated: 2026-07-03
---

# GitHub Merge Queue Docs

## Summary

- Merge queue guarantees FIFO merges where required checks always pass against the true post-merge state: queued PRs are grouped into a `merge_group` containing the latest base branch plus all PRs ahead in the queue, built on temporary `gh-readonly-queue/{base_branch}` branches.
- Build concurrency is configurable from 1 to 100 (maximum concurrent `merge_group` webhooks/CI builds), directly throttling queue velocity.
- Merge limits: minimum and maximum PRs merged into base at once are each configurable 1-100, plus a wait timeout that lets smaller groups merge when the queue is quiet — the batching knobs for deploy-per-merge pipelines.
- On CI failure the failing PR is automatically removed from the queue, the temporary branches are recreated without it, and remaining queued PRs are retested.
- "Jump the queue" prioritization exists but forces a full rebuild of all in-flight merge groups, slowing overall velocity — a concrete cost model for priority interrupts.

## Connections

- [[concepts/code factories]]
- [[concepts/issue tracker control plane]]
- [[sources/Cursor Self-Driving Codebases]]

## Notes

- Canonical URL: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue
- Living documentation with no stable publication date; the merge queue feature went GA in July 2023.
- Included because agent-produced PRs mostly flow through this mechanism today; its concurrency/batching/requeue semantics are the levers a factory tunes when PR volume becomes agent-scale.
