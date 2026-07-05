Title: Better, faster, less wrong: Enhancing issue grouping

URL Source: https://blog.sentry.io/enhancing-issue-grouping/

Published Time: 2026-06-12T09:00

Markdown Content:
Sentry’s job is to tell you when your app breaks. To do that, we group individual errors into issues. First by [fingerprinting](https://docs.sentry.io/concepts/data-management/event-grouping/), which lexically matches errors based on their structure, then by an AI fallback: when fingerprinting can’t find a match, an ML model compares the new error’s stacktrace against existing issues and merges it if they’re semantically similar. We recently upgraded the model, preventing 20% more duplicate issues from being created while halving the rate of incorrect merges.

AI-powered issue grouping is enabled by default and live for all Sentry customers.

## What makes grouping hard

We talked about v1 of AI grouping in [Using a transformer-based text embeddings model to reduce Sentry alerts by 40% and cut through noise](https://blog.sentry.io/how-sentry-decreased-issue-noise-with-ai/).

A good grouping algorithm minimizes both **undergrouping** and **overgrouping**. Minimizing undergrouping means Sentry isn’t spamming your feed with new issues for the same underlying problem. Minimizing overgrouping means Sentry always tells you about new categories of errors your app is experiencing. Striking the right balance between these can be tricky and subjective.

Overgrouping is arguably the more sinister failure mode. When Sentry incorrectly merges an error into an issue, we’re hiding a problem that should be addressed by a different work stream; this error may have a different priority, root cause, and fix.

To demonstrate how easy it is to mess this up, here’s a real example of 2 nearly identical stacktraces from the Sentry repo that have distinct root causes:

```
# Stacktrace A
ReadTimeoutError / TimeoutError
  autofix.py::generate_summary_and_run_automation
  issue_summary.py::get_issue_summary → _generate_summary
  → run_automation → get_autofix_state        # <-- diverges here
    utils.py::make_get_autofix_state_request
    signed_seer_api.py::make_signed_seer_api_request → urlopen

# Stacktrace B
ReadTimeoutError / TimeoutError
  autofix.py::generate_summary_and_run_automation
  issue_summary.py::get_issue_summary → _generate_summary
  → run_automation → get_and_update_group_fixability_score  # <-- diverges here
    issue_summary.py::_generate_fixability_score
    signed_seer_api.py::make_signed_seer_api_request → urlopen
```

Both errors are timeouts from the [Seer Autofix feature](https://sentry.io/product/seer/autofix/) and share the same request path. The needle in the haystack is in two stacktrace frames. The first timeout is from the `get_autofix_state` flow: a DB query that’ll run on a standard web server. The second timeout is from the `_generate_fixability_score` flow: an ML model call that’ll run on a GPU server through a separate connection pool with a 2x higher timeout threshold. Improving client-side and server-side handling of these requests entails independent work. Yet the v1 model merges these errors into a single issue. The v2 model separates them.

Grouping stacktraces is a nuanced task, not the kind that embeddings APIs are trained to handle. The heavyweight gemini-embeddings-2 model, for example, [flops on our task](https://github.com/getsentry/grouping-trainer/tree/main/eval/comparisons/test_full3/gemini-embedding-2_dim3072_vs_large-no-prefix_dim64). While [Jina AI’s code embeddings model](https://huggingface.co/jinaai/jina-embeddings-v2-base-code) was accurate and efficient for v1 of AI grouping, we knew we could do better than anything off the shelf. We’re sitting on a trove of production stacktraces, plus two years of v1 failure modes the team has internalized as tribal knowledge. LLMs let us apply that knowledge at scale through a labeling algorithm we ran on hundreds of thousands of stacktraces. The v2 model is trained on those labels and has been powering AI grouping since April.

## Here’s how v2 is doing in production

### We’re making fewer issues

AI grouping is preventing 70% of all new issues from being created, up from 50% before we started rolling out v2 on April 22. Among 3,800 large Sentry projects (projects ingesting at least 100 new issues/day with stable error volume before and after v2), 18% saw their rate of AI-prevented issues double since v2.

### Overgrouping has been cut in half

v1’s overgrouping rate, or its rate of incorrect merges, is 8%. While this number doesn’t sound terrible in the aggregate, the kicker is that the v1 model has a tendency to overgroup errors from certain platforms. Platform biases can significantly harm the Sentry experience at the project level. In a small but focused exploration, we found projects whose v1 overgrouping rates ranged from 30% to 60%. It’s not uncommon to find issues in these projects that are bloated with errors representing many distinct root causes.

v2’s overgrouping rate is 4%, and is low across all platforms. All projects in the cohort above now overgroup 2-15% of the time while maintaining or improving on v1 merge rates.

![Image 1: v2 achieves higher merge rates with lower overgrouping than v1 across Ruby, Native, Java, and Cocoa platforms](https://blog.sentry.io/_vercel/image?url=_astro%2Fv1-v2-overgrouping-by-platform.De83eOsB.png&w=1080&q=100)

_v2 improves across every platform where v1 significantly overgrouped. Merge rate is the fraction of new errors which are merged into an existing issue. The overgrouping rate is the fraction of these merges which are incorrect; the error is in an issue that it doesn’t truly belong to._

## How we trained v2

Sampling and labeling data were, by far, the most critical parts of our training pipeline. We sampled stacktraces from hundreds of consenting Sentry projects, selecting for a wide variety in project merge rates and stacktrace lengths, and partially stratified by platform to counter Sentry’s majority JavaScript makeup. We also increased sample weights for stacktrace pairs that were closer to the v1 model’s decision boundary, based on the hypothesis that these pairs are the ones where a successor stands to gain the most.

We labeled the data by prompting Claude Sonnet 4.5 with a thinking budget of 1,024 tokens. The prompt was carefully iterated to follow Sentry’s guidelines around issue grouping, including weighing the error’s underlying cause over surface-level semantics. We measured the prompt’s accuracy against expert-labeled stacktrace pairs from internal Sentry projects. The expert labelers were Sentry’s grouping czars: employees who have mulled over stacktrace similarity for years. We err on the side of avoiding overgrouping in our own labels and instructed Claude to do the same.

We then trained [lightonai/modernbert-embed-large](https://huggingface.co/lightonai/modernbert-embed-large) on these labeled stacktrace pairs. The training data contains hundreds of thousands of pairs of stacktraces ranging from 10 to 8192 tokens. Most training runs tested genuine improvement ideas. Some runs were for the love of the game. A couple of unique training choices are that we use a loss function from 2005, group the dataloader’s scan order to deduplicate forwards passes, and we do something funny with DDP after losing an afternoon failing to install `flash-attn` for `varlen`. Our findings, including interesting experiments that did _not_ yield improvements, are [documented in the grouping-trainer repo](https://github.com/getsentry/grouping-trainer/blob/main/notes.md).

Since we were running experiments in parallel to eke out accuracy, we built some [baby training infra](https://github.com/getsentry/grouping-trainer/blob/main/src/grouping_trainer/launch.py) to reduce headaches induced by GPU stockouts. We’ve gotten up to 20 L4, A100, and H100 GPUs going at the same time (a modest fleet for a team of our size), and all running within 30 minutes of being triggered.

Our training, offline eval, and baby infra code is available at [getsentry/grouping-trainer](https://github.com/getsentry/grouping-trainer).

On the evaluation side, we now measure overgrouping in production. Overgrouping has been a silent but deadly failure mode in the past. Uncovering it used to require manually scrutinizing merged issues in the UI based on customer reports. Today, we have a pipeline that can batch-label 1000s of merged issues from a SQL query.

## Modernizing v2 inference

We also upgraded the v2 model’s inference to reduce its overhead on Sentry’s ultra-hot error ingestion path. AI grouping v2 is 6x faster than v1, uses less GPU memory, and saves hundreds of GBs of DB space.

The most impactful modernization is embedding truncation. Because the v2 model is trained via [Matryoshka Representation Learning](https://arxiv.org/abs/2205.13147), truncating v2 embeddings from 768 dimensions to 64 sacrificed just 2% in accuracy while reducing p50 HNSW lookup times by 4x, p50 insertion times by 20x, and pgvector DB storage by 12x.

![Image 2: v2 HNSW lookups at 12ms p50 vs v1 at 52ms, and v2 inserts at 13ms p50 vs v1 at 270ms](https://blog.sentry.io/_vercel/image?url=_astro%2Fv1-v2-pgvector-query-insert-latency.0C7V96gJ.png&w=2048&q=100)

We also run the model in `bfloat16` and enabled PyTorch’s SDPA to get an easy inference speedup and eliminate CUDA OOMs in production. These changes are a one-liner thanks to [Hugging Face](https://huggingface.co/):

```
model = SentenceTransformer(
     "lightonai/modernbert-embed-large",
+    model_kwargs={"dtype": torch.bfloat16, "attn_implementation": "sdpa"}
 )
```

Finally, we compiled the model to fit our latency-sensitive + plain PyTorch server setup, reducing p50 model inference latency by almost 3x compared to no compilation. In case you have a similar setup and a long-tailed token distribution, we benchmarked this CUDA graph compilation strategy and made it [available on GitHub](https://github.com/kddubey/sentence-transformers/tree/kddubey/examples/compilation/examples/sentence_transformer/applications/compilation).

![Image 3: p50 model inference latency dropping from 45ms to 16ms after CUDA graph compilation](https://blog.sentry.io/_vercel/image?url=_astro%2Fmodel-compilation-latency-drop.694iT7wP.png&w=3840&q=100)

All of these changes were stress-tested offline by running them through a load test that closely mimics production: start with a pgvector DB backfilled with real projects’ stacktraces, and concurrently send the app real, new stacktraces from those projects.

## How we’ve enabled seamless model upgrades

Upgrading ML models for stateless inference is conceptually simple: load in the new model and serve it. AI grouping is far from stateless: it inserts embeddings at a rate proportional to issue creation, and stores this data for up to 90 days. Naively replacing the v1 model with the v2 one would cause a massive surge in new issues, as v2 has nothing in the database to match against. This meant we needed to ship the new model and backfill its embeddings without hurting the customer experience.

We considered a full backfill (like v1, which took months), waiting 90 days to accumulate v2 embeddings before switching, or going live with v2 immediately and falling back to v1 whenever v2 doesn’t have enough data. We went with option 3: customers get v2’s benefits from day one, and v2 can only improve on v1’s decisions, never undo them.

The mechanism hinges on two parameters we added to Seer’s grouping API: `model` and `training_mode`. When a project is opted into v2 via a feature flag, Sentry sends stacktraces to Seer with `model=v2`. Seer searches the v2 embedding space first; if it comes up empty, it falls back to v1.

There’s a subtlety, though: Seer uses **threshold-gated indexing**, which means embeddings are only stored when no sufficiently close match already exists in the index. This keeps the HNSW graph compact and improves search efficiency: since we only need any match within the threshold rather than the true nearest neighbor, a sparser graph with bounded edges (m=16) is all we need. The consequence, however, is that v2’s corpus would only grow from genuinely new events, leaving existing groups without v2 representations.

That’s where `training_mode` comes in. For group hashes that were previously only sent under v1, Sentry fires a request with `training_mode=true`. Seer stores the v2 embedding but returns no grouping result, which bypasses near-duplicate suppression to deliberately backfill the index. This populates v2’s database in real time, piggybacking on live traffic instead of running a separate job.

We rolled out project by project, starting internally. The entire migration took about 6 weeks with zero customer-reported regressions. And the infrastructure is reusable. If we train a v3 tomorrow, the upgrade path is the same: add a column, flip a flag, and let the fallback chain handle the transition.

## What’s next?

Labeling more data and finetuning a much bigger model will help. A more interesting line of research is to improve the model’s input. Today, the model only looks at the error’s stacktrace. A smarter model should be able to use signals attached to the error on ingestion, e.g., the transaction and variable values. Going a step further, what if Sentry accumulated knowledge about your app and attached relevant context dynamically: what’s the higher-level purpose of a transaction, how do downstream users experience an error? We’re currently exploring this context accumulation problem through [Seer](https://docs.sentry.io/product/ai-in-sentry/seer/).

In the meantime, v2 will be chugging along, routing your stacktraces to the right issue.
