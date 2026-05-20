# Long-Horizon Agents Map

Use this as a navigation page for long-running autonomy, persistent work, and agent operating environments. Source evidence should be reached through the linked concept and operation notes.

## Core Notes

- [[concepts/long-horizon agents]]
- [[concepts/durable dormant agents]]
- [[concepts/dreaming and memory consolidation]]
- [[concepts/versioned context]]
- [[operations/durable sessions]]
- [[concepts/context engineering]]
- [[operations/agent harnesses]]
- [[operations/agent observability]]
- [[operations/agent memory]]
- [[operations/sandboxes]]

## Mechanisms For Persistence And Recovery

- Keep task state outside the model context window.
- Use harness artifacts, logs, and checkpoints to survive context resets.
- Use explicit state machines and event-driven wakeups for work that pauses for days.
- Consolidate memory between sessions instead of replaying every past turn.
- Route risky actions through permissions and sandboxing.
- Use evals and observability to detect drift over long runs.
- Convert repeated procedures into skills or procedural memory.

## Related Synthesis

- [[maps/What Makes Agent Systems Better]]
- [[maps/Recent Agent Operating Concepts]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
- [[claims/Claim - Agent memory and skills create compounding improvement loops]]

## Source Trail

Follow the related-source sections in the core notes. Source cards in `sources/` hold the public evidence trail; private crawl logs and working registries stay outside this graph.
