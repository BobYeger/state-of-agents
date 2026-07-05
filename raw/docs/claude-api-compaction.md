Title: Compaction

URL Source: https://platform.claude.com/docs/en/build-with-claude/compaction

Markdown Content:
Messages Context management

Server-side context compaction for managing long conversations that approach context window limits.

This feature is eligible for [Zero Data Retention (ZDR)](https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention). When your organization has a ZDR arrangement, data sent through this feature is not stored after the API response is returned.

Server-side compaction is the recommended strategy for managing context in long-running conversations and agentic workflows. It handles context management automatically, without client-side summarization code.

Compaction extends the effective context length for long-running conversations and tasks by automatically summarizing older context when approaching the context window limit. It also keeps the active context small: as a conversation grows, response quality degrades, so compaction replaces older content with a concise summary.

For a deeper look at why long contexts degrade and how compaction helps, see [Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).

This is ideal for:

*   Chat-based, multi-turn conversations where you want users to use one chat for a long period of time
*   Task-oriented prompts that require a lot of follow-up work (often tool use) that might exceed the context window

Compaction is in beta. Include the [beta header](https://platform.claude.com/docs/en/api/beta-headers)`compact-2026-01-12` in your API requests to use this feature.

## Supported models

Compaction is supported on the following models:

*   Claude Fable 5 (claude-fable-5)
*   [Claude Mythos 5](https://anthropic.com/glasswing) (claude-mythos-5)
*   [Claude Mythos Preview](https://anthropic.com/glasswing) (claude-mythos-preview)
*   Claude Opus 4.8 (claude-opus-4-8)
*   Claude Opus 4.7 (claude-opus-4-7)
*   Claude Opus 4.6 (claude-opus-4-6)
*   Claude Sonnet 5 (claude-sonnet-5)
*   Claude Sonnet 4.6 (claude-sonnet-4-6)

## How compaction works

When compaction is enabled, Claude automatically summarizes your conversation when it reaches the configured token threshold. The API:

1.   Detects when input tokens reach your specified trigger threshold.
2.   Generates a summary of the current conversation.
3.   Creates a `compaction` block containing the summary.
4.   Continues the response with the compacted context.

On subsequent requests, append the response to your messages. The API automatically drops all content blocks prior to the `compaction` block, continuing the conversation from the summary.

![Image 1: Compaction flow: when input tokens reach the trigger, Claude writes a summary into a compaction block and continues](https://platform.claude.com/docs/images/compaction-flow.svg)
## Basic usage

Enable compaction by adding the `compact_20260112` strategy to `context_management.edits` in your Messages API request.

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `type` | string | Required | Must be `"compact_20260112"` |
| `trigger` | object | `{"type": "input_tokens", "value": 150000}` | When to trigger compaction. `input_tokens` is the only supported trigger type. `value` must be at least 50,000 tokens. |
| `pause_after_compaction` | boolean | `false` | Whether to pause after generating the compaction summary |
| `instructions` | string | `null` | Custom summarization prompt. Completely replaces the default prompt when provided. |

### Trigger configuration

Configure when compaction triggers using the `trigger` parameter:

### Custom summarization instructions

The default summarization prompt varies by model. Each default instructs Claude to write a summary inside `<summary></summary>` tags with the information needed to continue the task in a future context window. For example, some models use the following prompt:

You can provide custom instructions through the `instructions` parameter. Custom instructions don't supplement the default prompt. They replace it completely:

### Pausing after compaction

Use `pause_after_compaction` to pause the API after generating the compaction summary. This allows you to add additional content blocks (such as preserving recent messages or specific instruction-oriented messages) before the API continues with the response.

When enabled, the API returns a message with the `compaction` stop reason after generating the compaction block:

#### Enforcing a total token budget

When a model works on long tasks with many tool-use iterations, total token consumption can grow significantly. You can combine `pause_after_compaction` with a compaction counter to estimate cumulative usage and gracefully wrap up the task once a budget is reached.

This example appears in the SDK languages only: its value is the budget-tracking logic around the request. The raw request combines the `trigger` from [Trigger configuration](https://platform.claude.com/docs/en/build-with-claude/compaction#trigger-configuration) with `pause_after_compaction` from [Pausing after compaction](https://platform.claude.com/docs/en/build-with-claude/compaction#pausing-after-compaction).

## Working with compaction blocks

When compaction is triggered, the API returns a `compaction` block at the start of the assistant response.

A long-running conversation might result in multiple compactions. The last compaction block reflects the final state of the prompt, replacing content prior to it with the generated summary.

### Passing compaction blocks back

You must pass the `compaction` block back to the API on subsequent requests to continue the conversation with the shortened prompt. The simplest approach is to append the entire response content to your messages:

When the API receives a `compaction` block, all content blocks before it are ignored. You can either:

*   Keep the original messages in your list and let the API handle removing the compacted content
*   Manually drop the compacted messages and only include the compaction block onwards

### Streaming

The compaction block streams differently from text blocks. You receive a `content_block_start` event, followed by a single `content_block_delta` with the complete summary content (no intermediate streaming), and then a `content_block_stop` event.

### Prompt caching

Compaction works well with [prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching). You can add a `cache_control` breakpoint on compaction blocks to cache the summarized content.

#### Maximizing cache hits with system prompts

When compaction occurs, the summary becomes new content that needs to be written to the cache. Without additional cache breakpoints, this would also invalidate any cached system prompt, requiring it to be re-cached along with the compaction summary.

To maximize cache hit rates, add a `cache_control` breakpoint at the end of your system prompt. This keeps the system prompt cached separately from the conversation, so when compaction occurs:

*   The system prompt cache remains valid and is read from cache
*   Only the compaction summary needs to be written as a new cache entry

This keeps long system prompts cached across multiple compaction events throughout a conversation.

## Understanding usage

Compaction requires an additional sampling step, which contributes to rate limits and billing. The API returns detailed usage information in the response:

The `iterations` array shows usage for each sampling iteration. When compaction occurs, you'll see a `compaction` iteration followed by the main `message` iteration. The top-level `input_tokens` and `output_tokens` match the `message` iteration exactly in this example because there is only one non-compaction iteration. The final iteration's token counts reflect the effective context size after compaction.

The top-level `input_tokens` and `output_tokens` do not include compaction iteration usage. They reflect the sum of all non-compaction iterations. To calculate total tokens consumed and billed for a request, sum across all entries in the `usage.iterations` array.

If you previously relied on `usage.input_tokens` and `usage.output_tokens` for cost tracking or auditing, you'll need to update your tracking logic to aggregate across `usage.iterations` when compaction is enabled. With the compaction beta enabled, every response includes `usage.iterations`, even if no compaction occurred. A `compaction` entry appears only when a new compaction is triggered during the request. Re-applying a previous `compaction` block incurs no additional compaction cost, and the top-level usage fields remain accurate in that case.

## Combining with other features

### Server tools

When using server tools (such as web search), the compaction trigger is checked at the start of each sampling iteration. Compaction might occur multiple times within a single request depending on your trigger threshold and the amount of output generated.

### Token counting

The token counting endpoint (`/v1/messages/count_tokens`) applies existing `compaction` blocks in your prompt but does not trigger new compactions. Use it to check your effective token count after previous compactions:

## Examples

Here's a complete example of a long-running conversation with compaction:

Here's an example that uses `pause_after_compaction` to preserve the prior exchange and the current user message (three messages total) verbatim instead of summarizing them:

## Current limitations

*   **Same model for summarization:** The model specified in your request is used for summarization. There is no option to use a different (for example, cheaper) model for the summary.

*   **Compaction might fail when tools are defined:** When your request includes `tools`, the model occasionally calls a tool during the internal summarization step instead of writing a summary. When this occurs, the response contains a `compaction` block with `content: null`. To prevent this, set [`instructions`](https://platform.claude.com/docs/en/build-with-claude/compaction#custom-summarization-instructions) to a prompt that explicitly tells the model not to call tools, for example:

## Next steps

Was this page helpful?
