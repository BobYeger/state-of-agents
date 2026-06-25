---
title: "Keep Claude working toward a goal (/goal)"
aliases:
  - "Claude Code Goals"
  - "Claude Code /goal"
  - "/goal command"
source_type: "docs"
kind: "harness-docs"
status: "verified"
year: 2026
publication_date: "2026-06-23"
publication_date_basis: "accessed_living_docs_no_visible_publication_date"
source_updated_date: "2026-06-23"
source_updated_date_basis: "snapshot_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Anthropic"
venue: "Claude Code Docs"
url: "https://code.claude.com/docs/en/goal"
pdf_url: ""
artifacts: []
created: 2026-06-23
updated: 2026-06-23
---

# Keep Claude working toward a goal (/goal)

## Summary

- Official Claude Code docs for `/goal`: a slash command that sets a completion condition and keeps Claude working across turns, without re-prompting, until the condition is met. Requires Claude Code v2.1.139 or later.
- After each turn, a separate small fast model (defaults to Haiku) reads the condition plus the conversation and returns a yes/no decision with a short reason. "No" starts another turn and passes the reason as guidance; "yes" clears the goal and records an achieved entry.
- Architecturally it is a wrapper around a session-scoped prompt-based `Stop` hook: the same per-turn firing point as a user-written Stop hook, but session-scoped and typed inline rather than living in a settings file.
- The evaluator does not call tools or read files; it can only judge what Claude has already surfaced in the transcript, so effective conditions are verifiable from Claude's own output (e.g. "`npm test` exits 0").
- Pairs directly with [[sources/OpenAI Codex Using Goals]] for a Claude Code vs Codex Goals comparison: both turn a slash command into a persistent objective primitive with lifecycle controls and evidence-based completion.

## Claims

- [[claims/Claim - Runtime control and verification improve agent reliability]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Connections

- [[systems/Claude Code]]
- [[sources/Claude Code Hooks]]
- [[sources/OpenAI Codex Using Goals]]
- [[methods/hook-based control]]
- [[methods/runtime supervision]]
- [[concepts/loop engineering]]
- [[concepts/outcomes and rubric graders]]
- [[operations/agent harnesses]]
- [[operations/cost control]]
- [[operations/durable sessions]]
- [[methods/ralph loop]]
- [[reports/Harness Engineering Report]]

## Notes

- Canonical URL: https://code.claude.com/docs/en/goal

- **Completion contract checked by a separate model (Claim 1, confirmed).** Docs: "The `/goal` command sets a completion condition and Claude keeps working toward it without you prompting each step. After each turn, a small fast model checks whether the condition holds. If not, Claude starts another turn instead of returning control to you. The goal clears automatically once the condition is met." The evaluator is a distinct model from the one doing the work: "`/goal` adds a separate evaluator that checks your condition after every turn, so completion is decided by a fresh model rather than the one doing the work." It defaults to Haiku and returns "a yes-or-no decision and a short reason."

- **Lifecycle and relation to the Stop hook (Claim 2, confirmed).**
  - *Set*: `/goal <condition>`; setting a goal "starts a turn immediately, with the condition itself as the directive." A new goal replaces an active one (one goal per session). A `◎ /goal active` indicator shows elapsed time.
  - *Check status*: `/goal` with no argument shows the condition, run duration, turns evaluated, token spend, and the evaluator's most recent reason.
  - *Clear*: `/goal clear` (aliases: `stop`, `off`, `reset`, `none`, `cancel`); `/clear` also removes an active goal.
  - *Achieved*: a "yes" verdict clears the goal and records an achieved entry in the transcript; status afterward shows the achieved condition with duration, turn count, and token spend.
  - *Blocked*: there is no separate "blocked" state in the docs. To bound runaway loops, you embed a stop clause in the condition itself, e.g. "or stop after 20 turns"; the evaluator judges that clause from the conversation. (Note: a distinct blocked state is a Codex Goals concept, not Claude Code's — see comparison below.)
  - *Pause/resume*: there is no explicit pause command. Resume is implicit: a goal still active at session end is restored on `--resume`/`--continue`, but turn count, timer, and token baseline reset; an already-achieved or cleared goal is not restored.
  - *Stop-hook relation*: "How evaluation works" states plainly that "`/goal` is a wrapper around a session-scoped prompt-based Stop hook." Both `/goal` and a Stop hook fire after every turn; `/goal` is the session-scoped, inline shortcut, while a Stop hook lives in settings, applies to every session in scope, and can run a script (deterministic) or a prompt (model-evaluated). This matches [[sources/Claude Code Hooks]], which documents `/goal` as a built-in Stop-hook shortcut.

- **Requirements / failure modes.** `/goal` runs only in trusted workspaces (the evaluator is part of the hooks system) and is unavailable when `disableAllHooks` is set at any settings level or `allowManagedHooksOnly` is set in managed settings; in each case the command explains why rather than silently no-op'ing. The condition can be up to 4,000 characters. Evaluation tokens bill on the configured small fast model and are "typically negligible compared to main-turn spend."

- **Non-interactive.** Works in headless mode, the desktop app, and Remote Control. `claude -p "/goal <condition>"` runs the loop to completion in a single invocation; Ctrl+C interrupts.

- **Positioning vs other continuation mechanisms.** Three session-continuation approaches differ by what starts the next turn and what stops it: `/goal` (next turn when the previous finishes; stops when a model confirms the condition), `/loop` (next turn on a time interval; stops on user or Claude's own judgment), and a Stop hook (your script or prompt decides). Auto mode is complementary — it removes per-tool prompts within a turn, while `/goal` removes per-turn prompts.

- **Comparison with [[sources/OpenAI Codex Using Goals]] (for section 9).**
  - *Shared shape*: both promote a slash command into a persistent objective that survives across turns and drives evidence-based completion. Both warn that the goal must be verifiable from the agent's own surfaced output.
  - *Category*: Claude Code `/goal` and Codex `/goal` are both condition-driven goal primitives: keep working until a stated condition is met. Avoid over-teaching "thread" versus "session" because Codex docs use "thread" for a session-like work unit.
  - *Evaluator*: Claude Code is explicit that a separate small fast model (Haiku by default) judges completion after each turn and that `/goal` is literally a session-scoped prompt-based Stop hook. Codex's cookbook frames the goal as a compact contract (outcome, verification surface, constraints, boundaries, iteration policy, blocked stop condition).
  - *Lifecycle*: Codex documents an explicit "blocked" stop condition as part of the contract; Claude Code has no separate blocked state and instead relies on a turn/time clause embedded in the condition plus the inherent achieved/clear/resume states.
  - *Availability*: Claude Code `/goal` needs v2.1.139+; Codex Goals start in Codex 0.128.0.

- Publication date basis: accessed living docs, no visible publication date; snapshot accessed 2026-06-23.
- Web access during research: full — live docs at the canonical URL were reachable and used as the primary ground truth.
