---
title: "Beyond the basics with Claude Code"
aliases:
  - "Context Engineering: MCP, Skills, Hooks, Agents (talk)"
  - "Daisy Hollman Beyond the Basics"
  - "Code w/ Claude 2026 Beyond the Basics"
source_type: "talk"
kind: "conference-talk"
status: "verified"
year: 2026
publication_date: "2026-05-19"
publication_date_basis: "event_date_code_with_claude_london"
event_date: "2026-05-19"
youtube_upload_date: "2026-05-22"
source_updated_date: "2026-07-14"
source_updated_date_basis: "capture_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Daisy Hollman"
creator: "Daisy Hollman (Member of Technical Staff, Anthropic)"
venue: "Code w/ Claude 2026 (London)"
url: "https://www.youtube.com/watch?v=tuY2ChJIx48"
pdf_url: ""
medium: "video"
platform: "youtube"
video_id: "tuY2ChJIx48"
duration_seconds: 2839
language: "en"
transcript_status: "captured"
transcript_type: "local-asr-lightly-normalized"
transcript_language: "en"
transcript_review_status: "claim-ranges-spot-checked"
transcript_storage: "local-only"
transcript_locator: ".private/talk-transcripts/Beyond the basics with Claude Code - transcript.md"
transcript_sha256: "a89bbc0aef93efc5d98196131a0e3e644e9712c2773dfa69b07bd3b2edc6540f"
transcription_engine: "Whisper"
transcription_model: "large-v3-turbo"
transcription_tool_version: "not-recorded"
transcription_command: "not-recorded"
source_media_sha256: "not-recorded"
timestamp_generation_method: "not-recorded"
normalization_status: "light-product-name-normalization"
evidence_class: "official-conference-workshop"
metrics_status: "speaker-reported"
created: 2026-06-23
updated: 2026-07-14
---

# Beyond the basics with Claude Code

## Summary

- Daisy Hollman frames the jump from *agentic programming* to *agentic software engineering* as a harness-design problem. Large organizations must give agents access to the decisions and systems around the code, inject organization-specific knowledge without exhausting context, and connect existing developer feedback tools to the agent loop.
- The talk's three prerequisites are **access, knowledge, and tooling**. An agent that sees only a repository and shell misses design rationale, stakeholder conversations, CI/CD, dashboards, runbooks, and institutional vocabulary — the “why” that determines the right implementation path.
- Plugin design is context engineering under a fixed budget. The explicit four primitives are **MCP, Skills, Hooks, and Agents**. They differ in what stays in the parent prompt, what loads on demand, what executes outside context, and what moves into a separate context window.
- The scale test is not “does one customization work?” but “what happens with 10,000 or 100,000 of them?” Skills and subagents still pay for always-visible descriptions; tool search reduces MCP schema cost but creates a discoverability trade-off; hooks can filter outside context and inject nothing, making them the closest of the four to a zero-token-overhead abstraction.
- **CLAUDE.md is not one of the four plugin primitives.** It appears as the cautionary always-loaded design: allowing every plugin to add unconditional system-prompt text would look cheap locally and become globally unscalable. The earlier version of this note incorrectly presented CLAUDE.md as one of the four layers.
- The practical operating model is asynchronous and parallel: long-lived worktrees and persistent agent identities, agent-to-agent messaging, periodic loops for CI/PR babysitting, permission automation, a multi-session control surface, and remote check-ins. The resulting human bottleneck is context-switching latency, not merely model latency.

## Three Harness Requirements

1. **Access:** connect the agent to the places where work and rationale actually live — team chat, email, design documents, CI/CD, dashboards, meeting transcripts, runbooks, and internal systems — with appropriate permission boundaries. A useful audit is to note every time a developer must leave the agent surface and copy information back in.
2. **Knowledge:** organization-specific conventions and recent facts cannot realistically be trained into a fast-moving frontier model for each codebase. They must be supplied through in-context learning, retrieval, instructions, tools, and durable artifacts.
3. **Tooling:** adapt the existing developer environment into an agent environment. Linters, LSP feedback, generated-file warnings, tests, and CI are the agentic equivalents of IDE affordances. The best controls guide a more capable model rather than forcing a brittle action order.

## The Four Plugin Primitives

| Primitive | What is paid in the parent context | What scales | Scaling boundary called out in the talk |
|---|---|---|---|
| **MCP** | Tool names, descriptions, and schemas unless lazily discovered | Public, transport-agnostic integrations and capabilities requiring a standard auth/lifecycle boundary | Many servers multiply schemas; tool search can lazy-load details, but shorter descriptions make discovery less reliable. For internal developers who already have a shell and CLI, a Skill that teaches the CLI is often simpler. |
| **Skills** | A description used for triggering | The body, scripts, and resources load only when selected — a “lazy system prompt” | The body is pay-per-use, but every description is still paid. Richer descriptions trigger better; very large monorepos need hierarchy or discovery beyond a flat catalog. |
| **Hooks** | Nothing unless the hook returns text | Matching and filtering run on the machine outside the context window; irrelevant hooks can exit without injecting tokens | This is real zero *token* overhead for unused hooks, not zero compute or maintenance. Hooks cannot express every semantic condition cheaply, and using an agent to decide whether to inject context reintroduces token cost. |
| **Agents / subagents** | Agent description, invocation, and returned result | The subagent's instructions and bulk reading live in a separate context, so it can inspect many files without filling the parent | Tokens are displaced, not free. A flat catalog of many agent descriptions still burdens the parent prompt, and lossy result handoffs remain a design risk. |

The design principle is **do not pay for what you do not use**. Pick the mechanism by loading behavior, not by branding: public integration and auth boundary, progressive procedural disclosure, deterministic lifecycle feedback, or context-isolated delegated work.

## Context and Feedback Mechanics

- **Stable prefix, volatile suffix:** KV caching makes early prompt mutations expensive because they invalidate the cached suffix. Stable shared instructions and tool definitions belong earlier; task-specific, evictable information belongs later. A naive LRU-style prompt cache can save context length while increasing uncached inference cost.
- **Feedback should scale with intelligence:** post-tool hooks that run linters or warn about generated files behave like “red squigglies for agents.” They nudge and supply timely evidence without necessarily hard-blocking a capable model that has a legitimate exception.
- **Tighter loops beat model-only upgrades:** the talk's practical thesis is that the quickest codebase-specific gains often come from connecting existing scripts, tests, LSPs, and CI at the right moment, not waiting for a more capable model.
- **Curated primitives are not memory:** Hollman distinguishes evaluated, iterated plugin primitives from low-cost, short-lived information created opportunistically by an agent. Both have uses, but they should not share the same trust or lifecycle assumptions.

## Asynchronous Multi-Agent Operating Model

- Separate worktrees keep concurrent Claude Code sessions from overwriting one another. Hollman reports using long-lived worktrees whose agents retain stable identities and track upstream main, avoiding repeated environment setup.
- Agent messaging lets one live context explain something directly to another, but separation should remain available for redundancy, testing, or independent evaluation.
- A periodic `/loop` can poll slow CI and continue repairing failures, turning long wait states into asynchronous pipelines.
- Auto Mode is presented as a permission-classifier plus adversarial checking layer that makes overnight loops and agent teams practical. The speaker characterizes its additional token use as uncertain; the source does not support a durable quantitative overhead estimate.
- A multi-agent view and remote control reduce supervision and human context-switching latency by surfacing working, blocked, and inspectable sessions in one place.

## Timestamped Claims

- **03:21–03:55:** harness customization is organized around access, knowledge, and tooling.
- **04:00–08:45:** professional software engineering requires access to rationale and systems beyond source code; audit every manual copy/paste or tool switch as a missing agent connection.
- **09:55–11:19:** organization-specific knowledge is supplied through in-context learning and text-based harness artifacts rather than codebase-specific frontier-model weight updates.
- **12:28–14:45:** agent tooling should reproduce IDE-like feedback; post-tool hooks are “red squigglies,” and the claimed fastest route to codebase-specific improvement is a tighter feedback loop.
- **16:23–19:28:** context size is treated as a fixed target; scalable customization puts the smallest relevant information in at the right time and avoids paying for unused instructions.
- **19:57–21:41:** KV-cache economics favor stable shared prompt content early and volatile per-task content late.
- **22:32–22:41:** the talk explicitly names MCP, Skills, Hooks, and Agents as the four plugin primitives.
- **24:37–28:08:** use MCP for public integrations and external services; when internal developers already have a CLI and shell, a Skill teaching the CLI may avoid unnecessary schema, auth, and process-lifecycle overhead.
- **28:14–30:37:** Skills lazy-load bodies but always expose descriptions; triggering quality and description cost trade off, and a flat catalog does not scale indefinitely.
- **30:37–33:19:** hooks perform filtering outside context and incur no token cost when they inject nothing; semantic hook routing may itself become expensive.
- **33:19–36:18:** subagents isolate bulk context but leave descriptions in the parent; unconditional plugin-provided CLAUDE.md content is rejected as deceptively expensive at ecosystem scale.
- **37:29–46:36:** asynchronous/parallel use shifts the human problem toward context switching; worktrees, persistent identities, messaging, loops, automated permissions, control surfaces, and remote check-ins are the operational response.

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
- [[claims/Claim - Context management is an agent architecture choice]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[concepts/context engineering]]
- [[concepts/cache-aware harness design]]
- [[concepts/agent operating surfaces]]
- [[concepts/agent skills]]
- [[concepts/dynamic tool discovery]]
- [[concepts/subagent context isolation]]
- [[concepts/loop engineering]]
- [[methods/hook-based control]]
- [[methods/runtime supervision]]
- [[operations/agent harnesses]]
- [[operations/cost control]]
- [[operations/worktree isolation]]
- [[operations/durable sessions]]
- [[systems/Claude Code]]
- [[protocols/MCP]]
- [[sources/Claude Code Hooks]]
- [[sources/Claude Code Skills Docs]]
- [[sources/Claude Code Agent Teams]]
- [[sources/Anthropic Agent Skills]]
- [[sources/Anthropic Code Execution with MCP]]
- [[sources/Anthropic Claude Code Auto Mode]]

## Local Capture

- Private transcript: `.private/talk-transcripts/Beyond the basics with Claude Code - transcript.md`
- SHA-256: `a89bbc0aef93efc5d98196131a0e3e644e9712c2773dfa69b07bd3b2edc6540f`
- The original capture did not record the transcription package version, exact command, source-media hash, or timestamp-generation method. Those provenance gaps are retained explicitly rather than reconstructed.

## Evidence Boundary

This is an official Anthropic conference workshop and strong primary evidence for the speaker's design model and Claude Code team's reported practices. It is not a controlled evaluation. Scale examples such as monorepos with very large Skill catalogs, internal PR throughput, loop effectiveness, and Auto Mode overhead are speaker-reported and not independently audited. Product behavior is also time-sensitive because several features were described as actively changing.

## Notes

- Canonical URL: https://www.youtube.com/watch?v=tuY2ChJIx48 (Claude channel; YouTube upload date 2026-05-22).
- Official session page: https://claude.com/code-with-claude/session/ldn-beyond-the-basics-with-claude-code — Code w/ Claude 2026, London, 19 May 2026, 11:30–12:15; speaker Daisy Hollman (Member of Technical Staff, Anthropic).
- The local transcript was produced because YouTube reports captions disabled for this video. It was generated with Whisper large-v3-turbo, lightly normalized for obvious product-name errors, and not manually proofread end to end; only the cited claim ranges were spot-checked.
- The source-card correction matters: the four plugin primitives are MCP, Skills, Hooks, and Agents. CLAUDE.md is the separate example of unconditional context that would not scale as a plugin primitive.
