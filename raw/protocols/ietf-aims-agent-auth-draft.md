Title: AI Agent Authentication and Authorization

URL Source: https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/

Markdown Content:
Internet-Draft AI-Auth June 2026
Kasselman, et al.Expires 3 December 2026[Page]

## [Abstract](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#abstract)

This document proposes best practices for authentication and authorization of AI agent interactions. It leverages existing standards such as the Workload Identity in Multi-System Environments (WIMSE) architecture and OAuth 2.0 family of specifications. Rather than defining new protocols, this document describes how existing and widely deployed standards can be applied or extended to establish agent authentication and authorization. By doing so, it aims to provide a framework within which to use existing standards, identify gaps and guide future standardization efforts for agent authentication and authorization.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-abstract-1)

## [About This Document](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-about-this-document)

This note is to be removed before publishing as an RFC.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-note.1-1)

The latest revision of this draft can be found at [https://PieterKas.github.io/agent2agent-auth-framework/draft-klrc-aiagent-auth.html](https://pieterkas.github.io/agent2agent-auth-framework/draft-klrc-aiagent-auth.html). Status information for this document may be found at [https://datatracker.ietf.org/doc/draft-klrc-aiagent-auth/](https://datatracker.ietf.org/doc/draft-klrc-aiagent-auth/).[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-note.1-2)

Source for this draft and an issue tracker can be found at [https://github.com/PieterKas/agent2agent-auth-framework](https://github.com/PieterKas/agent2agent-auth-framework).[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-note.1-3)

## [Status of This Memo](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-status-of-this-memo)

This Internet-Draft is submitted in full conformance with the provisions of BCP 78 and BCP 79.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-boilerplate.1-1)

Internet-Drafts are working documents of the Internet Engineering Task Force (IETF). Note that other groups may also distribute working documents as Internet-Drafts. The list of current Internet-Drafts is at [https://datatracker.ietf.org/drafts/current/](https://datatracker.ietf.org/drafts/current/).[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-boilerplate.1-2)

Internet-Drafts are draft documents valid for a maximum of six months and may be updated, replaced, or obsoleted by other documents at any time. It is inappropriate to use Internet-Drafts as reference material or to cite them other than as "work in progress."[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-boilerplate.1-3)

This Internet-Draft will expire on 3 December 2026.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-boilerplate.1-4)

## [Copyright Notice](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-copyright-notice)

Copyright (c) 2026 IETF Trust and the persons identified as the document authors. All rights reserved.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-boilerplate.2-1)

This document is subject to BCP 78 and the IETF Trust's Legal Provisions Relating to IETF Documents ([https://trustee.ietf.org/license-info](https://trustee.ietf.org/license-info)) in effect on the date of publication of this document. Please review these documents carefully, as they describe your rights and restrictions with respect to this document. Code Components extracted from this document must include Revised BSD License text as described in Section 4.e of the Trust Legal Provisions and are provided without warranty as described in the Revised BSD License.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-boilerplate.2-2)

[▲](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#)
## [Table of Contents](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-table-of-contents)

*   [1](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-1).[Introduction](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-introduction)

*   [2](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-2).[Conventions and Definitions](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-conventions-and-definitions)

*   [3](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-3).[Agents are workloads](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-agents-are-workloads)

*   [4](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-4).[Agent Identity Management System](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-agent-identity-management-s)

*   [5](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-5).[Agent Identifier](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-agent-identifier)

*   [6](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-6).[Agent Credentials](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-agent-credentials)

*   [7](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-7).[Agent Credential Provisioning](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-agent-credential-provisioni)

*   [8](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-8).[Agent Authentication](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-agent-authentication)

    *   [8.1](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-8.1).[Transport Layer Authentication](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-transport-layer-authenticat)

        *   [8.1.1](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-8.1.1).[Limitations](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-limitations)

    *   [8.2](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-8.2).[Application Layer Authentication](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-application-layer-authentic)

        *   [8.2.1](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-8.2.1).[WIMSE Proof Tokens (WPTs)](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-wimse-proof-tokens-wpts)

        *   [8.2.2](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-8.2.2).[HTTP Message Signatures](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-http-message-signatures)

        *   [8.2.3](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-8.2.3).[Limitations](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-limitations-2)

*   [9](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9).[Agent Authorization](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-agent-authorization)

    *   [9.1](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.1).[Agent Mission](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-agent-mission)

    *   [9.2](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.2).[Leverage OAuth 2.0 as a Delegation Authorization Framework](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-leverage-oauth-20-as-a-dele)

    *   [9.3](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.3).[Use of OAuth 2.0 Access Tokens](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-use-of-oauth-20-access-toke)

    *   [9.4](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.4).[Obtaining an OAuth 2.0 Access Token](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-obtaining-an-oauth-20-acces)

        *   [9.4.1](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.4.1).[User Delegates Authorization](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-user-delegates-authorizatio)

        *   [9.4.2](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.4.2).[Agent Obtains Own Authorization](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-agent-obtains-own-authoriza)

        *   [9.4.3](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.4.3).[Agents Accessed by Systems or Other Agents](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-agents-accessed-by-systems-)

        *   [9.4.4](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.4.4).[OAuth 2.0 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-oauth-20-security-best-prac)

    *   [9.5](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.5).[Risk Reduction with Transaction Tokens](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-risk-reduction-with-transac)

    *   [9.6](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.6).[Cross Domain Access](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-cross-domain-access)

    *   [9.7](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.7).[Human in the Loop](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-human-in-the-loop)

    *   [9.8](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.8).[Tool-to-Service Access](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-tool-to-service-access)

    *   [9.9](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.9).[Privacy Considerations](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-privacy-considerations)

    *   [9.10](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.10).[OAuth 2.0 Discovery in Dynamic Environments](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-oauth-20-discovery-in-dynam)

        *   [9.10.1](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.10.1).[Authorization Server Capability Discovery](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-authorization-server-capabi)

        *   [9.10.2](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.10.2).[Protected Resource Capability Discovery](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-protected-resource-capabili)

        *   [9.10.3](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.10.3).[Client Capability Discovery](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-client-capability-discovery)

*   [10](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-10).[Agent Monitoring, Observability and Remediation](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-agent-monitoring-observabil)

*   [11](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-11).[Agent Authentication and Authorization Policy](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-agent-authentication-and-au)

*   [12](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-12).[Agent Compliance](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-agent-compliance)

*   [13](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-13).[Security Considerations](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-security-considerations)

*   [14](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-14).[Privacy Considerations](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-privacy-considerations-2)

*   [15](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-15).[IANA Considerations](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-iana-considerations)

*   [16](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-16).[Acknowledgments](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-acknowledgments)

*   [17](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-17).[References](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-references)

    *   [17.1](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-17.1).[Normative References](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-normative-references)

    *   [17.2](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-17.2).[Informative References](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-informative-references)

*   [Appendix A](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#appendix-A).[Document History](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-document-history)

*   [](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#appendix-B)[Authors' Addresses](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-authors-addresses)

## [1.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-1)[Introduction](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-introduction)

The rapid emergence of AI agents as autonomous workloads has sparked considerable innovation in authentication and authorization approaches. However, many of these efforts develop solutions in isolation, often reinventing existing mechanisms unaware of applicable prior art. This fragmentation risks creating incompatible implementations, duplicated development effort, and missed opportunities to leverage decades of established identity and authorization standards.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-1-1)

This document aims to help close that gap by providing a comprehensive model demonstrating how existing, well-established standards and some emergent specifications can be composed and applied to solve agent authentication and authorization challenges. Rather than proposing new protocols, this work focuses on integrating proven standards into a coherent framework tailored to the specific requirements of AI agent workloads.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-1-2)

By doing so, this document serves two complementary goals:[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-1-3)

1.   **Consolidation of prior art**: It establishes a baseline by showing how existing standards address the core identity, authentication, authorization, monitoring and observability needs of agent-based systems. Implementers and standards developers can reference this framework to avoid redundant work and ensure interoperability.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-1-4.1.1)

2.   **Foundation for future work**: As the agent ecosystem matures, having such a framework aids in identifying gaps and clarifies where extensions or profiles of existing standards are needed. This provides a foundation for more focused standardization efforts in areas needing novel work rather than variations of existing approaches.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-1-4.2.1)

## [2.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-2)[Conventions and Definitions](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-conventions-and-definitions)

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 [[RFC2119](https://www.rfc-editor.org/rfc/rfc2119)][[RFC8174](https://www.rfc-editor.org/rfc/rfc8174)] when, and only when, they appear in all capitals, as shown here.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-2-1)

## [3.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-3)[Agents are workloads](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-agents-are-workloads)

An Agent is a workload that iteratively interacts with a Large Language Model (LLM) and a set of Tools, Services and Resources. An agent performs its operations until a terminating condition, determined either by the LLM or by the agent's internal logic, is reached. It may receive input from a user, or act autonomously. [Figure 1](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#fig-ai-agent-workload) shows a conceptual model of the AI Agent as a workload and illustrates the high-level interaction model between the User or System, the AI Agent, the Large Language Model (LLM), Tools, Services, and Resources.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-3-1)

In this document, Tools, Services, and Resources are treated as a single category of external endpoints that an agent invokes or interacts with to complete a task. Communication within or between Tools, Services, and Resources is out of scope.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-3-2)

[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-3-3.1.1)

[Figure 1](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#figure-1): [AI Agent as a Workload](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-ai-agent-as-a-workload)

1.   Optional: The User or System (e.g. a batch job or another Agent) provides an initial request or instruction to the AI Agent.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-3-4.1.1)

2.   The AI Agent provides the available context to the LLM. Context is implementation, and deployment, specific and may include User or System input, system prompts, Tool descriptions, prior Tool, Service and Resource outputs, and other relevant state.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-3-4.2.1)

3.   The LLM returns output to the AI Agent facilitating selection of Tools, Services or Resources to invoke.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-3-4.3.1)

4.   The AI Agent invokes one or more external endpoints of selected Tools, Services or Resources. A Tool endpoint may itself be implemented by another AI agent.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-3-4.4.1)

5.   The external endpoint of the Tools, Services or Resources returns a result of the operation to the AI Agent, which may send the information as additional context to the Large Language Model, repeating steps 2-5 until the exit condition is reached and the task is completed.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-3-4.5.1)

6.   Optional: Once the exit condition is reached in step 5, the AI Agent may return a response to the User or System. The AI Agent may also return intermediate results or request additional input.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-3-4.6.1)

As shown in [Figure 1](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#fig-ai-agent-workload), the AI agent is a workload that needs an identifier and credentials so it can be authenticated by the Tools, Services, Resources, Large Language Model, System and the User (via the underlying operating system or platform, similar to existing applications and services). Once authenticated, these parties determine if the AI Agent is authorized to access the requested Large Language Model, Tools, Services or Resources. If the AI Agent is acting on behalf of a User or System, the User or System needs to delegate authority to the AI Agent, and the User or System context is preserved and used as input to authorization decisions and recorded in audit trails.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-3-5)

This document describes how AI Agents should leverage existing standards defined by SPIFFE [[SPIFFE](https://spiffe.io/docs/latest/spiffe-about/overview/)], WIMSE, OAuth and OpenID SSF [[SSF](https://openid.net/specs/openid-sharedsignals-framework-1_0-final.html)].[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-3-6)

## [4.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-4)[Agent Identity Management System](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-agent-identity-management-s)

This document defines the term Agent Identity Management System (AIMS) as a conceptual model describing the set of functions required to establish, maintain, and evaluate the identity and permissions of an agent workload. AIMS does not refer to a single product, protocol, or deployment architecture. AIMS may be implemented by one component or distributed across multiple systems (such as identity providers, provisioning services, authorization servers, policy engines, and runtime enforcement points).[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-4-1)

An Agent Identity Management System ensures that the right Agent has access to the right resources and tools at the right time for the right reason. An Agent identity management system depends on the following components to achieve its goals:[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-4-2)

*   **Agent Identifiers:** Unique identifier assigned to every Agent.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-4-3.1.1)

*   **Agent Credentials:** Cryptographic binding between the Agent Identifier and attributes of the Agent.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-4-3.2.1)

*   **Agent Credential Provisioning:** The mechanism for provisioning credentials to the agent at runtime.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-4-3.3.1)

*   **Agent Authentication:** Protocols and mechanisms used by the Agent to authenticate itself to Large Language Models or Tools (resource or server) in the system.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-4-3.4.1)

*   **Agent Authorization:** Protocols and systems used to determine if an Agent is allowed to access a Large Language Model or Tool (resource or server).[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-4-3.5.1)

*   **Agent Observability and Remediation:** Protocols and mechanisms to dynamically modify the authorization decisions based on observed behavior and system state.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-4-3.6.1)

*   **Agent Authentication and Authorization Policy:** The configuration and rules for each of the Agent Identity Management System.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-4-3.7.1)

*   **Agent Compliance:** Measurement of the state and functioning of the system against the stated policies.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-4-3.8.1)

The components form a logical stack in which higher layers depend on guarantees provided by lower layers, as illustrated in [Figure 2](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#fig-agent-identity-management-system).[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-4-4)

[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-4-5.1.1)

[Figure 2](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#figure-2): [Agent Identity Management System](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-agent-identity-management-sy)

## [5.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-5)[Agent Identifier](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-agent-identifier)

Agents MUST be uniquely identified in order to support authentication, authorization, auditing, and delegation.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-5-1)

The Workload Identity in Multi-System Environments (WIMSE) identifier as defined by [[WIMSE-ID](https://datatracker.ietf.org/doc/html/draft-ietf-wimse-identifier-02)] is the primary identifier for agents in this framework.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-5-2)

A WIMSE identifier is a URI that uniquely identifies a workload within a trust domain. Authorization decisions, delegation semantics, and audit records rely on this identifier remaining stable for the lifetime of the workload identity.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-5-3)

The Secure Production Identity Framework for Everyone ([[SPIFFE](https://spiffe.io/docs/latest/spiffe-about/overview/)]) identifier is a widely deployed and operationally mature implementation of the WIMSE identifier model. A SPIFFE identifier ([[SPIFFE-ID](https://github.com/spiffe/spiffe/blob/main/standards/SPIFFE-ID.md)]) is a URI in the form of `spiffe://<trust-domain>/<path>` that uniquely identifies a workload within a trust domain.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-5-4)

An agent participating in this framework MUST be assigned exactly one WIMSE identifier, which MAY be a SPIFFE ID.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-5-5)

## [6.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-6)[Agent Credentials](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-agent-credentials)

Agents MUST possess credentials that provide a cryptographic binding to the agent identifier. These credentials are considered primary credentials that are provisioned at runtime. An identifier alone is insufficient unless it can be verified to be controlled by the communicating agent through a cryptographic binding.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-6-1)

WIMSE credentials ([[WIMSE-CRED](https://datatracker.ietf.org/doc/html/draft-ietf-wimse-workload-creds-01)]) are defined as a profile of X.509 certificates and Workload Identity Tokens (WITs), while SPIFFE defines SPIFFE Verified ID (SVID) profiles of JSON Web Token (JWT-SVID), X.509 certificates (X.509-SVID) and WIMSE Workload Identity Tokens (WIT-SVID). SPIFFE SVID credentials are compatible with WIMSE defined credentials. The choice of an appropriate format depends on the trust model and integration requirements.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-6-2)

Agent credentials SHOULD be short-lived to minimize the risk of credential theft, MUST include an explicit expiration time after which it is no longer accepted, and MAY carry additional attributes relevant to the agent (for example trust domain, attestation evidence, or workload metadata).[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-6-3)

Deployments can improve the assurance of agent identity by protecting private keys using hardware-backed or isolated cryptographic storage such as TPMs, secure enclaves, or platform security modules when such capabilities are available. These mechanisms reduce key exfiltration risk but are not required for interoperability.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-6-4)

In some cases, agents MAY need secondary credentials to access a proprietary or legacy environment that is not compatible with the X.509, JWT or WIT it is provisioned with. In these cases an agent MAY exchange their primary credentials through a credential exchange mechanisms (e.g., OAuth 2.0 Token Exchange [[OAUTH-TOKEN-EXCHANGE](https://www.rfc-editor.org/rfc/rfc8693)], Transaction Tokens [[OAUTH-TXN-TOKENS](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-transaction-tokens-08)] or Workload Identity Federation). This allows an agent to obtain a credential targeted to a specific environment by leveraging the primary credential in its possession.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-6-5)

**Note**: Static API keys are an antipattern for agent identity. They are bearer artifacts that are not cryptographically bound, do not convey identity, are typically long-lived and are operationally difficult to rotate, making them unsuitable for secure agent authentication or authorization.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-6-6)

## [7.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-7)[Agent Credential Provisioning](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-agent-credential-provisioni)

Agent credential provisioning refers to the runtime issuance, renewal, lifecycle state and rotation of the credentials an agent uses to authenticate and authorize itself to other agents. Agents may be provisioned with one or more credential types as described in [Section 6](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#agent_credentials). Unlike static secrets, agent credentials are provisioned dynamically and are intentionally short-lived, eliminating the operational burden of manual expiration management and reducing the impact of credential compromise.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-7-1)

Credential provisioning is also the assessment point to confirm that the Agent and its runtime environment satisfy the posture requirements. In this document, posture assessment refers to the evaluation of signals about the Agent, its software, deployment context, runtime environment, and operational state. These signals can influence whether a credential is issued, which identifier is bound to the credential, what type of credential is issued, what attributes are included in the credential, and how long the credential remains valid.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-7-2)

Posture assessment mechanisms are deployment and risk specific. They may include hardware-backed evidence, trusted execution environment (TEE) evidence, software integrity measurements, supply-chain provenance, platform or orchestration-layer metadata, workload placement information, configuration state, operator assertions, or other environment-specific signals. Depending on the risk involved, a single signal may be sufficient, while higher-risk deployments may require multiple independent signals before credentials are issued or renewed.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-7-3)

Deployed workload identity systems commonly perform some form of posture assessment as part of credential provisioning. For example, SPIFFE implementations can evaluate platform and environment-specific information about a workload before binding it to a SPIFFE identifier and issuing an SVID. At a high level, a provisioning component gathers workload and execution context signals, verifies them according to local policy, and, if verification succeeds, issues short-lived credentials for subsequent authentication and authorization.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-7-4)

An Agent Identity Management System may incorporate multiple posture assessment mechanisms and implementations. The selection of mechanisms depends on deployment constraints, such as the underlying platform, available identity signals, and desired level of trust assurance. This document does not require any particular posture assessment mechanism, evidence format, or verifier architecture.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-7-5)

Agent credential provisioning must operate autonomously, scale to high-churn environments, and integrate closely with the posture assessment mechanisms used to establish trust in the Agent at each issuance or rotation event.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-7-6)

Agent credential provisioning typically includes two phases:[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-7-7)

1.   **Initial Provisioning**: The process by which an agent first acquires a credential bound to its identity. This often occurs immediately after deployment or instantiation and is based on verified properties of the agent (e.g., deployment context, posture assessment results, or orchestration metadata).[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-7-8.1.1)

2.   **Rotation/Renewal**: The automatic refresh of short-lived credentials before expiration. Continuous rotation ensures that credentials remain valid only for the minimum necessary time and that authorization state reflects current operational conditions.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-7-8.2.1)

The use of short-lived credentials provides a significant improvement in the risk profile and risk of credential exposure. It provides an alternative to explicit revocation mechanisms and simplifies lifecycle management in large, automated environments while removing the risks of downtime as a result of credential expiry.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-7-9)

Deployed frameworks such as [[SPIFFE](https://spiffe.io/docs/latest/spiffe-about/overview/)] provide proven mechanisms for automated, short-lived credential provisioning at runtime. In addition to issuing short-lived credentials, [[SPIFFE](https://spiffe.io/docs/latest/spiffe-about/overview/)] also provisions ephemeral cryptographic key material bound to each credential, further reducing the risks associated with compromising long-lived keys.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-7-10)

## [8.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-8)[Agent Authentication](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-agent-authentication)

Agents may authenticate using a variety of mechanisms, depending on the credentials they possess, the protocols supported in the deployment environment, and the risk profile of the application. As described in the WIMSE Architecture [[WIMSE-ARCH](https://datatracker.ietf.org/doc/html/draft-ietf-wimse-arch-07)], authentication can occur at either the transport layer or the application layer, and many deployments rely on a combination of both.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-8-1)

### [8.1.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-8.1)[Transport Layer Authentication](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-transport-layer-authenticat)

Transport-layer authentication establishes trust during the establishment of a secure transport channel. The most common mechanism used by agents is mutually-authenticated TLS (mTLS), in which both endpoints present X.509-based credentials and perform a bidirectional certificate exchange as part of the TLS negotiation. When paired with short-lived workload identities, such as those issued by SPIFFE or WIMSE, mTLS provides strong channel binding and cryptographic proof of control over the agent’s private key.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-8.1-1)

mTLS is particularly well-suited for environments where transport-level protection, peer authentication, and ephemeral workload identity are jointly required. It also simplifies authorization decisions by enabling agents to associate application-layer requests with an authenticated transport identity. One example of this is the use of mTLS in service mesh architectures such as Istio or LinkerD.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-8.1-2)

#### [8.1.1.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-8.1.1)[Limitations](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-limitations)

There are scenarios where transport-layer authentication is not desirable or cannot be relied upon. In architectures involving intermediaries, such as proxies, API gateways, service meshes, load balancers, or protocol translators, TLS sessions are often terminated and re-established, breaking the end-to-end continuity of transport-layer identity. Similarly, some deployment models (such as serverless platforms, multi-tenant edge environments, or cross-domain topologies) may obscure or abstract identity presented at the transport layer, making it difficult to bind application-layer actions to a credential presented at the transport layer. In these cases, application-layer authentication provides a more robust and portable mechanism for expressing agent identity and conveying attestation or policy-relevant attributes.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-8.1.1-1)

### [8.2.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-8.2)[Application Layer Authentication](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-application-layer-authentic)

Application-layer authentication allows agents to authenticate independently of the underlying transport. This enables end-to-end identity preservation even when requests traverse proxies, load balancers, or protocol translation layers.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-8.2-1)

The WIMSE working group defines WIMSE Proof Tokens and HTTP Message Signatures as authentication mechanisms that may be used by agents.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-8.2-2)

#### [8.2.1.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-8.2.1)[WIMSE Proof Tokens (WPTs)](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-wimse-proof-tokens-wpts)

WIMSE Workload Proof Tokens (WPTs, [[WIMSE-WPT](https://datatracker.ietf.org/doc/html/draft-ietf-wimse-wpt-01)]) are a protocol-independent, application-layer mechanism for proving possession of the private key associated with a Workload Identity Token (WIT). WPTs are generated by the agent, using the private key matching the public key in the WIT. A WPT is defined as a signed JSON Web Token (JWT) that binds an agent’s authentication to a specific message context, for example, an HTTP request, thereby providing proof of possession rather than relying on bearer semantics.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-8.2.1-1)

WPTs are designed to work alongside WITs [[WIMSE-CRED](https://datatracker.ietf.org/doc/html/draft-ietf-wimse-workload-creds-01)] and are typically short-lived to reduce the window for replay attacks. They carry claims such as audience (aud), expiration (exp), a unique token identifier (jti), and a hash of the associated WIT (wth). A WPT may also include hashes of other related tokens (e.g., a Transaction Token) to bind the authentication contexts to specific transaction or authorizations details.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-8.2.1-2)

Although the draft currently defines a protocol binding for HTTP (via a Workload-Proof-Token header), the core format is protocol-agnostic, making it applicable to other protocols. Its JWT structure and claims model allow WPTs to be bound to different protocols and transports, including asynchronous or non-HTTP messaging systems such as Kafka and gRPC, or other future protocol bindings. This design enables receiving systems to verify identity, key possession, and message binding at the application layer even in environments where transport-layer identity (e.g., mutual TLS) is insufficient or unavailable.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-8.2.1-3)

#### [8.2.2.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-8.2.2)[HTTP Message Signatures](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-http-message-signatures)

The WIMSE Workload-to-Workload Authentication with HTTP Signatures specification [[WIMSE-HTTPSIG](https://datatracker.ietf.org/doc/html/draft-ietf-wimse-http-signature-03)] defines an application-layer authentication profile built on the HTTP Message Signatures standard [[HTTP-SIG](https://www.rfc-editor.org/rfc/rfc9421)]. It is one of the mechanisms WIMSE defines for authenticating workloads in HTTP-based interactions where transport-layer protections may be insufficient or unavailable. The protocol combines a workload's Workload Identity Token (WIT) (which binds the agent's identity to a public key) with HTTP Message Signatures (using the corresponding private key), thereby providing proof of possession and message integrity for individual HTTP requests and responses. This approach ensures end-to-end authentication and integrity even when traffic traverses intermediaries such as TLS proxies or load balancers that break transport-layer identity continuity. The profile mandates signing of some request components (e.g., method, request-target, content digest, and the WIT itself) and supports optional response signing. Note that @request-target covers only the request-target string (typically path + query) and not the method, scheme, or authority; those are only protected if separately covered (e.g., @method, @scheme, @authority).[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-8.2.2-1)

#### [8.2.3.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-8.2.3)[Limitations](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-limitations-2)

Unlike transport-layer authentication, application-layer authentication does not inherently provide channel binding to the underlying secure transport. As a result, implementations MUST consider the risk of message relay or replay if tokens or signed messages are accepted outside their intended context. Deployments typically mitigate these risks through short token lifetimes, audience restrictions, nonce or unique identifier checks, and binding authentication to specific requests or transaction parameters.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-8.2.3-1)

## [9.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9)[Agent Authorization](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-agent-authorization)

Agents act on behalf of a user, a system, or on their own behalf as shown in [Figure 1](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#fig-ai-agent-workload) and need to obtain authorization when interacting with protected resources.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9-1)

### [9.1.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.1)[Agent Mission](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-agent-mission)

An Agent receives a Mission from a User, a System, or another Agent. The Mission is the task or objective the Agent will pursue. It is typically expressed in natural language and may require decomposition as it is mapped from a broad objective into specific resource requirements and corresponding access requests. The translation of a mission into authorization requirements is expected to occur as a planning step before the Agent requests authorization. The process through which the mission is translated into authorization requriements is out of scope of this specification. Once the required resources and their associated authorization requirements are determined, the Agent SHOULD use the mechanisms described in this section to obtain access.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.1-1)

### [9.2.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.2)[Leverage OAuth 2.0 as a Delegation Authorization Framework](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-leverage-oauth-20-as-a-dele)

The widely deployed OAuth 2.0 Authorization Framework [[OAUTH-FRAMEWORK](https://www.rfc-editor.org/rfc/rfc6749)] is a mechanism for delegated authorization that enables an Agent to obtain limited access to a protected resource (e.g., a service or API), intermediated by an Authorization Server, often with the explicit approval of the authenticated User. An Agent uses OAuth 2.0-based mechanisms to obtain authorization from a User, a System, or on its own behalf. OAuth 2.0 defines a wide range of authorization grant flows that supports these scenarios. In these Oauth 2.0 flows, an Agent acts as an OAuth 2.0 Client to an OAuth 2.0 Authorization Server, which receives the request, evaluate the authorization policy and returns an access token, which the Agent presents to the Resource Server (i.e. the protected resources such as the LLM or Tools in [Figure 1](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#fig-ai-agent-workload), which can evaluate its authorization policy and complete the request.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.2-1)

### [9.3.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.3)[Use of OAuth 2.0 Access Tokens](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-use-of-oauth-20-access-toke)

An OAuth access token represents the authorization granted to the Agent. In many deployments, access tokens are structured as JSON Web Tokens (JWTs) [[OAUTH-ACCESSTOKEN-JWT](https://www.rfc-editor.org/rfc/rfc9068)], which include claims such as 'client_id', 'sub', 'aud', 'scope', and other attributes relevant to authorization. The access token includes the Agent identity as the 'client_id' claim as defined in [Section 2.2](https://rfc-editor.org/rfc/rfc9068#section-2.2) of [[OAUTH-ACCESSTOKEN-JWT](https://www.rfc-editor.org/rfc/rfc9068)].[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.3-1)

When the Agent is acting on-behalf of another User or System, the User or System identifier is conveyed in the 'sub' claim as defined in [Section 2.2](https://rfc-editor.org/rfc/rfc9068#section-2.2) of [[OAUTH-ACCESSTOKEN-JWT](https://www.rfc-editor.org/rfc/rfc9068)]. These identifiers MUST be used by resource servers protected by the OAuth 2.0 authorization service, along with other claims in the access token, to determine if access to a resource should be allowed. The access token typically includes additional claims to convey contextual, attestation-derived, or policy-related information that enables fine-grained access control. The resource server uses the access token and the information it contains along with other authorization systems (e.g. policy based, attribute based or role based authorization systems) when enforcing access control. JWT access tokens can be validated directly by resource servers while other formats that are opaque to the resource server can be validated through a mechanism that calls back to the authorization server (the mechanism is called introspection despite the word having nearly the opposite meaning). This framework supports both models and does not require a specific token format, provided that equivalent authorization semantics are maintained.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.3-2)

A resource server in receipt of tokens opaque to it are able to obtain authorization and other information from the token through OAuth 2.0 Token Introspection [[OAUTH-TOKEN-INTROSPECTION](https://www.rfc-editor.org/rfc/rfc7662)]. The introspection response provides the active state of the token and associated authorization attributes equivalent to those conveyed in structured tokens.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.3-3)

### [9.4.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.4)[Obtaining an OAuth 2.0 Access Token](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-obtaining-an-oauth-20-acces)

OAuth 2.0 defines a number authorization grant flows in support of different authorization scenarios. The appropriate flow depends on the specific authorization scenario and the nature of User involvement. The following subsections describe the most relevant flows for Agent authorization.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.4-1)

#### [9.4.1.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.4.1)[User Delegates Authorization](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-user-delegates-authorizatio)

When a User delegates authorization to an Agent, the Agent SHOULD obtain an access token using the Authorization Code Grant as described in [Section 4.1](https://rfc-editor.org/rfc/rfc6749#section-4.1) of [[OAUTH-FRAMEWORK](https://www.rfc-editor.org/rfc/rfc6749)]. This redirection-based flow involves an interactive authorization process, typically in a web browser, in which the user authenticates to the authorization server and explicitly approves the requested access. Users SHOULD be authenticated using phishing-resistant authentication mechanisms such as a passkey. Once the user has approved the request, the authorization server returns an authorization code to the Agent via the redirect.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.4.1-1)

The Agent, acting as an OAuth client, then makes a token request to the authorization server to redeem the authorization code for an access token. When making this token request, the Agent authenticates itself directly to the authorization server using the credentials described in [Section 6](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#agent_credentials) with a compatible OAuth client authentication mechanism, and not with the use of static, long-lived client secrets. Compatible OAuth client authentication mechanisms are defined in [[OAUTH-CLIENTAUTH-JWT](https://www.rfc-editor.org/rfc/rfc7523)], [[OAUTH-CLIENTAUTH-MTLS](https://www.rfc-editor.org/rfc/rfc8705)] and [[OAUTH-SPIFFE](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-spiffe-client-auth-01)]. The OAuth client authentication step is distinct from, and occurs after, the user authentication and approval described above. The resulting access token reflects the authorization delegated to the Agent by the User and can be used by the Agent to access resources on behalf of the user. The use of OAuth negates the need for the Agent to have access to a User's credentials when accessing a resource on the User's behalf.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.4.1-2)

#### [9.4.2.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.4.2)[Agent Obtains Own Authorization](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-agent-obtains-own-authoriza)

Agents obtaining access tokens on their own behalf can use the Client Credentials Grant as described in [Section 4.4](https://rfc-editor.org/rfc/rfc6749#section-4.4) of [[OAUTH-FRAMEWORK](https://www.rfc-editor.org/rfc/rfc6749)] or the JWT Authorization Grant as described in [Section 2.1](https://rfc-editor.org/rfc/rfc7523#section-2.1) of [[OAUTH-CLIENTAUTH-JWT](https://www.rfc-editor.org/rfc/rfc7523)]. When using the Client Credentials Grant, the Agent authenticates itself using the credentials described in [Section 6](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#agent_credentials) with a compatible OAuth client authentication mechanism listed in previous section, and not with the use of static, long-lived client secrets. When using the JWT Authorization Grant, the Agent will be identified in the subject of the JWT assertion.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.4.2-1)

#### [9.4.3.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.4.3)[Agents Accessed by Systems or Other Agents](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-agents-accessed-by-systems-)

Agents themselves can act in the role of an OAuth protected resource and be invoked by a System (e.g. a batch job or another Agent). The System obtains an access token using an appropriate mechanism and then invokes the Agent presenting the access token.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.4.3-1)

#### [9.4.4.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.4.4)[OAuth 2.0 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-oauth-20-security-best-prac)

The Best Current Practice for OAuth 2.0 Security as described in [[OAUTH-BCP](https://www.rfc-editor.org/rfc/rfc9700)] are applicable when requesting and using access tokens.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.4.4-1)

### [9.5.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.5)[Risk Reduction with Transaction Tokens](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-risk-reduction-with-transac)

Resources servers, whether they are LLMs, Tools or Agents (in the Agent-to-Agent case) may be composed of multiple microservices that are invoked to complete a request. The access tokens presented to the Agent, LLM or Tools can typically be used with multiple transactions and consequently have broader scope than needed to complete any specific transaction. Passing the access token from one microservice to another within an invoked Agent, LLM or the Tools increases the risk of token theft and replay attacks. For example, an attacker may discover and access token passed between microservices in a log file or crash dump, exfiltrate it, and use it to invoke a new transaction with different parameters (e.g. increase the transaction amount, or invoke an unrelated call as part of executing a lateral move).[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.5-1)

To avoid passing access tokens between microservices, the Agent, LLM or Tools can exchange the received access token for a transaction token, as defined in the Transaction Token specification [[OAUTH-TXN-TOKENS](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-transaction-tokens-08)]. The transaction token allows for identity and authorization information to be passed along the internal call chain of microservices. The transaction token issuer enriches the transaction token with context of the caller that presented the access token (e.g. IP address, etc.), transaction context (transaction amount), identity information and a unique transaction identifier. This results in a downscoped token that is bound to a specific transaction and cannot be used as an access token, with another transaction, or within the same transaction with modified transaction details (e.g. change in transaction amount). Transaction tokens are typically short-lived, further limiting the risk in case they are obtained by an attacker by limiting the time window during which these tokens will be accepted.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.5-2)

A transaction token MAY be used to obtain an access token to call another service (e.g. another Agent, Tool or LLM) by using OAuth 2.0 Token Exchange as defined in [[OAUTH-TOKEN-EXCHANGE](https://www.rfc-editor.org/rfc/rfc8693)].[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.5-3)

### [9.6.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.6)[Cross Domain Access](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-cross-domain-access)

Agents often require access to resources that are protected by different OAuth 2.0 authorization servers. When the components in [Figure 1](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#fig-ai-agent-workload) are protected by different logical authorization servers, an Agent SHOULD use OAuth Identity and Authorization Chaining Across Domains as defined in ([[OAUTH-ID-CHAIN](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-identity-chaining-12)]), or a derived specification such as the Identity Assertion JWT Authorization Grant [[OAUTH-JWT-ASSERTION](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-identity-assertion-authz-grant-04)], to obtain an access token from the relevant authorization servers.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.6-1)

When using OAuth Identity and Authorization Chaining Across Domains ([[OAUTH-ID-CHAIN](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-identity-chaining-12)]), an Agent SHOULD use the access token or transaction token it received to obtain a JWT authorization grant as described in [Section 2.3](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-identity-chaining-12#section-2.3) of [[OAUTH-ID-CHAIN](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-identity-chaining-12)] and then use the JWT authorization grant it receives to obtain an access token for the resource it is trying to access as defined in [Section 2.4](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-identity-chaining-12#section-2.4) of [[OAUTH-ID-CHAIN](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-identity-chaining-12)].[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.6-2)

When using the Identity Assertion JWT Authorization Grant [[OAUTH-JWT-ASSERTION](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-identity-assertion-authz-grant-04)], the identity assertion (e.g. the OpenID Connect ID Token or SAML assertion) for the target end-user is used to obtain a JWT assertion as described in [Section 4.3](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-identity-assertion-authz-grant-04#section-4.3) of [[OAUTH-JWT-ASSERTION](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-identity-assertion-authz-grant-04)], which is then used to obtain an access token as described in [Section 4.4](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-identity-assertion-authz-grant-04#section-4.4) of [[OAUTH-JWT-ASSERTION](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-identity-assertion-authz-grant-04)].[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.6-3)

OAuth Identity and Authorization Chaining Across Domains ([[OAUTH-ID-CHAIN](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-identity-chaining-12)]) provides a general mechanism for obtaining cross-domain access that can be used whether an identity assertion like a SAML or OpenID Connect token is available or not. The Identity Assertion JWT Authorization Grant [[OAUTH-JWT-ASSERTION](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-identity-assertion-authz-grant-04)] is optimized for cases where an identity assertion like a SAML or OpenID Connect token is available from an identity provider that is trusted by all the OAuth authorization servers as it removes the need for the user to re-authenticate. This is typically used within enterprise deployments to simplify authorization delegation for multiple software-as-a-service offerings.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.6-4)

### [9.7.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.7)[Human in the Loop](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-human-in-the-loop)

An OAuth authorization server MAY conclude that the level of access requested by an Agent requires explicit user confirmation. In such cases the authorization server SHOULD either decline the request or obtain additional authorization from the User. An Agent, acting as an OAuth client, may use the OpenID Client Initiated Backchannel Authentication (CIBA) protocol. This triggers an out-of-band interaction allowing the user to approve or deny the requested operation without exposing credentials to the agent (for example a push notification requesting the user to approve a request through an authenticator application on their mobile device).[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.7-1)

Interactive agent frameworks may also solicit user confirmation directly during task execution (for example tool invocation approval or parameter confirmation). Such interactions do not by themselves constitute authorization and MUST be bound to a verifiable authorization grant issued by the authorization server. The agent SHOULD therefore translate user confirmation into an OAuth authorization event (e.g., step-up authorization via CIBA) before accessing protected resources.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.7-2)

This model aligns with user-solicitation patterns such as those described by the Model Context Protocol ([[MCP](https://modelcontextprotocol.io/specification)]), where an agent pauses execution and requests user confirmation before performing sensitive actions. The final authorization decision remains with the authorization server, and the agent MUST NOT treat local UI confirmation alone as sufficient authorization.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.7-3)

**Note:** Additional specification or design work may be needed to define how out-of-band interactions with the User occur at different stages of execution. CIBA itself only accounts for client initiation, which doesn't map well to cases that envision the need for User confirmation to occur mid-execution.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.7-4)

### [9.8.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.8)[Tool-to-Service Access](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-tool-to-service-access)

Tools expose interfaces to underlying services and resources. Access to the Tools can be controlled by OAuth and augmented by policy, attribute or role based authorization systems (amongst others). If the Tools are implemented as one or more microservices, it should use transaction tokens to reduce risk as described in [Section 9.5](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#txn-tokens-risk-reduction) to avoid passing access tokens around within the Tool implementation.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.8-1)

Access from the Tools to the resources and services MAY be controlled through a variety of authorization mechanisms, including OAuth. If access is controlled through OAuth, the Tools can use OAuth 2.0 Token Exchange as defined in [[OAUTH-TOKEN-EXCHANGE](https://www.rfc-editor.org/rfc/rfc8693)] to exchange the access token it received for a new access token to access the resource or service in question. When the Tool needs access to a resource protected by an authorization server other than the Tool's own authorization server, the OAuth Identity and Authorization Chaining Across Domains ([[OAUTH-ID-CHAIN](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-identity-chaining-12)]) can be used to obtain an access token from the authorization server protecting that resource.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.8-2)

**Note:** It is an anti-pattern for Tools to forward access tokens it received from the Agent to Services or Resources. It increases the risk of credential theft and lateral attacks.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.8-3)

### [9.9.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.9)[Privacy Considerations](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-privacy-considerations)

Authorization tokens may contain user identifiers, agent identifiers, audience restrictions, transaction details, and contextual attributes. Deployments SHOULD minimize disclosure of personally identifiable or sensitive information in tokens and prefer audience-restricted and short-lived tokens. Where possible, opaque tokens with introspection SHOULD be preferred when claim minimization is required.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.9-1)

Agents SHOULD request only the minimum scopes and authorization details necessary to complete a task. Resource servers SHOULD avoid logging full tokens and instead log token identifiers or hashes. When authorization context is propagated across services, derived or down-scoped tokens (such as transaction tokens) SHOULD be used to reduce correlation and replay risk.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.9-2)

Implementations MUST ensure that user identity information delegated to agents is not exposed to unrelated services and that cross-domain authorization exchanges only disclose information required for the target authorization decision.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.9-3)

### [9.10.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.10)[OAuth 2.0 Discovery in Dynamic Environments](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-oauth-20-discovery-in-dynam)

In dynamic Agent deployments (e.g., ephemeral workloads, multi-tenant services, and frequently changing endpoint topology), Agents and other participants MAY use OAuth discovery mechanisms to reduce static configuration and to bind runtime decisions to verifiable metadata.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.10-1)

#### [9.10.1.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.10.1)[Authorization Server Capability Discovery](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-authorization-server-capabi)

An Agent that needs to obtain tokens can discover authorization server endpoints and capabilities using OAuth 2.0 Authorization Server Metadata [[OAUTH-SERVER-METADATA](https://www.rfc-editor.org/rfc/rfc8414)] and/or OpenID Connect Discovery [[OpenIDConnect.Discovery](https://openid.net/specs/openid-connect-discovery-1_0-final.html)]. This allows the Agent to learn the authorization server issuer identifier, authorization and token endpoints, supported grant types, client authentication methods, signing keys (via jwks_uri), and other relevant capabilities without preconfiguring them.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.10.1-1)

#### [9.10.2.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.10.2)[Protected Resource Capability Discovery](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-protected-resource-capabili)

When an Agent is invoking a Tool, the Agent MAY use OAuth 2.0 Protected Resource Metadata [[OAUTH-RESOURCE-METADATA](https://www.rfc-editor.org/rfc/rfc9728)] to discover how the resource is protected, including the resource identifier and the applicable Authorization Server(s) that protects Tool access. This enables an Agent to select the correct issuer/audience and token acquisition flow at runtime, even when resources are deployed or moved dynamically.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.10.2-1)

A Tool that attempts to access and OAuth protected resource MAY use OAuth 2.0 Protected Resource Metadata [[OAUTH-RESOURCE-METADATA](https://www.rfc-editor.org/rfc/rfc9728)] in a similar way as an Agent. Similarly, a System may use [[OAUTH-RESOURCE-METADATA](https://www.rfc-editor.org/rfc/rfc9728)] when accessing an Agent.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.10.2-2)

#### [9.10.3.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.10.3)[Client Capability Discovery](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-client-capability-discovery)

Other actors (e.g., Authorization Servers, registrars, or policy systems) may need to learn about any entities (System, Agent, Tool) that acts as OAuth clients. Where supported, they MAY use Client ID Metadata Documents [[OAUTH-CLIENT-METADATA](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-client-id-metadata-document-01)], which allow a client to host its metadata at a URL-valued client_id so that the relying party can retrieve client properties (e.g., redirect URIs, display information, and other registered client metadata) without prior bilateral registration.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.10.3-1)

As an alternative, entities acting as OAuth clients MAY register their capabilities with authorization servers as defined in the OAuth 2.0 Dynamic Client Registration Protocol [[OAUTH-REGISTRATION](https://www.rfc-editor.org/rfc/rfc7591)].[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-9.10.3-2)

## [11.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-11)[Agent Authentication and Authorization Policy](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-agent-authentication-and-au)

The configuration and runtime parameters for Agent Identifiers [Section 5](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#agent_identifiers), Agent Credentials [Section 6](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#agent_credentials), Agent Credential Provisioning [Section 7](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#agent_credential_provisioning), Agent Authentication [Section 8](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#agent_authentication), Agent Authorization [Section 9](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#agent_authorization) and Agent Monitoring, Observability and Remediation [Section 10](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#agent_monitoring_and_remediation) collectively constitute the authentication and authorization policy within which the Agent operates.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-11-1)

Because these parameters are highly deployment and risk-model-specific (and often reflect local governance, regulatory, and operational constraints), the policy model and document format are out of scope for this framework and are not recommended as a target for standardization within this specification. Implementations MAY represent policy in any suitable “policy-as-code” or configuration format (e.g., JSON/YAML), provided it is versioned, reviewable, and supports consistent evaluation across the components participating in the end-to-end flow.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-11-2)

## [12.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-12)[Agent Compliance](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-agent-compliance)

Compliance for Agent-based systems SHOULD be assessed by auditing observed behavior and recorded evidence (logs, signals, and authorization decisions) against the deployment’s Agent Authentication and Authorization Policy [Section 11](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#agent_auhtentication_and_authorization_policy). Since compliance criteria are specific to individual deployments, organizations, industries and jurisdictions, they are out of scope for this framework though implementers SHOULD ensure strong observability and accountable governance, subject to their specific business needs.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-12-1)

## [13.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-13)[Security Considerations](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-security-considerations)

This document composes existing specifications to enable authentication and authorization between AI agents. The security considerations of each referenced specification apply in full.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-13-1)

In addition to the guidance included in existing specifications, additional security best practices and profiles have been developed for the Oauth protocol famility. The OAuth 2.0 Security Best Current Practice [[OAUTH-BCP](https://www.rfc-editor.org/rfc/rfc9700)] which captures current guidance on threats and mitigations that have emerged since the original OAuth 2.0 specifications were published. The FAPI 2.0 Security Profile [[OpenIDConnect.FAPI](https://openid.net/specs/fapi-security-profile-2_0-final.html)] defines a high-assurance profile of OAuth 2.0 suitable for high security applications.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-13-2)

## [14.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-14)[Privacy Considerations](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-privacy-considerations-2)

This document composes existing specifications to enable authentication and authorization between AI agents.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-14-1)

In addition to the the privacy considerations in [Section 9.9](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#privacy), the privacy considerations in each referenced specification apply in full.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-14-2)

## [15.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-15)[IANA Considerations](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-iana-considerations)

This document has no IANA actions.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-15-1)

## [16.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-16)[Acknowledgments](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-acknowledgments)

The authors would like to thank:[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-16-1)

*   Sean O'Dell for providing valuable input and feedback on this work.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-16-2.1.1)

*   Karl McGuinness for his blog posts on mission shaping as a pre-cursor to authroization [[MissionShaping](https://notes.karlmcguinness.com/notes/the-mission-shaping-problem/)][¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-16-2.2.1)

## [17.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-17)[References](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-references)

### [17.1.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#section-17.1)[Normative References](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-normative-references)

[A2A]"Agent2Agent (A2A) Protocol", n.d., <[https://github.com/a2aproject/A2A](https://github.com/a2aproject/A2A)>. [ACP]"Agentic Commerce Protocol", n.d., <[https://www.agenticcommerce.dev/docs](https://www.agenticcommerce.dev/docs)>. [AP2]"Agent Payments Protocol (AP2)", n.d., <[https://github.com/google-agentic-commerce/AP2](https://github.com/google-agentic-commerce/AP2)>. [CAEP]"OpenID Continuous Access Evaluation Profile 1.0", n.d., <[https://openid.net/specs/openid-caep-1_0-final.html](https://openid.net/specs/openid-caep-1_0-final.html)>. [HTTP-SIG]Backman, A., Ed., Richer, J., Ed., and M. Sporny, "HTTP Message Signatures", RFC 9421, DOI 10.17487/RFC9421, February 2024, <[https://www.rfc-editor.org/rfc/rfc9421](https://www.rfc-editor.org/rfc/rfc9421)>. [MCP]"Model Context Protocol", n.d., <[https://modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification)>. [OAUTH-ACCESSTOKEN-JWT]Bertocci, V., "JSON Web Token (JWT) Profile for OAuth 2.0 Access Tokens", RFC 9068, DOI 10.17487/RFC9068, October 2021, <[https://www.rfc-editor.org/rfc/rfc9068](https://www.rfc-editor.org/rfc/rfc9068)>. [OAUTH-BCP]Lodderstedt, T., Bradley, J., Labunets, A., and D. Fett, "Best Current Practice for OAuth 2.0 Security", BCP 240, RFC 9700, DOI 10.17487/RFC9700, January 2025, <[https://www.rfc-editor.org/rfc/rfc9700](https://www.rfc-editor.org/rfc/rfc9700)>. [OAUTH-CLIENT-METADATA]Parecki, A. and E. Smith, "OAuth Client ID Metadata Document", Work in Progress, Internet-Draft, draft-ietf-oauth-client-id-metadata-document-01, 1 March 2026, <[https://datatracker.ietf.org/doc/html/draft-ietf-oauth-client-id-metadata-document-01](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-client-id-metadata-document-01)>. [OAUTH-CLIENTAUTH-JWT]Jones, M., Campbell, B., and C. Mortimore, "JSON Web Token (JWT) Profile for OAuth 2.0 Client Authentication and Authorization Grants", RFC 7523, DOI 10.17487/RFC7523, May 2015, <[https://www.rfc-editor.org/rfc/rfc7523](https://www.rfc-editor.org/rfc/rfc7523)>. [OAUTH-CLIENTAUTH-MTLS]Campbell, B., Bradley, J., Sakimura, N., and T. Lodderstedt, "OAuth 2.0 Mutual-TLS Client Authentication and Certificate-Bound Access Tokens", RFC 8705, DOI 10.17487/RFC8705, February 2020, <[https://www.rfc-editor.org/rfc/rfc8705](https://www.rfc-editor.org/rfc/rfc8705)>. [OAUTH-FRAMEWORK]Hardt, D., Ed., "The OAuth 2.0 Authorization Framework", RFC 6749, DOI 10.17487/RFC6749, October 2012, <[https://www.rfc-editor.org/rfc/rfc6749](https://www.rfc-editor.org/rfc/rfc6749)>. [OAUTH-ID-CHAIN]Schwenkschuster, A., Kasselman, P., Burgin, K., Jenkins, M. J., Campbell, B., and A. Parecki, "OAuth Identity and Authorization Chaining Across Domains", Work in Progress, Internet-Draft, draft-ietf-oauth-identity-chaining-12, 11 May 2026, <[https://datatracker.ietf.org/doc/html/draft-ietf-oauth-identity-chaining-12](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-identity-chaining-12)>. [OAUTH-JWT-ASSERTION]Parecki, A., McGuinness, K., and B. Campbell, "Identity Assertion JWT Authorization Grant", Work in Progress, Internet-Draft, draft-ietf-oauth-identity-assertion-authz-grant-04, 21 May 2026, <[https://datatracker.ietf.org/doc/html/draft-ietf-oauth-identity-assertion-authz-grant-04](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-identity-assertion-authz-grant-04)>. [OAUTH-REGISTRATION]Richer, J., Ed., Jones, M., Bradley, J., Machulak, M., and P. Hunt, "OAuth 2.0 Dynamic Client Registration Protocol", RFC 7591, DOI 10.17487/RFC7591, July 2015, <[https://www.rfc-editor.org/rfc/rfc7591](https://www.rfc-editor.org/rfc/rfc7591)>. [OAUTH-RESOURCE-METADATA]Jones, M.B., Hunt, P., and A. Parecki, "OAuth 2.0 Protected Resource Metadata", RFC 9728, DOI 10.17487/RFC9728, April 2025, <[https://www.rfc-editor.org/rfc/rfc9728](https://www.rfc-editor.org/rfc/rfc9728)>. [OAUTH-SERVER-METADATA]Jones, M., Sakimura, N., and J. Bradley, "OAuth 2.0 Authorization Server Metadata", RFC 8414, DOI 10.17487/RFC8414, June 2018, <[https://www.rfc-editor.org/rfc/rfc8414](https://www.rfc-editor.org/rfc/rfc8414)>. [OAUTH-SPIFFE]Schwenkschuster, A., Kasselman, P., Rose, S., and S. Thorgersen, "OAuth SPIFFE Client Authentication", Work in Progress, Internet-Draft, draft-ietf-oauth-spiffe-client-auth-01, 2 March 2026, <[https://datatracker.ietf.org/doc/html/draft-ietf-oauth-spiffe-client-auth-01](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-spiffe-client-auth-01)>. [OAUTH-TOKEN-EXCHANGE]Jones, M., Nadalin, A., Campbell, B., Ed., Bradley, J., and C. Mortimore, "OAuth 2.0 Token Exchange", RFC 8693, DOI 10.17487/RFC8693, January 2020, <[https://www.rfc-editor.org/rfc/rfc8693](https://www.rfc-editor.org/rfc/rfc8693)>. [OAUTH-TOKEN-INTROSPECTION]Richer, J., Ed., "OAuth 2.0 Token Introspection", RFC 7662, DOI 10.17487/RFC7662, October 2015, <[https://www.rfc-editor.org/rfc/rfc7662](https://www.rfc-editor.org/rfc/rfc7662)>. [OAUTH-TXN-TOKENS]Tulshibagwale, A., Fletcher, G., and P. Kasselman, "Transaction Tokens", Work in Progress, Internet-Draft, draft-ietf-oauth-transaction-tokens-08, 2 March 2026, <[https://datatracker.ietf.org/doc/html/draft-ietf-oauth-transaction-tokens-08](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-transaction-tokens-08)>. [OpenIDConnect.AuthZEN]Gazitt, O., Ed., Brossard, D., Ed., and A. Tulshibagwale, Ed., "Authorization API 1.0", 2026, <[https://openid.net/specs/authorization-api-1_0.html](https://openid.net/specs/authorization-api-1_0.html)>. [OpenIDConnect.CIBA]"OpenID Connect Client-Initiated Backchannel Authentication Flow - Core 1.0", n.d., <[https://openid.net/specs/openid-client-initiated-backchannel-authentication-core-1_0.html](https://openid.net/specs/openid-client-initiated-backchannel-authentication-core-1_0.html)>. [OpenIDConnect.Discovery]"OpenID Connect Discovery 1.0", n.d., <[https://openid.net/specs/openid-connect-discovery-1_0-final.html](https://openid.net/specs/openid-connect-discovery-1_0-final.html)>. [OpenIDConnect.FAPI]"FAPI 2.0 Security Profile", n.d., <[https://openid.net/specs/fapi-security-profile-2_0-final.html](https://openid.net/specs/fapi-security-profile-2_0-final.html)>. [RFC2119]Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, DOI 10.17487/RFC2119, March 1997, <[https://www.rfc-editor.org/rfc/rfc2119](https://www.rfc-editor.org/rfc/rfc2119)>. [RFC8174]Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words", BCP 14, RFC 8174, DOI 10.17487/RFC8174, May 2017, <[https://www.rfc-editor.org/rfc/rfc8174](https://www.rfc-editor.org/rfc/rfc8174)>. [RISC]"OpenID Risk Incident Sharing and Coordination Profile 1.0", n.d., <[https://openid.net/specs/openid-risc-1_0-final.html](https://openid.net/specs/openid-risc-1_0-final.html)>. [SPIFFE]"Secure Production Identity Framework for Everyone", n.d., <[https://spiffe.io/docs/latest/spiffe-about/overview/](https://spiffe.io/docs/latest/spiffe-about/overview/)>. [SPIFFE-ID]"SPIFFE-ID", n.d., <[https://github.com/spiffe/spiffe/blob/main/standards/SPIFFE-ID.md](https://github.com/spiffe/spiffe/blob/main/standards/SPIFFE-ID.md)>. [SSF]"OpenID Shared Signals Framework Specification 1.0", n.d., <[https://openid.net/specs/openid-sharedsignals-framework-1_0-final.html](https://openid.net/specs/openid-sharedsignals-framework-1_0-final.html)>. [WIMSE-ARCH]Salowey, J. A., Rosomakho, Y., and H. Tschofenig, "Workload Identity in a Multi System Environment (WIMSE) Architecture", Work in Progress, Internet-Draft, draft-ietf-wimse-arch-07, 2 March 2026, <[https://datatracker.ietf.org/doc/html/draft-ietf-wimse-arch-07](https://datatracker.ietf.org/doc/html/draft-ietf-wimse-arch-07)>. [WIMSE-CRED]Campbell, B., Salowey, J. A., Schwenkschuster, A., Sheffer, Y., and Y. Rosomakho, "WIMSE Workload Credentials", Work in Progress, Internet-Draft, draft-ietf-wimse-workload-creds-01, 5 May 2026, <[https://datatracker.ietf.org/doc/html/draft-ietf-wimse-workload-creds-01](https://datatracker.ietf.org/doc/html/draft-ietf-wimse-workload-creds-01)>. [WIMSE-HTTPSIG]Salowey, J. A. and Y. Sheffer, "WIMSE Workload-to-Workload Authentication with HTTP Signatures", Work in Progress, Internet-Draft, draft-ietf-wimse-http-signature-03, 7 April 2026, <[https://datatracker.ietf.org/doc/html/draft-ietf-wimse-http-signature-03](https://datatracker.ietf.org/doc/html/draft-ietf-wimse-http-signature-03)>. [WIMSE-ID]Rosomakho, Y. and J. A. Salowey, "Workload Identifier", Work in Progress, Internet-Draft, draft-ietf-wimse-identifier-02, 2 March 2026, <[https://datatracker.ietf.org/doc/html/draft-ietf-wimse-identifier-02](https://datatracker.ietf.org/doc/html/draft-ietf-wimse-identifier-02)>. [WIMSE-WPT]Campbell, B. and A. Schwenkschuster, "WIMSE Workload Proof Token", Work in Progress, Internet-Draft, draft-ietf-wimse-wpt-01, 2 March 2026, <[https://datatracker.ietf.org/doc/html/draft-ietf-wimse-wpt-01](https://datatracker.ietf.org/doc/html/draft-ietf-wimse-wpt-01)>. 
## [Appendix A.](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#appendix-A)[Document History](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-document-history)

[[ To be removed from the final specification ]][¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#appendix-A-1)

-02[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#appendix-A-2)

*   Add Aaron Parecki from Okta as co-author.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#appendix-A-3.1.1)

*   Add reference to phishing resistent credentials (e.g. FIDO passkeys/authenticators) - see https://github.com/PieterKas/agent2agent-auth-framework/issues/106[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#appendix-A-3.2.1)

*   Fold attestation section into provosioning section. Change terminology to posture management.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#appendix-A-3.3.1)

*   Clarify Oauth authentication mechanisms when an Agent acts as and OAuth client.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#appendix-A-3.4.1)

*   Update Security Considerations section[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#appendix-A-3.5.1)

*   Add section on Agent Mission (see issue https://github.com/PieterKas/agent2agent-auth-framework/issues/107)[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#appendix-A-3.6.1)

-01[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#appendix-A-4)

*   Add Nick Steele from OpenAI as co-author.[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#appendix-A-5.1.1)

-00[¶](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#appendix-A-6)

## [Authors' Addresses](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth/#name-authors-addresses)

Pieter Kasselman

Defakto Security

Jean-François Lombardo

AWS

Yaroslav Rosomakho

Zscaler

Brian Campbell

Ping Identity

Nick Steele

OpenAI

Aaron Parecki

Okta
