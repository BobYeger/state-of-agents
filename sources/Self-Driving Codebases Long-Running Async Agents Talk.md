---
title: "Building Towards Self-Driving Codebases with Long-Running, Asynchronous Agents"
aliases: ["Staying in the context window means staying in distribution", "Self-Driving Codebases talk"]
source_type: "talk"
creator: "NVIDIA Developer (channel); content reflects Cursor's self-driving-codebases framing"
url: "https://www.youtube.com/watch?v=2Fp3jIrFTMo"
created: 2026-06-23
updated: 2026-06-23
---

# Building Towards Self-Driving Codebases with Long-Running, Asynchronous Agents

## Summary

- Long-running agents can spend millions of tokens; the load-bearing risk is **divergence over long runs**, not only time or cost.
- Headline framing: **staying within the context window means staying in distribution.** Models are trained on their context window, so preserving/curating context keeps the agent closer to its training distribution and reduces divergence. This is the deeper "why" behind context engineering — adjacent to, and sharper than, attention-based "context rot".
- **Subagents are the simplest multi-agent setup**: a main agent spawns subagents, each working one problem inside its own context window — i.e., each subagent stays in distribution. This frames multi-agent systems as a **dynamic spawning pattern**, not a fixed architecture.
- Roles shown: Worker, Researcher, Reviewer; with Cursor's planner pattern (Planner → Subplanner).
- Three execution approaches (mirroring the standard workflow patterns): **Sequential** (step B depends on step A; the last step is the "final destination"), **Parallel** (speed, can be async; subagents handle different aspects; outputs may be rated; needs an aggregation strategy), and **Evaluator-optimize** (two agents; needs evaluation/quality criteria).

## Claims

- [[claims/Claim - Context management is an agent architecture choice]]
- [[claims/Claim - Agent systems improve when structure matches the task]]
- [[claims/Claim - More agents are not automatically better]]

## Connections

- [[concepts/subagent context isolation]] — separate context window per subagent = staying in distribution
- [[concepts/long-horizon agents]] — divergence over long runs
- [[concepts/context engineering]] · [[concepts/context compaction]]
- [[concepts/multi-agent systems]] · [[methods/multi-agent orchestration]]
- [[sources/Cursor Self-Driving Codebases]] — same self-driving-codebases / planner-subplanner framing
- [[sources/Anthropic Building Effective Agents]] — the sequential / parallel / evaluator-optimizer workflow patterns

## Notes

- Source: talk on the NVIDIA Developer YouTube channel, "Building Towards Self-Driving Codebases with Long-Running, Asynchronous Agents" (https://www.youtube.com/watch?v=2Fp3jIrFTMo). Content relayed from the talk; the "self-driving codebases" term and the Planner → Subplanner pattern are Cursor's.
- Talk use: the "context window = in-distribution / divergence" framing is the unifying *why* for the harness/context half of the talk (sections 3, 5, 6) and the bridge to multi-agent (section 7): subagents help because separate context windows keep each one in distribution. The execution trio (sequential/parallel/evaluator-optimize) already appears via [[sources/Anthropic Building Effective Agents]]; this source reinforces it rather than adding a new pattern.
