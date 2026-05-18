Title: Introduction - OpenHarness

URL Source: https://docs.open-harness.dev/

Markdown Content:
# Introduction - OpenHarness

[Skip to main content](https://docs.open-harness.dev/#content-area)

[OpenHarness home page![Image 1: light logo](https://mintcdn.com/max-8f0c51d4/6CLDhc2myLoLNqya/logo/light.svg?fit=max&auto=format&n=6CLDhc2myLoLNqya&q=85&s=33ca0828c712c8e50b5c40e397889d7d)![Image 2: dark logo](https://mintcdn.com/max-8f0c51d4/6CLDhc2myLoLNqya/logo/dark.svg?fit=max&auto=format&n=6CLDhc2myLoLNqya&q=85&s=868e0d82995f12ca99aa5e41fa70830b)](https://docs.open-harness.dev/)

Search...

Ctrl K

##### Getting Started

*   [Introduction](https://docs.open-harness.dev/)
*   [Installation](https://docs.open-harness.dev/getting-started/installation)
*   [Quickstart](https://docs.open-harness.dev/getting-started/quickstart)

##### Core Concepts

*   [Agents](https://docs.open-harness.dev/core/agents)
*   [Sessions](https://docs.open-harness.dev/core/sessions)
*   [Middleware & Conversation](https://docs.open-harness.dev/core/middleware)
*   [Providers](https://docs.open-harness.dev/core/providers)

##### Tools

*   [Built-in Tools](https://docs.open-harness.dev/tools/built-in-tools)
*   [Custom Tools](https://docs.open-harness.dev/tools/custom-tools)
*   [Permissions](https://docs.open-harness.dev/tools/permissions)

##### Advanced

*   [Subagents](https://docs.open-harness.dev/advanced/subagents)
*   [MCP Servers](https://docs.open-harness.dev/advanced/mcp-servers)
*   [Skills](https://docs.open-harness.dev/advanced/skills)
*   [AGENTS.md](https://docs.open-harness.dev/advanced/agents-md)

##### UI Integration

*   [Server Streaming](https://docs.open-harness.dev/ui-integration/server-streaming)
*   [React](https://docs.open-harness.dev/ui-integration/react)
*   [Vue](https://docs.open-harness.dev/ui-integration/vue)

##### Resources

*   [Examples](https://docs.open-harness.dev/examples)

*   [Website](https://open-harness.dev/)
*   [GitHub](https://github.com/MaxGfeller/open-harness)
*    

[OpenHarness home page![Image 3: light logo](https://mintcdn.com/max-8f0c51d4/6CLDhc2myLoLNqya/logo/light.svg?fit=max&auto=format&n=6CLDhc2myLoLNqya&q=85&s=33ca0828c712c8e50b5c40e397889d7d)![Image 4: dark logo](https://mintcdn.com/max-8f0c51d4/6CLDhc2myLoLNqya/logo/dark.svg?fit=max&auto=format&n=6CLDhc2myLoLNqya&q=85&s=868e0d82995f12ca99aa5e41fa70830b)](https://docs.open-harness.dev/)

Search...

Ctrl K

*   [Website](https://open-harness.dev/)
*   [GitHub](https://github.com/MaxGfeller/open-harness)

Search...

Navigation

Getting Started

Introduction

[Documentation](https://docs.open-harness.dev/)

[Documentation](https://docs.open-harness.dev/)

Getting Started

# Introduction

Build capable, general-purpose AI agents in code

> ## Documentation Index
> 
> 
> Fetch the complete documentation index at: [https://docs.open-harness.dev/llms.txt](https://docs.open-harness.dev/llms.txt)
> 
> 
> Use this file to discover all available pages before exploring further.

OpenHarness is an open-source framework for building general-purpose AI agents programmatically. Built on [Vercel’s AI SDK](https://sdk.vercel.ai/), it provides the building blocks inspired by Claude Code, Codex, and similar advanced agent harnesses — but in a lightweight, composable form you can use in your own applications.
## [​](https://docs.open-harness.dev/#why-openharness)

Why OpenHarness?

Agent harnesses like Claude Code, Codex, and OpenCode are powerful general-purpose agents. While their creators offer SDKs (Claude Agent SDK, Codex App Server, etc.), these are heavy to use programmatically.OpenHarness gives you the same building blocks — multi-step tool loops, subagent delegation, context compaction, streaming UI integration — as composable primitives you control entirely in code.
## [​](https://docs.open-harness.dev/#key-features)

Key Features

## Stateless Agents

Agents are pure executors: pass in history, get back events. Full control over conversation state.

## Composable Middleware

Add compaction, retry, persistence, and hooks as independent, composable layers.

## Subagent Delegation

Agents can spawn child agents for subtasks, with configurable nesting depth and background execution.

## Provider Abstraction

Filesystem and shell access through swappable providers — run locally, in sandboxes, or in the cloud.

## MCP Integration

Connect to Model Context Protocol servers for external tools via stdio, HTTP, or SSE transports.

## AI SDK 5 UI Streaming

Stream agent sessions directly to React or Vue chat UIs with typed data parts.

## [​](https://docs.open-harness.dev/#quick-example)

Quick Example

```
import { Agent, createFsTools, createBashTool, NodeFsProvider, NodeShellProvider } from "@openharness/core";
import { openai } from "@ai-sdk/openai";

const agent = new Agent({
  name: "dev",
  model: openai("gpt-5.4"),
  tools: {
    ...createFsTools(new NodeFsProvider()),
    ...createBashTool(new NodeShellProvider()),
  },
  maxSteps: 20,
});

for await (const event of agent.run([], "Refactor the auth module")) {
  if (event.type === "text.delta") process.stdout.write(event.text);
}
```

[Installation Install OpenHarness packages in your project Next](https://docs.open-harness.dev/getting-started/installation)

Ctrl+I

[github](https://github.com/MaxGfeller/open-harness)

[Powered by This documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com/?utm_campaign=poweredBy&utm_medium=referral&utm_source=max-8f0c51d4)

On this page

*   [Why OpenHarness?](https://docs.open-harness.dev/#why-openharness)
*   [Key Features](https://docs.open-harness.dev/#key-features)
*   [Quick Example](https://docs.open-harness.dev/#quick-example)
