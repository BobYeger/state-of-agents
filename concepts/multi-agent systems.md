# Multi-Agent Systems

Multi-agent systems coordinate multiple agents through roles, communication channels, shared state, protocols, topologies, or market/social mechanisms.

## Key Design Dimensions

- Agents and roles
- Coordination topology
- Communication protocol
- Shared or private memory
- Centralized versus decentralized control
- Cooperation, competition, or mixed-motive interaction
- Runtime routing and budget control

## Improvement Levers

- Match the agent structure to task breadth, decomposition, context independence, and role specialization.
- Optimize prompts, roles, and topology instead of assuming a fixed team.
- Add runtime routing, dropout, supervision, and verification to control cost and error propagation.
- Use shared artifacts, memory, evals, and observability as coordination surfaces.
- Give shared state an explicit authority model: who may write, which version wins, and how conflicts resolve.

## Evidence on Scale and Coordination Cost

Coordination now has measured costs, not just anecdotes. [[sources/Towards a Science of Scaling Agent Systems]] finds independent agents amplify errors 17.2x versus 4.4x under centralized coordination, and coordination returns turn negative once the single-agent baseline passes roughly 0.45 accuracy. [[sources/MacNet]] shows performance follows a logistic curve in agent count and topology choice matters more than count. [[sources/Correlated Errors in Large Language Models]] explains why adding similar agents saturates: models agree 60% of the time when both err, even across vendors. On the coordination-mechanism side, [[sources/LLM Multi-Agent Blackboard System]] shows volunteer pickup from a shared blackboard beating coordinator-assigned subtasks by 13-57%, and [[sources/Cognition Dont Build Multi-Agents]] is the standing counter-position: parallel writers make conflicting implicit decisions, so writes should stay single-threaded. See [[methods/multi-agent orchestration]] for the design consequences and [[methods/debate and aggregation]] for when spending agents on the same question pays.

## Related

- [[methods/multi-agent orchestration]]
- [[maps/What Makes Agent Systems Better]]
- [[methods/topology optimization]]
- [[methods/debate and aggregation]]
- [[methods/runtime routing]]
- [[methods/runtime supervision]]
- [[protocols/agent protocols]]
- [[claims/Claim - More agents are not automatically better]]
- [[claims/Claim - Agent systems improve when structure matches the task]]

## Related Sources

- [[sources/Google AI Co-Scientist Article|Accelerating scientific breakthroughs with an AI co-scientist]]
- [[sources/AgentDropout|AgentDropout: Dynamic Agent Elimination for Token-Efficient and High-Performance LLM-Based Multi-Agent Collaboration]]
- [[sources/Agentic Large Language Models - A Survey|Agentic Large Language Models, a survey]]
- [[sources/Aligned Agents Biased Swarm|Aligned Agents, Biased Swarm: Measuring Bias Amplification in Multi-Agent Systems]]
- [[sources/A2A Specification|Agent2Agent Protocol Specification]]
- [[sources/Anthropic Multi-Agent Research System|How we built our multi-agent research system]]
- [[sources/MARSHAL|MARSHAL: Incentivizing Multi-Agent Reasoning via Self-Play with Strategic LLMs]]
- [[sources/MAS2|MAS2: Self-Generative, Self-Configuring, Self-Rectifying Multi-Agent Systems]]
- [[sources/MegaAgent|MegaAgent: A Large-Scale Autonomous LLM-based Multi-Agent System Without Predefined SOPs]]
- [[sources/Multi-Agent Collaboration Mechanisms - A Survey of LLMs|Multi-Agent Collaboration Mechanisms: A Survey of LLMs]]
- [[sources/Multi-Agent Collaboration via Evolving Orchestration|Multi-Agent Collaboration via Evolving Orchestration]]
- [[sources/Multi-Agent Design - MASS|Multi-Agent Design: Optimizing Agents with Better Prompts and Topologies]]
- [[sources/MultiAgentBench|MultiAgentBench: Evaluating the Collaboration and Competition of LLM agents]]
- [[sources/Cloudflare Project Think|Project Think: building the next generation of AI agents on Cloudflare]]
- [[sources/SiriuS|SiriuS: Self-improving Multi-agent Systems via Bootstrapped Reasoning]]
- [[sources/Cursor Multi-Agent Kernels|Speeding up GPU kernels by 38% with a multi-agent system]]
- [[sources/Stop Wasting Your Tokens|Stop Wasting Your Tokens: Towards Efficient Runtime Multi-Agent Systems]]
- [[sources/Stronger-MAS|Stronger-MAS: Multi-Agent Reinforcement Learning for Collaborative LLMs]]
- [[sources/AI Co-Scientist|Towards an AI Co-Scientist]]
- [[sources/Cursor Self-Driving Codebases|Towards self-driving codebases]]
- [[sources/When Agents Misremember Collectively|When Agents Misremember Collectively: Exploring the Mandela Effect in LLM-based Multi-Agent Systems]]
- [[sources/Why Do Multi-Agent LLM Systems Fail|Why Do Multi-Agent LLM Systems Fail?]]
- [[sources/X-MAS|X-MAS: Towards Building Multi-Agent Systems with Heterogeneous LLMs]]
- [[sources/Towards a Science of Scaling Agent Systems|Towards a Science of Scaling Agent Systems]]
- [[sources/MacNet|Scaling Large Language Model-based Multi-Agent Collaboration (MacNet)]]
- [[sources/Correlated Errors in Large Language Models|Correlated Errors in Large Language Models]]
- [[sources/Cognition Dont Build Multi-Agents|Don't Build Multi-Agents]]
- [[sources/Cognition Multi-Agents Whats Actually Working|Multi-Agents: What's Actually Working]]
- [[sources/LLM Multi-Agent Blackboard System|LLM-based Multi-Agent Blackboard System for Information Discovery in Data Science]]
- [[sources/Governed Shared Memory for Multi-Agent LLM Systems|Governed Shared Memory for Multi-Agent LLM Systems]]
- [[sources/G-Memory|G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems]]
