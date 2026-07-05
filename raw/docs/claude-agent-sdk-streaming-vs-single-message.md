Title: Streaming Input - Claude Code Docs

URL Source: https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode

Markdown Content:
> ## Documentation Index
> 
> 
> Fetch the complete documentation index at: [/docs/llms.txt](https://code.claude.com/docs/llms.txt)
> 
> 
> Use this file to discover all available pages before exploring further.

[Skip to main content](https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode#content-area)

[Claude Code Docs home page![Image 1: light logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/light.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=78fd01ff4f4340295a4f66e2ea54903c)![Image 2: dark logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/dark.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=1298a0c3b3a1da603b190d0de0e31712)](https://code.claude.com/docs/en/overview)

English

Search...

⌘K Ask Assistant

*   [Claude Developer Platform](https://platform.claude.com/)
*   [Claude Code on the Web](https://claude.ai/code)
*   [Claude Code on the Web](https://claude.ai/code)

Search...

Navigation

Input and output

Streaming Input

[Getting started](https://code.claude.com/docs/en/overview)[Build with Claude Code](https://code.claude.com/docs/en/agents)[Administration](https://code.claude.com/docs/en/admin-setup)[Configuration](https://code.claude.com/docs/en/settings)[Reference](https://code.claude.com/docs/en/cli-reference)[Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview)[What's New](https://code.claude.com/docs/en/whats-new)[Resources](https://code.claude.com/docs/en/legal-and-compliance)

### Agent SDK

*   [Overview](https://code.claude.com/docs/en/agent-sdk/overview)
*   [Quickstart](https://code.claude.com/docs/en/agent-sdk/quickstart)

### Core concepts

*   [How the agent loop works](https://code.claude.com/docs/en/agent-sdk/agent-loop)
*   [Use Claude Code features](https://code.claude.com/docs/en/agent-sdk/claude-code-features)
*   [Work with sessions](https://code.claude.com/docs/en/agent-sdk/sessions)
*   [Persist sessions to external storage](https://code.claude.com/docs/en/agent-sdk/session-storage)

### Input and output

*   [Streaming Input](https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode)
*   [Handle approvals and user input](https://code.claude.com/docs/en/agent-sdk/user-input)
*   [Stream responses in real-time](https://code.claude.com/docs/en/agent-sdk/streaming-output)
*   [Get structured output from agents](https://code.claude.com/docs/en/agent-sdk/structured-outputs)

### Extend with tools

*   [Give Claude custom tools](https://code.claude.com/docs/en/agent-sdk/custom-tools)
*   [Connect to external tools with MCP](https://code.claude.com/docs/en/agent-sdk/mcp)
*   [Scale to many tools with tool search](https://code.claude.com/docs/en/agent-sdk/tool-search)
*   [Subagents in the SDK](https://code.claude.com/docs/en/agent-sdk/subagents)

### Customize behavior

*   [Modifying system prompts](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts)
*   [Slash Commands in the SDK](https://code.claude.com/docs/en/agent-sdk/slash-commands)
*   [Agent Skills in the SDK](https://code.claude.com/docs/en/agent-sdk/skills)
*   [Plugins in the SDK](https://code.claude.com/docs/en/agent-sdk/plugins)

### Control and observability

*   [Configure permissions](https://code.claude.com/docs/en/agent-sdk/permissions)
*   [Intercept and control agent behavior with hooks](https://code.claude.com/docs/en/agent-sdk/hooks)
*   [Rewind file changes with checkpointing](https://code.claude.com/docs/en/agent-sdk/file-checkpointing)
*   [Track cost and usage](https://code.claude.com/docs/en/agent-sdk/cost-tracking)
*   [Observability with OpenTelemetry](https://code.claude.com/docs/en/agent-sdk/observability)
*   [Todo Lists](https://code.claude.com/docs/en/agent-sdk/todo-tracking)

### Deployment

*   [Hosting the Agent SDK](https://code.claude.com/docs/en/agent-sdk/hosting)
*   [Securely deploying AI agents](https://code.claude.com/docs/en/agent-sdk/secure-deployment)

### SDK references

*   [TypeScript SDK](https://code.claude.com/docs/en/agent-sdk/typescript)
*   [TypeScript V2 (removed)](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview)
*   [Python SDK](https://code.claude.com/docs/en/agent-sdk/python)
*   [Migration Guide](https://code.claude.com/docs/en/agent-sdk/migration-guide)

## On this page

*   [Overview](https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode#overview)
*   [Streaming Input Mode (Recommended)](https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode#streaming-input-mode-recommended)
    *   [How It Works](https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode#how-it-works)
    *   [Benefits](https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode#benefits)
    *   [Implementation Example](https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode#implementation-example)

*   [Single Message Input](https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode#single-message-input)
    *   [When to Use Single Message Input](https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode#when-to-use-single-message-input)
    *   [Limitations](https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode#limitations)
    *   [Implementation Example](https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode#implementation-example-2)

Input and output

# Streaming Input

Copy page

Understanding the two input modes for Claude Agent SDK and when to use each

Copy page

## [​](https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode#overview)

Overview

The Claude Agent SDK supports two distinct input modes for interacting with agents:
*   **Streaming Input Mode** (Default & Recommended) - A persistent, interactive session
*   **Single Message Input** - One-shot queries that use session state and resuming

This guide explains the differences, benefits, and use cases for each mode to help you choose the right approach for your application.
## [​](https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode#streaming-input-mode-recommended)

Streaming Input Mode (Recommended)

Streaming input mode is the **preferred** way to use the Claude Agent SDK. It provides full access to the agent’s capabilities and enables rich, interactive experiences.It allows the agent to operate as a long lived process that takes in user input, handles interruptions, surfaces permission requests, and handles session management.
### [​](https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode#how-it-works)

How It Works

### [​](https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode#benefits)

Benefits

## Image Uploads

Attach images directly to messages for visual analysis and understanding

## Queued Messages

Send multiple messages that process sequentially, with ability to interrupt

## Tool Integration

Full access to all tools and custom MCP servers during the session

## Real-time Feedback

See responses as they’re generated, not just final results

## Context Persistence

Maintain conversation context across multiple turns naturally

### [​](https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode#implementation-example)

Implementation Example

TypeScript

Python

```
import { query, type SDKUserMessage } from "@anthropic-ai/claude-agent-sdk";
import { readFile } from "fs/promises";

async function* generateMessages(): AsyncGenerator<SDKUserMessage> {
  // First message
  yield {
    type: "user",
    message: {
      role: "user",
      content: "Analyze this codebase for security issues"
    },
    parent_tool_use_id: null
  };

  // Wait for conditions or user input
  await new Promise((resolve) => setTimeout(resolve, 2000));

  // Follow-up with image
  yield {
    type: "user",
    message: {
      role: "user",
      content: [
        {
          type: "text",
          text: "Review this architecture diagram"
        },
        {
          type: "image",
          source: {
            type: "base64",
            media_type: "image/png",
            data: await readFile("diagram.png", "base64")
          }
        }
      ]
    },
    parent_tool_use_id: null
  };
}

// Process streaming responses
for await (const message of query({
  prompt: generateMessages(),
  options: {
    maxTurns: 10,
    allowedTools: ["Read", "Grep"]
  }
})) {
  if (message.type === "result" && message.subtype === "success") {
    console.log(message.result);
  }
}
```

In the TypeScript SDK, if your message generator throws, for example when a file it reads is missing, the stream ends with an error that reads `Claude Code process aborted by user` instead of the original error, so check the code inside your generator first when you see that message. The error may also be preceded by a long minified line of bundled SDK source, so read to the end of the output for the error text.In the Python SDK, a generator exception is logged at debug level and the session stalls without raising, so if a streaming session hangs with no output, enable debug logging and check your generator.

## [​](https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode#single-message-input)

Single Message Input

Single message input is simpler but more limited.
### [​](https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode#when-to-use-single-message-input)

When to Use Single Message Input

Use single message input when:
*   You need a one-shot response
*   You do not need image attachments or mid-session control methods
*   You need to operate in a stateless environment, such as a lambda function

### [​](https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode#limitations)

Limitations

Single message input mode does **not** support:
*   Direct image attachments in messages
*   Dynamic message queueing
*   Real-time interruption
*   Natural multi-turn conversations

If a query ends with an error result, such as `error_max_turns`, a single message `query()` call raises an error that includes the failure text after yielding the final result message, so wrap the loop in a try block if your code needs to continue. See [Handle the result](https://code.claude.com/docs/en/agent-sdk/agent-loop#handle-the-result) for the result subtypes.
### [​](https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode#implementation-example-2)

Implementation Example

TypeScript

Python

```
import { query } from "@anthropic-ai/claude-agent-sdk";

// Simple one-shot query
for await (const message of query({
  prompt: "Explain the authentication flow",
  options: {
    maxTurns: 1,
    allowedTools: ["Read", "Grep"]
  }
})) {
  if (message.type === "result" && message.subtype === "success") {
    console.log(message.result);
  }
}

// Continue conversation with session management
for await (const message of query({
  prompt: "Now explain the authorization process",
  options: {
    continue: true,
    maxTurns: 1
  }
})) {
  if (message.type === "result" && message.subtype === "success") {
    console.log(message.result);
  }
}
```

Was this page helpful?

Yes No

[Persist sessions to external storage](https://code.claude.com/docs/en/agent-sdk/session-storage)[Handle approvals and user input](https://code.claude.com/docs/en/agent-sdk/user-input)

⌘I

[Claude Code Docs home page![Image 3: light logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/light.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=78fd01ff4f4340295a4f66e2ea54903c)![Image 4: dark logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/dark.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=1298a0c3b3a1da603b190d0de0e31712)](https://code.claude.com/docs/en/overview)

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)

Company

[Anthropic](https://www.anthropic.com/company)[Careers](https://www.anthropic.com/careers)[Economic Futures](https://www.anthropic.com/economic-futures)[Research](https://www.anthropic.com/research)[News](https://www.anthropic.com/news)[Trust center](https://trust.anthropic.com/)[Transparency](https://www.anthropic.com/transparency)

Help and security

[Availability](https://www.anthropic.com/supported-countries)[Status](https://status.anthropic.com/)[Support center](https://support.claude.com/)

Learn

[Courses](https://www.anthropic.com/learn)[MCP connectors](https://claude.com/partners/mcp)[Customer stories](https://www.claude.com/customers)[Engineering blog](https://www.anthropic.com/engineering)[Events](https://www.anthropic.com/events)[Powered by Claude](https://claude.com/partners/powered-by-claude)[Service partners](https://claude.com/partners/services)[Startups program](https://claude.com/programs/startups)

Terms and policies

[Privacy choices](https://www.anthropic.com/legal/privacy)[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)

Assistant

Responses are generated using AI and may contain mistakes.
