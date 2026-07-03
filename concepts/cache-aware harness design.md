# Cache-Aware Harness Design

Cache-aware harness design treats the KV cache as a first-order constraint on how a harness assembles context: prompt ordering, tool exposure, and context edits are chosen to keep the token prefix stable across iterations, so that repeated inference over a growing transcript is billed and served as cache reads rather than fresh computation.

The reason this is a design concept and not a billing detail is the shape of an agent loop. Each iteration replays the entire transcript so far plus one new observation, which makes the workload overwhelmingly prefix-heavy. [[sources/Manus Context Engineering]] quantifies it: a typical task takes ~50 tool calls at a ~100:1 input-to-output token ratio, cached input costs 10x less than uncached, and the essay calls KV-cache hit rate "the single most important metric for a production-stage AI agent". [[sources/Claude API Prompt Caching]] gives the pricing mechanics behind that ratio: cache reads cost 0.1x base input, while writes cost 1.25x (5-minute TTL) or 2x (1-hour TTL) — so the economics only work when the same prefix is read many times.

## Design Rules

| Rule | Mechanism | Evidence |
|---|---|---|
| Order the prefix by stability | The cache hierarchy is tools -> system -> messages; a change high in the hierarchy invalidates everything downstream | [[sources/Claude API Prompt Caching]]: a tool-definition change invalidates the whole cache, while a `tool_choice` change invalidates only messages |
| Keep context append-only | Never edit or reorder earlier messages; only add to the end | [[sources/Claude API Prompt Caching]]: the top-level `cache_control` field auto-advances the breakpoint along the growing suffix — the API-native pattern for append-only loops |
| Place breakpoints deliberately | At most 4 explicit cache breakpoints per request; separate the segments that change at different rates | [[sources/Claude API Prompt Caching]]; [[sources/Claude API Compaction]]: put a breakpoint on the compaction block and keep the system prompt cached separately |
| Mask tools instead of removing them | Constrain tool choice per step without touching the tool definitions that head the prefix | [[sources/Manus Context Engineering]]: logit masking via a context-aware state machine, precisely because add/remove mid-loop invalidates the cache |
| Inject late instructions without prefix edits | Mid-conversation `{role: system}` messages add instructions while leaving the cached prefix intact | [[sources/Claude API Prompt Caching]] (Opus 4.8 feature) |
| Pre-warm predictable prefixes | Write the cache before the first real request | [[sources/Claude API Prompt Caching]]: a `max_tokens: 0` request writes the cache without sampling |

The masking rule is the sharpest tradeoff in the table. [[concepts/dynamic tool discovery]] argues for exposing tools on demand to keep the action space small; cache-aware design pushes the other way, because tool definitions sit at the top of the prefix hierarchy where any change is maximally expensive. Masking resolves the tension: the full tool set stays in the (cached) prefix, and availability is enforced at decode time.

## Compaction Is a Planned Cache Invalidation

Compaction rewrites history, so it is by definition a cache-destroying event; cache-aware design makes it a scheduled one rather than an accident. [[sources/Claude API Compaction]] documents the coordination pattern for server-side compaction: the compaction block gets its own `cache_control` breakpoint and the system prompt is cached separately, so the stable head of the prompt survives the rewrite and only the summarized middle is re-written to cache. [[sources/Claude Code Prompt Caching]] shows the same accounting at the harness level: compaction has runtime cost and cache consequences, not only semantic consequences, and the harness orders its prompt layers accordingly.

This is also why compaction frequency is a cost lever, not just a context-quality lever: each compaction pays a full re-write of the post-compaction prefix, so a harness that compacts eagerly can spend more on cache writes than it saves on input tokens.

## In-Turn Token Budgeting

A high cache hit rate makes appended tokens cheap, not free — every appended token is re-read on every subsequent iteration of the loop, so a bloated observation is paid for ~once per remaining step. Cache-aware harnesses therefore budget what each turn is allowed to append:

- **Restorable truncation.** [[sources/Manus Context Engineering]] drops bulky observations (page content) while keeping the handle to re-fetch them (the URL), so the append stays small without irreversible loss.
- **Observation hygiene.** [[concepts/observation masking]] and [[concepts/tool-result clearing]] cover reducing stale tool output; the cache constraint says to do this by appending less in the first place, or clearing in bulk at a compaction boundary, rather than editing history piecemeal.
- **Explicit triggers.** [[sources/Claude API Compaction]] exposes the overflow budget directly: compaction fires at a configurable input-token trigger (default 150,000), which turns "how much may the transcript grow" into a set parameter instead of an emergent outcome.

## The Counterweight: Cache Hits Are Not Context Quality

Append-only context maximizes cache hits while monotonically growing the transcript, and long context measurably degrades models. [[sources/Context Rot]] shows all 18 tested models degrade as input length grows, with focused ~300-token prompts consistently beating ~113k-token full prompts; [[sources/Lost in the Middle]] shows the positional half of the problem, with mid-context information costing 20+ points on multi-document QA. A harness tuned only for cache hit rate will drift toward exactly the long, distractor-laden contexts these studies show performing worst.

The design space is therefore a three-way tradeoff — cache hit rate, context quality, and token spend — and the resolutions live at different layers: append-only with restorable truncation inside a context window, compaction at planned boundaries, and [[concepts/handoff over compaction]] when a fresh context seeded from durable artifacts beats any rewrite. A recited plan file ([[sources/Manus Context Engineering]]'s continuously rewritten todo.md, appended rather than edited in place) counters mid-context drift without breaking the prefix.

## Failure Modes

- **Churned prefix.** Anything non-deterministic in the system prompt or tool serialization (timestamps, unordered maps, per-request IDs) silently drops the hit rate toward zero, multiplying input cost by ~10x ([[sources/Manus Context Engineering]], [[sources/Claude API Prompt Caching]]).
- **Editing history to tidy it.** Rewriting earlier messages breaks the cache and, when the edit removes failed actions, also removes the evidence the model needs to stop repeating them ([[sources/Manus Context Engineering]]).
- **Tool churn mid-loop.** Adding or removing tool definitions between steps invalidates the entire cache on every change; mask instead ([[sources/Manus Context Engineering]]).
- **Hoarding because it is cached.** Cheap re-reads invite unbounded transcripts; length-driven degradation arrives regardless of price ([[sources/Context Rot]]).
- **Over-paying for TTL.** 1-hour cache writes cost 2x base input; paying that for sessions that iterate every few seconds, or writing cache for prefixes read once, inverts the economics ([[sources/Claude API Prompt Caching]]).

## Related

- [[operations/agent harnesses]]
- [[operations/harness fault tolerance]]
- [[operations/cost control]]
- [[concepts/context engineering]]
- [[concepts/context compaction]]
- [[concepts/handoff over compaction]]
- [[concepts/observation masking]]
- [[concepts/tool-result clearing]]
- [[concepts/dynamic tool discovery]]
- [[maps/Context Management Map]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
