# Introducing Dynamic Workflows: durable execution that follows the tenant

Source URL: https://blog.cloudflare.com/dynamic-workflows/

Publication date: 2026-05-01

Authors: Dan Lapid; Luís Duarte

Capture note: readable local markdown snapshot generated from the public Cloudflare blog page. Remote images and decorative page chrome are omitted.

This post is also available in [日本語](https://blog.cloudflare.com/ja-jp/dynamic-workflows) and [한국어](https://blog.cloudflare.com/ko-kr/dynamic-workflows).

[Article hero image](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/rnOsb3NbZKTeboXYz1zgi/1af3453bc36960a949c084db725158df/image1.png)

When we first launched Workers eight years ago, it was a direct-to-developers platform. Over the years, we have expanded and scaled the ecosystem so that platforms could not only build on Workers directly, but they could also enable *their* customers to ship code to *us* through many multi-tenant applications. We now see on Workers: Applications where users describe what they want, and the AI writes the implementation. Multi-tenant SaaS where every customer's business logic is, at runtime, some TypeScript the platform has never seen before. Agents that write and run their own tools. CI/CD products where every repo defines its own pipeline.

Last month, when we shipped the [Dynamic Workers open beta](https://blog.cloudflare.com/dynamic-workers/), we gave those platforms a clean primitive for the *compute* side: hand the Workers runtime some code at runtime, get back an isolated, sandboxed Worker, on the same machine, in single-digit milliseconds. [Durable Object Facets](https://blog.cloudflare.com/durable-object-facets-dynamic-workers/) extended the same idea to *storage* — each dynamically-loaded app can have its own SQLite database, spun up on demand, with the platform sitting in front, as a supervisor. [Artifacts](https://blog.cloudflare.com/artifacts-git-for-agents-beta/) did the same for *source control*: a Git-native, versioned filesystem you can create by the tens of millions, one per agent, one per session, one per tenant. So, we have dynamic deployment for storage and source control. What’s next?

Today, we are bridging durable execution and dynamic deployment with [**Dynamic Workflows**](https://github.com/cloudflare/dynamic-workflows).

## The gap between durable and dynamic execution

[Cloudflare Workflows](https://developers.cloudflare.com/workflows/) is our durable execution engine. It turns a `run(event, step)` function into a program where every step survives failures, can sleep for hours or days, can wait for external events, and resumes exactly where it left off when the isolate is recycled. It's the right primitive for anything that has to "keep going" past a single request: onboarding flows, video transcoding pipelines, multi-stage billing, long-running agent loops, and — as of [Workflows V2](https://blog.cloudflare.com/workflows-v2/) — up to 50,000 concurrent instances and 300 new instances per second per account, redesigned for the agentic era.

But Workflows has always had one assumption baked in: the workflow code is part of your deployment. Your `wrangler.jsonc` has a block that says *"when the engine calls into* `*WORKFLOWS*`*, run the class called* `*MyWorkflow*`*."* One binding, one class. Per deploy.

That works fine if you own all the code. It's fine if you're running a traditional application.

It stops working the moment you want to let your customer ship *their* workflow.

Say you're building an app platform where the AI writes TypeScript for every tenant. Say you're running a CI/CD product where each repository has its own pipeline. Say you're using an agents SDK where each agent writes its own durable plan. In every one of these cases, the workflow is different for every tenant, every agent, every request. There is no single class to bind.

This is the same shape of problem that Dynamic Workers solved for compute and that Durable Object Facets solved for storage. We just hadn't solved it for durable execution yet.

## Dynamic Workflows

`@cloudflare/dynamic-workflows` is a small library. Roughly 300 lines of TypeScript. It lets a single Worker — the **Worker Loader** — route every `create()` call to a different tenant's code, and, critically, have the Workflows engine dispatch `run(event, step)` back to that same code when the workflow actually executes, seconds or hours or days later.

Here's the whole pattern. A Worker Loader:

```typescript
import {
  createDynamicWorkflowEntrypoint,
  DynamicWorkflowBinding,
  wrapWorkflowBinding,
} from '@cloudflare/dynamic-workflows';

// The library looks this class up on cloudflare:workers exports.
export { DynamicWorkflowBinding };

function loadTenant(env, tenantId) {
  return env.LOADER.get(tenantId, async () => ({
    compatibilityDate: '2026-01-01',
    mainModule: 'index.js',
    modules: { 'index.js': await fetchTenantCode(tenantId) },
    // The tenant sees this as a normal Workflow binding.
    env: { WORKFLOWS: wrapWorkflowBinding({ tenantId }) },
  }));
}

// Register this as class_name in wrangler.jsonc.
export const DynamicWorkflow = createDynamicWorkflowEntrypoint<Env>(
  async ({ env, metadata }) => {
    const stub = loadTenant(env, metadata.tenantId);
    return stub.getEntrypoint('TenantWorkflow');
  }
);

export default {
  fetch(request, env) {
    const tenantId = request.headers.get('x-tenant-id');
    return loadTenant(env, tenantId).getEntrypoint().fetch(request);
  },
};
```

Add to your `wrangler.jsonc`:

```json
"workflows": [
        {
            "name": "dynamic-workflow",
            "binding": "WORKFLOW",
            "class_name": "DynamicWorkflow"
        }
    ]
```

The tenant writes plain, idiomatic Workflows code. They have no idea they're being dispatched:

```typescript
import { WorkflowEntrypoint } from 'cloudflare:workers';

export class TenantWorkflow extends WorkflowEntrypoint {
  async run(event, step) {
    return step.do('greet', async () => \`Hello, ${event.payload.name}!\`);
  }
}

export default {
  async fetch(request, env) {
    const instance = await env.WORKFLOWS.create({ params: await request.json() });
    return Response.json({ id: await instance.id });
  },
};
```

That's it. The tenant calls `env.WORKFLOWS.create(...)` against what looks like a perfectly normal Workflow binding. Workflow IDs, `.status()`, `.pause()`, retries, hibernation, durable steps, `step.sleep('24 hours')`, `step.waitForEvent()` — everything works the way it always has.

The library handles one thing: making sure that when the Workflows engine eventually wakes up and calls `run(event, step)`, it ends up inside the *right tenant's* code.

## How it works

Three layers: the Workflows engine (platform) on top, your Worker Loader in the middle, your tenant's code (a Dynamic Worker) on the bottom.

When a request reaches the Worker Loader, it routes the execution to the correct dynamic code on the fly. The rest of the execution is a handoff between these three layers, left-to-right in time: the request enters, bounces up to the engine, is persisted, and later bounces back down again.

Walking the flow:

**① → ② Entering the tenant's code.** The Worker Loader receives an HTTP request, figures out which tenant it's for, loads that tenant's code via the Worker Loader, and forwards the request to its `default.fetch`. The `env` it hands the tenant contains `WORKFLOWS: wrapWorkflowBinding({ tenantId })`. As far as the tenant is concerned, that looks and acts like a real Workflow binding.

**③ Up to the Worker Loader.** When the tenant calls `env.WORKFLOWS.create({ params })`, it's actually making a Remote Procedure Call (RPC) into the Worker Loader — the wrapped binding is a `WorkerEntrypoint` subclass (`DynamicWorkflowBinding`) that the runtime specialized with the tenant's metadata at load time. That's why you have to `export { DynamicWorkflowBinding }` from your Worker Loader: the runtime builds per-tenant stubs by looking the class up in `cloudflare:workers` exports. Bindings that cross the Dynamic Worker boundary *have* to be RPC stubs — a plain `{ create, get }` object can't be structured-cloned, and the raw `Workflow` binding isn't serializable either.

Inside the Worker Loader, the wrapped binding transparently rewrites the payload:

```rust
tenant calls:  create({ params: { name: 'Alice' } })
                            │
                            ▼
engine sees:   create({ params: {
                  __workerLoaderMetadata: { tenantId: 't-42' },
                  params: { name: 'Alice' }
               }})
```

**④ Up to the engine.** The Worker Loader then calls `.create()` on the *real* `WORKFLOWS` binding with the envelope as the params. From here the Workflows engine takes over. It persists `event.payload` — which now includes the envelope — and schedules the run. Every time the engine later wakes up the workflow (whether that’s after a 24-hour sleep, a crash, or a deploy), the metadata rides along with the payload, waiting to route the run.

One implication: treat the metadata as a routing hint, not as authorization. The tenant can read it back via `instance.status()`. Don't put secrets in there.

**⑤ → ⑥ The engine comes back down.** When the engine is ready to run a step, it calls `.run(event, step)` on the class you registered in `wrangler.jsonc` — the one `createDynamicWorkflowEntrypoint` gave you. That class unwraps the envelope, hands the metadata to the `loadRunner` callback *you* wrote, and forwards the unwrapped event through to whatever runner the callback returns.

The callback is where everything interesting happens, and it's entirely yours. Fetch the tenant's latest source from R2. Check their plan tier and pick a region. Attach a tail Worker for per-tenant logging. Bundle TypeScript on the fly with [`@cloudflare/worker-bundler`](https://www.npmjs.com/package/@cloudflare/worker-bundler). In the common case, you just hand off to the Worker Loader:

```typescript
const stub = env.LOADER.get(tenantId, () => loadTenantCode(tenantId));
return stub.getEntrypoint('TenantWorkflow');
```

The Worker Loader caches by ID, so a workflow that runs many steps over many hours reuses the same dynamic Worker across them. When the isolate eventually gets evicted, the next `step.do()` pulls the code again and keeps going — the tenant's workflow has no idea anything happened. A Dynamic Worker boots in single-digit milliseconds using a few megabytes of memory, so the dispatch overhead is essentially free. You can have a million tenants, each with their own distinct workflow code, each spun up lazily on the step boundary where it's needed, and none of them cost anything while idle.

### The escape hatch

If you want to subclass `WorkflowEntrypoint` yourself — to add logging around `run()`, wire up per-tenant observability, or thread custom state through — the library exposes the lower-level `dispatchWorkflow` primitive that `createDynamicWorkflowEntrypoint` is built on:

```typescript
import { dispatchWorkflow } from '@cloudflare/dynamic-workflows';

export class MyDynamicWorkflow extends WorkflowEntrypoint {
  async run(event, step) {
    return dispatchWorkflow(
      { env: this.env, ctx: this.ctx },
      event,
      step,
      ({ metadata, env }) => loadRunnerForTenant(env, metadata),
    );
  }
}
```

Everything else — IDs, pause/resume, `sendEvent`, retries — falls through to the real Workflows engine untouched.

## Dynamic Workers are the primitive

Step back from the specifics for a second. Every interesting line of this library is either a wrapper around `.create()` on the outbound side or a wrapper around `WorkflowEntrypoint` on the inbound side. The actual work — spinning up the tenant's code, sandboxing it, routing RPC across the boundary, caching the isolate, hibernating between steps — is all done by Dynamic Workers underneath.

That's the real story, and it's a lot bigger than Workflows

Dynamic Workers is the primitive that swallows everything. [Durable Object Facets](https://blog.cloudflare.com/durable-object-facets-dynamic-workers/) is the same pattern applied to Durable Objects. Dynamic Workflows is that same pattern applied to `WorkflowEntrypoint`. Each one is the same small amount of envelope-and-unwrap glue between the static binding you've always had and the dynamic version you can now hand to your customers.

And we're not stopping at Workflows. Every binding that Workers currently exposes is heading for a dynamic counterpart — queues where each producer ships its own handler, caches, databases, object stores, AI bindings, and MCP servers where every tenant brings their own tools. Whatever you bind to a Worker today, you will soon be able to bind dynamically: dispatched per tenant, per agent, per request, at zero idle cost.

The unit economics of running a platform like this are, frankly, absurd. Shipping a multi-tenant product used to mean giving every customer their own container, their own database, their own disk, their own scheduler, and stitching it together with orchestration glue, service meshes, and hair-pulling billing math. Many of these applications have to support thousands of customers at the very least; millions, at the most. On Dynamic Workers and everything composing on top of them, idle tenants cost approximately nothing and active tenants share the same hardware through isolate-level multi-tenancy. The floor drops several orders of magnitude. A platform that used to cap out at thousands of paying customers can now reasonably serve tens of millions.

## What this unlocks

### Agent platforms that plan like engineers

Coding agents — [OpenCode](https://opencode.ai/), [Claude Code](https://code.claude.com/docs/en/overview), Codex, Pi — have been proving for the past year that LLMs are far better at *writing code* than at making sequential tool calls. The [Cloudflare Agents SDK](https://developers.cloudflare.com/agents/) and [Project Think](https://blog.cloudflare.com/project-think) extend that insight into durable execution: with primitives like fibers and sub-agents, an agent's long-running plan can survive crashes, hibernation, and redeploys without the user noticing.

Dynamic Workflows is the piece that lets that plan be a *first-class Cloudflare Workflow* — something the agent literally writes and the platform literally runs, with the full durability machinery behind it. A `run(event, step)` function the model wrote a minute ago, where every `step.do(...)` is independently retryable, every `step.sleep('24 hours')` hibernates for free, and every `step.waitForEvent(...)` waits indefinitely for the human to approve the next action. The agent writes the workflow; the platform runs it; neither has to know ahead of time what the plan looks like.

### SDKs and frameworks where the user brings the logic

If you're shipping a framework where your customer writes the `run(event, step)` function — a workflow builder UI, a visual automation tool, a per-tenant extension system, a low-code tool for non-developers — Dynamic Workflows is now the primitive that makes it work without compromise. You call `wrapWorkflowBinding({ tenantId })` once, hand the result to their code as `WORKFLOWS`, and every workflow instance they create is automatically tagged, routed back, and executed in their sandbox. The framework owns the Worker Loader; the user owns the workflow; neither has to care about the other.

### CI/CD at primitive speed

Here's the use case that's been getting us most excited.

Every CI/CD platform in existence is, underneath, a dispatcher of per-repo configuration files: *"run these steps, in this order, with these secrets, cache these directories, upload these artifacts."* Each repo has its own pipeline. Each branch might have its own variant. Each pull request spawns an instance of that pipeline that has to run to completion, survive a machine crash, retry a flaky step, stream logs, pause for approvals, and persist results.

That's *exactly* the shape of a durable workflow. The reason CI hasn't been built that way until now is that nobody had a cloud primitive where **the workflow itself is different for every repo, dispatched at runtime, at zero provisioning cost.** Now you do.

Here's what a CI pipeline looks like when it's just code your customer ships with their repo — say, in `.cloudflare/ci.ts`. The workflow itself is real; the `runInSandbox() / summarise()` / GitHub binding helpers below are platform-provided glue, the kind of thing you'd ship once in your dispatcher:

```typescript
import { WorkflowEntrypoint } from 'cloudflare:workers';

export class CIPipeline extends WorkflowEntrypoint {
  async run(event, step) {
    const { repo, sha, branch, pr } = event.payload;

    // Fork an isolated copy of the repo at this commit. Seconds, not minutes.
    const workspace = await step.do('checkout', () =>
      this.env.ARTIFACTS.fork(repo, { sha })
    );

    await step.do('install', () => runInSandbox(workspace, ['pnpm', 'install']));

    // Each parallel step is independently retryable.
    const [lint, test, build] = await Promise.all([
      step.do('lint',  () => runInSandbox(workspace, ['pnpm', 'lint'])),
      step.do('test',  () => runInSandbox(workspace, ['pnpm', 'test'])),
      step.do('build', () => runInSandbox(workspace, ['pnpm', 'build'])),
    ]);

    if (pr) {
      await step.do('comment', () =>
        this.env.GITHUB.commentOnPR(repo, pr, summarise({ lint, test, build }))
      );
    }

    // Workflow hibernates until approval arrives. No VM held open.
    if (branch === 'main') {
      await step.waitForEvent('approval', { type: 'deploy-approval', timeout: '24 hours' });
      await step.do('deploy', () => runInSandbox(workspace, ['pnpm', 'deploy']));
    }
  }
}
```

The platform owns the dispatcher. It ingests a webhook, figures out which repo it came from, loads *that repo's* `CIPipeline` class as a Dynamic Worker, and hands the run-off to Dynamic Workflows. The platform doesn't know what's in the pipeline. It doesn't need to. It's running a durable function that happens to live in the customer's repo.

Now line up what each step actually does:

- [**Artifacts**](https://blog.cloudflare.com/artifacts-git-for-agents-beta/) gives every repo a Git-native, versioned filesystem that lives on Cloudflare's globally distributed network. [ArtifactFS](https://github.com/cloudflare/artifact-fs) hydrates the tree lazily, so even a multi-GB repo is ready to work within single-digit seconds — and `fork()` gives each CI run its own isolated copy, with no `git clone` tax.
- [**Dynamic Workers**](https://blog.cloudflare.com/dynamic-workers/) run each lightweight step (lint, format, typecheck, bundle) in a sandboxed isolate that boots in milliseconds, on the same machine as the repo's data. No VM provisioning, no image pull, no cold start.
- [**Dynamic Workflows**](https://developers.cloudflare.com/dynamic-workers/usage/dynamic-workflows/) holds the whole run together. Steps are retryable and durable. The run hibernates for free while waiting on approvals. State and progress survive deploys, evictions, and crashes.
- [**Sandboxes**](https://blog.cloudflare.com/sandbox-ga/) handle the heavy corners — the step that needs `docker build`, the integration suite that needs Postgres running, the Rust compile that needs 8 cores. Snapshots to R2 mean even those warm-start in a couple of seconds.

A traditional CI run for a mid-sized JS repo looks something like: *allocate VM (15-30s) → pull base image (10s) →* `*git clone*` *(10s) →* `*npm ci*` *(30-60s) → run tests (actual work) → tear down*. Several minutes of ceremony before the first test runs, and you pay for the whole VM the whole time.

The same pipeline on this stack looks like: *edge fork of the repo (seconds) → each step boots a fresh isolate or snapshot-restored sandbox in milliseconds → runs the actual work → hibernates.* Nothing has to cold-start. Nothing has to be provisioned ahead of time. Nothing has to be kept warm. The repo doesn't move — the compute comes to it.

CI has never been this fast, and the reason it hasn't is that none of these primitives have existed together in one place. Now they do.

## Try it

`@cloudflare/dynamic-workflows` is MIT-licensed and on npm today:

```shell
npm install @cloudflare/dynamic-workflows
```

It runs on top of Dynamic Workers, which is in open beta on the Workers Paid plan. The [repo](https://github.com/cloudflare/dynamic-workflows) includes a working example — an interactive browser playground where you write a `TenantWorkflow` class, hit **Run**, and watch the steps execute with live-streaming logs and a per-step checklist that lights up as each `step.do()` commits. Clone it, deploy it, show it to a coworker.

If you're a platform, an SDK, a framework, or a CI/CD product, and you want to give your customers their own workflows without running their code in your own process: this is the primitive we built for you. If you're building agents that write durable plans, this is the primitive that makes those plans *real* Workflows. If you're just watching all of this, and it looks fun to build on top of: we'd love to see what you make.

Find us in the [Cloudflare Developers Discord](https://discord.cloudflare.com/).

<iframe title="cloudflare-tv-live-link" src="https://cloudflare.tv/embed/live.html"></iframe>[Workflows](https://blog.cloudflare.com/tag/workflows/) [Cloudflare Workers](https://blog.cloudflare.com/tag/workers/) [Durable Execution](https://blog.cloudflare.com/tag/durable-execution/) [Developer Platform](https://blog.cloudflare.com/tag/developer-platform/) [Developers](https://blog.cloudflare.com/tag/developers/)
