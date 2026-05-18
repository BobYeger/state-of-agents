Title: Memory

URL Source: https://docs.letta.com/letta-code/memory/

Markdown Content:
With Letta Code, you use the same agent indefinitely - across sessions, days, or months - and have it get better over time. Your agent remembers past interactions, learns your preferences, and self-edits its memory as it works.

Letta Code also allows you to customize your agent’s personality. With Claude Code or Codex, every user gets the same agent that acts identically. With Letta Code, you can deeply personalize your agents to be unique to _you_.

## Agents and conversations

[Section titled “Agents and conversations”](https://docs.letta.com/letta-code/memory/#agents-and-conversations)

In Letta Code, there are two important session concepts: **agents** and **conversations**.

*   An **agent** is an entity with a name, memories, a model configuration, messages, and other state.
*   A **conversation** is a message thread (or “session”) with an agent. You can have many parallel conversations with a single agent. Every agent also has a “default conversation” or “main chat”.

When you run the `letta` CLI command in a project directory, Letta Code resumes the default conversation with your last used agent. In the Letta Code desktop app, the left sidebar is sorted by agents, and you can see conversations sorted by activity date.

If you want to run many CLI sessions with a single agent in parallel (eg in separate terminal windows), use `letta --new` to start a new conversation. In the desktop app, simply press the notepad icon to start a new conversation.

Letta Code has a default agent pre-installed (called “Letta Code”). To swap agents in the CLI, use `/agents`. You can favorite an agent in the CLI with “/pin”, or by clicking the favorites button in the desktop app.

## Initializing your agent’s memory

[Section titled “Initializing your agent’s memory”](https://docs.letta.com/letta-code/memory/#initializing-your-agents-memory)

When you run `/init`, Letta Code performs an interactive initialization in the main conversation, guided by context constitution principles for durable identity, preferences, and project structure. Letta Code will read from prior Claude Code and OpenAI Codex sessions to learn about your working style and past + ongoing projects using [subagents](https://docs.letta.com/letta-code/subagents).

Run `/init` again whenever you want the agent to re-analyze your project, such as after major changes or adding documentation that you want the agent to ingest.

If your memory structure has drifted or become messy over time, run `/doctor` to audit the current memory layout and refine it for proper memory placement and efficient token usage.

## Manually triggering memory updates

[Section titled “Manually triggering memory updates”](https://docs.letta.com/letta-code/memory/#manually-triggering-memory-updates)

Your Letta Code agent can self-edit its own memory, and will use the context of the conversation to decide when to edit its memory (for example, to store new information learned in a session). In some cases, you may want to actively direct your agent to remember something via the `/remember` command.

For example, if you noticed your agent made an easily avoidable mistake, you can give direct guidance:

`> /remember not to make that mistake again`

You can also use the `/remember` command without any extra prompting, and the agent will infer your intent from the context to make a memory edit.

## Configuring dreaming (reflection)

[Section titled “Configuring dreaming (reflection)”](https://docs.letta.com/letta-code/memory/#configuring-dreaming-reflection)

To improve proactive memory creation and consolidation, Letta Code launches periodic sleep-time (dream) subagents to reflect on your recent conversations and interactions. These agents are launched in the background, and generally run for many steps since the subagents are thorough memory editors.

You can use the `/sleeptime` command in the CLI to configure your reflection settings, or by clicking the sleeping alien icon in the bottom-right of the app.

The **trigger** determines how often the reflection subagent is auto-launched:

*   `Off`: select to disable reflection subagents
*   `Step count`: launch a reflection subagent every N user messages
*   `Compaction event` (recommended, MemFS only): launch a reflection subagent when the context window is compacted / summarized

When a dream trigger fires, Letta Code launches the dream subagent in the background automatically.

## How Letta Code’s memory system works

[Section titled “How Letta Code’s memory system works”](https://docs.letta.com/letta-code/memory/#how-letta-codes-memory-system-works)

Your agent’s memory is stored in a git-backed filesystem called **MemFS** (short for “memory filesystem”), also known as a [context repository](https://www.letta.com/blog/context-repositories). Memory is organized as a directory of markdown files, cloned locally to `~/.letta/agents/<your-agent-id>/memory`. Your agent edits these files directly using its bash tools, then commits and pushes to save changes — giving you a full version history of everything your agent has learned.

Files in the `system/` directory are always loaded in full into the agent’s system prompt. Files outside `system/` are visible to the agent via the memory tree (filenames and descriptions), but their contents are not automatically loaded — keeping the context window lean.

For a full explanation of the MemFS file format, the `system/` hierarchy, git synchronization, and the `letta memory` CLI subcommands, see the [MemFS reference](https://docs.letta.com/letta-code/memfs).
