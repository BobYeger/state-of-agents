# LLM-Maintained Knowledge Bases

An LLM-maintained knowledge base is a persistent markdown corpus where an LLM helps ingest raw sources, maintain cross-linked synthesis pages, surface contradictions, and answer later queries from accumulated structure instead of starting over each time.

The important design move is to shift synthesis from query time to ingest and maintenance time. Raw sources remain immutable evidence, while generated pages accumulate summaries, claims, contradictions, relationships, maps, and reading queues.

For this vault, the rule is:

- `raw/` stores source material.
- `sources/` stores compact evidence cards with dates, citations, summaries, claims, and links to synthesis notes.
- Topic folders store synthesis and should own the durable conceptual connections.
- Project metadata, inventories, crawl reports, and scripts stay outside the graph.

## Maintained Wiki vs Organizational Retrieval

An LLM-maintained wiki is one form of organizational knowledge infrastructure, but not the only one. It creates durable synthesis pages whose summaries, claims, contradictions, and links can be inspected and improved over time. [[concepts/organizational knowledge systems|Federated organizational retrieval]] instead leaves authoritative work in systems such as chat, code, documents, tickets, and databases, continuously maintains query-ready derived indexes, and synthesizes an answer when a person or agent asks.

[[sources/Cerebras How We Built Our Knowledge Base]] is the production anchor for the second pattern. Its Slack distillation performs some ingest-time synthesis, but the durable product is an evidence index rather than a generated wiki. The distinction is freshness versus maintained connective structure, not a choice between “RAG” and “knowledge”: a mature system can use source-native retrieval to update a durable synthesis layer while preserving citations and authority boundaries.

## Experience Wiki vs Executable Skills

[[sources/WikiSkill]] uses a maintained wiki at a different boundary: as internal optimizer-facing memory between immutable execution traces and validated executable skills. A Wiki Maintainer turns successes, failures, and proposal outcomes into pattern pages and evolution and impact logs; a separate proposer uses that history to create or patch skills. The task-running agent receives the active skills but not the wiki by default. This is a write-maintain-compile pipeline for procedural memory, not a company brain or an organizational retrieval system.

The paper's ablation supports separating optimizer access from task-runtime context, but its no-wiki condition also removes the Wiki Maintainer, and the current wiki has no automated pruning or validation gate.

## Related

- [[concepts/context engineering]]
- [[concepts/organizational knowledge systems]]
- [[operations/agent memory]]
- [[operations/agent infrastructure]]

Implementation comparison notes are kept outside the public graph until they are promoted into synthesis notes.

## Related Sources

- [[sources/llm-wiki - Karpathy|llm-wiki]]
- [[sources/Cerebras How We Built Our Knowledge Base]]
- [[sources/WikiSkill]]
