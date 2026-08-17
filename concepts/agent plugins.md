# agent plugins

Agent Plugins are the portable package layer above [[concepts/agent skills|Agent Skills]] and [[protocols/MCP|MCP]]. A skill packages reusable procedure; MCP defines runtime communication with tools and data; an Agent Plugin groups one or both into a directory that compatible clients can discover and load.

Version 1.0.0 is deliberately a minimum interoperability floor. It does not try to make every feature of Codex, Cursor, VS Code, GitHub Copilot, Claude Code, or other agent hosts portable.

## Portable Contract

```text
plugin.json
skills/<skill-name>/SKILL.md  # optional component
mcp.json                      # optional component
com.vendor.client/...       # optional, non-portable extension
```

Only the root manifest is required. When present, Skills and MCP configuration use fixed locations; the manifest does not redirect them. Reverse-domain extension namespaces let vendors preserve richer behavior without adding it to the portable contract.

For clients that launch stdio plugin subprocesses, the specification defines `PLUGIN_ROOT` for bundled files and `PLUGIN_DATA` for persistent client-managed state. Containment applies to filesystem-resolved package paths, plugin-relative commands, and working directories rooted at the plugin or its client-managed data directory. It does not reinterpret ordinary arguments, environment values, or runtime-supplied paths as package paths, and it is not a subprocess sandbox.

## Layered Standardization

| Layer | Portable unit | What remains outside it |
|---|---|---|
| Agent Skills | `SKILL.md` plus optional scripts, references, and assets | Trigger policy, execution quality, permissions |
| MCP | Tool, resource, and prompt communication | Server trust, registry vetting, most host UX |
| Agent Plugins | Required `plugin.json`; optional `skills/` and/or `mcp.json` | Installation, updates, stores, signatures, policy |
| Vendor layer | Client extensions and native plugin formats | Not portable by definition |

The convergence is therefore compositional rather than a single universal plugin runtime. Portability must be evaluated at each layer: a client can conform while supporting only Skills or only MCP, and an MCP-capable client need not support every transport.

## Runtime-Plugin Boundary

[[sources/DeepSeek Harness Repository|DeepSeek Harness]] uses *plugin* for an internal runtime component that contributes services, typed events, and reversible registrations to a shared Cordis context. Its formal basis, [[sources/A Programming Paradigm for Spatiotemporal Composability|Cordis]], concerns component lifecycle and reactive dependency reconciliation. That is not the portable Agent Plugins package standard: Cordis does not define `plugin.json`, Skills/MCP packaging, cross-client distribution, or conformance, while Agent Plugins does not standardize a host's internal component graph or unload semantics.

## Vendor Adoption

[[sources/Agent Plugins Specification]] records an initial Technical Steering Committee spanning Amazon, Cursor, Microsoft, OpenAI, and Vercel. The project-maintained compatibility matrix lists VS Code, Cursor, GitHub Copilot, ChatGPT and Codex, Kiro, Hermes Agent, and OpenClaw.

Native formats remain broader. OpenAI's published packaging guide still centers `.codex-plugin/plugin.json`; Cursor retains `.cursor-plugin/plugin.json`; VS Code and GitHub layer agents, commands, hooks, and marketplace behavior around the portable core. Claude Code continues to document `.claude-plugin/plugin.json` and is not on the standard's current compatible-client list.

This coexistence is expected rather than a failure of the standard. Agent Plugins provides the common package substrate; clients retain control of installation, presentation, permissions, approval flows, and differentiated features.

## Trust and Maturity Boundary

Version 1 does not define a shared model for trust, permissions, sandboxing, signatures, provenance, secrets, dependencies, enterprise audit policy, or conformance testing. Installing a conforming plugin can still introduce executable MCP servers and untrusted skill instructions, so package compatibility must not be treated as a security endorsement.

The release is also very fresh: the versioned repository calls 1.0.0 published, while the generated documentation page still says Working Draft. The format is meaningful enough to track, but not settled infrastructure.

## Related Sources

- [[sources/Agent Plugins Specification]]
- [[sources/Agent Skills Specification]]
- [[sources/MCP Specification 2026-07-28]]
- [[sources/MCP Registry]]
- [[sources/DeepSeek Harness Repository]]
- [[sources/A Programming Paradigm for Spatiotemporal Composability]]

## Related

- [[concepts/agent skills]]
- [[protocols/MCP]]
- [[safety/protocol security]]
- [[operations/permissions]]
- [[operations/sandboxes]]
- [[maps/Agent Skills Map]]
