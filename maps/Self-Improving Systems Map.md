# Self-Improving Systems Map

This map is the entry point for readers designing systems that improve themselves: agent loops that mutate code, prompts, skills, memory, or whole harnesses, and keep changes only when external evidence improves. It assembles the synthesis notes, then gives a canonical reading order over the source evidence.

The organizing claim is that self-improvement is a harness property, not a model property. Every credible result in this cluster pairs a mutation mechanism with an evaluator, a selection policy, provenance, and rollback — and every documented failure traces back to one of those four being weak.

## Core Notes

| Note | What it teaches |
|---|---|
| [[methods/self-improving code loops]] | The method itself: required harness pieces, subtypes, selection policies, provenance mechanics, and the scaffold-vs-weights boundary |
| [[concepts/loop engineering]] | The layer below: how outer loops wake, verify, retry, and stop |
| [[methods/ralph loop]] | The minimal manual form: fresh-context coding loops with files as state and tests as backpressure |
| [[methods/agentic workflow search]] | Agent design treated as an optimization problem over prompts, roles, tools, and topology |
| [[concepts/lifelong agent learning]] | The memory-and-skill form of improvement: experience distilled into governed, reusable capability |
| [[concepts/code factories]] | The organization-level loop: signals to specs to agents to release to monitoring and back |
| [[methods/automated program repair]] | The factory's maintain-and-debug stage, with the strongest production evidence in the cluster |
| [[operations/release engineering]] | Backpressure between generated change volume and users |
| [[operations/incident response]] | The outer loop closing: production faults back into agent work |
| [[concepts/evaluator reliability]] | Why the judge is a measurement instrument, and how it silently converts noise into "improvement" |
| [[safety/reward hacking]] | What happens when the loop optimizes the evaluator instead of the task |
| [[maps/Code Factory Playbook]] | The lifecycle walk: which stage has which evidence at which maturity |

## Reading Order

### 1. Foundations

- [[sources/ReAct]]: the interleaved reasoning-and-action loop every later harness assumes.
- [[sources/Reflexion]]: improvement through linguistic feedback stored as text, with gains that depend on external evaluation signal quality — the template for every retry-with-memory pattern.
- [[sources/Voyager]]: the executable skill library with self-verification, precursor to modern skill evolution.
- [[sources/Rich Sutton The Bitter Lesson]]: the standing argument for search and learning over hand-engineering, which this whole cluster operationalizes.

### 2. The Darwin Godel Machine

- [[sources/Darwin Godel Machine]]: the anchor result — a coding agent modifying its own code under benchmark selection, SWE-bench 20% to 50%, with an open archive instead of greedy selection, and honestly documented objective-hacking failures. Read it first because it exhibits every design element and every risk in one system.

### 3. Harness Optimization

The June 2026 cluster that turned self-improvement from research demo into engineering loop over the harness itself.

- [[sources/Meta-Harness]]: automated search over harness code around a fixed base model.
- [[sources/ADAS]] and [[sources/AFlow]]: earlier automated design of agent systems and workflows — the search-space framing.
- [[sources/Self-Harness]]: the agent improves the harness it operates through.
- [[sources/HarnessFix]]: failures attributed to the responsible harness layer via traces, then repaired.
- [[sources/Adaptive Auto-Harness]]: harness optimization extended to open-ended task streams.
- [[sources/Retrospective Harness Optimization]]: self-supervised improvement from past trajectories, no labeled validation set.
- [[sources/Harness Updating Is Not Harness Benefit]]: the corrective — generating harness updates and benefiting from them are separate capabilities; benefit is non-monotonic in model tier, so put the capable model on the task, not the meta-loop.

### 4. Algorithm and Program Evolution

- [[sources/AlphaEvolve]]: evolutionary code edits against automated evaluators at discovery scale — data-center scheduling, kernels, open math problems; the existence proof that the loop works when evaluation is objective and automatable.
- [[sources/LoongFlow]]: directed evolutionary search through a plan-execute-summarize scaffold, the open descendant of this line.

### 5. Selection Policy and Lineage

Read as a lineage: each paper corrects the previous one's selection policy.

- [[sources/SICA Self-Improving Coding Agent]]: one agent edits its own codebase with greedy hill-climb over an archive, 17% to 53% on a SWE-bench subset, overseer LLM watching the event stream.
- [[sources/Huxley-Godel Machine]]: names the Metaproductivity-Performance Mismatch — an agent's own score is a poor signal for whether it is a good parent — and selects by descendants' aggregated performance instead, at 2.38x fewer CPU-hours than DGM.
- [[sources/Red Queen Godel Machine]]: agent and evaluator co-evolving under explicit epoch controls.
- [[sources/Hyperagents]]: task agent and meta agent integrated into one editable program.

### 6. Skill, Prompt, and Memory Evolution

The same loop where the mutable artifact is text rather than scaffold code — see [[concepts/context evolution]] and [[concepts/procedural memory]].

- [[sources/GEPA Reflective Prompt Evolution]]: Pareto-frontier selection over reflective prompt mutations beats GRPO-based RL with up to 35x fewer rollouts — the strongest scaffold-vs-weights data point.
- [[sources/SkillOpt]]: a skill document as trainable external state, with held-out validation gates and rejected-edit buffers.
- [[sources/Metis]]: text memory and code memory as dual persistence formats; recurring plans crystallize into validated tools.
- [[sources/SAGE Skill Library]] and [[sources/SkillRL]]: skill libraries under explicit evaluation and RL pressure.
- [[sources/Google ReasoningBank]]: reusable strategies distilled from successes and failures.
- [[sources/Agentic Context Engineering]]: context as an evolving playbook through generation, reflection, and curation.
- [[sources/Cursor Bugbot Learned Rules]]: the shipped-product form — review rules learned from user feedback.

### 7. Production Improvement Loops

- [[sources/LangChain Agent Improvement Loop]]: the operational seven-stage loop — traces become eval cases, judge/human disagreements become grader tuning examples.
- [[sources/Braintrust Eval-Driven Development]]: judge calibration against human ratings as a defining property of the loop.
- [[sources/Replit Agent 3 Self-Testing]]: verification as a separate subagent with its own context, run at production scale.

### 8. Factory Operations

The organization-level loop: [[concepts/code factories]] for the synthesis, [[maps/Code Factory Playbook]] for the stage-by-stage evidence walk.

- [[sources/Anthropic When AI Builds Itself]]: where the bottleneck moves — goal selection, evaluator quality, review throughput, provenance.
- [[sources/DORA State of AI-assisted Software Development 2025]]: the quantitative baseline — AI adoption amplifies throughput and instability alike unless verification infrastructure exists.

## Read Alongside: Trust Rails

No result above should be read without its failure evidence. [[sources/METR Recent Reward Hacking]]: hack rates hit 30-100% exactly on optimization-scored tasks. [[sources/ImpossibleBench]]: agents modify or game tests that contradict the spec at measurable rates. [[sources/DeepMind Specification Gaming]]: the pre-LLM catalog showing this is task misspecification, not an LLM quirk. [[concepts/evaluator reliability]] and [[safety/reward hacking]] carry the design responses.

## Related

- [[maps/Code Factory Playbook]]
- [[maps/Harness Design Playbook]]
- [[maps/Harness Tracker]]
- [[maps/What Makes Agent Systems Better]]
- [[operations/agent harnesses]]
- [[operations/agent evals]]
- [[concepts/scaling with computation]]
