---
title: "HarnessSafe: Evaluating Safety Across Persistent Carriers in Agent Harnesses"
aliases:
  - "HarnessSafe"
  - "Persistent-Risk Lifecycle benchmark"
source_type: "paper"
kind: "harness-safety-benchmark"
status: "verified"
year: 2026
publication_date: "2026-08-07"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: null
source_updated_date_basis: null
arxiv_id: "2608.06984"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Xiao Zhang"
  - "Yusheng Wang"
  - "Yuhao Fei"
  - "Dongyuan Li"
  - "Zian Liang"
  - "Liuyu Xiang"
  - "Hongxun Gu"
  - "Zhaofeng He"
venue: "arXiv"
url: "https://arxiv.org/abs/2608.06984"
pdf_url: "https://arxiv.org/pdf/2608.06984"
license: "CC BY 4.0"
license_url: "https://creativecommons.org/licenses/by/4.0/"
artifacts:
  - "raw/papers/HarnessSafe - Evaluating Safety Across Persistent Carriers in Agent Harnesses.pdf"
created: 2026-08-11
updated: 2026-08-11
---

# HarnessSafe

## Summary

- HarnessSafe evaluates delayed safety failures in which attacker-influenced content enters one task, persists through a harness carrier, and later affects an independently benign task after the original malicious input has left active context.
- Its 328 executable cases cover seven carrier families: memory (72), reusable skills (84), Tool/MCP surfaces (70), memory-to-skill transformation (36), subagent delegation (30), session summaries (30), and shared artifacts (6).
- Each case specifies a five-part Persistent-Risk Lifecycle: entry, carrier or carrier path, persistence boundary, later benign trigger, and observable violation. A harness adapter may use native paths and mechanisms only if it preserves those roles and their evidence requirements.
- Traces receive the furthest evidence-supported stage from N0 through N5b: no contact, exposure, payload influence, persistence and re-consumption, unsafe attempt, oracle-confirmed violation, and exact-canary confirmation. Workflow noncompletion is recorded separately and never counted as safe.
- Results show strong model–harness interaction. With GPT-5.6 Sol fixed, the Chain-Stage Score is 39.4 under Claude Code and 62.3 under Codex CLI. With Claude Code fixed, changing only the backend produces scores from 22.7 to 58.7.
- Matched controls support the lifecycle mechanism. Across 279 paired Claude Code / Claude Haiku 4.5 cases, full-attack success is 25.8%; replacing the attacker source lowers it to 0.4%, preventing persistence to 2.5%, removing the later trigger to 0.0%, and cleaning the carrier before reactivation to 1.8%.

## What the Stage Model Adds

Attack-success rate counts only oracle-confirmed N5a/N5b outcomes, while the Chain-Stage Score rewards earlier containment. This distinguishes configurations with similar final attack rates but different intervention points. It also exposes carrier-specific weaknesses: Codex CLI / GPT-5.6 Sol has the highest overall score among full-support configurations and leads five carrier families, yet has the lowest reusable-skill score.

The operational controls follow the lifecycle: screen low-trust input before ingestion; validate writes to persistent carriers; preserve provenance through summaries, skill generation, delegation, and artifact handoff; recheck authority at action time; and clean or quarantine state before later work reactivates it.

## Evidence Boundary

HarnessSafe is an author-run arXiv v1 benchmark, not an independent security audit or stable product ranking. Each case is run once per configuration under a permissive non-interactive profile. Cross-harness rows usually change both model and runtime; operating-system isolation, network reachability, approval modes, and supported carrier families also differ.

Coverage is uneven, including only six shared-artifact cases. Unsupported mappings and invalid or incomplete runs are excluded rather than counted safe, and complete native execution evidence is available for only part of the evaluation. The supplementary artifact permits aggregate checks but does not provide the case-keyed ledger needed to reconstruct every run and matched-control arm independently.

## Claims

- [[claims/Claim - Untrusted content must not drive agent control flow]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Connections

- [[safety/agent safety and security]]
- [[operations/agent memory]]
- [[operations/permissions]]
- [[concepts/agent skills]]
- [[concepts/context compaction]]
- [[maps/Safety Map]]

## Artifacts

- [[raw/papers/HarnessSafe - Evaluating Safety Across Persistent Carriers in Agent Harnesses.pdf]]

## Notes

- Canonical arXiv URL: https://arxiv.org/abs/2608.06984
- arXiv lists only v1 at capture time.
- The arXiv record describes a preprint; the PDF's 2027 AAAI copyright line is not evidence of acceptance.
- The paper and preserved PDF are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
