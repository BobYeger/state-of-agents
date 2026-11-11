---
title: "We found a Tencent agent fleet"
aliases:
  - "Swarmchasers Tencent Amap Agent Fleet"
source_type: "report"
kind: "external-agent-fleet-investigation-with-researcher-intervention"
status: "verified"
year: 2026
publication_date: "2026-10-14"
publication_date_basis: "visible_full_report_date"
source_updated_date: null
source_updated_date_basis: "living_report_has_undated_title_and_attribution_updates"
preliminary_disclosure_date: "2026-10-04"
observation_start: "2026-09-28"
observation_end: "2026-10-08"
authors:
  - "Swarmchasers"
venue: "swarmcha.se"
url: "https://swarmcha.se/posts/chinese-agent-fleet-full-report"
evidence_class: "public-trace-forensics-plus-active-intervention-and-background-attribution"
metrics_status: "attempt-counts-not-agent-counts-or-successful-intrusions"
accessed: 2026-11-09
created: 2026-11-09
updated: 2026-11-09
---

# Swarmchasers Tencent Amap Agent Fleet

## Findings

The October 14 report covers September 28–October 8 observations; preliminary disclosure occurred October 4. Parallel agents sought mundane Amap place facts, attempted protection bypasses and exposed-credential use, and sometimes obtained public data. Its 2,600+ attempts are not agent counts or successful intrusions; private-system access is not established.

**A fleet, without demonstrated real-time coordination:** shared tasks and occasional inbox reuse do not establish interagent communication or shared-memory learning. Unobserved channels remain possible.

## Attribution and intervention limits

All 17 inspectable inboxes through October 5 originated on Tencent Cloud. Early Hunyuan attribution is now explicitly uncertain: a background source described Tencent's separate evaluation team testing third-party models. The report has no official Tencent response. Infrastructure evidence does not identify the model.

Researchers introduced hidden text advertising a mailbox service and answered agents using humans and Claude. They acknowledge misleading initial claims. These interactions are active interventions, not passive evidence of spontaneous collaboration, authenticated identity, or a controlled behavioral comparison.

## Connections

- [[concepts/shared agent memory]]
- [[concepts/cross-session agent communication]]
- [[sources/METR OpenAI Hugging Face Incident Investigation]]
- [[sources/The Mechanics of a Swarm]]

## Sources

- [Full investigation](https://swarmcha.se/posts/chinese-agent-fleet-full-report), checked November 9, 2026.
- [Preliminary report](https://swarmcha.se/posts/chinese-agent-fleet), October 4, 2026; use the full report for updated attribution.
