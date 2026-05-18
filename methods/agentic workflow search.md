# Agentic Workflow Search

Automated or semi-automated search over agent workflows, prompts, roles, tools, and control-flow structures.

This method treats agent design itself as an optimization problem. Instead of hand-picking one prompt chain or team structure, the system searches over workflow code, role prompts, topology, tool placement, and stopping conditions, then keeps variants that improve measured performance.

## Improvement Claim

Workflow search improves agent systems by making design choices empirical. Prompts, roles, tools, topology, and control flow become candidates to test, not assumptions to defend.

## Design Variables

- Prompt and role definitions.
- Control-flow structure: sequential, branching, voting, reflection, debate, or iterative repair.
- Agent topology and communication paths.
- Tool availability, tool order, and tool-call constraints.
- Evaluation metric, budget, and rollback policy.

## Related Sources

- [[sources/AFlow|AFlow: Automating Agentic Workflow Generation]]
- [[sources/ADAS|Automated Design of Agentic Systems]]
- [[sources/HALO|HALO: Hierarchical Autonomous Logic-Oriented Orchestration for Multi-Agent LLM Systems]]
- [[sources/Karpathy Autoresearch|autoresearch]]
