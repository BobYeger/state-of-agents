Title: Windsurf - Cascade

URL Source: https://docs.windsurf.com/windsurf/cascade/cascade

Published Time: Sun, 17 May 2026 18:05:57 GMT

Markdown Content:
> ## Documentation Index
> 
> 
> Fetch the complete documentation index at: [https://docs.windsurf.com/llms.txt](https://docs.windsurf.com/llms.txt)
> 
> 
> Use this file to discover all available pages before exploring further.

Windsurf’s Cascade unlocks a new level of collaboration between human and AI.To open Cascade, press `Cmd/Ctrl+L`click the Cascade icon in the top right corner of the Windsurf window. Any selected text in the editor or terminal will automatically be included.

### Quick links to features

## Model selection

Select your desired model from the selection menu below the Cascade conversation input box. Click below too see the full list of the available models and their availability across different plans and pricing.

## Cascade Code / Cascade Chat

Cascade comes in two primary modes: **Code** and **Chat**.Code mode allows Cascade to create and make modifications to your codebase, while Chat mode is optimized for questions around your codebase or general coding principles.While in Chat mode, Cascade may propose new code to you that you can accept and insert.

## Plans and Todo Lists

Cascade has built-in planning capabilities that help improve performance for longer tasks.In the background, a specialized planning agent continuously refines the long-term plan while your selected model focuses on taking short-term actions based on that plan.Cascade will create a Todo list within the conversation to track progress on complex tasks. To make changes to the plan, simply ask Cascade to make updates to the Todo list.Cascade may also automatically make updates to the plan as it picks up new information, such as a [Memory](https://docs.windsurf.com/windsurf/cascade/memories), during the course of a conversation.

## Queued Messages

While you are waiting for Cascade to finish its current task, you can queue up new messages to execute in order once the task is complete.To add a message to the queue, simply type in your message while Cascade is working and press `Enter`.

*   **Send immediately**: Press Enter again on an empty text box to send it right away.
*   **Delete**: Remove any message from the queue before it’s sent

## Tool Calling

Cascade has a variety of tools at its disposal, such as Search, Analyze, [Web Search](https://docs.windsurf.com/windsurf/cascade/web-search), [MCP](https://docs.windsurf.com/windsurf/cascade/mcp), and the [terminal](https://docs.windsurf.com/windsurf/terminal).It can detect which packages and tools that you’re using, which ones need to be installed, and even install them for you. Just ask Cascade how to run your project and press Accept.

You can configure an `Auto-Continue` setting to have Cascade automatically continue its response if it hits a limit. These will consume a prompt credit(s) corresponding to the model you are using.

## Voice input

Use Voice input to use your voice to interact with Cascade. In its current form it can transcribe your speech to text.

[Video 12](https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/voice-mode.mp4?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=b6881ef11385d4f05fa151e0808a9e78)
## Named Checkpoints and Reverts

You have the ability to revert changes that Cascade has made. Simply hover your mouse over the original prompt and click on the revert arrow on the right, or revert directly from the table of contents. This will revert all code changes back to the state of your codebase at the desired step.

[Video 13](https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/cascade-revert.mp4?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=fe494383062acfc1efe07b23c03607a2)
You can also create a named snapshot/checkpoint of the current state of your project from within the conversation, which you can easily navigate to and revert at any time.

[Video 14](https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/namedcheckpoints.mp4?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=d3c50b95ea5c2e67c2f08f00af4d11f6)
## Real-time awareness

A unique capability of Windsurf and Cascade is that it is aware of your real-time actions, removing the need to prompt with context on your prior actions.Simply instruct Cascade to “Continue”.

[Video 15](https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/windsurf-continue.mp4?fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=72fa8688e966ff308daa5876e6dc7f98)
## Send problems to Cascade

When you have problems in your code which show up in the Problems panel at the bottom of the editor, simply click the `Send to Cascade` button to bring them into the Cascade panel as an @ mention.

## Explain and fix

For any errors that you run into from within the editor, you can simply highlight the error and click `Explain and Fix` to have Cascade fix it for you.

## Ignoring files

If you’d like Cascade to ignore files, you can add your files to `.codeiumignore` at the root of your workspace. This will prevent Cascade from viewing, editing or creating files inside of the paths designated. You can declare the file paths in a format similar to `.gitignore`.

## Global .codeiumignore

For enterprise customers managing multiple repositories, you can enforce ignore rules across all repositories by placing a global `.codeiumignore` file in the `~/.codeium/` folder. This global configuration will apply to all Windsurf workspaces on your system and works in addition to any repository-specific `.codeiumignore` files.

## Linter integration

Cascade can automatically fix linting errors on generated code. This is turned on by default, but it can be disabled by clicking `Auto-fix` on the tool call, and clicking `disable`. This edit will not consume any credits.

When Cascade makes an edit with the primary goal of fixing lints that it created and auto-detected, it may discount the edit to be free of credit charge. This is in recognition of the fact that fixing lint errors increases the number of tool calls that Cascade makes.

## Sharing your conversation

You can share your Cascade trajectories with your team by clicking the `...` Additional options button in the top right of the Cascade panel, and clicking `Share Conversation`.

## @-mention previous conversations

You can also reference previous conversations with other conversations via an `@-mention`.When you do this, Cascade will retrieve the most relevant and useful information like the conversation summaries and checkpoints, and specific parts of the conversation that you query for. It typically will not retrieve the full conversation as to not overwhelm the context window.

[Video 16](https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf/cascade/at-mention-convos.mp4?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=f580f0222fdf75ec42cb7a9470e6de02)
## Simultaneous Cascades

Users can have multiple Cascades running simultaneously. You can navigate between them using the dropdown menu in the top left of the Cascade panel.

If you expect two Cascades to edit similar files, you should consider using [worktrees](https://docs.windsurf.com/windsurf/cascade/worktrees) to keep them isolated.
