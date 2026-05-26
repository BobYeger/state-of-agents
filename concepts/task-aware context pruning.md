# Task-Aware Context Pruning

Task-aware context pruning selects or removes context according to the current goal rather than applying a generic compression rule.

This matters for code agents because naive token pruning can break syntax, line-level relationships, or implementation details. A good pruning policy preserves the context needed for the specific bug, feature, test, or refactor.

## Related

- [[concepts/context compaction]]
- [[concepts/prompt compression]]
- [[concepts/context retrieval]]
- [[operations/agent harnesses]]
- [[maps/Context Management Map]]

## Related Sources

- [[sources/SWE-Pruner]]
- [[sources/ContextBench]]
- [[sources/Prompt Compression Survey]]
