# Multi-Agent Benchmarks

Benchmarks for collaboration, competition, negotiation, social simulation, and coordination among multiple agents.

Multi-agent benchmarks should measure more than task success. The frontier questions are whether agents coordinate efficiently, avoid redundant work, recover from bad messages, terminate correctly, resist adversarial participants, and handle topology or role changes.

## Evaluation Dimensions

- Collaboration quality and division of labor.
- Competition, negotiation, and strategic behavior.
- Topology sensitivity: star, chain, tree, graph, blackboard, or supervisor.
- Failure modes: specification errors, inter-agent misalignment, verification failures, and termination failures.
- Security and robustness under compromised, contradictory, or colluding agents.

[[sources/Buzz Repository]] provides a benchmark-design artifact without a benchmark result. Harbor Buzz Orchestra records the roster, endpoint/model labels, prompt hashes, generation controls, prices, and timeout; isolates trials; and preserves event and agent logs. Persona prompts specify scoped work and cross-worker verification, while the runtime gates only liveness and orchestrator-authored completion. As of the audited 2026-08-02 snapshot it publishes no score, single-agent baseline, pass rate, or cost result; ATIF and token/cost result plumbing remain incomplete. Treat it as methodology awaiting results.

## Related

- [[concepts/multi-agent systems]]
- [[methods/deliberative control]]
- [[methods/multi-agent orchestration]]

## Related Sources

- [[sources/A2ASecBench|A2ASecBench: A Protocol-Aware Security Benchmark for Agent-to-Agent Multi-Agent Systems]]
- [[sources/MultiAgentBench|MultiAgentBench: Evaluating the Collaboration and Competition of LLM agents]]
- [[sources/Magentic-One|Magentic-One: A Generalist Multi-Agent System for Solving Complex Tasks]]
- [[sources/PEAR|PEAR: Planner-Executor Agent Robustness Benchmark]]
- [[sources/TAMAS|TAMAS: Benchmarking Adversarial Risks in Multi-Agent LLM Systems]]
- [[sources/Understanding Multi-Agent LLM Frameworks|Understanding Multi-Agent LLM Frameworks: A Unified Benchmark and Experimental Analysis]]
- [[sources/Why Do Multi-Agent LLM Systems Fail|Why Do Multi-Agent LLM Systems Fail?]]
- [[sources/Buzz Repository]]
