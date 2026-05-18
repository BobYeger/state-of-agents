# lifelong agent learning

Lifelong agent learning covers memory, reusable experience, learned rules, and post-deployment improvement loops.

The useful design question is how an agent turns experience into reusable, governed capability. Learning loops need memory, skill extraction, evaluation, provenance, and safe update rules; otherwise they can preserve errors as easily as improvements.

## Mechanisms

- Distill successful and failed trajectories into reusable strategies.
- Convert repeated procedures into skills or learned rules.
- Use evals to decide whether a learned behavior should be reused.
- Track provenance, scope, and freshness for learned memory.

## Related

- [[operations/agent memory]]
- [[concepts/procedural memory]]
- [[concepts/agent skills]]
- [[methods/multi-agent learning]]
- [[operations/agent evals]]
- [[claims/Claim - Agent memory and skills create compounding improvement loops]]
- [[maps/What Makes Agent Systems Better]]

## Related Sources

- [[sources/Google ReasoningBank]]
- [[sources/Cursor Bugbot Learned Rules]]
- [[sources/SkillRL]]
- [[sources/SAGE Skill Library]]
- [[sources/SiriuS]]
- [[sources/SkillsBench]]
- [[sources/Agentic Skills in the Wild]]
