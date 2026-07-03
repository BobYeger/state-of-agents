# agent protocol governance

Agent protocol governance is how agent protocols move from vendor proposals to open standards: neutral IP hosting, formal change processes, foundation stewardship, and consolidation of competing specs.

2025 was the year this happened for real. All three major vendor-launched agent protocols changed hands within nine months, and the change processes that now decide what MCP and A2A become are documented, dated, and citable.

## Governance Events

| Date | Event | What it settled | Source |
|---|---|---|---|
| 2025-06-23 | Google donates A2A to a new Linux Foundation project | Neutral IP hosting ~2.5 months after launch; founding members Google, AWS, Cisco, Microsoft, Salesforce, SAP, ServiceNow | [[sources/Linux Foundation A2A Project Launch]] records the donation, roster, and repo move to a2aproject/A2A |
| 2025-07-31 | MCP formalizes governance via SEP-932 | Python/PyTorch-style maintainer hierarchy; all spec changes flow through Specification Enhancement Proposals; membership is individual, not company seats | [[sources/MCP Governance and Stewardship]] documents the SEP process, working groups, and named maintainers |
| 2025-08-29 | IBM's ACP (BeeAI) merges into A2A | Explicit consolidation, not coexistence: ACP wound down active development after ~5 months as an independent LF protocol; IBM took an A2A TSC seat | [[sources/ACP Joins A2A Under Linux Foundation]] is the joint IBM/Google account of the merger and migration path |
| 2025-09-08 | MCP Registry launches in preview | Central authoritative catalog with sub-registry architecture and DNS/GitHub namespacing; still pre-GA as of 2026-07 | [[sources/MCP Registry]] describes the architecture and its reactive denylist moderation |
| 2025-12-09 | Anthropic donates MCP; Agentic AI Foundation established | AAIF is a directed fund under the Linux Foundation co-founded by Anthropic, Block, and OpenAI; MCP's maintainer-led technical governance explicitly unchanged | [[sources/Anthropic MCP Donation and Agentic AI Foundation]] records the donation, co-founders, and adoption figures at transfer |
| 2026-03-12 | A2A v1.0.0 ships | First stable major release under LF governance | [[sources/A2A Specification]] is the versioned v1.0.0 spec |
| 2026-03-23 | CNCF publishes cloud native agentic standards | First vendor-neutral deployment-standards framework naming a concrete protocol stack: MCP, A2A, AP2, SPIFFE/SPIRE | [[sources/CNCF Cloud Native Agentic Standards]] is the endorsement snapshot, self-described as high-churn |
| 2026-05-21 | MCP 2026-07-28 release candidate freezes | Next revision developed under working-group process with a 10-week SDK validation window before the scheduled 2026-07-28 final | [[sources/MCP Specification 2026-07-28 Release Candidate]] details the RC content and the roadmap shift to working-group-driven development |

## What the 2025 Events Teach

- Donation is now table stakes, not an endpoint. A2A went to the Linux Foundation about 2.5 months after launch ([[sources/Linux Foundation A2A Project Launch]]); vendors treat neutral hosting as a precondition for multi-vendor adoption rather than a reward for maturity.
- Foundation hosting does not guarantee survival. IBM's ACP was donated to the Linux Foundation in March 2025 and merged out of existence by August — roughly a 5-month lifespan ([[sources/ACP Joins A2A Under Linux Foundation]]). Governance venue and ecosystem traction are separate variables.
- Donation and governance are separable. The MCP transfer moved IP and funding to AAIF while leaving day-to-day technical authority with the existing maintainer hierarchy and SEP process ([[sources/MCP Governance and Stewardship]] is the primary evidence that the board handles membership and money, not spec content).
- The venues are multiplying by layer. Protocol specs sit with LF/AAIF, deployment and identity standards with CNCF ([[sources/CNCF Cloud Native Agentic Standards]]), and agent authentication is moving onto the IETF standards track ([[sources/IETF AIMS Agent Auth Draft]] proposes short-lived cryptographic credentials to replace static API keys). Tracking one foundation no longer covers the stack.
- Naming is not governed. IBM's Agent Communication Protocol and Zed's Agent Client Protocol are both "ACP"; this vault's [[protocols/ACP]] is Zed's, which remains active.

## Adoption Evidence and the Counterweight

Adoption datapoints at the governance milestones: MCP transferred with 10,000+ active public servers and 97M+ monthly SDK downloads, vendor-reported ([[sources/Anthropic MCP Donation and Agentic AI Foundation]]); A2A was donated with over 100 supporting companies, a promotional press-release figure ([[sources/Linux Foundation A2A Project Launch]]). Post-v1.0 A2A support shows up in infrastructure — [[sources/kagent]] makes A2A first-class for agent delegation on Kubernetes, [[sources/agentgateway]] proxies A2A alongside MCP in one data plane, and [[sources/Microsoft Entra Agent ID]] supports A2A for agent-to-agent authentication.

The counterweight: infrastructure support is not production traffic. [[sources/Cognition Multi-Agents Whats Actually Working]] describes production manager-child delegation coordinated over internal MCP — one of the most visible multi-agent deployments routes around the agent-to-agent protocol entirely. And [[sources/A Survey of AI Agent Protocols]], the field's taxonomy backbone, pre-dates both the LF consolidation and the MCP 2025-11-25 revision, so its per-protocol comparisons are a 2025 snapshot. Governance maturity is currently ahead of demonstrated cross-organization adoption, especially for A2A.

## Related

- [[protocols/agent protocols]]
- [[protocols/MCP]]
- [[protocols/A2A]]
- [[protocols/ACP]]
- [[safety/protocol security]]
- [[maps/Protocols Map]]

## Related Sources

- [[sources/Anthropic Introducing MCP]]
- [[sources/MCP Specification 2025-11-25]]
- [[sources/MCP Specification 2026-07-28 Release Candidate]]
- [[sources/MCP Governance and Stewardship]]
- [[sources/MCP Registry]]
- [[sources/Anthropic MCP Donation and Agentic AI Foundation]]
- [[sources/Linux Foundation A2A Project Launch]]
- [[sources/ACP Joins A2A Under Linux Foundation]]
- [[sources/A2A Specification]]
- [[sources/A2A GitHub Repository]]
- [[sources/CNCF Cloud Native Agentic Standards]]
- [[sources/IETF AIMS Agent Auth Draft]]
- [[sources/A Survey of AI Agent Protocols]]
- [[sources/Google Developer Guide to AI Agent Protocols]]
- [[sources/Google Agent Payments Protocol AP2]]
- [[sources/Google Universal Commerce Protocol]]
