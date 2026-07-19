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

## Context Management Benchmarks

- [[sources/LOCA-bench]]
- [[sources/ContextBench]]
- [[sources/Letta Context-Bench]]
