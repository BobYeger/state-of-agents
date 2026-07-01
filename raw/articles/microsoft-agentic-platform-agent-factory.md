AI is already changing how teams build software, and the biggest shift goes beyond writing code faster. It’s reshaping the full software lifecycle, from planning and development to security, operations, and modernization. Inside Microsoft, we build and run software at massive scale, across every kind of codebase, and we put these agentic tools to work ourselves before we put them in your hands. The Customer Zero series gives you an inside view of how we’re applying AI across the entire software development lifecycle, and to share what we’re learning so you can lead your own transformation. This blog is the first in a series to give software leaders a practical view inside Microsoft and our transformation.

At Ignite 2025, we shared the vision of Microsoft’s transformation from a software factory to an AI and agent factory. Breakthroughs in AI reasoning, planning, and tool-calling are changing how we build software. An agent factory is what comes next, where agents collaborate across the entire software development lifecycle, systems learn and improve each cycle, and every team works side by side with agents.

Building agents with agents has unlocked faster, higher-quality workflows for developers. GitHub Copilot, Azure SRE Agent, and custom agents grounded in context architectures have enabled developers in ways previously unimaginable: they’re saving time at each stage of work by collaborating with agents for outcomes like faster planning cycles, more accurate internal knowledge search, automated PR reviews, and improved app security and operations. Beyond the business impact of faster, higher-quality delivery, we’re able to foster an innersource culture where teams share agents and knowledge with each other.

![Microsoft Engineering Diversity and Scale graphic](https://devblogs.microsoft.com/wp-content/uploads/2026/06/Graphic_MIcrosoftEngineeringDiversityScale.webp)

Microsoft Engineering Diversity and Scale graphic

These innovations are happening at every scale, from smaller teams entrusted with critical projects to our largest teams operating at enormous scale. Each team is solving unique challenges, but one thing stays consistent. AI is helping them work faster and smarter than before.

As part of our transformation, we’re building an agentic platform around four frontier goals for Microsoft Engineering.

- Rearchitect the software lifecycle and with agentic workflows
- Unleash developer creativity by using agents as side-by-side collaborators
- Build security, compliance, and governance directly into the engineering platform
- Create the most productive and fulfilling developer experience

With AI in hand, product managers can develop more robust plans and solutions for engineers to execute on, strengthening how the two roles work together. Product managers and developers are empowered by agents to direct large-scale engineering efforts by leveraging iterative, incremental agent tasks driven by human expertise. For example, developers are able to delegate toil like security fixes and framework upgrades into agent tasks and break down simpler feature work into agent-driven PRs. And our developers feel the difference. With agents as part of their workflow, 62% of our developers say AI has [increased their overall job satisfaction](https://arxiv.org/abs/2508.00178) and 88% report [increased task throughput](https://arxiv.org/abs/2508.00178).

Another important shift we’ve made is moving from undifferentiated code to unambiguous intent. In practice, that means treating specs as a single source of truth to define what we’re building, help generate the right changes, verify that the system behaves as intended, and even help operate it in production. When specs are written clearly and kept current, agents, pipelines, and platforms can consistently follow them. This turns intent (the standards, best practices, and non-negotiables) into repeatable, auditable automation.

With an agentic platform, we’re building systems that iterate, learn, and scale. Using agents, our workflows have evolved with product managers and developers using agents at each step. Over 90% of Microsoft developers now use GitHub Copilot, and our AI code review covers [90% of Microsoft pull requests](https://devblogs.microsoft.com/engineering-at-microsoft/enhancing-code-quality-at-scale-with-ai-powered-code-reviews/) and speeds completion time by more than 10%. But this is bigger than giving developers an assist. It’s reshaping how the work itself gets done.

![Agentic Software Design Lifecycle diagram](https://devblogs.microsoft.com/wp-content/uploads/2026/06/Graphic_AgenticSDLC.webp)

Agentic Software Design Lifecycle diagram

Everything we’ve described so far, for both product managers and engineers, is already underway and continuing to grow. The benefits are tangible and measurable, showing up in the daily work and in the numbers:

- Reduced time-to-mitigation on security and ops issues with over [**50,000** **developer hours saved**](https://techcommunity.microsoft.com/blog/appsonazureblog/how-we-build-and-use-azure-sre-agent-with-agentic-workflows/4508753) with Azure SRE Agent
- Lightspeed modernization compared to previous manual efforts with [**80-90% accuracy in migrating hundreds of repos**](https://devblogs.microsoft.com/engineering-at-microsoft/the-interaction-changes-everything-treating-ai-agents-as-collaborators-not-automation/) in the Entra SDK migration
- Faster time-to-delivery with [**55% reduction in manual developer toil**](https://techcommunity.microsoft.com/blog/appsonazureblog/how-microsoft-1es-uses-agentic-ai-to-take-on-security-and-compliance-at-scale/4515191) using specialized agents and human-AI relationship best practices

Central to our transformation is delegating toil to agents. Security, modernization, migration, and ops are all critical to software, and agents can now carry more of that load so developers can spend their time on the innovative and meaningful feature work they do best. That shift does more than speed delivery. It makes the work more fulfilling, which is exactly the kind of developer experience we set out to build.

In this series, we’ll share what’s working for us and what we’re learning as we build for an agentic era. Each post explores a real-world use case, with practical takeaways for software teams of any size.

Real change comes from how teams work day to day, from idea through deployment. Explore the series and build on what’s working in Microsoft’s Customer Zero efforts to jump-start your own progress.

## How we build and use Azure SRE Agent with agentic workflows

Microsoft needed a new operational model for managing always-on cloud systems at the scale and speed of modern AI development. In this blog, the Azure SRE Agent team explains how Microsoft built and adopted agentic workflows that continuously investigate incidents, reason across operational signals, and assist engineers with remediation and recovery tasks. By combining AI agents with operational expertise, the team reduced manual toil while helping engineers focus more time on product innovation and reliability engineering.

![How we build and use Azure SRE Agent with agentic workflows](https://devblogs.microsoft.com/wp-content/uploads/2026/06/Graphic_HowWeBuildSREAgent.webp)

How we build and use Azure SRE Agent with agentic workflows

[Learn how Microsoft builds agents with agents](https://techcommunity.microsoft.com/blog/appsonazureblog/how-we-build-and-use-azure-sre-agent-with-agentic-workflows/4508753) and uses Azure SRE agent to drastically reduce manual effort in incident response.

## How Microsoft 1ES uses agentic AI to take on security and compliance at scale

Microsoft’s One Engineering System (1ES) organization needed a way to reduce the operational burden of security and compliance work on dependencies across thousands of repositories without slowing developer velocity. In this blog, Jenny Ferries explains how 1ES combined frontier AI models, agent runtimes, and agent specialization through skills to help automate complex remediation workflows.

![How Microsoft 1ES uses agentic AI to take on security and compliance at scale](https://devblogs.microsoft.com/wp-content/uploads/2026/06/Graphic_1ESAgenticAIforSecurity.webp)

How Microsoft 1ES uses agentic AI to take on security and compliance at scale

[Read more on how Microsoft uses agentic AI to remediate security issues](https://techcommunity.microsoft.com/blog/appsonazureblog/how-microsoft-1es-uses-agentic-ai-to-take-on-security-and-compliance-at-scale/4515191) and reduce developer toil at scale.

## From Copilots to Coworkers: How AI agents are transforming Azure Networking operations

Azure Networking is one of the largest fiber-optic networks in the world; as it continues to grow, the organization needed to transform with AI to mitigate against complexity and scale teams’ efforts to new heights. In this blog, the Denizcan Billor explains how AI agents evolved from assistive copilots into an agent organization of digital coworkers capable of investigating incidents, coordinating remediation, and accelerating network operations at scale. By embedding agents alongside practitioners within the same ecosystem, Azure Networking significantly increased autonomous incident resolution while helping engineers respond on higher-value work.

![From Copilots to Coworkers: How AI agents are transforming Azure Networking Operations](https://devblogs.microsoft.com/wp-content/uploads/2026/06/Graphic_FromCopilotsToCoworkers.webp)

From Copilots to Coworkers: How AI agents are transforming Azure Networking Operations

[Learn how Azure Networking accelerates incident remediation](https://techcommunity.microsoft.com/blog/appsonazureblog/from-copilots-to-coworkers-how-ai-agents-are-transforming-azure-networking-opera/4519850) and reduces operational toil across a variety of use cases.

## Read more stories

The three stories above are great examples of the many stories we continue to publish on how Microsoft builds and operates with AI. To see the latest stories from Microsoft Engineering leads, [you can find more on Tech Community](https://aka.ms/customerzeroblogs).