---
title: "A Programming Paradigm for Spatiotemporal Composability"
aliases:
  - "Spatiotemporal Composability"
  - "Cordis paper"
source_type: "paper"
kind: "dynamic-composability-formalism"
status: "verified"
year: 2026
publication_date: "2026-08-13"
publication_date_basis: "repository_draft_date"
source_updated_date: "2026-08-13"
source_updated_date_basis: "captured_pdf_creation_and_repository_commit_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Yifan Shi"
  - "Wei Zhang"
  - "Tianyi Cui"
venue: "Actively revised preprint"
url: "https://github.com/cordiverse/paper/tree/948a07b369c62adb3b12e102458be5c18dfb69b9"
pdf_url: "https://github.com/cordiverse/paper/blob/948a07b369c62adb3b12e102458be5c18dfb69b9/paper.pdf"
license: "No license stated"
license_url: null
evidence_class: "unreviewed-formal-preprint-and-observational-case-study"
metrics_status: "single-ecosystem-observational-no-controlled-evaluation"
created: 2026-08-17
updated: 2026-08-17
---

# A Programming Paradigm for Spatiotemporal Composability

## Summary

- The paper separates dynamic composition into **temporal composability**, where removing a component reverses its context-mediated effects, and **spatial composability**, where declared dependencies drive activation and teardown as providers change.
- A revertible effect returns both a new context state and a left inverse. A reactive coeffect is a typed dependency key whose availability changes are classified as activating, deactivating, or neutral.
- The component calculus adds per-instance fibers, committed dependency views, asynchronous transitions, partial rollback, failure states, and dependent-before-provider teardown. Conditional results cover recovery exactness, dependency ordering, progress, and confluence.
- Cordis implements the design with reversible registrations, dependency injection, configuration reconciliation, and hot module replacement. The Koishi case study supplies adoption evidence, not a controlled evaluation.
- Applying the design to a continuously self-modifying agent harness is explicitly future validation rather than a demonstrated result.

## Design Consequences

- Runtime harness modification needs two distinct controls: ownership and reversal of each component's effects, plus dependency-aware reactivation and teardown. A rollback stack alone does not preserve a changing component graph.
- Effects should pass through a component-scoped context, return local disposers, and unwind in LIFO order. Dependencies should be declared and resolved to stable provider identities for the duration of a transition.
- A provider should first stop advertising its capability, then wait for affected dependents to quiesce, and only then run its own teardown. External emissions, failed cleanup, and untrusted code require separate transaction, compensation, and sandbox boundaries.

## Evidence Boundary

This is an 88-page, actively revised preprint with handwritten, unmechanized proofs. The implementation does not verify the formal obligations: correct inverses, confinement, commutativity or independence, acyclic dependencies, finite work, and total provision remain assumptions. The confluence theorem compares quiescent, failure-free runs with the same orchestration steps, and inverse failure is not modeled. The recursive context type also contains a negative occurrence whose semantics are not justified in the manuscript.

The empirical material is limited to a top-100 VS Code extension survey and one observational TypeScript ecosystem. Koishi reportedly has more than 4,000 plugins, but it uses Cordis v3 while the paper formalizes a redesigned Cordis v4. No overhead benchmark, baseline comparison, user study, large-graph stress test, or agent-harness evaluation is reported.

## Connections

- [[sources/DeepSeek Harness Repository]]
- [[operations/agent harnesses]]
- [[operations/harness fault tolerance]]
- [[concepts/agent plugins]]
- [[maps/Harness Design Playbook]]
- [[maps/Self-Improving Systems Map]]

## Notes

- Canonical repository: https://github.com/cordiverse/paper
- Audited snapshot: https://github.com/cordiverse/paper/tree/948a07b369c62adb3b12e102458be5c18dfb69b9
- Draft PDF: https://github.com/cordiverse/paper/blob/948a07b369c62adb3b12e102458be5c18dfb69b9/paper.pdf
- Draft date: August 13, 2026.
- Authors are affiliated with Peking University and DeepSeek-AI.
- The repository contains the README and binary PDF but no manuscript source, proof artifact, study data, or license. Public access therefore does not grant reuse rights.
