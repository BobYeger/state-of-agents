# Claim - Context management is an agent architecture choice

Agent context management is not a single technique like summarization. It is a design space across compaction, masking, clearing, retrieval, memory offload, handoff, subagent isolation, and task-aware pruning.

## Evidence

- [[sources/Anthropic Context Engineering Cookbook]] separates compaction, tool-result clearing, and memory as different primitives.
- [[sources/The Complexity Trap]] shows simple observation masking can match or beat LLM summarization in software-engineering agent settings.
- [[sources/ACON]] treats long-horizon agent context compression as an optimization problem over observations and interaction histories.
- [[sources/Parallel Context Compaction]] shows compaction also has serving/runtime consequences: latency, predictable summary volume, and block-level control.
- [[sources/Amp Handoff]] argues for focused new-thread handoff instead of stacking compaction summaries.
- [[sources/SWE-Pruner]] shows coding agents need task-aware pruning because generic compression can break code structure or remove goal-relevant lines.
- [[sources/ContextBench]] evaluates whether coding agents retrieve the right code context, not just whether they solve the final issue.
- [[sources/To Retrieve or To Think]] frames context evolution as deciding whether to retrieve more evidence or reason with the existing context.

## Implications

- Treat compaction choices as harness design, not post-processing.
- Preserve exact details when they are hard to re-fetch.
- Prefer clearing or masking for stale, bulky, re-fetchable tool outputs.
- Prefer handoff when a long thread has become a poor unit of work.

## Related

- [[concepts/context compaction]]
- [[concepts/context engineering]]
- [[concepts/observation masking]]
- [[concepts/tool-result clearing]]
- [[concepts/context retrieval]]
- [[concepts/task-aware context pruning]]
- [[concepts/context evolution]]
- [[concepts/handoff over compaction]]
- [[operations/agent memory]]
- [[maps/Context Management Map]]
