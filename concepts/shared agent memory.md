# Shared Agent Memory

Shared agent memory is memory written and read by more than one agent or session: a team, fleet, or organization reuses one store instead of each agent keeping private state.

Single-agent memory asks what one agent should remember. Shared memory adds distribution problems: multiple writers, conflicting facts, unclear authority, and the risk that one agent's mistake becomes every agent's belief. The idea is older than LLM agents — blackboard systems coordinated specialist modules through a shared workspace ([[sources/Corkill Blackboard Systems]]: the classic architecture and why it faded), and it is returning as a coordination substrate for agent teams ([[sources/LLM Multi-Agent Blackboard System]]). [[sources/Memory in the Age of AI Agents]] names multi-agent memory an open frontier and traces the shift from isolated per-agent memories with message passing toward centralized shared structures.

## Failure Modes

[[sources/Governed Shared Memory for Multi-Agent LLM Systems]] formalizes the fleet-memory problem and names the first four; the others come from adjacent evidence.

| Failure mode | What happens | Evidence |
|---|---|---|
| Unauthorized leakage | A memory crosses a tenant, team, or fleet boundary it should not. | [[sources/Governed Shared Memory for Multi-Agent LLM Systems]] |
| Stale propagation | Superseded facts keep circulating because nothing marks them invalid. | [[sources/Governed Shared Memory for Multi-Agent LLM Systems]], [[sources/LongMemEval]]: knowledge-update questions are where memory systems drop accuracy |
| Contradiction persistence | Conflicting writes coexist with no resolution rule. | [[sources/Governed Shared Memory for Multi-Agent LLM Systems]] |
| Provenance collapse | Nobody can reconstruct which agent wrote a memory or what it was derived from. | [[sources/Governed Shared Memory for Multi-Agent LLM Systems]] |
| Collective false memory | Agents reinforce each other's misremembering until the group converges on a wrong fact. | [[sources/When Agents Misremember Collectively]]: measures Mandela-effect contagion in MAS |
| Poisoned write | Injected or adversarial content becomes trusted memory for every future reader. | [[sources/Memory Poisoning Attacks in LLM Agents]]; [[sources/Claude Managed Agents Memory Stores]]: vendor docs warn that a read-write shared store turns injection into durable trust |

## Design Decisions

### Write authority

Decide who may write before deciding what to store. The strongest current pattern separates a read-only shared reference store, attached to many sessions, from narrow read-write stores scoped per user, team, or project — [[sources/Claude Managed Agents Memory Stores]] documents this as the recommended layout, with access enforced at the filesystem level rather than by prompt. [[sources/Governed Shared Memory for Multi-Agent LLM Systems]] generalizes it as policy-governed propagation: a memory crosses an agent boundary only when a policy says it may. Prompt-level discipline is not an enforcement mechanism here; the write path itself must check authority.

### Concurrent-write reconciliation

Two mechanisms cover most cases:

- Optimistic concurrency for same-memory races: [[sources/Claude Managed Agents Memory Stores]] uses a content-hash precondition — an update applies only if the stored hash matches what the writer read, otherwise the writer re-reads and retries.
- Temporal supersession for contradicting facts: [[sources/Governed Shared Memory for Multi-Agent LLM Systems]] makes newer writes override older conflicting data while retaining the old version, so "which version is current" has a defined answer.

Bi-temporal substrates strengthen the second mechanism: [[sources/Zep Temporal Knowledge Graph Memory]] records both when a fact became true and when it stopped being true, so supersession is a query rather than a cleanup job. The governance-testing result in the MemClaw evaluation is a caution: ordering conflicts between synchronous duplicate detection and asynchronous contradiction resolution were a real architectural bug found only by testing the reconciliation path.

### Namespacing

Scope is the primary leakage control. Workspace- or fleet-scoped stores with scoped retrieval keep queries from crossing boundaries; the MemClaw evaluation reports high intra-fleet visibility with zero cross-fleet leakage, and also that governance testing surfaced scope-enforcement gaps in sub-tenant credential access — namespacing must be tested adversarially, not assumed from the schema.

### Provenance and audit

Every write should be attributable and every version retained. [[sources/Claude Managed Agents Memory Stores]] creates an immutable version per mutation, attributed to the writing session, with a redaction path that scrubs secrets without destroying the audit trail. [[sources/Governed Shared Memory for Multi-Agent LLM Systems]] reconstructed complete depth-four derivation chains with correct writer identity. Retroactive rewriting schemes trade against this: [[sources/A-MEM]] improves coherence by letting new memories rewrite old ones, but erases the original record — acceptable for a private store, not for a shared one.

### Lesson propagation without mistake propagation

The reason to share memory at all is that one agent's experience should improve the others. The risk is symmetric: shared memory also propagates errors, and the collective-false-memory result shows groups can amplify rather than dampen them. Useful separations:

- Separate insight from trajectory. [[sources/G-Memory]] keeps a hierarchy of high-level insights, per-query records, and agent-specific interaction graphs, propagating generalizable lessons across the team without flattening raw per-agent history into shared truth; it reports up to +20.89% embodied-action and +10.12% knowledge-QA gains across five benchmarks without modifying the MAS frameworks.
- Promote through a consolidation gate, not on write. [[concepts/dreaming and memory consolidation]] gives raw experience a review step before it becomes shared reference material; [[sources/Claude Managed Agents Memory Stores]] implements this as dreaming sessions that consolidate a fragmented store into a new output store rather than editing shared memory in place.
- Mine experience deliberately. [[sources/Experiential Co-Learning]] has software-agent teams extract shortcut-oriented experience from historical trajectories for reuse — propagation as a curation step, not a side effect of logging.

## Evidence Quality

The constructive results are early. G-Memory's gains are on simulated MAS benchmarks with no production deployment. The MemClaw governance evaluation tests the authors' own service with no cross-system comparison. The Managed Agents customer figures (Rakuten, Wisedocs) are vendor-reported. The failure-mode taxonomy and the governance primitives are the durable contribution; the specific numbers are not yet load-bearing.

## Related

- [[operations/agent memory]]
- [[concepts/dreaming and memory consolidation]]
- [[concepts/multi-agent systems]]
- [[concepts/agent teams]]
- [[methods/multi-agent orchestration]]
- [[safety/prompt injection]]
- [[claims/Claim - Agent memory and skills create compounding improvement loops]]
- [[maps/Context Management Map]]
