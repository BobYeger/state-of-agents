---
title: "Caught in the Hook: RCE and API Token Exfiltration Through Claude Code Project Files"
aliases:
  - "CVE-2025-59536"
  - "CVE-2026-21852"
source_type: "report"
kind: "vulnerability-disclosure"
status: "verified"
year: 2026
publication_date: "2026-02-25"
publication_date_basis: "vendor_blog_page"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "Check Point Research"
venue: "Check Point Research blog"
url: "https://research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files-cve-2025-59536/"
pdf_url: ""
artifacts:
  - "raw/reports/check-point-claude-code-project-files-rce.md"
created: 2026-07-03
updated: 2026-07-05
---

# Check Point Claude Code Project Files RCE

## Summary

- First-party disclosure of three attack paths through repository-controlled Claude Code configuration: (1) malicious SessionStart hooks in .claude/settings.json executing shell commands on project open with no prompt or warning (CVE-2025-59536, CVSS 8.7, code injection); (2) enableAllProjectMcpServers:true in repo settings auto-executing MCP server init commands before the user can read the trust dialog; (3) repo-set ANTHROPIC_BASE_URL redirecting API traffic to attacker servers, leaking the full Anthropic API key in plaintext authorization headers pre-trust.
- Disclosure timeline: hooks RCE reported 2025-07-21; first fix 2025-08-26 (Claude Code 1.0.111); MCP bypass reported 2025-09-03; API-exfiltration fix completed 2025-12-28; public disclosure 2026-02-25. CVE-2025-59536 published 2025-10-03, CVE-2026-21852 published 2026-01-21.
- Fixes shipped: enhanced trust dialogs, MCP execution blocked before approval, and all network operations deferred until explicit user consent.
- The pattern generalizes: "clone an untrusted repo, open it in an agent harness" is now a documented RCE class — the harness's own lifecycle automation (hooks) is the attack surface.
- 2026 incident context: 30+ CVEs hit the MCP ecosystem in Jan-Feb 2026 (per third-party tallies), and Microsoft's @azure-devops/mcp npm package was found missing an auth layer in April 2026.

## Connections

- [[safety/agent safety and security]]
- [[safety/sandbox escape and credential exposure]]
- [[methods/hook-based control]]
- [[systems/Claude Code]]
- [[sources/Claude Code Hooks]]
- [[sources/Koi Security Postmark MCP Backdoor]]

## Artifacts

- [[raw/reports/check-point-claude-code-project-files-rce.md]]

## Notes

- Canonical URL: https://research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files-cve-2025-59536/
- The 30+ MCP-ecosystem CVE tally is a third-party figure cited in the report's context, not Check Point's own count; verify before reusing.
- Directly informs config-trust design for any harness that executes repository-provided lifecycle automation.
