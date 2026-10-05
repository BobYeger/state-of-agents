---
title: "Advisor Agents"
aliases:
  - "Executor-advisor pattern"
  - "On-demand agent advice"
created: 2026-10-05
updated: 2026-10-05
---

# Advisor Agents

An advisor supplies guidance to an executor that retains responsibility for the task. Consultation can change the executor's plan, interpretation, or next action without handing over the whole task. Advice is a role; it does not require a particular vendor tool, a stronger model, or a separate process.

## Distinguish the Control Decisions

| Mechanism | Who initiates it? | What comes back? | Who continues the task? |
|---|---|---|---|
| Model routing | Router before generation | Answer from the selected model | Selected model or caller |
| Escalation cascade | Quality gate after an answer | Replacement answer from another model | Caller |
| Advisor consultation | Executor or a harness checkpoint | Guidance, critique, uncertainty, or a proposed plan | Original executor |
| Delegated worker | Coordinator assigning a bounded task | Findings, artifact, or completed action | Coordinator integrates the result |
| Independent observer | Event subscription or a monitoring policy | Warning or intervention request | Executor, unless a separate control policy stops it |

An advisor can investigate with its own tools in some designs; a particular tool-free provider implementation does not define the whole category. Likewise, an observer may provide advice, but its independent activation means the actor need not recognize its own need for help. See [[concepts/background agents]] and [[methods/runtime supervision]].

## Research Before the Product Surface

These are conceptual antecedents and related evidence, not a claim that product teams adopted the papers.

- **2023 — conditional capability spending:** [[sources/FrugalGPT]] learns when to accept a cheaper answer or escalate.
- **2024 — selection before generation:** [[sources/RouteLLM]] learns which model should answer from preference data.
- **2023–2025 — independent checking:** [[sources/AI Control Despite Intentional Subversion]] and [[sources/Monitoring Reasoning Models for Misbehavior]] evaluate supervisors separately from actors. Their threat models and observation channels differ from ordinary task advice.
- **2026 — role allocation:** [[sources/Think Big Search Small]] isolates where model capacity matters in hierarchical retrieval. It supports measuring different roles separately; it does not prove universal gains from adding an advisor.
- **Shipped implementation:** [[sources/Claude Advisor Tool]] exposes consultation inside one request. [[sources/Claude Code Mods and You Should Know]] supplies a separately activated observer role. The two place the decision to seek help in different parts of the harness.

## Design and Evaluation

The central policy is **when to consult**. Potential checkpoints include an ambiguous plan, repeated failed attempts, conflicting evidence, a consequential action, or a completion claim. These are candidate policies to test, not validated universal triggers. A fixed consultation on every step can waste tokens, while consultation left entirely to the executor can miss errors the executor does not notice.

Give advice a clear contract: the question, relevant evidence, constraints, uncertainty, and what could change the next action. Distinguish the advisor's recommendation from an authorization decision. The executor or harness still checks permissions and verifies effects.

Compare one executor, a stronger executor, conditional advice, and a fixed-budget review policy on the same tasks. Measure marginal task success, time to recovery, false interventions, total cost, and whether advice was followed. Record consultation timing and the evidence available at that moment; otherwise a better result cannot be attributed to the advisor. Separate-context inference alone does not establish independent evidence or independent mistakes.

## Related

- [[concepts/agent loop]]
- [[methods/runtime routing]]
- [[methods/deliberative control]]
- [[concepts/evaluator reliability]]
- [[concepts/subagent context isolation]]
- [[operations/cost control]]
