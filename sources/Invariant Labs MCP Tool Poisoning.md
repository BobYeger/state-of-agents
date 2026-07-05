---
title: "MCP Security Notification: Tool Poisoning Attacks"
aliases:
  - "Tool Poisoning Attacks"
  - "TPA"
source_type: "article"
kind: "tool-poisoning-disclosure"
status: "verified"
year: 2025
publication_date: "2025-04-01"
publication_date_basis: "vendor_blog_page"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Luca Beurer-Kellner"
  - "Marc Fischer"
venue: "Invariant Labs blog"
url: "https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks"
pdf_url: ""
artifacts:
  - "raw/articles/invariant-labs-mcp-tool-poisoning.md"
created: 2026-07-03
updated: 2026-07-05
---

# MCP Security Notification: Tool Poisoning Attacks

## Summary

- Canonical disclosure of MCP Tool Poisoning Attacks (TPA): malicious instructions embedded in a tool's description or parameter descriptions are invisible to the user but read by the model as trusted context.
- Worked example: an innocuous "add" tool whose description contains `<IMPORTANT>` tags instructing the model to read `~/.cursor/mcp.json` and `~/.ssh/id_rsa` and exfiltrate the contents via a hidden `sidenote` parameter, while returning a normal math answer to disguise the action.
- Names three attack sub-classes: (1) rug pulls — a server silently changes its tool descriptions after the client has approved them; (2) shadowing / cross-server — a malicious server injects instructions that alter a co-connected trusted server's behavior (e.g. redirecting a `send_email` tool to an attacker address even when the user names a different recipient); (3) basic parameter-description poisoning.
- An April 7 follow-up demonstrated exfiltrating WhatsApp chat history by having a poisoned trivia-game MCP server hijack a co-connected whatsapp-mcp server.
- Confirmed susceptible clients at disclosure: Anthropic, OpenAI, Zapier, Cursor. Invariant shipped open-source mcp-scan (announced April 11, 2025) to scan installed servers for poisoning, rug pulls, and cross-origin escalation.

## Connections

- [[protocols/MCP]]
- [[safety/prompt injection]]
- [[safety/protocol security]]
- [[safety/agent safety and security]]
- [[sources/MCP Security Best Practices]]
- [[sources/Willison Lethal Trifecta]]

## Artifacts

- [[raw/articles/invariant-labs-mcp-tool-poisoning.md]]

## Notes

- Canonical URL: https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks
- Origin of the named attack classes (tool poisoning, rug pulls, cross-server shadowing) now standard in MCP security discussions; later MCP spec security guidance addresses the same surface.
- Attacks were demonstrated by Invariant, not observed in the wild in this disclosure; see the Postmark MCP backdoor for an in-the-wild instance of the rug-pull pattern.
