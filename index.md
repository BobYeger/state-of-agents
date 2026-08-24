# State of AI Agents Knowledge Base

This vault tracks frontier AI agent research and practice, with emphasis on multi-agent systems, long-horizon tasks, protocol interoperability, production infrastructure, evaluation, and safety.

## Start Here

- [[maps/Research Map]]
- [[maps/Systems Map]]
- [[maps/Claims Map]]
- [[maps/Harness Tracker]]
- [[maps/Harness Design Playbook]]
- [[maps/Self-Improving Systems Map]]
- [[maps/Code Factory Playbook]]
- [[maps/What Makes Agent Systems Better]]
- [[maps/Frontier Reading Queue]]

## Entry Points by Goal

- **Designing a harness for agent work** — start at [[maps/Harness Design Playbook]] for the decision path (architecture choice, the eighteen harness questions, verification and failure-mode design), and [[maps/Harness Tracker]] for the inventory of shipped harnesses to compare against.
- **Designing multi-agent teams and communication** — start at [[maps/MAS Orchestration and Architecture]] for topology and task-fit choices, [[maps/Agent Teams and Workforces Map]] for concrete team shapes, and [[reports/Multi Agent Report]] for the evidence synthesis, including cross-session channels and shared-state boundaries.
- **Designing memory and context** — start at [[maps/Context Management Map]] for the architecture, [[reports/Agent Memory Report]] for the full evidence synthesis, and [[reports/Agent Memory Technical Brief]] for the implementation-oriented schema and evaluation guidance.
- **Building systems that improve themselves** — start at [[maps/Self-Improving Systems Map]] for the synthesis notes and the canonical reading order over the evidence, and [[maps/Code Factory Playbook]] for the organization-level lifecycle with the maturity of evidence marked per stage.

Project metadata and private working artifacts are kept outside the public knowledge graph. This repository contains the public vault, the source notes, and the raw source archive needed to inspect the evidence trail.

## Operating Model

- Source notes are compact evidence cards with dates, citations, summaries, and links to synthesis notes.
- Full source material lives under `raw/` and is excluded from the graph view.
- Maps are navigation pages, not source registries.
- Durable connections should live in concepts, systems, methods, protocols, benchmarks, safety, operations, and claims.
- Promotional or product-only pages are included only when they expose useful architecture, harness, protocol, evaluation, safety, or operational details.

## Core Areas

- [[concepts/agentic systems]]
- [[concepts/multi-agent systems]]
- [[concepts/agent teams]]
- [[concepts/cross-session agent communication]]
- [[concepts/long-horizon agents]]
- [[concepts/tool use]]
- [[concepts/context engineering]]
- [[concepts/context compaction]]
- [[concepts/LLM-maintained knowledge bases]]
- [[protocols/agent protocols]]
- [[benchmarks/agent evaluation]]
- [[safety/agent safety and security]]
- [[operations/agent infrastructure]]
- [[maps/Agent Teams and Workforces Map]]
- [[maps/Context Management Map]]
