# agent skills

Agent skills are reusable procedural artifacts for agents. In the current SKILL.md ecosystem, a skill is usually a folder with a required `SKILL.md` file plus optional scripts, references, and assets.

Skills differ from tools: tools provide actions, while skills provide procedural knowledge for when and how to use actions reliably. They differ from broad project instructions because agents can discover/load skills on demand.

[[concepts/agent plugins|Agent Plugins]] provide the higher package layer: one portable plugin can combine skills with [[protocols/MCP|MCP]] server configuration while leaving vendor-specific features in client extensions.

## Skill Use Is a Harness Capability

A valid skill artifact does not imply that an agent can use it reliably. [[sources/Skill-Use]] separates three failure points under progressive disclosure:

- **Trigger:** recognize from compact metadata that a skill applies and load its full procedure.
- **Compliance:** execute the required steps after loading it.
- **Boundary:** avoid operations the skill explicitly forbids.

Across 79 real skills, 177 executable tasks, eight models, and two coding-agent harnesses, the strongest combined score is 0.613. Triggering and compliance fail independently, and both scores and model rankings move with the harness. Skill use should therefore be evaluated as a model–harness–skill configuration: retrieval-only tests miss procedural failures, while task-success-only tests can reward an agent that bypassed the governed procedure.

## Key Sources

- [[sources/Anthropic Agent Skills]]
- [[sources/Anthropic Building Effective AI Agents eBook]]
- [[sources/Agent Skills Specification]]
- [[sources/Agent Plugins Specification]]
- [[sources/OpenAI Skills Docs]]
- [[sources/GitHub Copilot Agent Skills Docs]]
- [[sources/SkillsBench]]
- [[sources/Skill-Use]]
- [[sources/SkillOpt]]
- [[sources/Agent Skills for Large Language Models]]

## Related

- [[concepts/procedural memory]]
- [[concepts/agent plugins]]
- [[operations/agent harnesses]]
- [[protocols/MCP]]
- [[maps/Agent Skills Map]]
