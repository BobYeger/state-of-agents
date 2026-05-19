# LLM-Maintained Knowledge Bases

An LLM-maintained knowledge base is a persistent markdown corpus where an LLM helps ingest raw sources, maintain cross-linked synthesis pages, surface contradictions, and answer later queries from accumulated structure instead of starting over each time.

The important design move is to shift synthesis from query time to ingest and maintenance time. Raw sources remain immutable evidence, while generated pages accumulate summaries, claims, contradictions, relationships, maps, and reading queues.

For this vault, the rule is:

- `raw/` stores source material.
- `sources/` stores compact evidence cards with dates, citations, summaries, claims, and links to synthesis notes.
- Topic folders store synthesis and should own the durable conceptual connections.
- Project metadata, inventories, crawl reports, and scripts stay outside the graph.

## Related

- [[concepts/context engineering]]
- [[operations/agent memory]]
- [[operations/agent infrastructure]]

Implementation comparison notes are kept outside the public graph until they are promoted into synthesis notes.

## Related Sources

- [[sources/llm-wiki - Karpathy|llm-wiki]]
