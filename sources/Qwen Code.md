---
title: "Qwen Code"
aliases:
  - "Qwen Code CLI"
  - "Qwen-Code"
source_type: "repository"
kind: "agent-harness-repository"
status: "verified"
year: 2025
publication_date: "2025-06-26"
publication_date_basis: "github_repository_created_at"
source_updated_date: "2026-08-19"
source_updated_date_basis: "pinned_commit_author_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Qwen Team"
venue: "GitHub"
url: "https://github.com/QwenLM/qwen-code"
pdf_url: ""
license: "Apache-2.0"
license_url: "https://github.com/QwenLM/qwen-code/blob/8b2593d79b8c56d5248d2d89764b4f974ae5c354/LICENSE"
evidence_class: "open-source-implementation-and-maintainer-documentation"
metrics_status: "implementation-evidence-only"
artifacts: []
created: 2026-08-19
updated: 2026-08-19
---

# Qwen Code

## Summary

- Qwen Code is an executable TypeScript coding-agent harness, not the separate [[sources/Qwen-Agent Repository|Qwen-Agent]] framework. Interactive and headless CLI surfaces construct a UI-independent runtime in `packages/core`; ACP bridges, SDKs, IDE integrations, and other clients reuse that core.
- The core owns prompt and context construction, provider calls, tool registration and execution, permission policy, sessions, memory, and telemetry. Its loop sends the prompt, history, and tool schemas to a configured provider; validates and mediates requested calls; executes tools; returns observations; and continues until the model produces a final result.
- Built-in tools cover filesystem edits, shell commands, search, planning, web access, memory, skills, and subagents, while MCP adds external tools, prompts, and resources. The provider layer supports Qwen as well as OpenAI-, Anthropic-, and Gemini-compatible APIs and local backends.
- Official lineage is specific: the project was originally based on Google Gemini CLI v0.8.2, then stopped syncing with that upstream starting with Qwen Code v0.1 and developed independently. It should therefore be described as a derived lineage, not as a currently synchronized Gemini CLI fork.

## Harness Profile

- **State and context:** direct sessions persist history and metadata when chat recording is enabled; the CLI supports resume, branch, export, compaction, per-turn diffs, and file restoration from checkpoints. Hierarchical `QWEN.md`, compatible `AGENTS.md`, local transcripts, and runtime state are distinct surfaces rather than one undifferentiated memory system.
- **Control and isolation:** plan, ask-permissions, auto-edit, classifier-driven auto, and YOLO modes mediate tools. Sandboxing is opt-in and disabled by default, using macOS Seatbelt or Docker/Podman; YOLO auto-approval does not enable a sandbox. Extension packages can include executable MCP servers, hooks, skills, and agents and therefore inherit substantial host authority.
- **Multi-agent:** the shipped `agent` tool supports named subagents with fresh contexts and fork subagents with inherited history, foreground or background execution, parallel calls, progress events, continuation, and caller-selected tool restrictions. The docs explicitly say fork tool lists are not administrator-enforced sandboxes. Collaborative Agent Team adds shared tasks, messages, and an optional worktree writer, but remains experimental and flag-gated.
- **Memory and skills:** user-authored `QWEN.md` instructions and stable Agent Skills are shipped. Managed auto-memory writes inspectable Markdown across sessions and is documented as on by default; git-shared team memory and automatic sync are opt-in and carry ordinary repository and secret-handling risks.
- **Observability:** opt-in OpenTelemetry export is documented as off by default and covers interaction, provider request, tool, approval wait, hook, subagent, session, and daemon signals. Local transcripts, `/stats`, structured headless streams, checkpoints, and diffs provide additional audit surfaces but have different retention and privacy properties.

## Shipped versus Experimental

The direct CLI and headless loop, built-in and MCP tools, permission modes, opt-in sandbox, persisted sessions, compaction, checkpoints, subagents, memory, skills, hooks, and OpenTelemetry instrumentation are documented as shipped. Agent Team coordination and `qwen serve` daemon mode are explicitly experimental; LSP and session-workflow surfaces are also feature-gated. Files under `docs/design/` and `docs/plans/` are design evidence, not proof that the described work has shipped.

## Evidence Boundary

This card audits repository commit `8b2593d79b8c56d5248d2d89764b4f974ae5c354`, dated August 19, 2026. The implementation and official documentation establish a broad current harness surface, but the README's product-comparison table and feature-parity claims are maintainer claims, not an independent evaluation. No model benchmark is treated as evidence for harness quality here.

Persisted transcripts and file checkpoints enable resumption and rollback of recorded edits; they do not make arbitrary shell, network, or external-service effects transactional. Auto-memory behavior is documented implementation, not evidence of improved outcomes. Experimental Agent Team should not be represented as the default multi-agent control plane, and caller-chosen subagent restrictions should not be upgraded into a security boundary.

## Connections

- [[sources/Qwen-Agent Repository]]
- [[maps/Harness Tracker]]
- [[operations/agent harnesses]]
- [[systems/china agent ecosystem]]
- [[operations/agent memory]]
- [[operations/sandboxes]]
- [[concepts/agent skills]]
- [[protocols/MCP]]
- [[protocols/ACP]]

## Notes

- Canonical repository: https://github.com/QwenLM/qwen-code
- Audited snapshot: https://github.com/QwenLM/qwen-code/tree/8b2593d79b8c56d5248d2d89764b4f974ae5c354
- Gemini CLI lineage statement: https://github.com/QwenLM/qwen-code/blob/8b2593d79b8c56d5248d2d89764b4f974ae5c354/README.md#acknowledgments
- Architecture and runtime boundaries: https://github.com/QwenLM/qwen-code/blob/8b2593d79b8c56d5248d2d89764b4f974ae5c354/docs/developers/architecture.md
- Tool loop: https://github.com/QwenLM/qwen-code/blob/8b2593d79b8c56d5248d2d89764b4f974ae5c354/docs/developers/tools/introduction.md
- Sessions, commands, and checkpoints: https://github.com/QwenLM/qwen-code/blob/8b2593d79b8c56d5248d2d89764b4f974ae5c354/docs/users/features/commands.md
- Approval modes: https://github.com/QwenLM/qwen-code/blob/8b2593d79b8c56d5248d2d89764b4f974ae5c354/docs/users/features/approval-mode.md
- Sandbox: https://github.com/QwenLM/qwen-code/blob/8b2593d79b8c56d5248d2d89764b4f974ae5c354/docs/users/features/sandbox.md
- Subagents: https://github.com/QwenLM/qwen-code/blob/8b2593d79b8c56d5248d2d89764b4f974ae5c354/docs/users/features/sub-agents.md
- Experimental Agent Team: https://github.com/QwenLM/qwen-code/blob/8b2593d79b8c56d5248d2d89764b4f974ae5c354/docs/users/features/multi-agent-coordination.md
- Memory: https://github.com/QwenLM/qwen-code/blob/8b2593d79b8c56d5248d2d89764b4f974ae5c354/docs/users/features/memory.md
- Skills: https://github.com/QwenLM/qwen-code/blob/8b2593d79b8c56d5248d2d89764b4f974ae5c354/docs/users/features/skills.md
- OpenTelemetry: https://github.com/QwenLM/qwen-code/blob/8b2593d79b8c56d5248d2d89764b4f974ae5c354/docs/developers/development/telemetry.md
- No repository content was copied into the vault.
