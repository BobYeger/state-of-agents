---
title: "What is eval-driven development: How to ship high-quality agents without guessing"
aliases:
  - "Eval-driven development"
source_type: "article"
kind: "eval-gating"
status: "verified"
year: 2026
publication_date: "2026-02-18"
publication_date_basis: "vendor_article_page"
authors:
  - "Braintrust Team"
venue: "Braintrust articles"
url: "https://www.braintrust.dev/articles/eval-driven-development"
created: 2026-07-03
updated: 2026-07-03
---

# Braintrust Eval-Driven Development

## Summary

- Defines eval-driven development by four properties: evals function as specifications, dataset/run lineage is tracked, judges are calibrated against human ratings, and regression gates block deployment.
- Staged gate pipeline: development runs a smaller eval subset for fast iteration; staging requires the full suite on the complete golden dataset; production adds safety/compliance evals; CI blocks automatically if any metric falls below its threshold at any gate.
- Canary deployments route live traffic to the updated version and measure quality with the same eval criteria used offline; production monitoring runs a subset of the same evals against live traffic to detect degradation.
- Golden sets (curated inputs paired with approved reference outputs) grow over time as production traces revealing new edge cases are added, expanding regression coverage.

## Connections

- [[operations/agent evals]]
- [[concepts/code factories]]
- [[methods/self-improving code loops]]
- [[sources/Google SRE Workbook Canarying Releases]]
- [[sources/LangSmith Evaluation Concepts]]

## Notes

- Canonical URL: https://www.braintrust.dev/articles/eval-driven-development
- Vendor article; presents the dev-staging-prod gating pattern in the abstract but with Braintrust's product as the implied implementation, and offers no empirical data on gate effectiveness.
