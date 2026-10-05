---
title: Agent Capability Research Lineage
aliases:
  - Research Before Agent Services
created: 2026-10-05
updated: 2026-10-05
---

# Agent Capability Research Lineage

Start here to understand agent capabilities through research questions and experiments before comparing their service implementations. This October 5, 2026 update combines earlier missing foundations with research since the vault's September 15–17 refresh.

Dates establish precedence, not provenance. A paper can test a related mechanism without having invented every version of it or directly influencing a later product. A research blog can explain an experiment without supplying independent corroboration. Source cards preserve those distinctions.

## From Research Question to Operating Concept

| Question | Read the concept | Earlier research | What remains to establish |
|---|---|---|---|
| How should observation change the next action? | [[concepts/agent loop]] | [[sources/ReAct]] (2022); [[sources/Cognitive Architectures for Language Agents]] (2023) | Recovery, pending work, and completion contracts beyond the basic decision cycle |
| How can an agent find tools it was not shown? | [[concepts/dynamic tool discovery]] | [[sources/Gorilla]] (2023); [[sources/AnyTool]] (2024); [[sources/MCP-Zero]] (2025) | Retrieval quality, schema freshness, discoverability of new tools, and permission at execution |
| Which tool work belongs in code or a scheduler? | [[concepts/programmatic tool calling]] | [[sources/LLMCompiler]] (2023); [[sources/CodeAct]] (2024) | Dependency correctness, semantic judgment, and safe effects alongside latency savings |
| When is another model worth consulting? | [[concepts/advisor agents]]; [[methods/runtime routing]] | [[sources/FrugalGPT]] (2023); [[sources/RouteLLM]] (2024); [[sources/Think Big Search Small]] (2026) | Whole-task benefit from advice, distinct from selecting a model or replacing an answer |
| When should an agent wake or offer help? | [[concepts/background agents]]; [[concepts/event-driven agents]] | [[sources/Hearsay-II]] (1980); [[sources/Proactive Agent]] (2024); [[sources/ProAgentBench]] (2026) | Useful intervention timing, missed needs, and interruption burden |
| Can idle computation help the next request? | [[concepts/dreaming and memory consolidation]] | [[sources/Generative Agents]] (2023); [[sources/Sleep-time Compute]] (2025) | Whether preparation is reused enough to justify its total cost |
| Who may reuse a remembered fact? | [[concepts/shared agent memory]] | [[sources/Collaborative Memory]] (2025) | Revocation, derived memories, and access enforcement across communication surfaces |
| How much should a retrieved memory influence action? | [[concepts/memory use calibration]] | [[sources/LongMemEval]]; [[sources/MemOps]]; [[sources/MemCalib]] (2026) | Influence, freshness, and authority measured separately |
| What exactly improves when an agent learns? | [[concepts/harness-aware agent learning]] | [[sources/Reflexion]]; [[sources/Voyager]] (2023); [[sources/Darwin Godel Machine]] (2025) | Transfer and held-out improvement in memory, harness, or parameters |
| Does a browser agent generalize beyond its examples? | [[concepts/tool use]]; [[concepts/agent loop]] | [[sources/Mind2Web]] (2023) | Live task completion, recovery, and action consequences beyond offline prediction |

## New Research to Read Next

For personal assistants, [[concepts/persistent personal agents]] adds the earlier mixed-initiative, interruption, and delegation literature. [[systems/personal assistant agents]] compares current products against those questions. [[methods/agent runtime selection]] turns the runtime evidence into choices for builders using frameworks or their own loops.

1. [[sources/SCLATE]] — evaluate the agent's lifecycle, including session boundaries and scheduled memory work.
2. [[sources/Agent Lightning v1.0]] — train through the actual harness rather than replacing it with a simplified training loop.
3. [[sources/AIDE2 Recursive Self-Improvement]] — examine measured harness self-modification and the separate, unresolved test of better recursive self-improvement.
4. [[sources/MemCalib]] — evaluate memory influence after retrieval.
5. [[sources/Agent Evaluation Reliability]] — decide whether a comparison ranks complete systems or underlying models.
6. [[sources/Does Learning to Predict the World Help Agents Act]] — ablate the proposed mechanism, not just the whole package, when assessing world-model training.

These extend existing research rather than establishing one universal architecture. See [[maps/Self-Improving Systems Map]] and [[maps/Evaluation Map]] for the surrounding evidence.

## Research Blogs Worth Following Back to the Experiment

- [[sources/Lilian Weng LLM Powered Autonomous Agents]] is an early synthesis and reference trail. Follow its citations for experimental claims.
- [[sources/Sleep-time Compute]] links the Letta/UC Berkeley paper, reproducible experiment code, and the authors' implementation blog. The lab and product accounts are one evidence family.
- [[sources/Manus Context Engineering]] records production design choices and failure experience. It is useful engineering evidence, with no controlled attribution for every recommendation.
- [[sources/Cloudflare Code Mode MCP]] and [[sources/Cloudflare Code Mode MCP API]] explain implemented tool-interface changes; compare their engineering claims with CodeAct and LLMCompiler experiments.
- [[sources/LangChain Harness Model Routing]] reports a production A/B test. Its proxy outcomes and scope make a useful contrast with RouteLLM's benchmark experiments.

These sources include university groups, individual researchers, startups, and vendor engineering teams. Institutional independence, publication timing, open code, controlled evaluation, and replication are separate properties; none can substitute for the others.

## Compare the Service Contract After Understanding the Mechanism

| Capability boundary | Current implementation example | Evidence type |
|---|---|---|
| Tools can change between turns | [[sources/Claude Mid-Conversation Tool Definitions]] | September 22 beta API contract |
| Work can continue around pending results and input | [[sources/OpenAI Async Tools and Steering]] | September 3 API contract; an earlier synthesis gap |
| A side agent watches a running task | [[sources/Claude Code Mods and You Should Know]] | October 1 shipped feature, no established effectiveness result |
| Events wake persistent responsibilities | [[sources/OpenAI MCP Events]]; [[sources/OpenAI Dots]] | Living integration/product docs; exact initial release dates unverified |
| Memory follows caller and channel | [[sources/LangChain Identity-Scoped Agent Memory]] | September 24 implementation report |
| Browser execution joins a managed harness | [[sources/OpenAI Agents API Computer Use]] | September 29 API contract |

## How to Extend This Map

For a new capability, look backward through the method's references and forward through papers testing its failure modes. Prefer an executable artifact, ablation, matched-budget baseline, or deployment experiment over a launch claim. Record the workload, evaluator, negative results, and what the paper leaves unresolved. Keep untested proposals and living service contracts labeled as such.

## Related

- [[maps/Research Map]]
- [[maps/Harness Design Playbook]]
- [[maps/Recent Agent Operating Concepts]]
- [[maps/Frontier Reading Queue]]
