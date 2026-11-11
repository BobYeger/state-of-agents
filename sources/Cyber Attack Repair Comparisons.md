---
title: "Does AI Help Cyber Attackers or Defenders? Evidence from Nonpublic Vulnerabilities and Subsequent Attacks"
aliases: ["Cyber Attack Repair Comparisons"]
source_type: "paper"
status: "verified"
publication_date: "2026-10-05"
publication_date_basis: "arxiv_v1_submission_date"
source_version: "arxiv_v1"
arxiv_id: "2610.06584"
authors: ["Tobias Heldt", "Matt Turk", "Christoph Landolt", "Mario Fritz"]
venue: "arXiv"
url: "https://arxiv.org/abs/2610.06584"
evidence_class: "author-run-attack-repair-experiments"
metrics_status: "author-reported"
created: 2026-11-09
updated: 2026-11-09
tags: [research, cyber, evaluation, verification]
---

# Cyber Attack Repair Comparisons

## Design

Compares autonomous exploitation and repair across five expertise-selected nonpublic environments, alongside 209 disclosed vulnerabilities and cryptographic tasks. Deterministic graders score outcomes; repair must preserve functionality. Models, harnesses, and scoring criteria differ, so score contrasts do not establish a universal attacker advantage or human productivity gain.

## Findings and Limits

Repair leads in two nonpublic environments and attack in three. Additional exploits succeed in 92/524 dependent test intervals after the original exploit stops; intervals include intermediate states. The 115/117 attacker-win statistic also counts broken builds or functionality failures, not solely bypasses of valid patches.

Sequential tests retain sessions and evolving code; attackers see repairs. Results are descriptive, not independent trial estimates. Private tasks restrict reproduction, and absence of public advisories does not prove training-data absence. Structured review's matched improvement comes from one pair; all other pairs tie.

[Primary methods, results, and limitations, Sections IV–VII](https://arxiv.org/html/2610.06584v1).

## Connections

- [[concepts/evaluator reliability]]
- [[operations/agent evals]]
- [[safety/agent safety and security]]
