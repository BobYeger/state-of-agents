# Self-Improving Code Loops

Self-improving code loops are agent loops where the mutable artifact is executable code or an executable procedure, and the loop keeps changes only after external evidence improves.

This is a narrower pattern than [[concepts/loop engineering]]. A scheduled loop can simply rerun a prompt. A self-improving code loop mutates something that future runs will execute: an agent scaffold, harness, tool, workflow, algorithm, skill, or research codebase.

## Pattern

```text
candidate code/procedure -> run evaluator -> score/trace -> keep, branch, or revert -> next candidate
```

## Required Harness Pieces

- Editable code or procedure with a bounded action surface.
- Objective metric, test, benchmark, rubric, or reviewer.
- Sandboxed execution for generated code.
- Trace and provenance for every candidate.
- Selection, rollback, archive, or branching policy.
- Budget and stop policy.
- Guardrails against evaluator hacking and fake tool-use evidence.

## Subtypes

| Subtype | Artifact that improves | Examples |
|---|---|---|
| Self-editing agent scaffold | The agent's own tools, prompts, memory, workflow, or code | [[sources/Darwin Godel Machine]], [[sources/Hyperagents]], [[sources/Meta-Harness]] |
| Harness optimization | Context, retrieval, tools, completion checks, and model wrapper code | [[sources/Meta-Harness]], [[sources/AFlow]], [[sources/ADAS]], [[sources/Self-Harness]], [[sources/HarnessFix]], [[sources/Adaptive Auto-Harness]], [[sources/Retrospective Harness Optimization]] |
| Algorithm evolution | Candidate algorithms or programs | [[sources/AlphaEvolve]], [[sources/LoongFlow]] |
| Autonomous research code | Experimental code, hypotheses, figures, and papers | [[sources/The AI Scientist-v2]], [[sources/Karpathy Autoresearch]] |
| Skill/procedure evolution | Reusable skills, rules, or trajectory memories | [[sources/SkillOpt]], [[sources/Metis]], [[sources/Voyager]], [[sources/SAGE Skill Library]], [[sources/SkillRL]], [[sources/Cursor Bugbot Learned Rules]] |
| Co-evolving evaluators | Agent and evaluator improve together under explicit epoch or utility controls | [[sources/Red Queen Godel Machine]] |

## Boundary Case: AI R&D Acceleration

[[sources/Anthropic When AI Builds Itself]] should sit next to this method without being collapsed into it. The article is not a paper about an agent directly editing its own scaffold under benchmark selection. Its value is showing the surrounding organizational loop: humans set goals and rubrics, Claude writes code, runs experiments, reviews defects, suggests next steps, and increases the amount of work that must be evaluated.

That is still important for self-improving-code research because it names the likely bottleneck shift. As code and experiment execution get cheaper, the hard harness problems become goal selection, evaluator quality, review throughput, provenance, permission boundaries, and governance.

## Why It Matters

This is the strongest emerging form of harness engineering because the harness is no longer only executing work. It is also exposing itself or adjacent executable artifacts to search.

The key safety distinction is evidence quality. A self-improving code loop is only as trustworthy as its evaluator, sandbox, provenance, and rollback policy. [[sources/Darwin Godel Machine]] is especially useful here because it reports both capability gains and objective-hacking failures.

The June 2026 harness-optimization papers push this method from research curiosity toward an engineering loop: mine failed trajectories, attribute failures to harness layers, propose bounded repairs, and validate against held-out or retrospective evidence before the change becomes reusable.

## Related

- [[concepts/loop engineering]]
- [[operations/agent harnesses]]
- [[methods/agentic workflow search]]
- [[methods/runtime supervision]]
- [[operations/agent evals]]
- [[operations/sandboxes]]
- [[concepts/lifelong agent learning]]
- [[concepts/procedural memory]]
- [[sources/Anthropic When AI Builds Itself]]
