Title: Using a transformer–based text embeddings model to reduce Sentry alerts by 40% and cut through noise

URL Source: https://blog.sentry.io/how-sentry-decreased-issue-noise-with-ai/

Published Time: 2025-02-05T09:32

Markdown Content:
Sentry uses [Issue Grouping](https://docs.sentry.io/concepts/data-management/event-grouping/) to aggregate identical errors and prevent duplicate issues from being created, and duplicate alerts being sent.

One of the chief complaints we’ve [heard from our users](https://github.com/getsentry/sentry/discussions/66319) is that in some cases the existing algorithm did not sufficiently group similar errors together, and Sentry would create separate issues and alerts, causing unnecessary disruption–or at least annoyance–to developers.

To address that, we recently deployed the largest ever improvement to our issue grouping algorithm. Our new, AI-powered approach uses a transformer–based text embeddings model to achieve a **40% reduction in new issues created**, while maintaining sub-100ms end-to-end processing latency.

In this article, we’ll review the process of developing, testing, and deploying AI-powered issue grouping.

## Why duplicate issues happen

The core value proposition of Sentry is that you don’t have to sift through logs to find what you’re looking for. When a new problem occurs, it ends up on your [issues feed](https://docs.sentry.io/product/issues/) and in your email or messaging platform. The key to all of this is the grouping algorithm. While it’s relatively straightforward for an experienced developer to look at two different stack traces and decide whether or not they represent the same issue, translating the process into robust heuristics is a deceptively complex problem.

Consider a React application where the same “Invalid prop” error can manifest with different stack frame orderings. The error might first appear in `validateProp(Select.js:42)` followed by `Anonymous Component(App.js:123)`, or vice versa. Similarly, in Python applications, what appears to be the same `KeyError` might occur with slightly different line numbers (`line 145` vs `line 147`) due to code refactoring. Async operations add even more complexity, where identical errors can surface through different execution paths–for instance, a `ValueError` in a Python async function might bubble up through either `asyncio/tasks.py` or `asyncio/runners.py`. Our grouping algorithm needs to recognize these variations as manifestations of the same underlying issue while still maintaining the ability to distinguish genuinely different errors.

On top of this, Sentry is both fast and efficient. Our grouping algorithm must not significantly slow down event ingestion or make it too expensive.

## The problem with the existing grouping solution

Our traditional grouping algorithm operates by generating [unique fingerprints](https://docs.sentry.io/concepts/data-management/event-grouping/#default-error-grouping-algorithms) for each error through a cascade of increasingly broad matching strategies. Starting with stack traces (the most precise method), the algorithm examines each frame–carefully distinguishing between application code and third-party libraries–and normalizes them according to platform-specific rules. For example, we handle Python tracebacks differently than minified JavaScript stack traces. When stack traces aren’t available or sufficient, the system falls back to examining exception types and values, and as a last resort, uses normalized versions of error messages.

The final output is a “fingerprint”, or “hash”, representing the error. Ideally, if another error caused by the same stack trace comes in, it will have the same fingerprint and is grouped together accordingly.

This layered approach, refined over years of real-world usage, helps ensure that related errors get grouped together while distinct issues remain separate.

## Our initial attempts at improving grouping

Our primary goal was to introduce a more principled _similarity_ metric for issues–that way we can avoid relying on increasingly convoluted heuristics to pre-process the stack traces, and instead simply merge stack traces that look sufficiently similar to each other. This led us to explore text similarity metrics, particularly[Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance), which measures the minimum number of single-character edits required to transform one string into another. This approach provides an intuitive and precise way to quantify how different two stack traces were, but these comparisons are impossibly inefficient to run at scale.

To address the performance challenges, we evaluated[Locality Sensitive Hashing](https://en.wikipedia.org/wiki/Locality-sensitive_hashing) (LSH). Rather than computing exact edit distances, LSH projects text into a space where similar text is likely to hash to the same or nearby buckets. For stack traces, this involves breaking them into n-grams or shingles (overlapping sequences of frames) and using[MinHash](https://en.wikipedia.org/wiki/MinHash) to approximate set similarity. This allowed us to efficiently find candidate matches without having to compare each new error against our entire corpus.

However, we found that text similarity–whether computed exactly or approximated via LSH–was an imperfect proxy for actual error similarity. Stack traces that appeared very similar textually could represent fundamentally different error conditions if they diverged at critical points (like the root exception type or the triggering frame). Conversely, traces that appeared quite different by edit distance might represent the same underlying error, just with different variable names or line numbers due to code changes.

We needed an approach that could capture the semantic structure of errors, not just their textual similarity.

## Landing on an AI-powered solution

Our final architecture should feel familiar to anyone building modern [Retrieval-Augmented Generation (RAG)](https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/) systems. At its core is a fine-tuned, transformer-based, text embeddings model that encodes stack traces into vectors capturing the semantic essence of each error.

This approach outperforms simplistic edit-distance measures because the transformer’s attention mechanism helps _tune out_ noisy variations—like shifting line numbers—and concentrate on meaningful signals that indicate genuine error similarity.

Sentry is both open source as well as a heavy user of Postgres, so the fantastic[pgvector](https://github.com/pgvector/pgvector) extension was an easy choice for vector search (we used a[HNSW](https://www.pinecone.io/learn/series/faiss/hnsw/) index) and storage.

The architecture is relatively simple: when our existing, cost-effective fingerprinting algorithm detects a new hash (generated by our existing grouping system), it sends the error data to[Seer](https://github.com/getsentry/seer), our AI/ML service. Seer generates the vector embedding and checks it against existing embeddings in the database. If a match is found, Sentry merges the new hash with the existing issue. Because most errors are easily recognized by our classic fingerprinting, we incur the higher embedding cost only for de-duplication scenarios that actually need it.

![Image 1: Diagram showing the data flow. 1. Event is sent to Sentry 2. The event, with stack trace, is sent to the Seer service 3. Seer generates the embeddings 4. Seer queries PostgreSQL (with pgvector) embeddings for the nearest neighbor. 5. PostgreSQL responds with any near enough IDs 6. Seer responds to Sentry with the qualifying IDs](https://blog.sentry.io/_vercel/image?url=_astro%2Finline-0.CnjA8E83.png&w=1080&q=100)

## Evaluation

We didn’t take any shortcuts when it came to evaluating the quality of our changes.

In what euphemistically became known as “Escape Rooms” (where you get to leave the room after you finish labeling) we enlisted several engineers to hand label thousands of example issues where AI-powered issue grouping was making different decisions than our old logic.

![Image 2: Example of an “Escape Room” exercise: a Sentry engineer is reviewing situations where the in-development AI-powered issue grouping model returned a different result than the traditional algorithm, to choose the most correct answer.](https://blog.sentry.io/_vercel/image?url=_astro%2Finline-1.DOu88oJ8.png&w=1200&q=100)

Our goal was to make grouping _at least a little bit better_ for everyone without making the experience worse for anyone. With this in mind, we settled on a very conservative threshold to apply to our similarity scoring, one that overwhelmingly corresponded to human evaluators deciding that the two stack traces were indeed semantically identical.

At the same time, we also wanted to make sure that we weren’t “overcorrecting”, and too eagerly group unrelated issues together. Due to the conservative choices in similarity threshold, during our internal testing we observed that our false positive issue grouping rate was virtually zero, while providing for a substantial reduction in incorrect new issue creation.

We also evaluated several strategies to improve the quality of our algorithm and/or decrease costs. Our first optimization focused on[embedding quantization](https://sbert.net/examples/applications/embedding-quantization/README.html), comparing full float32 precision against float16, int8, and binary quantization of our 768-dimensional vectors. While quantization offered significant storage savings (reducing vector size by up to 32x) and slightly faster distance calculations, it degraded accuracy sufficiently for us to decide to stick with full precision embeddings.

We also explored a few different options for improving the quality of our Approximate Nearest Neighbor (ANN) search and the underlying HNSW index. We experimented with reranking different numbers of candidates (from top-1 to top-100) using exact cosine similarity calculations. We found that in practice, top-100 reranking provided a modest (~1%) improvement in recall with virtually no impact on latency.

![Image 3: One of our validation plots, showing the impact on the ef_search and brute force reranking on Approximate Nearest Neighbor (ANN) recall.](https://blog.sentry.io/_vercel/image?url=_astro%2Finline-2.BnXKeYwq.png&w=828&q=100)

Our pgvector query implementation reveals why increasing our reranking limit to top-100 had such a small performance impact. While we set `k=100` in our candidate retrieval query, we apply two distance thresholds: a more permissive `hnsw_distance` for initial HNSW-based filtering, and a stricter `distance` threshold for final matching. The query first uses the HNSW index to efficiently filter candidates within the permissive threshold, then applies exact cosine distance calculations (ordered by increasing distance) up to our limit of 100 candidates. In practice, the stricter `distance` threshold means we typically process far fewer than 100 candidates during reranking.

```
candidates = (
	session.query(DbGroupingRecord)
	.filter(
		DbGroupingRecord.project_id == project_id,
		DbGroupingRecord.stacktrace_embedding.cosine_distance(embedding)
		<= max(distance, hnsw_distance),
		DbGroupingRecord.hash != hash,
	)
	.order_by(DbGroupingRecord.stacktrace_embedding.cosine_distance(embedding))
	.limit(max(k, hnsw_candidates))
	.execution_options(**custom_options)
	.all()
)
```

## Bringing AI-powered issue grouping to production

### CPU vs GPU Inference

Given that the model is relatively small (161 million parameters), we wanted to evaluate whether CPUs could provide sufficient performance while saving on cost.

Using[locust](https://locust.io/), we tested various configurations with NVIDIA L4 GPUs vs CPU-only instances. For tuning CPU inference, we found this[blog post](https://medium.com/@quocnle/how-we-scaled-bert-to-serve-1-billion-daily-requests-on-cpus-d99be090db26) from roblox to be very helpful.

Ultimately, we found the GPUs comparable in price to CPU inference, while being about 4x faster. Batch processing would further speed things up, but this would have been more difficult to integrate with the rest of our ingestion pipeline.

Our current implementation, which uses gunicorn and Flask, relies on threading to improve concurrency. We found that increasing the number of gunicorn workers improved GPU utilization, but it also causes each worker to load its own copy of the model into GPU memory. This creates memory constraints that prevent us from scaling up. We hope to be able to solve this by transitioning to a framework like TorchServe, or by modifying our setup process to have the workers share the model between them like in [this post](https://www.streppone.it/cosimo/blog/2021/08/deploying-large-deep-learning-models-in-production/).

### Optimizing pgvector

The following are some considerations and tunings we made to operationalize pgvector.

#### HNSW Index

The HNSW index performs best when stored in memory. To rightsize our database, we used the following formula to estimate memory usage per vector:

_Memory per vector = d × 4+M × 2 × 4_

Where:

*   _d_ is the **dimensionality** of the indexed vectors.
*   _M_ is the **number of edges per node** in the constructed graph (we set this constant to 16).

We found this formula to be directionally accurate, though the actual memory footprint in our production environment was higher than expected.

#### Hash Partitioning

We applied[hash partitioning](https://docs.gitlab.com/development/database/partitioning/hash/) based on `project_id` to improve performance. This was an important optimization, since within a table the HNSW index must be shared across _all_ of the partitions. This optimization improved query latency and increased recall.

## Real-world results: 40% fewer issues and alerts

We rolled these changes out slowly over the course of the last several months, first backfilling existing issues for projects, then turning on ingestion.

Overall, we have observed that new issue creation drops by roughly 40% for most platforms and projects. It means that Sentry users should now expect to get 40% less issues (and 40% less alerts) compared to before, allowing fewer distractions and more focus time.

AI-powered issue grouping is enabled by default for all [Sentry](https://sentry.io/welcome/) users, at no additional cost.

We also want to hear from you! Let us know your thoughts on the new issue grouping, including any feedback or suggestion: you can reach us on the [Sentry Discord](https://discord.gg/sentry).
