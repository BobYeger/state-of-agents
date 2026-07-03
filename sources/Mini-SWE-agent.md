---
title: "mini-SWE-agent (repository)"
aliases:
  - "mini-swe-agent"
source_type: "repository"
kind: "minimal-harness"
status: "verified"
year: 2026
publication_date: "2026-07-02"
publication_date_basis: "github_latest_release_date"
arxiv_id: null
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: null
authors:
  - "SWE-agent team (Princeton/Stanford)"
  - "Kilian Lieret"
venue: "GitHub"
url: "https://github.com/SWE-agent/mini-swe-agent"
pdf_url: ""
created: 2026-07-03
updated: 2026-07-03
---

# Mini-SWE-agent

## Summary

- A roughly 100-line Python agent class whose only tool is bash; it does not even use the LM tool-calling interface, so it works with any model.
- Scores over 74% on SWE-bench Verified (up from ~65% at its 2025 launch) — a striking minimal-harness baseline against elaborate scaffolds.
- Design: linear message history (every step appended); each action runs via an independent subprocess.run with no stateful shell session.
- Actively maintained: v2.4.4 released 2026-07-02, 63 releases total, 5.5k stars; used by Meta, NVIDIA, Essential AI, and IBM as an evaluation baseline.
- Built by the same Princeton/Stanford team behind SWE-bench and SWE-agent — the authors' own answer to how much of the ACI is still needed as models improve.

## Claims

- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Connections

- [[operations/agent harnesses]]
- [[maps/Harness Tracker]]
- [[sources/SWE-agent]]
- [[sources/SWE-bench Verified]]
- [[sources/The Complexity Trap]]

## Notes

- Canonical URL: https://github.com/SWE-agent/mini-swe-agent
- Functions as the control condition for harness-engineering claims: it quantifies how much harness complexity current models still require. The claim link above is comparative — the repo is evidence that as models improve, interface machinery matters less than it did in the 2024 SWE-agent result.
- Living repository: the >74% SWE-bench Verified figure and release stats are as of 2026-07-02 and will drift.
