---
title: "AIOpsLab: A Holistic Framework to Evaluate AI Agents for Enabling Autonomous Clouds"
aliases:
  - "AIOpsLab"
source_type: "paper"
kind: "ops-agent-benchmark"
status: "verified"
year: 2025
publication_date: "2025-01-12"
publication_date_basis: "arxiv_abs_page"
arxiv_id: "2501.06706"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Yinfang Chen"
  - "Manish Shetty"
  - "Gagan Somashekar"
  - "Minghua Ma"
venue: "MLSys 2025 (arXiv) / Microsoft Research"
url: "https://arxiv.org/abs/2501.06706"
pdf_url: "https://arxiv.org/pdf/2501.06706"
artifacts:
  - "raw/papers/AIOpsLab - A Holistic Framework to Evaluate AI Agents for Enabling Autonomous Clouds.pdf"
created: 2026-07-03
updated: 2026-07-05
---

# AIOpsLab

## Summary

- End-to-end evaluation harness for "AgentOps": deploys microservice applications on Kubernetes, injects controlled faults (network partitions, resource exhaustion, misconfigurations), generates user workloads, and exports telemetry (metrics, traces, logs).
- Provides a standardized Agent-Cloud Interface (ACI) — an API through which any LLM agent interacts with the live environment — decoupling agent design from environment orchestration.
- Frames the target paradigm as AI agents autonomously managing the entire incident lifecycle (detection, localization, root-cause analysis, mitigation) toward self-healing cloud systems.
- Benchmarks state-of-the-art LLM agents and documents their capability limits on complex operational tasks; accepted at MLSys 2025.
- Open source at microsoft.github.io/AIOpsLab; companion paper "AIOpsLab in Action" appeared in the FSE 2025 companion (ACM DOI 10.1145/3696630.3728619).

## Connections

- [[benchmarks/agent evaluation]]
- [[operations/agent evals]]
- [[concepts/code factories]]
- [[sources/RCACopilot]]
- [[sources/Datadog Bits AI Eval Platform]]

## Artifacts

- [[raw/papers/AIOpsLab - A Holistic Framework to Evaluate AI Agents for Enabling Autonomous Clouds.pdf]]

## Notes

- Canonical URL: https://arxiv.org/abs/2501.06706
- Faults are injected and controlled, so difficulty is curated rather than sampled from production incident distributions — complementary to replay-based eval platforms like Datadog's.
