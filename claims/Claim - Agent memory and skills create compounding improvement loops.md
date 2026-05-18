# Claim - Agent Memory And Skills Create Compounding Improvement Loops

Agent systems improve when successful procedures, failed attempts, learned rules, and reusable strategies are captured as memory or skills and then evaluated before reuse. This turns one-off agent work into compounding procedural knowledge.

## Supporting Sources

- [[sources/Anthropic Agent Skills]] and [[sources/Agent Skills Specification]] define the modern skill package as reusable procedural knowledge.
- [[sources/SkillsBench]] measures when skills help across diverse tasks.
- [[sources/Agentic Skills in the Wild]] adds the realistic constraint that agents must retrieve and choose useful skills from larger collections.
- [[sources/Google ReasoningBank]] distills strategies from successful and failed experiences.
- [[sources/SiriuS]] uses bootstrapped reasoning trajectories for self-improving MAS.
- [[sources/SAGE Skill Library]] and [[sources/SkillRL]] study skill libraries as evolving agent state.
- [[sources/Voyager]] is the pre-SKILL.md precedent for executable skill libraries and self-verification.
- [[sources/Cursor Bugbot Learned Rules]] is a deployed feedback-to-rules example.

## Design Implications

- Store procedures, not just facts.
- Track provenance and task context for learned memory.
- Evaluate skills before broad reuse.
- Separate trusted project instructions from untrusted retrieved content.
- Prefer compact, discoverable skills over stuffing every procedure into the base prompt.

## Related

- [[maps/What Makes Agent Systems Better]]
- [[maps/Agent Skills Map]]
- [[concepts/agent skills]]
- [[concepts/procedural memory]]
- [[operations/agent memory]]
- [[concepts/lifelong agent learning]]
