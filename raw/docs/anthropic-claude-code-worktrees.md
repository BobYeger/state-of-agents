A [git worktree](https://git-scm.com/docs/git-worktree) is a separate working directory with its own files and branch, sharing the same repository history and remote as your main checkout. Running each Claude Code session in its own worktree means edits in one session never touch files in another, so you can have Claude building a feature in one terminal while fixing a bug in a second.

This page covers worktree isolation in the CLI. Everything below assumes a git repository. For other version control systems, see [Non-git version control](#non-git-version-control). The [desktop app](https://code.claude.com/docs/en/desktop#work-in-parallel-with-sessions) creates a worktree for every new session automatically.

Worktrees are one of several ways to run Claude in parallel. They isolate file edits, while [subagents](https://code.claude.com/docs/en/sub-agents) and [agent teams](https://code.claude.com/docs/en/agent-teams) coordinate the work itself. See [Run agents in parallel](https://code.claude.com/docs/en/agents) to compare the approaches, or skip ahead to [Isolate subagents with worktrees](#isolate-subagents-with-worktrees) to use worktrees and subagents together.

## Start Claude in a worktree

Pass `--worktree` or `-w` to create an isolated worktree and start Claude in it. By default, the worktree is created under `.claude/worktrees/<value>/` at your repository root, on a new branch named `worktree-<value>`:

```shellscript
claude --worktree feature-auth
```

To put worktrees somewhere else, configure a [`WorktreeCreate` hook](#non-git-version-control). Run the command again with a different name in another terminal to start a second isolated session:

```shellscript
claude --worktree bugfix-123
```

If you omit the name, Claude generates one such as `bright-running-fox`:

```shellscript
claude --worktree
```

You can also ask Claude to “work in a worktree” during a session, and it will create one with the [`EnterWorktree`](https://code.claude.com/docs/en/tools-reference) tool.

Before using `--worktree` in a directory for the first time, accept the workspace trust dialog by running `claude` once in that directory. If trust has not yet been accepted, `--worktree` exits with an error and prompts you to run `claude` in the directory first, including when combined with `-p`.

Add `.claude/worktrees/` to your `.gitignore` so worktree contents don’t appear as untracked files in your main checkout.

### Choose the base branch

Worktrees branch from your repository’s default branch, `origin/HEAD`, so they start from a clean tree matching the remote. If no remote is configured or the fetch fails, the worktree falls back to your current local `HEAD`. To always branch from local `HEAD` instead, set `worktree.baseRef` to `"head"` in [settings](https://code.claude.com/docs/en/settings#worktree-settings). Setting `baseRef` to `"head"` makes new worktrees carry your unpushed commits and feature-branch state, which is useful when isolating subagents that need to operate on in-progress work. The setting accepts only `"fresh"` or `"head"`, not arbitrary git refs:

```json
{
  "worktree": {
    "baseRef": "head"
  }
}
```

To branch from a specific pull request, pass the PR number prefixed with `#`, or a full GitHub pull request URL. Claude Code fetches `pull/<number>/head` from `origin` and creates the worktree at `.claude/worktrees/pr-<number>`:

```shellscript
claude --worktree "#1234"
```

For full control over how worktrees are created, configure a [`WorktreeCreate` hook](https://code.claude.com/docs/en/hooks#worktreecreate), which replaces the default `git worktree` logic entirely.

## Copy gitignored files into worktrees

A worktree is a fresh checkout, so untracked files like `.env` or `.env.local` from your main repository are not present. To copy them automatically when Claude creates a worktree, add a `.worktreeinclude` file to your project root.

The file uses `.gitignore` syntax. Only files that match a pattern and are also gitignored are copied, so tracked files are never duplicated.

This `.worktreeinclude` copies two env files and a secrets config into each new worktree:

```text
.env
.env.local
config/secrets.json
```

This applies to worktrees created with `--worktree`, [subagent worktrees](#isolate-subagents-with-worktrees), and parallel sessions in the [desktop app](https://code.claude.com/docs/en/desktop#work-in-parallel-with-sessions).

## Isolate subagents with worktrees

Subagents can run in their own worktrees so parallel edits don’t conflict. Ask Claude to “use worktrees for your agents”, or set it permanently on a [custom subagent](https://code.claude.com/docs/en/sub-agents#supported-frontmatter-fields) by adding `isolation: worktree` to the frontmatter. Each subagent gets a temporary worktree that is removed automatically when the subagent finishes without changes.

Subagent worktrees use the same [base branch](#choose-the-base-branch) as `--worktree`, so they branch from your repository’s default branch unless `worktree.baseRef` is set to `"head"`.

## Clean up worktrees

When you exit a worktree session, cleanup depends on whether you made changes:

- **No uncommitted changes, no untracked files, and no new commits**: the worktree and its branch are removed automatically. If the session has a [name](https://code.claude.com/docs/en/sessions#name-your-sessions), Claude prompts instead so you can keep the worktree for later
- **Uncommitted changes, untracked files, or new commits exist**: Claude prompts you to keep or remove the worktree. Keeping preserves the directory and branch so you can return later. Removing deletes the worktree directory and its branch, discarding any uncommitted changes, untracked files, and commits
- **Non-interactive runs**: worktrees created with `--worktree` alongside `-p` are not cleaned up automatically since there is no exit prompt. Remove them with `git worktree remove`

Subagent worktrees orphaned by a crash or interrupted run are removed at startup once they are older than your [`cleanupPeriodDays`](https://code.claude.com/docs/en/settings#available-settings) setting, provided they have no uncommitted changes, no untracked files, and no unpushed commits. Worktrees you create with `--worktree` are never removed by this sweep.

## Manage worktrees manually

For full control over worktree location and branch configuration, create worktrees with Git directly. This is useful when you need to check out a specific existing branch or place the worktree outside the repository.

Create a worktree on a new branch:

```shellscript
git worktree add ../project-feature-a -b feature-a
```

Create a worktree from an existing branch:

```shellscript
git worktree add ../project-bugfix bugfix-123
```

Start Claude in the worktree:

```shellscript
cd ../project-feature-a && claude
```

List your worktrees:

```shellscript
git worktree list
```

Remove one when you’re done with it:

```shellscript
git worktree remove ../project-feature-a
```

See the [Git worktree documentation](https://git-scm.com/docs/git-worktree) for the full command reference. Remember to initialize your development environment in each new worktree: install dependencies, set up virtual environments, or run whatever your project’s setup requires.

## Non-git version control

Worktree isolation uses git by default. For SVN, Perforce, Mercurial, or other systems, configure [`WorktreeCreate` and `WorktreeRemove` hooks](https://code.claude.com/docs/en/hooks#worktreecreate) to provide custom creation and cleanup logic. Because the hook replaces the default git behavior, [`.worktreeinclude`](#copy-gitignored-files-into-worktrees) is not processed when you use `--worktree`. Copy any local configuration files inside your hook script instead.

This `WorktreeCreate` hook reads the worktree name from stdin, checks out a fresh SVN working copy, and prints the directory path so Claude Code can use it as the session’s working directory:

```json
{
  "hooks": {
    "WorktreeCreate": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "bash -c 'NAME=$(jq -r .name); DIR=\"$HOME/.claude/worktrees/$NAME\"; svn checkout https://svn.example.com/repo/trunk \"$DIR\" >&2 && echo \"$DIR\"'"
          }
        ]
      }
    ]
  }
}
```

Pair it with a `WorktreeRemove` hook to clean up when the session ends. See the [hooks reference](https://code.claude.com/docs/en/hooks#worktreecreate) for the input schema and a removal example.

## See also

Worktrees handle file isolation. The related pages below cover delegating work into those isolated checkouts and switching between the sessions you create:

- [Subagents](https://code.claude.com/docs/en/sub-agents): delegate work to isolated agents within a session
- [Agent teams](https://code.claude.com/docs/en/agent-teams): coordinate multiple Claude sessions automatically
- [Manage sessions](https://code.claude.com/docs/en/sessions): name, resume, and switch between conversations
- [Desktop parallel sessions](https://code.claude.com/docs/en/desktop#work-in-parallel-with-sessions): worktree-backed sessions in the desktop app