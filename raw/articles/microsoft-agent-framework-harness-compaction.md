Agent harness is the layer where model reasoning connects to real execution: shell and filesystem access, approval flows, and context management across long-running sessions. With *Agent Framework*, these patterns can now be built consistently in both Python and.NET.

In this post, we’ll look at three practical building blocks for production agents:

- **Local shell harness** for controlled host-side execution
- **Hosted shell harness** for managed execution environments
- **Context compaction** for keeping long conversations efficient and reliable

## Shell and Filesystem Harness

Many agent experiences need to do more than generate text. They need to inspect files, run commands, and work with the surrounding environment in a controlled way. *Agent Framework* makes it possible to model those capabilities explicitly, with approval patterns where needed.

The following examples show compact harness patterns in both Python and.NET.

**Python: Local shell with approvals**

```
import asyncio
import subprocess
from typing import Any

from agent_framework import Agent, Message, tool
from agent_framework.openai import OpenAIResponsesClient

@tool(approval_mode="always_require")
def run_bash(command: str) -> str:
    """Execute a shell command locally and return stdout, stderr, and exit code."""
    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        timeout=30,
    )
    parts: list[str] = []
    if result.stdout:
        parts.append(result.stdout)
    if result.stderr:
        parts.append(f"stderr: {result.stderr}")
    parts.append(f"exit_code: {result.returncode}")
    return "\n".join(parts)

async def run_with_approvals(query: str, agent: Agent) -> Any:
    current_input: str | list[Any] = query

    while True:
        result = await agent.run(current_input)
        if not result.user_input_requests:
            return result

        next_input: list[Any] = [query]
        for request in result.user_input_requests:
            print(f"Shell request: {request.function_call.name}")
            print(f"Arguments: {request.function_call.arguments}")
            approved = (await asyncio.to_thread(input, "Approve command? (y/n): ")).strip().lower() == "y"
            next_input.append(Message("assistant", [request]))
            next_input.append(Message("user", [request.to_function_approval_response(approved)]))
            if not approved:
                return "Shell command execution was rejected by user."

        current_input = next_input

async def main() -> None:
    client = OpenAIResponsesClient(
        model_id="<responses-model-id>",
        api_key="<your-openai-api-key>",
    )
    local_shell_tool = client.get_shell_tool(func=run_bash)

    agent = Agent(
        client=client,
        instructions="You are a helpful assistant that can run shell commands.",
        tools=[local_shell_tool],
    )

    result = await run_with_approvals(
        "Use run_bash to execute \`python --version\` and show only stdout.",
        agent,
    )
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
```

This pattern keeps execution on the host machine while giving the application a clear approval checkpoint before the command runs.

**Security note:** For local shell execution, we recommend running this logic in an isolated environment and keeping explicit approval in place before commands are allowed to run.

**Python: Hosted shell in a managed environment**

```
import asyncio

from agent_framework import Agent
from agent_framework.openai import OpenAIResponsesClient

async def main() -> None:
    client = OpenAIResponsesClient(
        model_id="<responses-model-id>",
        api_key="<your-openai-api-key>",
    )
    shell_tool = client.get_shell_tool()

    agent = Agent(
        client=client,
        instructions="You are a helpful assistant that can execute shell commands.",
        tools=shell_tool,
    )

    result = await agent.run("Use a shell command to show the current date and time")
    print(result)

    for message in result.messages:
        shell_calls = [c for c in message.contents if c.type == "shell_tool_call"]
        shell_results = [c for c in message.contents if c.type == "shell_tool_result"]

        if shell_calls:
            print(f"Shell commands: {shell_calls[0].commands}")
        if shell_results and shell_results[0].outputs:
            for output in shell_results[0].outputs:
                if output.stdout:
                    print(f"Stdout: {output.stdout}")
                if output.stderr:
                    print(f"Stderr: {output.stderr}")
                if output.exit_code is not None:
                    print(f"Exit code: {output.exit_code}")

if __name__ == "__main__":
    asyncio.run(main())
```

Hosted shell is useful when you want the agent to execute commands in a provider-managed environment rather than directly on the local machine.

**.NET: Local shell with approvals**

```cs
using System.ComponentModel;
using System.Diagnostics;
using Microsoft.Agents.AI;
using Microsoft.Extensions.AI;
using OpenAI;

var apiKey = "<your-openai-api-key>";
var model = "<responses-model-id>";

[Description("Execute a shell command locally and return stdout, stderr and exit code.")]
static string RunBash([Description("Bash command to execute.")] string command)
{
    using Process process = new()
    {
        StartInfo = new ProcessStartInfo
        {
            FileName = "/bin/bash",
            ArgumentList = { "-lc", command },
            RedirectStandardOutput = true,
            RedirectStandardError = true,
            UseShellExecute = false,
        }
    };

    process.Start();
    process.WaitForExit(30_000);

    string stdout = process.StandardOutput.ReadToEnd();
    string stderr = process.StandardError.ReadToEnd();

    return $"stdout:\n{stdout}\nstderr:\n{stderr}\nexit_code:{process.ExitCode}";
}

IChatClient chatClient = new OpenAIClient(apiKey)
    .GetResponsesClient(model)
    .AsIChatClient();

AIAgent agent = chatClient.AsAIAgent(
    name: "LocalShellAgent",
    instructions: "Use tools when needed. Avoid destructive commands.",
    tools: [new ApprovalRequiredAIFunction(AIFunctionFactory.Create(RunBash, name: "run_bash"))]);

AgentSession session = await agent.CreateSessionAsync();
AgentResponse response = await agent.RunAsync("Use run_bash to execute \`dotnet --version\` and return only stdout.", session);

List<FunctionApprovalRequestContent> approvalRequests = response.Messages
    .SelectMany(m => m.Contents)
    .OfType<FunctionApprovalRequestContent>()
    .ToList();

while (approvalRequests.Count > 0)
{
    List<ChatMessage> approvals = approvalRequests
        .Select(request => new ChatMessage(ChatRole.User, [request.CreateResponse(approved: true)]))
        .ToList();

    response = await agent.RunAsync(approvals, session);
    approvalRequests = response.Messages
        .SelectMany(m => m.Contents)
        .OfType<FunctionApprovalRequestContent>()
        .ToList();
}

Console.WriteLine(response);
```

Like the Python version, this approach combines local execution with an explicit approval flow so the application stays in control of what actually runs.

**Security note:** For local shell execution, we recommend running this logic in an isolated environment and keeping explicit approval in place before commands are allowed to run.

**.NET: Hosted shell with protocol-level configuration**

```cs
using Microsoft.Agents.AI;
using Microsoft.Extensions.AI;
using OpenAI;
using OpenAI.Responses;

var apiKey = "<your-openai-api-key>";
var model = "<responses-model-id>";

IChatClient chatClient = new OpenAIClient(apiKey)
    .GetResponsesClient(model)
    .AsIChatClient();

CreateResponseOptions hostedShellOptions = new();
hostedShellOptions.Patch.Set(
    "$.tools"u8,
    BinaryData.FromObjectAsJson(new object[]
    {
        new
        {
            type = "shell",
            environment = new
            {
                type = "container_auto"
            }
        }
    }));

AIAgent agent = chatClient
    .AsBuilder()
    .BuildAIAgent(new ChatClientAgentOptions
    {
        Name = "HostedShellAgent",
        UseProvidedChatClientAsIs = true,
        ChatOptions = new ChatOptions
        {
            Instructions = "Use shell commands to answer precisely.",
            RawRepresentationFactory = _ => hostedShellOptions
        }
    });

AgentResponse response = await agent.RunAsync("Use a shell command to print UTC date/time. Return only command output.");
Console.WriteLine(response);
```

This makes it possible to target a managed shell environment from.NET today while keeping the rest of the agent flow in the standard Agent Framework programming model.

## Context Compaction

Long-running agent sessions accumulate chat history that can exceed a model’s context window. The *Agent Framework* includes a built-in compaction system that automatically manages conversation history before each model call — keeping agents within their token budget without losing important context ([Docs](https://learn.microsoft.com/agent-framework/agents/conversations/compaction)).

**Python: In-run compaction on the agent**

```
import asyncio

from agent_framework import Agent, InMemoryHistoryProvider, SlidingWindowStrategy, tool
from agent_framework.openai import OpenAIChatClient

@tool(approval_mode="never_require")
def get_weather(city: str) -> str:
    weather_data = {
        "London": "cloudy, 12°C",
        "Paris": "sunny, 18°C",
        "Tokyo": "rainy, 22°C",
    }
    return weather_data.get(city, f"No data for {city}")

async def main() -> None:
    client = OpenAIChatClient(
        model_id="<chat-model-id>",
        api_key="<your-openai-api-key>",
    )

    agent = Agent(
        client=client,
        instructions="You are a helpful weather assistant.",
        tools=[get_weather],
        context_providers=[InMemoryHistoryProvider()],
        compaction_strategy=SlidingWindowStrategy(keep_last_groups=3),
    )

    session = agent.create_session()
    for query in [
        "What is the weather in London?",
        "How about Paris?",
        "And Tokyo?",
        "Which city is the warmest?",
    ]:
        result = await agent.run(query, session=session)
        print(result.text)

if __name__ == "__main__":
    asyncio.run(main())
```

This example keeps the most recent conversational context intact while trimming older tool-heavy exchanges that no longer need to be replayed in full.

**.NET: Compaction pipeline with multiple strategies**

```cs
using System.ComponentModel;
using Microsoft.Agents.AI;
using Microsoft.Agents.AI.Compaction;
using Microsoft.Extensions.AI;
using OpenAI;

var apiKey = "<your-openai-api-key>";
var model = "<chat-model-id>";

[Description("Look up the current price of a product by name.")]
static string LookupPrice([Description("The product to look up.")] string productName) =>
    productName.ToUpperInvariant() switch
    {
        "LAPTOP" => "The laptop costs $999.99.",
        "KEYBOARD" => "The keyboard costs $79.99.",
        "MOUSE" => "The mouse costs $29.99.",
        _ => $"No data for {productName}."
    };

IChatClient chatClient = new OpenAIClient(apiKey)
    .GetChatClient(model)
    .AsIChatClient();

PipelineCompactionStrategy compactionPipeline = new(
    new ToolResultCompactionStrategy(CompactionTriggers.MessagesExceed(7)),
    new SlidingWindowCompactionStrategy(CompactionTriggers.TurnsExceed(4)),
    new TruncationCompactionStrategy(CompactionTriggers.GroupsExceed(12)));

AIAgent agent = chatClient
    .AsBuilder()
    .UseAIContextProviders(new CompactionProvider(compactionPipeline))
    .BuildAIAgent(new ChatClientAgentOptions
    {
        Name = "ShoppingAssistant",
        ChatOptions = new ChatOptions
        {
            Instructions = "You are a concise shopping assistant.",
            Tools = [AIFunctionFactory.Create(LookupPrice)]
        },
        ChatHistoryProvider = new InMemoryChatHistoryProvider()
    });

AgentSession session = await agent.CreateSessionAsync();

string[] prompts =
[
    "What's the price of a laptop?",
    "How about a keyboard?",
    "And a mouse?",
    "Which is cheapest?",
    "What was the first product I asked about?"
];

foreach (string prompt in prompts)
{
    Console.WriteLine($"User: {prompt}");
    AgentResponse response = await agent.RunAsync(prompt, session);
    Console.WriteLine($"Agent: {response}\\n");

    if (session.TryGetInMemoryChatHistory(out var history))
    {
        Console.WriteLine($"[Stored message count: {history.Count}]\\n");
    }
}
```

By combining multiple compaction strategies, you can keep sessions responsive and cost-aware without giving up continuity.

## What’s Next?

These patterns make Agent Framework a stronger foundation for real-world agent systems:

- **Local shell with approvals** enables controlled execution on the host.
- **Hosted shell** supports execution in managed environments.
- **Compaction strategies** help long-running sessions stay within limits while preserving useful context.

Whether you are building an assistant that can inspect a project workspace or a multi-step workflow that needs durable context over time, these capabilities help close the gap between model reasoning and practical execution.

For more information, check out our [documentation](https://learn.microsoft.com/en-us/agent-framework/) and examples on [GitHub](https://github.com/microsoft/agent-framework), and install the latest packages from [NuGet (.NET)](https://www.nuget.org/packages/Microsoft.Agents.AI/) or [PyPI (Python)](https://pypi.org/project/agent-framework/).