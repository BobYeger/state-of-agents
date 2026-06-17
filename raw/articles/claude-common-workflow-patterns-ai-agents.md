# Common workflow patterns for AI agents—and when to use them

Source URL: https://claude.com/blog/common-workflow-patterns-for-ai-agents-and-when-to-use-them

Capture date: 2026-06-17

Capture note: concise local research snapshot from the public Claude Blog page. The source card should cite the canonical URL for the full article.

## Core framing

Claude Blog frames workflows as structure around agent autonomy. A workflow defines the overall process, checkpoints, and boundaries while each step can still use agent reasoning and tool calls.

The article gives a production selection guide for three common workflow patterns:

| Pattern | Use when | Avoid when | Main tradeoff |
|---|---|---|---|
| Sequential | Steps have clear dependencies and later stages need earlier outputs. | A single agent can handle the task or the work needs collaboration rather than handoff. | Better focus and accuracy at the cost of latency. |
| Parallel | Subtasks are independent, multiple perspectives help, or latency is the bottleneck. | Agents need cumulative context, quotas/cost make concurrency wasteful, or aggregation is unclear. | Faster completion and separation of concerns at the cost of more calls and synthesis complexity. |
| Evaluator-optimizer | Quality criteria are clear and first drafts are not good enough. | First-attempt quality is sufficient, deterministic tools are better, criteria are subjective, or real-time response is required. | Higher quality through feedback loops at the cost of extra tokens, latency, and stop-policy design. |

## Decision heuristics

- Try the task as a single agent call first.
- Default to the simplest workflow that reaches the quality bar.
- Use sequential workflows when task dependencies are real.
- Use parallel workflows only when work can be split independently and the aggregation strategy is known.
- Use evaluator-optimizer loops only when the quality improvement can be measured.
- Define failure handling, retries, latency/cost limits, baselines, and stopping criteria before adding workflow complexity.

## Harness relevance

This source is useful for harness engineering because workflow choice determines where state moves, when agents run, how results aggregate, and what stops the run. The article turns "use multiple agents" into a bounded design decision: dependencies, independence, quality criteria, latency, token cost, and observability decide the pattern.

## Local connections

- [[sources/Anthropic Building Effective Agents]] is the broader architecture taxonomy.
- [[sources/Anthropic Multi-Agent Coordination Patterns]] extends the conversation toward persistent multi-agent coordination structures.
- [[sources/Claude Code Workflows]] shows one implementation surface where workflow scripts make orchestration state explicit.
- [[sources/Cloudflare Dynamic Workflows]] shows the durable-infrastructure version of workflow orchestration.
