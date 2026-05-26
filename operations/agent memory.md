# Agent Memory

Agent memory stores reusable knowledge, preferences, task state, or experience outside the current context window.

## Memory Risks

Memory poisoning attacks corrupt an agent's stored facts, preferences, procedures, or learned experience so future behavior is manipulated.

It matters more for agents than for chatbots because agents reuse state. A bad instruction, false fact, poisoned preference, or malicious tool note can persist across tasks and silently influence future planning, retrieval, or delegation.

## Improvement Claim

Memory improves agents when it stores reusable procedures and experience with provenance, scope, and evaluation. Unchecked memory can make agents worse; curated memory and skills can compound capability.

Useful control points:

- Separate trusted long-term memory from untrusted retrieved content.
- Track provenance, write authority, and expiration for memory items.
- Avoid turning user-visible documents or web pages directly into durable instructions.
- Add review gates before memories affect high-authority actions.
- Periodically audit memory for stale, adversarial, or overfit entries.

## Related

- [[concepts/context engineering]]
- [[concepts/context compaction]]
- [[concepts/dreaming and memory consolidation]]
- [[concepts/reasoning memory]]
- [[claims/Claim - Agent memory and skills create compounding improvement loops]]
- [[maps/Context Management Map]]
- [[maps/What Makes Agent Systems Better]]
- [[safety/prompt injection]]
- [[operations/durable sessions]]

## Related Sources

- [[sources/Agent Security Bench|Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents]]
- [[sources/AgentNet|AgentNet: Decentralized Evolutionary Coordination for LLM-based Multi-Agent Systems]]
- [[sources/Cloudflare Agent Memory|Agents that remember: introducing Agent Memory]]
- [[sources/Anthropic Context Engineering Cookbook|Context Engineering for AI Agents: Memory vs. Compaction vs. Tool Clearing]]
- [[sources/Anthropic Managed Agents Dreaming Outcomes|New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration]]
- [[sources/Anthropic Effective Context Engineering|Effective context engineering for AI agents]]
- [[sources/Memory for Autonomous LLM Agents|Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers]]
- [[sources/Trajectory-Informed Memory Generation|Trajectory-Informed Memory Generation for Self-Improving Agent Systems]]
- [[sources/Google ReasoningBank|ReasoningBank: Enabling agents to learn from experience]]
- [[sources/SiriuS|SiriuS: Self-improving Multi-agent Systems via Bootstrapped Reasoning]]
- [[sources/When Agents Misremember Collectively|When Agents Misremember Collectively: Exploring the Mandela Effect in LLM-based Multi-Agent Systems]]

## Skills and Procedural Memory

- [[concepts/procedural memory]]
- [[sources/SAGE Skill Library]]
- [[sources/SkillRL]]
- [[sources/Voyager]]
