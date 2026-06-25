---
title: "Beyond the basics with Claude Code"
aliases:
  - "Context Engineering: MCP, CLAUDE.md, Skills, Hooks (talk)"
  - "Daisy Hollman Beyond the Basics"
  - "Code w/ Claude 2026 Beyond the Basics"
source_type: "talk"
kind: "conference-talk"
status: "verified"
year: 2026
publication_date: "2026-05-19"
publication_date_basis: "event_date_code_with_claude_london"
source_updated_date: "2026-06-23"
source_updated_date_basis: "snapshot_date"
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
artifacts: []
created: 2026-06-23
updated: 2026-06-23
---

# Beyond the basics with Claude Code

## Summary

- Conference workshop by Daisy Hollman (Anthropic) at Code w/ Claude 2026 (London, 19 May 2026), published on the Claude YouTube channel. Subject: "the mechanics that separate basic Claude Code use from real leverage."
- Frames customization through a small set of plugin abstractions — CLAUDE.md, MCP, Skills, and Hooks (plus subagents) — and treats the choice between them as a context-budget decision, not a feature checklist.
- Core through-line: each abstraction differs in *when and how selectively it loads into context*, ranging from always-loaded (CLAUDE.md) and always-in-context tool definitions (MCP), through on-demand progressive disclosure (Skills), to zero-baseline deterministic injection (Hooks).
- Best source for [[concepts/context engineering]] as applied to a coding harness: the hard problem is "choosing the right information to put into a fixed box," and the abstractions are ranked by how cheaply and selectively they fill that box.
- Memorable framings: hooks as "red squigglies for agents" (small corrections injected at the moment of a mistake rather than caught in review); and the thesis that great work with Claude Code comes from tighter feedback loops, not a better model.

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
- [[claims/Claim - Context management is an agent architecture choice]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[concepts/context engineering]]
- [[concepts/agent operating surfaces]]
- [[concepts/agent skills]]
- [[concepts/dynamic tool discovery]]
- [[concepts/loop engineering]]
- [[methods/hook-based control]]
- [[methods/runtime supervision]]
- [[operations/agent harnesses]]
- [[operations/cost control]]
- [[systems/Claude Code]]
- [[protocols/MCP]]
- [[sources/Claude Code Hooks]]
- [[sources/Claude Code Skills Docs]]
- [[sources/Anthropic Agent Skills]]
- [[sources/Anthropic Code Execution with MCP]]
- [[sources/Anthropic Claude Code Auto Mode]]

## The Four Layers (loading model)

The talk's value for a "context engineering" section is the ordering by *loading selectivity and determinism*. Each layer is a way to give a coding agent tools, instructions, or context — but each pays a different price and loads at a different moment.

- **MCP (Model Context Protocol)** — gives the agent *tools* by exposing external systems through a universal standard. Cost: full tool descriptions sit in context, effectively always-in-context per turn. The talk's caution: "Twenty MCP servers, each exposing fifteen tools, means your prompt is mostly tool definitions before Claude reads a single line of your code." Lazily-loading definitions help but remain expensive; direct CLI access is often more context-efficient than wrapping a capability in an MCP server.
- **CLAUDE.md** — gives the agent *standing instructions/context* (team standards, conventions, acronyms). Cost: always loaded, consumed on *every turn regardless of relevance*. The talk's caution: stuffing it with everything "may feel like a good idea, but you pay for all of it on every turn," which can degrade performance and raise cost rather than improve them.
- **Skills** — gives the agent *procedural knowledge / scoped tools* on demand. Cost: only the frontmatter (name + description, ~100 tokens per skill) is scanned at session start; the SKILL.md body, scripts, and reference files load only once the skill fires. This is progressive disclosure, making Skills markedly more context-efficient than MCP for the same capability.
- **Hooks** — gives the agent *deterministic lifecycle control and just-in-time context*. Cost: the only abstraction that consumes no context until it fires. Hooks run scripts at fixed points in the loop and inject content (or block/correct) exactly when needed — "red squigglies for agents."

Spectrum captured in the conference notes: the abstractions run "from always-in-context (CLAUDE.md) to deterministic lifecycle control (Hooks), progressing toward more efficient context management strategies."

## Notes

- Canonical URL: https://www.youtube.com/watch?v=tuY2ChJIx48 (channel: Claude / @claude; title confirmed via YouTube oEmbed: "Beyond the basics with Claude Code").
- Official session page: https://claude.com/code-with-claude/session/ldn-beyond-the-basics-with-claude-code — speaker Daisy Hollman (Member of Technical Staff, Anthropic); Code w/ Claude 2026, London, 19 May 2026, 11:30–12:15, workshop. Session description's four focus areas: CLAUDE.md, MCP, Skills, and Auto Mode.
- The talk also discusses subagents and Auto Mode; this note centers the four context-loading layers most relevant to a context-engineering section.
- Ordering note: the talk presents the abstractions and the always-in-context → deterministic *loading spectrum*; the exact left-to-right sequence "MCP → CLAUDE.md → Skills → Hooks" is the presenter's chosen framing for talk section 6. It is consistent with the talk's content (the four layers and the cheapest/most-selective progression) but the talk does not assert that single fixed order verbatim. The session description orders them CLAUDE.md, MCP, Skills, Auto Mode.
- Correction to a common misreading: this is NOT "each layer scales context further." The opposite — it is about loading *less* and more selectively/deterministically as you move from MCP/CLAUDE.md (always paid) to Skills (on-demand) to Hooks (zero baseline). The engineering goal is context efficiency and tighter feedback loops.
- Corroboration of the Skills progressive-disclosure detail (metadata ~100 tokens at startup; body and bundled files load on demand) from Anthropic's official guidance: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- Conference write-up grounding the per-layer context-cost framing and the "red squigglies for agents" / feedback-loop thesis: https://chrisebert.net/notes-from-code-with-claude-2026/
- Transcript/description page (uListen) was rate-limited (HTTP 429) at capture time: https://ulisten.ai/channels/claude/beyond-the-basics-with-claude-code_tuY2ChJIx48/details
