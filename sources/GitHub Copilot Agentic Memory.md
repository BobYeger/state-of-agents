---
title: "Building an agentic memory system for GitHub Copilot"
aliases:
  - "GitHub Copilot Agentic Memory"
  - "Copilot Memory"
source_type: "article"
kind: "vendor-engineering-report"
status: "verified"
year: 2026
publication_date: "2026-01-15"
publication_date_basis: "github_blog_visible_date"
source_updated_date: null
source_updated_date_basis: null
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Tiferet Gazit"
venue: "GitHub Blog"
url: "https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/"
pdf_url: ""
evidence_class: "vendor-engineering-report"
metrics_status: "vendor-reported-undisclosed-sample-size"
created: 2026-08-16
updated: 2026-08-16
---

# GitHub Copilot Agentic Memory

## Summary

- GitHub's deployed design stores repository facts with code-location citations. Agents create memories through a `store_memory` tool call, receive recent memories in later prompts, verify cited locations against the current branch before use, and correct or refresh a memory when the code supports a different fact.
- This just-in-time verification is the central architecture choice: GitHub avoids a heavyweight offline curation service and lets current code arbitrate stale, conflicting, abandoned-branch, or injected memories. Repository facts are shared across Copilot cloud agent, code review, and CLI, but remain scoped to the repository.
- Current documentation distinguishes repository-level facts from user-level preferences. Facts can be shared with repository users; preferences follow one user across repositories and are not applied by code review. Unused entries are deleted after 28 days, with the timer potentially reset after successful validation and use.
- GitHub reports that memory raised code-review precision by 3% and recall by 4% in its evaluation. In production A/B tests it reports a seven-point increase in coding-agent pull-request merge rate (90% vs. 83%) and a two-point increase in positive feedback on review comments (77% vs. 75%), with both A/B effects reported at `p < 0.00001`.

## Evidence Boundary

The architecture and measurements are first-party. GitHub does not disclose the number of repositories, pull requests, users, test cases, or A/B observations; it provides no confidence intervals, raw data, or independent replication. Its claim that agents rejected or repaired adversarial memories "across all test cases" is therefore useful operational evidence, not a quantified robustness guarantee. The 3% precision and 4% recall changes also lack baselines and are not identified as relative changes or percentage-point changes.

## Claims

- [[claims/Claim - Agent memory and skills create compounding improvement loops]]
- [[claims/Claim - Context management is an agent architecture choice]]

## Connections

- [[operations/agent memory]]
- [[concepts/shared agent memory]]
- [[concepts/versioned context]]
- [[sources/GitHub Copilot Coding Agent]]

## Notes

- [Engineering article](https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/) (2026-01-15).
- [Current concepts documentation](https://docs.github.com/en/copilot/concepts/agents/copilot-memory) and [memory-management documentation](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/copilot-memory).
- Changelog history: [public-preview launch](https://github.blog/changelog/2026-01-15-agentic-memory-for-github-copilot-is-in-public-preview/), [default-on for Pro and Pro+](https://github.blog/changelog/2026-03-04-copilot-memory-now-on-by-default-for-pro-and-pro-users-in-public-preview/), [scope/deletion/CLI controls](https://github.blog/changelog/2026-05-26-copilot-memory-has-more-controls-for-deletion-scope-and-the-copilot-cli/), and [Business/Enterprise user preferences and governance](https://github.blog/changelog/2026-06-02-copilot-memory-supports-user-preferences-for-business-enterprise/).
- The January engineering article describes the launch state as opt-in. The current documentation supersedes that availability detail: individual plans are on by default, while organization- and enterprise-managed plans require an administrator policy and allow individual opt-out.
