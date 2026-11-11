---
title: "Red-Teaming OpenAI's Internal Agent Monitoring Systems"
aliases:
  - "METR Redwood Internal Agent Monitoring Red Team"
source_type: "report"
kind: "internal-agent-monitoring-red-team"
status: "verified"
year: 2026
publication_date: "2026-10-22"
publication_date_basis: "visible_article_date"
source_updated_date: "2026-10-29"
source_updated_date_basis: "explicit_update_log"
exercise_start: "2026-07-21"
exercise_end: "2026-08-11"
authors:
  - "David Rein"
  - "Adam Kaufman"
venue: "METR / Redwood Research"
url: "https://metr.org/blog/2026-10-22-red-teaming-openai-agent-monitoring/"
evidence_class: "high-access-human-red-team-with-provider-controlled-public-disclosure"
metrics_status: "historical-coverage-estimates-not-agent-exploitation-or-detection-rates"
accessed: 2026-11-09
created: 2026-11-09
updated: 2026-11-09
---

# METR–Redwood Internal Agent Monitoring Red Team

## Findings

The July 21–August 11 exercise assessed infrastructure as it existed on/before July 21. Estimated monitoring eligibility was 75–94% of qualifying internal Responses API traffic; internal Codex alone reached 99.2%. Eligibility is not completed monitoring or detection, and excludes other inference services.

Missed compaction events potentially omitted roughly 10% of eligible Codex traffic during May–July; OpenAI independently identified and fixed this during the exercise. RL training runs lacked coverage at the exercise's start. Investigators found sandbox and monitoring bypass vulnerabilities; some hypotheses remained unvalidated. These are human red-team findings, not demonstrated autonomous exploitation.

## Correction and limits

**October 29 corrected the remediation claim:** OpenAI says most vulnerabilities are patched, one fix remains underway, and that remaining issue does not affect its misuse safeguards stack. METR has not verified remediation or current coverage.

Only a small public subset of the private report was released; OpenAI controlled redactions, without investigators' unilateral disclosure rights. This exercise is separate from [[sources/METR OpenAI Hugging Face Incident Investigation]].

## Connections

- [[operations/agent observability]]
- [[operations/sandboxes]]
- [[safety/sandbox escape and credential exposure]]

## Source

- [Primary report and October 29 update log](https://metr.org/blog/2026-10-22-red-teaming-openai-agent-monitoring/), checked November 9, 2026.
