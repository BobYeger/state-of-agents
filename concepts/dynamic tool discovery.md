---
title: "Dynamic Tool Discovery"
aliases:
  - "Runtime tool discovery"
tags:
  - agents/tools
updated: 2026-10-05
---

# Dynamic Tool Discovery

Dynamic tool discovery lets agents retrieve, request, or search for tools at runtime instead of loading every possible tool definition into context.

The design goal is to preserve context budget and autonomy as tool ecosystems grow. The failure mode is hidden tool mismatch: the agent may choose poorly, retrieve stale capabilities, or miss a necessary tool unless retrieval and tool metadata are evaluated.

## Separate the Mechanisms

| Mechanism | What changes | What it does not establish |
|---|---|---|
| Tool/document retrieval | Candidates found from a catalog or documentation index | Correct arguments, successful execution, or permission |
| Deferred schema exposure | Which already-known definitions enter model context now | A new executable capability or a new authorization grant |
| Capability definition changes | Definitions offered during the session, including new schemas or versions | That the remote implementation stayed unchanged |
| Registry synchronization and listing pinning | Freshness of the catalog, or stability of the offered definitions across requests | Transactional consistency or safe replay of external effects |
| Execution-time authority | Which actor may execute which operation on which resource | A retrieval problem; this requires runtime enforcement |

These are architectural distinctions, not interchangeable product names. A tool can be discoverable but unauthorized, authorized but absent from context, or correctly retrieved with an obsolete schema.

## Research Before the Current Services

The sequence below records earlier experiments and later implementations. It does not claim that a vendor inherited an idea from a particular paper.

| Source | Question it tested or implemented | Evidence boundary |
|---|---|---|
| [[sources/Toolformer]] (2023) | Can a model learn useful tool-call decisions from self-generated examples? | Predefined tools; training-time call learning rather than catalog discovery |
| [[sources/Gorilla]] (2023) | Can retrieved documentation improve API calls and adapt them to changed documentation? | Retrieval quality matters; generated ML API calls rather than full workflow execution |
| [[sources/AnyTool]] (2024) | Can hierarchical agents retry discovery when the initial candidates cannot solve a request? | End-to-end API benchmarks, with substantial repeated-call cost |
| [[sources/ScaleMCP]] (May 2025) | Can agents re-query an automatically synchronized MCP catalog? | Constructed financial tools; answer quality and correct tool use diverge |
| [[sources/MCP-Zero]] (June 2025) | Can the model describe a missing capability and request it on demand? | Retrieval and tool-context experiments; broader execution reliability remains open |
| [[sources/Cloudflare Code Mode MCP API]] (February 2026) | Can code search a large API specification behind a small fixed MCP surface? | Deployed engineering design and schema-size measurements |
| [[sources/Claude Mid-Conversation Tool Definitions]] (September 22, 2026) | Can a conversation acquire new definitions without rewriting its cached prefix? | API contract for mutation and MCP listing pinning, not retrieval-quality evidence |

[[sources/Anthropic Advanced Tool Use]] provides the complementary deferred-loading implementation: selecting what to reveal from a catalog is different from the newer ability to define something not present at session start. [[concepts/programmatic tool calling]] addresses how selected operations execute together.

## What to Measure

Evaluate the whole chain: required-tool recall, correct schema/version, argument correctness, completed user outcome, and total cost including discovery. Keep retrieval failures visible: AnyTool shows why a grader must not reward a request merely because it is judged unsolvable with the tools retrieved.

Cache savings need their own accounting. A smaller exposed schema can reduce prompt size while additional retrieval turns increase latency. Pinning an old listing can preserve reproducibility while allowing it to become stale. Neither optimization decides whether an action is authorized.

## Research Questions

- When should the agent search again, broaden the catalog, or report a genuinely missing capability?
- How does retrieval perform on human requests, ambiguous tool names, and changed schemas rather than synthetic descriptions that resemble the index?
- Can a session retain a reproducible definition history while refreshing capabilities that changed on the server?
- How should discovered tools carry provenance, allowed resource scope, and expiry into the execution layer?

## Related Sources

- [[sources/MCP-Zero]]
- [[sources/ScaleMCP]]
- [[sources/Anthropic Advanced Tool Use]]
- [[sources/Anthropic Code Execution with MCP]]
- [[sources/Cloudflare Code Mode MCP API]]
- [[sources/OpenAI Agents SDK Tools]]
- [[sources/Toolformer]]
- [[sources/Gorilla]]
- [[sources/AnyTool]]
- [[sources/Claude Mid-Conversation Tool Definitions]]

## Related

- [[concepts/tool use]]
- [[concepts/agent operating surfaces]]
- [[protocols/MCP]]
- [[operations/cost control]]
- [[concepts/programmatic tool calling]]
- [[concepts/cache-aware harness design]]
- [[concepts/tool-use contracts]]
- [[operations/permissions]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
