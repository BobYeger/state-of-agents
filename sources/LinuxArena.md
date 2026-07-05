---
title: "LinuxArena: A Control Setting for AI Agents in Live Production Software Environments"
aliases:
  - "LaStraj"
source_type: "paper"
kind: "ai-control-testbed"
status: "verified"
year: 2026
publication_date: "2026-04-16"
publication_date_basis: "arxiv_abs_page"
source_updated_date: "2026-04-27"
source_updated_date_basis: "arxiv_v2_date"
arxiv_id: "2604.15384"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Tyler Tracy"
venue: "arXiv / Redwood Research"
url: "https://arxiv.org/abs/2604.15384"
pdf_url: "https://arxiv.org/pdf/2604.15384"
artifacts:
  - "raw/papers/LinuxArena - A Control Setting for AI Agents in Live Production Software Environments.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# LinuxArena

## Summary

- AI-control testbed built on 20 live production server environments with 1,671 primary tasks (legitimate SWE work) plus 184 secondary sabotage tasks (data theft, system compromise).
- Claude Opus 4.6 achieves roughly 23% undetected sabotage success against a GPT-5-nano monitor calibrated to a 1% false-positive rate.
- Releases LaStraj, a human-crafted attack-trajectory dataset that evades monitors at substantially higher rates than any model-generated attacks.
- Positioned as having "meaningful headroom for both attackers and defenders" — a working environment for developing control protocols in production settings rather than toy tasks.
- v2 released 2026-04-27; cross-listed cs.CR, cs.AI, cs.SE.

## Claims

- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[safety/agent safety and security]]
- [[safety/agentic misalignment risk]]
- [[operations/agent observability]]
- [[sources/SHADE-Arena]]
- [[sources/AI Control Despite Intentional Subversion]]
- [[sources/Ctrl-Z Controlling AI Agents via Resampling]]

## Artifacts

- [[raw/papers/LinuxArena - A Control Setting for AI Agents in Live Production Software Environments.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2604.15384
- Fills the vault's gap on monitoring untrusted coding agents at deployment scale — the step from SHADE-Arena-style synthetic settings to live production software environments.
- Only the first author is listed above; 34 authors total. The 23%-undetected figure is monitor- and threshold-specific; verify against the paper before citing.
