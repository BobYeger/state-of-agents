# Loop Engineering

Source URL: https://addyosmani.com/blog/loop-engineering/

Capture date: 2026-06-14

Capture note: partial research snapshot only. The article is summarized rather than copied in full.

## Core framing

Addy Osmani frames loop engineering as a new layer above direct prompting: instead of repeatedly prompting an agent by hand, the developer designs a system that prompts, monitors, retries, and feeds state back into one or more agents.

The article explicitly connects this to agent harnesses. Its main distinction is that harness engineering gives an agent tools, context, skills, policies, subagents, and execution structure, while loop engineering adds recurring prompts, timers, external memory, and self-feeding state so that the harness can keep running across iterations.

## Key excerpts

Short excerpts retained for local citation:

> "designing loops that prompt your agents"

> "My job is to write loops."

> "Loop engineering is harness engineering with a timer"

## Main components

The article maps modern coding-agent loops across:

- Automations and scheduled tasks.
- Worktrees and isolated workspaces.
- Skills and reusable procedures.
- Plugins, connectors, and MCP-style tools.
- Subagents and agent teams.
- Memory/state outside the chat transcript.

## Claude/Codex relevance

The article treats Claude Code `/loop`, `/goal`, hooks, workflows, subagents, skills, and worktrees as examples of the same shift: the human designs the outer loop rather than manually steering every turn.

For Codex-style environments, the comparable pieces are goals, thread/worktree isolation, skills, MCP/tools, subagents, local files, and resumable task state.

## Risks

The article highlights risks that belong in harness analysis:

- Verification debt: a loop can keep working without proving it is doing the right work.
- Comprehension debt: generated changes can outpace the human's ability to understand them.
- Cost and runaway behavior: unattended loops spend tokens and tool time.
- Cognitive surrender: delegating the loop can weaken developer judgment if no evidence gate is present.
