---
title: "Levels of Autonomy for AI Agents"
aliases:
  - "Autonomy certificates"
  - "L1-L5 agent autonomy levels"
source_type: "paper"
kind: "autonomy-taxonomy"
status: "verified"
year: 2025
publication_date: "2025-07-28"
publication_date_basis: "arxiv_v2_date"
arxiv_id: "2506.12469"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "K. J. Kevin Feng"
  - "David W. McDonald"
  - "Amy X. Zhang"
venue: "Knight First Amendment Institute (Columbia) / arXiv"
url: "https://arxiv.org/abs/2506.12469"
pdf_url: "https://arxiv.org/pdf/2506.12469"
created: 2026-07-03
updated: 2026-07-03
---

# Levels of Autonomy for AI Agents

## Summary

- Defines five autonomy levels by the role the user CAN take, not by agent capability: L1 operator, L2 collaborator, L3 consultant, L4 approver, L5 observer. Autonomy is framed as a design decision separable from capability and operational environment.
- Maps shipped products to levels (as of June 2025): L1 ChatGPT Canvas / Microsoft Copilot, L2 OpenAI Operator, L3 Gemini Deep Research / GitHub Copilot Agent, L4 Devin / SWE-agent, L5 Voyager / The AI Scientist.
- Proposes "autonomy certificates": a third-party body issues a certificate specifying the maximum operating autonomy level for a given technical spec plus operational environment. The developer submits a privately deployed agent plus an "autonomy case" — an evidence-based argument, analogous to safety cases, that the agent behaves at level X and no higher. Certificates must be renewed when specs or environment change.
- Argues certificates aid multi-agent composition: predicting which agents can work synergistically at mixed autonomy levels rather than all-L1 or all-L5.
- Proposes "assisted evaluations" to measure autonomy separately from capability: run the agent fully autonomously, then progressively add user involvement (L4 down to L1) until it passes a success threshold; the minimum user-involvement level needed determines the classification.

## Connections

- [[concepts/human-in-the-loop agents]]
- [[operations/permissions]]
- [[operations/agent evals]]
- [[safety/agent safety and security]]
- [[sources/Anthropic Measuring Agent Autonomy]]
- [[sources/The 2025 AI Agent Index]]

## Notes

- Canonical URL: https://arxiv.org/abs/2506.12469
- Canonical web version at knightcolumbia.org/content/levels-of-autonomy-for-ai-agents-1; v1 submitted 2025-06-14, v2 2025-07-28.
- Autonomy certificates and assisted evaluations are proposals, not deployed mechanisms; no certifying body exists as of mid-2026.
