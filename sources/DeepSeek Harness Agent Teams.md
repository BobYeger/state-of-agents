---
title: "DeepSeek Harness Agent Teams"
aliases:
  - "DeepSeek Agent Teams"
  - "@deepseek-ai/dsh-experimental-agent-team"
  - "@deepseek-ai/dsh-experimental-tool-agent-team"
source_type: "repository"
kind: "experimental-agent-team-implementation"
status: "verified"
year: 2026
publication_date: "2026-08-14"
publication_date_basis: "feature_commit_author_date"
source_updated_date: "2026-08-21"
source_updated_date_basis: "pinned_release_commit_author_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "DeepSeek AI"
venue: "GitHub"
url: "https://github.com/deepseek-ai/deepseek-harness"
pdf_url: ""
license: "MIT"
license_url: "https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/LICENSE"
evidence_class: "open-source-experimental-implementation-and-maintainer-documentation"
metrics_status: "implementation-and-test-evidence-without-performance-results"
artifacts: []
created: 2026-08-24
updated: 2026-08-24
---

# DeepSeek Harness Agent Teams

## Summary

- DeepSeek Harness implements an opt-in Agent Teams domain over its durable continuable-child sessions. A runtime root is the Lead of a flat named roster; teammates are direct continuable children, while ordinary subagents and forks remain outside that roster.
- The Lead's append-only Session log owns a durable peer mailbox. A send is flushed before delivery, carries a stable message id and sender identity into the target history, and receives a durable delivered acknowledgment only after the target inbox or history records it.
- Quiet `send_message` does not wake an inactive teammate; `followup_task` makes the message the target's next FIFO turn and can cold-resume it. Recovery retries queued-minus-delivered mail in target order and de-duplicates against the target Session.
- A shared task board stores complete revisioned snapshots and a dependency DAG. Compare-and-set mutations reject stale revisions; task ownership and path `writeScopes` coordinate work, but write scopes are advisory and do not lock the filesystem.

## Coordination and Authority

Only the Lead creates or interrupts teammates, while every Team member can address peers and use the task board subject to owner and revision checks. Fresh teammates start without parent history; forked teammates receive the Lead's completed-turn prefix but not the in-flight delegation turn. `wait_agent` waits on a post-registration roster, mailbox, task, or status edge and requires callers to re-read authoritative state after waking.

All members share one process and checkout. The Team layer provides no automatic worktree, branch, merge, filesystem lock, remote teammate, nested team, or automatic release of abandoned task ownership. The Lead remains responsible for work partitioning, final-diff review, and tests.

## Release and Evidence Boundary

This card audits repository tag `dsh-v0.1.1-rc.2` at commit `b150a551b8d465e31e418e1b2eaf5e79bbb7d28e`, dated August 21, 2026. The implementation exists in `packages/experimental/agent-team` and `packages/experimental/tool-agent-team`, and both manifests are `private: true`.

Repository policy mechanically excludes every package under `packages/experimental/` from the dsh pack and publish set and prevents released packages from depending on them. Agent Teams therefore is inspectable implementation evidence, but not a shipped stable DeepSeek Harness capability. Its delivery guarantee is process-local retry plus target-Session de-duplication, explicitly not cross-process exactly-once delivery; it also has no mailbox timeline UI.

The repository documents extensive unit, persistence, lifecycle, invariant, and composition tests, but no controlled comparison of team versus single-agent quality, latency, cost, or reliability. Prompt policy and task ownership coordinate agents; they are not confinement mechanisms.

## Connections

- [[sources/DeepSeek Harness Repository]]
- [[concepts/cross-session agent communication]]
- [[concepts/agent teams]]
- [[operations/agent harnesses]]
- [[operations/durable sessions]]
- [[operations/worktree isolation]]
- [[maps/Harness Tracker]]

## Notes

- Audited snapshot and release tag: https://github.com/deepseek-ai/deepseek-harness/tree/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e
- Agent Teams design note: https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/.agents/notes/implemented/feature/2026-08-05-agent-teams.md
- Runtime package: https://github.com/deepseek-ai/deepseek-harness/tree/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/packages/experimental/agent-team
- Model-facing tools: https://github.com/deepseek-ai/deepseek-harness/tree/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/packages/experimental/tool-agent-team
- Release-exclusion decision: https://github.com/deepseek-ai/deepseek-harness/blob/b150a551b8d465e31e418e1b2eaf5e79bbb7d28e/.agents/notes/implemented/architecture/2026-08-18-experimental-agent-teams-packages.md
- Feature implementation commit: https://github.com/deepseek-ai/deepseek-harness/commit/3546f595b96ad1f1094a4b7a986333d6c299ebe2
- No repository content was copied into the vault.
