# Tool-Result Clearing

Tool-result clearing removes or abbreviates old tool outputs while preserving the fact that the tool call happened.

This is useful when tool outputs are large, stale, or re-fetchable. It differs from summarization because the harness is not trying to preserve every semantic detail; it is deciding that the exact result should not remain in the active context window.

## Related

- [[concepts/context compaction]]
- [[concepts/observation masking]]
- [[concepts/programmatic tool calling]]
- [[concepts/tool-use contracts]]
- [[operations/agent harnesses]]
- [[maps/Context Management Map]]

## Related Sources

- [[sources/Anthropic Context Engineering Cookbook]]
- [[sources/Anthropic Effective Context Engineering]]
- [[sources/Microsoft Agent Framework Harness Compaction]]
