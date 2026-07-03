---
title: "sandbox-runtime: OS-level sandboxing for agent processes (anthropic-experimental)"
aliases:
  - "sandbox-runtime"
  - "@anthropic-ai/sandbox-runtime"
source_type: "repository"
kind: "sandbox-runtime"
status: "verified"
year: 2025
publication_date: "2025-10-20"
publication_date_basis: "github_repo"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Anthropic"
venue: "GitHub repository"
url: "https://github.com/anthropic-experimental/sandbox-runtime"
pdf_url: ""
created: 2026-07-03
updated: 2026-07-03
---

# sandbox-runtime (anthropic-experimental)

## Summary

- OS-level sandboxing for agent processes without containers: bubblewrap plus seccomp BPF filters on Linux, sandbox-exec with dynamically generated Seatbelt profiles on macOS, and alpha Windows support via Windows Filtering Platform and ACL stamping.
- All network egress is forced through host-side HTTP and SOCKS5 proxies reached over Unix domain sockets (socat bridging); on Linux the network namespace is removed entirely, so no traffic can bypass the proxy choke point.
- A seccomp BPF filter blocks AF_UNIX socket creation at the syscall level when `allowAllUnixSockets=false`, applied via a two-stage apply-seccomp binary inside a nested PID namespace.
- The host proxy is the enforcement point for domain allowlists, per-request user confirmation, and arbitrary custom egress rules — the same architecture Claude Code on the web uses to keep git credentials outside the sandbox (the proxy validates a scoped in-sandbox credential, checks branch/repo, then attaches the real GitHub token).
- Distributed as @anthropic-ai/sandbox-runtime on npm under Apache 2.0; ~4.6k stars, 344 forks, used by 482 projects; v0.0.63 released 2026-07-01, so actively maintained nine months after the October 2025 launch.

## Connections

- [[operations/sandboxes]]
- [[operations/permissions]]
- [[safety/sandbox escape and credential exposure]]
- [[systems/Claude Code]]
- [[sources/Anthropic Claude Code Sandboxing]]

## Notes

- Canonical URL: https://github.com/anthropic-experimental/sandbox-runtime
- Reference implementation of the proxy-egress choke point that enables proxy-injected credentials and secretless sandboxes; companion to the October 2025 Claude Code sandboxing post already in the vault.
- Repo sits under anthropic-experimental; API stability is not guaranteed (v0.0.x versioning).
