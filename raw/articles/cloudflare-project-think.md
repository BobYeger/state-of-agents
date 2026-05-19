# Project Think: building the next generation of AI agents on Cloudflare

Source URL: https://blog.cloudflare.com/project-think/

Summary: Announcing a preview of the next edition of the Agents SDK — from lightweight primitives to a batteries-included platform for AI agents that think, act, and persist.

Capture note: readable local markdown snapshot generated from the archived HTML capture. Remote images and decorative page chrome are omitted.


2026-04-15

- /author/sunil/ Sunil Pai (/author/sunil/)

- /author/kate-reznykova/ Kate Reznykova (/author/kate-reznykova/)

Today, we're introducing Project Think: the next generation of the Agents SDK (https://developers.cloudflare.com/agents/). Project Think is a set of new primitives for building long-running agents (durable execution, sub-agents, sandboxed code execution, persistent sessions) and an opinionated base class that wires them all together. Use the primitives to build exactly what you need, or use the base class to get started fast.

Something happened earlier this year that changed how we think about AI. Tools like Pi (https://github.com/badlogic/pi-mono), OpenClaw (https://github.com/openclaw), Claude Code (https://docs.anthropic.com/en/docs/agents), and Codex (https://openai.com/codex) proved a simple but powerful idea: give an LLM the ability to read files, write code, execute it, and remember what it learned, and you get something that looks less like a developer tool and more like a general-purpose assistant.

These coding agents aren't just writing code anymore. People are using them to manage calendars, analyze datasets, negotiate purchases, file taxes, and automate entire business workflows. The pattern is always the same: the agent reads context, reasons about it, writes code to take action, observes the result, and iterates. Code is the universal medium of action.

Our team has been using these coding agents every day. And we kept running into the same walls:

- They only run on your laptop or an expensive VPS: there's no sharing, no collaboration, no handoff between devices.

- They're expensive when idle : a fixed monthly cost whether the agent is working or not. Scale that to a team, or a company, and it adds up fast.

- They require management and manual setup : installing dependencies, managing updates, configuring identity and secrets.

And there's a deeper structural issue. Traditional applications serve many users from one instance. As mentioned in our Welcome to Agents Week post, agents are one-to-one (https://blog.cloudflare.com/welcome-to-agents-week/). Each agent is a unique instance, serving one user, running one task. A restaurant has a menu and a kitchen optimized to churn out dishes at volume. An agent is more like a personal chef: different ingredients, different techniques, different tools every time.

That fundamentally changes the scaling math. If a hundred million knowledge workers each use an agentic assistant at even modest concurrency, you need capacity for tens of millions of simultaneous sessions. At current per-container costs, that's unsustainable. We need a different foundation.

That's what we've been building.

## Introducing Project Think

Project Think ships a set of new primitives for the Agents SDK:

- Durable execution with fibers: crash recovery, checkpointing, automatic keepalive

- Sub-agents : isolated child agents with their own SQLite and typed RPC

- Persistent sessions : tree-structured messages, forking, compaction, full-text search

- Sandboxed code execution : Dynamic Workers, codemode, runtime npm resolution

- The execution ladder : workspace, isolate, npm, browser, sandbox

- Self-authored extensions : agents that write their own tools at runtime

Each of these is usable directly with the Agent base class. Build exactly what you need with the primitives, or use the Think base class to get started fast. Let's look at what each one does.

## Long-running agents

Agents, as they exist today, are ephemeral. They run for a session, tied to a single process or device, and then they are gone. A coding agent that dies when your laptop sleeps, that’s a tool. An agent that persists — that can wake up on demand, continue work after interruptions, and carry forward the state without depending on your local runtime — that starts to look like infrastructure. And it changes the scaling model for agents completely.

The Agents SDK builds on Durable Objects (https://developers.cloudflare.com/durable-objects/) to give every agent an identity, persistent state, and the ability to wake on message. This is the actor model (https://en.wikipedia.org/wiki/Actor_model): each agent is an addressable entity with its own SQLite database. It consumes zero compute when hibernated. When something happens (an HTTP request, a WebSocket message, a scheduled alarm, an inbound email) the platform wakes the agent, loads its state, and hands it the event. The agent does its work, then goes back to sleep.

VMs / Containers

Durable Objects

Idle cost

Full compute cost, always

Zero (hibernated)

Scaling

Provision and manage capacity

Automatic, per-agent

State

External database required

Built-in SQLite

Recovery

You build it (process managers, health checks)

Platform restarts, state survives

Identity / routing

You build it (load balancers, sticky sessions)

Built-in (name → agent)

10,000 agents, each active 1% of the time

10,000 always-on instances

~100 active at any moment

This changes the economics of running agents at scale. Instead of "one expensive agent per power user," you can build "one agent per customer" or "one agent per task" or "one agent per email thread." The marginal cost of spawning a new agent is effectively zero.

### Surviving crashes: durable execution with fibers

An LLM call takes 30 seconds. A multi-turn agent loop can run for much longer. At any point during that window, the execution environment can vanish: a deploy, a platform restart, hitting resource limits. The upstream connection to the model provider is severed permanently, in-memory state is lost, and connected clients see the stream stop with no explanation.

runFiber() (https://developers.cloudflare.com/agents/api-reference/durable-execution/) solves this. A fiber is a durable function invocation: registered in SQLite before execution begins, checkpointable at any point via stash() , and recoverable on restart via onFiberRecovered .

import { Agent } from "agents";
export class ResearchAgent extends Agent {
async startResearch(topic: string) {
void this.runFiber("research", async (ctx) => {
const findings = [];
for (let i = 0; i
The SDK keeps the agent alive automatically during fiber execution, no special configuration needed. For work measured in minutes, keepAlive() / keepAliveWhile() prevents eviction during active work. For longer operations (CI pipelines, design reviews, video generation) the agent starts the work, persists the job ID, hibernates, and wakes on callback.

### Delegating work: sub-agents via Facets

A single agent shouldn't do everything itself. Sub-agents (https://developers.cloudflare.com/agents/api-reference/sub-agents/) are child Durable Objects colocated with the parent via Facets (https://blog.cloudflare.com/durable-object-facets-dynamic-workers/), each with their own isolated SQLite and execution context:

import { Agent } from "agents";
export class ResearchAgent extends Agent {
async search(query: string) { /* ... */ }
}
export class ReviewAgent extends Agent {
async analyze(query: string) { /* ... */ }
}
export class Orchestrator extends Agent {
async handleTask(task: string) {
const researcher = await this.subAgent(ResearchAgent, "research");
const reviewer = await this.subAgent(ReviewAgent, "review");
const [research, review] = await Promise.all([
researcher.search(task),
reviewer.analyze(task)
]);
return this.synthesize(research, review);
}
}
Sub-agents are isolated at the storage level. Each one gets its own SQLite database, and there’s no implicit sharing of data between them. This is enforced by the runtime where sub-agent RPC latency is a function call. TypeScript catches misuse at compile time.

### Conversations that persist: the Session API

Agents that run for days or weeks need more than the typical flat list of messages. The experimental Session API (https://developers.cloudflare.com/agents/api-reference/sessions/) models this explicitly. Available on the Agent base class, conversations are stored as trees, where each message has a parent_id. This enables forking (explore an alternative without losing the original path), non-destructive compaction (summarize older messages rather than deleting them), and full-text search across conversation history via FTS5 (https://www.sqlite.org/fts5.html).

import { Agent } from "agents";
import { Session, SessionManager } from "agents/experimental/memory/session";
export class MyAgent extends Agent {
sessions = SessionManager.create(this);
async onStart() {
const session = this.sessions.create("main");
const history = session.getHistory();
const forked = this.sessions.fork(session.id, messageId, "alternative-approach");
}
}
Session is usable directly with Agent , and it's the storage layer that the Think base class builds on.

## From tool calls to code execution

Conventional tool-calling has an awkward shape. The model calls a tool, pulls the result back through the context window, calls another tool, pulls that back, and so on. As the tool surface grows, this gets both expensive and clumsy. A hundred files means a hundred round-trips through the model.

But models are better at writing code to use a system than they are at playing the tool-calling game (https://blog.cloudflare.com/code-mode/). This is the insight behind @cloudflare/codemode (https://github.com/cloudflare/agents/tree/main/packages/codemode): instead of sequential tool calls, the LLM writes a single program that handles the entire task.

// The LLM writes this. It runs in a sandboxed Dynamic Worker.
const files = await tools.find({ pattern: "**/*.ts" });
const results = [];
for (const file of files) {
const content = await tools.read({ path: file });
if (content.includes("TODO")) {
results.push({ file, todos: content.match(/\/\/ TODO:.*/g) });
}
}
return results;
Instead of 100 round-trips to the model, you just run a single program. This leads to fewer tokens used, faster execution, and better results. The Cloudflare API MCP server (https://github.com/cloudflare/mcp) demonstrates this at scale. We expose only two tools (search() and execute()) , which consume ~1,000 tokens, vs. ~1.17 million tokens for the naive tool-per-endpoint equivalent. This is a 99.9% reduction.

### The missing primitive: safe sandboxes

Once you accept that models should write code on behalf of users, the question becomes: where does that code run? Not eventually, not after a product team turns it into a roadmap item. Right now, for this user, against this system, with tightly defined permissions.

Dynamic Workers (https://blog.cloudflare.com/dynamic-workers/) are that sandbox. A fresh V8 isolate spun up at runtime, in milliseconds, with a few megabytes of memory. That's roughly 100x faster and up to 100x more memory-efficient than a container. You can start a new one for every single request, run a snippet of code, and throw it away.

The critical design choice is the capability model. Instead of starting with a general-purpose machine and trying to constrain it, Dynamic Workers begin with almost no ambient authority ( globalOutbound: null , no network access) and the developer grants capabilities explicitly, resource by resource, through bindings. We go from asking "how do we stop this thing from doing too much?" to "what exactly do we want this thing to be able to do?"

This is the right question for agent infrastructure.

### The execution ladder

This capability model leads naturally to a spectrum of compute environments, an execution ladder that the agent escalates through as needed:

Tier 0 is the Workspace, a durable virtual filesystem backed by SQLite and R2. Read, write, edit, search, grep, diff. Powered by @cloudflare/shell (https://www.npmjs.com/package/@cloudflare/shell).

Tier 1 is a Dynamic Worker: LLM-generated JavaScript running in a sandboxed isolate with no network access. Powered by @cloudflare/codemode (https://www.npmjs.com/package/@cloudflare/codemode).

Tier 2 adds npm. @cloudflare/worker-bundler (https://github.com/cloudflare/agents/tree/main/packages/worker-bundler) fetches packages from the registry, bundles them with esbuild, and loads the result into the Dynamic Worker. The agent writes import { z } from "zod" and it just works.

Tier 3 is a headless browser via Cloudflare Browser Run (https://developers.cloudflare.com/browser-rendering/). Navigate, click, extract, screenshot. Useful when the service doesn't support agents yet via MCP or APIs.

Tier 4 is a Cloudflare Sandbox (https://developers.cloudflare.com/sandbox/) configured with your toolchains, repos, and dependencies: git clone, npm test, cargo build , synced bidirectionally with the Workspace.

The key design principle: the agent should be useful at Tier 0 alone, where each tier is additive. The user can add capabilities as they go.

### Building blocks, not a framework

All of these primitives are available as standalone packages. Dynamic Workers (https://blog.cloudflare.com/dynamic-workers/), @cloudflare/codemode (https://github.com/cloudflare/agents/tree/main/packages/codemode), @cloudflare/worker-bundler (https://github.com/cloudflare/agents/tree/main/packages/worker-bundler), and @cloudflare/shell (https://www.npmjs.com/package/@cloudflare/shell) (a durable filesystem with tools) are all usable directly with the Agent base class. You can combine them to give any agent a workspace, code execution, and runtime package resolution without adopting an opinionated framework.

## The platform

Here's the complete stack for building agents on Cloudflare:

Capability

What it does

Powered by

Per-agent isolation

Every agent is its own world

Durable Objects (https://developers.cloudflare.com/durable-objects/) (DOs)

Zero cost when idle

$0 until the agent wakes up

DO Hibernation (https://developers.cloudflare.com/durable-objects/best-practices/websockets/#websocket-hibernation-api)

Persistent state

Queryable, transactional storage

DO SQLite (https://developers.cloudflare.com/durable-objects/best-practices/access-durable-objects-storage/)

Durable filesystem

Files that survive restarts

Workspace (SQLite + R2 (https://developers.cloudflare.com/r2/))

Sandboxed code execution

Run LLM-generated code safely

Dynamic Workers (https://blog.cloudflare.com/dynamic-workers/) + @cloudflare/codemode (https://github.com/cloudflare/agents/tree/main/packages/codemode)

Runtime dependencies

import * from react just works

@cloudflare/worker-bundler (https://github.com/cloudflare/agents/tree/main/packages/worker-bundler)

Web automation

Browse, navigate, fill forms

Browser Run (https://developers.cloudflare.com/browser-rendering/)

Full OS access

git, compilers, test runners

Sandboxes (https://developers.cloudflare.com/sandbox/)

Scheduled execution

Proactive, not just reactive

DO Alarms + Fibers (https://developers.cloudflare.com/durable-objects/api/alarms/)

Real-time streaming

Token-by-token to any client

WebSockets

External tools

Connect to any tool server

MCP

Agent coordination

Typed RPC between agents

Sub-agents (Facets (https://developers.cloudflare.com/dynamic-workers/usage/durable-object-facets/))

Model access

Connect to an LLM to power the agent

AI Gateway (https://developers.cloudflare.com/ai-gateway/) + Workers AI (https://developers.cloudflare.com/workers-ai/) (or Bring Your Own Model)

Each of these is a building block. Together, they form something new: a platform where anyone can build, deploy, and run AI agents as capable as the ones running on your local machine today, but serverless (https://www.cloudflare.com/learning/serverless/what-is-serverless/), durable, and safe by construction.

## The Think base class

Now that you've seen the primitives, here's what happens when you wire them all together.

Think is an opinionated harness that handles the full chat lifecycle: agentic loop, message persistence, streaming, tool execution, stream resumption, and extensions. You focus on what makes your agent unique.

The minimal subclass looks like this:

import { Think } from "@cloudflare/think";
import { createWorkersAI } from "workers-ai-provider";
export class MyAgent extends Think {
getModel() {
return createWorkersAI({ binding: this.env.AI })(
"@cf/moonshotai/kimi-k2.5"
);
}
}
That’s effectively all you need to have a working chat agent with streaming, persistence, abort/cancel, error handling, resumable streams, and a built-in workspace filesystem. Deploy with npx wrangler deploy .

Think makes decisions for you. When you need more control, you can override the ones you care about:

Override

Purpose

getModel()

Return the LanguageModel to use

getSystemPrompt()

System prompt

getTools()

AI SDK compatible ToolSet for the agentic loop

maxSteps

Max tool-call rounds per turn

configureSession()

Context blocks, compaction, search, skills

Under the hood, Think runs the complete agentic loop on every turn: it assembles the context (base instructions + tool descriptions + skills + memory + conversation history), calls streamText , executes tool calls (with output truncation to prevent context blowup), appends results, loops until the model is done or the step limit is reached. All messages are persisted after each turn.

### Lifecycle hooks

Think gives you hooks at every stage of the chat turn, without requiring you to own the whole pipeline:

beforeTurn()
→ streamText()
→ beforeToolCall()
→ afterToolCall()
→ onStepFinish()
→ onChatResponse()
Switch to a lower cost model for follow-up turns, limit the tools it can use, and pass in client-side context on each turn. Also log every tool call to analytics and automatically trigger one more follow-up turn after the model completes, all without replacing onChatMessage .

### Persistent memory and long conversations

Think builds on Session API (https://developers.cloudflare.com/agents/api-reference/sessions/?cf_target_id=E7A3D837FA7DC4C7DDA822B3DE0F831B) as its storage layer, giving you tree-structured messages with branching built in.

On top of that, it adds persistent memory through context blocks . These are structured sections of the system prompt that the model can read and update over time, and they persist across hibernation . The model sees "MEMORY (Important facts, use set_context to update) [42%, 462/1100 tokens]" and can proactively remember things.

configureSession(session: Session) {
return session
.withContext("soul", {
provider: { get: async () => "You are a helpful coding assistant." }
})
.withContext("memory", {
description: "Important facts learned during conversation.",
maxTokens: 2000
})
.withCachedPrompt();
}
Sessions are flexible. You can run multiple conversations per agent and fork them to try a different direction without losing the original.

As context grows, Think handles limits with non-destructive compaction. Older messages are summarized instead of removed, while the full history remains stored in SQLite.

Search is built in as well. Using FTS5, you can query conversation history within a session or across all the sessions. The agent is also able to search its own past using search_context tool.

### The full execution ladder, wired in

Think integrates the entire execution ladder into a single getTools() return:

import { Think } from "@cloudflare/think";
import { createWorkspaceTools } from "@cloudflare/think/tools/workspace";
import { createExecuteTool } from "@cloudflare/think/tools/execute";
import { createBrowserTools } from "@cloudflare/think/tools/browser";
import { createSandboxTools } from "@cloudflare/think/tools/sandbox";
import { createExtensionTools } from "@cloudflare/think/tools/extensions";
export class MyAgent extends Think {
extensionLoader = this.env.LOADER;
getModel() {
/* ... */
}
getTools() {
return {
execute: createExecuteTool({
tools: createWorkspaceTools(this.workspace),
loader: this.env.LOADER
}),
...createBrowserTools(this.env.BROWSER),
...createSandboxTools(this.env.SANDBOX), // configured per-agent: toolchains, repos, snapshots
...createExtensionTools({ manager: this.extensionManager! }),
...this.extensionManager!.getTools()
};
}
}
Self-authored extensions
#self-authored-extensions
Think takes code execution one step further. An agent can write its own extensions: TypeScript programs that run in Dynamic Workers, declaring permissions for network access and workspace operations.

{
"name": "github",
"description": "GitHub integration: PRs, issues, repos",
"tools": ["create_pr", "list_issues", "review_pr"],
"permissions": {
"network": ["api.github.com"],
"workspace": "read-write"
}
}
Think's ExtensionManager bundles the extension (optionally with npm deps via @cloudflare/worker-bundler ), loads it into a Dynamic Worker, and registers the new tools. The extension persists in DO storage and survives hibernation. The next time the user asks about pull requests, the agent has a github_create_pr tool that didn't exist 30 seconds ago.

This is the kind of self-improvement loop that makes agents genuinely more useful over time. Not through fine-tuning or RLHF, but through code. The agent is able to write new capabilities for itself, all in sandboxed, auditable, and revocable TypeScript.

### Sub-agent RPC

Think also works as a sub-agent, called via chat() over RPC from a parent, with streaming events via callback:

const researcher = await this.subAgent(ResearchSession, "research");
const result = await researcher.chat(`Research this: ${task}`, streamRelay);
Each child gets its own conversation tree, memory, tools, and model. The parent doesn't need to know the details.

### Getting started

Project Think is experimental. The API surface is stable but will continue to evolve in the coming days and weeks. We're already using it internally to build our own background agent infrastructure, and we're sharing it early so you can build alongside us.

npm install @cloudflare/think agents ai @cloudflare/shell zod workers-ai-provider
// src/server.ts
import { Think } from "@cloudflare/think";
import { createWorkersAI } from "workers-ai-provider";
import { routeAgentRequest } from "agents";
export class MyAgent extends Think {
getModel() {
return createWorkersAI({ binding: this.env.AI })(
"@cf/moonshotai/kimi-k2.5"
);
}
}
export default {
async fetch(request: Request, env: Env) {
return (
(await routeAgentRequest(request, env)) ||
new Response("Not found", { status: 404 })
);
}
} satisfies ExportedHandler ;
// src/client.tsx
import { useAgent } from "agents/react";
import { useAgentChat } from "@cloudflare/ai-chat/react";
function Chat() {
const agent = useAgent({ agent: "MyAgent" });
const { messages, sendMessage, status } = useAgentChat({ agent });
// Render your chat UI
}
Think speaks the same WebSocket protocol as @cloudflare/ai-chat , so existing UI components work out of the box. If you've built on AIChatAgent (https://developers.cloudflare.com/agents/api-reference/chat-agents/), your client code doesn't change.

## The third wave

We see three waves of AI agents:

The first wave was chatbots. They were stateless, reactive, and fragile. Every conversation started from scratch with no memory, no tools, and no ability to act. This made them useful for answering questions, but limited them to only answering questions.

The second wave was coding agents. These are stateful, tool-using and far more capable tools like Pi, Claude Code, OpenClaw, and Codex. These agents can read codebases, write code, execute it, and iterate. These proved that an LLM with the right tools is a general-purpose machine, but they run on your laptop, for one user, with no durability guarantees.

Now we are entering the third wave: agents as infrastructure. Durable, distributed, structurally safe, and serverless. These are agents that run on the Internet, survive failures, cost nothing when idle, and enforce security through architecture rather than behavior. Agents that any developer can build and deploy for any number of users.

This is the direction we’re betting on.

The Agents SDK is already powering thousands of production agents. With Project Think and the the primitives it introduces, we're adding the missing pieces to make those agents dramatically more capable: persistent workspaces, sandboxed code execution, durable long-running tasks, structural security, sub-agent coordination, and self-authored extensions.

It's available today in preview. We're building alongside you, and we'd genuinely love to see what you (and your coding agent) create with it.

Think is part of the Cloudflare Agents SDK, available as @cloudflare/think. The features described in this post are in preview. APIs may change as we incorporate feedback. Check the documentation (https://github.com/cloudflare/agents/blob/main/docs/think/index.md) and example (https://github.com/cloudflare/agents/tree/main/examples/assistant) to get started.