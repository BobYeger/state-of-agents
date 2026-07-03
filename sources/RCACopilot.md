---
title: "Automatic Root Cause Analysis via Large Language Models for Cloud Incidents"
aliases:
  - "RCACopilot"
source_type: "paper"
kind: "incident-rca"
status: "verified"
year: 2023
publication_date: "2023-05-25"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2305.15778"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Yinfang Chen"
  - "Huaibing Xie"
  - "Minghua Ma"
  - "Yu Kang"
  - "Xin Gao"
  - "Liu Shi"
  - "Yunjie Cao"
  - "Xuedong Gao"
  - "Hao Fan"
  - "Ming Wen"
  - "Jun Zeng"
  - "Supriyo Ghosh"
  - "Xuchao Zhang"
  - "Chaoyun Zhang"
  - "Qingwei Lin"
  - "Saravan Rajmohan"
  - "Dongmei Zhang"
  - "Tianyin Xu"
venue: "EuroSys 2024 (arXiv preprint 2023) / Microsoft, UIUC"
url: "https://arxiv.org/abs/2305.15778"
pdf_url: "https://arxiv.org/pdf/2305.15778"
created: 2026-07-03
updated: 2026-07-03
---

# RCACopilot

## Summary

- RCACopilot is an on-call system at Microsoft that matches incoming incidents to incident handlers by alert type, aggregates critical runtime diagnostic information, predicts the incident's root-cause category, and emits an explanatory narrative.
- Achieves root-cause analysis accuracy of 0.766, evaluated on a year-long dataset of real Microsoft cloud incidents.
- The diagnostic-information-collection component had been in production at Microsoft for over four years at publication — deterministic collection pipelines precede and feed the LLM layer.
- Architecture pattern: alert-type routing to a handler, diagnostic aggregation, then LLM classification and narration — a canonical anomaly-to-ticket pipeline decomposition.
- arXiv v1 2023-05-25, v4 2023-11-13; published at EuroSys 2024 (ACM DOI 10.1145/3627703.3629553).

## Connections

- [[concepts/code factories]]
- [[sources/AIOpsLab]]
- [[sources/Meta AI Incident Response]]
- [[sources/Azure SRE Agent Docs]]

## Notes

- Canonical URL: https://arxiv.org/abs/2305.15778
- Full 18-author list verified against the arXiv abs page (2026-07-03). Dated to arXiv v1 (2023-05-25) per vault convention for conference papers; the EuroSys 2024 publication month (2024-04) is retained in the venue field only.
- The 0.766 accuracy is on Microsoft's internal incident distribution with predefined root-cause categories; it is a classification accuracy, not an end-to-end mitigation success rate.
