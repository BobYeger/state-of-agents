# Claim - Agent Systems Improve When Structure Matches The Task

Agent systems improve when the decomposition, roles, communication topology, and coordination protocol match the task. Multi-agent systems are most defensible when the work is broad, parallelizable, context-heavy, or benefits from specialized roles.

## The Design Rule

Task-contingent orchestration: choose the smallest structure that creates useful parallelism, independent context, specialization, or verification without adding unnecessary coordination cost. The cost side of the same decision is [[claims/Claim - Coordination is a cost the task must justify]].

## Supporting Sources

- [[sources/Towards a Science of Scaling Agent Systems]] is the quantitative anchor: across 260 configurations, relative performance against a single-agent baseline spans +80.8% (decomposable financial reasoning under centralized coordination) to -70.0% (sequential planning under independent agents), and a predictor built from coordination metrics selects the best architecture for 87% of held-out configurations — structure-task fit is measurable, not taste.
- [[sources/Do More Agents Help]] shows the fit has to be found, not assumed: fixed multi-agent workflows often trail matched single-agent setups under a normalized protocol, while runtime-generated workflows can help on harder tasks.
- [[sources/Anthropic Multi-Agent Research System]] is the clearest production case for broad research tasks where subagents get separate context windows and tool-heavy search paths.
- [[sources/Anthropic Building Effective AI Agents eBook]] gives enterprise decision guidance for choosing single-agent, workflow, hierarchical multi-agent, or collaborative multi-agent architectures based on task breadth, dependencies, risk, budget, and auditability.
- [[sources/Claude Common Workflow Patterns for AI Agents]] gives the production heuristic for matching workflow structure to task shape: sequential for dependencies, parallel for independent subtasks, evaluator-optimizer for measurable quality improvement.
- [[sources/Google Scaling Agent Systems]] frames scaling as a scientific question about when coordination helps versus when it adds overhead.
- [[sources/Multi-Agent Collaboration Mechanisms - A Survey of LLMs]] gives the taxonomy: actors, structures, strategies, cooperation/competition, and coordination protocols.
- [[sources/Multi-Agent Design - MASS]] shows prompts and topologies jointly determine MAS quality.
- [[sources/MultiAgentBench]] treats coordination protocol and topology as measured variables.
- [[sources/Understanding Multi-Agent LLM Frameworks]] shows framework architecture can strongly affect latency, planning accuracy, and coordination success.
- [[sources/The Orchestration of Multi-Agent Systems]] frames orchestration as the control plane that makes agent collectives coherent, auditable, and policy-compliant.
- [[sources/Magentic-One]] is a concrete orchestrator-worker architecture where the lead agent plans, tracks progress, delegates, and replans.
- [[sources/Google ADK Multi-Agent Patterns]] is practical evidence for pipelines, routing, delegation, and human-in-loop patterns.
- [[sources/OpenRouter Fusion Beats Frontier]] is product evidence for task-fit model panels: deep-research synthesis benefits from parallel model diversity and a judge/synthesizer, while simpler coding remains better served by selective use.
- [[sources/Plan-Then-Execute]] and [[sources/VeriMAP]] show that explicit planner-executor or planner-executor-verifier structure helps when tasks benefit from plan review, structured subtask I/O, or verification.

## Design Implications

- Start from task structure, not team size.
- Prefer single-agent or workflow patterns when decomposition is weak.
- Use multi-agent structures when agents can own distinct context, tools, subtasks, or review roles.
- Make the communication pattern explicit enough to evaluate.

## Related

- [[claims/Claim - Coordination is a cost the task must justify]]
- [[maps/What Makes Agent Systems Better]]
- [[maps/MAS Orchestration and Architecture]]
- [[methods/multi-agent orchestration]]
- [[methods/deliberative control]]
- [[methods/topology optimization]]
- [[concepts/multi-agent systems]]
