Title: Overview of Azure SRE Agent

URL Source: https://learn.microsoft.com/en-us/azure/sre-agent/overview

Markdown Content:
Azure SRE Agent safely automates operational work and reduces toil, so your team spends less time on incident triage and manual runbooks and more time building.

It connects your observability tools, incident platforms, and source code repositories into a single automated workflow. When something breaks at 3 AM, instead of jumping between Grafana, PagerDuty, and Slack, you get one investigation with answers already in it, including what changed, what's affected, and what to do next.

The agent proposes changes and your team approves. No change deploys without human sign-off.

Every investigation the agent runs builds institutional knowledge that persists across conversations and accumulates over time, whether you're a team of twenty or the only person who knows how the system works.

Picture alerts firing at 2:47 AM for your payment-service from Azure Monitor, PagerDuty, or any connected monitoring platform.

Within minutes, SRE Agent:

*   Queries Application Insights and identifies a memory trend that started 40 minutes before the alert
*   Correlates the trend with a deployment event from your GitHub repository two hours earlier
*   Identifies the specific commit and proposes two mitigations: restart the affected pod and adjust the memory scaling threshold (HPA)
*   Creates a ticket in ServiceNow, PagerDuty, or your incident channel with the full investigation summary prefilled

A notification surfaces the proposed mitigation. The on-call engineer reviews the summary and approves with a single action, with no runbook required and no context-switching. The investigation resolves in 7 minutes in a single thread, with no war room and no tab-switching between Grafana, PagerDuty, and Slack.

SRE Agent can manage the full range of Azure services your team relies on:

*   **Compute services**: Virtual machines, App Service, Container Apps, Azure Kubernetes Service (AKS), Azure Functions, and more.

*   **Storage services**: Blob storage, file shares, managed disks, and storage accounts.

*   **Networking services**: Virtual networks, load balancers, application gateways, and network security groups.

*   **Database services**: Azure SQL Database, Cosmos DB, PostgreSQL, MySQL, and Redis.

*   **Monitoring and management**: Azure Monitor, Log Analytics, Application Insights, and Resource Manager.

You can automate any Azure CLI operation through SRE Agent using runbooks, subagents, and [agent hooks](https://learn.microsoft.com/en-us/azure/sre-agent/agent-hooks).

*   **Automate incidents**: When an alert fires, the agent queries your monitoring tools, correlates signals across systems, identifies probable root cause, and proposes mitigations. This process reduces mean time to recovery (MTTR), improves service availability, and catches failure patterns before they become incidents.

*   **Automate scheduled workflows**: Run proactive health checks, compliance sweeps, and routine operational tasks on a defined schedule. Results surface in your connected incident platform or notification channel.

*   **Investigate and advise**: Ask natural-language questions about your environment, such as "what changed in the last hour?" or "why is this service degraded?", and get grounded answers with source citations.

SRE Agent combines fine-tuned Azure expertise with full customization capabilities. Out of the box, it understands and manages Azure resources with intelligent defaults for common operational tasks.

The agent operates through five extension primitives:

*   **Skills**: Discrete capabilities, including marketplace runbooks and Azure CLI scripts, that extend the agent's operational reach without requiring custom code.

*   **Subagents**: Purpose-built agents for specific operational domains. Five subagents ship built-in (architecture, logs and metrics, source code, root cause analysis, and scanning), and you can build additional custom subagents or compose them for cross-domain investigations.

*   **Python tools**: Custom logic, data transformations, and API integrations for scenarios that require code rather than configuration.

*   **MCP servers**: Connect to 40+ pre-built connectors (Datadog, Prometheus, Grafana, New Relic, Splunk, Elasticsearch, Dynatrace, AWS CloudWatch, GCP Stackdriver, and more) or any custom tool through the Model Context Protocol standard.

*   **Agent hooks**: Event-triggered automations that run at defined points in the agent lifecycle, either before investigation or after resolution. Two executor types are supported: command hooks run deterministic CLI operations, and prompt hooks produce LLM-evaluated structured JSON output. Use hooks to enforce policies, emit telemetry, or integrate with external approval workflows. See [agent hooks](https://learn.microsoft.com/en-us/azure/sre-agent/agent-hooks).

*   **Permission gate**: A pre-execution safety layer that evaluates every proposed tool call before it runs. Operators can require human approval, enforce policy rules, or block disallowed operations, ensuring your team remains in control even during fully automated workflows. Audit telemetry routes to your own Application Insights instance for compliance visibility.

For the full primitive taxonomy, including RBAC scoping, cost attribution, and audit trail patterns, see [Subagents and extensibility](https://learn.microsoft.com/en-us/azure/sre-agent/sub-agents) and [Agent hooks](https://learn.microsoft.com/en-us/azure/sre-agent/agent-hooks).

Every investigation teaches your agent something new, and that knowledge stays even when you don't. It captures root causes, resolution steps, preferences, and operational patterns. If you're the only one who knows how the system works, that's no longer a single point of failure. For teams, new members ramp up faster, on-call quality stays consistent regardless of who's paged, and your collective expertise grows automatically.

Tip

**Team example:** A new engineer joins on-call. The agent already knows deployment patterns, past incidents, and team procedures, delivering consistent quality from day one.

**Solo example:** You go on vacation. The agent carries your operational context so whoever covers doesn't start from scratch.

Azure SRE Agent integrates with your operational ecosystem in the following ways:

**Monitoring and observability:**

*   Azure Monitor (metrics, logs, alerts, workbooks)
*   Application Insights
*   Log Analytics
*   Grafana

**Incident management:**

*   Azure Monitor Alerts
*   PagerDuty
*   ServiceNow

**Source control and CI/CD:**

*   GitHub (repositories, issues)
*   Azure DevOps (repos, work items)

**Data sources:**

*   Azure Data Explorer (Kusto) clusters
*   Model Context Protocol (MCP) servers

**Communication and notifications:**

*   Slack
*   Microsoft Teams

Get started working with Azure SRE Agent by scheduling a task, handling an incident, or building a custom agent.

*   [Schedule a task](https://learn.microsoft.com/en-us/azure/sre-agent/overview#tabpanel_1_task)
*   [Handle an incident](https://learn.microsoft.com/en-us/azure/sre-agent/overview#tabpanel_1_incident)
*   [Build a custom agent](https://learn.microsoft.com/en-us/azure/sre-agent/overview#tabpanel_1_subagent)

Use scheduled tasks to automate routine operational work (health checks, cleanup, and compliance sweeps) without writing infrastructure code.

1.   Select the **Schedule tasks** tab.

2.   Enter task details.

3.   Define the schedule to run your task.

4.   Craft custom agent instructions for the task.

5.   Select **Create scheduled task**.

6.   Results from your scheduled task surface in your connected incident platform or notification channel.

SRE Agent delivers progressive value as it learns your environment, your patterns, and your operational history.

| Milestone | What happens |
| --- | --- |
| **Day 1** | Connect your tools, triage your first incident, and get immediate diagnostic value from built-in Azure knowledge. |
| **Week 1** | The agent learns your environment topology, common failure patterns, and escalation preferences. Investigations get faster and more accurate. |
| **Month 1** | Institutional knowledge compounds. Teams report catching failure patterns before they escalate. New team members contribute from their first on-call shift with no tribal knowledge required. |

Organizations using Azure SRE Agent report significant reductions in mean time to recovery and operational overhead across early pilots.

Whether you're evaluating for a team or running operations solo, start with the progressive value table in the preceding section. Then explore:

| Resource | What you find |
| --- | --- |
| [Pricing and billing](https://learn.microsoft.com/en-us/azure/sre-agent/pricing-billing) | Usage-based pricing, free tier eligibility, and capacity planning |
| [Security overview](https://learn.microsoft.com/en-us/azure/sre-agent/security-overview) | Data handling, privacy, network integration |
| [Create and set up](https://learn.microsoft.com/en-us/azure/sre-agent/create-agent) | How to run a structured pilot |
| [Team setup and roles](https://learn.microsoft.com/en-us/azure/sre-agent/create-agent) | Administrator vs. Standard User roles, phased rollout guide |

Keep the following considerations in mind as you use Azure SRE Agent:

*   English is the only supported language in the chat interface.
*   For more information about how Azure SRE Agent manages data, see the [Microsoft privacy policy](https://www.microsoft.com/privacy/privacystatement).
*   Availability varies by region and tenant configuration.
*   Costs are usage-based. See [Pricing and billing](https://learn.microsoft.com/en-us/azure/sre-agent/pricing-billing) for the current rate model and free tier details.
*   As with any AI system, SRE Agent might occasionally produce incorrect conclusions or propose mitigations that don't apply to your environment. Always review proposed actions before approving.

When you create an agent, the following resources are also automatically created for you:

*   Azure Application Insights
*   Log Analytics workspace
*   Managed Identity

These resources support agent observability and identity management. You can view and manage them in your Azure subscription.
