---
title: "Deployment-Time Memorization in Foundation-Model Agents"
aliases:
  - "Deployment-Time Memorization"
  - "Memorization by Design in Foundation-Model Agents"
source_type: "paper"
kind: "memory-privacy-study"
status: "verified"
year: 2026
publication_date: "2026-06-08"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: "2026-07-09"
source_updated_date_basis: "arxiv_v2_submission_date"
arxiv_id: "2606.10062"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Lei (Rachel) Chen"
  - "Guilin Zhang"
  - "Kai Zhao"
  - "Dalmo Cirne"
  - "Andy Olsen"
  - "Zeke Miller"
  - "Xu Chu"
  - "Alet Blanken"
  - "Amine Anoun"
  - "Jerry Ting"
venue: "ICML MemFM 2026 Workshop"
url: "https://arxiv.org/abs/2606.10062"
pdf_url: "https://arxiv.org/pdf/2606.10062"
license: "CC BY 4.0"
license_url: "https://creativecommons.org/licenses/by/4.0/"
created: 2026-08-16
updated: 2026-08-16
---

# Deployment-Time Memorization in Foundation-Model Agents

## Summary

- The paper treats persistent agent memory as an explicit deployment-time memorization pipeline rather than only a property of model weights. It jointly measures Personalization Recall (PR), Adversarial Extraction Rate (AER), and post-deletion Forgetting Residue Score (FRS).
- The controlled design varies three knobs: raw turns versus key-fact or one-sentence summaries, retrieval breadth `k ∈ {1,3,6}`, and five deletion modes ranging from no-op and raw-only scrubbing to resummarization, full purge, and tombstone redaction.
- On 500 stratified LongMemEval instances, key-fact summarization changes pooled AER from 0.73 to 0.29 for Gemma 3 12B and from 0.70 to 0.28 for GPT-4o-mini. Pooled PR changes from 0.57 to 0.52 and 0.59 to 0.54 respectively. Once the canary is absent from the summary, increasing retrieval breadth does not restore it.
- Privacy results are probe-dependent. GPT-4o-mini refuses the jailbreak template at every summarization level, creating a zero-AER alignment floor for that probe even while direct and indirect extraction still leak. Per-probe reporting is therefore necessary.
- The deletion study uses 50 cases per evaluated setting. With key-fact summaries, deleting only the raw record leaves the derived summary tier recoverable at FRS 0.21 for Gemma and 0.22 for GPT-4o-mini, statistically indistinguishable from leaving it untouched. Resummarizing cleaned input, fully purging derived text, or tombstone-redacting every tier produces zero observed worst-tier residue in this test.
- The leakage canaries are high-entropy strings and extraction is exact substring matching, making attribution clean but narrower than deletion of semantically paraphrasable personal facts.

## Report Implications

Deletion must operate over a derivation graph, not one record. Memory data should carry origin tier, `derived_from`, transformation history, and a purge or tombstone group that reaches summaries, embeddings, caches, skills, and other materialized views.

Memory evaluation should report three separate properties: useful recall, extractability under multiple probe classes, and deletion fidelity after every derived tier is rebuilt or invalidated. Compression can improve the privacy frontier while simultaneously creating deletion residue if lineage is not preserved.

## Evidence Boundary

This is a four-page ICML MemFM 2026 workshop paper. The main privacy–utility sweep covers 500 LongMemEval instances and two models; a third model and LoCoMo provide smaller qualitative replications. The deletion benchmark remains at 50 cases and text surfaces only, with no scaled test of embedding, cache, backup, or semantically equivalent residue.

High-entropy canaries are intentionally unlike most real deletion requests, and exact matching cannot detect paraphrased recovery. The observed zeros are therefore results for this probe and pipeline, not a compliance guarantee. Utility also depends on the chosen automatic metric; the appendix finds only moderate agreement among cosine, LLM-judge, and fact-level scoring.

## Claims

- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[operations/agent memory]]
- [[operations/permissions]]
- [[safety/agent safety and security]]
- [[maps/Safety Map]]
- [[sources/HarnessSafe]]
- [[sources/LongMemEval]]

## Notes

- Canonical arXiv URL: https://arxiv.org/abs/2606.10062
- arXiv records v1 on 2026-06-08 and v2 on 2026-07-09.
- The paper is identified as an ICML MemFM 2026 Workshop contribution.
- The paper is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
