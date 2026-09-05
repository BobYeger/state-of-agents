# Harness Design Playbook

This playbook is the decision path for designing a harness around a task. [[maps/Harness Tracker]] is the inventory of shipped harnesses; [[reports/Harness Engineering Report]] is the narrative treatment; this page is the sequence of choices, each linked to the note that carries the evidence.

The order matters: architecture first, then the eighteen harness questions, then failure-mode and verification design. Most harness problems are architecture problems chosen too early or verification problems discovered too late.

## Step 1: Choose the Architecture

Measure the single-agent baseline before adding anything. [[sources/Towards a Science of Scaling Agent Systems]] shows coordination yields diminishing or negative returns once the single-agent baseline exceeds roughly 0.45 accuracy, and relative performance against single-agent spans +80.8% (decomposable financial reasoning under centralized coordination) to -70.0% (sequential planning under independent agents) — architecture selection matched to task structure, not agent count, is the decision that matters.

| Task property | Choice | Evidence |
|---|---|---|
| Single agent already performs well | Stay single-agent; add context management, not agents | [[sources/Towards a Science of Scaling Agent Systems]]: coordination yields diminishing or negative returns past capability saturation; [[sources/Cognition Dont Build Multi-Agents]]: single-threaded agent plus compression beats parallel subagents for shared-artifact work |
| Task shape is known and repeatable | Fixed workflow or pipeline; remove the model's freedom to choose actions | [[sources/Agentless]]: a three-phase pipeline beat all open-source agent scaffolds on SWE-bench Lite at $0.70 per issue; [[sources/Anthropic Building Effective Agents]]: workflows before agents |
| Read-heavy, parallelizable breadth (research, investigation, review) | Orchestrator with read-only workers reporting back | [[sources/Anthropic Multi-Agent Research System]]: orchestrator-worker gains on breadth-first research at a large token multiple; [[sources/Towards a Science of Scaling Agent Systems]]: centralized coordination contains error amplification to 4.4x versus 17.2x for independent agents |
| Write-heavy work on a shared artifact | Single writer; parallelize read-only research and review | [[sources/Cognition Dont Build Multi-Agents]] and [[sources/Cognition Multi-Agents Whats Actually Working]]: parallel writers make conflicting implicit decisions and the production patterns keep writes single-threaded; [[sources/Factory How Missions Work]] and [[sources/Factory Missions Multi-Agent Architecture Talk]]: ordered feature mutation with internal read-only fan-out in the April-May 2026 architecture snapshot (vendor-reported; current product topology may differ) |
| Massive, benchmarkable greenfield build with many separable leaves | Recursive planner-worker swarm plus a purpose-built coordination substrate | [[sources/Cursor Agent Swarm Model Economics]]: a vendor-run SQLite rebuild improved under a new harness with custom VCS, explicit design authority, conflict agents, and megafile controls; exceptional scale and a cheap held-out evaluator make this a boundary case, not the default for shared-codebase work |
| Long-lived roles with a verification loop | Team with explicit ownership, durable handoffs, and a clean-context verifier | [[sources/MiniMax Agent Team]]: Leader/Worker/Verifier with retries; [[sources/Cognition Multi-Agents Whats Actually Working]]: a reviewer with completely clean context catches ~2 bugs per PR; [[sources/Factory How Missions Work]]: orchestrator/worker/validator roles with milestone gates; [[sources/Claude Code Agent Teams]]: shared task state across sessions — see [[concepts/agent teams]] |
| Cheap verifier, expensive generation | Sampling and voting, with eyes open about correlation | [[sources/More Agents Is All You Need]]: ensembling scales with instance count on reasoning tasks; [[sources/Correlated Errors in Large Language Models]]: models agree on the wrong answer ~60% of the time when both err, so voting gains cap early; [[sources/Stop Overvaluing Multi-Agent Debate]]: debate often fails to beat self-consistency at higher cost |

Two overheads to budget explicitly: tool-heavy tasks suffer disproportionately from coordination ([[sources/Towards a Science of Scaling Agent Systems]]), and topology choice persists while the marginal agent decays ([[sources/MacNet]]). At fleet scale, also budget for a coordination substrate: Cursor reports a purpose-built VCS, neutral conflict resolution, design-document references, and megafile decomposition as necessary control-plane machinery ([[sources/Cursor Agent Swarm Model Economics]]). [[methods/multi-agent orchestration]] carries the full treatment.

## Step 2: The Eighteen Questions

The checklist from [[reports/Harness Engineering Report]], expanded with the note that answers each question. If a question has no answer, the system is a prompt demo, not a harness.

| # | Question | Where the vault answers it |
|---|---|---|
| 1 | What is the goal, and what evidence proves it? | [[concepts/outcomes and rubric graders]]; [[sources/Claude Managed Agents Define Outcomes]]: rubric-defined outcomes as the API-level target; [[sources/OpenAI Codex Using Goals]] and [[sources/Claude Code Goals]]: evidence-checked completion contracts; [[sources/Factory How Missions Work]]: implementation-independent validation contract written during planning |
| 2 | What happens when the evidence says "not yet"? | [[methods/hook-based control]]: Stop hooks make completion criteria executable; [[concepts/loop engineering]]: retry, continuation, and stop policy as designed properties |
| 3 | What is the max turn, time, cost, or risk boundary? | [[operations/cost control]]; [[sources/METR Measuring Long Task Completion]]: time horizons as the quantitative frame for how long an agent runs per unit of oversight; [[sources/LiteLLM Proxy Budgets and Spend Tracking]] and [[sources/Claude Apps Gateway Spend Limits]]: enforcement mechanisms |
| 4 | Which state is in context, and which state is durable? | [[concepts/context engineering]]; [[operations/durable sessions]]; [[concepts/handoff over compaction]]: when to restart clean instead of compressing; [[sources/Context Engineering MCP CLAUDE-md Skills Hooks Talk]]: choose always-loaded, progressively disclosed, or just-in-time context deliberately; [[sources/Factory How Missions Work]]: externalized mission state; [[sources/Factory Missions Multi-Agent Architecture Talk]]: structured handoffs across clean-context workers |
| 5 | What can be re-fetched instead of remembered? | [[concepts/context retrieval]]; [[concepts/cache-aware harness design]]; [[sources/Manus Context Engineering]]: restorable truncation and KV-cache hit rate as the governing production metric |
| 6 | Which tools are available, and what errors do they return? | [[concepts/tool use]] and [[concepts/tool-use contracts]]; [[sources/Anthropic Writing Tools for Agents]]: tool design as interface design; [[sources/Claude API Errors]]: the provider error taxonomy retry policies must branch on |
| 7 | Which actions need human approval? | [[concepts/human-in-the-loop agents]]; [[operations/permissions]]; [[sources/Levels of Autonomy for AI Agents]]: autonomy as a design decision separable from capability; [[sources/LangGraph Interrupts]]: pause/resume mechanics and their idempotency burden |
| 8 | What sandbox or workspace boundary contains execution? | [[operations/sandboxes]]; [[sources/Anthropic Sandbox Runtime Repository]] and [[sources/Kubernetes Agent Sandbox]]: the current isolation primitives |
| 9 | Is multi-agent execution appropriate for the dependency and shared-state pattern? | [[methods/multi-agent orchestration]]; [[sources/Towards a Science of Scaling Agent Systems]]: task structure and baseline capability govern whether coordination helps; [[sources/Cognition Dont Build Multi-Agents]]: shared-artifact work often needs one writer |
| 10 | How are subagents isolated, coordinated, compacted, and handed off? | [[concepts/subagent context isolation]]; [[operations/worktree isolation]]; [[concepts/handoff over compaction]]; [[operations/durable sessions]] |
| 11 | Which roles need the strongest model, and when should they be consulted? | [[methods/runtime routing]]; [[sources/Think Big Search Small]]: delegator capacity dominates executor capacity in hierarchical search; [[sources/Claude Advisor Tool]]: concentrate expensive reasoning at selected checkpoints |
| 12 | Which stages belong in generated code versus direct semantic tool calls? | [[concepts/programmatic tool calling]]; [[sources/OpenAI Programmatic Tool Calling]]: keep judgment, writes, and approvals in direct calls; [[sources/Claude Code Workflows]]: move repeatable orchestration into inspectable scripts |
| 13 | How are traces, artifacts, decisions, and progress claims inspected later? | [[operations/agent observability]]; [[sources/OpenTelemetry GenAI Semantic Conventions]]: the emerging trace standard; [[sources/LangChain Agent Improvement Loop]]: traces as improvement-loop evidence; [[sources/Factory How Missions Work]] and [[sources/Factory Missions Multi-Agent Architecture Talk]]: externalized state and operator-facing artifacts |
| 14 | How does the system resume after crash, context loss, or human delay? | [[operations/harness fault tolerance]]; [[sources/Temporal OpenAI Agents SDK Integration]] and [[sources/Restate Durable AI Loops]]: durable execution mapped onto agent loops; [[sources/Atomix]]: transactional semantics for tool side effects |
| 15 | Which evaluator decides done, and has the task–grader contract been audited? | [[concepts/evaluator reliability]]: the judge as a measurement instrument; [[concepts/outcomes and rubric graders]]; [[operations/agent evals]]; [[sources/OpenAI SWE-bench Pro Audit]]: prompt, environment, and grader must measure the same contract |
| 16 | Which positive scope and external evidence are required before a high-impact action or completion claim? | [[operations/permissions]]; [[sources/OpenAI GPT-5.6 System Card]]: persistence can widen scope and fabricate completion; [[claims/Claim - Runtime control and verification improve agent reliability]] |
| 17 | If sessions communicate, what are the sender identity, target authority, wake, persistence, acknowledgment, reply, and inbound-policy contracts? | [[concepts/cross-session agent communication]]; [[operations/durable sessions]]; [[operations/permissions]]; [[sources/Claude Code Cross-Session Messaging]] and [[sources/OpenAI Codex Session Queueing]]: peer messages and queued turns are different authority and delivery contracts |
| 18 | Which shared services or external fetch paths can produce durable side effects across runs, and how are they isolated and monitored? | [[operations/sandboxes]]; [[operations/agent observability]]; [[sources/OpenAI Hugging Face Incident Technical Report]] and [[sources/METR OpenAI Hugging Face Incident Investigation]]: shared infrastructure can become an unauthorized communication and egress plane; [[sources/Discovery of a New OpenAI Agent Message Board]]: nominally read-oriented access can still create public shared state |

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
