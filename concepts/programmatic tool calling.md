# Programmatic Tool Calling

Programmatic tool calling lets an agent write code that calls tools, loops over results, filters noisy outputs, and returns only useful information to the model.

This differs from one-tool-call-at-a-time function calling. It moves intermediate computation into an execution runtime, reducing context pressure and model round trips while making tool orchestration more inspectable.

## Related Sources

- [[sources/Anthropic Code Execution with MCP]]
- [[sources/Cloudflare Code Mode MCP]]
- [[sources/LangChain Deep Agents v0.6]]
- [[sources/OpenAI Responses API Computer Environment]]

## Related

- [[concepts/tool use]]
- [[concepts/dynamic tool discovery]]
- [[operations/agent harnesses]]
- [[operations/cost control]]
