---
title: "Learning and Reasoning about Interruption"
aliases:
  - "Interruption Workbench"
source_type: "paper"
kind: "personalized-interruption-cost-prediction"
status: "verified"
year: 2003
publication_date: null
publication_date_basis: "ICMI 2003; MSR catalog labels October, paper conference imprint November 5–7; exact publication day not established"
event_start_date: "2003-11-05"
event_end_date: "2003-11-07"
source_updated_date: null
source_version: "Microsoft Research-hosted ICMI 2003 paper; inspected October 5, 2026"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "not assessed"
authors:
  - "Eric Horvitz"
  - "Johnson Apacible"
venue: "ICMI 2003 / ACM / Microsoft Research"
url: "https://www.microsoft.com/en-us/research/publication/learning-and-reasoning-about-interruption/"
pdf_url: "https://www.microsoft.com/en-us/research/wp-content/uploads/2003/01/iw.pdf"
evidence_class: "peer-reviewed-personalized-prediction-and-feature-ablation-experiments"
artifacts: []
created: 2026-10-05
updated: 2026-10-05
---

# Learning and Reasoning about Interruption

## Contribution

The Interruption Workbench learns personalized Bayesian models from desktop activity, calendars, audio, and vision. Users annotate interruption costs in recorded activity; models estimate current interruptibility and time until a less disruptive opportunity. Notification decisions can balance these costs against information value.

The main evaluation uses two office users, each supplying five hours. Current-state accuracy reaches 73% and 64%, compared with majority-state baselines of 53% and 37%. Feature ablations test what desktop events and additional sensors contribute.

## Evidence Boundary

Tests randomly split two-second cases 85/15, so they do not establish independent cross-session generalization. Transferring one person's model to the other performs poorly; a pooled model adds a third user. This is evidence for learnable, individual interruption patterns, not demonstrated long-term benefit from proactive notifications. It supplies a historical mechanism for personal assistants; adoption by current products is not established.

## Connections

- [[concepts/persistent personal agents]]
- [[systems/personal assistant agents]]
- [[concepts/event-driven agents]]
- [[sources/Principles of Mixed-Initiative User Interfaces]]
- [[sources/Proactive Agent]]
- [[sources/ProAgentBench]]

## Primary Links

- [Institution publication record](https://www.microsoft.com/en-us/research/publication/learning-and-reasoning-about-interruption/).
- [Full text](https://www.microsoft.com/en-us/research/wp-content/uploads/2003/01/iw.pdf), sections 3–5 and Tables 1–4.
