---
title: "First Malicious MCP in the Wild: The Postmark Backdoor That's Stealing Your Emails"
aliases:
  - "postmark-mcp backdoor"
source_type: "article"
kind: "supply-chain-incident"
status: "verified"
year: 2025
publication_date: "2025-09-25"
publication_date_basis: "vendor_blog_page"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Idan Dardikman"
venue: "Koi Security blog"
url: "https://www.koi.ai/blog/postmark-mcp-npm-malicious-backdoor-email-theft"
pdf_url: ""
created: 2026-07-03
updated: 2026-07-03
---

# First Malicious MCP in the Wild: The Postmark Backdoor

## Summary

- First confirmed malicious MCP server found in the wild: npm package `postmark-mcp`, a clone of Postmark/ActiveCampaign's legitimate repository, uploaded by user "phanpak" on 2025-09-15.
- Versions 1.0.0–1.0.15 were clean; the backdoor landed in v1.0.16 (published 2025-09-17) as a single line (line 231) adding a silent BCC of every outbound email to phan@giftshop[.]club (C2 domain giftshop[.]club).
- Roughly 1,500 downloads/week; Koi estimates ~300 organizations installed it, implying roughly 3,000–15,000 emails/day exfiltrated at peak.
- Demonstrates the trust-then-poison rug-pull pattern applied to package registries: 15 clean releases build trust before a malicious minor version bump; because MCP servers are invoked autonomously and repeatedly by the agent, one line yields continuous exfiltration.
- The developer deleted the package (~2025-09-25) after exposure, but deletion does not remove already-installed instances. Detected by Koi's behavioral risk engine flagging the new BCC behavior.

## Connections

- [[protocols/MCP]]
- [[safety/protocol security]]
- [[safety/agent safety and security]]
- [[sources/Invariant Labs MCP Tool Poisoning]]
- [[sources/MCP Security Best Practices]]

## Notes

- Canonical URL: https://www.koi.ai/blog/postmark-mcp-npm-malicious-backdoor-email-theft
- Victim and volume figures (~300 orgs, 3,000–15,000 emails/day) are Koi Security estimates derived from download counts, not confirmed incident-response numbers.
- Turns the rug-pull class described by Invariant Labs from a demonstrated attack into a documented incident.
