# Operator

Operator is OpenAI's browser/computer-using agent product powered by the Computer-Using Agent model.

It matters because it turns GUI interaction into the agent's action space: screenshots, clicks, typing, browser state, and user confirmations become part of the loop. This makes Operator a useful anchor for prompt injection, UI-grounded tool use, and safety boundaries around real-world web actions.

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
