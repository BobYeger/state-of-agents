---
title: "The Multi-Agent Architecture That Actually Ships"
aliases:
  - "Factory Missions multi-agent architecture"
  - "Missions: Multi-Agent Systems That Ship for Days"
  - "Luke Alvoeiro Factory talk"
source_type: "talk"
kind: "vendor-architecture-talk"
status: "verified"
year: 2026
publication_date: "2026-05-06"
publication_date_basis: "youtube_upload_date"
event_date: null
youtube_upload_date: "2026-05-06"
source_updated_date: "2026-07-14"
source_updated_date_basis: "capture_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Luke Alvoeiro"
creator: "AI Engineer (channel); Luke Alvoeiro (Factory)"
venue: "AI Engineer channel (conference event unverified)"
url: "https://www.youtube.com/watch?v=ow1we5PzK-o"
pdf_url: ""
medium: "video"
platform: "youtube"
video_id: "ow1we5PzK-o"
duration_seconds: 1110
language: "en"
transcript_status: "captured"
transcript_type: "youtube-auto-captions"
transcript_language: "en"
transcript_review_status: "claim-ranges-spot-checked"
transcript_storage: "local-only"
transcript_locator: ".private/talk-transcripts/The Multi-Agent Architecture That Actually Ships - transcript.md"
transcript_sha256: "b9467c8fe342643d7b828c04e10535de43132364fb0a20cfeae01c1a4e291cc4"
caption_source_artifact: "not-retained"
capture_tool_version: "not-recorded"
capture_command: "not-recorded"
evidence_class: "vendor-operator-report"
metrics_status: "vendor-reported"
created: 2026-07-14
updated: 2026-07-14
---

# The Multi-Agent Architecture That Actually Ships

## Summary

- Factory's Missions architecture composes four coordination strategies — delegation, creator-verifier separation, broadcast through shared state, and negotiation at milestone boundaries — into a three-role system of orchestrator, workers, and validators.
- The most transferable mechanism is a **validation contract written during planning, before implementation**. It defines correctness independently of the code and maps every feature to one or more assertions, so tests are not allowed to merely ratify implementation decisions.
- In the architecture described in this May 2026 talk, shared-artifact mutation is serial: one worker or validator runs at a time, while read-only search, API research, and code review may fan out internally. This is a dated architecture claim, not a guarantee about every current Missions execution mode.
- Each worker starts with clean context and hands off a committed working tree plus a structured record of completed and omitted work, commands and exit codes, discovered issues, and procedure compliance. Validators also start clean, making verification adversarial by design.
- Validation has two layers: scrutiny (tests, types, lint, and clean-context code-review agents) and behavioral QA (launch the live application and exercise user flows through computer use). The speaker says behavioral execution consumes most mission wall time.
- Most orchestration policy lives in prompts and skills — about 700 lines of text in the reported implementation — while deterministic code stays thin and handles bookkeeping, validation gates, and unresolved handoff issues. This is directly relevant to building a model-improving rather than model-pinned harness.

## Architecture and Control Loop

```text
human goal
  -> orchestrator clarifies scope
  -> plan + milestones + implementation-independent validation contract
  -> clean-context worker implements one feature and commits
  -> structured handoff enters shared mission state
  -> scrutiny validator + behavioral validator
  -> orchestrator scopes corrective work at milestone boundary
  -> repeat until every contract assertion is covered
```

The architecture deliberately separates intelligence from discipline. Models plan, implement, review, and adapt; deterministic machinery records state, enforces unresolved-issue gates, and invokes validation. It is also model-agnostic by role: planning, implementation, and validation can use different model families, and the talk suggests cross-provider validation as one way to reduce correlated bias.

## Timestamped Claims

- **04:03–05:07:** Missions combines delegation, creator-verifier, broadcast, and negotiation; the orchestrator produces features, milestones, and a validation contract defining done before coding begins.
- **05:13–06:00:** workers receive clean context and commit their feature before the next worker; validators check behavior, not only code shape.
- **06:23–06:53:** tests written after implementation can confirm the implementation's own decisions, so correctness assertions are authored during planning and assigned across features.
- **06:57–08:06:** scrutiny and user-testing validators run after milestones; neither has seen the implementation before, making validation intentionally adversarial.
- **08:19–09:00:** structured handoffs retain completed and omitted work, commands, exit codes, issues, and procedure compliance; milestone failures create scoped corrective work.
- **09:06–10:23:** the longest reported Mission ran 16 days. Feature mutation is serial, with parallelism reserved for read-only work; the claimed error-rate improvement is not quantified.
- **10:30–11:17:** Mission Control exposes completion, budget consumption, active work, handoffs, discoveries, and course corrections for asynchronous supervision.
- **11:22–12:59:** model selection is role-specific and provider-agnostic; validation contracts and milestone checkpoints are claimed to let weaker or open-weight models participate successfully.
- **13:08–13:57:** in the presented Slack-clone run, Factory reports about 60% of time and tokens going to implementation, validation never passing first try, roughly half the final lines being tests, and 90% test coverage. [[sources/Factory How Missions Work]] is the primary written source for the exact values; neither source provides comparative evidence.
- **14:48–15:47:** orchestration is mostly prompts and skills rather than a hard-coded state machine; thin deterministic logic performs bookkeeping and blocks progress on unresolved handoff issues.

## Claims

- [[claims/Claim - Agent teams need explicit organization]]
- [[claims/Claim - Context management is an agent architecture choice]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[sources/Factory How Missions Work]]
- [[maps/MAS Orchestration and Architecture]]
- [[maps/Harness Design Playbook]]
- [[maps/Code Factory Playbook]]
- [[methods/multi-agent orchestration]]
- [[concepts/subagent context isolation]]
- [[concepts/handoff over compaction]]
- [[concepts/loop engineering]]
- [[concepts/code factories]]
- [[operations/agent observability]]
- [[operations/agent evals]]
- [[sources/Cognition Multi-Agents Whats Actually Working]]
- [[sources/Factory 2.0 Software Factory]]
- [[sources/Anthropic Effective Harnesses for Long-Running Agents]]

## Local Capture

- Private transcript: `.private/talk-transcripts/The Multi-Agent Architecture That Actually Ships - transcript.md`
- SHA-256: `b9467c8fe342643d7b828c04e10535de43132364fb0a20cfeae01c1a4e291cc4`
- The original VTT or JSON3 caption artifact and capture command were not retained. The normalized transcript is therefore useful for timestamp lookup but not a lossless caption archive.

## Evidence Boundary

This is unusually concrete operator evidence, but it remains a vendor conference talk. Architecture descriptions and product behavior are direct source claims; the 16-day maximum and adoption claims are not independently audited. The talk supplies no controlled comparison of the architecture it describes against a parallel or single-agent baseline, and “error rate drops dramatically” is not accompanied by a measured rate. Use [[sources/Factory How Missions Work]] as the primary source for the April 2026 architecture and exact Slack-clone telemetry.

## Notes

- Canonical URL: https://www.youtube.com/watch?v=ow1we5PzK-o (AI Engineer channel; YouTube title and upload metadata captured 2026-07-14).
- Event date and venue remain unverified; the YouTube upload date is recorded separately rather than being inferred as the event date.
- The source calls the product “Missions” and the monitoring surface “Mission Control.”
- The local transcript preserves normalized YouTube-generated English captions with timestamps; automatic-caption errors remain possible, and only cited claim ranges were spot-checked.
- Factory's current [Missions product page](https://factory.ai/product/missions), checked 2026-07-14, advertises parallel Droid execution. The public sources do not resolve whether that is a newer topology or parallelism at a different task granularity, so the serial-mutation description is scoped to this talk and the April article.
