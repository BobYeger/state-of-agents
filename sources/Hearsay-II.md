---
title: "The Hearsay-II Speech-Understanding System: Integrating Knowledge to Resolve Uncertainty"
aliases:
  - "Hearsay-II"
source_type: "paper"
kind: "blackboard-architecture"
status: "verified"
year: 1980
publication_date: "1980-06"
publication_date_basis: "journal_issue_month_day_not_specified"
authors:
  - "Lee D. Erman"
  - "Frederick Hayes-Roth"
  - "Victor R. Lesser"
  - "D. Raj Reddy"
venue: "ACM Computing Surveys 12(2), 213–253"
url: "https://mas.cs.umass.edu/Documents/Erman_Hearsay80.pdf"
pdf_url: "https://mas.cs.umass.edu/Documents/Erman_Hearsay80.pdf"
evidence_class: "historical-system-and-experimental-report"
artifacts: []
created: 2026-10-05
updated: 2026-10-05
---

# Hearsay-II

## Contribution

Independent knowledge sources react to changes in a shared blackboard. A control mechanism selects promising eligible work under limited resources. Section 1.2, including its condition/action explanation and footnote on printed page 218, describes replacing repeated polling with event-triggered activation.

## Evidence Boundary

The paper reports an implemented speech-understanding system and comparative experiments. It establishes a historical coordination mechanism, not evidence that modern LLM workers benefit from the same policy or that an event subscription provides crash recovery. No direct influence on a particular 2026 service is asserted.

## Connections

- [[concepts/event-driven agents]]
- [[concepts/shared agent memory]]
- [[sources/Corkill Blackboard Systems]]
- [[sources/LLM Multi-Agent Blackboard System]]
- [[maps/Agent Capability Research Lineage]]
