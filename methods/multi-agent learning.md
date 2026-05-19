# Multi-Agent Learning

Training, self-play, reinforcement learning, and self-improvement methods for LLM-based multi-agent systems.

The key problem is credit assignment. Multi-agent workflows have roles, turns, communication effects, and shared outcomes, so naive single-agent reward grouping can hide which agent action helped or harmed the final result.

## Improvement Claim

Learning improves multi-agent systems when it assigns credit to roles, turns, interaction policies, and reusable trajectories. The useful target is not only a better final answer; it is a better collaboration policy.

## Learning Targets

- Role-specific policies and prompts.
- Turn-level interaction behavior.
- Planner, coordinator, and worker policies.
- Experience libraries from successful or failed trajectories.
- Self-play between cooperative and competitive agents.

## Related

- [[methods/deliberative control]]
- [[concepts/scaling with computation]]

## Related Sources

- [[sources/Learning to Deliberate|Learning to Deliberate: Meta-policy Collaboration for Agentic LLMs with Multi-agent Reinforcement Learning]]
- [[sources/HiPER|HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents]]
- [[sources/Lazy Agents to Deliberation|Unlocking the Power of Multi-Agent LLM for Reasoning: From Lazy Agents to Deliberation]]
- [[sources/MARSHAL|MARSHAL: Incentivizing Multi-Agent Reasoning via Self-Play with Strategic LLMs]]
- [[sources/MAS2|MAS2: Self-Generative, Self-Configuring, Self-Rectifying Multi-Agent Systems]]
- [[sources/OWL|OWL: Optimized Workforce Learning for General Multi-Agent Assistance in Real-World Task Automation]]
- [[sources/SiriuS|SiriuS: Self-improving Multi-agent Systems via Bootstrapped Reasoning]]
- [[sources/Stronger-MAS|Stronger-MAS: Multi-Agent Reinforcement Learning for Collaborative LLMs]]
