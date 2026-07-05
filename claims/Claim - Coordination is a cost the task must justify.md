# Claim - Coordination Is a Cost the Task Must Justify

Every agent added to a system buys coverage, diversity, parallelism, or specialization at a measurable price: communication overhead, coordination failures, error propagation, cost, latency, and emergent social effects. Production multi-agent systems are normal in 2026; the design decision is matching coordination spend to task structure, and the costs now have numbers.

## Supporting Sources

- [[sources/Towards a Science of Scaling Agent Systems]] prices the claim across 260 configurations: independent agents amplify trace-level errors 17.2x versus 4.4x under centralized coordination, coordination yields diminishing or negative returns once the single-agent baseline exceeds roughly 0.45 accuracy, and tool-heavy tasks pay disproportionate overhead.
- [[sources/Do More Agents Help]] adds the controlled comparison: under a normalized protocol, five of six fixed multi-agent systems trail a matched single-agent anchor by 2.56-11.29 points at worse accuracy-cost trade-offs.
- [[sources/MacNet]] gives the scaling shape: returns follow a logistic curve in agent count, so the marginal agent decays while topology choice persists.
- [[sources/Cognition Multi-Agents Whats Actually Working]] is the production accounting: after ten months running multi-agent systems, writes stay single-threaded and added agents must pay for themselves as measured review intelligence.
- [[sources/Anthropic Building Effective Agents]] argues for simple workflows when they are enough and treats agentic complexity as an engineering tradeoff.
- [[sources/Anthropic Building Effective AI Agents eBook]] gives the enterprise version of the same principle: start with single agents, add Skills and routing first, then move to workflows or multi-agent systems when measurable requirements justify the cost.
- [[sources/Claude Common Workflow Patterns for AI Agents]] says to try a single agent first and add sequential, parallel, or evaluator-optimizer workflow structure only when the task shape justifies the cost.
- [[sources/Anthropic Multi-Agent Research System]] reports strong gains for broad research tasks, but also notes high token cost and narrower domains where multi-agent systems are not the right fit.
- [[sources/MultiAgentBench]] evaluates multiple topologies and makes coordination protocol a measured variable rather than an assumed improvement.
- [[sources/Multi-Agent Design - MASS]] shows that prompts and topology jointly matter; adding agents without topology design is not the point.
- [[sources/Why Do Multi-Agent LLM Systems Fail]] provides the strongest failure taxonomy: specification/design failures, inter-agent misalignment, and verification or termination failures.
- [[sources/AgentDropout]] and [[sources/Stop Wasting Your Tokens]] both treat unnecessary agents or messages as a runtime efficiency and quality problem.
- [[sources/OpenRouter Fusion Beats Frontier]] is a qualifying product example: model panels can beat solo models on a deep-research benchmark, but the article also frames Fusion as task-selective, slower, and not a drop-in replacement for coding or long-horizon work.
- [[sources/Understanding Multi-Agent LLM Frameworks]] shows framework architecture can strongly change latency, planning accuracy, and coordination success.
- [[sources/Aligned Agents Biased Swarm]] extends the claim into safety: individually aligned or neutral agents can still amplify collective bias.

## Contradicting Or Qualifying Sources

- Anthropic's multi-agent research system is evidence that multi-agent systems can substantially outperform single-agent setups when the task is broad, parallelizable, and context-heavy.
- [[sources/MegaAgent]], [[sources/AgentNet]], [[sources/OWL]], and [[sources/AI Co-Scientist]] are positive examples where decomposition, specialization, or dynamic coordination are central to the system design.
- [[sources/Multi-Agent Collaboration Mechanisms - A Survey of LLMs]] is the taxonomy anchor for when collaboration structure, role design, and coordination protocol are meaningful design variables.

## Current Synthesis

A task justifies coordination spend when it has breadth, decomposability, independent context, or role specialization; the measured thresholds and architecture-selection evidence live in [[methods/multi-agent orchestration]] and [[methods/topology optimization]]. The design toolkit that makes the spend pay: task-contingent orchestration, topology search, runtime supervision, dropout/routing, explicit verification, strong harnesses, tool contracts, and reusable memory/skills rather than fixed agent teams.

For what makes the spend productive, start with the "What Makes Agent Systems Better" map.

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
