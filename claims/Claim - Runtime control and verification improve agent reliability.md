# Claim - Runtime Control And Verification Improve Agent Reliability

Agent systems improve when runtime behavior is supervised, pruned, verified, and stopped deliberately. Reliability comes less from adding more agents and more from controlling when agents speak, when they are silenced, how outputs are checked, and how failure is detected.

## Supporting Sources

- [[sources/Why Do Multi-Agent LLM Systems Fail]] identifies verification and termination failures as core MAS failure modes.
- [[sources/Stop Wasting Your Tokens]] introduces runtime supervision to intervene, reduce misinformation propagation, and cut waste.
- [[sources/AgentDropout]] shows redundant agents and communication can be removed dynamically.
- [[sources/Multi-Agent Collaboration via Evolving Orchestration]] supports adaptive orchestration instead of fixed execution.
- [[sources/MiniMax Agent Team]] is a concrete Leader / Worker / Verifier runtime pattern.
- [[sources/VeriMAP]] shows planning can produce verification functions and structured I/O for subtasks.
- [[sources/PEAR]] shows planner-stage attacks can be especially dangerous in planner-executor agents.
- [[sources/AgentFlow]] treats planner, executor, verifier, and generator roles as an optimizable live system.
- [[sources/Claude Managed Agents Define Outcomes]] makes the definition of done executable through rubric-driven artifact evaluation and repair feedback.
- [[sources/Claude Code Hooks]] makes lifecycle control explicit: hooks can block tool calls, inject context, enforce stop conditions, gate task completion, and log hook execution.
- [[sources/Anthropic Building Effective AI Agents eBook]] treats observability, auditability, quality gates, failure handling, and cost visibility as production requirements for workflow and multi-agent systems.
- [[sources/Claude Common Workflow Patterns for AI Agents]] emphasizes stopping criteria, measurable quality thresholds, fallback behavior, retry logic, and aggregation strategy before adding workflow complexity.
- [[sources/Cursor Building Better Bugbot]] and [[sources/Cursor Bugbot Learned Rules]] show production improvement through eval loops and feedback.
- [[sources/Anthropic Demystifying Agent Evals]] makes agent evals a design practice for multi-turn, tool-using behavior.
- [[sources/OpenAI Codex Using Goals]] makes completion criteria, lifecycle state, budget limits, and evidence checks first-class thread state for Codex continuation.
- [[sources/OpenRouter Fusion Beats Frontier]] shows runtime selection and synthesis as a controllable path: a base model can use Fusion selectively for high-value questions, with benchmark contamination controls and per-task cost/latency tradeoffs.
- [[sources/Claude Fable 5 Prompting Guide]] reports that auditing status claims against actual tool results nearly eliminated fabricated progress in Anthropic's tests and recommends fresh-context verifier subagents for long runs.
- [[sources/OpenAI GPT-5.6 System Card]] documents over-persistence producing destructive out-of-scope actions, credential misuse, fabricated research, and false completion claims, while reasoning-aware monitors outperformed action-only monitoring in external tests.
- [[sources/OpenAI Programmatic Tool Calling]] preserves direct calls and application approval for writes, semantic judgment, citations, and other stages where code-mediated control flow would weaken authorization or evidence.
- [[sources/OpenAI SWE-bench Pro Audit]] and [[sources/DeepSWE]] show that verification infrastructure itself must be audited: inherited tests can reject valid alternatives or pass incomplete work, while implementation-independent functional verifiers reduce but do not eliminate disagreement.
- [[sources/Factory How Missions Work]] defines observable correctness before feature decomposition, separates implementation from acceptance authority, and converts validator findings into bounded repair work; its reported convergence remains a single vendor case rather than a controlled comparison.

## Design Implications

- Build verifier, critic, evaluator, or monitor roles only where they have clear authority and signal.
- Track stopping conditions and failure modes as first-class state.
- Use dropout, routing, and supervision to reduce redundant conversation.
- Treat cost, latency, and error propagation as reliability concerns, not only operational concerns.
- Require externally checkable evidence before accepting progress, success, or completion reports.

## Related

- [[maps/What Makes Agent Systems Better]]
- [[methods/deliberative control]]
- [[methods/hook-based control]]
- [[methods/runtime supervision]]
- [[methods/runtime routing]]
- [[concepts/outcomes and rubric graders]]
- [[operations/agent observability]]
- [[operations/agent evals]]
- [[operations/cost control]]
