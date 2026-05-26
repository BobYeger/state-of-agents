# Cursor 3.2: Multitask, Worktrees, and Multi-root Workspaces

Canonical URL: https://cursor.com/changelog/04-24-26

3.2 Apr 24, 2026 · Changelog

# Multitask, Worktrees, and Multi-root Workspaces

This release introduces a new way to multitask with async subagents, an improved worktrees experience, and multi-root workspaces for making cross-repo changes.

## # Multitask in Agents Window

With /multitask , Cursor will run async subagents to parallelize your requests instead of adding them to the queue. It will also break down larger tasks into smaller chunks for a fleet of async subagents to tackle simultaneously.

If you already have messages in the queue, you can ask Cursor to multitask on them instead of waiting for the current run to finish.

## # Worktrees in Agents Window

We've added new and improved worktrees in the Agents Window .

Run isolated tasks in the background across different branches. When you're ready to test changes, move any branch into your local foreground with one click.

## # Multi-root workspaces in Agents Window

A single agent session can now target a reusable workspace made of multiple folders.

This allows Cursor to make cross-repo changes spanning frontend, backend, and shared libraries, without retargeting the agent every time it moves between repos.
