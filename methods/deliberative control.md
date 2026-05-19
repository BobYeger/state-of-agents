# Deliberative Control

Deliberative control separates deciding from doing. In agent systems this appears as plan-then-execute, planner-executor, planner-executor-verifier, supervisor-worker, leader-worker-verifier, plan/act modes, and explicit System-2 deliberation before action.

The core idea is not simply to add another agent. It is to make control flow explicit: a planner or deliberator chooses a strategy, an executor acts in the environment, and a verifier, critic, evaluator, or human gate checks whether the work should continue, revise, stop, or escalate.

## Pattern

| Role | Responsibility |
|---|---|
| Deliberator / Planner | Decompose the task, choose strategy, create a plan or DAG, set dependencies and constraints. |
| Executor / Worker | Perform local subtasks, call tools, search, edit files, run code, and produce structured outputs. |
| Verifier / Critic / Evaluator | Check outputs, validate contracts, run tests, detect unsafe or low-quality work, and trigger repair. |
| Coordinator / Sequencer | Manage state, route messages, decide when to replan, stop, retry, or ask a human. |

## Improvement Claim

Deliberative control improves agent systems when the task benefits from planning before action, structured handoffs, verification, or security boundaries. It is especially useful for long-horizon, tool-heavy, web-facing, safety-sensitive, or multi-agent tasks where uncontrolled ReAct-style loops can drift or be manipulated by observations.

## Failure Modes

- Bad plans can create misplaced user trust or lock the executor into a brittle path.
- Planner-stage compromise is high leverage because the planner controls downstream execution.
- Extra planner/verifier roles add latency and coordination cost when the task is simple.
- Verification only helps when the verifier has real authority, signal, and access to relevant evidence.

## Related

- [[methods/multi-agent orchestration]]
- [[methods/runtime supervision]]
- [[methods/runtime routing]]
- [[methods/multi-agent learning]]
- [[operations/agent harnesses]]
- [[operations/agent observability]]
- [[operations/agent evals]]
- [[concepts/human-in-the-loop agents]]
- [[operations/permissions]]
- [[safety/agent safety and security]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
- [[claims/Claim - Agent systems improve when structure matches the task]]
- [[maps/What Makes Agent Systems Better]]

## Related Sources

- [[sources/On Three-Layer Architectures]]
- [[sources/Anthropic Building Effective Agents]]
- [[sources/Anthropic Think Tool]]
- [[sources/Anthropic Harness Design Long-Running Apps]]
- [[sources/MiniMax Agent Team]]
- [[sources/OpenClaw Agent Harness Plugins]]
- [[sources/SAND]]
- [[sources/Plan-Then-Execute]]
- [[sources/Learning to Deliberate]]
- [[sources/Architecting Resilient LLM Agents]]
- [[sources/PEAR]]
- [[sources/VeriMAP]]
- [[sources/AgentFlow]]
- [[sources/Lazy Agents to Deliberation]]
- [[sources/HiPER]]
- [[sources/MADRA]]
- [[sources/Web Agents Plan-Then-Execute]]
