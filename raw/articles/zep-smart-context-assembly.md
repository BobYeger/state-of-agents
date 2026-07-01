Today we're announcing **Smart Context Assembly**, an upgrade to how Zep's default Context Block is built. It produces a smaller Context Block: fewer tokens, and more accurate answers. The same `thread.get_user_context` call you already make now returns the new Context Block automatically, with no SDK update required. It's available now to all Zep customers.

## What Smart Context Assembly is

[Smart Context Assembly](https://help.getzep.com/retrieving-context?ref=blog.getzep.com#zeps-context-block) is the new method that builds Zep's default Context Block. It retrieves across all six of Zep's context types: facts, entities, episodes, Observations, thread summaries, and the user summary.

The previous Context Block was built by running a separate search per context type with a fixed result limit per type, then combining the results into the block. That produced the same shape regardless of the query: a fixed number of facts, a fixed number of entities, and so on. Smart Context Assembly ranks candidates from the other five types simultaneously and fills the block up to a 2,500-character budget. The block's shape adapts to each query.

![Side-by-side comparison of a legacy Context Block (longer, with content cut off by a truncation indicator) and a Smart Context Assembly Context Block (shorter, with user summary, facts, and Observations sections).](https://storage.ghost.io/c/79/c4/79c4903e-2432-4c0e-b8c8-c8988fef71ec/content/images/size/w2400/2026/06/sa-v9-comparison.png)

Side-by-side comparison of a legacy Context Block (longer, with content cut off by a truncation indicator) and a Smart Context Assembly Context Block (shorter, with user summary, facts, and Observations sections).

Smart Context Assembly is powered by [Auto Search](https://help.getzep.com/searching-the-graph?ref=blog.getzep.com#auto-search), a new graph search mode we're also announcing today. Auto Search runs the cross-scope ranking and the character-budget packing. It's also exposed as a standalone feature through `graph.search`, so you can call it directly from your own code.

## Why it matters

Smart Context Assembly produces higher-quality context per token. On the LoCoMo benchmark, that means far fewer tokens for only a small accuracy cost: it reaches 86.5% accuracy on a median of 2,680 tokens, versus 94.7% on 5,760 tokens for the legacy Context Block — 54% fewer tokens for about 8 points of accuracy.

![](https://storage.ghost.io/c/79/c4/79c4903e-2432-4c0e-b8c8-c8988fef71ec/content/images/size/w2400/2026/06/sa-benchmark-tokens-accuracy.png)

LoCoMo benchmark: Smart Context Assembly uses 2,680 median tokens at 86.5% accuracy, versus 5,760 tokens at 94.7% for the legacy Context Block — less than half the tokens at comparable accuracy.

In other runs, fewer tokens have even come with higher accuracy. On one LoCoMo run, a medium-sized legacy Context Block scored 80%, while a smaller Context Block from Smart Context Assembly scored 85%.

Fewer tokens means lower cost per call and more room in the context window for the rest of your agent’s prompt. The character budget also makes prompt sizes predictable across users and queries, so you can size context to your model and prompt budget without per-scope tuning.

## How to use it

To use Smart Context Assembly, keep calling `thread.get_user_context` as you already do; it now returns the new Context Block automatically.

```
context = client.thread.get_user_context(thread_id="thread_abc123")
print(context.context)
```

To use Auto Search directly, call `graph.search` with `scope="auto"`. The rendered Context Block comes back on `results.context`. Set `max_characters` to size it to your model's context window, and pass `return_raw_results=True` to also get the retrieved items as structured arrays.

```
results = client.graph.search(
    user_id="user_abc",
    query="What does Alice work on?",
    scope="auto",
    max_characters=4000,
)

print(results.context)
```

## Getting started

To get started, see the [Smart Context Assembly docs](https://help.getzep.com/retrieving-context?ref=blog.getzep.com#zeps-context-block). Smart Context Assembly and Auto Search are both available to all Zep customers today.