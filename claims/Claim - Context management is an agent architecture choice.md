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
- [[sources/OpenAI Responses API Multi-Agent]] gives every root and subagent an independently compacted context, making context isolation and compaction part of the orchestration topology.
- [[sources/Claude Fable 5 Prompting Guide]] shows model-specific context behavior: external Markdown lessons help long runs, while exposing a remaining-token countdown can trigger premature summarization or handoff.
- [[sources/Context Engineering MCP CLAUDE-md Skills Hooks Talk]] distinguishes always-visible metadata, progressively disclosed procedures, deterministic just-in-time feedback, and context-isolated delegation as different loading policies.
- [[sources/Factory How Missions Work]] uses fresh role contexts plus authoritative shared artifacts so no one trajectory must carry the full mission state.
- [[sources/Toward Reliable Context Compression for Long-Horizon Agents]] evaluates individual compaction events through paired closed-loop continuations from the same environment state, showing why behavioral continuity is a stronger target than summary similarity.

## Implications

- Treat compaction choices as harness design, not post-processing.
- Preserve exact details when they are hard to re-fetch.
- Prefer clearing or masking for stale, bulky, re-fetchable tool outputs.
- Prefer handoff when a long thread has become a poor unit of work.
- Treat subagent boundaries and model-visible budget signals as context-policy choices, not neutral UI details.
- Test lossy context transitions at the boundary: compare what equivalent continuations can execute before and after compaction, then retain the resulting failures as regression cases.

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
