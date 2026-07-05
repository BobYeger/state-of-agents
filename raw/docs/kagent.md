Title: What is kagent

URL Source: https://kagent.dev/docs/kagent/introduction/what-is-kagent

Markdown Content:
## Introducing kagent[#](https://kagent.dev/docs/kagent/introduction/what-is-kagent#introducing-kagent)

kagent is an open-source programming framework that brings the power of agentic AI to cloud-native environments. Built specifically for DevOps and platform engineers, kagent enables AI agents to run directly in Kubernetes clusters to automate operations, troubleshoot issues, and solve complex cloud-native challenges.

kagent was created at [Solo.io](https://www.solo.io/) in 2025 and is a [Cloud Native Computing Foundation](https://www.cncf.io/) sandbox project.

Unlike traditional chatbots, kagent leverages advanced reasoning and iterative planning capabilities to autonomously handle multi-step problems in cloud-native environments. It transforms AI insights into concrete actions, helping teams tackle common operational challenges like:

*   Diagnosing connectivity issues across multiple service hops
*   Troubleshooting application performance degradation
*   Automating alert generation from Prometheus metrics
*   Debugging Gateway and HTTPRoute configurations
*   Managing progressive rollouts with Argo Rollouts

## Core Components[#](https://kagent.dev/docs/kagent/introduction/what-is-kagent#core-components)

kagent's architecture consists of three main components:

*   **Tools**: Any MCP-style function that agents can leverage to interact with cloud-native systems. kagent comes with pre-built tools that include capabilities like displaying pod logs, querying Prometheus metrics, generating resources and more. You can check the available tools in the [tool registry](https://kagent.dev/tools).
*   **Agents**: Autonomous systems that plan, execute, and analyze tasks using the available tools. These agents can chain multiple operations together to solve complex problems. Each agent can have access to one or more tools to accomplish its work. Agents can also be grouped into teams where a planning agent comes up with a plan and assigns tasks to individual agents in the team.
*   **Framework**: A flexible interface that allows running agents either through a UI or declaratively. Built on Google's ADK framework, it provides extensive customization options.

## Why kagent?[#](https://kagent.dev/docs/kagent/introduction/what-is-kagent#why-kagent)

kagent addresses the growing complexity of cloud-native operations by:

*   Automating routine troubleshooting and operational tasks
*   Reducing the need for specialist intervention in common scenarios
*   Enabling teams to formalize and share their operational expertise
*   Providing a platform for building and sharing custom AI agents

## Platform features[#](https://kagent.dev/docs/kagent/introduction/what-is-kagent#platform-features)

Everything works with a single `helm install`. No add-ons, no extra databases, no waiting for enterprise.

**Agent lifecycle via CRDs**Define, version, and roll out agents with kubectl and GitOps — the same workflow as every other workload.

**Multi-runtime support**Go and Python ADK runtimes. Pick the language that fits, or mix both in the same cluster.

**BYO frameworks**LangGraph, CrewAI, Google ADK, or your own — bring any agent framework and kagent orchestrates it.

**Long-term memory**Persistent vector-backed memory across sessions. Agents remember context, not just the last prompt.

**Human-in-the-loop**Tool approval gates, agent-initiated questions, and cascading HITL — humans stay in control.

**Agent-to-Agent (A2A)**Agents discover and invoke each other. Compose multi-agent workflows with first-class delegation.

**Skills from Git**Load markdown knowledge from Git repos at startup. Agents learn your runbooks, ADRs, and internal docs.

**Prompt templates**Reusable prompt fragments stored as ConfigMaps. DRY your system prompts across agents.

**Context compaction**Auto-summarization of long conversation histories. Agents stay coherent without blowing token budgets.

**Sandbox & security**Agent sandboxing, RBAC, and security hardening out of the box. Run untrusted code safely.

**Full observability**OTel tracing, Prometheus metrics, structured logs. See every prompt, every tool call, every token.

**Postgres storage**Production-grade Postgres-backed storage with reviewable migrations. No proprietary database lock-in.

## Enterprise distributions[#](https://kagent.dev/docs/kagent/introduction/what-is-kagent#enterprise-distributions)

Check out [Solo Enterprise for kagent](https://www.solo.io/products/kagent-enterprise), a comprehensive agent management interface for creating, validating, debugging, deploying, and monitoring AI agents across federated Kubernetes clusters. Solo Enterprise for kagent adds enterprise-grade capabilities on top of the kagent open source project, including advanced management features, observability tools, and multicluster federation support.

## Getting Started[#](https://kagent.dev/docs/kagent/introduction/what-is-kagent#getting-started)

To start using kagent in your environment, check out the [Quick Start Guide](https://kagent.dev/docs/kagent/getting-started/quickstart) guide. For a deeper understanding of how kagent works, refer to the [kagent architecture](https://kagent.dev/docs/kagent/concepts/architecture).

Ready to contribute? Visit our [Github repository](https://github.com/kagent-dev) to learn how you can help expand the ecosystem of cloud-native AI agents.

Join the kagent community:

*   Explore our repositories on [GitHub](https://github.com/kagent-dev)
*   Join the discussion in the #kagent channel on CNCF Slack
*   Check our [FAQ](https://kagent.dev/docs/kagent/resources/faq) for common questions
*   Follow our [Feature Roadmap](https://github.com/kagent-dev/kagent/blob/main/README.md#roadmap) for upcoming developments

Kagent Lab: Discover kagent and kmcp

Free, on‑demand lab: build custom AI agents with kagent and integrate tools via kmcp on Kubernetes.
