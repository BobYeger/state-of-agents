# Multi-Agent Orchestration

Multi-agent orchestration is the design of agent roles, routing, communication, shared state, and stopping conditions across a multi-agent system.

## Improvement Claim

Orchestration improves agent systems when it turns task structure into explicit roles, artifacts, routing rules, and stopping conditions. The best orchestration reduces ambiguity and coordination cost rather than multiplying participants.

## Coordination Cost Is Now Measurable

The question "should this be multi-agent at all" has moved from taste to measurement. [[sources/Towards a Science of Scaling Agent Systems]] evaluates five canonical architectures across 260 configurations and 9 models: independent parallel agents amplify trace-level errors 17.2x while centralized coordination contains amplification to 4.4x; coordination returns turn negative once the single-agent baseline exceeds roughly 0.45 accuracy; and tool-heavy tasks suffer disproportionately from coordination overhead. The spread between the best and worst architecture choice on the same task runs from +80.8% to -70.0% against the single-agent baseline — architecture selection, not agent count, is the decision that matters. [[sources/MacNet]] reaches the same conclusion from the scaling side: performance follows a logistic curve in agent count, and irregular topologies beat regular ones, so the marginal agent decays while the topology choice persists.

For designers this yields a concrete order of operations: measure the single-agent baseline first; if it is already strong, coordination is more likely to subtract than add; if the task decomposes, prefer centralized coordination for its error containment; budget for the disproportionate overhead on tool-heavy work.

## Handoff Information Design

What crosses an agent boundary is a design surface, and the strongest positions disagree in an instructive way. [[sources/Cognition Dont Build Multi-Agents]] argues that handoffs should carry full agent traces rather than summaries, because actions encode implicit decisions and parallel workers making conflicting implicit decisions produce incoherent results — the case for single-threaded execution with context compression instead of parallel subagents. The ten-month follow-up [[sources/Cognition Multi-Agents Whats Actually Working]] narrows rather than retracts this: multiple agents may contribute intelligence (a review loop catching ~2 bugs per PR, escalation to a stronger model, manager-child delegation), but writes stay single-threaded, and reviewers perform best with completely *clean* context rather than shared context.

The two essays jointly define the tradeoff: share full traces when the receiving agent must continue the same decision stream; strip context deliberately when the receiving agent's value is an independent check. Handoffs fail in both directions — too little context produces conflicting implicit decisions, too much context destroys the independence that made a second agent worth invoking.

## Shared State and Concurrency

When agents coordinate through shared artifacts rather than messages, the orchestration problem becomes a distributed-systems problem with known results.

- [[sources/Corkill Blackboard Systems]]: the 1991 statement of the blackboard model — independent knowledge sources over a global store with a *separate* control component scheduling activations — is a single-writer control loop over a multi-writer store, the design ancestor of agent task queues.
- [[sources/LLM Multi-Agent Blackboard System]]: LLM-era evidence that posting requests to a shared blackboard and letting agents volunteer beats coordinator-assigned subtasks by 13-57% on data-science benchmarks, because the coordinator no longer needs a model of each agent's expertise.
- [[sources/You Cannot Have Exactly-Once Delivery]]: task pickup between agents must be designed at-least-once plus idempotent; exactly-once delivery is impossible at the delivery layer.
- [[sources/Atomix]]: names the failure modes of orchestrators that mishandle tool side effects under concurrency — partial effects, losing-branch residue, stale writes, irreversible sends — and proposes transactional settlement with per-resource frontiers.
- [[sources/Governed Shared Memory for Multi-Agent LLM Systems]]: fleet-shared memory fails as leakage, stale propagation, persistent contradiction, and provenance collapse; the governance primitives are scoped retrieval, temporal supersession, provenance tracking, and policy-governed propagation.
- [[sources/G-Memory]]: a constructive design for team memory — hierarchical insight/query/interaction graphs propagate cross-trial lessons without flattening per-agent context.

The recurring lesson: shared state needs an explicit authority model (who may write, which version wins, how conflicts resolve) before it needs more participants. Cognition's single-writer principle, Corkill's control component, and Atomix's commit frontiers are the same idea at three layers.

## Related

- [[concepts/multi-agent systems]]
- [[concepts/agent teams]]
- [[maps/MAS Orchestration and Architecture]]
- [[maps/Agent Teams and Workforces Map]]
- [[maps/What Makes Agent Systems Better]]
- [[claims/Claim - Agent systems improve when structure matches the task]]
- [[claims/Claim - Agent teams need explicit organization]]
- [[methods/deliberative control]]
- [[methods/codex thread orchestration]]
- [[methods/topology optimization]]
- [[methods/debate and aggregation]]
- [[methods/runtime supervision]]

## Related Sources

- [[sources/AFlow|AFlow: Automating Agentic Workflow Generation]]
- [[sources/Anthropic Building Effective AI Agents eBook]]
- [[sources/Claude Common Workflow Patterns for AI Agents|Common workflow patterns for AI agents—and when to use them]]
- [[sources/Anthropic Multi-Agent Coordination Patterns|Multi-agent coordination patterns: Five approaches and when to use them]]
- [[sources/Claude Code Agent Teams|Orchestrate teams of Claude Code sessions]]
- [[sources/Google ADK Multi-Agent Patterns|Developer's guide to multi-agent patterns in ADK]]
- [[sources/AgentNet|AgentNet: Decentralized Evolutionary Coordination for LLM-based Multi-Agent Systems]]
- [[sources/ADAS|Automated Design of Agentic Systems]]
- [[sources/Anthropic Building Effective Agents|Building effective agents]]
- [[sources/HALO|HALO: Hierarchical Autonomous Logic-Oriented Orchestration for Multi-Agent LLM Systems]]
- [[sources/The Orchestration of Multi-Agent Systems|The Orchestration of Multi-Agent Systems: Architectures, Protocols, and Enterprise Adoption]]
- [[sources/Magentic-One|Magentic-One: A Generalist Multi-Agent System for Solving Complex Tasks]]
- [[sources/Magentic-UI|Magentic-UI: Towards Human-in-the-loop Agentic Systems]]
- [[sources/ChatDev|ChatDev: Communicative Agents for Software Development]]
- [[sources/MetaGPT|MetaGPT: Meta Programming for a Multi-Agent Collaborative Framework]]
- [[sources/Experiential Co-Learning|Experiential Co-Learning of Software-Developing Agents]]
- [[sources/Croto|Multi-Agent Collaboration via Cross-Team Orchestration]]
- [[sources/Agyn|Agyn: A Multi-Agent System for Team-Based Autonomous Software Engineering]]
- [[sources/Multi-Agent Teams Hold Experts Back|Multi-Agent Teams Hold Experts Back]]
- [[sources/Orchestrating Human-AI Teams|Orchestrating Human-AI Teams]]
- [[sources/Developing Guidelines for Human-LLM Agent Teams|Developing Guidelines for Human-LLM Agent Teams]]
- [[sources/MALBO|MALBO: Multi-Agent LLM Bayesian Optimization]]
- [[sources/VeriMAP|Verification-Aware Planning for Multi-Agent Systems]]
- [[sources/AgentFlow|In-the-Flow Agentic System Optimization for Effective Planning and Tool Use]]
- [[sources/Anthropic Multi-Agent Research System|How we built our multi-agent research system]]
- [[sources/MAPRO|MAPRO: Recasting Multi-Agent Prompt Optimization as Maximum a Posteriori Inference]]
- [[sources/MAS2|MAS2: Self-Generative, Self-Configuring, Self-Rectifying Multi-Agent Systems]]
- [[sources/MasRouter|MasRouter: Learning to Route LLMs for Multi-Agent Systems]]
- [[sources/OpenRouter Fusion Beats Frontier]]
- [[sources/MegaAgent|MegaAgent: A Large-Scale Autonomous LLM-based Multi-Agent System Without Predefined SOPs]]
- [[sources/Multi-Agent Collaboration Mechanisms - A Survey of LLMs|Multi-Agent Collaboration Mechanisms: A Survey of LLMs]]
- [[sources/Multi-Agent Collaboration via Evolving Orchestration|Multi-Agent Collaboration via Evolving Orchestration]]
- [[sources/Multi-Agent Design - MASS|Multi-Agent Design: Optimizing Agents with Better Prompts and Topologies]]
- [[sources/OWL|OWL: Optimized Workforce Learning for General Multi-Agent Assistance in Real-World Task Automation]]
- [[sources/Graph-of-Agents|Graph-of-Agents: A Graph-based Framework for Multi-Agent LLM Collaboration]]
- [[sources/Understanding Multi-Agent LLM Frameworks|Understanding Multi-Agent LLM Frameworks: A Unified Benchmark and Experimental Analysis]]
- [[sources/Towards a Science of Scaling Agent Systems|Towards a Science of Scaling Agent Systems]]
- [[sources/MacNet|Scaling Large Language Model-based Multi-Agent Collaboration (MacNet)]]
- [[sources/Cognition Dont Build Multi-Agents|Don't Build Multi-Agents]]
- [[sources/Cognition Multi-Agents Whats Actually Working|Multi-Agents: What's Actually Working]]
- [[sources/Corkill Blackboard Systems|Blackboard Systems (Corkill 1991)]]
- [[sources/LLM Multi-Agent Blackboard System|LLM-based Multi-Agent Blackboard System for Information Discovery in Data Science]]
- [[sources/You Cannot Have Exactly-Once Delivery|You Cannot Have Exactly-Once Delivery]]
- [[sources/Atomix|Atomix: Timely, Transactional Tool Use for Reliable Agentic Workflows]]
- [[sources/Governed Shared Memory for Multi-Agent LLM Systems|Governed Shared Memory for Multi-Agent LLM Systems]]
- [[sources/G-Memory|G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems]]
