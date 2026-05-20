By default, Managed Agents executes tools and code inside [Anthropic-managed cloud containers](https://platform.claude.com/docs/en/managed-agents/cloud-containers). Self-hosted sandboxes keep the orchestration on Anthropic's side but move tool execution into infrastructure you control, so the agent's code, filesystem, and network egress never leave your environment.

Self-hosted sandboxes are not yet available on [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws).

## How it differs from cloud environments

|  | Cloud environment | Self-hosted sandbox |
| --- | --- | --- |
| Where tools run | Anthropic-managed containers | Your infrastructure |
| Network reach | Anthropic's egress controls | Your network policy |
| File and GitHub repo mounting | Managed by Anthropic | Managed by you |
| Lifecycle | Managed by Anthropic | Managed by you |

Self-hosting is a good fit when the agent needs to operate on data that cannot leave your network boundary, reach internal services that are not publicly routable, or run under your organization's own compliance and audit controls.

## When to combine with MCP tunnels

Self-hosting controls *where the agent's code executes*. [MCP tunnels](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview) controls *how Anthropic reaches MCP servers in your network*. They are independent: a session running in Anthropic's cloud containers can still reach private MCP servers through a tunnel, and a self-hosted session can use either tunneled or public MCP servers. Use both when you want execution and tool access to stay inside your boundary.

## Environment worker

The following guide describes how to build a worker with any generic sandboxing platform. Additional, platform-specific guides are available for [Cloudflare](https://developers.cloudflare.com/sandbox/claude-managed-agents/), [Daytona](https://www.daytona.io/docs/en/guides/claude/claude-managed-agents), [Modal](https://github.com/modal-labs/claude-managed-agents-modal-sandbox), and [Vercel](https://vercel.com/kb/guide/run-claude-managed-agent-tools-with-vercel-sandbox).

An environment worker is a process you run on your own infrastructure that receives tool execution requests from Anthropic and runs them locally. The `self_hosted` environment is a work queue connecting Anthropic's orchestration to your worker: when a [session](https://platform.claude.com/docs/en/managed-agents/sessions) is assigned to an environment, Anthropic enqueues it as a work item. Your worker claims items from that queue, spawns an execution context for each session, downloads the [agent's skills](https://platform.claude.com/docs/en/managed-agents/skills), runs tool calls locally, and posts results back.

Work is claimed by polling the environment's queue: either by an **always-on worker** that polls continuously, or a **webhook-triggered handler** that wakes on `session.status_run_started` and starts polling.

Both CLI and SDK include pre-built workers to orchestrate your sessions. The `ant` CLI supports the always-on pattern only; the SDK supports both always-on and webhook-triggered architectures.

The CLI and SDK both are configurable (see [reference](#reference)), but if you require more control, you can leverage the [Environments Work endpoints](https://platform.claude.com/docs/en/api/beta/environments/work) directly and implement your own worker.

The SDK helpers require `/bin/bash` at that exact path. The TypeScript SDK additionally requires `unzip`, `tar`, and Node.js 22 or later. These dependencies are resolved at fixed paths and do not respect `PATH` overrides.

### Sandbox filesystem

- **`/workspace`**: the default working directory for tool execution and skill download. Skills are downloaded to `/workspace/skills/<name>/`. If you change `--workdir` from the default, update your agent's system prompt so Claude knows where to find them.
- **`/mnt/session/outputs`**: the agent writes final output files to this path. When running in a container, mount a host directory here to retrieve them.

## Start a session

Once your worker is running, create a session that targets the environment. Anthropic enqueues it and your worker claims and executes it.

File and GitHub resource mounting are handled in your container image rather than by Anthropic. To load your sandbox with session-specific files, you can pass session metadata when creating the session. Your orchestration layer can read that metadata and mount the relevant files before the worker starts executing.

```
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    metadata={"input_file": "s3://my-bucket/data.csv"},
)
```

[Memory](https://platform.claude.com/docs/en/managed-agents/memory) is not yet supported with self-hosted sandboxes.

## Reference

## Monitoring and operations

These calls run from your monitoring or operations tooling, authenticated with your Claude API key, to observe and manage the worker fleet. The claim and keep-alive loop is handled inside the worker helpers, so you don't call those endpoints directly.

These endpoints authenticate with your organization API key, not the environment key. Call them from outside the worker host. Setting `ANTHROPIC_API_KEY` on the worker host exposes an organization-scoped credential to agent tool calls.

`work.stats` returns the queue state for an environment:

- `depth` is the number of items waiting to be claimed. Scale your worker fleet or alert on backlog based on this value.
- `pending` is the number of items a worker has claimed and is currently processing.
- `oldest_queued_at` is the timestamp of the oldest item in the queue, or `null` if the queue is empty.
- `workers_polling` is the number of workers that have polled in the last 30 seconds. Use this for liveness alerting.

```
import os

import anthropic

client = anthropic.Anthropic()

stats = client.beta.environments.work.stats(os.environ["ANTHROPIC_ENVIRONMENT_ID"])
print(f"depth={stats.depth} pending={stats.pending}")
```

```
{
  "type": "work_queue_stats",
  "depth": 0,
  "pending": 0,
  "oldest_queued_at": null,
  "workers_polling": 0
}
```

### Stop a session gracefully

Use `work.stop` to ask the worker handling a specific session to shut it down cleanly. The worker finishes any in-flight tool call, posts a final status, and releases the session. Pass `force: true` in the request body to interrupt immediately instead of waiting for the current tool call to complete.

Because these calls run from your operations tooling rather than the worker host, `ANTHROPIC_WORK_ID` isn't set automatically. Set it to the target work item's ID before running the following examples.

```
import os

import anthropic

client = anthropic.Anthropic()

work = client.beta.environments.work.stop(
    os.environ["ANTHROPIC_WORK_ID"],
    environment_id=os.environ["ANTHROPIC_ENVIRONMENT_ID"],
)
print(work.state)
```[Managed Agent sessions](https://platform.claude.com/docs/en/managed-agents/sessions)

[

Create a session to run your agent and begin executing tasks.

](https://platform.claude.com/docs/en/managed-agents/sessions)[

MCP tunnels overview

Reach MCP servers inside your private network from any execution environment.

](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview)[

Security model

Understand the shared responsibility model for self-hosted sandbox environments.

](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-security)

Was this page helpful?