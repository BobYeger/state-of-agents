---
title: "Git Worktrees for Agents: Evolution and Vendor Approaches"
aliases:
  - "Worktrees for Parallel Agents"
  - "Worktree vs VM Isolation"
source_type: "synthesis"
kind: "vendor-comparison"
status: "verified"
year: 2026
publication_date: "2026-06-23"
publication_date_basis: "vault_synthesis_compiled_date"
source_updated_date: null
source_updated_date_basis: null
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Matan (vault synthesis)"
venue: "State of Agents vault"
url: "https://git-scm.com/docs/git-worktree"
pdf_url: ""
artifacts: []
created: 2026-06-23
updated: 2026-06-23
---

# Git Worktrees for Agents: Evolution and Vendor Approaches

## Summary

- Synthesis note tracing how git worktrees became an agentic-parallelism primitive, and comparing how Claude Code, OpenAI Codex, and Devin isolate parallel agents.
- A git worktree is a separate working directory with its own files and branch that shares one repository's history, refs, and `.git` object database; the same branch cannot normally be checked out in two worktrees at once. This is git-level (file/branch) isolation, not a security or runtime sandbox.
- Evolution arc: manual developer worktrees (context-switch without stashing) -> agent-managed parallel worktrees (Claude Code, Codex) -> full VM / dev-environment isolation per agent (Devin "managed Devins").
- Key per-vendor split: Claude Code and Codex run parallel agents in worktrees on the user's local machine; Devin runs each managed agent in its own isolated cloud VM with its own shell, browser, and dev environment.

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
- [[claims/Claim - Agent teams need explicit organization]]
- [[concepts/subagent context isolation]]
- [[concepts/agent teams]]

## Connections

- [[operations/worktree isolation]]
- [[operations/sandboxes]]
- [[operations/agent harnesses]]
- [[sources/Anthropic Claude Code Worktrees]]
- [[sources/OpenAI Codex App Worktrees]]
- [[sources/Devin Manages Devins]]
- [[sources/Nate Ross Claude Code Worktrees]]
- [[systems/Claude Code]]
- [[systems/Codex]]
- [[concepts/issue tracker control plane]]

## Notes

### What a git worktree is (the primitive)

- The official git docs describe `git worktree` as letting "you to check out more than one branch at a time," with each worktree a linked working directory that references back to the main worktree's `.git` directory. Shared: object database and refs (via `$GIT_COMMON_DIR`); per-worktree: working files, index, and `HEAD` (via `$GIT_DIR`).
- The canonical motivating example in the git docs is the human context-switch: you are mid-refactor, an emergency fix lands, so you "create a temporary linked worktree to make the emergency fix, remove it when done, and then resume your earlier refactoring session" — i.e. no stashing or extra clone.
- Worktrees differ from clones: clones are fully separate copies; worktrees share history, objects, and refs, so creation is near-instant and disk usage is minimal. Commits in one worktree are visible to the others.
- Canonical URL: https://git-scm.com/docs/git-worktree

### Why this suits parallel agents

- Each agent gets its own working directory and git index while sharing a single object store, which prevents file-level edit collisions, branch checkout contention, and cross-task context contamination on the same repo.
- Decomposition guidance from practitioner write-ups: split parallel work along domain/feature boundaries; avoid tasks that touch the same files from different directions.

### Claude Code (worktrees, local)

- Official docs: "A git worktree is a separate working directory with its own files and branch, sharing the same repository history and remote as your main checkout." Running each session in its own worktree means "edits in one session never touch files in another."
- Entry points: `claude --worktree <name>` (or `-w`) creates a worktree under `.claude/worktrees/<value>/` on a new branch `worktree-<value>`; omitting the name auto-generates one (e.g. `bright-running-fox`). Mid-session, asking Claude to "work in a worktree" invokes the `EnterWorktree` tool.
- Base branch: worktrees branch from `origin/HEAD` (clean tree matching remote) by default; `worktree.baseRef: "head"` branches from local `HEAD` to carry unpushed/in-progress work. `--worktree "#1234"` branches from a PR.
- Subagent isolation: set `isolation: worktree` in a custom subagent's frontmatter (or ask "use worktrees for your agents"); each subagent gets a temporary worktree removed automatically when it finishes without changes.
- Secrets/env: a fresh checkout lacks untracked files like `.env`; a `.worktreeinclude` file (`.gitignore` syntax) copies matched-and-gitignored files into each new worktree. Only gitignored matches are copied, so tracked files are never duplicated.
- Coordination: worktrees handle file isolation only; subagents and agent teams "coordinate the work itself." The docs are explicit that worktrees "isolate file edits, while subagents and agent teams coordinate the work."
- Lifecycle: clean exits with no changes auto-remove the worktree and branch; dirty exits prompt to keep or remove. Subagent/background worktrees are swept once older than `cleanupPeriodDays` (if clean); `--worktree` worktrees are never auto-swept. Running agents `git worktree lock` their worktree against concurrent cleanup.
- Scale guidance (practitioner consensus, e.g. Anthropic/community): run roughly 2-4 parallel sessions; ~5+ on a large codebase hits API rate limits and makes review hard.
- Non-git VCS: `WorktreeCreate`/`WorktreeRemove` hooks replace default git behavior (SVN, Perforce, Mercurial). When a hook is used, `.worktreeinclude` is not processed.
- Source: https://code.claude.com/docs/en/worktrees

### OpenAI Codex app/CLI (worktrees, local)

- Official Codex app docs: worktrees let Codex "run multiple independent tasks in the same project without interfering with each other," each worktree keeping its own file copies while sharing the same `.git` metadata.
- Use it "when you want to try a new idea without touching your current work, or when you want Codex to run independent tasks side by side." Automations "run on dedicated background worktrees so they don't conflict with your ongoing work."
- Mechanics: select "Worktree" when creating a thread, pick a base branch, submit. Codex creates worktrees in `$CODEX_HOME/worktrees` in detached-HEAD state. A "Handoff" feature moves a thread between Local and Worktree environments, handling the git operations.
- Branch constraint mirrors git: "Git only allows a branch to be checked out in one place at a time," so checking out an existing worktree branch locally errors.
- Secrets/env: Codex also supports a root `.worktreeinclude` to copy ignored files (e.g. `.env`, config) into new managed worktrees — convergent design with Claude Code.
- Lifecycle: by default Codex keeps ~15 recent Codex-managed worktrees, auto-deleting older ones after "saving a snapshot of the work."
- The Codex docs make no claim of security isolation between worktrees.
- Source: https://developers.openai.com/codex/app/worktrees

### Devin "managed Devins" (isolated VMs, cloud)

- Cognition's launch post: each managed Devin runs in "its own isolated virtual machine with its own terminal, browser, and development environment." Each "can independently run shell commands, execute tests, and verify its own changes before reporting back."
- This is a different isolation level than worktrees: full machine/dev-environment isolation per agent rather than shared-repo working trees on one host.
- Coordination (control plane): the main Devin "scopes the work, assigns each piece to a managed Devin, monitors progress, resolves any conflicts, and compiles the results." Devin docs list coordinator primitives: spin up managed Devins, message child sessions, monitor ACU consumption, sleep/terminate children, and schedule self-reminders for long-running sessions.
- Rationale: avoids the single-session failure mode where "context accumulates, focus degrades, and the quality of each subtask suffers"; each managed Devin "gets a clean slate, a narrow focus, its own shell, and its own test runner. And they all run in parallel."
- Secrets/env in Devin's VM model: Devin starts each session from a Machine Snapshot capturing installed software, cloned repos, auth tokens, and on-disk files; secrets (API keys, DB URLs, OAuth tokens) live in a built-in Secrets vault scoped to Devin's cloud workspaces rather than checked into git. Environment is per-VM, not per-worktree.
- Sources: https://cognition.com/blog/devin-can-now-manage-devins ; https://docs.devin.ai/work-with-devin/advanced-capabilities ; https://docs.devin.ai/onboard-devin/repo-setup

### Per-vendor comparison

| Dimension | Claude Code | OpenAI Codex (app/CLI) | Devin (managed Devins) |
|---|---|---|---|
| Isolation level | Git worktree, local host | Git worktree, local host | Full isolated cloud VM per agent |
| What is isolated | Files, branch, index (shared `.git`) | Files, branch, index (shared `.git`) | Shell, browser, dev env, filesystem, processes |
| Secrets / env | `.worktreeinclude` copies gitignored `.env`/config into each worktree | `.worktreeinclude` copies ignored files into managed worktrees | Secrets vault + Machine Snapshot per VM |
| IDE / runtime access | User's local machine, terminal/desktop sessions | Codex desktop app threads, local | Each VM has own terminal + browser + editor |
| Coordination | Subagents / agent teams over worktrees | Threads + automations + Handoff | Main Devin scopes, assigns, monitors, resolves, compiles |
| Lifecycle | Auto-clean if no changes; `cleanupPeriodDays` sweep; locks while running | Keeps ~15 recent worktrees; snapshot before delete | Spin up / message / sleep / terminate child VMs |
| Same-host resource contention | Yes (shared ports/db/daemon) | Yes (shared ports/db/daemon) | No (separate VMs) |

### Cross-check with [[operations/worktree isolation]]

- The vault note states a worktree "is not a security sandbox" and is "a filesystem and Git isolation primitive." This is correct and corroborated by both the git model and independent practitioner sources: worktrees "isolate branches, not runtimes," sharing the same object database, ports, and Docker daemon unless you intervene. None of the three vendors' worktree docs claim security isolation between worktrees.
- The note's failure modes (gitignored `.env` not auto-present; ports/db/caches still collide; worktrees do not replace reviews/tests/permission gates) are confirmed: `.worktreeinclude` exists precisely because `.env` is absent, and same-host worktrees share ports/db/daemon. No corrections needed; this synthesis extends it with the cross-vendor isolation ladder.

### Candor / limits

- Vendor specifics here are fast-moving living docs. Claude Code and Codex worktree behaviors (flags, `.worktreeinclude`, cleanup counts) are grounded in current official docs but may shift between releases.
- Codex's exact retained-worktree count (~15) and Claude Code's 2-4 parallel-session guidance are point-in-time figures, not hard guarantees.
- Devin's docs confirm isolated VMs and coordinator primitives but are thinner on precise per-VM networking/secrets scoping; the secrets-vault and Machine-Snapshot details come from Devin onboarding docs rather than the managed-Devins launch post itself.
