# Ralph Loop

The Ralph loop is a coding-agent harness pattern: run the agent in repeated short loops with fresh context, explicit files as state, tests as backpressure, and commits or plan updates as durable progress.

It is useful because it turns an open-ended coding session into a restartable control loop. The model does not need to remember everything in chat; the repository, specs, `AGENTS.md`, implementation plan, test results, and git history become the durable substrate.

## Pattern

- Define requirements as files, usually specs or jobs-to-be-done.
- Maintain an implementation plan as the active task ledger.
- Start each loop from a small prompt plus repository files, not a long chat transcript.
- Pick one bounded task, investigate, implement, validate, and commit or update the plan.
- End the loop deliberately so the next iteration starts with cleaned context.

## Why It Matters

- Fresh context reduces drift and context pollution.
- Files and commits make progress auditable and recoverable.
- Tests, builds, and review criteria provide backpressure against plausible but broken code.
- The loop composes with worktrees, subagents, and rubric-based outcomes.

## Risks

- Without good specs, the loop can optimize locally while missing the actual product goal.
- Without tests or graders, the loop may simply produce repeated plausible changes.
- Without disciplined plan updates, the repository becomes state but not memory.
- It can hide coordination problems if many loops run in parallel without merge and review policy.

## Related Sources

- [[sources/Ralph Playbook]]
- [[sources/Claude Managed Agents Define Outcomes]]
- [[sources/Anthropic Effective Harnesses for Long-Running Agents]]
- [[sources/OpenAI Codex Agent Loop]]

## Related

- [[operations/agent harnesses]]
- [[concepts/long-horizon agents]]
- [[concepts/context engineering]]
- [[operations/worktree isolation]]
- [[operations/durable sessions]]
- [[concepts/outcomes and rubric graders]]
- [[systems/Claude Code]]
- [[systems/Codex]]
