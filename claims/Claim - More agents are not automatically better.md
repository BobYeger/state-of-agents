# Claim - More Agents Are Not Automatically Better

More agents can increase coverage, diversity, parallelism, and specialization, but they can also increase communication overhead, coordination failures, cost, latency, error propagation, and emergent social harms.

## Supporting Sources

- [[sources/Anthropic Building Effective Agents]] argues for simple workflows when they are enough and treats agentic complexity as an engineering tradeoff.
- [[sources/Anthropic Multi-Agent Research System]] reports strong gains for broad research tasks, but also notes high token cost and narrower domains where multi-agent systems are not the right fit.
- [[sources/MultiAgentBench]] evaluates multiple topologies and makes coordination protocol a measured variable rather than an assumed improvement.
- [[sources/Multi-Agent Design - MASS]] shows that prompts and topology jointly matter; adding agents without topology design is not the point.
- [[sources/Why Do Multi-Agent LLM Systems Fail]] provides the strongest failure taxonomy: specification/design failures, inter-agent misalignment, and verification or termination failures.
- [[sources/AgentDropout]] and [[sources/Stop Wasting Your Tokens]] both treat unnecessary agents or messages as a runtime efficiency and quality problem.
- [[sources/Understanding Multi-Agent LLM Frameworks]] shows framework architecture can strongly change latency, planning accuracy, and coordination success.
- [[sources/Aligned Agents Biased Swarm]] extends the claim into safety: individually aligned or neutral agents can still amplify collective bias.

## Contradicting Or Qualifying Sources

- Anthropic's multi-agent research system is evidence that multi-agent systems can substantially outperform single-agent setups when the task is broad, parallelizable, and context-heavy.
- [[sources/MegaAgent]], [[sources/AgentNet]], [[sources/OWL]], and [[sources/AI Co-Scientist]] are positive examples where decomposition, specialization, or dynamic coordination are central to the system design.
- [[sources/Multi-Agent Collaboration Mechanisms - A Survey of LLMs]] is the taxonomy anchor for when collaboration structure, role design, and coordination protocol are meaningful design variables.

## Current Synthesis

The useful frontier question is not whether multi-agent systems are better; it is when a task has enough breadth, decomposability, independent context, or role specialization to justify the coordination cost. The best evidence points toward task-contingent orchestration, topology search, runtime supervision, dropout/routing, explicit verification, strong harnesses, tool contracts, and reusable memory/skills rather than fixed agent teams.

For the positive side of this claim, start with the "What Makes Agent Systems Better" map.

## Related

- [[concepts/multi-agent systems]]
- [[methods/multi-agent orchestration]]
- [[methods/topology optimization]]
- [[methods/runtime routing]]
- [[methods/runtime supervision]]
- [[maps/What Makes Agent Systems Better]]
- [[claims/Claim - Agent systems improve when structure matches the task]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
- [[claims/Claim - Agent memory and skills create compounding improvement loops]]
- [[benchmarks/multi-agent benchmarks]]

## Related Sources

- [[sources/TheAgentCompany|TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks]]
- [[sources/Cursor Self-Driving Codebases|Towards self-driving codebases]]
