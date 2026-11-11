---
title: "CyberXero: An AI-Augmented Initial Access Broker Targeting Ukrainian Critical Infrastructure"
source_type: "incident-report"
kind: "adversarial-agent-deployment"
status: "verified"
year: 2026
authors: ["SOCRadar Threat Research Unit"]
publisher: "SOCRadar"
publication_date: "2026-10-06"
publication_date_basis: "primary_article_dateline"
event_window: "Infrastructure observed July 2026; AI augmentation after late July; active at October 6 publication"
evidence_basis: "Recovered exposed working directory, agent definitions/session logs, infrastructure correlations, and victim exports"
url: "https://socradar.io/blog/cyberxero-ai-iab-ukraine-critical-infrastructure/"
created: 2026-11-09
updated: 2026-11-09
tags: [research, security, multi-agent, harness]
---

# SOCRadar CyberXero Agent Campaign

## Coordination and Human Role

SOCRadar finds 51 specialized Claude Code agent definitions and a separate PentAGI integration. Roles divide intrusion stages, with different model budgets. Definitions do not establish 51 concurrent workers.

An operator combines automated web targeting with selective, partly manual Ukrainian activity. Sessions include attempted circumvention and sustained model refusals; they do not establish an unattended campaign. [Primary investigation](https://socradar.io/blog/cyberxero-ai-iab-ukraine-critical-infrastructure/)

## Evidence and Denominators

Recovered notifications describe 4,708 targets scanned, 429 administration panels reached and 32 shells deployed in 61 seconds. These are distinct pipeline counts, not 429 independently verified victims or AI's isolated contribution to throughput.

SOCRadar reports file-confirmed exfiltration from four Ukrainian organizations, exceeding 628,000 records. Seven energy/utility targets lacked confirmed compromise. This is vendor artifact verification, not an independent victim audit.

Russian-speaking, financially motivated attribution rests on account/forum/infrastructure correlations; state sponsorship is not established. A proposed buyer is speculative; no sale was evidenced. [Attribution and victimology](https://socradar.io/blog/cyberxero-ai-iab-ukraine-critical-infrastructure/)

## Connections

- [[sources/NorForge Cairn Intrusions and Harness Takeovers]]
- [[methods/multi-agent orchestration]]
- [[operations/agent infrastructure]]
