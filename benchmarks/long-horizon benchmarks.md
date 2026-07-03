# Long-Horizon Benchmarks

Long-horizon benchmarks measure tasks requiring many steps, tool calls, state transitions, or sustained work over time. The measurement problem is distinct from single-shot evaluation: at long horizons the binding constraints are persistence, error recovery, and memory rather than per-step competence, and individual task suites saturate quickly enough that the durable object of measurement is the trend line, not any one leaderboard.

## The METR Time-Horizon Methodology

The reference approach fits a curve instead of reporting a score: the 50%-task-completion time horizon is the human task duration at which a model succeeds half the time, fit across human-baselined task suites.

- [[sources/METR Measuring Long Task Completion]] defines the metric and the headline trend — the frontier 50% horizon has doubled roughly every 7 months since 2019 — and names the drivers: reliability, mistake adaptation, reasoning, and tool-use competence.
- [[sources/METR Time Horizon 1.1]] is the current reference: 228 tasks (8+ hour tasks doubled to 31), infrastructure migrated to [[sources/Inspect Framework]], and revised doubling estimates (~131 days since 2023, ~89 days since 2024). Frontier horizons sit in the hours — Claude Opus 4.5 at 320 minutes with a 170–729 CI — and METR flags that only 5 of 31 long tasks have measured rather than estimated human baselines, so long-horizon intervals are wide.

Two design lessons transfer. First, the methodology survives benchmark churn: tasks can be added and retired without breaking the fitted horizon, which is exactly what raw leaderboard scores cannot offer. Second, success rate is not the whole story at long horizons — [[sources/METR Frontier Risk Report 2026]] found that on >8-hour tasks at least 16% of successful runs involved cheating on review, so long-horizon scores need the transcript-inspection discipline in [[concepts/evaluator reliability]].

## Task Suites

| Suite | Horizon shape | What it isolates |
|---|---|---|
| [[sources/TheAgentCompany]] | Multi-checkpoint professional workflows across websites, code, and coworker communication | The gap between simple-task competence and full workflow completion |
| [[sources/Terminal-Bench]] | Hard multi-step terminal tasks graded by final container state | Sustained environment manipulation; its 2.1 release showed long-horizon task suites decay and need continuous validation |
| The SWE-bench line (see [[benchmarks/coding agent benchmarks]]) | Repository issues through to passing held-out tests; [[sources/SWE-bench Pro]] extends to deliberately long-horizon tasks with frontier launch scores below 25% | Long-horizon coding specifically, with the contamination and grading caveats documented in that note |
| [[sources/LongMemEval]] | Question answering over long multi-session chat histories | The memory axis: overall accuracy drops ~30% when memorizing information across sustained interactions, tested along information extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention |
| [[sources/PaperBench]], [[sources/MLR-Bench]] | Research replication and open-ended ML research | Multi-day expert work graded by rubric |
| [[sources/BrowseComp]], [[sources/OpenAI Deep Research System Card]] | Extended browsing and research sessions | Long-horizon information seeking |

## Reading Long-Horizon Scores

- Average success rates overstate deployability at long horizons; the pass^k reliability bound from [[sources/Tau-Bench]] falls much faster with task length than pass@1 suggests ([[operations/agent evals]] covers the reporting discipline).
- Run-to-run variance grows with trajectory length — [[sources/On Randomness in Agentic Evals]] shows trajectories diverge within the first few percent of tokens and cascade into different solution strategies, so long-horizon comparisons need more runs, not fewer.
- What the agent system does between steps matters as much as the model: the harness patterns for surviving long horizons live in [[concepts/long-horizon agents]] and [[operations/durable sessions]].

## Related

- [[concepts/long-horizon agents]]
- [[operations/durable sessions]]
- [[benchmarks/agent evaluation]]
- [[benchmarks/coding agent benchmarks]]
- [[concepts/evaluator reliability]]
- [[operations/agent evals]]
- [[maps/Evaluation Map]]

## Related Sources

- [[sources/Google AI Co-Scientist Article|Accelerating scientific breakthroughs with an AI co-scientist]]
- [[sources/BrowseComp|BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents]]
- [[sources/BrowseSafe|BrowseSafe: Understanding and Preventing Prompt Injection Within AI Browser Agents]]
- [[sources/OpenAI Deep Research System Card|Deep research System Card]]
- [[sources/Evaluation and Benchmarking of LLM Agents - A Survey|Evaluation and Benchmarking of LLM Agents: A Survey]]
- [[sources/LongMemEval]]
- [[sources/METR Frontier Risk Report 2026]]
- [[sources/METR Measuring Long Task Completion]]
- [[sources/METR Time Horizon 1.1]]
- [[sources/MLR-Bench|MLR-Bench: Evaluating AI Agents on Open-Ended Machine Learning Research]]
- [[sources/OWL|OWL: Optimized Workforce Learning for General Multi-Agent Assistance in Real-World Task Automation]]
- [[sources/PaperBench|PaperBench: Evaluating AI's Ability to Replicate AI Research]]
- [[sources/Cursor Multi-Agent Kernels|Speeding up GPU kernels by 38% with a multi-agent system]]
- [[sources/Terminal-Bench]]
- [[sources/TheAgentCompany|TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks]]
