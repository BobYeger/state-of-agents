# Run prompts on a schedule

Source URL: https://code.claude.com/docs/en/scheduled-tasks

Capture date: 2026-06-14

Capture note: readable local markdown snapshot generated from the public Claude Code docs page. The page did not expose a stable publication date in this pass.

Claude Code scheduled tasks are a local scheduling surface for rerunning prompts inside a Claude Code session. The docs describe this as `/loop` plus cron-backed tools that let Claude create, list, and delete scheduled prompts.

## Requirements and scope

- Requires Claude Code v2.1.72 or later.
- Tasks run only while Claude Code is open and idle enough to take another turn.
- Tasks are scoped to the current conversation/session.
- A new conversation does not automatically inherit existing scheduled tasks.
- `--resume` or `--continue` can restore unexpired tasks from a resumed session.
- Recurring tasks expire after 7 days.

## Scheduling modes

The page compares three recurring-work surfaces:

| Surface | Where it runs | Persistence | Typical use |
|---|---|---|---|
| Claude cloud scheduled tasks | Cloud | Persistent | Cloud reminders and recurring prompts |
| Claude Desktop scheduled tasks | Local desktop | Persistent while configured | Desktop recurring work |
| Claude Code `/loop` | Local Claude Code session | Session-scoped | Developer tasks that need local repo, tools, or terminal state |

## `/loop`

`/loop` asks Claude Code to rerun a prompt on a cadence. The command can be used with:

- An interval and a prompt.
- A prompt only, letting Claude decide the next interval after each iteration.
- No arguments, using a default maintenance prompt or a project/user `loop.md` prompt when configured.

Examples from the docs include fixed cadence review work and command reuse:

```text
/loop 20m /review-pr 1234
```

The docs position `/loop` as different from `/goal`:

- `/goal` repeats after each previous turn until a completion condition is judged satisfied.
- `/loop` repeats after a time interval until stopped, expired, or judged complete by Claude.

## `loop.md`

A `loop.md` file replaces the built-in bare `/loop` maintenance prompt. Claude Code looks first for `.claude/loop.md` in the project and then for `~/.claude/loop.md` in the user home directory.

The file is plain Markdown with no required structure and is read as if the user had typed the `/loop` prompt directly. Edits take effect on the next iteration. Content beyond 25,000 bytes is truncated.

On Bedrock, Vertex AI, and Microsoft Foundry, `loop.md` is not read; bare `/loop` prints the usage message instead.

## Cron tools

The underlying tool surface includes:

- `CronCreate`
- `CronList`
- `CronDelete`

The docs state that a session can have up to 50 scheduled tasks. Claude Code schedules prompts in the user's local timezone, applies jitter, and does not catch up on missed executions if the program was closed or busy.

## Operational notes

- Scheduled prompts enqueue between turns at low priority.
- Background Bash or monitor tasks are not restored just because a scheduled prompt is restored.
- Recurring tasks have deterministic jitter to avoid synchronized API traffic.
- `CLAUDE_CODE_DISABLE_CRON=1` disables cron tools and `/loop`.
- Scheduled tasks can be useful for local checks, reminders, PR watch loops, periodic test runs, and repo maintenance, but they are not a durable hosted workflow runtime.

## Harness relevance

`/loop` turns a prompt into a time-triggered control loop. It is a harness feature because the runtime now owns cadence, resumption, expiry, task identity, and continuation, while the model handles each scheduled iteration.
