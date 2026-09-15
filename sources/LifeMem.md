---
title: "LifeMem: Enabling Lifelong Experience Reuse for LLM Agents"
aliases:
  - "LifeMem"
source_type: "paper"
kind: "lifelong-agent-memory"
status: "verified"
year: 2026
publication_date: "2026-09-11"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: "2026-09-11"
source_updated_date_basis: "arxiv_v1_submission_date"
source_version: "arxiv_v1"
arxiv_id: "2609.12655"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Yuli Qiu"
  - "Yutong Li"
  - "Wei Su"
  - "Zeming Liu"
  - "Wanxiang Che"
  - "Heyan Huang"
  - "Haifeng Wang"
  - "Yuhang Guo"
venue: "arXiv; EMNLP 2026 Main Conference (acceptance reported in arXiv record)"
url: "https://arxiv.org/abs/2609.12655"
pdf_url: "https://arxiv.org/pdf/2609.12655"
created: 2026-09-15
updated: 2026-09-15
---

# LifeMem

## Contribution

Groups interaction trajectories by workflow, distills skills within each group, and retrieves environment-compatible examples alongside transferable procedures. Memory organization changes; model weights stay fixed.

## Evidence

- Ten environments, 12,489 training and 1,230 test instances; GPT-4o-mini, DeepSeek-v3.2-exp, and Qwen3-32B.
- GPT-4o-mini overall performance: ExpeL 41.85 versus LifeMem 44.13; backward transfer +3.10 versus +5.66 (Table 2).
- Ablations remove either skills or examples; removing concrete examples causes the larger loss (Table 9).

## Boundaries

Benefits vary across domains, and some memory-assisted results trail memory-free ReAct. Task order changes outcomes. New trajectories include model-generated actions reviewed by humans; the dataset is not wholly human-authored. Prompt-length estimates exclude full trajectory execution costs. The paper does not establish frontier-model or production gains.

## What It Teaches

Test retention and transfer as experience accumulates. Abstract procedures and environment-specific examples play complementary roles; indiscriminate cross-environment retrieval can interfere with correct actions.

## Connections

- [[concepts/lifelong agent learning]]
- [[concepts/procedural memory]]
- [[reports/Agent Memory Report]]
- [[reports/Agent Memory Technical Brief]]
- [[benchmarks/agent memory benchmarks]]
- [[sources/Reflexion]]
- [[sources/Metis]]

## Primary Links

- [Paper and submission history](https://arxiv.org/abs/2609.12655)
- [Full text, v1](https://arxiv.org/html/2609.12655v1)
- [Author code and data](https://github.com/BITHLP/LifeMem)
