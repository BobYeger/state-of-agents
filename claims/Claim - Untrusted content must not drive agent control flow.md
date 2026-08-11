# Claim - Untrusted Content Must Not Drive Agent Control Flow

Prompt injection is unsolved at the model layer, so agent security comes from architecture: decide what the agent will do using trusted input only, and let untrusted content act as data — parsed, labeled, and policy-checked — never as instructions that select the next action. Detection-based defenses filter some attacks; structural separation of control flow from untrusted data removes the attack class.

## Supporting Sources

- [[sources/Willison Dual LLM Pattern]] originates the split (2023): a privileged LLM with tool access sees only trusted input, a quarantined LLM parses untrusted content with no tools, and raw untrusted text never reaches the privileged side.
- [[sources/CaMeL]] makes the separation provable: a privileged model plans from the user query alone, a quarantined model extracts data, and an interpreter with capability-tagged values enforces policy before every tool call — untrusted data cannot influence control flow by construction, at a measured utility cost (77% vs 84% on AgentDojo v1). It also fixes the dual-LLM pattern's data-dependency exfiltration hole.
- [[sources/FIDES]] gives the information-flow-control formulation: integrity and confidentiality labels propagated by deterministic taint tracking, two invariants (tool calls require trusted-integrity data; data flows only to permitted readers), and hide/unhide primitives to recover task expressiveness.
- [[sources/Web Agents Plan-Then-Execute]] applies the same principle to computer use: commit to a task-specific plan before observing runtime web content, because ReAct-style agents let pages steer execution.
- [[sources/Design Patterns for Securing LLM Agents]] catalogues the implementable pattern family — plan-then-execute, code-then-execute, action-selector, context-minimization — bridging the papers to buildable controls.
- [[sources/Willison Lethal Trifecta]] supplies the operational test: private data, untrusted content, and an egress channel together make exfiltration inevitable; once untrusted input is ingested, consequential actions must be structurally constrained.
- [[sources/The Attacker Moves Second]] is the negative result that forces the claim: adaptive attackers achieved >90% success against twelve published detection- and training-based defenses that had reported near-zero attack rates, so in-band filtering cannot carry the security argument.
- [[sources/EchoLeak]] is the incident proof: a zero-click exfiltration from Microsoft 365 Copilot in which the injection classifier (XPIA) was bypassed and untrusted email content drove the agent's retrieval and rendering behavior end to end.
- [[sources/Invariant Labs MCP Tool Poisoning]] shows control-flow capture does not require user-visible content: instructions hidden in MCP tool descriptions redirect a co-connected trusted server's actions.
- [[sources/Check Point Claude Code Project Files RCE]] extends the surface to configuration: repository-provided hooks and settings executed on project open are untrusted content driving harness control flow directly (CVE-2025-59536).
- [[sources/PEAR]] quantifies why the planning stage is the crown jewel: planner-stage attacks are disproportionately damaging in planner-executor agents.
- [[sources/HarnessSafe]] extends the boundary across time: attacker influence can survive through memory, skills, tools/MCP, summaries, subagents, and shared artifacts, then drive a later benign task after the original input has left active context.

## Design Implications

- Derive plans, tool selections, and arguments-with-consequences from trusted input; route untrusted content through a quarantined parse step that returns typed data, not text that re-enters the prompt as instructions.
- Enforce the boundary deterministically (interpreter, taint labels, policy engine) rather than by model judgment; models are the component the attacker optimizes against.
- Treat tool descriptions, MCP server metadata, repository config, and lifecycle automation as untrusted inputs with the same standing as web content.
- Use the lethal-trifecta test at review time: if an agent combines private data, untrusted content, and egress, require a by-design control, not a classifier.
- Accept and budget the utility cost — the CaMeL/FIDES line shows expressiveness can be partially recovered, but some tasks are unsecurable without constraining them.
- Preserve provenance and re-validate persistent state when it crosses sessions, carriers, agents, or workspaces; ingestion-time filtering does not contain a payload that later reappears through a trusted summary or artifact.

## Related

- [[safety/prompt injection]]
- [[safety/protocol security]]
- [[methods/deliberative control]]
- [[operations/permissions]]
- [[concepts/tool use]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]
