---
title: "EchoLeak: The First Real-World Zero-Click Prompt Injection Exploit in a Production LLM System (CVE-2025-32711)"
aliases:
  - "EchoLeak"
  - "CVE-2025-32711"
source_type: "paper"
kind: "prompt-injection-incident"
status: "verified"
year: 2025
publication_date: "2025-09-06"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2509.10540"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Pavan Reddy"
  - "Aditya Sanjay Gujral"
venue: "arXiv (AAAI Fall Symposium Series 2025)"
url: "https://arxiv.org/abs/2509.10540"
pdf_url: "https://arxiv.org/pdf/2509.10540"
artifacts:
  - "raw/papers/EchoLeak - The First Real-World Zero-Click Prompt Injection Exploit in a Production LLM System (CVE-2025-32711).pdf"
created: 2026-07-03
updated: 2026-07-05
---

# EchoLeak (CVE-2025-32711)

## Summary

- Analysis of CVE-2025-32711 ("EchoLeak"), disclosed by Aim Labs and patched server-side by Microsoft in June 2025 (CVSS 9.3, critical); no user action required and no known in-the-wild exploitation.
- First real-world zero-click prompt-injection data exfiltration in a production LLM application (Microsoft 365 Copilot): a single crafted email, with no user interaction, causes Copilot to read in-scope org data (chats, OneDrive, SharePoint, Teams) and leak it to an attacker.
- Coins "LLM Scope Violation": untrusted external input manipulates the model into accessing higher-privilege internal data across trust boundaries.
- Exfiltration chain: bypass Microsoft's XPIA (Cross-Prompt Injection Attempt) classifier, evade link redaction with reference-style Markdown, trigger auto-fetched Markdown images, and abuse a Microsoft Teams proxy allowed by the Content Security Policy to reach an attacker server.
- Proposed defenses: prompt partitioning, provenance-based access controls, stricter CSP, and least-privilege / defense-in-depth architecture.

## Connections

- [[safety/prompt injection]]
- [[safety/agent safety and security]]
- [[sources/Willison Lethal Trifecta]]
- [[sources/Design Patterns for Securing LLM Agents]]
- [[sources/CaMeL]]

## Artifacts

- [[raw/papers/EchoLeak - The First Real-World Zero-Click Prompt Injection Exploit in a Production LLM System (CVE-2025-32711).pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2509.10540
- This is a third-party academic analysis; the original disclosure is by Aim Labs / Aim Security (June 2025). The CVE and patch details originate there.
- Instantiates the lethal-trifecta pattern (private data + untrusted content + exfiltration channel) end to end, and shows classifier-based injection defenses (XPIA) failing while egress controls (CSP) were the load-bearing but incomplete layer.
