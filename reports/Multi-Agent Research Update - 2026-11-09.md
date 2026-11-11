---
title: "Multi-Agent Research Update — 2026-11-09"
aliases: []
tags: [research-update, multi-agent]
created: 2026-11-09
updated: 2026-11-09
---

# Multi-Agent Research Update — 2026-11-09

This targeted update extends the September [[reports/Multi Agent Report]]. It emphasizes primary sources published September 17–October 25, checked November 9. Source identity and claim locations were verified; experiments were not reproduced. `status: verified` on a source card does not imply independent validation of its results.

## What Changes the Existing Synthesis

| New evidence | Change to the research model | Important limit |
|---|---|---|
| [[sources/Scaling Discovery through Test-Time Communication]] | Communication can accumulate verified discoveries, beyond dividing an already decomposable task. | Objective feedback and enough exploration budget matter; independent attempts remain a required baseline. |
| [[sources/ScaleMAS]] | The shared store's retrieval policy can matter as much as the communication graph. | A group finding a correct answer does not demonstrate that it selects that answer for delivery. |
| [[sources/OpenDGO]] | Study who holds information and who synthesizes it alongside topology. | Treat reported rankings as provisional; distinguish analytic cost models from measured runtime. |
| [[sources/SAIGE]] | Choose context boundaries as dependencies become apparent. | Its strongest gains are workload-specific, not evidence for unlimited recursive delegation. |
| [[sources/Runtime Agent Coordination for AI Scientists]] | Adaptive selection and additional verification machinery need separate evaluation. | The exploratory design does not isolate contracts from verification. |
| [[sources/Anthropic Folding Subagents into the Main Loop]] | Architecture simplification belongs in the optimization search space. | Vendor practice reports motivate experiments rather than settle the comparison. |

These findings qualify the vault's earlier emphasis on decomposability. My synthesis is that two routes can justify collaboration: independent work with compact handoffs, or iterative exploration where externally checked discoveries can improve another agent's next action. Neither route follows from headcount alone.

## Evaluation Changes to Adopt

The [[reports/DAIR Paper Review - 2026-11-09|DAIR follow-up]] adds [[sources/AgentBaton]] for within-task handoffs and [[sources/EMMA]] for retained workflow configuration. These motivate separate tests of allocation and learning; neither requires a parallel swarm. Configuration admissibility should also be distinguished from measured improvement.

The following is a proposed research protocol, not a reproduced result:

1. Compare one strong agent, independent parallel attempts, and communicating agents. Hold tools, access, and task inputs constant; report both configured budgets and actual consumption.
2. Evaluate the delivered artifact separately from best-of-team availability. Include the cost and error of selecting among candidates.
3. Ablate the shared store into private stores. This separates personal note-taking benefits from information crossing agent boundaries.
4. Log which records were read, what evidence was adopted, and which later artifacts depended on it. A message count is not evidence of useful uptake.
5. Test stale or incorrect contributions, worker loss, contradictory requirements, and a changed task distribution. Measure recovery and regressions as well as success.
6. Re-run the comparison after replacing tightly coupled subagents with skills. Keep mandatory checks outside any optimization that can silently bypass them.

## Priority Follow-Up Experiments

- **Verified sharing versus broadcast:** compare evidence-bearing artifacts with unstructured updates on the same exploratory task. Measure both independent discovery and convergence onto wrong ideas.
- **Selection gap:** add a realistic final selector to a pass@N experiment. Determine whether group capability survives a deployable commitment rule.
- **Shared-codebase integration:** follow the complementary factory update, [[reports/Code Factories Update - 2026-11-09]], for asynchronous and conflicting patch benchmarks. Mergeability and joint specification satisfaction need separate checks.
- **Replication before topology recommendations:** obtain runnable configurations, exact backbones, seed-level results, and held-out topology selection for new organization benchmarks.

## Reading Order

The [[reports/Cyber Swarms and Attacker Findings - 2026-11-09|cyber follow-up]] adds observed deployments and [[sources/CAIRN]] as a controlled architecture comparison. Keep evidence that a team was deployed separate from evidence that coordination caused a benefit. Fleets, recovered role definitions, and concurrent workers are different units.

Start with [[sources/Scaling Discovery through Test-Time Communication]] and its negative task result; then [[sources/ScaleMAS]] for the storage/retrieval mechanism. Read [[sources/SAIGE]] beside [[sources/Anthropic Folding Subagents into the Main Loop]] for the context-boundary decision. Use [[sources/Runtime Agent Coordination for AI Scientists]] as the counterexample to assuming every additional control layer improves scores. [[sources/OpenDGO]] supplies an experimental factorization to test locally.

Return to [[maps/MAS Orchestration and Architecture]], [[benchmarks/multi-agent benchmarks]], and [[reports/Research Update - 2026-11-09]] for the wider synthesis.
