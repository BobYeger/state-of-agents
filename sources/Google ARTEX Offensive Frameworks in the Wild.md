---
title: "ARTEX and Friends: Enter Agentic Offensive Frameworks"
source_type: "incident-response-report"
kind: "adversarial-agent-deployment"
status: "verified"
year: 2026
authors: ["Aurora Blum", "David Mainor", "Rohit Nambiar", "Omar ElAhdan", "Matthew McWhirt", "Will Silverstone", "Bhavesh Dhake", "Chris Busse"]
publisher: "Google Threat Intelligence Group and Mandiant"
publication_date: "2026-10-30"
publication_date_basis: "primary_article_dateline"
event_window: "Observed incident-response use since late August 2026"
evidence_basis: "Mandiant incident-response investigations, operational artifacts and GTIG research telemetry"
url: "https://cloud.google.com/blog/topics/threat-intelligence/artex-and-friends-enter-agentic-offensive-frameworks"
created: 2026-11-09
updated: 2026-11-09
tags: [research, security, multi-agent, harness]
---

# Google ARTEX Offensive Frameworks in the Wild

## Observed Deployment

GTIG/Mandiant observe substantial intrusion stages since late August. ARTEX organizes six specialized subagents; operators sometimes supply compromised credentials before delegation. Investigators observe error recovery, lateral movement, and data-collection preparation by criminal and suspected espionage actors. [Primary report](https://cloud.google.com/blog/topics/threat-intelligence/artex-and-friends-enter-agentic-offensive-frameworks)

## Measurement and Autonomy Limits

One sequence contains 27 events within 23 seconds of active burst time. Operations include long pauses: burst speed is not total compromise time. Another sequence produces 240 log events; investigators suggest subagents overwriting each other's work may explain errors. This is an inference.

Most PentAGI observations remain reconnaissance/scanning; some progress to intrusion and persistence. No complete victim denominator or aggregate success rate is supplied. Attribution remains vendor assessment.

The report forecasts attacks with little or no human interaction. Current evidence supports delegated phases with variable intervention; forecasts are not incident measurements. [Observations and evolution sections](https://cloud.google.com/blog/topics/threat-intelligence/artex-and-friends-enter-agentic-offensive-frameworks)

## Connections

- [[sources/SOCRadar CyberXero Agent Campaign]]
- [[sources/NorForge Cairn Intrusions and Harness Takeovers]]
- [[methods/multi-agent orchestration]]
