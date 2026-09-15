# Evaluation Map

Use this as a navigation page for evaluation, benchmark families, and eval tooling. Source evidence should be reached through the benchmark notes.

Agent evaluation is one of the main mechanisms for making agent systems better: it turns tool use, autonomy, recovery, cost, and safety behavior into something that can be compared and improved.

## Core Notes

- [[benchmarks/agent evaluation]]
- [[benchmarks/coding agent benchmarks]]
- [[benchmarks/multi-agent benchmarks]]
- [[benchmarks/long-horizon benchmarks]]
- [[operations/agent evals]]
- [[concepts/evaluator reliability]]
- [[concepts/outcomes and rubric graders]]
- [[methods/deliberative control]]
- [[maps/Context Management Map]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]
- [[maps/What Makes Agent Systems Better]]

## Systems And Tooling

- [[systems/OpenHands]]
- [[systems/AI co-scientist]]
- [[concepts/tool use]]
- [[concepts/context retrieval]]

## Source Trail

Follow the related-source sections in the benchmark notes. Source cards in `sources/` hold the public evidence trail; private crawl logs and working registries stay outside this graph.

## Current Benchmark Validity Updates

- [[sources/OpenAI SWE-bench Pro Audit]] documents task and grader defects serious enough for OpenAI to retract its SWE-bench Pro recommendation.
- [[sources/DeepSWE]] uses original repository tasks and functional verifiers, and shows a large disagreement between an LLM judge and the benchmark's execution-based grader.
- [[sources/Think Big Search Small]] separates delegation quality from execution quality, making model-capacity allocation itself an evaluated system variable.
- [[sources/What Does an LLM-Agent Leaderboard Rank Actually Compare]] defines when a leaderboard difference supports a scoped superiority claim, including population, labels, coverage, and uncertainty.
- [[sources/SWE-Bench Pro Verified]] implements leakage controls and repairs selected tasks; its source card records an unresolved baseline-count inconsistency and limited repair scope.

## Alignment and Monitor Evaluation

- [[sources/OpenAI GPT-6 Astra System Card]] separates alignment measurements from declining monitorability, and documents limits of deployment simulation and peer-message evaluations.
- [[sources/Anthropic Alignment Assessment Cybersecurity Incidents]] turns incidents into tests of stopping, authorization, and simulation assumptions while retaining the limitations of resampling and model self-reports.
- [[concepts/evaluator reliability]] connects both to detector auditing and evaluation awareness; [[operations/agent evals]] translates them into regression cases.

## Context Management Benchmarks

- [[sources/LOCA-bench]]
- [[sources/ContextBench]]
- [[sources/Letta Context-Bench]]
- [[sources/Toward Reliable Context Compression for Long-Horizon Agents]]

## Harness-Conditioned Benchmarks

- [[sources/LoopsBench]] evaluates sustained coding as a model–harness–outer-loop configuration over dependency-structured work and retained regression obligations.
- [[sources/Skill-Use]] separates skill triggering, procedural compliance, and boundary adherence across models and harnesses.
- [[sources/Evo-Bench]] holds a policy model fixed while measuring whether an evolver can improve executable harness code on held-out tasks.
- [[sources/HarnessSafe]] evaluates safety across complete persistent-carrier lifecycles and treats the model–harness configuration as the comparison unit.
