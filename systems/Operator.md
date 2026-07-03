# Operator

> [!note] Historical
> Operator was deprecated mid-2025 and folded into [[systems/ChatGPT agent]], which absorbed its browser/computer-use capability alongside deep research behavior ([[sources/OpenAI ChatGPT Agent System Card]]: system card for the unified successor product). This note is kept as a record of the standalone product and its design pattern.

Operator was OpenAI's browser/computer-using agent product powered by the Computer-Using Agent model.

It mattered because it turned GUI interaction into the agent's action space: screenshots, clicks, typing, browser state, and user confirmations became part of the loop. It remains a useful anchor for prompt injection, UI-grounded tool use, and safety boundaries around real-world web actions — the patterns survived the product.

## Design Pattern

- Use visual browser state as observations rather than only APIs or text.
- Give the agent a constrained action space over clicks, typing, and navigation.
- Require stronger confirmation and isolation around purchases, credentials, and irreversible actions.

## Related

- [[systems/ChatGPT agent]]
- [[concepts/tool use]]
- [[safety/prompt injection]]
- [[safety/agent safety and security]]

## Related Sources

- [[sources/OpenAI Computer-Using Agent|Computer-Using Agent]]
- [[sources/OpenAI ChatGPT Agent System Card|ChatGPT agent System Card]]
- [[sources/OpenAI Operator System Card|Operator System Card]]
