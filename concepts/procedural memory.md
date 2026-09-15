# procedural memory

Procedural memory is the agent-system pattern of storing reusable know-how: workflows, tactics, scripts, examples, policies, or skill libraries that can be retrieved and reused across tasks.

In this vault, Agent Skills are the standardized packaging layer for procedural memory. Older skill-library systems such as Voyager show the same idea before SKILL.md: successful behaviors are saved and reused rather than rediscovered from scratch.

## Key Sources

- [[sources/Voyager]]
- [[sources/Anthropic Agent Skills]]
- [[sources/SAGE Skill Library]]
- [[sources/SkillRL]]
- [[sources/SkillOpt]]
- [[sources/WikiSkill]]
- [[sources/SkillAdam]]
- [[sources/LifeMem]]
- [[sources/SE-GoS]]
- [[sources/SiriuS]]
- [[sources/Google ReasoningBank]]

## Separate the Procedure from Its Maintenance

Keep the executable procedure, its retrieval index, and the optimizer's history distinct. [[sources/SkillOpt]], [[sources/WikiSkill]], and [[sources/SkillAdam]] use different proposal and acceptance designs; their scores should not hide those differences. [[sources/SE-GoS]] changes retrieval structure without changing skill bodies. [[sources/LifeMem]] pairs abstract workflows with concrete environment-compatible examples. Evaluate each changed layer and retain a stop/revert path when extra updates cease to help.

## Related

- [[concepts/agent skills]]
- [[operations/agent memory]]
- [[operations/agent harnesses]]
