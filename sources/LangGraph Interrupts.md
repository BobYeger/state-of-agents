---
title: "LangGraph Interrupts (human-in-the-loop pause/resume)"
aliases:
  - "LangGraph interrupt()"
  - "LangGraph human-in-the-loop interrupts"
source_type: "docs"
kind: "interrupt-resume"
status: "verified"
year: 2026
publication_date: "2026-07"
publication_date_basis: "docs_access_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "LangChain"
venue: "LangChain Docs (docs.langchain.com)"
url: "https://docs.langchain.com/oss/python/langgraph/interrupts"
pdf_url: ""
artifacts:
  - "raw/docs/langgraph-interrupts.md"
created: 2026-07-03
updated: 2026-07-05
---

# LangGraph Interrupts

## Summary

- `interrupt()` works by throwing a special exception that propagates up the stack; the runtime catches it, pauses the graph, and persists exact state via a mandatory checkpointer, with `thread_id` as the persistent cursor for resume.
- Resume semantics: re-invoke with `Command(resume=value)`; the value becomes the return value of the `interrupt()` call — but the runtime restarts the entire node from the beginning, not from the interrupt line, so pre-interrupt code re-executes and must be idempotent (side effects belong after the interrupt).
- Multiple interrupts in one node are matched strictly by index (order-sensitive); parallel-branch interrupts resume via a dict mapping interrupt ids to values: `Command(resume={i.id: answer})`.
- Surface area: `graph.invoke()` returns interrupts under `result["__interrupt__"]`; `stream_events(version="v3")` exposes `stream.interrupts` and a boolean `stream.interrupted` for loop-until-done clients.
- Documented anti-patterns: never wrap `interrupt()` in a bare try/except, never conditionally skip interrupt calls, never loop interrupts with `while True` (use conditional edges); only JSON-serializable values may be passed.
- Static `interrupt_before`/`interrupt_after` at compile time are explicitly demoted to debugging tools, not recommended for production human-in-the-loop.

## Claims

- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[concepts/human-in-the-loop agents]]
- [[operations/durable sessions]]
- [[protocols/AG-UI]]
- [[sources/LangGraph Docs]]
- [[sources/AG-UI Protocol]]
- [[sources/Claude Managed Agents Session Event Stream]]

## Artifacts

- [[raw/docs/langgraph-interrupts.md]]

## Notes

- Canonical URL: https://docs.langchain.com/oss/python/langgraph/interrupts
- The node-restart resume model (whole node re-executes from the top) is the key mechanic AG-UI's 2026 interrupt lifecycle and CopilotKit build on, and the reason the docs demand idempotent pre-interrupt code.
- Living docs page with no visible publication date; the date above is the access date, and details are specific to the Python OSS docs.
