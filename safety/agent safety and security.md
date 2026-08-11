# Agent Safety and Security

Agent safety covers the risks created when models can act, use tools, access private data, persist memory, coordinate with other agents, or operate over long horizons.

## Major Risk Areas

- [[safety/prompt injection]]
- [[safety/protocol security]]
- [[safety/reward hacking]]
- [[safety/AI control]]
- [[safety/sandbox escape and credential exposure]]
- [[operations/agent memory]]
- [[safety/agentic misalignment risk]]
- [[methods/deliberative control]]
- [[operations/sandboxes]]

## Persistent Harness Carriers

Agent security is temporal as well as per-request. [[sources/HarnessSafe]] models a Persistent-Risk Lifecycle in which attacker-influenced content enters during one task, survives through memory, skills, MCP/tools, summaries, subagents, or shared artifacts, and is activated later by an otherwise benign request. Its 328 executable cases use trace-based stage scoring to show where a chain enters, persists, crosses a boundary, triggers, and finally causes a violation.

The main design lesson is that containment belongs to the model–harness configuration and to the entire carrier lifecycle. A scanner or prompt defense at ingestion is not sufficient if transformed content later crosses into a trusted summary, generated skill, delegated context, or shared artifact. Provenance, taint, expiry, re-validation at trust-boundary crossings, and stage-level traces must follow persistent state after the original session ends. The benchmark is a new preprint with mostly one run per configuration, so its per-harness ordering should not be treated as a stable product ranking.

Delegation creates a related non-adversarial failure: [[sources/MasDrift]] shows authorization constraints drifting as goals move through multi-agent architectures. Together the two results argue that persisted content and delegated authority need external provenance that survives model-written summaries and handoffs.

## Related Sources

- [[sources/AI Control Despite Intentional Subversion|AI Control: Improving Safety Despite Intentional Subversion]]
- [[sources/Agent Security Bench|Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents]]
- [[sources/AgentDojo|AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents]]
- [[sources/Agentic Misalignment|Agentic Misalignment: How LLMs Could be Insider Threats]]
- [[sources/Aligned Agents Biased Swarm|Aligned Agents, Biased Swarm: Measuring Bias Amplification in Multi-Agent Systems]]
- [[sources/Anthropic Disrupting AI Espionage|Disrupting the First Reported AI-Orchestrated Cyber Espionage Campaign]]
- [[sources/Anthropic Petri|Petri: An Open-Source Auditing Tool to Accelerate AI Safety Research]]
- [[sources/BrowseSafe|BrowseSafe: Understanding and Preventing Prompt Injection Within AI Browser Agents]]
- [[sources/Architecting Resilient LLM Agents|Architecting Resilient LLM Agents]]
- [[sources/HarnessSafe|HarnessSafe: Evaluating Safety Across Persistent Carriers in Agent Harnesses]]
- [[sources/CaMeL|Defeating Prompt Injections by Design (CaMeL)]]
- [[sources/Chain of Thought Monitorability|Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety]]
- [[sources/Check Point Claude Code Project Files RCE|RCE and API Token Exfiltration Through Claude Code Project Files]]
- [[sources/Constitutional Classifiers|Constitutional Classifiers: Defending against Universal Jailbreaks]]
- [[sources/Ctrl-Z Controlling AI Agents via Resampling|Ctrl-Z: Controlling AI Agents via Resampling]]
- [[sources/DeepMind Specification Gaming|Specification Gaming: The Flip Side of AI Ingenuity]]
- [[sources/EchoLeak|EchoLeak: The First Real-World Zero-Click Prompt Injection Exploit (CVE-2025-32711)]]
- [[sources/FIDES|Securing AI Agents with Information-Flow Control (FIDES)]]
- [[sources/ImpossibleBench|ImpossibleBench: Measuring LLMs' Propensity of Exploiting Test Cases]]
- [[sources/In-Context Scheming|Frontier Models are Capable of In-Context Scheming]]
- [[sources/Koi Security ClawHavoc|ClawHavoc: 341 Malicious ClawHub Skills]]
- [[sources/Koi Security Postmark MCP Backdoor|First Malicious MCP in the Wild: The Postmark Backdoor]]
- [[sources/LlamaFirewall|LlamaFirewall: An open source guardrail system for building secure AI agents]]
- [[sources/METR Frontier Risk Report 2026|Frontier Risk Report (February to March 2026)]]
- [[sources/METR Recent Reward Hacking|Recent Frontier Models Are Reward Hacking]]
- [[sources/MasDrift|MasDrift: Benchmarking Authorization Preservation Across Multi-Agent Architectures]]
- [[sources/Monitoring Reasoning Models for Misbehavior|Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation]]
- [[sources/OpenAI Deep Research System Card|Deep research System Card]]
- [[sources/PEAR|PEAR: Planner-Executor Agent Robustness Benchmark]]
- [[sources/Evaluation and Benchmarking of LLM Agents - A Survey|Evaluation and Benchmarking of LLM Agents: A Survey]]
- [[sources/OpenAI ChatGPT Agent System Card|ChatGPT agent System Card]]
- [[sources/MLR-Bench|MLR-Bench: Evaluating AI Agents on Open-Ended Machine Learning Research]]
- [[sources/Microsoft Taxonomy of Failure Modes in AI Agents|Taxonomy of Failure Modes in Agentic AI Systems]]
- [[sources/OpenAI Operator System Card|Operator System Card]]
- [[sources/Anthropic Safe and Trustworthy Agents Framework|Our framework for developing safe and trustworthy agents]]
- [[sources/Anthropic Shortcuts to Sabotage|From shortcuts to sabotage]]
- [[sources/Anthropic Teaching Claude Why|Teaching Claude why]]
- [[sources/Anthropic When AI Builds Itself|When AI builds itself]]
- [[sources/Sabotage Evaluations for Frontier Models|Sabotage Evaluations for Frontier Models]]
- [[sources/SecAlign|SecAlign: Defending Against Prompt Injection with Preference Optimization]]
- [[sources/SHADE-Arena|SHADE-Arena: Evaluating Sabotage and Monitoring in LLM Agents]]
- [[sources/Stress Testing Anti-Scheming Training|Stress Testing Deliberative Alignment for Anti-Scheming Training]]
- [[sources/TAMAS|TAMAS: Benchmarking Adversarial Risks in Multi-Agent LLM Systems]]
- [[sources/The Attacker Moves Second|The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses]]
- [[sources/The Instruction Hierarchy|The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions]]
- [[sources/Web Agents Plan-Then-Execute|Web Agents Should Adopt the Plan-Then-Execute Paradigm]]
- [[sources/Willison Dual LLM Pattern|The Dual LLM Pattern for Building AI Assistants That Can Resist Prompt Injection]]
- [[sources/Willison Lethal Trifecta|The Lethal Trifecta for AI Agents]]
- [[sources/The 2025 AI Agent Index|The 2025 AI Agent Index: Documenting Technical and Safety Features of Deployed Agentic AI Systems]]
