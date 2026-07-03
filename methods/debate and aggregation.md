# Debate and Aggregation

Debate and aggregation are inference-time methods that combine multiple model outputs on the same task — by voting, synthesis, structured argument, or a judge — into one answer.

This is narrower than [[methods/multi-agent orchestration]]. Orchestration divides a task into different roles and subtasks; aggregation spends extra samples or extra participants on the *same* question and then reconciles them. The design questions are correspondingly different: not "who owns what" but "how do outputs get reconciled, and when does another sample stop paying for itself."

## Aggregation Families

| Family | Mechanism | Anchor evidence |
|---|---|---|
| Self-consistency | Sample diverse reasoning paths from one model, majority-vote over final answers | [[sources/Self-Consistency Improves Chain of Thought Reasoning]]: +17.9% GSM8K over greedy decoding; the control condition in every later debate evaluation |
| Sampling ensembles | Many independent samples, no communication, vote | [[sources/More Agents Is All You Need]]: Llama2-13B with 15 samples beats single-query Llama2-70B on GSM8K; gains grow with task difficulty |
| Consensus debate | Agents read each other's answers and revise over rounds toward a common answer | [[sources/Multiagent Debate Improves Factuality and Reasoning]]: the original "society of minds" setup, 3 agents and 2 rounds, reports reduced hallucination |
| Adversarial debate with a judge | Debaters argue assigned opposing positions; a separate, weaker judge picks the winner | [[sources/Debating with More Persuasive LLMs]]: non-expert judges reach 76% vs 48% baseline; optimizing debaters for persuasiveness helps truth-finding |
| Layered synthesis | Each layer regenerates a response conditioned on all previous-layer outputs; aggregation by rewriting, not voting | [[sources/Mixture-of-Agents]]: open-source ensemble at 65.1% on AlpacaEval 2.0 vs 57.5% for GPT-4o |
| Judge aggregation | One model scores or ranks candidate outputs | [[sources/Judging LLM-as-a-Judge with MT-Bench]]: over 80% judge-human agreement, plus the position/verbosity/self-enhancement bias taxonomy; [[sources/Agent-as-a-Judge]] extends this to agent trajectories |

## What the Evidence Shows

The pro-aggregation results are real but predate cost-matched comparisons. [[sources/Multiagent Debate Improves Factuality and Reasoning]] reports gains across arithmetic, MMLU, and biography factuality with no task-specific tuning; [[sources/More Agents Is All You Need]] shows performance scaling with sample count, orthogonal to other methods; [[sources/Mixture-of-Agents]] documents the "collaborativeness" phenomenon in which models improve when shown other models' outputs even when those outputs are individually worse.

The controlled evaluations are corrective. [[sources/Should We Be Going MAD]] benchmarks debate protocols on cost, time, and accuracy and finds debate does not reliably outperform self-consistency and ensembling. [[sources/Stop Overvaluing Multi-Agent Debate]] evaluates five debate methods across nine benchmarks and four base models under matched conditions and finds they often fail to beat chain-of-thought and self-consistency while consuming significantly more compute.

The mechanism behind both saturation and debate failure is error correlation. [[sources/Correlated Errors in Large Language Models]] measures 350+ models and finds that when two models err, they agree 60% of the time — far above independence — which breaks the jury-theorem assumption behind majority voting. Correlation is worst among large, accurate models even across vendors, so diversity cannot be bought by mixing frontier providers. The same correlation contaminates judge aggregation: judge errors correlate with judged-model errors.

Consensus debate adds a second failure channel: sycophantic convergence. Debaters agree with the majority rather than argue, so rounds entrench the initial distribution instead of correcting it. Two levers measurably counter this. [[sources/Should We Be Going MAD]] shows that tuning agent agreement levels ("agreement modulation") can push debate past all non-debate protocols. [[sources/Stop Overvaluing Multi-Agent Debate]] identifies model heterogeneity among debaters as a universal antidote, converging with [[sources/X-MAS]] from the framework-design side. [[sources/Aligned Agents Biased Swarm]] is the cautionary complement: interaction can amplify shared biases rather than cancel them.

## Voting Versus Judge

| Condition | Prefer voting | Prefer a judge |
|---|---|---|
| Answer space | Discrete, extractable final answers | Open-ended or long-form outputs |
| Error structure | Errors plausibly decorrelated (diverse paths, heterogeneous models) | Voters share failure modes; a stronger or differently-informed judge exists |
| Information asymmetry | None; all voters see the same task | Judge can be weaker than debaters if debaters are forced into opposing positions ([[sources/Debating with More Persuasive LLMs]]) |
| Known risks | Correlated errors make added votes redundant ([[sources/Correlated Errors in Large Language Models]]) | Position, verbosity, and self-enhancement bias ([[sources/Judging LLM-as-a-Judge with MT-Bench]]); judge-voter error correlation |

The strongest option, when available, is neither: an execution-grounded check. Voting over candidate patches where a test suite defines equivalence is self-consistency with a verifier attached, and tests do not share the model's error distribution.

## When Aggregation Wastes Tokens

- **Above the capability threshold.** [[sources/Towards a Science of Scaling Agent Systems]] finds coordination yields diminishing or negative returns once the single-agent baseline exceeds roughly 0.45 accuracy; aggregation is a remedy for mid-difficulty tasks, not a universal amplifier.
- **On tool-heavy agentic tasks.** The same study finds tool-heavy tasks suffer disproportionately from multi-agent overhead. The aggregation evidence base is almost entirely single-shot QA and reasoning; [[sources/Mixture-of-Agents]] results are on LLM-judged chat benchmarks, and transfer to long tool-use trajectories is unestablished.
- **When voters are clones.** Homogeneous frontier models duplicate each other's mistakes; budget spent on a fifth correlated sample buys less than one heterogeneous debater or one independent verification channel.
- **When structure would do more.** [[sources/MacNet]] finds topology choice outperforms raw participant count, with performance following a logistic curve in agent count — the marginal agent decays predictably.

Default decision procedure: establish the self-consistency baseline at the intended budget first, since it is the cheapest member of the family and the published debate methods often fail to beat it. Escalate to debate only with heterogeneous debaters and tuned agreement pressure; use assigned-position debate with a separate judge when the goal is oversight of outputs the checker cannot verify directly; replace votes with execution checks wherever one exists.

## Related

- [[methods/multi-agent orchestration]]
- [[methods/topology optimization]]
- [[methods/deliberative control]]
- [[concepts/multi-agent systems]]
- [[concepts/scaling with computation]]
- [[concepts/outcomes and rubric graders]]
- [[operations/agent evals]]
- [[operations/cost control]]
- [[maps/MAS Orchestration and Architecture]]
- [[claims/Claim - More agents are not automatically better]]
- [[claims/Claim - Agent systems improve when structure matches the task]]
