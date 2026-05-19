Title: ReasoningBank: Enabling agents to learn from experience

URL Source: https://research.google/blog/reasoningbank-enabling-agents-to-learn-from-experience/

Markdown Content:
Agents are becoming increasingly crucial in tackling complex real-world tasks, ranging from general web navigation to assisting with extensive software engineering codebases. However, as these agents transition into persistent, long-running roles in the real world, they face a critical limitation: they struggle to analyze and learn from successful and failed experiences after deployment.

Agents approaching each new task without a memory mechanism will repeatedly make the same strategic errors and discard valuable insights. To address this, various forms of agent memory have been introduced to store information about past interactions for reuse. However, existing methods generally focus on saving exhaustive records of every action taken — such as the trajectory memory used in [Synapse](https://arxiv.org/abs/2306.07863) — or only documenting workflows summarized from successful attempts, as seen in [Agent Workflow Memory](https://arxiv.org/abs/2409.07429)). These approaches have two fundamental drawbacks: first, by recording detailed actions instead of tactical foresight, they fail to distill higher-level, transferable reasoning patterns; second, by over-emphasizing successful experiences, they miss out on a primary source of learning — their own failures.

To bridge this gap, in our ICLR paper, "[ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory](https://arxiv.org/abs/2509.25140)", we introduce a novel agent memory framework ([github](https://github.com/google-research/reasoning-bank)) that distills useful insights from both successful and failed experiences for test-time self-evolution. When evaluated on web browsing and software engineering benchmarks, ReasoningBank enhances both agent effectiveness (higher success rates) and efficiency (fewer task steps) compared to baseline approaches.

## Distilling insights with ReasoningBank

ReasoningBank distills global reasoning patterns into high-level, structured memories. Each structured memory item contains the following:

*   _Title_: A concise identifier summarizing the core strategy.
*   _Description_: A brief summary of the memory item.
*   _Content_: The distilled reasoning steps, decision rationales, or operational insights extracted from past experiences.

The memory workflow operates in a continuous, closed loop of retrieval, extraction, and consolidation. Before taking action, the agent draws upon the ReasoningBank to gather relevant memories into its context. It then interacts with the environment and uses an [LLM-as-a-judge](https://arxiv.org/abs/2306.05685) to self-assess the resulting trajectory and extracts success insights or failure reflection. Notably, this self-judgement does not need to be perfectly accurate, as we find ReasoningBank to be quite robust against judgment noise. During extraction, the agent distills workflows and generalizable insights from the trajectory into new memories. For simplicity, we directly append these to the ReasoningBank, leaving more sophisticated consolidation strategies for future work.

Crucially, unlike existing [workflow memory strategies](https://arxiv.org/abs/2409.07429) that only focus on successful runs, ReasoningBank actively analyzes failed experiences to source counterfactual signals and pitfalls. By distilling these mistakes into preventative lessons, ReasoningBank builds powerful strategic guardrails. For example, instead of merely learning a procedural rule like "click the 'Load More' button”, the agent might learn from a past failure to "always verify the current page identifier first to avoid infinite scroll traps before attempting to load more results”.

## Memory-aware test-time scaling (MaTTS)

[Test-time scaling](https://arxiv.org/abs/2408.03314) (TTS) — scaling compute at inference time — has shown immense effectiveness in reasoning domains like [math](https://arxiv.org/abs/2501.19393) and [competitive programming](https://arxiv.org/abs/2502.14382). However, in agentic environments, existing TTS methods often discard the exploration trajectory and treat the final answer as the only useful outcome. This overlooked exploration is actually a rich data source that could accelerate an agent's ability to learn from experience over time.

We bridge this gap by explicitly linking memory with scaling through memory-aware test-time scaling (MaTTS). By using ReasoningBank as a powerful experience learner, MaTTS distills extensive exploration into high-quality memories via contrastive and refinement signals. We demonstrate the power of MaTTS functions through two distinct forms of scaling:

*   _Parallel scaling_: The agent generates multiple distinct trajectories for the same query under the guidance of memory. Through self-contrast, ReasoningBank compares successful and spuriously reasoned trajectories to distill more robust strategies and synthesize higher-quality memories.
*   _Sequential scaling_: The agent iteratively refines reasoning within a single trajectory to produce strong intermediate rationale. ReasoningBank captures these intermediate insights on the agent's trial-and-errors and progressive improvement as high-quality memory items.

MaTTS establishes a strong synergy: high-quality memory from ReasoningBank steers the scaled exploration towards more promising strategies, and in return, the scaled interactions generate significantly richer learning signals that feed back into an even smarter ReasoningBank to help the agent.

## Performance & emergent capabilities

We evaluated ReasoningBank across challenging benchmarks covering dynamic environments. Using the [ReAct](https://arxiv.org/abs/2210.03629) prompting strategy as the foundation for all agents, we compared ReasoningBank against three memory configurations: a memory-free baseline (Vanilla ReAct), [Synapse](https://arxiv.org/abs/2306.07863) (Trajectory Memory) and [AWM](https://arxiv.org/abs/2409.07429) (Workflow Memory). From our main evaluation results with [Gemini-2.5-Flash](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash) on [WebArena](https://arxiv.org/abs/2307.13854) and [SWE-Bench-Verified](https://openai.com/index/introducing-swe-bench-verified/), we have the following key observations:

*   _Superior success rates_: ReasoningBank without scaling outperformed memory-free agents by 8.3% on WebArena and 4.6% on SWE-Bench-Verified.
*   _Efficiency gains_: Because the agent actively accesses past decision rationales, it executes commands with vastly reduced aimless exploration. On SWE-Bench-Verified, ReasoningBank saved almost 3 total execution steps per task over memory-free baselines.
*   _MaTTS synergy_: When adding MaTTS (parallel scaling with a scaling factor k=5), success rates are further boosted. ReasoningBank w/ MaTTS improves over ReasoningBank by a 3% success rate increase and 0.4 fewer steps on WebArena.

Importantly, during evaluation, we observed the emergence of strategic maturity. In a web-browsing example, the agent's initial curated rules resembled simple procedural checklists (e.g., "Look for page links"). As the agent persisted through more problem sets, these memories were incorporated during execution. Building upon existing knowledge, the agent distilled new trajectories into more advanced memories. Over time, simple checklists evolved into memories with compositional, preventative logic structures (e.g., "Cross-reference tasks continuously with active page filters to ensure retrieved datasets aren't paginated prematurely"). See the [paper](https://arxiv.org/abs/2509.25140) for more details.

## Conclusion

ReasoningBank provides a powerful framework for enabling LLMs to learn from experiences and evolve into continuous learners during test-time. We believe memory-driven experience scaling represents a crucial new frontier for agent scaling.

We are excited to share this with the broader research community.

## Acknowledgements

_This research was conducted by Siru Ouyang, Jun Yan, I-Hung Hsu, Yanfei Chen, Ke Jiang, Zifeng Wang, Rujun Han, Long T. Le, Samira Daruki, Xiangru Tang, Vishy Tirumalashetty, George Lee, Mahsan Rofouei, Hangfei Lin, Jiawei Han, Chen-Yu Lee, and Tomas Pfister._
