---
title: "Goose Agent"
aliases:
  - "goose"
  - "Block Goose"
source_type: "repository"
kind: "agent-harness-repository"
status: "verified"
year: 2024
publication_date: "2024-08-23"
publication_date_basis: "github_repository_created_at"
source_updated_date: "2026-08-19"
source_updated_date_basis: "pinned_commit_author_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "goose maintainers"
venue: "GitHub"
url: "https://github.com/aaif-goose/goose"
pdf_url: ""
license: "Apache-2.0"
license_url: "https://github.com/aaif-goose/goose/blob/9f941fbfc5f479d26747d13147457138163ab94e/LICENSE"
evidence_class: "open-source-implementation-and-maintainer-documentation"
metrics_status: "implementation-evidence-only"
artifacts: []
created: 2026-08-19
updated: 2026-08-19
---

# Goose Agent

## Summary

- goose is a local, general-purpose agent harness with desktop, CLI, and API surfaces. Founded by Block, it is now stewarded through the Agentic AI Foundation at the Linux Foundation; the former `block/goose` URL redirects to the current repository.
- Its documented architecture separates the interface, the agent that owns the interactive loop, and extensions. The loop sends the request, conversation context, and tool schemas to a provider; executes returned tool calls; feeds results or execution errors back to the model; revises context; and repeats until a final response.
- Tools are extension-owned and predominantly connected through MCP. Shipped platform and built-in extensions cover development, automation, memory, skills, and subagent delegation; goose can also run as an ACP server or use an external ACP agent as its provider.
- Sessions are automatically saved to a local SQLite database shared by desktop and CLI. The product supports search, resume, fork or duplicate, import, and export; automatic compaction summarizes older history before context-limit fallback strategies are applied.

## Harness Profile

- **Control:** autonomous, manual-approval, smart-approval, and chat-only modes sit above per-tool `always allow`, `ask before`, and `never allow` rules. The documentation describes read/write classification as a provider-interpreted best effort. Native goose documentation does not establish a general OS sandbox for its developer tools; an external CLI or ACP provider may add its own sandbox.
- **Multi-agent:** the default `summon` platform extension can launch temporary internal subagents sequentially or in parallel, with separate context, visible tool activity, configurable extension access, turn limits, and timeouts. Subagents cannot recursively spawn subagents or alter extensions or schedules. This is parent-worker delegation, not evidence of a durable shared task graph, peer messaging, or worktree isolation.
- **Memory and instructions:** `.goosehints` and `AGENTS.md` provide hierarchical project instructions; MOIM can re-read persistent instructions on every turn; the enabled-by-default Skills extension discovers instructions progressively. Long-term local/global memory is a separate built-in MCP extension, so it should not be treated as an unconditional property of every session.
- **Observability:** local session records, component and raw LLM-request logs, downloadable diagnostics, and optional OpenTelemetry or Langfuse export are implemented. Anonymous product telemetry is separately configurable and documented as off by default; diagnostics and raw request logs can contain prompts, code, secrets, and tool output.

## Shipped versus Experimental

The loop, MCP extensions, session persistence, compaction, permission modes, skills, memory extension, subagents, local diagnostics, and optional observability export are documented user-facing features at this snapshot. The documentation explicitly groups mobile and remote access, the VS Code extension, and several local-model/tool-shim paths under an experimental section; they are not used here as stable harness evidence.

## Evidence Boundary

This card audits repository commit `9f941fbfc5f479d26747d13147457138163ab94e`, dated August 19, 2026. Code and maintainer documentation establish a substantial executable harness, but do not independently establish production reliability, security, or comparative task performance.

SQLite conversation persistence makes sessions inspectable and resumable; it is not evidence that external side effects are transactional, idempotent, or crash-replayed. Permission prompts and model-assisted risk classification are control mechanisms rather than isolation boundaries. Likewise, separate subagent contexts reduce main-context pressure but do not by themselves provide filesystem or process isolation.

## Connections

- [[maps/Harness Tracker]]
- [[operations/agent harnesses]]
- [[operations/agent memory]]
- [[concepts/context compaction]]
- [[concepts/agent skills]]
- [[protocols/MCP]]
- [[protocols/ACP]]

## Notes

- Canonical repository: https://github.com/aaif-goose/goose
- Audited snapshot: https://github.com/aaif-goose/goose/tree/9f941fbfc5f479d26747d13147457138163ab94e
- Architecture and loop: https://github.com/aaif-goose/goose/blob/9f941fbfc5f479d26747d13147457138163ab94e/documentation/docs/goose-architecture/goose-architecture.md
- Sessions and SQLite storage: https://github.com/aaif-goose/goose/blob/9f941fbfc5f479d26747d13147457138163ab94e/documentation/docs/guides/sessions/session-management.md
- Context management: https://github.com/aaif-goose/goose/blob/9f941fbfc5f479d26747d13147457138163ab94e/documentation/docs/guides/sessions/smart-context-management.md
- Permission modes and tool rules: https://github.com/aaif-goose/goose/blob/9f941fbfc5f479d26747d13147457138163ab94e/documentation/docs/guides/managing-tools/goose-permissions.md
- Subagents: https://github.com/aaif-goose/goose/blob/9f941fbfc5f479d26747d13147457138163ab94e/documentation/docs/guides/context-engineering/subagents.mdx
- Memory extension: https://github.com/aaif-goose/goose/blob/9f941fbfc5f479d26747d13147457138163ab94e/documentation/docs/mcp/memory-mcp.md
- Local logs: https://github.com/aaif-goose/goose/blob/9f941fbfc5f479d26747d13147457138163ab94e/documentation/docs/guides/logs.md
- OpenTelemetry configuration: https://github.com/aaif-goose/goose/blob/9f941fbfc5f479d26747d13147457138163ab94e/documentation/docs/guides/environment-variables.md#observability
- Experimental-feature boundary: https://github.com/aaif-goose/goose/blob/9f941fbfc5f479d26747d13147457138163ab94e/documentation/docs/experimental/index.md
- No repository content was copied into the vault.
