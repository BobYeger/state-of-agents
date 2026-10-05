---
title: "Programmatic Tool Calling"
aliases:
  - "Code-based tool orchestration"
tags:
  - agents/tools
updated: 2026-10-05
---

# Programmatic Tool Calling

Programmatic tool calling lets an agent write code that calls tools, loops over results, filters noisy outputs, and returns only useful information to the model.

This differs from one-tool-call-at-a-time function calling. It moves intermediate computation into an execution runtime, reducing context pressure and model round trips while making tool orchestration more inspectable.

## Research Before the Current Services

[[sources/LLMCompiler]] (December 2023 preprint; June 2024 revision) tests an explicit dependency graph: a model plans calls, a scheduler dispatches ready work, and results unblock downstream operations. [[sources/CodeAct]] (February 2024 preprint) tests executable Python as the model's action representation, including control flow and correction from interpreter feedback. These are related but distinct decisions: scheduling a graph does not require unrestricted generated code, and generated code does not automatically have a correct dependency graph.

[[sources/Toolformer]] supplies an earlier boundary: learning useful individual calls did not establish chained or interactive tool use. The later papers test orchestration mechanisms that an isolated call-selection benchmark cannot establish.

[[sources/Cloudflare Code Mode MCP]] (September 2025) contributes a concrete engineering experiment: convert MCP schemas into a TypeScript API and run generated code against it. [[sources/Cloudflare Code Mode MCP API]] (February 2026) then places discovery and execution behind two server tools. These are implementation comparisons with the research, not evidence of direct historical causation. [[sources/Anthropic Code Execution with MCP]] and [[sources/OpenAI Programmatic Tool Calling]] document other implementations of the same broad design space.

## Choose the Execution Shape

| Shape | Useful when | Main question to verify |
|---|---|---|
| Direct model tool calls | Each observation needs interpretation or changes the next action | Did the model actually inspect the result before deciding? |
| Generated program | Bounded loops, filtering, joins, and deterministic transformations dominate | Did the program preserve the intended data and obey runtime limits? |
| Planned dependency graph | Independent calls can run concurrently and dependencies are explicit | Are both data dependencies and conflicting side effects represented? |
| Hybrid | A bounded computation can return a compact result before the next semantic decision | Where must control return to the model or user? |

This table is an architectural synthesis. The strongest evidence comes from matching the experimental workload to the proposed execution shape, rather than treating a paper's maximum speedup as a property of every agent.

The boundary is task-shaped rather than vendor-shaped. [[sources/OpenAI Programmatic Tool Calling]] recommends generated code for bounded control flow and structured operations such as filtering, joining, ranking, deduplication, and aggregation. It recommends direct model tool calls where each result needs semantic judgment, the action needs approval, or final citations and native artifacts must be preserved. The program runtime is still an untrusted caller: application-side permission checks, idempotency, and approval gates remain necessary.

## Evidence and Runtime Boundaries

CodeAct's success-rate comparisons and LLMCompiler's latency/cost experiments support testing the representation and scheduler separately. Cloudflare's fixed schema footprint measures a different quantity: it does not include every discovery result, generated program, or tool observation in the eventual task.

Authority follows execution. Every operation reached inside a generated loop needs the same scope checks as a directly invoked tool. A model-visible `execute` wrapper can conceal a large executable surface; the wrapper's small schema is no proof of restricted authority. [[sources/Atomix]] explains the additional concurrency problem: a syntactically valid plan can still leave partial writes, stale effects, or irreversible sends. A sandbox limits reachable resources; it does not make allowed effects atomic.

## Research Questions

- Under equal task success and total budget, when does code composition beat direct calls or a dependency scheduler?
- Which intermediate results must return to the model for judgment, citation, or approval?
- Can a generated program resume after partial failure without duplicating external effects?
- How do we evaluate filtering that saves tokens but accidentally removes decisive evidence?

## Related Sources

- [[sources/Anthropic Code Execution with MCP]]
- [[sources/Cloudflare Code Mode MCP]]
- [[sources/Cloudflare Code Mode MCP API]]
- [[sources/LangChain Deep Agents v0.6]]
- [[sources/OpenAI Responses API Computer Environment]]
- [[sources/OpenAI Programmatic Tool Calling]]
- [[sources/OpenAI GPT-5.6]]
- [[sources/CodeAct]]
- [[sources/LLMCompiler]]
- [[sources/Toolformer]]
- [[sources/Atomix]]

## Related

- [[concepts/tool use]]
- [[concepts/dynamic tool discovery]]
- [[concepts/agent operating surfaces]]
- [[operations/agent harnesses]]
- [[operations/cost control]]
- [[operations/permissions]]
- [[operations/sandboxes]]
- [[concepts/tool-use contracts]]
