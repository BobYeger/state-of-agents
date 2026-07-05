# Harness Design Playbook

This playbook is the decision path for designing a harness around a task. [[maps/Harness Tracker]] is the inventory of shipped harnesses; [[reports/Harness Engineering Report]] is the narrative treatment; this page is the sequence of choices, each linked to the note that carries the evidence.

The order matters: architecture first, then the twelve harness questions, then failure-mode and verification design. Most harness problems are architecture problems chosen too early or verification problems discovered too late.

## Step 1: Choose the Architecture

Measure the single-agent baseline before adding anything. [[sources/Towards a Science of Scaling Agent Systems]] shows coordination yields diminishing or negative returns once the single-agent baseline exceeds roughly 0.45 accuracy, and relative performance against single-agent spans +80.8% (decomposable financial reasoning under centralized coordination) to -70.0% (sequential planning under independent agents) — architecture selection matched to task structure, not agent count, is the decision that matters.

| Task property | Choice | Evidence |
|---|---|---|
| Single agent already performs well | Stay single-agent; add context management, not agents | [[sources/Towards a Science of Scaling Agent Systems]]: coordination yields diminishing or negative returns past capability saturation; [[sources/Cognition Dont Build Multi-Agents]]: single-threaded agent plus compression beats parallel subagents for shared-artifact work |
| Task shape is known and repeatable | Fixed workflow or pipeline; remove the model's freedom to choose actions | [[sources/Agentless]]: a three-phase pipeline beat all open-source agent scaffolds on SWE-bench Lite at $0.70 per issue; [[sources/Anthropic Building Effective Agents]]: workflows before agents |
| Read-heavy, parallelizable breadth (research, investigation, review) | Orchestrator with read-only workers reporting back | [[sources/Anthropic Multi-Agent Research System]]: orchestrator-worker gains on breadth-first research at a large token multiple; [[sources/Towards a Science of Scaling Agent Systems]]: centralized coordination contains error amplification to 4.4x versus 17.2x for independent agents |
| Write-heavy work on a shared artifact | Single writer; other agents advise, review, or answer questions | [[sources/Cognition Dont Build Multi-Agents]]: parallel writers make conflicting implicit decisions; [[sources/Cognition Multi-Agents Whats Actually Working]]: the ten-month follow-up keeps writes single-threaded across all three production patterns |
| Long-lived roles with a verification loop | Team with explicit ownership and a verifier role | [[sources/MiniMax Agent Team]]: Leader/Worker/Verifier with retries; [[sources/Cognition Multi-Agents Whats Actually Working]]: a reviewer with completely clean context catches ~2 bugs per PR; [[sources/Claude Code Agent Teams]]: shared task state across sessions — see [[concepts/agent teams]] |
| Cheap verifier, expensive generation | Sampling and voting, with eyes open about correlation | [[sources/More Agents Is All You Need]]: ensembling scales with instance count on reasoning tasks; [[sources/Correlated Errors in Large Language Models]]: models agree on the wrong answer ~60% of the time when both err, so voting gains cap early; [[sources/Stop Overvaluing Multi-Agent Debate]]: debate often fails to beat self-consistency at higher cost |

Two overheads to budget explicitly: tool-heavy tasks suffer disproportionately from coordination ([[sources/Towards a Science of Scaling Agent Systems]]), and topology choice persists while the marginal agent decays ([[sources/MacNet]]). [[methods/multi-agent orchestration]] carries the full treatment.

## Step 2: The Twelve Questions

The checklist from [[reports/Harness Engineering Report]], expanded with the note that answers each question. If a question has no answer, the system is a prompt demo, not a harness.

| # | Question | Where the vault answers it |
|---|---|---|
| 1 | What is the goal, and what evidence proves it? | [[concepts/outcomes and rubric graders]]; [[sources/Claude Managed Agents Define Outcomes]]: rubric-defined outcomes as the API-level target; [[sources/OpenAI Codex Using Goals]] and [[sources/Claude Code Goals]]: evidence-checked completion contracts |
| 2 | What happens when the evidence says "not yet"? | [[methods/hook-based control]]: Stop hooks make completion criteria executable; [[concepts/loop engineering]]: retry, continuation, and stop policy as designed properties |
| 3 | What is the max turn, time, cost, or risk boundary? | [[operations/cost control]]; [[sources/METR Measuring Long Task Completion]]: time horizons as the quantitative frame for how long an agent runs per unit of oversight; [[sources/LiteLLM Proxy Budgets and Spend Tracking]] and [[sources/Claude Apps Gateway Spend Limits]]: enforcement mechanisms |
| 4 | Which state is in context, and which state is durable? | [[concepts/context engineering]]; [[operations/durable sessions]]; [[concepts/handoff over compaction]]: when to restart clean instead of compressing |
| 5 | What can be re-fetched instead of remembered? | [[concepts/context retrieval]]; [[concepts/cache-aware harness design]]; [[sources/Manus Context Engineering]]: restorable truncation and KV-cache hit rate as the governing production metric |
| 6 | Which tools are available, and what errors do they return? | [[concepts/tool use]] and [[concepts/tool-use contracts]]; [[sources/Anthropic Writing Tools for Agents]]: tool design as interface design; [[sources/Claude API Errors]]: the provider error taxonomy retry policies must branch on |
| 7 | Which actions need human approval? | [[concepts/human-in-the-loop agents]]; [[operations/permissions]]; [[sources/Levels of Autonomy for AI Agents]]: autonomy as a design decision separable from capability; [[sources/LangGraph Interrupts]]: pause/resume mechanics and their idempotency burden |
| 8 | What sandbox or workspace boundary contains execution? | [[operations/sandboxes]]; [[sources/Anthropic Sandbox Runtime Repository]] and [[sources/Kubernetes Agent Sandbox]]: the current isolation primitives |
| 9 | How are subagents isolated and coordinated? | [[concepts/subagent context isolation]]; [[operations/worktree isolation]]; [[methods/multi-agent orchestration]] |
| 10 | How are traces, artifacts, and decisions inspected later? | [[operations/agent observability]]; [[sources/OpenTelemetry GenAI Semantic Conventions]]: the emerging trace standard; [[sources/LangChain Agent Improvement Loop]]: traces as the raw material of the improvement loop |
| 11 | How does the system resume after crash, context loss, or human delay? | [[operations/harness fault tolerance]]; [[sources/Temporal OpenAI Agents SDK Integration]] and [[sources/Restate Durable AI Loops]]: durable execution mapped onto agent loops; [[sources/Atomix]]: transactional semantics for tool side effects |
| 12 | Which evaluator decides done? | [[concepts/evaluator reliability]]: the judge as a measurement instrument; [[concepts/outcomes and rubric graders]]; [[operations/agent evals]] |

## Step 3: Design for Failure

Design against the documented catalog, not intuition. [[concepts/agent failure modes]] compiles the named failure modes — specification and termination failures, expert dilution, lossy handoffs, collective false memory, correlated errors, review-gate erosion — each with its countermeasure and evidence.

Verification design has its own discipline:

- Treat every keep/revert or pass/fail decision as a measurement with error bars. [[sources/On Randomness in Agentic Evals]]: single-run pass@1 varies by 2.2-6.0 points even at temperature 0; [[sources/Adding Error Bars to Evals]] supplies the statistical machinery.
- Report reliability, not just capability. [[sources/Tau-Bench]]: pass^k (all k of k trials) is the deployment-relevant bound, and agents near 50% average success fall below 25% at pass^8.
- Assume the evaluator will be gamed under pressure. [[safety/reward hacking]] carries the incidence data and the design responses — read-only test access, trace monitoring, judges from a different model family.
- Score the environment, not only the agent. [[sources/Factory Agent Readiness]]: build, tests, docs, and observability readiness gate what any harness can achieve in a given repository.

## Related

- [[maps/Harness Tracker]]
- [[reports/Harness Engineering Report]]
- [[operations/agent harnesses]]
- [[concepts/agent failure modes]]
- [[concepts/evaluator reliability]]
- [[maps/Self-Improving Systems Map]]
- [[maps/Code Factory Playbook]]
- [[maps/Evaluation Map]]
- [[maps/What Makes Agent Systems Better]]
