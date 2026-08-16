---
title: "When Memory Becomes Authority: Benchmarking Authority Collapse at the Memory Consolidation Boundary"
aliases:
  - "When Memory Becomes Authority"
  - "AuthMem-Bench"
  - "Authority Collapse Benchmark"
source_type: "paper"
kind: "memory-authority-benchmark"
status: "verified"
year: 2026
publication_date: "2026-08-03"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: "2026-08-04"
source_updated_date_basis: "arxiv_v2_submission_date"
arxiv_id: "2608.01679"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Qiuyang Zhan"
  - "Rui Zhang"
  - "Sheng Guo"
  - "Lepeng Zhao"
  - "Zhuotao Liu"
venue: "arXiv"
url: "https://arxiv.org/abs/2608.01679"
pdf_url: "https://arxiv.org/pdf/2608.01679"
license: "arXiv non-exclusive distribution"
license_url: "https://arxiv.org/licenses/nonexclusive-distrib/1.0/"
created: 2026-08-16
updated: 2026-08-16
---

# When Memory Becomes Authority

## Summary

- The paper defines **authority collapse**: consolidation preserves a proposition but erases the source conditions governing how it may be reused, turning a report, tool observation, or assistant suggestion into an apparent user fact, preference, or standing instruction.
- AuthMem-Bench constructs 350 paired cases from 50 base histories crossed with seven source-to-use transitions. Each pair holds the focal proposition, operative value, later task, tool schema, and action predicate fixed while changing whether the proposition has a user authority witness.
- Module A crosses seven memory-writing objectives with seven LLM backbones. Authority upgrades occur in 48 of 49 configurations. The only zero-upgrade cell omits all 350 non-authorizing propositions, avoiding collapse through non-retention rather than preserving authority.
- In the controlled action module, source-washed memories without authority metadata produce 50.3% unauthorized-action rate and 49.4% authorized task success. Natural-language source attribution lowers unauthorized action to 40.5%; gold structured labels lower it to 5.8% for washed text and 2.7% when source attribution is also present, while authorized success remains 53.9%.
- The frozen end-to-end pipeline uses a predicted primary source mapped to `Authorized`, `Attested`, or `Unendorsed`. On 70 held-out pairs, predicted metadata changes prohibited actions from 10/70 to 0/70 while authorized completions remain 20/70. Across all 350 pairs, observed unauthorized action falls from 16.9% to 0.0%, while authorized success changes from 39.7% to 40.0%.
- The defense governs how retained memory may be used; it does not repair omission. The selected consolidator retains the focal proposition in only 256 of 350 authorized histories.

## Report Implications

Memory provenance and operational authorization must be separate fields. `user`, `assistant`, `tool`, or `web` describes origin; it does not by itself encode whether a memory may personalize an answer, justify a protected action, or become a standing instruction.

The memory contract should persist source spans, writer identity, authority label, and permitted uses through consolidation and retrieval, then enforce them again at the action boundary. Authority is also distinct from factual confidence: a true tool observation can still be unauthorized for a particular downstream use.

## Evidence Boundary

This is an author-run arXiv v2 benchmark over synthetic paired transformations derived from 50 τ²-Bench and APIGen histories. Its three-label authority policy is deliberately role-based and narrower than a real deployment policy with delegated scopes, revocation, organizations, and jurisdiction-specific rules.

Module A uses an LLM judge, while the downstream action modules use exact tool-call predicates. The strongest end-to-end claim comes from one selected pipeline and only 70 held-out pairs; zero observed violations is not evidence of zero residual risk. Model and product-prompt results are configuration-specific, while the durable finding is that source distinctions can be lost and that explicit use constraints outperform prose attribution under this protocol.

## Claims

- [[claims/Claim - Untrusted content must not drive agent control flow]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]

## Connections

- [[operations/agent memory]]
- [[operations/permissions]]
- [[safety/agent safety and security]]
- [[maps/Safety Map]]
- [[sources/HarnessSafe]]
- [[sources/Memory Poisoning Attacks in LLM Agents]]

## Notes

- Canonical arXiv URL: https://arxiv.org/abs/2608.01679
- The paper evaluates v2; arXiv records v1 on 2026-08-03 and v2 on 2026-08-04.
- arXiv lists its non-exclusive distribution license, not a Creative Commons reuse license.
