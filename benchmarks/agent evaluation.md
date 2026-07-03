# Agent Evaluation

Agent evaluation measures behavior across multi-step interaction with tools, environments, users, memory, and changing state. This is the hub note for the public benchmark record; coding-specific evidence lives in [[benchmarks/coding agent benchmarks]], the operational pipeline for evaluating a system you own lives in [[operations/agent evals]], and the reliability of the measuring instrument itself lives in [[concepts/evaluator reliability]].

## Evaluation Axes

- Task success
- Tool-use reliability
- Long-horizon persistence
- Cost and latency
- Safety and policy adherence
- Robustness to prompt injection and tool failure
- Memory across sessions
- Recovery from mistakes

No single benchmark covers these axes; families divide them up.

## Benchmark Families

| Family | Grading approach | Anchors |
|---|---|---|
| Repository issue resolution | Held-out unit tests on real codebases | The SWE-bench family — full treatment in [[benchmarks/coding agent benchmarks]], including its contamination-driven retirement cycle |
| Terminal and environment work | Final container state, human-verified per task | [[sources/Terminal-Bench]] — 89 Dockerized tasks whose 2.1 release (28 of 89 tasks fixed within months) established that agentic benchmark tasks decay and need continuous validation |
| Tool-agent-user interaction | Final database state against a goal state, with an LM-simulated user and policy constraints | [[sources/Tau-Bench]] — origin of pass^k, the pessimistic all-k-of-k reliability bound; agents near 50% average success fell below 25% at pass^8 |
| Simulated workplace | Checkpointed completion of professional tasks across websites, code, and coworker communication | [[sources/TheAgentCompany]] — agents handle simpler tasks but remain weak on harder long-horizon workflows |
| Operations and SRE | Live Kubernetes environments with controlled fault injection and exported telemetry | [[sources/AIOpsLab]] — standardizes the agent-cloud interface so any agent can be benchmarked on incident detection through mitigation |
| Research and open-ended work | Rubric or replication grading | [[sources/PaperBench]] on replicating AI research; [[sources/MLR-Bench]] on open-ended ML research |
| Browsing | Hard-to-find answer retrieval | [[sources/BrowseComp]] |
| Memory | Question answering over long interactive histories | [[sources/LongMemEval]] — five memory abilities including knowledge updates and abstention; the de-facto reporting benchmark for memory systems |
| Security and control | Attack success and undetected-sabotage rates | [[sources/AgentDojo]] and [[sources/InjecAgent]] for prompt injection; [[sources/Agent Security Bench]] for formalized attack/defense; [[sources/IH-Challenge]] for instruction-hierarchy robustness training and evaluation; [[sources/LinuxArena]] for control-style monitoring of sabotage in live production environments (see [[safety/AI control]]) |

## Methodology and Validity

The benchmark record is only usable with its known defects in view.

- [[sources/AI Agents That Matter]] named the five systemic failures — accuracy-only reporting without cost, conflated audiences, inadequate holdouts, shortcut overfitting, and irreproducibility — and made the cost-accuracy Pareto frontier the correct optimization target.
- [[sources/Rigorous Agentic Benchmarks]] turned that critique into an audit checklist (task validity, outcome validity, reporting) and found 7 of 10 popular agentic benchmarks with outcome-validity flaws, including grading bugs that misestimate performance by up to 100% relative.
- [[sources/Holistic Agent Leaderboard]] is the reporting infrastructure answer: standardized rollouts across nine benchmarks, cost reported against accuracy by default, and LLM-aided transcript inspection that caught agents fetching benchmark answers instead of solving tasks.
- [[sources/Evaluation and Benchmarking of LLM Agents - A Survey]] is the academic map of the space.
- Run-to-run variance, judge bias, and gaming pressure apply to every row above; the evidence and design responses are consolidated in [[concepts/evaluator reliability]].

Because individual benchmarks saturate and decay, the durable capability trend line is the METR time-horizon methodology — [[sources/METR Measuring Long Task Completion]] defines the 50% time-horizon metric and [[sources/METR Time Horizon 1.1]] is the current reference; both are treated fully in [[benchmarks/long-horizon benchmarks]].

## Related

- [[benchmarks/coding agent benchmarks]]
- [[benchmarks/long-horizon benchmarks]]
- [[benchmarks/multi-agent benchmarks]]
- [[operations/agent evals]]
- [[concepts/evaluator reliability]]
- [[methods/deliberative control]]
- [[safety/agent safety and security]]
- [[safety/AI control]]
- [[maps/Evaluation Map]]

## Related Sources

- [[sources/Agent Security Bench|Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents]]
- [[sources/AgentDojo|AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents]]
- [[sources/AI Agent Systems - Architectures Applications and Evaluation|AI Agent Systems: Architectures, Applications, and Evaluation]]
- [[sources/AI Agents That Matter]]
- [[sources/AIOpsLab]]
- [[sources/Adding Error Bars to Evals]]
- [[sources/BrowseComp|BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents]]
- [[sources/Evaluation and Benchmarking of LLM Agents - A Survey|Evaluation and Benchmarking of LLM Agents: A Survey]]
- [[sources/Holistic Agent Leaderboard]]
- [[sources/IH-Challenge]]
- [[sources/InjecAgent|InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents]]
- [[sources/LinuxArena]]
- [[sources/LongMemEval]]
- [[sources/METR Measuring Long Task Completion]]
- [[sources/METR Time Horizon 1.1]]
- [[sources/MLR-Bench|MLR-Bench: Evaluating AI Agents on Open-Ended Machine Learning Research]]
- [[sources/On Randomness in Agentic Evals]]
- [[sources/OpenHands|OpenHands: An Open Platform for AI Software Developers as Generalist Agents]]
- [[sources/PaperBench|PaperBench: Evaluating AI's Ability to Replicate AI Research]]
- [[sources/PEAR|PEAR: Planner-Executor Agent Robustness Benchmark]]
- [[sources/Plan-Then-Execute|Plan-Then-Execute]]
- [[sources/Rigorous Agentic Benchmarks]]
- [[sources/Tau-Bench]]
- [[sources/Terminal-Bench]]
- [[sources/TheAgentCompany|TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks]]
- [[sources/AI Co-Scientist|Towards an AI Co-Scientist]]
- [[sources/Anthropic Writing Tools for Agents|Writing effective tools for agents - with agents]]
