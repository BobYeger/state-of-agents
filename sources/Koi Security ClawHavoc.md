---
title: "ClawHavoc: 341 Malicious ClawHub Skills Found by the Bot They Were Targeting"
aliases:
  - "ClawHavoc"
source_type: "article"
kind: "supply-chain-incident"
status: "verified"
year: 2026
publication_date: "2026-02-01"
publication_date_basis: "vendor_blog_page"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Oren Yomtov"
venue: "Koi Security blog"
url: "https://www.koi.ai/blog/clawhavoc-341-malicious-clawedbot-skills-found-by-the-bot-they-were-targeting"
pdf_url: ""
created: 2026-07-03
updated: 2026-07-05
---

# ClawHavoc: 341 Malicious ClawHub Skills

## Summary

- Audit of ClawHub, OpenClaw's official skill marketplace: 341 of 2,857 skills malicious (11.9%) on 2026-02-01; a 2026-02-16 rescan found 824 malicious of 10,700+ (7.7%), and Antiy Labs later catalogued 1,184 malicious skills historically.
- 335 of the 341 belong to one coordinated campaign ("ClawHavoc") delivering Atomic macOS Stealer (AMOS) — a 521KB universal Mach-O binary that steals keychain credentials, browser data (Chrome/Safari/Firefox/Brave/Edge/Vivaldi/Opera), 60+ crypto wallets, Telegram sessions, and SSH keys.
- Novel delivery technique, "ClickFix 2.0": fake "Prerequisites" sections inside SKILL.md instruct the user to download a password-protected "openclaw-agent" archive (password: openclaw) and run it; the password protection evades AV scanning and the AI agent itself surfaces the fake setup step to the user.
- Targeted high-value categories: crypto tools (111 skills), YouTube utilities (57), finance/social (51), Polymarket bots (34), auto-updaters (28), Google Workspace (17), ETH gas trackers (15).
- Six outliers used other techniques: an embedded reverse shell (better-polymarket), fake auth executables (bybit-agent), and direct credential exfiltration to webhook.site (rankaj). Published IOCs include IPs 91.92.242.30, 202.161.50.59, and 54.91.154.110.

## Connections

- [[concepts/agent skills]]
- [[safety/agent safety and security]]
- [[sources/OpenClaw Repository]]
- [[sources/Agentic Skills in the Wild]]
- [[sources/Koi Security Postmark MCP Backdoor]]

## Notes

- Canonical URL: https://www.koi.ai/blog/clawhavoc-341-malicious-clawedbot-skills-found-by-the-bot-they-were-targeting
- No raw/ capture: the article embeds malicious-skill payloads/IOCs, and local security scanning quarantines any on-disk copy (verified 2026-07-05). Intentionally left link-only; do not retry the capture.
- Malicious-skill counts moved quickly (341 → 824 → 1,184 across three snapshots by different parties); treat any single percentage as a point-in-time measurement.
- Strongest quantified evidence to date that agent-skill marketplaces are an active supply-chain attack surface, extending the MCP-server attack pattern to skill ecosystems.
