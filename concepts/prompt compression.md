# Prompt Compression

Prompt compression reduces the input prompt before inference, usually by pruning tokens, compressing retrieved passages, or representing long context in compact vectors.

It is useful background for agent context management, but it is not the same as agent compaction. Prompt compression usually operates on a prepared input; agent compaction operates on a growing trajectory of goals, tool calls, observations, decisions, files, failures, and handoffs.

## Related

- [[concepts/context compaction]]
- [[concepts/context engineering]]
- [[concepts/task-aware context pruning]]
- [[operations/cost control]]
- [[maps/Context Management Map]]

## Related Sources

- [[sources/Prompt Compression Survey]]
- [[sources/LLMLingua]]
- [[sources/Selective Context]]
- [[sources/RECOMP]]
- [[sources/AutoCompressors]]
- [[sources/Pretraining Context Compressor]]
