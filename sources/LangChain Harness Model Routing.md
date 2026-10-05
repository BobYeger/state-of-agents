---
title: "How to Build a Model Router in the Harness"
aliases: []
source_type: "article"
kind: "production-routing-experiment"
status: "verified"
year: 2026
publication_date: "2026-10-01"
publication_date_basis: "visible_blog_publication_date"
venue: "LangChain blog"
url: "https://www.langchain.com/blog/how-to-build-a-model-router-in-the-harness"
evidence_class: "vendor-run-production-AB-test"
metrics_status: "author-reported-proxy-outcomes"
artifacts: []
created: 2026-10-05
updated: 2026-10-05
---

# LangChain Harness Model Routing

Reports a 973-thread Open SWE experiment comparing routing with always using GPT-6 Astra. Median thread cost was $0.94 versus $2.61; merged-PR rates were 29.2% versus 27.3% (p = .49). The measured reduction is median cost; the nonsignificant quality proxy does not prove equivalence.

Selection occurs once per thread. Subagent model selection and mid-thread rerouting are listed as future work. Workload composition and merged-PR outcomes limit generalization; this is one team's production experiment, not independent replication.

## Connections

- [[methods/runtime routing]]
- [[concepts/advisor agents]]
- [[sources/RouteLLM]]
- [[sources/FrugalGPT]]
- [[maps/Agent Capability Research Lineage]]
