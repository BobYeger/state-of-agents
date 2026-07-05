Title: What is Microsoft Entra Agent ID? - Microsoft Entra Agent ID

URL Source: https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id

Markdown Content:
Microsoft Entra Agent ID is an identity and security framework that extends Microsoft Entra capabilities to AI agents. As organizations deploy assistive, autonomous, and user-like agents, they need purpose-built identity constructs to authenticate, authorize, govern, and protect these nonhuman identities. Microsoft Entra Agent ID addresses these needs by providing a unified platform for managing agent identities at enterprise scale.

[![Image 1: Diagram showing agent security capabilities offered by Microsoft Entra Agent ID.](https://learn.microsoft.com/en-us/entra/agent-id/media/what-is-microsoft-entra-agent-id/microsoft-entra-agent-identity-capabilities.png)](https://learn.microsoft.com/en-us/entra/agent-id/media/what-is-microsoft-entra-agent-id/microsoft-entra-agent-identity-capabilities-expanded.png#lightbox)

Microsoft Entra Agent ID brings together identity management, access protection, governance, and compliance for AI agents.

The [Microsoft Entra Agent identity platform](https://learn.microsoft.com/en-us/entra/agent-id/what-is-agent-id-platform) enables developers to create and manage [agent identities](https://learn.microsoft.com/en-us/entra/agent-id/what-are-agent-identities), which are specialized identity constructs built for AI agents. Agent identity blueprints serve as templates for creating individual agent identities with parent-child relationships, enabling consistent security policies across large numbers of agents. The platform supports standard protocols such as OAuth 2.0, MCP, and A2A for authentication and agent-to-agent communication.

Microsoft Entra Agent ID works with agents built on Microsoft and non-Microsoft platforms. Organizations can [integrate third-party agents](https://learn.microsoft.com/en-us/entra/agent-id/configure-third-party-agents) from platforms such as AWS Bedrock and n8n by using the Microsoft Entra Auth SDK (sidecar) or workload identity federation, giving every agent a governed identity regardless of where it was built.

Microsoft Entra Agent ID extends existing Microsoft Entra security and governance capabilities to agent identities. Agents receive the same identity-driven protections as users and workloads, including adaptive access policies, real-time risk detection, lifecycle management, and network-level controls. All agent authentication and activity is logged for compliance and audit.

For details on how these capabilities work for agents, see:

*   [Microsoft Entra security for AI overview](https://learn.microsoft.com/en-us/entra/agent-id/security-for-ai-overview)
*   [Conditional Access for agents](https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id)
*   [Identity Protection for agents](https://learn.microsoft.com/en-us/entra/id-protection/concept-risky-agents)
*   [Identity governance for agents](https://learn.microsoft.com/en-us/entra/id-governance/agent-id-governance-overview)
*   [Network controls for agents](https://learn.microsoft.com/en-us/entra/global-secure-access/concept-secure-web-ai-gateway-agents)
*   [Sign-in and audit logs for agents](https://learn.microsoft.com/en-us/entra/agent-id/sign-in-audit-logs-agents)

Microsoft Entra Agent ID is a product within Microsoft Entra that provides the platform for creating and managing agent identities and agent identity blueprints. Agent ID is available for all Microsoft Entra customers.

[Microsoft Agent 365](https://learn.microsoft.com/en-us/microsoft-agent-365/overview) enables agents to operate across Microsoft 365 services and enterprise workflows, which requires a **Microsoft Agent 365** license for each user. For pricing details, see [Microsoft Agent 365 plans and pricing](https://www.microsoft.com/microsoft-agent-365#plans-and-pricing).

Extending Microsoft Entra security features to agents requires **Microsoft 365 E7** (includes Agent 365 and Microsoft Entra Suite) or **Microsoft 365 E5** paired with a **Microsoft Agent 365** license. Customers without E5 or E7 can use the following standalone licensing options with a **Microsoft Agent 365** license:

*   **Conditional Access for agents**: Microsoft Entra ID P1
*   **ID Protection for agents**: Microsoft Entra ID P2
*   **ID Governance for agents**: Microsoft Entra ID P1
*   **Network controls for agents**: Microsoft Entra Internet Access, included in Microsoft Entra Suite or licensed separately. For more information, see [What is Global Secure Access](https://learn.microsoft.com/en-us/entra/global-secure-access/overview-what-is-global-secure-access#licensing-overview).

*   [Microsoft Entra security for AI overview](https://learn.microsoft.com/en-us/entra/agent-id/security-for-ai-overview)
*   [What are agent identities?](https://learn.microsoft.com/en-us/entra/agent-id/what-are-agent-identities)
*   [What is the Microsoft Entra Agent identity platform?](https://learn.microsoft.com/en-us/entra/agent-id/what-is-agent-id-platform)
