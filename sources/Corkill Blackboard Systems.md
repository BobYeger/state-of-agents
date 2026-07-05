---
title: "Blackboard Systems"
aliases:
  - "Corkill 1991"
source_type: "article"
kind: "blackboard-architecture"
status: "verified"
year: 1991
publication_date: "1991-09"
publication_date_basis: "ai_expert_issue_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Daniel D. Corkill"
venue: "AI Expert 6(9):40-47 (unabridged version hosted by UMass MAS lab)"
url: "https://mas.cs.umass.edu/Documents/Corkill/ai-expert.pdf"
pdf_url: "https://mas.cs.umass.edu/Documents/Corkill/ai-expert.pdf"
artifacts:
  - "raw/articles/corkill-blackboard-systems.md"
created: 2026-07-03
updated: 2026-07-05
---

# Corkill Blackboard Systems

## Summary

- Defines the blackboard model as exactly three components: knowledge sources (KSs) as independent black-box modules, the blackboard as a global database holding input data, partial solutions, and control information, and a separate control component making runtime decisions about problem-solving and resource expenditure.
- Distinguishes KSs (static knowledge repositories) from KS activations (a KS plus its specific triggering context) — activations, not KSs, are the active entities competing for execution, which matters when many events trigger the same KS.
- Control cycle: an executing KS activation generates events as it writes to the blackboard; events are queued and ranked until the activation completes; control then triggers and ranks pending KS activations and selects the most appropriate one — an explicit single-writer scheduling loop over a multi-writer store.
- The control component asks triggered KSs for cheap estimates ("if executed, I'll produce contributions of this type, with these qualities, at these costs") rather than possessing their expertise — preserving modularity.
- Warns that "a system containing subsystems that communicate using a global database is incorrectly presented as a blackboard system" (e.g., FORTRAN COMMON) — true blackboards require closely interacting KSs plus a separate control mechanism.
- Gives criteria for when to use a blackboard: diverse specialized representations, heterogeneous integration, many developers, uncertain knowledge or limited data, need for dynamic control; documents the fielded Pontecello Burden Adviser (FMC/Cimflex, started 1985) for phosphorus furnace control.

## Claims

- [[claims/Claim - Agent teams need explicit organization]]

## Connections

- [[methods/multi-agent orchestration]]
- [[methods/runtime routing]]
- [[concepts/multi-agent systems]]
- [[sources/LLM Multi-Agent Blackboard System]]

## Artifacts

- [[raw/articles/corkill-blackboard-systems.md]]

## Notes

- Canonical URL: https://mas.cs.umass.edu/Documents/Corkill/ai-expert.pdf
- The canonical, most readable statement of blackboard components and control semantics — the architecture LLM shared-workspace papers now cite; the vault previously had no dedicated blackboard card.
- Pre-LLM source (1991); its single-writer control loop over a shared store is the design ancestor of modern agent task queues and shared-workspace coordination.
