# Claim - Agent Memory And Skills Create Compounding Improvement Loops

Agent systems improve when successful procedures, failed attempts, learned rules, and reusable strategies are captured as memory or skills and then evaluated before reuse. This turns one-off agent work into compounding procedural knowledge.

## Supporting Sources

- [[sources/Anthropic Agent Skills]] and [[sources/Agent Skills Specification]] define the modern skill package as reusable procedural knowledge.
- [[sources/SkillsBench]] measures when skills help across diverse tasks.
- [[sources/SkillOpt]] trains natural-language skill files through scored rollouts, bounded text edits, rejected-edit feedback, and held-out validation gates.
- [[sources/OpenAI Codex Record and Replay]] turns demonstrated workflows into reusable skills, making tacit GUI/workflow knowledge inspectable and repeatable.
- [[sources/Agent Memory Characterization]], [[sources/Are We Ready For An Agent-Native Memory System]], and [[sources/Memora]] treat memory as a maintained agent subsystem rather than a raw context dump.
- [[sources/Metis]] shows the bridge between textual experience and validated callable tools.
- [[sources/Memory Poisoning Attacks in LLM Agents]] gives the safety constraint: compounding memory can also compound adversarial writes and stale facts.
- [[sources/Anthropic Building Effective AI Agents eBook]] presents Skills as modular capability packages that let single-agent and multi-agent systems reuse workflows, domain knowledge, integrations, and best practices.
- [[sources/Agentic Skills in the Wild]] adds the realistic constraint that agents must retrieve and choose useful skills from larger collections.
- [[sources/Google ReasoningBank]] distills strategies from successful and failed experiences.
- [[sources/SiriuS]] uses bootstrapped reasoning trajectories for self-improving MAS.
- [[sources/SAGE Skill Library]] and [[sources/SkillRL]] study skill libraries as evolving agent state.
- [[sources/Voyager]] is the pre-SKILL.md precedent for executable skill libraries and self-verification.
- [[sources/Cursor Bugbot Learned Rules]] is a deployed feedback-to-rules example.
- [[sources/Darwin Godel Machine]], [[sources/Hyperagents]], and [[sources/Meta-Harness]] extend the pattern from memory/skills to executable self-improvement over agent and harness code.
- [[sources/AlphaEvolve]] and [[sources/The AI Scientist-v2]] show the adjacent algorithm/research-code version: mutate code or hypotheses, evaluate, select, and repeat.

## Design Implications

- Store procedures, not just facts.
- Track provenance and task context for learned memory.
- Evaluate skills before broad reuse.
- For executable improvements, require sandboxing, rollback, and evaluator-hardening before reuse.
- Separate trusted project instructions from untrusted retrieved content.
- Prefer compact, discoverable skills over stuffing every procedure into the base prompt.
- Add provenance, validity, and deletion paths before allowing memory to influence future runs automatically.

## Related

- [[maps/What Makes Agent Systems Better]]
- [[maps/Agent Skills Map]]
- [[concepts/agent skills]]
- [[concepts/procedural memory]]
- [[operations/agent memory]]
- [[concepts/lifelong agent learning]]
- [[methods/self-improving code loops]]
