---
title: "Decentralized Multi-Agent Coordination and Communication in Shared Codebases"
aliases: ["ParallACT"]
tags: [sources, multi-agent, code-factories]
source_type: "paper"
status: "verified"
evidence_class: "research-benchmark"
publication_date: "2026-10-30"
publication_date_basis: "arxiv_v1_submission_date"
source_version: "arxiv_v1"
arxiv_id: "2611.00314"
authors: ["Rishabh Mediratta", "Lingyun Xiao", "Peter Stone", "Joydeep Biswas", "Elias Stengel-Eskin"]
venue: "arXiv"
url: "https://arxiv.org/abs/2611.00314"
created: 2026-11-09
updated: 2026-11-09
---

# ParallACT

## Contribution

Two agents receive separate principals' complementary or conflicting requirements. The diagnostic dataset contains 155 instances. Claude Code/Opus 4.8 runs on an 85-instance subset; six open-weight model/harness combinations run on all instances.

## Evidence

On contradictory tasks, Opus joint success falls from 62% for one agent seeing both requirements to 16% for unaware parallel agents. Sequential handoff reaches 54%; messaging reaches 20%. Reported success accepts the best result from specified merge policies, not one deployed merge algorithm.

## Boundaries

Tasks deliberately require coordination; rates do not estimate production frequency. Two-agent evidence does not establish larger-team behavior. The oracle has both requirements, so its advantage includes information access. Token cost uses a weighted proxy normalized within configuration, not cross-provider dollars.

## Connections

- [[concepts/code factories]]
- [[concepts/cross-session agent communication]]
- [[sources/Passes Alone Fails Together]]

## Primary Link

[Full text v1, Sections 3–4 and limitations](https://arxiv.org/html/2611.00314v1).
