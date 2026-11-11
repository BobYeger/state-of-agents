---
title: "NorForge: Cairn Intrusions and Harness Takeovers"
source_type: "incident-report-series"
kind: "adversarial-agent-deployment"
status: "verified"
year: 2026
authors: ["Snorre Fagerland"]
publisher: "NorForge"
publication_date: "2026-10-19"
publication_date_basis: "primary_article_dateline"
source_updated_date: "2026-10-26"
source_updated_date_basis: "separate_followup_article_dateline"
event_window: "Intrusions observed before October 19; takeover waves October 20 onward; possibly related reconnaissance October 10"
evidence_basis: "Exposed control panels, task logs, selected independently checked compromises; passive observation for takeover follow-up"
url: "https://norforge.com/blog/inside_cairn"
followup_url: "https://norforge.com/blog/automated-subversion-attempted-takeover"
created: 2026-11-09
updated: 2026-11-09
tags: [research, security, multi-agent, harness]
---

# NorForge Cairn Intrusions and Harness Takeovers

## Observed Deployment

The [October 19 investigation](https://norforge.com/blog/inside_cairn) identifies over 20 likely malicious exposed panels. AIA0001 has over 1,100 projects across 14 panels; these are tasks, not independently verified victim totals. NorForge checks selected compromises directly, including a live uploader. Its approximate 10% success estimate mixes different goals and cannot establish a general intrusion rate.

Workers coordinate through shared facts/intents; humans supply goals and can insert hints. NorForge rates AIA0001/0002 malicious with high confidence, AIA0003 with low confidence. Language does not establish nationality; worker names only suggest model/backend identity.

## Attackers Become Targets

The [October 26 follow-up](https://norforge.com/blog/automated-subversion-attempted-takeover) observes injected tasks on at least 17 panels, including apparently legitimate installations. Tasks expose credentials, establish access, and sometimes execute malware. Host escape was not established. The main waves begin October 20; possible October 10 reconnaissance is not conclusively linked.

Synchronization establishes scripting. Attacker-side AI orchestration remains uncertain; pauses suggest human infrastructure preparation. AIA0009/AIA0010 are tentative clusters, not identified operators. Seventeen targeted panels does not mean seventeen successful host takeovers.

## Connection and Limits

The blackboard architecture matches [oritera/Cairn](https://github.com/oritera/Cairn), supporting a connection to [[sources/CAIRN]] by inference; incident versions are unspecified. Publicly exposed deployments are a selected sample. Neither report demonstrates an autonomous campaign without human involvement.

Related: [[methods/multi-agent orchestration]], [[operations/sandboxes]].
