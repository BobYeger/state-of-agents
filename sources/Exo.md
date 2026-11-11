---
title: "Exo: An Architecture for Self-Improving Systems at Runtime"
aliases: ["Exo", "Exo: A Harness Architecture for Runtime Self-Improvement"]
tags: [sources, harnesses, self-improvement]
source_type: "paper"
status: "verified"
evidence_class: "research-system"
publication_date: "2026-10-30"
publication_date_basis: "arxiv_v1_submission_date"
source_version: "arxiv_v1"
arxiv_id: "2611.00463"
authors: ["Alexander Krentsel", "Sylvia Ratnasamy", "Ion Stoica", "Martin Casado", "Ankur Goyal"]
venue: "arXiv"
url: "https://arxiv.org/abs/2611.00463"
discovery_url: "https://academy.dair.ai/papers/collections/self-improving-agents?view=latest"
created: 2026-11-09
updated: 2026-11-09
---

# Exo

## Mechanism

The running agent edits its executor: tools, context, memory policies, and improvement procedures. A separate mechanism preserves history/versioned artifacts and controls replacement. The default guardian checks build success, not task correctness or improvement.

## Evidence

Against the same initial policy without self-editing, AppWorld uses GPT-5.6-Sol, 50 learning scenarios, 100 held-out variants, and three seeds. Total model cost including learning falls 43%, with both arms achieving 96.9% held-out success. CLB's 19-issue sequence has no held-out phase. Open-world headline comparisons have one run per entry; less repetitive quests make specialization more expensive.

## Boundaries

Appendix A makes enforcement conditional: the broadly writable development configuration does not enforce the protection boundary. Rollback does not reverse external effects. These are bounded efficiency results, not proof of generally safe self-improvement.

## Connections

- [[methods/self-improving code loops]]
- [[operations/durable sessions]]
- [[reports/Code Factories Update - 2026-11-09]]

[Primary PDF, Sections 4–5 and Appendix A](https://arxiv.org/pdf/2611.00463v1). HTML truncates before the complete evaluation; the PDF was reviewed.
