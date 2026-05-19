Title: Build and deploy Remote Model Context Protocol (MCP) servers to Cloudflare

URL Source: https://blog.cloudflare.com/remote-model-context-protocol-servers-mcp/

Published Time: 2025-03-25T13:59+00:00

Markdown Content:
2025-03-25

9 min read


It feels like almost everyone building AI applications and [agents](https://www.cloudflare.com/learning/ai/what-is-agentic-ai/) is talking about the [Model Context Protocol](https://www.cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/) (MCP), as well as building MCP servers that you install and run locally on your own computer.

You can now [build and deploy remote MCP servers](https://developers.cloudflare.com/agents/guides/remote-mcp-server/) to Cloudflare. We’ve added four things to Cloudflare that handle the hard parts of building remote MCP servers for you:

1.   [workers-oauth-provider](https://developers.cloudflare.com/agents/model-context-protocol/authorization) — an [OAuth](https://www.cloudflare.com/learning/access-management/what-is-oauth/) Provider that makes authorization easy

2.   [McpAgent](https://developers.cloudflare.com/agents/model-context-protocol/tools/) —a class built into the [Cloudflare Agents SDK](https://developers.cloudflare.com/agents/) that handles remote transport

3.   [mcp-remote](https://developers.cloudflare.com/agents/guides/test-remote-mcp-server/) —an adapter that lets MCP clients that otherwise only support local connections work with remote MCP servers

4.   [AI playground as a remote MCP client](https://playground.ai.cloudflare.com/) —a chat interface that allows you to connect to remote MCP servers, with the authentication check included

The button below, or the [developer docs](https://developers.cloudflare.com/agents/guides/remote-mcp-server/), will get you up and running in production with [this example MCP server](https://github.com/cloudflare/ai/tree/main/demos/remote-mcp-server) in less than two minutes:

[![Image 2: Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/ai/tree/main/demos/remote-mcp-server)

Unlike the local MCP servers you may have previously used, remote MCP servers are accessible on the Internet. People simply sign in and grant permissions to MCP clients using familiar authorization flows. We think this is going to be a massive deal — connecting coding agents to MCP servers has blown developers’ minds over the past few months, and remote MCP servers have the same potential to open up similar new ways of working with LLMs and agents to a much wider audience, including more everyday consumer use cases.

## From local to remote —bringing MCP to the masses

MCP is quickly becoming the common protocol that enables LLMs to go beyond [inference](https://www.cloudflare.com/learning/ai/inference-vs-training/) and [RAG](https://developers.cloudflare.com/reference-architecture/diagrams/ai/ai-rag/), and take actions that require access beyond the AI application itself (like sending an email, deploying a code change, publishing blog posts, you name it). It enables AI agents (MCP clients) to access tools and resources from external services (MCP servers).

To date, MCP has been limited to running locally on your own machine — if you want to access a tool on the web using MCP, it’s up to you to set up the server locally. You haven’t been able to use MCP from web-based interfaces or mobile apps, and there hasn’t been a way to let people authenticate and grant the MCP client permission. Effectively, MCP servers haven’t yet been brought online.

Support for [remote MCP connections](https://spec.modelcontextprotocol.io/specification/draft/basic/transports/#streamable-http) changes this. It creates the opportunity to reach a wider audience of Internet users who aren’t going to install and run MCP servers locally for use with desktop apps. Remote MCP support is like the transition from desktop software to web-based software. People expect to continue tasks across devices and to login and have things just work. Local MCP is great for developers, but remote MCP connections are the missing piece to reach everyone on the Internet.

## Making authentication and authorization just work with MCP

Beyond just changing the transport layer — from [stdio](https://modelcontextprotocol.io/docs/concepts/transports#standard-input%2Foutput-stdio) to [streamable HTTP](https://github.com/modelcontextprotocol/specification/pull/206) — when you build a remote MCP server that uses information from the end user’s account, you need [authentication and authorization](https://www.cloudflare.com/learning/access-management/authn-vs-authz/). You need a way to allow users to login and prove who they are (authentication) and a way for users to control what the AI agent will be able to access when using a service (authorization).

MCP does this with [OAuth](https://oauth.net/2/), which has been the standard protocol that allows users to grant applications to access their information or services, without sharing passwords. Here, the MCP Server itself acts as the OAuth Provider. However, OAuth with MCP is hard to implement yourself, so when you build MCP servers on Cloudflare we provide it for you.

### workers-oauth-provider — an OAuth 2.1 Provider library for Cloudflare Workers

When you [deploy an MCP Server](https://developers.cloudflare.com/agents/guides/remote-mcp-server/) to Cloudflare, your Worker acts as an OAuth Provider, using [workers-oauth-provider](https://github.com/cloudflare/workers-oauth-provider), a new TypeScript library that wraps your Worker’s code, adding authorization to API endpoints, including (but not limited to) MCP server API endpoints.

Your MCP server will receive the already-authenticated user details as a parameter. You don’t need to perform any checks of your own, or directly manage tokens. You can still fully control how you authenticate users: from what UI they see when they log in, to which provider they use to log in. You can choose to bring your own third-party authentication and authorization providers like Google or GitHub, or integrate with your own.

The complete [MCP OAuth flow](https://spec.modelcontextprotocol.io/specification/draft/basic/authorization/) looks like this:

Here, your MCP server acts as both an OAuth client to your upstream service, _and_ as an OAuth server (also referred to as an OAuth “provider”) to MCP clients. You can use any upstream authentication flow you want, but workers-oauth-provider guarantees that your MCP server is [spec-compliant](https://spec.modelcontextprotocol.io/specification/draft/basic/authorization) and able to work with the full range of client apps & websites. This includes support for Dynamic Client Registration ([RFC 7591](https://datatracker.ietf.org/doc/html/rfc7591)) and Authorization Server Metadata ([RFC 8414](https://datatracker.ietf.org/doc/html/rfc8414)).

### A simple, pluggable interface for OAuth

When you build an MCP server with Cloudflare Workers, you provide an instance of the OAuth Provider paths to your authorization, token, and client registration endpoints, along with [handlers](https://developers.cloudflare.com/workers/runtime-apis/handlers/fetch/) for your MCP Server, and for auth:

```
import OAuthProvider from "@cloudflare/workers-oauth-provider";
import MyMCPServer from "./my-mcp-server";
import MyAuthHandler from "./auth-handler";

export default new OAuthProvider({
  apiRoute: "/sse", // MCP clients connect to your server at this route
  apiHandler: MyMCPServer.mount('/sse'), // Your MCP Server implmentation
  defaultHandler: MyAuthHandler, // Your authentication implementation
  authorizeEndpoint: "/authorize",
  tokenEndpoint: "/token",
  clientRegistrationEndpoint: "/register",
});
```

This abstraction lets you easily plug in your own authentication. Take a look at [this example](https://github.com/cloudflare/ai/blob/main/demos/remote-mcp-github-oauth/src/github-handler.ts) that uses GitHub as the identity provider for an MCP server, in less than 100 lines of code, by implementing /callback and /authorize routes.

### Why do MCP servers issue their own tokens?

You may have noticed in the authorization diagram above, and in the [authorization section](https://spec.modelcontextprotocol.io/specification/draft/basic/authorization) of the MCP spec, that the MCP server issues its own token to the MCP client.

Instead of passing the token it receives from the upstream provider directly to the MCP client, your Worker stores an encrypted access token in [Workers KV](https://developers.cloudflare.com/kv/). It then issues its own token to the client. As shown in the [GitHub example](https://github.com/cloudflare/ai/blob/main/demos/remote-mcp-github-oauth/src/github-handler.ts) above, this is handled on your behalf by the workers-oauth-provider — your code never directly handles writing this token, preventing mistakes. You can see this in the following code snippet from the [GitHub example](https://github.com/cloudflare/ai/blob/main/demos/remote-mcp-github-oauth/src/github-handler.ts) above:

```
// When you call completeAuthorization, the accessToken you pass to it
  // is encrypted and stored, and never exposed to the MCP client
  // A new, separate token is generated and provided to the client at the /token endpoint
  const { redirectTo } = await c.env.OAUTH_PROVIDER.completeAuthorization({
    request: oauthReqInfo,
    userId: login,
    metadata: { label: name },
    scope: oauthReqInfo.scope,
    props: {
      accessToken,  // Stored encrypted, never sent to MCP client
    },
  })

  return Response.redirect(redirectTo)
```

On the surface, this indirection might sound more complicated. Why does it work this way?

By issuing its own token, MCP Servers can restrict access and enforce more granular controls than the upstream provider. If a token you issue to an MCP client is compromised, the attacker only gets the limited permissions you've explicitly granted through your MCP tools, not the full access of the original token.

Let’s say your MCP server requests that the user authorize permission to read emails from their Gmail account, using the [gmail.readonly scope](https://developers.google.com/identity/protocols/oauth2/scopes#gmail). The tool that the MCP server exposes is more narrow, and allows reading travel booking notifications from a limited set of senders, to handle a question like “What’s the check-out time for my hotel room tomorrow?” You can enforce this constraint in your MCP server, and if the token you issue to the MCP client is compromised, because the token is to your MCP server — and not the raw token to the upstream provider (Google) — an attacker cannot use it to read arbitrary emails. They can only call the tools your MCP server provides. OWASP calls out [“Excessive Agency”](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/) as one of the top risk factors for building AI applications, and by issuing its own token to the client and enforcing constraints, your MCP server can limit tools access to only what the client needs.

Or building off the earlier GitHub example, you can enforce that only a specific user is allowed to access a particular tool. In the example below, only users that are part of an allowlist can see or call the generateImage tool, that uses [Workers AI](https://developers.cloudflare.com/workers-ai/) to generate an image based on a prompt:

```
import { McpAgent } from "agents/mcp";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";

const USER_ALLOWLIST = ["geelen"];

export class MyMCP extends McpAgent<Props, Env> {
  server = new McpServer({
    name: "Github OAuth Proxy Demo",
    version: "1.0.0",
  });

  async init() {
    // Dynamically add tools based on the user's identity
    if (USER_ALLOWLIST.has(this.props.login)) {
      this.server.tool(
        'generateImage',
        'Generate an image using the flux-1-schnell model.',
        {
          prompt: z.string().describe('A text description of the image you want to generate.')
        },
        async ({ prompt }) => {
          const response = await this.env.AI.run('@cf/black-forest-labs/flux-1-schnell', { 
            prompt, 
            steps: 8 
          })
          return {
            content: [{ type: 'image', data: response.image!, mimeType: 'image/jpeg' }],
          }
        }
      )
    }
  }
}
```

## Introducing McpAgent: remote transport support that works today, and will work with the revision to the MCP spec

The next step to opening up MCP beyond your local machine is to open up a remote transport layer for communication. MCP servers you run on your local machine just communicate over [stdio](https://modelcontextprotocol.io/docs/concepts/transports#standard-input%2Foutput-stdio), but for an MCP server to be callable over the Internet, it must implement [remote transport](https://spec.modelcontextprotocol.io/specification/draft/basic/transports/#http-with-sse).

The [McpAgent](https://github.com/cloudflare/agents/blob/2f82f51784f4e27292249747b5fbeeef94305552/packages/agents/src/mcp.ts) class we introduced today as part of our [Agents SDK](https://github.com/cloudflare/agents) handles this for you, using [Durable Objects](https://developers.cloudflare.com/durable-objects/) behind the scenes to hold a persistent connection open, so that the MCP client can send [server-sent events (SSE)](https://modelcontextprotocol.io/docs/concepts/transports#server-sent-events-sse) to your MCP server. You don’t have to write code to deal with transport or serialization yourself. A minimal MCP server in 15 lines of code can look like this:

```
import { McpAgent } from "agents/mcp";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";

export class MyMCP extends McpAgent {
  server = new McpServer({
    name: "Demo",
    version: "1.0.0",
  });
  async init() {
    this.server.tool("add", { a: z.number(), b: z.number() }, async ({ a, b }) => ({
      content: [{ type: "text", text: String(a + b) }],
    }));
  }
}
```

After much [discussion](https://github.com/modelcontextprotocol/specification/discussions/102), remote transport in the MCP spec is changing, with [Streamable HTTP replacing HTTP+SSE](https://github.com/modelcontextprotocol/specification/pull/206) This allows for stateless, pure HTTP connections to MCP servers, with an option to upgrade to SSE, and removes the need for the MCP client to send messages to a separate endpoint than the one it first connects to. The McpAgent class will change with it and just work with streamable HTTP, so that you don’t have to start over to support the revision to how transport works.

This applies to future iterations of transport as well. Today, the vast majority of MCP servers only expose tools, which are simple [remote procedure call (RPC)](https://en.wikipedia.org/wiki/Remote_procedure_call) methods that can be provided by a stateless transport. But more complex human-in-the-loop and agent-to-agent interactions will need [prompts](https://modelcontextprotocol.io/docs/concepts/prompts) and [sampling](https://modelcontextprotocol.io/docs/concepts/sampling). We expect these types of chatty, two-way interactions will need to be real-time, which will be challenging to do well without a bidirectional transport layer. When that time comes, Cloudflare, the [Agents SDK](https://developers.cloudflare.com/agents/), and Durable Objects all natively support [WebSockets](https://developers.cloudflare.com/durable-objects/best-practices/websockets/), which enable full-duplex, bidirectional real-time communication.

## Stateful, agentic MCP servers

When you build MCP servers on Cloudflare, each MCP client session is backed by a Durable Object, via the [Agents SDK](https://developers.cloudflare.com/agents/). This means each session can manage and persist its own state, [backed by its own SQL database](https://developers.cloudflare.com/agents/api-reference/store-and-sync-state/).

This opens the door to building stateful MCP servers. Rather than just acting as a stateless layer between a client app and an external API, MCP servers on Cloudflare can themselves be stateful applications —games, a shopping cart plus checkout flow, a [persistent knowledge graph](https://github.com/modelcontextprotocol/servers/tree/main/src/memory), or anything else you can dream up. When you build on Cloudflare, MCP servers can be much more than a layer in front of your REST API.

To understand the basics of how this works, let’s look at a minimal example that increments a counter:

```
import { McpAgent } from "agents/mcp";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";

type State = { counter: number }

export class MyMCP extends McpAgent<Env, State, {}> {
  server = new McpServer({
    name: "Demo",
    version: "1.0.0",
  });

  initialState: State = {
    counter: 1,
  }

  async init() {
    this.server.resource(`counter`, `mcp://resource/counter`, (uri) => {
      return {
        contents: [{ uri: uri.href, text: String(this.state.counter) }],
      }
    })

    this.server.tool('add', 'Add to the counter, stored in the MCP', { a: z.number() }, async ({ a }) => {
      this.setState({ ...this.state, counter: this.state.counter + a })

      return {
        content: [{ type: 'text', text: String(`Added ${a}, total is now ${this.state.counter}`) }],
      }
    })
  }

  onStateUpdate(state: State) {
    console.log({ stateUpdate: state })
  }

}
```

For a given session, the MCP server above will remember the state of the counter across tool calls.

From within an MCP server, you can use Cloudflare’s whole developer platform, and have your MCP server [spin up its own web browser](https://developers.cloudflare.com/agents/api-reference/browse-the-web/), [trigger a Workflow](https://developers.cloudflare.com/agents/api-reference/run-workflows/), [call AI models](https://developers.cloudflare.com/agents/api-reference/using-ai-models/), and more. We’re excited to see the MCP ecosystem evolve into more advanced use cases.

## Connect to remote MCP servers from MCP clients that today only support local MCP

Cloudflare is supporting remote MCP early — before the most prominent MCP client applications support remote, authenticated MCP, and before other platforms support remote MCP. We’re doing this to give you a head start building for where MCP is headed.

But if you build a remote MCP server today, this presents a challenge — how can people start using your MCP server if there aren’t MCP clients that support remote MCP?

We have two new tools that allow you to test your remote MCP server and simulate how users will interact with it in the future:

We updated the [Workers AI Playground](https://playground.ai.cloudflare.com/) to be a fully remote MCP client that allows you to connect to any remote MCP server with built-in authentication support. This online chat interface lets you immediately test your remote MCP servers without having to install anything on your device. Instead, just enter the remote MCP server’s URL (e.g. https://remote-server.example.com/sse) and click Connect.

Once you click Connect, you’ll go through the authentication flow (if you set one up) and after, you will be able to interact with the MCP server tools directly from the chat interface.

If you prefer to use a client like Claude Desktop or Cursor that already supports MCP but doesn’t yet handle remote connections with authentication, you can use [mcp-remote](https://www.npmjs.com/package/mcp-remote). mcp-remote is an adapter that lets MCP clients that otherwise only support local connections to work with remote MCP servers. This gives you and your users the ability to preview what interactions with your remote MCP server will be like from the tools you’re already using today, without having to wait for the client to support remote MCP natively.

We’ve [published a guide](https://developers.cloudflare.com/agents/guides/test-remote-mcp-server/) on how to use mcp-remote with popular MCP clients including Claude Desktop, Cursor, and Windsurf. In Claude Desktop, you add the following to your configuration file:

```
{
  "mcpServers": {
    "remote-example": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://remote-server.example.com/sse"
      ]
    }
  }
}
```

Remote Model Context Protocol (MCP) is coming! When client apps support remote MCP servers, the audience of people who can use them opens up from just us, developers, to the rest of the population — who may never even know what MCP is or stands for.

Building a remote MCP server is the way to bring your service into the AI assistants and tools that millions of people use. We’re excited to see many of the biggest companies on the Internet are busy building MCP servers right now, and we are curious about the businesses that pop-up in an agent-first, MCP-native way.

On Cloudflare, [you can start building today](https://developers.cloudflare.com/agents/guides/remote-mcp-server/). We’re ready for you, and ready to help build with you. Email us at [1800-mcp@cloudflare.com](https://blog.cloudflare.com/remote-model-context-protocol-servers-mcp/#), and we’ll help get you going. There’s lots more to come with MCP, and we’re excited to see what you build.

[AI](https://blog.cloudflare.com/tag/ai/)[Developers](https://blog.cloudflare.com/tag/developers/)[MCP](https://blog.cloudflare.com/tag/mcp/)[Agents](https://blog.cloudflare.com/tag/agents/)
