# Programmatic Tool Calling

Programmatic tool calling lets an agent write code that calls tools, loops over results, filters noisy outputs, and returns only useful information to the model.

This differs from one-tool-call-at-a-time function calling. It moves intermediate computation into an execution runtime, reducing context pressure and model round trips while making tool orchestration more inspectable.

The boundary is task-shaped rather than vendor-shaped. [[sources/OpenAI Programmatic Tool Calling]] recommends generated code for bounded control flow and structured operations such as filtering, joining, ranking, deduplication, and aggregation. It recommends direct model tool calls where each result needs semantic judgment, the action needs approval, or final citations and native artifacts must be preserved. The program runtime is still an untrusted caller: application-side permission checks, idempotency, and approval gates remain necessary.

## Related Sources

- [[sources/Anthropic Code Execution with MCP]]
- [[sources/Cloudflare Code Mode MCP]]
- [[sources/Cloudflare Code Mode MCP API]]
- [[sources/LangChain Deep Agents v0.6]]
- [[sources/OpenAI Responses API Computer Environment]]
- [[sources/OpenAI Programmatic Tool Calling]]
- [[sources/OpenAI GPT-5.6]]

## Related

- [[concepts/tool use]]
- [[concepts/dynamic tool discovery]]
- [[concepts/agent operating surfaces]]
- [[operations/agent harnesses]]
- [[operations/cost control]]
