# Loop Engineering

Loop engineering is the design of outer control loops that prompt, schedule, monitor, retry, verify, and feed state back into agents over time.

It is closely related to [[operations/agent harnesses]], but it names a slightly higher layer. Harness engineering designs the runtime scaffold around a model: tools, context, execution, permissions, logs, subagents, memory, and resumption. Loop engineering designs how that scaffold is repeatedly invoked and corrected.

## Distinctions

| Loop | What repeats | Stop condition | State lives in |
|---|---|---|---|
| Inner agent loop | model call, tool call, observation | model returns final or policy stops | context window and harness event stream |
| Goal loop | next turn after previous turn | completion condition is judged satisfied or blocked | goal state plus conversation/session |
| Hook loop | lifecycle event, matcher, handler, decision | hook allows, blocks, injects context, or lets runtime continue | hook config, handler output, transcript, event stream |
| Scheduled loop | prompt on a cadence | user stop, expiry, or model decides work is done | scheduler task plus session/local state |
| Workflow loop | coded phases and worker calls | script completion, stop, pause, or failure | workflow runtime variables and artifacts |
| Ralph loop | fresh coding-agent run over repo files | commit, plan update, or bounded failure | specs, plan, tests, git history |
| Self-improving code loop | code mutation, evaluation, selection | metric improves, rollback, or budget stops | codebase, benchmark traces, archive of variants |

## Design Questions

- What wakes the loop: a user turn, timer, webhook, issue state, test failure, or external event?
- What objective and evidence standard does the loop carry?
- What state is durable outside the model context?
- Which tools, files, network paths, and credentials can the loop touch?
- Which checks can stop, repair, or escalate the loop?
- How are cost, time, and parallelism bounded?

## Why It Belongs to Harness Engineering

Loop engineering is part of harness engineering because a loop is not just a prompt. It changes runtime behavior: when turns start, how continuation happens, where intermediate results live, how work resumes, who verifies progress, and when the system stops.

The current graph has several loop-engineering forms:

- [[sources/Addy Osmani Loop Engineering]]: names the June 2026 industry framing of designing loops that prompt agents, with automations, worktrees, skills, connectors, subagents, and external memory as the operating pieces.
- [[sources/Andrew Ng Three Key Loops]]: separates fast agentic coding loops from slower developer and external feedback loops, making product feedback cadence part of loop design.
- [[sources/Armin Ronacher The Coming Loop]]: distinguishes the inner agent loop from the harness-level loop and emphasizes bounded, legible use for porting, experiments, security scanning, and research.
- [[sources/Claude Code Scheduled Tasks]]: `/loop` and cron tools make prompt recurrence a Claude Code runtime feature.
- [[sources/OpenAI Codex Automations]]: Codex thread automations are heartbeat-style recurring wake-up calls attached to a thread — the Codex analogue of `/loop`, distinct from the persistent objective of `/goal`.
- [[sources/OpenAI Codex Using Goals]]: Codex Goals make a persistent, thread-scoped objective into an evidence-checked continuation loop.
- [[sources/Claude Code Hooks]]: hooks make lifecycle interception points programmable; Claude Code documents `/goal` as a built-in shortcut for a session-scoped prompt-based `Stop` hook.
- [[sources/Claude Code Goals]]: `/goal` sets a completion condition that a separate small evaluator model re-checks after every turn, turning a slash command into a persistent, evidence-checked continuation loop.
- [[sources/Claude Common Workflow Patterns for AI Agents]]: sequential, parallel, and evaluator-optimizer workflows are recurring control patterns with explicit dependency, aggregation, and stop-policy tradeoffs.
- [[sources/Claude Code Workflows]]: workflow scripts move orchestration state out of conversation context and into executable JavaScript.
- [[sources/Cloudflare Dynamic Workflows]]: durable infrastructure persists and resumes workflow steps, including agent-written plans.
- [[methods/self-improving code loops]]: executable artifacts mutate under evaluator feedback, so loop quality depends on tests, sandboxes, archives, and rollback.
- [[methods/ralph loop]]: repository files, tests, plans, and commits become the loop substrate.
- [[sources/OpenAI Codex Agent Loop]]: the inner model-tool-observation loop is the base layer every higher loop builds on.
- [[concepts/code factories]]: lifts loop engineering into an organization-level SDLC control plane.
- [[sources/Anthropic When AI Builds Itself]]: shows AI development itself becoming a goal -> implementation -> experiment -> review loop, with human judgement and verification as the bottleneck.

## Risks

- A loop can amplify a weak objective faster than a single prompt.
- Repetition without external evidence creates plausible progress without reliability.
- Long loops create comprehension debt when generated artifacts outpace review.
- Scheduled or unattended loops need explicit cost, permission, and stop policies.
- Self-improving code loops can overfit or hack the evaluator if the evidence surface is weak.
- AI-R&D loops can shift the bottleneck from doing work to choosing goals, judging evidence, and verifying that generated work should be trusted.
- Factory-style loops can create codebases that assume machine participation for future maintenance, so comprehension and auditability must be designed into the harness.

## Related

- [[operations/agent harnesses]]
- [[concepts/code factories]]
- [[operations/agent infrastructure]]
- [[operations/durable sessions]]
- [[operations/agent observability]]
- [[operations/worktree isolation]]
- [[operations/permissions]]
- [[concepts/outcomes and rubric graders]]
- [[concepts/subagent context isolation]]
- [[concepts/agent skills]]
- [[methods/hook-based control]]
- [[methods/ralph loop]]
- [[methods/self-improving code loops]]
- [[methods/multi-agent orchestration]]
