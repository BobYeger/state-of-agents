# Agent Identity

Agent identity is the operations layer that answers four questions for every agent action: which principal is acting, on whose behalf, under which credential, and who can observe or revoke it.

Agents break the two identity models enterprises already run. They are not human users: one user can spawn hundreds of ephemeral agents, and an agent's authority should usually be a subset of its principal's, scoped to a task. They are not plain workloads either: a service account has fixed behavior reviewed at deploy time, while an agent decides at runtime what it will call. The practical consequence is that static API keys and shared service accounts — the default plumbing of 2024-era agent deployments — provide neither attribution nor revocation at the granularity agents need.

## Three Legs of Agent Identity

Agent identity is being standardized on three separate legs. They answer different questions and do not substitute for each other.

| Leg | Question answered | Mechanisms | Evidence |
|---|---|---|---|
| Enterprise directory identity | Which agent is this inside my org, and what policy applies to it? | Directory-registered agent principals, conditional access, audit logging | [[sources/Microsoft Entra Agent ID]]: every Foundry/Copilot Studio agent gets a directory-visible identity with the full Entra policy stack, GA as of June 2026 |
| Workload identity | How does the agent process authenticate to services without long-lived secrets? | SPIFFE/WIMSE identifiers, short-lived X.509/JWT-SVID credentials, mTLS | [[sources/IETF AIMS Agent Auth Draft]]: composes existing standards into a layered agent-identity stack; mandates exactly one WIMSE identifier per agent |
| Web-facing traffic identity | How does a third-party origin know this request comes from a legitimate agent? | RFC 9421 HTTP Message Signatures validated at the edge | [[sources/Cloudflare Signed Agents]]: per-request cryptographic attribution replacing IP-range and user-agent heuristics |

A design that covers only one leg leaves the others as anonymous traffic. Entra-style directory identity says nothing to origins outside the tenant; signed traffic says nothing about internal policy.

## Delegation Chains

The hard problem is not naming agents but scoping delegation: user → orchestrator → subagent → tool call, where each hop should carry less authority than the one before.

- [[sources/IETF AIMS Agent Auth Draft]] maps OAuth flows to delegation scenarios: authorization code + PKCE for user-delegated access, client credentials for autonomous access, token exchange for cross-domain hops, and Transaction Tokens for per-transaction downscoping that limits lateral movement.
- [[sources/Identity Assertion JWT Authorization Grant]] (ID-JAG, the spec behind Okta Cross App Access) makes the enterprise IdP the policy decision point for cross-domain access: the client exchanges an SSO identity assertion for a JWT authorization grant, replacing N-by-M pairwise app consents. This is the current best answer to "how does my agent reach a SaaS app in another trust domain on the user's behalf without a consent screen per pair."
- [[sources/MCP Authorization]] covers the tool-server hop: MCP servers as OAuth resource servers, so tool access rides on tokens rather than ambient credentials.

The design rule that falls out of these drafts: every hop in the chain should be a token exchange that narrows scope, and the chain should be reconstructable from logs. If a subagent's token is indistinguishable from its parent's, attribution and revocation both fail.

## Cross-Agent Injection Is the Threat Model

Identity infrastructure is necessary but answers only "who is acting." The delegation-specific threat is that a correctly authenticated agent acts on attacker-supplied intent — the confused deputy, at machine speed.

- [[sources/EchoLeak]]: a single crafted email made Microsoft 365 Copilot read in-scope org data and exfiltrate it, zero-click — the agent's legitimate delegated access was the attack's power source, and the paper names this "LLM Scope Violation."
- [[sources/Invariant Labs MCP Tool Poisoning]]: a malicious tool server can redirect a co-connected trusted server's actions (cross-server shadowing), so authenticating both servers does not prevent one from steering the other through the shared model context.
- [[sources/Koi Security Postmark MCP Backdoor]]: an authenticated, user-installed MCP server silently BCC'd outbound email after fifteen clean releases — identity and consent were granted to a principal that later changed behavior.
- [[sources/Willison Lethal Trifecta]] gives the design test: an agent identity that combines private-data access, untrusted-content exposure, and an external channel is exfiltration-capable regardless of how well it authenticates.

The consequence for identity design: scopes should be set assuming the agent will be steered. Delegation narrowing, transaction-scoped tokens, and egress restrictions bound the blast radius of a successful injection; authentication alone bounds nothing. Runtime enforcement of those bounds is the subject of [[operations/permissions]].

## Design Guidance

- Assign one stable identifier per agent, then derive per-task credentials from it. [[sources/IETF AIMS Agent Auth Draft]] makes the one-identifier rule normative; [[sources/Microsoft Entra Agent ID]] implements fleet-scale variants through parent-child identity blueprints so one policy propagates across derived identities.
- Replace static API keys with short-lived credentials bound to the workload. This is the explicit credential model of the AIMS draft and the premise of workload-identity federation for third-party agents in Entra.
- Put the IdP, not the agent framework, at the center of cross-domain policy ([[sources/Identity Assertion JWT Authorization Grant]]). Framework-level allowlists do not survive an agent moving between harnesses.
- Log identity per request, not per session. Signed-agent-style per-request attribution ([[sources/Cloudflare Signed Agents]]) is what makes post-incident reconstruction possible when one agent in a fleet misbehaves.
- Treat revocation latency as a first-class metric. Continuous-evaluation signals (OpenID SSF/CAEP in the AIMS stack) exist because session-lifetime revocation is too slow for agents that act in seconds.

## Maturity

The standards are early. AIMS is an individual IETF submission, not working-group adopted; ID-JAG is WG-adopted but still a draft whose token-exchange semantics may change. [[sources/Microsoft Entra Agent ID]] is the largest deployed system and is GA, but it is a single-vendor directory model that complements rather than implements the IETF track. Cross-vendor authorship on AIMS (AWS, OpenAI, Okta, Zscaler, Ping, Defakto) suggests convergence, but a designer today should expect to bridge at least two of the three legs with custom glue.

## Related

- [[operations/permissions]]
- [[safety/prompt injection]]
- [[safety/agent safety and security]]
- [[safety/sandbox escape and credential exposure]]
- [[protocols/agent protocols]]
- [[protocols/MCP]]
- [[protocols/A2A]]
- [[operations/agent observability]]
- [[sources/MCP Security Best Practices]]
