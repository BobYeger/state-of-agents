# AI Co-Scientist

Google's AI co-scientist is a multi-agent scientific-discovery system for generating, refining, ranking, and reviewing research hypotheses.

It matters because it is one of the clearest industry examples of a domain-specific multi-agent research system. The architecture uses specialized roles for generation, reflection, ranking, evolution, and debate rather than treating "research" as a single monolithic assistant task.

## Design Pattern

- Use multiple specialized agents to explore a hypothesis space.
- Separate proposal generation from critique, ranking, and refinement.
- Keep a human scientist in the loop for problem framing, interpretation, and experimental judgment.

## Related

- [[concepts/multi-agent systems]]
- [[methods/multi-agent orchestration]]
- [[methods/multi-agent learning]]
- [[benchmarks/agent evaluation]]
- [[concepts/long-horizon agents]]

## Related Sources

- [[sources/Google AI Co-Scientist Article|Accelerating scientific breakthroughs with an AI co-scientist]]
- [[sources/AI Co-Scientist|Towards an AI Co-Scientist]]
- [[sources/Google MLE-STAR]]
