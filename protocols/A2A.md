# A2A

Agent2Agent is an interoperability protocol for communication and coordination among agents across vendors, frameworks, and enterprise systems. Where [[protocols/MCP]] connects an agent to tools and data, A2A lets independently implemented agents advertise skills through agent cards, exchange tasks, stream progress, and return artifacts ([[sources/A2A Specification]] is the primary source for protocol semantics).

## Version and Governance Timeline

| Date | Event | Source |
|---|---|---|
| 2025-04-09 | Google launches A2A | [[sources/A2A GitHub Repository]] tracks the living implementation surface |
| 2025-06-23 | Google donates spec, SDKs, and tooling to a new Linux Foundation project; founding members Google, AWS, Cisco, Microsoft, Salesforce, SAP, ServiceNow | [[sources/Linux Foundation A2A Project Launch]] |
| 2025-08-29 | IBM's ACP merges into A2A; IBM joins the Technical Steering Committee | [[sources/ACP Joins A2A Under Linux Foundation]] |
| 2026-03-12 | v1.0.0 ships — first stable major release under LF governance | [[sources/A2A Specification]] |

Version 1.0.0 is the protocol's stability commitment: a versioned spec produced under neutral multi-vendor governance rather than a Google draft, published roughly nine months after the donation. The vault's spec card and raw capture track the v1.0.0 path specifically, so protocol claims can be pinned to the stable release rather than the moving `latest` docs.

## Relationship to the ACP Merge

IBM's Agent Communication Protocol (launched March 2025 to power BeeAI, donated to the Linux Foundation the same month) wound down as an independent protocol and merged into A2A in August 2025 — a consolidation, not a bridge: BeeAI users got adapters and a migration guide rather than a compatibility layer in the spec ([[sources/ACP Joins A2A Under Linux Foundation]] is the joint IBM/Google account, and its ~5-month independent lifespan is the standing evidence that foundation hosting does not guarantee protocol survival). Name collision warning: this vault's [[protocols/ACP]] is Zed's Agent Client Protocol — editor-to-agent, unrelated, still active.

## Adoption Evidence and Its Limits

Post-v1.0 support is visible in infrastructure:

- [[sources/kagent]] makes A2A first-class for agent-to-agent discovery and delegation on Kubernetes (CNCF ecosystem).
- [[sources/agentgateway]] handles A2A alongside MCP and LLM traffic in a single proxy data plane.
- [[sources/Microsoft Entra Agent ID]] supports A2A in its agent identity and authentication platform.
- [[sources/CNCF Cloud Native Agentic Standards]] names A2A in its endorsed cloud-native protocol stack.
- [[sources/Google ADK A2A Cross-Language Multi-Agent Team]] demonstrates a working cross-language agent team coordinated over the protocol.

The counterweight: this is infrastructure readiness, not demonstrated cross-organization production traffic. The launch-era "over 100 companies" figure is promotional ([[sources/Linux Foundation A2A Project Launch]]), and the most visible production multi-agent deployment routes around A2A entirely — [[sources/Cognition Multi-Agents Whats Actually Working]] coordinates manager-child delegation over internal MCP. A2A's core value proposition, agents interoperating across trust and vendor boundaries, remains mostly prospective as of mid-2026; within a single organization, an internal tool protocol has so far been sufficient.

## Security

Cross-boundary agent communication inherits every injection and impersonation problem, plus discovery: [[sources/A2ASecBench]] is the protocol-aware security benchmark for A2A multi-agent systems, and [[sources/Building A Secure Agentic AI Application Leveraging A2A Protocol]] is the reference secure-deployment walkthrough. General threat framing lives in [[safety/protocol security]].

## Related

- [[protocols/agent protocols]]
- [[protocols/agent protocol governance]]
- [[protocols/MCP]]
- [[protocols/ACP]]
- [[concepts/multi-agent systems]]
- [[safety/protocol security]]

## Related Sources

- [[sources/A2A Specification|Agent2Agent Protocol Specification]]
- [[sources/A2A GitHub Repository|A2A GitHub Repository]]
- [[sources/Linux Foundation A2A Project Launch]]
- [[sources/ACP Joins A2A Under Linux Foundation]]
- [[sources/A2ASecBench|A2ASecBench: A Protocol-Aware Security Benchmark for Agent-to-Agent Multi-Agent Systems]]
- [[sources/Building A Secure Agentic AI Application Leveraging A2A Protocol|Building A Secure Agentic AI Application Leveraging A2A Protocol]]
- [[sources/Google ADK Multi-Agent Patterns|Developer's guide to multi-agent patterns in ADK]]
- [[sources/Google ADK A2A Cross-Language Multi-Agent Team]]
- [[sources/A2A Course]]
