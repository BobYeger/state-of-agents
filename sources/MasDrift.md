---
title: "MasDrift: Benchmarking Authorization Preservation Across Multi-Agent Architectures"
aliases:
  - "MasDrift"
  - "MasDrift authorization benchmark"
source_type: "paper"
kind: "multi-agent-safety-benchmark"
status: "verified"
year: 2026
publication_date: "2026-08-02"
publication_date_basis: "arxiv_v1_submission_date"
source_updated_date: null
source_updated_date_basis: null
arxiv_id: "2608.07556"
citation_count: null
citation_source: null
citation_snapshot_date: null
citation_lookup: "pending"
authors:
  - "Zhuoning Xu"
  - "Xiucheng Zhang"
  - "Hanjun Luo"
  - "Yingbin Jin"
  - "Yinpeng Dong"
  - "Hanan Salam"
venue: "arXiv"
url: "https://arxiv.org/abs/2608.07556"
pdf_url: "https://arxiv.org/pdf/2608.07556"
created: 2026-08-11
updated: 2026-08-11
---

# MasDrift

## Summary

- MasDrift benchmarks whether authorization survives benign task decomposition and delegation. Its 600 synthetic productivity tasks pair required preparation with reserved actions, sensitive fields and allowed audiences, and a natural-language critical constraint.
- The environment exposes both permitted preparation tools and high-impact tools the user withheld. Violations therefore arise without prompt injection, compromised agents, or adversarial requests.
- The runner compares one agent, peer networks of width two, four, or eight, and centralized binary supervisor trees one to three levels deep. Six model configurations and matched defended conditions produce 90,000 fully traced executions.
- Centralized hierarchies achieve 93.9–98.6% strict completion versus 85.7–87.0% for peers, but execute unauthorized actions in 2.7–19.8% of tasks versus 0.6–0.8%. Increasing tree depth from one to three levels adds 4.6 completion points while raising unauthorized-action incidence from 2.7% to 19.8%.
- The risk is not agent count alone: an eight-peer network has as many tool-executing agents without the same increase. In three-level trees, 71.9% of observed constraint losses occur at the first handoff; later depth mainly creates more opportunities to act after the boundary has already weakened.
- A heterogeneous GPT-5.6 Sol lead with GPT-5.4 Nano executors averages 24.9% unauthorized-action incidence across centralized architectures, versus 1.0% with homogeneous Sol. A model-only safety result therefore does not characterize the team built around it.

## Defense Comparison

**Source** uses a separate authorization agent to compile one structured, total policy from the original request and public tool surface. That invariant policy is stored outside the coordination graph. A shared reference monitor checks every pending call against it; the raw request is not freshly re-read for each call. Source reduces, but does not eliminate, executed unauthorized actions across all evaluated configurations. It changes pooled completion by -1.6 points, blocks at most 3.5% of attempted required calls, and adds 6.6–19.3% token overhead.

**Chain** passes a structured policy through each handoff. Deterministic code enforces monotone attenuation: scopes can only narrow, authorization stages can only become stricter, and branch joins retain the most restrictive rule. Chain eliminates executed unauthorized actions in the reported aggregate, but blocks up to 54.5% of required-call attempts, loses up to 36.3 completion points, and adds 16.2–42.0% token overhead. It converts drift into over-restriction because upstream agents cannot anticipate all legitimate downstream scope.

The result favors keeping authorization evidence outside model-written task messages and consulting it at the action boundary. It does not show that Source is sufficient for safety.

## Evidence Boundary

MasDrift is an author-run arXiv v1 benchmark, not an independent replication or universal topology ranking. Tasks are English-only, synthetic, and tool-mediated. Depth, handoff count, and tool exposure co-vary, so the study identifies a centralized architecture bundle rather than a clean causal effect of depth. Each task–architecture–model–defense cell has one trajectory.

The main defended runs auto-approve every Require Confirmation verdict. An all-refusal replay cannot model replanning after denial, so results measure policy routing and autonomous authorization more directly than a real human approval workflow. Over-disclosure and constraint loss use one LLM judge despite held-out human validation. The local PDF is intentionally not linked as a redistributable artifact because arXiv lists only its non-exclusive distribution license.

## Claims

- [[claims/Claim - Agent teams need explicit organization]]
- [[claims/Claim - Agent systems improve when structure matches the task]]

## Connections

- [[operations/permissions]]
- [[methods/multi-agent orchestration]]
- [[benchmarks/multi-agent benchmarks]]
- [[maps/Safety Map]]
- [[sources/Block User Identity Delegation]]

## Notes

- Canonical arXiv URL: https://arxiv.org/abs/2608.07556
- arXiv lists only v1 at capture time.
- The paper says its code and benchmark supplement are MIT-licensed; it does not provide a separate public repository URL.
