# Tool Use

Tool use is the interface between probabilistic model behavior and deterministic external systems. Tool schemas, errors, affordances, permissions, and observability are part of the agent design, not implementation details.

## Tool Contracts

Tool contracts define what an agent can call, what inputs are valid, what outputs mean, what errors look like, and how the system monitors or constrains tool execution.

The contract is where many agent failures become engineering failures. A weak contract makes the model infer hidden semantics, ignore errors, over-trust tool output, or take unsafe action with insufficient confirmation.

Tool quality is therefore one of the main positive levers for agent performance. Better tools reduce ambiguity, make recovery possible, and give the harness useful observations.

Useful contract surface:

- Schema: required fields, valid ranges, defaults, and examples.
- Semantics: what the tool guarantees and what it does not guarantee.
- Error model: recoverable errors, fatal errors, partial success, and ambiguous output.
- Authority: what the call is allowed to read, write, spend, send, or delete.
- Observability: logs, traces, approvals, and post-action audit data.

## Related

- [[protocols/MCP]]
- [[claims/Claim - Harnesses tools and context are core agent performance levers]]
- [[operations/sandboxes]]
- [[operations/permissions]]
- [[safety/prompt injection]]

## Related Sources

- [[sources/Agent Security Bench|Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents]]
- [[sources/AgentDojo|AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents]]
- [[sources/Agentic Large Language Models - A Survey|Agentic Large Language Models, a survey]]
- [[sources/AI Agent Systems - Architectures Applications and Evaluation|AI Agent Systems: Architectures, Applications, and Evaluation]]
- [[sources/A2A Specification|Agent2Agent Protocol Specification]]
- [[sources/Anthropic Building Effective Agents|Building effective agents]]
- [[sources/OpenAI Computer-Using Agent|Computer-Using Agent]]
- [[sources/Cursor Agent Computer Use|Cursor agents can now control their own computers]]
- [[sources/Anthropic Effective Context Engineering|Effective context engineering for AI agents]]
- [[sources/OpenAI Responses API Computer Environment|From model to agent: Equipping the Responses API with a computer environment]]
- [[sources/Anthropic Multi-Agent Research System|How we built our multi-agent research system]]
- [[sources/OpenAI ChatGPT Agent System Card|ChatGPT agent System Card]]
- [[sources/OpenAI Agents SDK Docs|OpenAI Agents SDK Documentation]]
- [[sources/OpenHands|OpenHands: An Open Platform for AI Software Developers as Generalist Agents]]
- [[sources/OpenAI Codex Agent Loop|Unrolling the Codex agent loop]]
- [[sources/Design Patterns for Securing LLM Agents|Design Patterns for Securing LLM Agents against Prompt Injections]]
- [[sources/InjecAgent|InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents]]
- [[sources/Anthropic Writing Tools for Agents|Writing effective tools for agents - with agents]]
