---
title: "SWE-Bench Pro Verified: A Reliable Benchmark for Software Engineering Agents"
aliases:
  - "SWE-Bench Pro Verified"
source_type: "paper"
kind: "coding-benchmark-repair"
status: "verified"
year: 2026
publication_date: "2026-09-08"
publication_date_basis: "arxiv_v1_submission_history"
source_updated_date: "2026-09-08"
source_updated_date_basis: "arxiv_v1_submission_history"
source_version: "arXiv v1; inspected September 15, 2026"
arxiv_id: "2609.08149"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "not assessed"
authors:
  - "Pujun Zheng"
  - "Zixin Shang"
  - "Shufan Jiang"
  - "Wenhui Tian"
  - "Dongsheng Zhu"
  - "Zerun Ma"
  - "Dingbo Yuan"
  - "Qi Zhang"
venue: "arXiv / Shanghai Artificial Intelligence Laboratory, ECNU, Fudan"
url: "https://arxiv.org/abs/2609.08149"
pdf_url: "https://arxiv.org/pdf/2609.08149v1"
evidence_class: "preprint-with-evals-and-released-benchmark-repair"
artifacts: []
created: 2026-09-15
updated: 2026-09-15
---

# SWE-Bench Pro Verified

## Summary

- Repairs the 731-task public SWE-Bench Pro split through two distinct interventions: restrict access to answer-bearing artifacts at evaluation time, then refine instructions/tests for 102 reviewed tasks.
- Reconstructs repositories, conceals evaluation artifacts, filters metadata, and blocks known online solution sources. In a paired GLM-5.2 audit, confirmed local answer-file access fell from 103 tasks to zero and network answer-file access from 49 to zero; these task populations can overlap.
- Uses mini-swe-agent with AgentCompass across seven models. Human experts finalize task edits after LLM-assisted filtering and drafting. Most refinements change requirements; 17 of the 102 change hidden test patches.

## Numerical Caution

The v1 results do not fully reconcile. Table 3 reports GLM-5.2 baseline accuracy of 78.80%, but Table 4's baseline pass counts total 404 + 186 = 590 of 731, or 80.71%. Its anti-hacking pass count does match 57.32%. The paper does not explain this difference; the claimed 21.48-point decline should not be reused as a settled paired estimate. This discrepancy does not by itself invalidate the released controls or task edits.

## Connections

- [[sources/SWE-bench Pro]]
- [[sources/OpenAI SWE-bench Pro Audit]]
- [[sources/DeepSWE]]
- [[concepts/evaluator reliability]]
- [[benchmarks/coding agent benchmarks]]
- [[operations/agent evals]]

## Evidence Limits and Resources

- Repair covers 102 selected instances, not every flaw identified by prior audits. Network blocklists may miss proxies, mirrors, dynamic hosts, and alternate routes; local cleanup may leave residual information.
- Causal classification of pass-to-fail transitions uses an LLM annotator. Finding no observed collateral damage is not proof the controls preserve every valid workflow. “Verified” is the release name, not a vault endorsement of universal validity.
- [Versioned paper](https://arxiv.org/html/2609.08149v1), [AgentCompass code](https://github.com/open-compass/AgentCompass), and [released dataset](https://huggingface.co/datasets/opencompass/SWEBench-Pro-Verified). Independent replication and broad adoption were not established in this review.
