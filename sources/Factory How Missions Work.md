---
title: "How Missions Work"
aliases:
  - "Factory Missions architecture"
  - "Factory How Missions Work"
  - "Missions architecture article"
source_type: "article"
kind: "vendor-architecture"
status: "verified"
year: 2026
publication_date: "2026-04-10"
publication_date_basis: "visible_page_date"
source_updated_date: "2026-07-14"
source_updated_date_basis: "capture_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Theo Luan"
creator: "Theo Luan (Factory)"
venue: "Factory.ai"
url: "https://factory.ai/news/missions-architecture"
pdf_url: ""
evidence_class: "vendor-architecture-report"
metrics_status: "vendor-reported-single-run"
artifacts:
  - "raw/articles/factory-how-missions-work.md"
created: 2026-07-14
updated: 2026-07-14
---

# How Missions Work

## Summary

- Factory describes Missions as an orchestrator-worker-validator system for multi-day software work. Each role receives a narrow objective and fresh context so implementation history does not become evaluation bias.
- The orchestrator writes an implementation-independent **validation contract before decomposing the project into features**. Every feature claims coverage of contract assertions, and fresh user-testing validators later exercise those assertions as black-box behavior.
- Mission state lives in shared artifacts: the validation contract, feature list, research notes, operating rules, and an evolving knowledge base. Workers and validators read the subset relevant to their role rather than inheriting one growing transcript.
- In this April 2026 architecture snapshot, a programmatic runner starts a worker for each feature **in order**, then triggers scrutiny and user-testing validation at milestone boundaries. The companion talk adds that read-only research and review may fan out internally.
- The article reports detailed telemetry for one Slack-clone Mission, but provides no single-agent, parallel-writer, or alternate-harness control. The run is concrete operator evidence, not a comparative evaluation.

## Architecture Snapshot

```text
human goal
  -> orchestrator clarifies requirements
  -> validation contract defines observable success
  -> contract is mapped to features and milestones
  -> fresh worker writes tests and implements one feature
  -> shared artifacts carry state across workers
  -> fresh scrutiny and user-testing validators evaluate a milestone
  -> orchestrator turns findings into bounded fix features
  -> milestone repeats until its contract assertions pass
```

The separation is incentive-aware. Workers implement but do not make the final correctness decision. Validators report gaps but do not repair them. The orchestrator plans and responds to evidence but delegates deep investigation so its own context remains focused.

## Reported Slack-Clone Run

| Measure | Factory-reported value |
|---|---:|
| Total runtime | 16.5 hours |
| Implementation | 9.98 hours / 60.5% |
| Validation | 6.14 hours / 37.2% |
| Total agent runs | 185 |
| Total tokens | 778.5M |
| Generated lines | 38.8K |
| Test share | 52.5% |
| Statement coverage | 89.25% |
| First-round milestone passes | 0 of 6 |
| Milestones passing by round four | 6 of 6 |
| Fix features / implementation features | 21 / 61 |
| Validator findings | 81 |

These measurements show how this one Mission spent its budget and converged. They do not establish that the architecture outperforms a simpler or more parallel alternative.

## Temporal Boundary

This card describes the architecture Factory published on 2026-04-10. Factory's current [Missions product page](https://factory.ai/product/missions), checked on 2026-07-14, advertises parallel Droid execution across independent subtasks. The public sources do not establish whether this is a later architecture, a different task granularity, or parallelism across repositories while shared-artifact mutation remains ordered. Do not generalize the April runner into a timeless claim that Missions is always serial.

## Claims

- [[claims/Claim - Agent teams need explicit organization]]
- [[claims/Claim - Context management is an agent architecture choice]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[sources/Factory Missions Multi-Agent Architecture Talk]]
- [[sources/Factory 2.0 Software Factory]]
- [[sources/Cognition Multi-Agents Whats Actually Working]]
- [[sources/Anthropic Effective Harnesses for Long-Running Agents]]
- [[maps/MAS Orchestration and Architecture]]
- [[maps/Harness Design Playbook]]
- [[maps/Code Factory Playbook]]
- [[methods/multi-agent orchestration]]
- [[concepts/subagent context isolation]]
- [[concepts/handoff over compaction]]
- [[operations/agent observability]]
- [[operations/agent evals]]

## Artifacts

- [[raw/articles/factory-how-missions-work.md]]

## Evidence Boundary

This is Factory's first-party written architecture report and the strongest primary source in the vault for the April 2026 Missions design. All performance numbers describe one vendor-selected run. The article supplies no controlled baseline, independent audit, uncertainty estimate, or evidence that the same topology remains current.

## Notes

- Canonical URL: https://factory.ai/news/missions-architecture
- Author and publication date are visible on the article page: Theo Luan, 2026-04-10.
- The structured capture retains metadata, architecture facts, and numeric telemetry without republishing the article verbatim.
