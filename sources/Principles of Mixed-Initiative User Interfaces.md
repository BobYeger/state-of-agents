---
title: "Principles of Mixed-Initiative User Interfaces"
aliases:
  - "LookOut"
source_type: "paper"
kind: "mixed-initiative-personal-assistance"
status: "verified"
year: 1999
publication_date: null
publication_month: "1999-05"
publication_date_basis: "author_publication_page_confirms_month; exact publication day not established"
source_updated_date: null
source_version: "Author-hosted CHI 1999 paper; inspected October 5, 2026"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "not assessed"
authors:
  - "Eric Horvitz"
venue: "CHI 1999, pages 159–166 / Microsoft Research"
url: "https://erichorvitz.com/uiact.htm"
pdf_url: "https://erichorvitz.com/chi99horvitz.pdf"
evidence_class: "peer-reviewed-design-principles-and-working-prototype"
artifacts: []
created: 2026-10-05
updated: 2026-10-05
---

# Principles of Mixed-Initiative User Interfaces

## Contribution

Horvitz makes assistance a decision under uncertainty: compare the expected value of acting, asking, and doing nothing, including interruption and mistaken-action costs. Direct manipulation remains available; users can invoke, refine, or dismiss assistance. Defaults and user-adjustable thresholds govern initiative.

LookOut demonstrates this coupling in email and calendar work: infer scheduling intent, prepare an appointment, and leave room for correction. Timing models use message length and observed delay before users request scheduling, showing that recognizing a need and choosing when to intervene are separate problems.

## Evidence Boundary

The paper combines design principles, an implemented prototype, and timing observations from several users. It does not establish long-term productivity gains or reliable general-purpose autonomy through a large controlled deployment. Its durable contribution is the architecture of adjustable initiative and uncertainty-aware interaction. This is a historical research precedent, without documented adoption by the contemporary products linked below.

## Connections

- [[concepts/persistent personal agents]]
- [[systems/personal assistant agents]]
- [[concepts/human-in-the-loop agents]]
- [[sources/Learning and Reasoning about Interruption]]

## Primary Links

- [Author publication record](https://erichorvitz.com/uiact.htm).
- [Full text](https://erichorvitz.com/chi99horvitz.pdf), principles, LookOut, decision theory, and service timing sections.
