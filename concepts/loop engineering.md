# Loop Engineering

Loop engineering is the design of outer control loops that prompt, schedule, monitor, retry, verify, and feed state back into agents over time.

It is closely related to [[operations/agent harnesses]], but it names a slightly higher layer. Harness engineering designs the runtime scaffold around a model: tools, context, execution, permissions, logs, subagents, memory, and resumption. Loop engineering designs how that scaffold is repeatedly invoked and corrected.

## Distinctions

| Loop | What repeats | Stop condition | State lives in |
|---|---|---|---|
| Inner agent loop | model call, tool call, observation | model returns final or policy stops | context window and harness event stream |
| Goal loop | next turn after previous turn | completion condition is judged satisfied or blocked | goal state plus conversation/session |
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

- [[sources/Claude Code Scheduled Tasks]]: `/loop` and cron tools make prompt recurrence a Claude Code runtime feature.
- [[sources/Claude Code Workflows]]: workflow scripts move orchestration state out of conversation context and into executable JavaScript.
- [[sources/Cloudflare Dynamic Workflows]]: durable infrastructure persists and resumes workflow steps, including agent-written plans.
- [[methods/self-improving code loops]]: executable artifacts mutate under evaluator feedback, so loop quality depends on tests, sandboxes, archives, and rollback.
- [[methods/ralph loop]]: repository files, tests, plans, and commits become the loop substrate.
- [[sources/OpenAI Codex Agent Loop]]: the inner model-tool-observation loop is the base layer every higher loop builds on.
- [[sources/Addy Osmani Loop Engineering]]: names the current industry framing of designing loops that prompt agents.

## Risks

- A loop can amplify a weak objective faster than a single prompt.
- Repetition without external evidence creates plausible progress without reliability.
- Long loops create comprehension debt when generated artifacts outpace review.
- Scheduled or unattended loops need explicit cost, permission, and stop policies.
- Self-improving code loops can overfit or hack the evaluator if the evidence surface is weak.

## Related

- [[operations/agent harnesses]]
- [[operations/agent infrastructure]]
- [[operations/durable sessions]]
- [[operations/agent observability]]
- [[operations/worktree isolation]]
- [[operations/permissions]]
- [[concepts/outcomes and rubric graders]]
- [[concepts/subagent context isolation]]
- [[concepts/agent skills]]
- [[methods/ralph loop]]
- [[methods/self-improving code loops]]
- [[methods/multi-agent orchestration]]
