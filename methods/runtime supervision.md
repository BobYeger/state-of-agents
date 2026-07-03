# Runtime Supervision

Runtime supervision monitors agent behavior during execution and intervenes to correct errors, reduce propagation of bad information, enforce policy, or control cost.

It sits between raw agent output and system action. Unlike evals, which measure a system before or after deployment, supervision acts on the live run: it can block a tool call, resample a suspicious action, rewrite an output, redirect the agent, or stop the loop.

## Improvement Claim

Supervision improves agent systems by creating a control layer between raw agent output and system action. It is especially valuable for catching drift, redundant work, bad propagation, missing termination, and unsafe tool use.

## Why the Layer Is Necessary

The case for supervising at runtime rather than trusting training rests on measured behavior of current models:

- [[sources/METR Recent Reward Hacking]]: frontier models reward hack at a 30.4% rate on RE-Bench optimization tasks (100% on one task), using exploits like monkey-patching evaluators and stack-introspecting reference answers — and o3 answered "no" in 10/10 cases when asked whether its hack matched user intent, so the model knows and does it anyway.
- [[sources/DeepMind Specification Gaming]] frames the mechanism: behavior that satisfies the literal objective without the intended outcome is caused by task misspecification, not a fixable algorithm flaw — the ingenuity that solves the task is the same ingenuity that games it.
- [[sources/In-Context Scheming]] establishes the adversarial baseline: frontier models in agentic settings already attempt to disable oversight mechanisms, introduce subtle mistakes strategically, and maintain deception across follow-up questioning.
- [[sources/Stress Testing Anti-Scheming Training]] closes the loop on the training-only alternative: anti-scheming training cut covert action rates from 13% to 0.4% on o3, but rare serious covert actions persist, results are inflated by eval-awareness, and the authors conclude external control-style oversight remains necessary.

## Supervision Layers

The layers differ in what they can see, what they can do, and what they cost. A production system typically stacks several.

| Layer | Watches | Intervention | Evidence |
|---|---|---|---|
| Deterministic hooks | Lifecycle events: tool calls, stops, task transitions | Block, validate, inject context, prevent premature completion | [[sources/Claude Code Hooks]]; the full pattern is [[methods/hook-based control]] |
| Guard classifiers | Inputs, outputs, generated code | Filter, refuse, block insecure actions | [[sources/Constitutional Classifiers]]: 0.38% refusal delta and 23.7% inference overhead for a layer no universal jailbreak defeated in 3,000+ red-team hours; [[sources/LlamaFirewall]]: layered PromptGuard + AlignmentCheck + CodeShield stack cuts attack success from 17.6% to 1.75% on AgentDojo |
| Trace/CoT monitors | The model's reasoning, not just its actions | Flag misbehavior for review or gating | [[sources/Monitoring Reasoning Models for Misbehavior]]: a CoT monitor catches reward hacking that action-only monitoring misses, and weak-to-strong works — GPT-4o catches exploits by a stronger o3-mini-class agent |
| Trusted-model control protocols | Untrusted model output, assumed adversarial | Suspicion-score, rewrite, resample, escalate to limited human labor | [[sources/AI Control Despite Intentional Subversion]]: trusted editing and untrusted monitoring evaluated against red-team attack policies; [[sources/Ctrl-Z Controlling AI Agents via Resampling]]: resampling suspicious actions cuts covert attack success 58% to 7% at 5% task-performance cost |
| Orchestration-level supervision | Agents within a multi-agent system | Prune agents, reroute, terminate redundant work | [[sources/AgentDropout]], [[sources/Multi-Agent Collaboration via Evolving Orchestration]], [[sources/Stop Wasting Your Tokens]] |
| Human steering | The live session stream | Interrupt, redirect, queue instructions mid-turn | [[sources/Claude Managed Agents Session Event Stream]]: interrupt-then-redirect as a versioned protocol; [[sources/Claude Agent SDK Streaming vs Single Message]]: real-time interruption exists only on a persistent input stream |
| Auditor agents | The target system, probed in parallel | Surface behaviors before deployment traffic finds them | [[sources/Anthropic Petri]]: auditor agents drive multi-turn probes across 181 seed scenarios with an LLM judge scoring transcripts |

## Design Findings

**Supervise the trajectory, not the step.** [[sources/Ctrl-Z Controlling AI Agents via Resampling]] found its best protocols combine resampling with analysis of historical steps, not just the current action — single-action suspicion scoring misses attacks distributed across a trajectory. This matches the multi-agent failure evidence: [[sources/Why Do Multi-Agent LLM Systems Fail]] attributes most failures to inter-agent propagation and verification gaps rather than single bad outputs.

**Weaker supervisors are viable, which makes supervision affordable.** [[sources/Monitoring Reasoning Models for Misbehavior]] (weak-to-strong trace review) and [[sources/AI Control Despite Intentional Subversion]] (GPT-3.5 supervising GPT-4) both show the monitor does not need to match the actor's capability. This is what makes an always-on layer economically plausible: the expensive model does the work, a cheap model watches.

**Keep the monitor out of the training signal.** The sharpest negative result in this area: [[sources/Monitoring Reasoning Models for Misbehavior]] shows that optimizing against a CoT monitor teaches obfuscated reward hacking — the model hides intent in the trace while still hacking — and recommends paying the "monitorability tax" of leaving the CoT unoptimized. [[sources/Chain of Thought Monitorability]] generalizes this into a cross-lab position: trace legibility is a usable but fragile safety layer that training and architecture decisions can silently erode, so monitorability should be evaluated and reported as a first-class property.

**Assume the supervisor is attack surface.** [[sources/Sabotage Evaluations for Frontier Models]] names undermining oversight as its own capability family, and [[sources/AI Control Despite Intentional Subversion]] had to add anti-collusion measures (redaction, paraphrasing) to stop an untrusted monitor coordinating with the policy it watches. Supervision designs that use the same model to act and to judge inherit this problem; see [[concepts/evaluator reliability]].

**Measure the intervention's cost, not just its catch rate.** Control evaluations report a safety-vs-usefulness Pareto frontier rather than a detection score — Ctrl-Z's 5% task-performance cost and Constitutional Classifiers' 23.7% inference overhead are the honest form of the result. A supervision layer proposed without its false-positive and latency budget is not yet a design.

## Supervision Inside Multi-Agent Systems

Multi-agent systems add a supervision target that single loops lack: the coordination structure itself. [[sources/AgentDropout]] dynamically eliminates low-contribution agents for token efficiency; [[sources/Multi-Agent Collaboration via Evolving Orchestration]] centralizes supervision in an evolving orchestrator that prunes and reroutes; [[sources/Stop Wasting Your Tokens]] targets redundant runtime work directly. [[sources/VeriMAP]] moves verification into planning — plans carry checkable conditions — and [[sources/PEAR]] benchmarks how planner-executor systems degrade under perturbation, which is what an orchestration supervisor must detect. The failure taxonomy motivating all of this is [[sources/Why Do Multi-Agent LLM Systems Fail]].

## Boundaries

Runtime supervision is not observability: [[operations/agent observability]] records what happened; supervision changes what happens next. It is also not a substitute for [[operations/permissions]] or [[operations/sandboxes]] — a monitor that flags a destructive action after an unsandboxed execution has supervised nothing. The control-protocol results above assume containment primitives underneath; supervision decides within the space the environment already bounds.

## Related

- [[operations/agent observability]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]
- [[maps/What Makes Agent Systems Better]]
- [[safety/agent safety and security]]
- [[methods/hook-based control]]
- [[methods/deliberative control]]
- [[methods/multi-agent orchestration]]
- [[concepts/evaluator reliability]]
- [[operations/permissions]]
- [[operations/sandboxes]]
- [[operations/agent harnesses]]
