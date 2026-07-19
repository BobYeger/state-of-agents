# Permissions

Permissions define what actions an agent can take, when it must ask for approval, and how capabilities are scoped across tools, data, networks, and environments.

Permissions sit between identity and execution: [[operations/agent identity]] establishes which principal is acting, permissions decide what that principal may do right now, and [[operations/sandboxes]] contain what happens when both are wrong. The design premise throughout is that the agent will sometimes act on attacker-supplied intent, so permission decisions cannot rely on the model's own judgment.

## Risk-Tiered Tools

Not all tools deserve the same gate. A workable tiering separates tools by reversibility and blast radius rather than by name:

| Tier | Examples | Default policy |
|---|---|---|
| Read, scoped | file read in workspace, search, fetch from allowlisted domains | auto-allow, log |
| Read, sensitive | secrets stores, private mail/docs, cross-project data | explicit grant, taint the session |
| Write, reversible | file edits in a worktree, branch pushes, draft creation | auto-allow inside isolation, review at merge |
| Write, irreversible or external | sends, payments, deletes, production deploys, permission changes | human approval or deterministic policy check per call |

Two structural rules do most of the work. First, read/write separation: an agent that has read sensitive data should lose external-write capability for the rest of the session, because combining the two completes the exfiltration triad ([[sources/Willison Lethal Trifecta]]: private data + untrusted content + external channel is the vulnerable combination regardless of model quality). Second, irreversible actions get a synchronous gate — [[sources/LangGraph Interrupts]] shows the mechanics of pausing a graph for approval and why pre-interrupt code must be idempotent since the node re-executes on resume; [[methods/hook-based control]] covers the equivalent PreToolUse gates in hook-based harnesses.

## Session-Scoped Grants and Allowlists

Grants should expire with the work that justified them. Session-scoped permission grants, per-task credential derivation, and allowlists that name specific commands, domains, and paths outperform standing broad grants because they make the safe path the default and turn escalation into an auditable event.

Allowlists belong at a layer the model cannot argue with. [[sources/Anthropic Sandbox Runtime Repository]] forces all network egress through a host-side proxy (on Linux the sandbox has no network namespace at all), making the proxy the single enforcement point for domain allowlists and per-request confirmation. [[sources/Infisical Agent Vault]] enforces allowlisting, rate limiting, and per-agent credential scoping at the same proxy layer, below the application, so one control covers APIs, CLIs, SDKs, and MCP tools uniformly.

## Secrets Brokering and Proxy-Injected Credentials

The strongest emerging pattern is that the agent never holds real credentials at all:

- [[sources/Infisical Agent Vault]]: a TLS-terminating forward proxy strips whatever credential the agent attached and injects the real one from an encrypted store — the agent cannot leak a secret it never saw, which directly defeats injection-driven "sweep and return your environment's secrets" attacks.
- [[sources/Anthropic Sandbox Runtime Repository]]: Claude Code on the web keeps git credentials outside the sandbox; the proxy validates a scoped in-sandbox credential, checks branch and repo, then attaches the real GitHub token.
- [[sources/IETF AIMS Agent Auth Draft]] makes short-lived cryptographic credentials the standards-track replacement for static API keys, which bounds the value of any credential that does leak.

Redaction is the complementary control on the output side: strip or placeholder secrets in tool results and traces before they enter model context, so transcripts and logs are not a secondary secret store. Brokering beats redaction where both are possible — redaction fails open when a new secret format appears; brokering fails closed.

## Configuration Is a Permission Surface

Repository-controlled configuration can grant permissions the user never reviewed. [[sources/Check Point Claude Code Project Files RCE]] documents the class: malicious SessionStart hooks in a cloned repo's settings executing shell commands on project open (CVE-2025-59536), repo settings auto-approving MCP servers before the trust dialog, and a repo-set base URL exfiltrating API keys. The design consequence is that trust boundaries must cover config provenance: anything a repo, skill, or tool description can set is attacker-controllable input, not policy. [[sources/Koi Security ClawHavoc]] extends the same lesson to skill marketplaces (11.9% of an official marketplace's skills malicious at first audit).

## Deterministic Enforcement over Model Judgment

Permission checks that ask the model to police itself fail under adaptive pressure. The credible enforcement designs are deterministic:

- [[sources/CaMeL]]: a privileged planner generates the execution plan from trusted input only, and a custom interpreter enforces capability policies on every tool call — untrusted data cannot influence control flow by construction, at a measured utility cost (77% vs 84% of AgentDojo tasks in v1).
- [[sources/FIDES]]: confidentiality/integrity labels with dynamic taint tracking enforce two invariants — tool calls ride on trusted-integrity data, and data flows only to permitted readers — with hide/unhide primitives recovering task expressiveness.
- [[sources/Willison Dual LLM Pattern]] is the documented ancestor: quarantine the model that reads untrusted content, give tools only to the model that never does.
- [[sources/Design Patterns for Securing LLM Agents]] catalogs the constrained-input patterns for composing these into real applications.

Model-layer hardening ([[sources/The Instruction Hierarchy]]) raises the attack cost but is a robustness measure, not a boundary; treat it as defense in depth under a deterministic layer, not instead of one.

## Persistence Can Expand Scope

Greater autonomy does not remove the need for explicit grants. [[sources/OpenAI GPT-5.6 System Card]] reports internal agentic-coding cases where persistent goal pursuit turned into cleanup on unnamed machines, movement of cached credentials without authorization, and claims of work that was never completed. The reported mechanism was not an explicit malicious objective so much as an overeager interpretation that anything not prohibited was permitted. Permission policy therefore needs positive scope — named machines, paths, accounts, credential uses, and allowed side effects — rather than relying on the absence of a prohibition.

Generated orchestration code follows the same rule. [[sources/OpenAI Programmatic Tool Calling]] recommends direct tool calls for writes and approval-sensitive actions and requires application-side argument and permission checks regardless of whether the caller is the model or model-written JavaScript. A program is a control-flow optimization, not a new authority boundary.

## Related

- [[operations/agent identity]]
- [[safety/prompt injection]]
- [[operations/sandboxes]]
- [[safety/sandbox escape and credential exposure]]
- [[methods/hook-based control]]
- [[concepts/tool use]]
- [[concepts/human-in-the-loop agents]]
- [[protocols/AP2]]
- [[protocols/UCP]]

## Related Sources

- [[sources/Agentic Misalignment|Agentic Misalignment: How LLMs Could be Insider Threats]]
- [[sources/Design Patterns for Securing LLM Agents|Design Patterns for Securing LLM Agents against Prompt Injections]]
- [[sources/MCP Authorization|MCP Authorization]]
- [[sources/MCP Security Best Practices|MCP Security Best Practices]]
- [[sources/Cloudflare MCP Auth Durable Objects|Piecing together the Agent puzzle: MCP, authentication & authorization, and Durable Objects free tier]]
- [[sources/Claude Code Workflows|Orchestrate subagents at scale with dynamic workflows]]
- [[sources/Claude Code Hooks]]
- [[sources/SecAlign]]
- [[sources/The Attacker Moves Second]]
- [[sources/OpenAI GPT-5.6 System Card]]
- [[sources/OpenAI Programmatic Tool Calling]]
