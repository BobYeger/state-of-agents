# human-in-the-loop agents

Human-in-the-loop agent design decides when a system should keep acting autonomously and when it should pause, ask, route, or escalate.

The useful pattern is calibrated intervention. Humans should not be asked for every trivial step, but they should be brought in for ambiguity, irreversible actions, high-authority tool calls, policy-sensitive work, and cases where the agent lacks confidence or grounding.

Human-in-the-loop agents explicitly involve users in planning, approval, correction, monitoring, or handoff.

## Improvement Levers

- Ask humans at planning boundaries, not only after failure.
- Require approval for purchases, credentials, production writes, and external messages.
- Use human feedback to update evals, rules, memories, or skills.
- Keep human decisions visible in traces for audit and future training.

## Related

- [[operations/permissions]]
- [[operations/agent observability]]
- [[methods/runtime supervision]]
- [[claims/Claim - Runtime control and verification improve agent reliability]]
- [[maps/What Makes Agent Systems Better]]

## Related Sources

- [[sources/Anthropic Trustworthy Agents]]
- [[sources/Anthropic Claude Code Auto Mode]]
- [[sources/OpenAI Running Codex Safely]]
- [[sources/Google ADK Multi-Agent Patterns]]
- [[sources/Anthropic Measuring Agent Autonomy]]
