# Scaling With Computation

Scaling with computation is the design principle that methods should improve as more compute, data, search, feedback, and experience become available.

In this vault, the useful version of the idea is not that all hand-designed structure is bad. The useful rule is that structure should make scalable search and learning easier: better environments, better tool interfaces, better evals, better reward signals, better memory, and better feedback loops.

## Agent-System Implications

- Prefer designs that can be improved by more runs, better traces, stronger evals, larger context, broader tool use, or learned policies.
- Treat prompts, topologies, workflows, and skills as things to search, train, evaluate, and revise.
- Be skeptical of architectures that rely mostly on human-written assumptions and cannot benefit from more computation or experience.
- Use harnesses, observability, and evals to turn agent behavior into data that future runs can exploit.

## Related

- [[concepts/agentic systems]]
- [[methods/agentic workflow search]]
- [[methods/multi-agent learning]]
- [[operations/agent evals]]
- [[operations/agent memory]]
- [[claims/Claim - Agent memory and skills create compounding improvement loops]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]

## Related Sources

- [[sources/Rich Sutton The Bitter Lesson]]
- [[sources/Google Scaling Agent Systems]]
- [[sources/AFlow]]
- [[sources/ADAS]]
- [[sources/Multi-Agent Design - MASS]]
- [[sources/SiriuS]]
