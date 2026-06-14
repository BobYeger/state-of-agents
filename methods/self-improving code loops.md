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
| Harness optimization | Context, retrieval, tools, completion checks, and model wrapper code | [[sources/Meta-Harness]], [[sources/AFlow]], [[sources/ADAS]] |
| Algorithm evolution | Candidate algorithms or programs | [[sources/AlphaEvolve]], [[sources/LoongFlow]] |
| Autonomous research code | Experimental code, hypotheses, figures, and papers | [[sources/The AI Scientist-v2]], [[sources/Karpathy Autoresearch]] |
| Skill/procedure evolution | Reusable skills, rules, or trajectory memories | [[sources/Voyager]], [[sources/SAGE Skill Library]], [[sources/SkillRL]], [[sources/Cursor Bugbot Learned Rules]] |

## Why It Matters

This is the strongest emerging form of harness engineering because the harness is no longer only executing work. It is also exposing itself or adjacent executable artifacts to search.

The key safety distinction is evidence quality. A self-improving code loop is only as trustworthy as its evaluator, sandbox, provenance, and rollback policy. [[sources/Darwin Godel Machine]] is especially useful here because it reports both capability gains and objective-hacking failures.

## Related

- [[concepts/loop engineering]]
- [[operations/agent harnesses]]
- [[methods/agentic workflow search]]
- [[methods/runtime supervision]]
- [[operations/agent evals]]
- [[operations/sandboxes]]
- [[concepts/lifelong agent learning]]
- [[concepts/procedural memory]]
