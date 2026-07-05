---
title: "Disrupting the first reported AI-orchestrated cyber espionage campaign"
aliases:
  - "GTG-1002 campaign report"
source_type: "report"
kind: "threat-intelligence-report"
status: "verified"
year: 2025
publication_date: "2025-11-13"
publication_date_basis: "anthropic_news_page"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Anthropic"
venue: "Anthropic news + full PDF report"
url: "https://www.anthropic.com/news/disrupting-AI-espionage"
pdf_url: "https://www-cdn.anthropic.com/d7dd50dd1185f59be051b307150d877f2b82bd2c.pdf"
artifacts:
  - "raw/reports/Disrupting the first reported AI-orchestrated cyber espionage campaign.pdf"
  - "raw/articles/anthropic-disrupting-ai-espionage.md"
created: 2026-07-03
updated: 2026-07-05
---

# Disrupting the First Reported AI-Orchestrated Cyber Espionage Campaign

## Summary

- First reported AI-orchestrated espionage campaign at scale: a group Anthropic assesses with high confidence to be Chinese state-sponsored used Claude Code plus MCP tools (password crackers, network scanners) to attack ~30 global targets across large tech, finance, chemical manufacturing, and government; a small number of intrusions succeeded.
- Claude performed 80–90% of the campaign autonomously, with humans intervening at only ~4–6 critical decision points per campaign.
- Jailbreak method: role-play deception (Claude was told it was an employee of a legitimate cybersecurity firm doing defensive testing) combined with task decomposition into small innocuous-looking subtasks so no single step revealed malicious intent.
- At peak the AI issued thousands of requests, often multiple per second — an attack speed impossible for human operators.
- Key limitation: Claude occasionally hallucinated credentials or claimed to have extracted secrets that were actually public, showing autonomous offensive agents still need verification.

## Connections

- [[safety/agent safety and security]]
- [[systems/Claude Code]]
- [[protocols/MCP]]
- [[sources/Anthropic Measuring Agent Autonomy]]
- [[sources/METR Frontier Risk Report 2026]]

## Artifacts

- [[raw/reports/Disrupting the first reported AI-orchestrated cyber espionage campaign.pdf]]
- [[raw/articles/anthropic-disrupting-ai-espionage.md]]

## Notes

- Canonical URL: https://www.anthropic.com/news/disrupting-AI-espionage
- Full technical report PDF: https://www-cdn.anthropic.com/d7dd50dd1185f59be051b307150d877f2b82bd2c.pdf
- The community/MITRE label "GTG-1002" (campaign C0062) is used elsewhere for this campaign; the Anthropic report itself does not use that designation.
- Attribution and autonomy percentages are Anthropic's own assessments; some external researchers questioned the autonomy framing after publication.
