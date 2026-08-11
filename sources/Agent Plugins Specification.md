---
title: "Agent Plugins Specification 1.0.0"
aliases:
  - "Agent Plugins 1.0"
  - "Open Plugin Specification"
  - "Open Plugin Spec"
source_type: "spec"
kind: "plugin-package-standard"
status: "verified"
year: 2026
publication_date: "2026-07-24"
publication_date_basis: "specification_publication_commit_timestamp"
source_updated_date: "2026-08-06"
source_updated_date_basis: "open_standard_positioning_commit_timestamp"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Agent Plugins Project"
venue: "Agent Plugins"
url: "https://github.com/agentplugins/agent-plugins-spec/blob/1fc1b6270e3cc492ec2d24ad7a34277c6d53b9c1/spec/1.0.0.md"
pdf_url: ""
artifacts:
  - "raw/protocols/agent-plugins-specification-1.0.0.md"
created: 2026-08-11
updated: 2026-08-11
---

# Agent Plugins Specification 1.0.0

## Summary

- Agent Plugins 1.0.0 defines an open, vendor-neutral package format for portable agent capabilities. Its interoperability floor deliberately contains only two component types with existing cross-client formats: Agent Skills and MCP servers.
- A conforming package requires only a closed-schema `plugin.json` at its root. It may also contain skills under `skills/<name>/SKILL.md`, MCP server configuration in `mcp.json`, or both. The manifest requires `$schema` and `name`; component locations are fixed rather than declared in the manifest.
- Vendor- or client-specific capabilities live under reverse-domain keys in `extensions` and optional matching top-level directories. This lets a portable core coexist with richer native features without presenting those features as standardized.
- Clients that launch stdio plugin subprocesses must provide `${PLUGIN_ROOT}` for bundled files and `${PLUGIN_DATA}` for client-managed persistent state. Filesystem-resolved package paths, plugin-relative `command` values, and rooted `cwd` values have containment rules; ordinary arguments, environment values, and runtime-supplied paths are not thereby confined, and the specification does not sandbox subprocesses.
- Conformance is incremental: a client may support Skills, MCP, or both, and MCP transport support can differ. Compatibility with the package format therefore does not imply feature parity between clients.
- Distribution, installation, permissions, approval UX, authentication, credential storage, and client-specific behavior remain under host control.

## Portable Contract

| Surface | Version 1 contract |
|---|---|
| Manifest | Root `plugin.json` using `https://agent-plugins.org/schemas/1.0.0/plugin.schema.json` |
| Skills | Optional `skills/`; immediate children containing a conforming `SKILL.md` |
| MCP | Optional root `mcp.json`; stdio, Streamable HTTP, and optional legacy SSE configurations |
| Extensions | Reverse-domain manifest namespaces and matching optional top-level directories |
| Stdio subprocess paths | Client-provided `PLUGIN_ROOT` and persistent `PLUGIN_DATA` |

## Governance and Adoption

The initial core maintainers are affiliated with Amazon, Cursor, Microsoft, OpenAI, and Vercel; Vercel's Jonathan Hefner is lead core maintainer. Governance assigns roles to individuals, reserves no company seats, and prohibits one vendor from holding a majority of core-maintainer seats.

The project's compatibility matrix lists VS Code, Cursor, GitHub Copilot, ChatGPT and Codex, Kiro, Hermes Agent, and OpenClaw. This is declared client support rather than evidence that all clients load every component or transport. Anthropic is absent from both the initial Technical Steering Committee and compatibility matrix even though Agent Skills and MCP originated in its ecosystem.

## Design Consequences

- Agent Plugins standardizes a package boundary above [[concepts/agent skills|Agent Skills]] and [[protocols/MCP|MCP]]; it does not replace either underlying standard.
- The narrow core explains how clients can converge on package portability while retaining proprietary agents, hooks, commands, rules, UI metadata, marketplaces, and policy systems.
- A conforming package is not thereby trusted. Version 1 does not define signatures, provenance, permissions, sandboxing, secret acquisition, dependencies, enterprise policy, or a conformance test suite.
- `mcp.json` is a portable connection configuration, distinct from the MCP wire protocol and from the MCP Registry's server-authored `server.json` metadata.

## Connections

- [[concepts/agent plugins]]
- [[concepts/agent skills]]
- [[protocols/MCP]]
- [[safety/protocol security]]
- [[maps/Agent Skills Map]]
- [[sources/Agent Skills Specification]]

## Artifacts

- [[raw/protocols/agent-plugins-specification-1.0.0.md]]

## Evidence Boundary

The versioned specification is the normative primary source for package layout, manifest fields, extensions, environment variables, and conformance. The governance file, maintainer list, compatibility matrix, and future-considerations document are official first-party project records, not independent evidence of adoption or production reliability. The compatibility matrix should be read as declared support because the specification explicitly permits partial conformance.

There is also a point-in-time publication inconsistency. The canonical repository marks version 1.0.0 as **Published**, while the generated specification page still labels it **Working Draft** as of 2026-08-11. This card treats the versioned repository document and its July 24 publication commit as canonical while retaining the website mismatch as a maturity signal.

## Notes

- Canonical publication snapshot: https://github.com/agentplugins/agent-plugins-spec/blob/1fc1b6270e3cc492ec2d24ad7a34277c6d53b9c1/spec/1.0.0.md
- Live specification: https://github.com/agentplugins/agent-plugins-spec/blob/main/spec/1.0.0.md
- Publication commit: https://github.com/agentplugins/agent-plugins-spec/commit/1fc1b6270e3cc492ec2d24ad7a34277c6d53b9c1
- Project homepage: https://agent-plugins.org/
- Governance: https://github.com/agentplugins/agent-plugins-spec/blob/main/GOVERNANCE.md
- Maintainers: https://github.com/agentplugins/agent-plugins-spec/blob/main/MAINTAINERS.md
- Compatible clients: https://agent-plugins.org/compatible-clients
- Explicitly deferred concerns: https://github.com/agentplugins/agent-plugins-spec/blob/main/FUTURE_CONSIDERATIONS.md
- OpenAI's current native packaging guide: https://developers.openai.com/plugins/build/plugins
- Cursor's native and standard package comparison: https://cursor.com/docs/plugins
- VS Code's Agent Plugins documentation: https://code.visualstudio.com/docs/agent-customization/agent-plugins
- Claude Code's separate native plugin format: https://code.claude.com/docs/en/plugins-reference
- Publication date basis: the repository commit titled "Publish Agent Plugins Specification 1.0.0" on 2026-07-24.
- Source update basis: the project's 2026-08-06 change describing Agent Plugins as an open standard.
- `Open Plugin Specification` and `Open Plugin Spec` are retained as historical aliases: the project used that name before renaming itself to Agent Plugins prior to publication.
- The captured specification text is licensed under CC BY 4.0 and preserved unchanged below the attribution header; repository code and schemas use Apache 2.0.
