# Frontier Reading Queue

Prioritized queue for deeper reading. Source notes and raw artifacts are already present for this first tranche.

## Priority 0: Process Anchors

- [[sources/llm-wiki - Karpathy]]
- [[sources/Rich Sutton The Bitter Lesson]]

## Priority 1: Deep Reading

- [[sources/Agent Memory Characterization]]
- [[sources/Harness-1]]
- [[sources/Self-Harness]]
- [[sources/HarnessFix]]
- [[sources/Adaptive Auto-Harness]]
- [[sources/Recursive Agent Harnesses]]
- [[sources/Why Do Multi-Agent LLM Systems Fail]]
- [[sources/Multi-Agent Design - MASS]]
- [[sources/Anthropic Multi-Agent Research System]]
- [[sources/A2ASecBench]]
- [[sources/SAND]]
- [[sources/VeriMAP]]
- [[sources/AgentFlow]]
- [[sources/Anthropic Managed Agents]]
- [[sources/OpenHands]]
- [[sources/TheAgentCompany]]
- [[sources/MLR-Bench]]
- [[sources/OpenAI Codex Agent Loop]]
- [[sources/Cloudflare Project Think]]

## Priority 2: July 2026 Follow-Up

These are the strongest uncatalogued leads from the GPT-5.6/Fable/J-space sweep. Promote them only after a full-text read and claim-level verification.

- Better Harnesses, Smaller Models: Harness Design Dominates Model Scale in Agentic Coding — tests whether harness quality can outweigh model scale on software tasks. https://arxiv.org/abs/2607.08938
- Remember When It Matters: Memory Control for Long-Horizon Agents — studies when agents should retain, retrieve, or discard working state. https://arxiv.org/abs/2607.08716
- Scoped Verification (GRACE) — proposes verification whose scope tracks the agent's actual change set rather than a broad task-level verdict. https://arxiv.org/abs/2607.09175
- Long-Horizon-Terminal-Bench — extends terminal-agent evaluation toward longer, stateful task trajectories. https://arxiv.org/abs/2607.08964
- Agentic coding and persistent returns to expertise (Anthropic) — examines how human domain expertise continues to matter when coding agents do more of the execution. https://www.anthropic.com/research/claude-code-expertise
- GRAM / off-switch dual-use research (Anthropic) — studies capability-control trade-offs around stopping or redirecting agents. https://www.anthropic.com/research/off-switch-dual-use
- Test-Time Harness Evolution — treats the runtime scaffold itself as an object of test-time adaptation. https://arxiv.org/abs/2607.08124
- AgentLens — analyzes agent behavior through trajectory-level representations and diagnostics. https://arxiv.org/abs/2607.06624
- STRACE — develops structured tracing for diagnosing long agent trajectories. https://arxiv.org/abs/2607.07702

## Priority 3: June 2026 Follow-Up

- [[sources/SWE-MeM]]
- [[sources/TokenPilot]]
- [[sources/Memory Poisoning Attacks in LLM Agents]]
- [[sources/Do More Agents Help]]
- [[sources/MAS-Lab]]
- [[sources/Metis]]
- [[sources/Red Queen Godel Machine]]
- [[sources/GitHub Agentic Workflows]]
- [[sources/Google Agentic Resource Discovery]]

## Priority 4: Verification Backlog

Unverified leads are kept outside the public graph until they have enough source evidence to become source notes.

## Priority 5: Verified External Leads (2026-07-03 research sweep)

~180 URL-verified leads, no source cards yet. Plain URLs by design; promote to `sources/` cards on deep read.

**Harness design, context engineering, and steering**

- Context Compaction Deep Dive: Codex CLI, Claude Code, and OpenCode (Daniel Vaughan, Apr 2026) — only side-by-side comparison of compaction triggers, headroom formulas, and recovery budgets across the major coding CLIs. https://codex.danielvaughan.com/2026/04/14/context-compaction-deep-dive-codex-cli-claude-code-opencode/
- Context Engineering in Manus (Lance Martin/LangChain, Oct 2025) — records how the Manus harness evolved post-production: compaction-vs-summarization split, layered action space. https://rlancemartin.github.io/2025/10/15/manus/
- Context editing: clear_tool_uses and clear_thinking (Anthropic docs, Oct 2025) — vendor-quantified thresholds for when removing context is worth breaking the cache. https://platform.claude.com/docs/en/build-with-claude/context-editing
- Explore the context window (Claude Code docs, Jul 2026) — concrete in-turn window-allocation breakdown and compaction-survival rules for a flagship harness. https://code.claude.com/docs/en/context-window
- How Claude Code Builds a System Prompt (Drew Breunig, Apr 2026) — practitioner dissection of a real harness's prefix assembly order and cache boundaries. https://www.dbreunig.com/2026/04/04/how-claude-code-builds-a-system-prompt.html
- How Long Contexts Fail (Drew Breunig, Jun 2025) — the context poisoning/rot failure-mode taxonomy that justifies token budgets and compaction thresholds. https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html
- How to Fix Your Context (Drew Breunig, Jun 2025) — companion tactics taxonomy mapping one-to-one onto harness levers: masking, quarantine, pruning, offloading. https://www.dbreunig.com/2025/06/26/how-to-fix-your-context.html
- Background mode (OpenAI docs, May 2025) — cursor-based resumable streaming and advisory idempotent cancellation for background agent work. https://developers.openai.com/api/docs/guides/background
- Cancellation & Abort Propagation: Claude Code vs. Hermes Agent (Ken Huang, May 2026) — only source dissecting what happens to in-flight tool calls and subprocesses on user interrupt. https://kenhuangus.substack.com/p/chapter-2-cancellation-and-abort

**Durable execution and fault tolerance**

- Why Checkpoints Aren't Durable Execution (Diagrid, Feb 2026) — names the failure modes (duplicate side effects, silent death, mid-iteration resume) separating "has a checkpointer" from "survives unattended". https://www.diagrid.io/blog/checkpoints-are-not-durable-execution-why-langgraph-crewai-google-adk-and-others-fall-short-for-production-agent-workflows
- Temporal Replay 2026 announcements (Temporal, May 2026) — durable streaming, sandbox integration, and multi-SDK coverage mark durable execution becoming the default agent substrate. https://temporal.io/blog/replay-2026-product-announcements
- Durable Execution for Building Crashproof AI Agents (DBOS, Feb 2025) — library-embedded single-Postgres-transaction approach, a third architecture vs Temporal's server and Restate's middleware. https://www.dbos.dev/blog/durable-execution-crashproof-ai-agents
- Durable execution (LangGraph docs, Jul 2026) — the exit/async/sync durability-mode tradeoff every graph-based harness must decide. https://docs.langchain.com/oss/python/langgraph/durable-execution
- Error codes (OpenAI docs, Jul 2026) — provider error taxonomy that matters for harnesses using Responses-API state as their resume mechanism. https://developers.openai.com/api/docs/guides/error-codes

**Shared-state coordination and task queues**

- The Hearsay-II Speech-Understanding System (Erman et al., ACM Computing Surveys, 1980) — origin evidence for opportunistic, event-triggered coordination over shared state. https://mas.cs.umass.edu/Documents/Erman_Hearsay80.pdf
- Designing Data-Intensive Applications, 2nd Edition (Kleppmann & Riccomini, Mar 2026) — foundational consistency/ordering vocabulary (linearizability, consensus) for blackboard and task-queue design. https://martin.kleppmann.com/2026/03/24/designing-data-intensive-applications-2e.html
- LLM Multi-Agent Systems Based on Blackboard Architecture (Han & Zhang, Jul 2025) — corroborates that shared-state selection loops beat fixed message-passing topologies on unstructured problems. https://arxiv.org/abs/2507.01701
- Maxim Fateev on durable execution for AI agents (WorkOS, Apr 2026) — connects delivery-semantics theory to the production task-queue substrate code factories run on. https://workos.com/blog/maxim-fateev-temporal-durable-execution-ai-agents
- Multi-Agent Memory from a Computer Architecture Perspective (UC San Diego, Mar 2026) — named taxonomy for visibility/ordering/coherence in shared agent workspaces. https://arxiv.org/abs/2603.10062

**Multi-agent debate, scaling laws, and shared memory**

- Not All Flips Are Conformity (arXiv, May 2026) — measured causal decomposition of when debate converges vs entrenches, with an intervention result. https://arxiv.org/abs/2606.00820
- Peacemaker or Troublemaker: How Sycophancy Shapes Multi-Agent Debate (UW-Madison/Amazon, Sep 2025) — the judge side of silent agreement: judges echo rather than adjudicate. https://arxiv.org/abs/2509.23055
- Talk Isn't Always Cheap: Failure Modes in Multi-Agent Debate (JHU/Vector, Sep 2025) — sharpest negative result: strong majorities corrupted by weak minorities. https://arxiv.org/abs/2509.05396
- Are More LLM Calls All You Need? (Stanford/Berkeley et al., Mar 2024) — earliest analytical scaling law for call-count vs performance in compound systems. https://arxiv.org/abs/2403.02419
- The Ringelmann Effect in Multi-Agent LLM Systems (arXiv, May 2026) — cheap predictive law for effective team size; heterogeneity escapes the ceiling. https://arxiv.org/abs/2606.02646
- Collaborative Memory: Multi-User Memory Sharing with Dynamic Access Control (arXiv, May 2025) — formal auditable write-authority model: bipartite permission graphs plus provenance. https://arxiv.org/abs/2505.18279
- MIRIX: Multi-Agent Memory System (MIRIX AI, Jul 2025) — the multi-agent-as-memory-manager pattern with per-type write authority. https://arxiv.org/abs/2507.07957
- Multi-Agent Transactive Memory (arXiv, Jun 2026) — lesson propagation across an agent population via trajectory reuse; its missing quality gating is itself a datapoint. https://arxiv.org/abs/2606.19911
- Multi-agent shared memory blocks (Letta docs, Jul 2026) — most explicit published concurrency semantics for cross-agent memory: append-safe vs last-writer-wins. https://docs.letta.com/guides/agents/multi-agent-shared-memory

**Memory substrates, benchmarks, and long-context limits**

- Control-Plane Placement Shapes Forgetting (arXiv, Jun 2026) — architecture-vs-forgetting study across thirteen configurations plus the ForgetEval benchmark. https://arxiv.org/abs/2606.15903
- From RAG to Memory (HippoRAG 2) (ICML 2025) — crispest statement of the graph-vs-vector factual/associative trade-off. https://arxiv.org/abs/2502.14802
- LazyGraphRAG (Microsoft Research, Nov 2024) — GraphRAG's own successor showing eager graph indexing is often not worth its cost. https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/
- MemBench (Renmin/Huawei, ACL 2025 Findings) — agent-centric rather than chat-centric memory benchmark with reflective-memory scenarios. https://arxiv.org/abs/2506.21605
- State of AI Agent Memory 2026 (Mem0, Jul 2026) — freshest single table tying LoCoMo/LongMemEval/BEAM scores together; vendor-published caveat. https://mem0.ai/blog/state-of-ai-agent-memory-2026
- Classifier Context Rot (Martin & Roger, May 2026) — context rot afflicts the monitors and judges harnesses rely on, not just the workers. https://arxiv.org/abs/2605.12366
- MemoryBank (Sun Yat-sen, AAAI 2024) — lineage source for principled time-based decay/forgetting policies in agent memory. https://arxiv.org/abs/2305.10250
- NoLiMa: Long-Context Evaluation Beyond Literal Matching (LMU/Adobe, ICML 2025) — completes the degradation triad with associative-retrieval failure; advertised windows overstate effective context. https://arxiv.org/abs/2502.05167
- Rethinking Memory Mechanisms of Foundation Agents (arXiv survey, Feb 2026) — newest comprehensive map connecting the CoALA-era taxonomy to 2026 practice. https://arxiv.org/abs/2602.06052

**Methodology lineage**

- STaR: Bootstrapping Reasoning With Reasoning (NeurIPS 2022) — oldest node in the self-improvement lineage: bootstrap from verified successes. https://arxiv.org/abs/2203.14465
- Self-Refine: Iterative Refinement with Self-Feedback (NeurIPS 2023) — iterative refinement plateaus without external signal, complementing Reflexion. https://arxiv.org/abs/2303.17651
- From Question Answering to Task Completion: Survey on Agent System and Harness Design (arXiv, Jun 2026) — academic taxonomy (six responsibilities, four paradigms) framing the lineage papers. https://arxiv.org/abs/2606.20683
- Inside the Scaffold: A Source-Code Taxonomy of Coding Agent Architectures (arXiv, Apr 2026) — shows ReAct et al. are now composable building blocks inside real harnesses. https://arxiv.org/abs/2604.03515

**Selection policies, agentic RL, and self-improving loops**

- MAP-Elites: Illuminating search spaces by mapping elites (Mouret & Clune, 2015) — the quality-diversity selection mechanism DGM and AlphaEvolve inherit. https://arxiv.org/abs/1504.04909
- OpenEvolve (GitHub, May 2025) — runnable open-source AlphaEvolve counterpart where every selection knob is inspectable. https://github.com/codelion/openevolve
- PACE: Anytime-Valid Acceptance Tests for Self-Evolving Agents (arXiv, Jun 2026) — quantifies how noisy the accept-or-reject decision in every self-improving loop is. https://arxiv.org/abs/2606.08106
- DeepSeek-R1 (DeepSeek-AI, Jan 2025) — canonical RLVR/GRPO citation for the weights side of the weights-vs-harness boundary. https://arxiv.org/abs/2501.12948
- Kimi K2: Open Agentic Intelligence (Moonshot AI, Jul 2025) — most detailed open account of a frontier agentic-coding RL recipe. https://arxiv.org/abs/2507.20534
- SWE-Gym: Training SE Agents and Verifiers (Berkeley et al., ICML 2025) — canonical executable-training-environment plus learned-verifier recipe. https://arxiv.org/abs/2412.21139
- Continual Harness: Online Adaptation for Self-Improving Foundation Agents (Princeton/Google, May 2026) — the online, no-reset quadrant missing from offline harness-optimization work. https://arxiv.org/abs/2605.09998
- Demystifying RL for Long-Horizon Tool-Using Agents (CUHK/IDEA, Mar 2026) — numbers-heavy agentic-RL recipe for the training side the vault barely covers. https://arxiv.org/abs/2603.21972
- Beyond pass@1: Reliability Science for Long-Horizon Agents (arXiv, Mar 2026) — reliability vocabulary beyond pass@k; its memory-scaffolding-hurts finding counters several memory cards. https://arxiv.org/abs/2603.29231
- FALAT: Tracing Failures in LLM Agent Trajectories (Concordia, May 2026) — automated failure attribution, the diagnosis step a self-healing factory needs before auto-repair. https://arxiv.org/abs/2606.00765
- TrajAD: Trajectory Anomaly Detection (arXiv, Feb 2026) — runtime detect-localize-rollback mechanism; trained verifiers beat frontier zero-shot monitors. https://arxiv.org/abs/2602.06443

**Reward hacking and evaluator gaming**

- Inoculation Prompting (Anthropic Alignment, Oct 2025) — training-time defense that breaks the reward-hacking-to-sabotage generalization. https://alignment.anthropic.com/2025/inoculation-prompting/
- Monitoring Monitorability (OpenAI, Dec 2025) — turns "monitor the CoT" into a measured, regression-testable property with deployable design knobs. https://arxiv.org/abs/2512.18311
- SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents (Weco AI, May 2026) — quantified holdout-canary gap metric and a scaling law tying hacking to task horizon. https://arxiv.org/abs/2605.21384

**Coding-agent and computer-use benchmarks**

- GAIA (Meta/Hugging Face, Nov 2023) — lineage anchor for general-assistant evaluation that carded systems report scores on. https://arxiv.org/abs/2311.12983
- ARE: Scaling Up Agent Environments (Gaia2) (Meta Superintelligence Labs, Sep 2025) — only major benchmark scoring agent-to-agent collaboration and time pressure. https://arxiv.org/abs/2509.17158
- HCAST: Human-Calibrated Autonomy Software Tasks (METR, Mar 2025) — the human-baseline task suite under the time-horizon trend line. https://arxiv.org/abs/2503.17354
- MLE-bench (OpenAI, Oct 2024) — measures whether agents can do ML engineering itself, the recursive capability a self-improving factory depends on. https://arxiv.org/abs/2410.07095
- OSWorld (XLANG/Salesforce/Stanford, NeurIPS 2024) — the standard execution-verified computer-use benchmark. https://arxiv.org/abs/2404.07972
- OSWorld 2.0 (XLANG Lab, Jun 2026) — resets the computer-use trend line from 83.5% to ~20% and names the long-horizon failure modes. https://arxiv.org/abs/2606.29537
- SWE-Lancer (OpenAI, Feb 2025) — only benchmark pricing coding-agent capability in real market dollars. https://arxiv.org/abs/2502.12115
- SWE-rebench (Nebius, May 2025) — continuous fresh-task supply as the structural answer to contamination. https://arxiv.org/abs/2505.20411
- WebArena (CMU, ICLR 2024) — canonical self-hosted-replica web environment later benchmarks inherit; mostly lineage value now. https://arxiv.org/abs/2307.13854
- tau2-bench (Sierra, Jun 2025) — dual-control design for testing agents that must coordinate with another acting party. https://arxiv.org/abs/2506.07982

**Benchmark validity and judge reliability**

- Automated Benchmark Auditing for AI Agents (Duke/Stanford/Together, May 2026) — repeatable audit pipeline with fresh error rates on SWE-bench Verified and Terminal-Bench 2. https://arxiv.org/abs/2605.26079
- Search-Time Contamination in Deep Research Agents (arXiv, Jun 2026) — contamination that happens at inference time through the agent's own tools. https://arxiv.org/abs/2606.05241
- The Leaderboard Illusion (Cohere Labs et al., Apr 2025) — named leaderboard failure modes: selective disclosure, sampling bias, data asymmetry. https://arxiv.org/abs/2504.20879
- A Survey on LLM-as-a-Judge (arXiv, Nov 2024) — single reference map of the judge-reliability literature. https://arxiv.org/abs/2411.15594
- HealthBench (OpenAI, May 2025) — reference design for per-example expert rubrics with meta-validated model graders. https://arxiv.org/abs/2505.08775
- Towards a Science of AI Agent Reliability (Princeton, ICML 2026) — 12-metric reliability framework beyond pass@k. https://arxiv.org/abs/2602.16666
- Who Validates the Validators? (UC Berkeley, UIST 2024) — criteria-drift evidence for why judges need a human-alignment loop around them. https://arxiv.org/abs/2404.12272

**Offline vs online evaluation**

- Your AI Product Needs Evals (Hamel Husain, Mar 2024) — the most-cited writeup of the unit-test to trace-review to A/B ladder platforms later productized. https://hamel.dev/blog/posts/evals/
- Langfuse Evaluation Core Concepts (docs, Jul 2026) — the open-source dataset-from-traces and online scoring loop. https://langfuse.com/docs/evaluation/core-concepts
- Statsig AI Evals Overview (docs, Jul 2026) — only source wiring eval verdicts directly into feature-gate/experiment infrastructure. https://docs.statsig.com/ai-evals/overview
- Trace grading (OpenAI docs, Jul 2026) — current traces-to-datasets promotion pattern on a third major platform. https://developers.openai.com/api/docs/guides/trace-grading

**Observability and tracing standards**

- Inside the LLM Call: GenAI Observability with OpenTelemetry (OTel blog, May 2026) — official explainer of agent span semantics and the opt-in content-capture model. https://opentelemetry.io/blog/2026/genai-observability/
- OpenInference (Arize AI, Dec 2023) — the second major convention spec; documents the standards split every platform bridges. https://github.com/Arize-ai/openinference
- OpenLLMetry (Traceloop, Sep 2023) — the instrumentation-SDK layer and historical source of the GenAI semconv. https://github.com/traceloop/openllmetry
- Datadog LLM Observability supports OTel GenAI conventions (Datadog, Dec 2025) — evidence the OTel GenAI standard crossed into major-vendor production. https://www.datadoghq.com/blog/llm-otel-semantic-convention/
- Langfuse for Agents (changelog, Nov 2025) — the leading open-source platform's answer to what of plans/tool calls/costs gets captured and visualized. https://langfuse.com/changelog/2025-11-05-langfuse-for-agents
- Braintrust tracing (docs, Jun 2026) — eval-first traces embedding grader reasoning, the feedback signal a self-improving factory consumes. https://www.braintrust.dev/docs/guides/traces
- AgentOps (GitHub, Aug 2025) — session-replay plus execution-graph angle, distinct from trace-first tools. https://github.com/AgentOps-AI/agentops

**Prompt-injection defenses**

- Spotlighting (Microsoft, Mar 2024) — canonical data-marking defense on the prompt-transformation rung of the defense ladder. https://arxiv.org/abs/2403.14720
- StruQ: Structured Queries (UC Berkeley, USENIX Security 2025) — names the secure-front-end channel-separation pattern; mostly superseded by SecAlign. https://arxiv.org/abs/2402.06363
- Meta SecAlign (Meta FAIR/Berkeley, Jul 2025) — open, inspectable model-layer defense baseline that scales to agentic workloads. https://arxiv.org/abs/2507.02735
- Lessons from Defending Gemini Against Indirect Prompt Injections (Google DeepMind, May 2025) — only account of a frontier lab operationalizing the full model-layer defense stack against adaptive attackers. https://arxiv.org/abs/2505.14534
- Mitigating prompt injections in browser use (Anthropic, Nov 2025) — RL-based model hardening plus runtime classifiers, with a concrete residual-risk number. https://www.anthropic.com/research/prompt-injection-defenses
- Agents Rule of Two (Meta AI, Oct 2025) — operationalizes the lethal trifecta as a deployable choose-2-of-3 policy gate per session. https://ai.meta.com/blog/practical-ai-agent-security/
- Progent: Privilege Control for AI Agents (Berkeley/UCSB, Apr 2025) — third leg of deterministic enforcement: LLM-generated policies with SMT-checked monotonic confinement. https://arxiv.org/abs/2504.11703
- AI Agents May Always Fall for Prompt Injections (Abdelnabi & Bagdasarian, May 2026) — strongest 2026 argument that IFC architectures shift rather than end the problem. https://arxiv.org/abs/2605.17634

**AI control and security incidents**

- Evaluating Control Protocols for Untrusted AI Agents (Anthropic/Redwood, Nov 2025) — newest full control-protocol evaluation with adversarially stronger red teams. https://arxiv.org/abs/2511.02997
- Attack Selection in Agentic AI Control Evaluations (arXiv, Jun 2026) — control-eval numbers are optimistic unless attack timing is modeled. https://arxiv.org/abs/2606.06529
- ControlArena (UK AISI + Redwood, Oct 2025) — operational tooling for running control evaluations in a code-factory pipeline. https://github.com/UKGovernmentBEIS/control-arena
- Indirect Prompt Injection in Perplexity Comet (Brave, Aug 2025) — canonical browser-agent exploit disclosure with a cross-origin exfil PoC. https://brave.com/blog/comet-prompt-injection/
- Piloting Claude for Chrome (Anthropic, Aug 2025) — quantifies which defenses actually move the needle: permissions plus classifiers cut attack success ~2x. https://claude.com/blog/claude-for-chrome
- Hardening ChatGPT Atlas against prompt injection (OpenAI, Dec 2025) — the RL-red-team plus rapid-retrain defense pattern, and the admission injection is unsolvable. https://openai.com/index/hardening-atlas-against-prompt-injection/
- ToxicSkills (Snyk, Feb 2026) — population-level supply-chain stats: 36.8% of agent skills flawed, 13.4% critical. https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/
- Replit agent deleted production database (The Register, Jul 2025) — canonical destructive-autonomy incident motivating dev/prod isolation and planning-only modes. https://www.theregister.com/2025/07/21/replit_saastr_vibe_coding_incident/

**Agent identity, auth, and secrets**

- Prompt Infection: LLM-to-LLM Injection in Multi-Agent Systems (arXiv, Oct 2024) — the threat model motivating the whole delegation-chain identity stack. https://arxiv.org/abs/2410.07283
- OAuth 2.0 On-Behalf-Of User Authorization for AI Agents (IETF draft, Aug 2025) — first widely cited "OAuth for agents" proposal; its expiry and non-adoption is itself the finding. https://datatracker.ietf.org/doc/draft-oauth-ai-agents-on-behalf-of-user/
- Cross App Access (XAA) walkthrough (Okta, Sep 2025) — the accessible mechanism explainer for the ID-JAG spec with real roles and code. https://developer.okta.com/blog/2025/09/03/cross-app-access
- WIMSE Architecture draft-07 (IETF WG, Mar 2026) — the workload-identity foundation the AIMS agent stack normatively depends on. https://datatracker.ietf.org/doc/draft-ietf-wimse-arch/
- AIP: Agent Identity Protocol (arXiv, Mar 2026) — cryptographic delegation-chain design targeting MCP/A2A gaps, with measured overhead numbers. https://arxiv.org/abs/2603.24775
- Web Bot Auth (Cloudflare docs, Jul 2026) — the header/key-directory mechanics for implementing or validating signed-agent traffic. https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/
- Secure AI identity with HashiCorp Vault (HashiCorp, Jul 2025) — short-lived scoped tokens per agent session, with real TTL numbers. https://www.hashicorp.com/en/blog/secure-ai-identity-with-hashicorp-vault
- Credential Brokering for AI Agents, Explained (Infisical, May 2026) — names credential brokering as a cross-vendor pattern beyond any single product. https://infisical.com/blog/credential-brokering-for-ai-agents
- 1Password Secure Agentic Autofill (1Password, Oct 2025) — human-approved, out-of-band credential injection for browser agents, a distinct mechanism class from proxies. https://www.1password.dev/agentic-autofill
- 1Password as trusted access layer for Codex (1Password, May 2026) — a frontier coding harness natively integrating "use secrets without seeing them". https://1password.com/blog/1password-trusted-access-layer-for-openai-codex
- MCP Authorization spec, 2025-11-25 revision (MCP, Nov 2025) — token-storage and short-lived-token guidance superseding the vault's pinned 2025-06-18 card. https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization
- Langfuse Masking (docs, Jul 2026) — the trace-redaction leg: observability pipelines capture full tool I/O even with brokered credentials. https://langfuse.com/docs/observability/features/masking

**Cost governance and gateways**

- AI coding assistant pricing and ROI guide 2026 (DX, Jun 2026) — closest published fleet-level per-task economics, with real spend-escalation datapoints. https://getdx.com/blog/ai-coding-assistant-pricing/
- FinOps for AI Overview (FinOps Foundation, Feb 2026) — the org-level governance framework agent spend controls plug into. https://www.finops.org/wg/finops-for-ai-overview/
- Linux Foundation Tokenomics Foundation announcement (LF, Jun 2026) — token metering/attribution becoming a standards problem (FOCUS extension). https://www.linuxfoundation.org/press/linux-foundation-announces-the-intent-to-launch-the-tokenomics-foundation-to-establish-open-standards-for-ai-cost-management
- OpenRouter Guardrails (docs, Jul 2026) — policy-as-guardrail combining budget, model, and data-retention controls. https://openrouter.ai/docs/guides/features/guardrails
- Portkey budget and rate limits (docs, Jul 2026) — representative gateway enforcement with a distinct alert-then-block model. https://portkey.ai/docs/product/administration/enforce-budget-and-rate-limit

**Autonomy gradation and human review gates**

- Devin Review docs (Cognition, Jun 2026) — a shipped product's concrete trust dial: confidence tiers, CI-gated auto-merge, spend limits, org allowlists. https://docs.devin.ai/work-with-devin/devin-review
- Five levels of AI coding agent autonomy (Swarmia, Mar 2026) — bridges the academic autonomy taxonomy to merge-policy and review-burden mechanics with production data points. https://www.swarmia.com/blog/five-levels-ai-agent-autonomy/
- Model AI Governance Framework for Agentic AI (IMDA Singapore, Jan 2026) — the regulatory reference point enterprise harness designers will be asked to comply with. https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/press-releases/2026/new-model-ai-governance-framework-for-agentic-ai
- Automation bias: a systematic review (JAMIA, 2012) — canonical quantitative anchor (26% erroneous-advice-following) behind every rubber-stamping claim. https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/
- AI Safety and Automation Bias (CSET, Nov 2024) — why gate design must combine technical and organizational fail-safes, not one approval click. https://cset.georgetown.edu/publication/ai-safety-and-automation-bias/
- AIDev: Studying AI Coding Agents on GitHub (Queen's/Huawei, Feb 2026) — nearly a million agent PRs in the wild, the denominator behind review-throughput claims. https://arxiv.org/abs/2602.09185
- Early-Stage Prediction of Review Effort in AI-Generated Pull Requests (arXiv, Jan 2026) — a measured sampling curve: 20% review budget catches 69% of high-effort PRs. https://arxiv.org/abs/2601.00753
- Human-AI Synergy in Agentic Code Review (Queen's, Mar 2026) — quantifies what AI reviewers are worth and what they cost (11.8% more review rounds). https://arxiv.org/abs/2603.15911
- More Code, Less Reuse (MSR 2026) — reviewer sentiment is friendlier toward agent PRs even as measured maintainability is worse. https://arxiv.org/abs/2601.21276

**Program repair, test generation, and release engineering**

- SapFix and Sapienz (Meta, Sep 2018) — production-repair lineage: fault localization, layered patches, and approval gates were solved pre-LLM. https://engineering.fb.com/2018/09/13/developer-tools/finding-and-fixing-software-bugs-automatically-with-sapfix-and-sapienz/
- Flaky Tests at Google (Google Testing Blog, May 2016) — canonical numbers for the quarantine/rerun/SLO pattern; flakiness is the failure mode of tests-as-backpressure. https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html
- Practical Mutation Testing at Scale (Google, 2021) — the reference design for a code factory's test-strength gauge. https://arxiv.org/abs/2102.11378
- RepairAgent (Stuttgart/UC Davis, ICSE 2025) — FSM-gated tool-use pattern bridging fixed-prompt APR and enterprise agents. https://arxiv.org/abs/2403.17134
- Amazon Q Developer $260M milestone (AWS, Aug 2024) — largest publicly claimed ROI number for autonomous code maintenance, methodology caveats included. https://aws.amazon.com/blogs/devops/amazon-q-developer-just-reached-a-260-million-dollar-milestone/
- Just-in-Time Catching Test Generation at Meta (arXiv, Jan 2026) — turns test generation into a pre-merge backpressure gate on every pull request. https://arxiv.org/abs/2601.22832
- Keeping Master Green at Scale (Uber SubmitQueue, EuroSys 2019) — foundational speculative merge-queue architecture agent-scale landing systems converge on. https://dl.acm.org/doi/10.1145/3302424.3303970
- CI at Scale: Lean, Green, and Fast (Uber, Jan 2025) — quantifies the cost side of speculative merge queues and the optimization levers as change volume rises. https://arxiv.org/abs/2501.03440
- SRE Book Ch. 8: Release Engineering (Google, 2016) — self-service, push-on-green, and hermetic builds as preconditions of any agent-scale pipeline. https://sre.google/sre-book/release-engineering/
- Argo Rollouts (CNCF, living docs) — reference open-source implementation of metric-gated progressive delivery and automated rollback. https://argo-rollouts.readthedocs.io/en/stable/
- LaunchDarkly Guarded Rollouts (docs, 2024–2026) — commercial state of the art for statistically-gated automatic rollback at the flag layer. https://launchdarkly.com/docs/home/releases/guarded-rollouts
- LaunchDarkly AgentControl (docs, May 2026) — extends progressive delivery to agent configuration itself: canarying and rollback for prompts and models. https://launchdarkly.com/docs/home/agentcontrol

**Signal intake, triage, and SRE agents**

- DeepTriage (IBM Research, 2018) — origin point of deep-learning bug triage and its standard benchmark datasets. https://arxiv.org/abs/1801.01275
- Teaching machines to triage Firefox bugs (BugBug) (Mozilla, Apr 2019) — the canonical pre-LLM deployed triage bot, with confidence-threshold gating and real time-to-action numbers. https://hacks.mozilla.org/2019/04/teaching-machines-to-triage-firefox-bugs/
- Duplicate Bug Report Detection: How Far Are We? (ACM TOSEM, Dec 2022) — production-deployed simple methods match fancy research models; benchmark hygiene dominates. https://arxiv.org/abs/2212.00548
- How we built Triage Intelligence (Linear, Sep 2025) — retrieval-then-reason dedup architecture and prose-configurable triage policy. https://linear.app/now/how-we-built-triage-intelligence
- The Agentics (GitHub Next, Jun 2026) — where the actual triage workflow implementations behind GitHub Agentic Workflows live. https://github.com/githubnext/agentics
- Meet the new Bits AI SRE (Datadog, Mar 2026) — most complete deployed alert-intake pipeline, plus the bits.md config pattern crossing over from coding harnesses. https://www.datadoghq.com/blog/bits-ai-sre-deeper-reasoning/
- Introducing Bits AI SRE (Datadog, Dec 2025) — clearest published hypothesis-validate-classify SRE-agent reasoning architecture from an observability vendor. https://www.datadoghq.com/blog/bits-ai-sre/
- Azure SRE Agent GA (Microsoft, Apr 2026) — Microsoft operating its own cloud with 1,300+ SRE agents, the largest disclosed ops-agent deployment. https://techcommunity.microsoft.com/blog/appsonazureblog/announcing-general-availability-for-the-azure-sre-agent/4500682
- Building AI Agents for Autonomous Clouds (Microsoft Research, Jul 2024) — design rationale for agent-cloud interfaces and chaos-based evaluation. https://arxiv.org/abs/2407.12165
- DrP: Meta's root cause analysis platform (Meta, Dec 2025) — only public numbers on auto-remediation scale (50k analyses/day) and findings-to-PR automation. https://engineering.fb.com/2025/12/19/data-infrastructure/drp-metas-root-cause-analysis-platform-at-scale/
- How it feels to run an incident with AI SRE (incident.io, Apr 2026) — best public demonstration of the incident-to-PR loop closing through MCP between an SRE agent and a coding agent. https://incident.io/blog/how-it-feels-to-run-an-incident-with-ai-sre
- PagerDuty SRE Agent (PagerDuty, Mar 2026) — the incumbent paging vendor's agent architecture and the cross-vendor agent-integration pattern. https://www.pagerduty.com/blog/ai/meet-your-virtual-responder-pagerdutys-sre-agent-for-ai-driven-reliability/

**Kubernetes and self-hosted deployment**

- Agent substrate on Kubernetes with kagent (Solo.io, Jun 2026) — concrete snapshot/resume timings, microVM isolation, and egress-gateway credential injection numbers. https://www.solo.io/blog/agent-substrate-powers-kubernetes-agents-with-kagent
- CNCF TOC Initiative: Cloud-Native Foundations for Distributed Agentic Systems (CNCF, Jun 2025) — tracks where CNCF-level agent standardization (Agent CRD, MCP-for-Clusters) is heading. https://github.com/cncf/toc/issues/1746
- Dapr Agents (CNCF/Diagrid docs, Jun 2026) — the actor/workflow durable-execution topology, distinct from kagent's CRD-per-agent model. https://docs.dapr.io/developing-ai/dapr-agents/
- Kgateway v2.1 with agentgateway (CNCF, Nov 2025) — the Gateway API control plane plus agent-native data plane topology enterprises actually deploy. https://www.cncf.io/blog/2025/11/18/kgateway-v2-1-is-released/
- Agent Gateway overhaul: A2A, MCP, and Gateway API (Solo.io, Jul 2025) — spec-version-level detail on protocol-aware routing. https://www.solo.io/blog/updated-a2a-and-mcp-gateway
- Why cloud native belongs at the heart of agentic AI (Orange Innovation via CNCF, Jun 2026) — the only end-user enterprise account: regulated-industry deployment with policy in OPA, not prompts. https://www.cncf.io/blog/2026/06/17/why-cloud-native-belongs-at-the-heart-of-agentic-ai-lessons-from-building-a-multi-agent-security-platform-on-kubernetes/

**Frontier systems and vendor developments**

- Google announces Gemini CLI (Google, Jun 2025) — canonical launch reference for a CLI harness the vault cites but cannot substantiate. https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/
- Jules out of public beta (Google Labs, Aug 2025) — GA anchor for Google's async coding agent. https://blog.google/technology/google-labs/jules-now-available/
- Jules tools and API (Google Labs, Oct 2025) — the web agent becoming a programmable CI/CD component: agent-as-API. https://blog.google/technology/google-labs/jules-tools-jules-api/
- Google I/O 2026 developer keynote roundup (Google, May 2026) — single source for Google's whole 2026 agent stack: Antigravity 2.0, managed agents, WebMCP, Jules absorption. https://developers.googleblog.com/all-the-news-from-the-google-io-2026-developer-keynote/
- GitHub Copilot app (GitHub, Jun 2026) — worktree-isolated parallel sessions and desktop mission control, successor to Agent HQ. https://github.blog/news-insights/product-news/github-copilot-app-the-agent-native-desktop-experience/
- Cognition's acquisition of Windsurf (Cognition, Jul 2025) — grounds the agent-plus-IDE consolidation trend. https://cognition.com/blog/windsurf
- Droid: #1 on Terminal-Bench (Factory, Sep 2025) — the cross-model harness-dominates-model result. https://factory.ai/news/terminal-bench
- Droid Exec headless overview (Factory docs, Sep 2025) — scripting a coding agent inside CI, with named autonomy tiers and orchestrator/worker/validator mission mode. https://docs.factory.ai/cli/droid-exec/overview
- Introducing Wide Research (Manus, Jul 2025) — the homogeneous-swarm counterpoint to role-based orchestration. https://manus.im/blog/introducing-wide-research
- Amazon Q Developer end-of-support (AWS, Apr 2026) — a hyperscaler retiring its assistant for Kiro's spec-driven agent factory (specs/hooks/steering/subagents). https://aws.amazon.com/blogs/devops/amazon-q-developer-end-of-support-announcement/
- Cursor 3.8 Automations improvements (Cursor, Jun 2026) — clearest vendor implementation of self-healing code-factory loops: CI-failure triage, review auto-fix. https://cursor.com/changelog/06-18-26

**Protocols and ecosystem governance**

- A2A v1.0 release notes (Linux Foundation, Mar 2026) — what changed and why in the protocol's governance-era release, including IBM's post-merge seat. https://a2a-protocol.org/latest/whats-new-v1/
- A2A surpasses 150 organizations (Linux Foundation, Apr 2026) — the most concrete production-adoption datapoints for A2A post-v1.0. https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year
- What happened to Google's A2A? (Fatih Kadir Akın, Sep 2025) — the credible critical counterweight to LF/vendor adoption narratives. https://blog.fka.dev/blog/2025-09-11-what-happened-to-googles-a2a/
- MCP Apps (SEP-1865) (MCP blog, Nov 2025) — a new interactive-UI surface and a rare Anthropic-OpenAI co-authored standardization event. https://blog.modelcontextprotocol.io/posts/2025-11-21-mcp-apps/
- AGENTS.md (Agentic AI Foundation, Aug 2025) — the cross-vendor substrate for repo-level agent instructions; referenced across the vault with no dedicated card. https://agents.md/
- Launching the x402 Foundation (Cloudflare/Coinbase, Sep 2025) — the HTTP-native payments-protocol contender with the most 2026 institutional backing. https://blog.cloudflare.com/x402/

**Systems catalog long tail**

- The Contract Net Protocol (Reid G. Smith, IEEE ToC, 1980) — 45-year-old origin of the delegation, bidding, and task-routing patterns behind A2A-style coordination. https://www.reidgsmith.com/The_Contract_Net_Protocol_Dec-1980.pdf
- When "A Helpful Assistant" Is Not Really Helpful (EMNLP 2024 Findings) — controlled evidence that personas in system prompts do not improve performance. https://arxiv.org/abs/2311.10054
- UI-TARS-2 Technical Report (ByteDance Seed, Sep 2025) — strongest public account of a GUI-agent RL data flywheel and sandbox rollout platform. https://arxiv.org/abs/2509.02544
- Agentic Commerce Protocol (Stripe/OpenAI, Sep 2025) — the OpenAI/Stripe side of the agentic-payments protocol landscape, complementing AP2/UCP. https://stripe.com/blog/developing-an-open-standard-for-agentic-commerce
- Introducing x402 V2 (Coinbase, Dec 2025) — the machine-to-machine micropayment rail agents actually transact on today. https://www.x402.org/writing/x402-v2-launch
