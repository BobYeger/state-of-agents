---
title: "HorizonBench: Long-Horizon Personalization with Evolving Preferences"
aliases:
  - "HorizonBench"
source_type: "paper"
kind: "evolving-user-preference-benchmark"
status: "verified"
year: 2026
publication_date: "2026-04-19"
publication_date_basis: "arxiv_v1_submission_history"
source_updated_date: "2026-04-19"
source_updated_date_basis: "arxiv_v1_only_in_submission_history"
source_version: "arXiv v1; inspected October 5, 2026"
arxiv_id: "2604.17283"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "not assessed"
authors:
  - "Shuyue Stella Li"
  - "Bhargavi Paranjape"
  - "Kerem Oktar"
  - "Zhongyao Ma"
  - "Gelin Zhou"
  - "Lin Guan"
  - "Na Zhang"
  - "Sem Park"
  - "Lin Chen"
  - "Diyi Yang"
  - "Yulia Tsvetkov"
  - "Asli Celikyilmaz"
venue: "arXiv"
url: "https://arxiv.org/abs/2604.17283"
pdf_url: "https://arxiv.org/pdf/2604.17283v1"
license: "CC BY 4.0"
license_url: "https://creativecommons.org/licenses/by/4.0/"
evidence_class: "preprint-synthetic-benchmark-with-controlled-experiments"
artifacts: []
created: 2026-10-05
updated: 2026-10-05
---

# HorizonBench

## Contribution

HorizonBench distinguishes retrieving an earlier preference from updating a user model after relevant events. A structured mental-state graph generates six-month histories for 360 fictional users and 4,245 five-option questions, including outdated preferences as distractors.

Across 25 models, the best accuracy is 52.8%. On evolved preferences, every model selects the old value on more than a third of wrong answers. Controlled variants change history length, expression explicitness, and option subtlety. Persistent assistants need to evaluate preference revision separately from recall.

## Evidence Boundary

These are synthetic recognition tasks, not longitudinal human relationships or executed assistance. Generator-defined preference changes do not establish how real people change. Human annotation accuracy is 56–64%, with moderate agreement; the labels contain meaningful ambiguity. The strict item filter selects cases five validation models miss without history, shaping difficulty. Do not infer permission to silently overwrite a real user's preferences, or adoption by contemporary products.

## Connections

- [[concepts/persistent personal agents]]
- [[systems/personal assistant agents]]
- [[concepts/memory use calibration]]
- [[benchmarks/agent memory benchmarks]]
- [[sources/MemCalib]]

## Primary Links

- [Submission history](https://arxiv.org/abs/2604.17283).
- [Full text, v1](https://arxiv.org/html/2604.17283v1), sections 4–6 and limitations.
- [Author code and data](https://github.com/stellalisy/HorizonBench).
