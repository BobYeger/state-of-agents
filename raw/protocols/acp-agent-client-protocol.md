Title: Introduction - Agent Client Protocol

URL Source: https://agentclientprotocol.com/

Published Time: Mon, 18 May 2026 04:44:31 GMT

Markdown Content:
> ## Documentation Index
> 
> 
> Fetch the complete documentation index at: [https://agentclientprotocol.com/llms.txt](https://agentclientprotocol.com/llms.txt)
> 
> 
> Use this file to discover all available pages before exploring further.

The Agent Client Protocol (ACP) standardizes communication between code editors/IDEs and coding agents and is suitable for both local and remote scenarios.

## Why ACP?

AI coding agents and editors are tightly coupled but interoperability isn’t the default. Each editor must build custom integrations for every agent they want to support, and agents must implement editor-specific APIs to reach users. This creates several problems:

*   Integration overhead: Every new agent-editor combination requires custom work
*   Limited compatibility: Agents work with only a subset of available editors
*   Developer lock-in: Choosing an agent often means accepting their available interfaces

ACP solves this by providing a standardized protocol for agent-editor communication, similar to how the [Language Server Protocol (LSP)](https://microsoft.github.io/language-server-protocol/) standardized language server integration.Agents that implement ACP work with any compatible editor. Editors that support ACP gain access to the entire ecosystem of ACP-compatible agents. This decoupling allows both sides to innovate independently while giving developers the freedom to choose the best tools for their workflow.

## Overview

ACP assumes that the user is primarily in their editor, and wants to reach out and use agents to assist them with specific tasks.ACP is suitable for both local and remote scenarios:

*   **Local agents** run as sub-processes of the code editor, communicating via JSON-RPC over stdio.
*   **Remote agents** can be hosted in the cloud or on separate infrastructure, communicating over HTTP or WebSocket

The protocol re-uses the JSON representations used in MCP where possible, but includes custom types for useful agentic coding UX elements, like displaying diffs.The default format for user-readable text is Markdown, which allows enough flexibility to represent rich formatting without requiring that the code editor is capable of rendering HTML.
