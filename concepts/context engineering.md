# Context Engineering

Context engineering is the design of what information enters, leaves, persists outside, or is transformed before entering an agent's context window.

For agents, context engineering is performance engineering. The context window carries task state, tool descriptions, memory, examples, artifacts, and prior observations; bad context makes agents brittle even when the model and agent count are strong.

## Why Bigger Windows Do Not Remove the Discipline

The premise of compaction, retrieval, and memory architecture is that filling a large window is not free. Two lines of evidence establish this:

- Position degrades recall. [[sources/Lost in the Middle]] shows U-shaped positional performance: models use information at the beginning and end of context well and drop roughly 20+ points of multi-document QA accuracy when the same information sits in the middle, even on explicitly long-context models. Measured on 2023-era models, but the successor study confirms the direction.
- Length degrades everything. [[sources/Context Rot]] tested 18 models across four organizations and found all of them degrade as input grows, even on trivial copy tasks; distractors compound with length, and focused ~300-token prompts consistently beat ~113k-token full prompts on LongMemEval across every model family. Chroma sells retrieval, so read the framing with that in mind, but the cross-vendor dataset is the strongest length-degradation evidence available.

The design consequences: relevant information should be selected and placed, not accumulated; token count is a cost the architecture should justify per token; and compaction is not merely a budget workaround but a quality intervention. Practitioner reports converge on the same conclusion from production — [[sources/Manus Context Engineering]] treats KV-cache hit rate as the top production metric, keeps a continuously rewritten plan file to recite goals into recent attention against mid-context drift, and uses restorable compression (drop page content, keep the URL) so truncation never destroys information irreversibly.

## Related

- [[operations/durable sessions]]
- [[concepts/long-horizon agents]]
- [[operations/agent memory]]
- [[concepts/versioned context]]
- [[concepts/context compaction]]
- [[concepts/context retrieval]]
- [[concepts/context evolution]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
- [[claims/Claim - Context management is an agent architecture choice]]
- [[maps/Context Management Map]]
- [[maps/What Makes Agent Systems Better]]

## Related Sources

- [[sources/Cloudflare Agent Memory|Agents that remember: introducing Agent Memory]]
- [[sources/Anthropic Effective Context Engineering|Effective context engineering for AI agents]]
- [[sources/Agentic Context Engineering|Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models]]
- [[sources/LangSmith Context Hub|Introducing LangSmith Context Hub]]
- [[sources/Anthropic Multi-Agent Research System|How we built our multi-agent research system]]
- [[sources/llm-wiki - Karpathy|llm-wiki]]
- [[sources/OpenAI Codex Agent Loop|Unrolling the Codex agent loop]]
- [[sources/Anthropic Context Engineering Cookbook|Context Engineering for AI Agents: Memory vs. Compaction vs. Tool Clearing]]
- [[sources/The Complexity Trap|The Complexity Trap]]
- [[sources/ACON|ACON]]
- [[sources/Lost in the Middle|Lost in the Middle: How Language Models Use Long Contexts]]
- [[sources/Context Rot|Context Rot: How Increasing Input Tokens Impacts LLM Performance]]
- [[sources/Manus Context Engineering|Context Engineering for AI Agents: Lessons from Building Manus]]
