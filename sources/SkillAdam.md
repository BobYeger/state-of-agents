---
title: "SkillAdam: Stable and Efficient Skill Evolution for Agents"
aliases:
  - "SkillAdam"
source_type: "paper"
kind: "skill-optimization"
status: "verified"
year: 2026
publication_date: "2026-09-08"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: "2026-09-08"
source_updated_date_basis: "arxiv_v1_submission_date"
source_version: "arxiv_v1"
arxiv_id: "2609.08944"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Gaoyuan Li"
  - "Meihao Fan"
  - "Yizhe Liu"
  - "Shaolei Zhang"
  - "Ju Fan"
  - "Siyi Wang"
  - "Jiaheng Hou"
  - "Xudong Weng"
  - "Honghan Tian"
  - "Zang Li"
venue: "arXiv"
url: "https://arxiv.org/abs/2609.08944"
pdf_url: "https://arxiv.org/pdf/2609.08944"
created: 2026-09-15
updated: 2026-09-15
---

# SkillAdam

## Contribution

A frozen agent's Markdown skill is optimized using persistent issue/attempt history and an edit budget that shrinks when case-level effects vary. Adam supplies a functional analogy; no numerical skill gradients are computed.

## Evidence

- Seven benchmarks; mostly GPT-5.5, with Claude Sonnet 4.5 for DeepPlanning.
- DeepPlanning aggregate: 21.7% with SkillOpt versus 28.3% with SkillAdam; optimization tokens fall 67.3%, API requests 68.8% (Table 6).
- Those costs exclude skill initialization and final tests; token counts are not dollar costs.

## Boundaries

Each test case runs once. For six benchmarks, SkillAdam combines training and selection partitions while SkillOpt retains its split. Acceptance uses the proposal's sampled optimization cases, without an additional validation set. Baseline protocols differ, and several baseline results are imported from SkillOpt. These comparisons do not isolate optimizer memory or establish universal superiority.

## What It Teaches

Record unsuccessful fixes and control edit scope; retain an independent final test. Read with [[sources/SkillOpt]] and [[sources/WikiSkill]] as alternative optimizer-state designs, not interchangeable validation protocols.

## Connections

- [[maps/Agent Skills Map]]
- [[reports/Self-Improving Systems Report]]
- [[reports/Agent Memory Report]]
- [[concepts/procedural memory]]
- [[concepts/evaluator reliability]]

## Primary Links

- [Paper and submission history](https://arxiv.org/abs/2609.08944)
- [Full text, v1](https://arxiv.org/html/2609.08944v1)
- [Author repository](https://github.com/ruc-datalab/SkillAdam)
