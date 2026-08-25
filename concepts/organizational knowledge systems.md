# Organizational Knowledge Systems

An organizational knowledge system—often marketed as a “company brain”—gives people, automations, and agents a shared way to find and use evidence scattered across an organization. It is a knowledge-access layer, not necessarily a new source of truth: teams may continue working in chat, code, ticketing, document, and database systems while a separate layer maintains fresh indexes, provenance, permissions, and query interfaces over them.

## Boundaries

| Pattern | Durable Authority | Where Synthesis Happens | Primary Use |
|---|---|---|---|
| [[concepts/LLM-maintained knowledge bases]] | Immutable sources plus maintained synthesis pages | During ingestion and ongoing curation | Accumulating cross-linked understanding |
| Federated organizational retrieval | Source systems remain authoritative; a query-ready index holds derived copies | Distillation at ingestion and synthesis at query time | Finding current evidence across organizational silos |
| [[operations/agent memory]] | A memory store records facts, preferences, experiences, or procedures for later agent use | During or between agent sessions | Continuity and adaptation across runs |
| [[concepts/shared agent memory]] | Several agents read or mutate a governed common store | During work and consolidation | Team coordination and reusable fleet knowledge |

These forms can be combined, but they should not be conflated. A retrieval plane does not resolve contradictions merely because it can find both claims. A maintained wiki may be easier to read but less fresh than source-native search. Agent memory may encode learned procedures that never appeared in an authoritative company system.

## Design Contract

- **Source and freshness:** Record the authoritative source, connector state, update cadence, deletion behavior, and derivation path for every indexed object.
- **Retrieval diversity:** Preserve exact lexical search for identifiers and error strings alongside semantic retrieval; fuse and rerank rather than trusting one scorer.
- **Context restoration:** Return source citations and enough neighboring context to recover preconditions, caveats, and conversational meaning.
- **Identity and authority:** Propagate source permissions into retrieval-time enforcement. Relevance projects, collections, and namespaces are not security boundaries unless the implementation establishes that contract.
- **Human–agent parity:** Prefer narrow evidence primitives that both user interfaces and agent clients can call. Keep retrieval tools cheap and inspectable; let the caller own higher-level planning and synthesis where appropriate.
- **Evaluation:** Measure answer support, retrieval precision and recall, staleness, permission leakage, latency, cost, and downstream task outcomes—not query volume alone.
- **Safety:** Treat chat, documents, tickets, and code comments as untrusted content. Provenance and citations aid review but do not neutralize indirect prompt injection or poisoned organizational knowledge.

[[sources/Cerebras How We Built Our Knowledge Base]] is the current production architecture anchor. It leaves authoring in existing tools, continuously builds a common retrieval index, and exposes the evidence through both a web agent and MCP. Its adoption figures are vendor-reported and its authorization implementation is not public.

## Related

- [[concepts/LLM-maintained knowledge bases]]
- [[concepts/context retrieval]]
- [[concepts/versioned context]]
- [[concepts/shared agent memory]]
- [[operations/agent memory]]
- [[operations/permissions]]
- [[safety/prompt injection]]
- [[maps/Context Management Map]]
