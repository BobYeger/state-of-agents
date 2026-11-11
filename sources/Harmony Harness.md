---
title: "Harmony Harness: Multi-Objective Self-Evolution of Agent Harnesses"
aliases: ["Harmony Harness"]
source_type: "paper"
kind: "self-improving-harness"
status: "verified"
year: 2026
publication_date: "2026-10-10"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: "2026-10-10"
source_version: "arxiv_v1"
arxiv_id: "2610.15150"
authors: ["Weichen Yu", "Lesly Miculicich", "Bhavana Dalvi Mishra", "Jiefeng Chen", "Shuo Li", "Matt Fredrikson", "Tomas Pfister", "Long T. Le"]
venue: "arXiv"
url: "https://arxiv.org/abs/2610.15150"
pdf_url: "https://arxiv.org/pdf/2610.15150v1"
created: 2026-11-09
updated: 2026-11-09
tags: [research, harness, self-improvement]
---

# Harmony Harness

## Contribution

Evolves security and functionality as separate objectives, while factoring general mechanisms from benchmark-specific adaptations. Decomposition maintains several objective preferences; an inference-time composition step assembles applicable components.

## Evidence and Limits

Author experiments use SecRepoBench and BaxBench, plus transfer to CWEval. Table 1 reports security improvements surviving distribution shift where several baselines lose most gains. Three runs are reported, but individual splits contain at most 30 or 28 tasks; infrastructure failures reduce some denominators.

The observed Pareto fronts are narrow and sometimes collapse to one candidate best on both objectives. This limits evidence that broad frontier diversity itself explains improvement. Functional and security tests cover these benchmarks' checks, not arbitrary security properties. Generalization, composition, and search changes should be read as distinct mechanisms.

## Connections

- [[concepts/evaluator reliability]]
- [[methods/self-improving code loops]]
- [[sources/HarnessPro]]
- [[reports/Harness Self-Improvement Update - 2026-11-09]]

## Primary Links

- [Metadata](https://arxiv.org/abs/2610.15150)
- [Full text v1, Tables 1–2 and Appendices C–D](https://arxiv.org/html/2610.15150v1)
