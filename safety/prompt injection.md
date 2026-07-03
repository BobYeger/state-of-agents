# Prompt Injection

Prompt injection attacks manipulate an agent through untrusted content in tool outputs, web pages, documents, messages, or shared memory. The agent cannot distinguish instructions it should follow from instructions embedded in data it should merely process, so any content channel becomes a potential command channel.

## Threat Model

[[sources/Willison Lethal Trifecta]] gives the working test: an agent with access to private data, exposure to untrusted content, and an external communication channel is exfiltration-vulnerable regardless of model quality. The pattern is no longer hypothetical. [[sources/EchoLeak]] documents a zero-click exfiltration from Microsoft 365 Copilot (CVE-2025-32711, CVSS 9.3): one crafted email caused Copilot to read in-scope organizational data and leak it through auto-fetched images, bypassing Microsoft's injection classifier on the way. [[sources/Invariant Labs MCP Tool Poisoning]] shows the injection can live in tool metadata rather than content — instructions in an MCP tool description invisible to the user but trusted by the model — and [[sources/Check Point Claude Code Project Files RCE]] shows repository-provided configuration executing on project open, making "clone and open" an injection vector into the harness itself.

## Defense Layers

No single layer holds. [[sources/The Attacker Moves Second]] attacked twelve published defenses — prompting-based, training-based, and classifier-based — with adaptive, defense-aware attackers and exceeded 90% attack success against most of them; human red-teamers reached 100%. The design consequence: detection layers reduce exposure, but the security argument must rest on the architectural layer.

| Layer | Representative work | What it catches | What it misses |
|---|---|---|---|
| Architectural (by design) | [[sources/CaMeL]]: privileged planner + quarantined parser + capability-enforcing interpreter; [[sources/FIDES]]: information-flow labels with deterministic invariants; [[sources/Willison Dual LLM Pattern]]: the 2023 ancestor; [[sources/Web Agents Plan-Then-Execute]]: commit to a plan before observing untrusted content; code-then-execute and related patterns in [[sources/Design Patterns for Securing LLM Agents]] | The attack class itself — untrusted data cannot select actions by construction | Costs task expressiveness (CaMeL solved 77% vs 84% undefended on [[sources/AgentDojo]] v1); social engineering of the human; attacks within the granted capability set |
| Model layer (weights) | [[sources/The Instruction Hierarchy]]: trained privilege ordering system > developer > user > tool output; [[sources/IH-Challenge]]: its 2026 RL successor (84.1% to 94.1% robustness on GPT-5-Mini); [[sources/SecAlign]]: adversarial preference optimization driving evaluated attack success below 10% | Raises attacker cost broadly, including against unseen attack types; no runtime overhead | Probabilistic, and exactly the layer adaptive attacks optimize against; robustness numbers hold only for the tested attack suites |
| Prompt layer | Spotlighting/delimiting untrusted spans so the model can attribute provenance | Casual and accidental injections | Trivially bypassed under adversarial pressure; no enforcement |
| Classifier guardrails | [[sources/LlamaFirewall]]: input scanner + CoT alignment auditor + code scanner (1.75% ASR combined on its own eval); [[sources/Constitutional Classifiers]]: constitution-trained input/output classifiers surviving 3,000+ red-team hours against universal jailbreaks at 0.38% refusal and 23.7% compute overhead | High-volume commodity attacks; trace-level auditors catch goal deviation that input scanners miss | Defense-aware attackers ([[sources/The Attacker Moves Second]]); EchoLeak bypassed exactly this layer in production |
| Egress and credential controls | [[sources/Infisical Agent Vault]]: proxy-injected credentials the agent never sees; CSP/link-redaction as in the EchoLeak analysis; [[safety/sandbox escape and credential exposure]] | Converts successful injection into failed exfiltration; covers APIs, CLIs, and MCP tools uniformly below the application layer | Damage through permitted channels; EchoLeak found an allowed proxy that CSP missed |

The layers compose in one direction: architecture bounds what an injected agent can do, model and classifier layers reduce how often injection succeeds, and egress controls limit what a successful injection is worth. Running only the middle layers — the common deployment — is the configuration the adaptive-attack results say fails.

## Measurement

- [[sources/InjecAgent]] is the early indirect-injection baseline for tool-integrated agents; [[sources/AgentDojo]] succeeded it as the dynamic environment architectural defenses report against — the CaMeL utility cost above is an AgentDojo number.
- [[sources/Agent Security Bench]] widens the attack surface past injection to memory poisoning, backdoor-style, and mixed attacks under one harness.
- [[sources/PEAR]] isolates planner-executor architectures: attacks that land in the planning stage do more damage than executor-stage attacks, because the planner controls everything downstream.
- [[sources/BrowseSafe]] measures injection against browser agents specifically; from the product side, [[sources/OpenAI Operator System Card]] names prompt injection alongside harmful tasks and model mistakes as a core risk category for the [[sources/OpenAI Computer-Using Agent]] model behind Operator.

All static suites share the caveat from [[sources/The Attacker Moves Second]]: scores against fixed attack strings bound the casual attacker, not the adaptive one.

## Design Guidance

- Start from the trifecta: remove or gate one leg (usually egress) before tuning detection.
- Treat tool descriptions, server metadata, and repository config as untrusted input channels, not just page and document content.
- Keep policy enforcement deterministic; see [[claims/Claim - Untrusted content must not drive agent control flow]] for the full argument and evidence.
- Evaluate any defense against adaptive attacks, not static attack strings — reported near-zero attack rates from static evaluation have not survived contact with defense-aware attackers.

## Related

- [[claims/Claim - Untrusted content must not drive agent control flow]]
- [[safety/protocol security]]
- [[safety/sandbox escape and credential exposure]]
- [[concepts/tool use]]
- [[operations/permissions]]
- [[safety/agent safety and security]]
