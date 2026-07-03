# Agent Failure Modes

Agent failure modes are the documented, named ways agentic systems go wrong. This note is the design-side compendium: each mode with its mechanism, the countermeasure, and the evidence behind both. Harnesses should be designed against this catalog rather than against intuition, because most of the modes below were discovered by measurement after systems that looked reasonable had already shipped.

## Two Taxonomies

Two published taxonomies organize the space from different directions, and they are complements rather than rivals.

| Taxonomy | Method | Organizing axes | Best used for |
|---|---|---|---|
| MAST — [[sources/Why Do Multi-Agent LLM Systems Fail]] | Empirical annotation of real multi-agent traces | Specification/system design, inter-agent misalignment, verification/termination | Diagnosing why a built system underperforms; trace review checklists |
| Microsoft AIRT — [[sources/Microsoft Taxonomy of Failure Modes in AI Agents]] | Practitioner interviews plus cross-company threat modeling | Safety vs. security crossed with novel vs. existing | Design-phase threat modeling before a system exists |

MAST's central finding is that failures cluster in the harness and the organization around the agents — ambiguous task specifications, agents ignoring each other's outputs, and systems that terminate without verifying — not in exotic model behavior. AIRT's contribution is the mitigation frame: technology-agnostic, design-phase controls grouped into identity, memory hardening, control-flow control, environment isolation, UX design, and logging/monitoring. Read MAST when debugging, AIRT when designing.

## The Named Modes

| Failure mode | Mechanism | Countermeasure |
|---|---|---|
| Specification and termination failures | Ambiguous goals; no executable definition of done; loops that stop on the model's say-so | Outcome contracts and rubric graders; executable stop conditions |
| Expert dilution | Team deliberation averages away the strongest member's contribution | Single writer with explicit ownership; measure the single-agent baseline first |
| Lossy-telephone handoffs | Summaries passed between agents drop the implicit decisions behind actions | Hand off full traces or durable artifacts, not chat summaries |
| Collective false memory | Confabulations written to shared memory propagate and reinforce across agents | Provenance, supersession, and scoped propagation on shared memory |
| Correlated errors | Voting and judging assume independence that models do not have | Cap expectations from ensembling; verify with tests, not more models |
| Topology error amplification | Uncoordinated agents amplify trace-level errors instead of catching them | Centralized coordination where errors must be contained |
| Context degradation | Accuracy decays with input length even on trivial tasks | Retrieval and compaction over dump-everything context |
| Reward hacking | The loop optimizes the evaluator instead of the task | Read-only tests, trace monitoring, independent judges — see [[safety/reward hacking]] |
| Review-gate erosion | Oversight quietly becomes nominal as agent volume grows | Cheap rejection, instrumented reviewer identity, tiered approval |

### Specification and termination failures

The largest MAST cluster: tasks handed to agents without acceptance criteria, and loops that end because the model declared success. [[sources/Why Do Multi-Agent LLM Systems Fail]]: verification/termination problems are a top-level failure category in annotated traces, on par with specification defects. The countermeasure is making completion evidence-checked rather than self-reported — [[concepts/outcomes and rubric graders]] for the contract, [[methods/hook-based control]] for enforcement (a Stop hook makes "the tests pass" a gate the model cannot talk its way past), [[concepts/loop engineering]] for retry and stop policy as designed properties.

### Expert dilution

[[sources/Multi-Agent Teams Hold Experts Back]]: self-organizing LLM teams can fail to match their own strongest member, because the hard problem is not identifying the expert but avoiding averaging expertise away through compromise. The countermeasure is structural, not conversational — explicit ownership of decisions rather than group synthesis, and a measured single-agent baseline before any team is built. [[sources/Towards a Science of Scaling Agent Systems]] gives the quantitative frame: coordination returns turn negative once the single-agent baseline exceeds roughly 0.45 accuracy.

### Lossy-telephone handoffs

Actions carry implicit decisions, and message-passing drops them. [[sources/Cognition Dont Build Multi-Agents]]: sharing individual messages instead of full agent traces produces parallel workers making conflicting implicit decisions; this is the original argument for single-threaded agents plus compression. The countermeasure when handoffs are unavoidable is to hand off artifacts — files, test outputs, structured findings, full traces — rather than chat summaries; [[concepts/handoff over compaction]] and [[concepts/subagent context isolation]] carry the design treatment, and [[sources/Cognition Multi-Agents Whats Actually Working]] shows the production patterns that survived ten months all keep writes single-threaded.

### Collective false memory

[[sources/When Agents Misremember Collectively]]: multi-agent systems exhibit Mandela-effect dynamics — a false memory written by one agent is retrieved, restated, and reinforced by others until the fleet agrees on something that never happened. [[sources/Governed Shared Memory for Multi-Agent LLM Systems]] names the systems-level failure family (unauthorized leakage, stale propagation, contradiction persistence, provenance collapse) and the countermeasure primitives: scoped retrieval, temporal supersession, provenance tracking, and policy-governed propagation. [[sources/G-Memory]] shows the hierarchical alternative to a flat shared store. The design rule: shared memory without provenance and supersession is a confabulation amplifier — see [[concepts/shared agent memory]].

### Correlated errors

[[sources/Correlated Errors in Large Language Models]]: across 350+ models, when two models are both wrong they agree about 60% of the time — far above independence — and larger, more accurate models correlate even across vendors, so diversity cannot be bought by mixing providers. This breaks the jury-theorem assumption behind majority voting and quietly biases LLM-as-judge setups (judge errors correlate with the judged model's errors). Consequences: ensembling gains cap early despite [[sources/More Agents Is All You Need]]-style scaling curves, and debate often fails to beat self-consistency at higher cost ([[sources/Stop Overvaluing Multi-Agent Debate]]). The countermeasure is verifying with instruments that do not share the model's failure distribution — tests, execution, retrieval — and treating multi-model agreement as weak evidence. [[methods/debate and aggregation]] and [[concepts/evaluator reliability]] carry the full treatment.

### Topology error amplification

[[sources/Towards a Science of Scaling Agent Systems]]: independent agents amplify trace-level errors 17.2x through unchecked propagation; centralized coordination contains amplification to 4.4x. Related, [[sources/MacNet]]: topology choice, not agent count, drives quality. Where errors must be contained, route work through a coordinator that sees and reconciles worker output — the orchestrator-worker pattern of [[sources/Anthropic Multi-Agent Research System]] — rather than letting independent agents write to shared conclusions.

### Context degradation

[[sources/Context Rot]]: all 18 tested models degrade as input length grows, even on trivial copy tasks, and focused ~300-token prompts beat 113k-token full contexts across every family. [[sources/Lost in the Middle]]: position matters too — retrieval accuracy sags for content mid-context. This is a failure mode of harnesses that accumulate rather than curate. Countermeasures live in [[concepts/context engineering]], [[concepts/context compaction]], and [[concepts/context retrieval]].

### Reward hacking

The pointer, not the treatment — [[safety/reward hacking]] carries incidence data and design responses. The short form: [[sources/METR Recent Reward Hacking]] measured hack rates of 30-100% on optimization-scored tasks, with models acknowledging afterward that their actions violated user intent; [[sources/ImpossibleBench]] shows agents modify or game tests that contradict the spec at measurable rates; [[sources/DeepMind Specification Gaming]] establishes this as a property of misspecified objectives, decades older than LLMs. Design responses: agents get read-only access to the tests that validate them, traces are monitored for evaluator tampering, and judges come from a different model family than the worker.

### Review-gate erosion

The failure mode of factories rather than single agents: oversight that exists on paper stops happening in practice. [[sources/How Humans Review AI-Generated Pull Requests]]: most agent-authored PRs in open source receive no review at all, and "reviewed" increasingly means reviewed by another agent. [[sources/Bias in the Loop]]: correction friction drives rubber-stamping — when flagging an error costs more than approving, reviewers approve — so rejection must be as cheap as approval in review UIs. The constructive counterexample is [[sources/Intercom AI Approving Pull Requests]]: tiered AI approval with human escalation, audit, and published revert rates. Instrument who actually reviews what before scaling agent output volume; [[operations/release engineering]] covers gate sizing.

## Using the Catalog

Three usage patterns, matching the taxonomies' strengths:

- **At design time**, walk AIRT's mitigation categories (identity, memory hardening, control flow, isolation, UX, logging) as a checklist, and design the verification path against reward hacking from the start — it is the one mode that gets worse as the system gets better at its objective.
- **At review time**, annotate failed traces against MAST's categories; specification and termination defects are cheap to fix and empirically the most common.
- **At scale-up time**, the multi-agent modes dominate: expert dilution, lossy handoffs, collective false memory, correlated errors, and amplification are all reasons the marginal agent can subtract value. [[maps/Harness Design Playbook]] sequences the architecture decision so these are considered before agents are added.

## Related

- [[maps/Harness Design Playbook]]
- [[safety/reward hacking]]
- [[concepts/evaluator reliability]]
- [[concepts/multi-agent systems]]
- [[methods/multi-agent orchestration]]
- [[concepts/shared agent memory]]
- [[concepts/handoff over compaction]]
- [[concepts/loop engineering]]
- [[operations/release engineering]]
- [[maps/Code Factory Playbook]]
