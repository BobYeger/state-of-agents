---
title: "From Untrusted Input to Trusted Memory: A Systematic Study of Memory Poisoning Attacks in LLM Agents"
aliases:
  - "Memory Poisoning Attacks in LLM Agents"
source_type: "paper"
kind: "agent-memory-security"
status: "verified"
year: 2026
publication_date: "2026-06-03"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: "2026-06-18"
source_updated_date_basis: "arxiv_v2_revision_date"
arxiv_id: "2606.04329"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Pritam Dash"
  - "Tongyu Ge"
  - "Aditi Jain"
  - "Tanmay Shah"
  - "Zhiwei Shang"
venue: "arXiv"
url: "https://arxiv.org/abs/2606.04329"
pdf_url: "https://arxiv.org/pdf/2606.04329"
artifacts:
  - "raw/papers/From Untrusted Input to Trusted Memory - Memory Poisoning Attacks in LLM Agents.pdf"
created: 2026-07-01
updated: 2026-07-01
---

# From Untrusted Input to Trusted Memory

## Summary

- Systematic study of memory poisoning in LLM agents: persistent memory means one bad write can influence many future turns.
- Identifies memory write channels, structural vulnerabilities, and a taxonomy of memory poisoning attacks.
- Introduces MPBench and reports that more aggressive memory write/retrieval behavior can increase exploitability.
- Important counterweight to memory enthusiasm: memory must be governed, validated, scoped, and forgettable.

## Claims

- [[claims/Claim - Agent memory and skills create compounding improvement loops]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[operations/agent memory]]
- [[safety/prompt injection]]
- [[safety/agent safety and security]]
- [[operations/permissions]]
- [[maps/Safety Map]]
- [[maps/Context Management Map]]

## Artifacts

- [[raw/papers/From Untrusted Input to Trusted Memory - Memory Poisoning Attacks in LLM Agents.pdf]]

## Notes

- Canonical arXiv URL: https://arxiv.org/abs/2606.04329
- arXiv metadata: submitted June 3, 2026; revised June 18, 2026.
- Main vault use: cite whenever durable memory is presented as a control surface. It is also an attack surface.
