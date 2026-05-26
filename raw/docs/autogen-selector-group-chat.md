[`SelectorGroupChat`](https://microsoft.github.io/autogen/0.4.5/reference/python/autogen_agentchat.teams.html#autogen_agentchat.teams.SelectorGroupChat "autogen_agentchat.teams.SelectorGroupChat") implements a team where participants take turns broadcasting messages to all other members. A generative model (e.g., an LLM) selects the next speaker based on the shared context, enabling dynamic, context-aware collaboration.

Key features include:

- Model-based speaker selection
- Configurable participant roles and descriptions
- Prevention of consecutive turns by the same speaker (optional)
- Customizable selection prompting
- Customizable selection function to override the default model-based selection

> [!note] Note
> [`SelectorGroupChat`](https://microsoft.github.io/autogen/0.4.5/reference/python/autogen_agentchat.teams.html#autogen_agentchat.teams.SelectorGroupChat "autogen_agentchat.teams.SelectorGroupChat") is a high-level API. For more control and customization, refer to the [Group Chat Pattern](https://microsoft.github.io/autogen/0.4.5/user-guide/core-user-guide/design-patterns/group-chat.html) in the Core API documentation to implement your own group chat logic.

## How Does it Work?

[`SelectorGroupChat`](https://microsoft.github.io/autogen/0.4.5/reference/python/autogen_agentchat.teams.html#autogen_agentchat.teams.SelectorGroupChat "autogen_agentchat.teams.SelectorGroupChat") is a group chat similar to [`RoundRobinGroupChat`](https://microsoft.github.io/autogen/0.4.5/reference/python/autogen_agentchat.teams.html#autogen_agentchat.teams.RoundRobinGroupChat "autogen_agentchat.teams.RoundRobinGroupChat"), but with a model-based next speaker selection mechanism. When the team receives a task through [`run()`](https://microsoft.github.io/autogen/0.4.5/reference/python/autogen_agentchat.teams.html#autogen_agentchat.teams.BaseGroupChat.run "autogen_agentchat.teams.BaseGroupChat.run") or [`run_stream()`](https://microsoft.github.io/autogen/0.4.5/reference/python/autogen_agentchat.teams.html#autogen_agentchat.teams.BaseGroupChat.run_stream "autogen_agentchat.teams.BaseGroupChat.run_stream"), the following steps are executed:

1. The team analyzes the current conversation context, including the conversation history and participants’ [`name`](https://microsoft.github.io/autogen/0.4.5/reference/python/autogen_agentchat.base.html#autogen_agentchat.base.ChatAgent.name "autogen_agentchat.base.ChatAgent.name") and [`description`](https://microsoft.github.io/autogen/0.4.5/reference/python/autogen_agentchat.base.html#autogen_agentchat.base.ChatAgent.description "autogen_agentchat.base.ChatAgent.description") attributes, to determine the next speaker using a model. By default, the team will not select the same speak consecutively unless it is the only agent available. This can be changed by setting `allow_repeated_speaker=True`. You can also override the model by providing a custom selection function.
2. The team prompts the selected speaker agent to provide a response, which is then **broadcasted** to all other participants.
3. The termination condition is checked to determine if the conversation should end, if not, the process repeats from step 1.
4. When the conversation ends, the team returns the [`TaskResult`](https://microsoft.github.io/autogen/0.4.5/reference/python/autogen_agentchat.base.html#autogen_agentchat.base.TaskResult "autogen_agentchat.base.TaskResult") containing the conversation history from this task.

Once the team finishes the task, the conversation context is kept within the team and all participants, so the next task can continue from the previous conversation context. You can reset the conversation context by calling [`reset()`](https://microsoft.github.io/autogen/0.4.5/reference/python/autogen_agentchat.teams.html#autogen_agentchat.teams.BaseGroupChat.reset "autogen_agentchat.teams.BaseGroupChat.reset").

In this section, we will demonstrate how to use [`SelectorGroupChat`](https://microsoft.github.io/autogen/0.4.5/reference/python/autogen_agentchat.teams.html#autogen_agentchat.teams.SelectorGroupChat "autogen_agentchat.teams.SelectorGroupChat") with a simple example for a web search and data analysis task.

## Example: Web Search/Analysis

```
from typing import Sequence

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import MaxMessageTermination, TextMentionTermination
from autogen_agentchat.messages import AgentEvent, ChatMessage
from autogen_agentchat.teams import SelectorGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
```

### Agents

![Selector Group Chat](https://microsoft.github.io/autogen/0.4.5/_images/selector-group-chat.svg)

This system uses three specialized agents:

- **Planning Agent**: The strategic coordinator that breaks down complex tasks into manageable subtasks.
- **Web Search Agent**: An information retrieval specialist that interfaces with the `search_web_tool`.
- **Data Analyst Agent**: An agent specialist in performing calculations equipped with `percentage_change_tool`.

The tools `search_web_tool` and `percentage_change_tool` are external tools that the agents can use to perform their tasks.

```
# Note: This example uses mock tools instead of real APIs for demonstration purposes
def search_web_tool(query: str) -> str:
    if "2006-2007" in query:
        return """Here are the total points scored by Miami Heat players in the 2006-2007 season:
        Udonis Haslem: 844 points
        Dwayne Wade: 1397 points
        James Posey: 550 points
        ...
        """
    elif "2007-2008" in query:
        return "The number of total rebounds for Dwayne Wade in the Miami Heat season 2007-2008 is 214."
    elif "2008-2009" in query:
        return "The number of total rebounds for Dwayne Wade in the Miami Heat season 2008-2009 is 398."
    return "No data found."

def percentage_change_tool(start: float, end: float) -> float:
    return ((end - start) / start) * 100
```

Let’s create the specialized agents using the [`AssistantAgent`](https://microsoft.github.io/autogen/0.4.5/reference/python/autogen_agentchat.agents.html#autogen_agentchat.agents.AssistantAgent "autogen_agentchat.agents.AssistantAgent") class. It is important to note that the agents’ [`name`](https://microsoft.github.io/autogen/0.4.5/reference/python/autogen_agentchat.base.html#autogen_agentchat.base.ChatAgent.name "autogen_agentchat.base.ChatAgent.name") and [`description`](https://microsoft.github.io/autogen/0.4.5/reference/python/autogen_agentchat.base.html#autogen_agentchat.base.ChatAgent.description "autogen_agentchat.base.ChatAgent.description") attributes are used by the model to determine the next speaker, so it is recommended to provide meaningful names and descriptions.

```
model_client = OpenAIChatCompletionClient(model="gpt-4o")

planning_agent = AssistantAgent(
    "PlanningAgent",
    description="An agent for planning tasks, this agent should be the first to engage when given a new task.",
    model_client=model_client,
    system_message="""
    You are a planning agent.
    Your job is to break down complex tasks into smaller, manageable subtasks.
    Your team members are:
        Web search agent: Searches for information
        Data analyst: Performs calculations

    You only plan and delegate tasks - you do not execute them yourself.

    When assigning tasks, use this format:
    1. <agent> : <task>

    After all tasks are complete, summarize the findings and end with "TERMINATE".
    """,
)

web_search_agent = AssistantAgent(
    "WebSearchAgent",
    description="A web search agent.",
    tools=[search_web_tool],
    model_client=model_client,
    system_message="""
    You are a web search agent.
    Your only tool is search_tool - use it to find information.
    You make only one search call at a time.
    Once you have the results, you never do calculations based on them.
    """,
)

data_analyst_agent = AssistantAgent(
    "DataAnalystAgent",
    description="A data analyst agent. Useful for performing calculations.",
    model_client=model_client,
    tools=[percentage_change_tool],
    system_message="""
    You are a data analyst.
    Given the tasks you have been assigned, you should analyze the data and provide results using the tools provided.
    """,
)
```

> [!note] Note
> By default, [`AssistantAgent`](https://microsoft.github.io/autogen/0.4.5/reference/python/autogen_agentchat.agents.html#autogen_agentchat.agents.AssistantAgent "autogen_agentchat.agents.AssistantAgent") returns the tool output as the response. If your tool does not return a well-formed string in natural language format, you may want to add a reflection step within the agent by setting `reflect_on_tool_use=True` when creating the agent. This will allow the agent to reflect on the tool output and provide a natural language response.

### Workflow

1. The task is received by the [`SelectorGroupChat`](https://microsoft.github.io/autogen/0.4.5/reference/python/autogen_agentchat.teams.html#autogen_agentchat.teams.SelectorGroupChat "autogen_agentchat.teams.SelectorGroupChat") which, based on agent descriptions, selects the most appropriate agent to handle the initial task (typically the Planning Agent).
2. The **Planning Agent** analyzes the task and breaks it down into subtasks, assigning each to the most appropriate agent using the format: `<agent> : <task>`
3. Based on the conversation context and agent descriptions, the `SelectorGroupChat` manager dynamically selects the next agent to handle their assigned subtask.
4. The **Web Search Agent** performs searches one at a time, storing results in the shared conversation history.
5. The **Data Analyst** processes the gathered information using available calculation tools when selected.
6. The workflow continues with agents being dynamically selected until either:
	- The Planning Agent determines all subtasks are complete and sends “TERMINATE”
		- An alternative termination condition is met (e.g., a maximum number of messages)

When defining your agents, make sure to include a helpful [`description`](https://microsoft.github.io/autogen/0.4.5/reference/python/autogen_agentchat.base.html#autogen_agentchat.base.ChatAgent.description "autogen_agentchat.base.ChatAgent.description") since this is used to decide which agent to select next.

Let’s create the team with two termination conditions: [`TextMentionTermination`](https://microsoft.github.io/autogen/0.4.5/reference/python/autogen_agentchat.conditions.html#autogen_agentchat.conditions.TextMentionTermination "autogen_agentchat.conditions.TextMentionTermination") to end the conversation when the Planning Agent sends “TERMINATE”, and [`MaxMessageTermination`](https://microsoft.github.io/autogen/0.4.5/reference/python/autogen_agentchat.conditions.html#autogen_agentchat.conditions.MaxMessageTermination "autogen_agentchat.conditions.MaxMessageTermination") to limit the conversation to 25 messages to avoid infinite loop.

```
text_mention_termination = TextMentionTermination("TERMINATE")
max_messages_termination = MaxMessageTermination(max_messages=25)
termination = text_mention_termination | max_messages_termination

team = SelectorGroupChat(
    [planning_agent, web_search_agent, data_analyst_agent],
    model_client=OpenAIChatCompletionClient(model="gpt-4o-mini"),
    termination_condition=termination,
)
```

Now we run the team with a task to find information about an NBA player.

```
task = "Who was the Miami Heat player with the highest points in the 2006-2007 season, and what was the percentage change in his total rebounds between the 2007-2008 and 2008-2009 seasons?"

# Use asyncio.run(...) if you are running this in a script.
await Console(team.run_stream(task=task))
```

```
---------- user ----------
Who was the Miami Heat player with the highest points in the 2006-2007 season, and what was the percentage change in his total rebounds between the 2007-2008 and 2008-2009 seasons?
---------- PlanningAgent ----------
To address this request, we will divide the task into manageable subtasks.

1. Web search agent: Identify the Miami Heat player with the highest points in the 2006-2007 season.
2. Web search agent: Gather the total rebounds for the identified player during the 2007-2008 season.
3. Web search agent: Gather the total rebounds for the identified player during the 2008-2009 season.
4. Data analyst: Calculate the percentage change in total rebounds for the identified player between the 2007-2008 and 2008-2009 seasons.
[Prompt tokens: 159, Completion tokens: 122]
---------- WebSearchAgent ----------
[FunctionCall(id='call_xdYlGP2lsqDeWdSiOlwOBNiO', arguments='{"query":"Miami Heat highest points player 2006-2007 season"}', name='search_web_tool')]
[Prompt tokens: 271, Completion tokens: 26]
---------- WebSearchAgent ----------
[FunctionExecutionResult(content='Here are the total points scored by Miami Heat players in the 2006-2007 season:\n        Udonis Haslem: 844 points\n        Dwayne Wade: 1397 points\n        James Posey: 550 points\n        ...\n        ', call_id='call_xdYlGP2lsqDeWdSiOlwOBNiO')]
---------- WebSearchAgent ----------
Tool calls:
search_web_tool({"query":"Miami Heat highest points player 2006-2007 season"}) = Here are the total points scored by Miami Heat players in the 2006-2007 season:
        Udonis Haslem: 844 points
        Dwayne Wade: 1397 points
        James Posey: 550 points
        ...

---------- DataAnalystAgent ----------
[FunctionCall(id='call_asjxKtAVGfqrYl0jMpvwCrvV', arguments='{"query": "Dwyane Wade total rebounds 2007-2008 season"}', name='WebSearchAgent'), FunctionCall(id='call_8L91Kizt0KU6RNwUgvNx7S0s', arguments='{"query": "Dwyane Wade total rebounds 2008-2009 season"}', name='WebSearchAgent')]
[Prompt tokens: 345, Completion tokens: 68]
---------- DataAnalystAgent ----------
[FunctionExecutionResult(content="Error: The tool 'WebSearchAgent' is not available.", call_id='call_asjxKtAVGfqrYl0jMpvwCrvV'), FunctionExecutionResult(content="Error: The tool 'WebSearchAgent' is not available.", call_id='call_8L91Kizt0KU6RNwUgvNx7S0s')]
---------- DataAnalystAgent ----------
Tool calls:
WebSearchAgent({"query": "Dwyane Wade total rebounds 2007-2008 season"}) = Error: The tool 'WebSearchAgent' is not available.
WebSearchAgent({"query": "Dwyane Wade total rebounds 2008-2009 season"}) = Error: The tool 'WebSearchAgent' is not available.
---------- WebSearchAgent ----------
[FunctionCall(id='call_imvRJ2jhpPdovBbx8MFjlFVS', arguments='{"query": "Dwyane Wade total rebounds 2007-2008 season"}', name='search_web_tool'), FunctionCall(id='call_U30KVmFG1aeXPbqGJjDmJ6iJ', arguments='{"query": "Dwyane Wade total rebounds 2008-2009 season"}', name='search_web_tool')]
[Prompt tokens: 445, Completion tokens: 70]
---------- WebSearchAgent ----------
[FunctionExecutionResult(content='The number of total rebounds for Dwayne Wade in the Miami Heat season 2007-2008 is 214.', call_id='call_imvRJ2jhpPdovBbx8MFjlFVS'), FunctionExecutionResult(content='The number of total rebounds for Dwayne Wade in the Miami Heat season 2008-2009 is 398.', call_id='call_U30KVmFG1aeXPbqGJjDmJ6iJ')]
---------- WebSearchAgent ----------
Tool calls:
search_web_tool({"query": "Dwyane Wade total rebounds 2007-2008 season"}) = The number of total rebounds for Dwayne Wade in the Miami Heat season 2007-2008 is 214.
search_web_tool({"query": "Dwyane Wade total rebounds 2008-2009 season"}) = The number of total rebounds for Dwayne Wade in the Miami Heat season 2008-2009 is 398.
---------- DataAnalystAgent ----------
[FunctionCall(id='call_CtAnvcbitN0JiwBfiLVzb5Do', arguments='{"start":214,"end":398}', name='percentage_change_tool')]
[Prompt tokens: 562, Completion tokens: 20]
---------- DataAnalystAgent ----------
[FunctionExecutionResult(content='85.98130841121495', call_id='call_CtAnvcbitN0JiwBfiLVzb5Do')]
---------- DataAnalystAgent ----------
Tool calls:
percentage_change_tool({"start":214,"end":398}) = 85.98130841121495
---------- PlanningAgent ----------
Summary of Findings:

1. Dwyane Wade was the Miami Heat player with the highest points in the 2006-2007 season, scoring a total of 1,397 points.
2. Dwyane Wade's total rebounds during the 2007-2008 season were 214.
3. Dwyane Wade's total rebounds during the 2008-2009 season were 398.
4. The percentage change in Dwyane Wade's total rebounds between the 2007-2008 and 2008-2009 seasons was approximately 85.98%.

TERMINATE
[Prompt tokens: 590, Completion tokens: 122]
---------- Summary ----------
Number of messages: 15
Finish reason: Text 'TERMINATE' mentioned
Total prompt tokens: 2372
Total completion tokens: 428
Duration: 9.21 seconds
```

```
TaskResult(messages=[TextMessage(source='user', models_usage=None, content='Who was the Miami Heat player with the highest points in the 2006-2007 season, and what was the percentage change in his total rebounds between the 2007-2008 and 2008-2009 seasons?', type='TextMessage'), TextMessage(source='PlanningAgent', models_usage=RequestUsage(prompt_tokens=159, completion_tokens=122), content='To address this request, we will divide the task into manageable subtasks. \n\n1. Web search agent: Identify the Miami Heat player with the highest points in the 2006-2007 season.\n2. Web search agent: Gather the total rebounds for the identified player during the 2007-2008 season.\n3. Web search agent: Gather the total rebounds for the identified player during the 2008-2009 season.\n4. Data analyst: Calculate the percentage change in total rebounds for the identified player between the 2007-2008 and 2008-2009 seasons.', type='TextMessage'), ToolCallRequestEvent(source='WebSearchAgent', models_usage=RequestUsage(prompt_tokens=271, completion_tokens=26), content=[FunctionCall(id='call_xdYlGP2lsqDeWdSiOlwOBNiO', arguments='{"query":"Miami Heat highest points player 2006-2007 season"}', name='search_web_tool')], type='ToolCallRequestEvent'), ToolCallExecutionEvent(source='WebSearchAgent', models_usage=None, content=[FunctionExecutionResult(content='Here are the total points scored by Miami Heat players in the 2006-2007 season:\n        Udonis Haslem: 844 points\n        Dwayne Wade: 1397 points\n        James Posey: 550 points\n        ...\n        ', call_id='call_xdYlGP2lsqDeWdSiOlwOBNiO')], type='ToolCallExecutionEvent'), TextMessage(source='WebSearchAgent', models_usage=None, content='Tool calls:\nsearch_web_tool({"query":"Miami Heat highest points player 2006-2007 season"}) = Here are the total points scored by Miami Heat players in the 2006-2007 season:\n        Udonis Haslem: 844 points\n        Dwayne Wade: 1397 points\n        James Posey: 550 points\n        ...\n        ', type='TextMessage'), ToolCallRequestEvent(source='DataAnalystAgent', models_usage=RequestUsage(prompt_tokens=345, completion_tokens=68), content=[FunctionCall(id='call_asjxKtAVGfqrYl0jMpvwCrvV', arguments='{"query": "Dwyane Wade total rebounds 2007-2008 season"}', name='WebSearchAgent'), FunctionCall(id='call_8L91Kizt0KU6RNwUgvNx7S0s', arguments='{"query": "Dwyane Wade total rebounds 2008-2009 season"}', name='WebSearchAgent')], type='ToolCallRequestEvent'), ToolCallExecutionEvent(source='DataAnalystAgent', models_usage=None, content=[FunctionExecutionResult(content="Error: The tool 'WebSearchAgent' is not available.", call_id='call_asjxKtAVGfqrYl0jMpvwCrvV'), FunctionExecutionResult(content="Error: The tool 'WebSearchAgent' is not available.", call_id='call_8L91Kizt0KU6RNwUgvNx7S0s')], type='ToolCallExecutionEvent'), TextMessage(source='DataAnalystAgent', models_usage=None, content='Tool calls:\nWebSearchAgent({"query": "Dwyane Wade total rebounds 2007-2008 season"}) = Error: The tool \'WebSearchAgent\' is not available.\nWebSearchAgent({"query": "Dwyane Wade total rebounds 2008-2009 season"}) = Error: The tool \'WebSearchAgent\' is not available.', type='TextMessage'), ToolCallRequestEvent(source='WebSearchAgent', models_usage=RequestUsage(prompt_tokens=445, completion_tokens=70), content=[FunctionCall(id='call_imvRJ2jhpPdovBbx8MFjlFVS', arguments='{"query": "Dwyane Wade total rebounds 2007-2008 season"}', name='search_web_tool'), FunctionCall(id='call_U30KVmFG1aeXPbqGJjDmJ6iJ', arguments='{"query": "Dwyane Wade total rebounds 2008-2009 season"}', name='search_web_tool')], type='ToolCallRequestEvent'), ToolCallExecutionEvent(source='WebSearchAgent', models_usage=None, content=[FunctionExecutionResult(content='The number of total rebounds for Dwayne Wade in the Miami Heat season 2007-2008 is 214.', call_id='call_imvRJ2jhpPdovBbx8MFjlFVS'), FunctionExecutionResult(content='The number of total rebounds for Dwayne Wade in the Miami Heat season 2008-2009 is 398.', call_id='call_U30KVmFG1aeXPbqGJjDmJ6iJ')], type='ToolCallExecutionEvent'), TextMessage(source='WebSearchAgent', models_usage=None, content='Tool calls:\nsearch_web_tool({"query": "Dwyane Wade total rebounds 2007-2008 season"}) = The number of total rebounds for Dwayne Wade in the Miami Heat season 2007-2008 is 214.\nsearch_web_tool({"query": "Dwyane Wade total rebounds 2008-2009 season"}) = The number of total rebounds for Dwayne Wade in the Miami Heat season 2008-2009 is 398.', type='TextMessage'), ToolCallRequestEvent(source='DataAnalystAgent', models_usage=RequestUsage(prompt_tokens=562, completion_tokens=20), content=[FunctionCall(id='call_CtAnvcbitN0JiwBfiLVzb5Do', arguments='{"start":214,"end":398}', name='percentage_change_tool')], type='ToolCallRequestEvent'), ToolCallExecutionEvent(source='DataAnalystAgent', models_usage=None, content=[FunctionExecutionResult(content='85.98130841121495', call_id='call_CtAnvcbitN0JiwBfiLVzb5Do')], type='ToolCallExecutionEvent'), TextMessage(source='DataAnalystAgent', models_usage=None, content='Tool calls:\npercentage_change_tool({"start":214,"end":398}) = 85.98130841121495', type='TextMessage'), TextMessage(source='PlanningAgent', models_usage=RequestUsage(prompt_tokens=590, completion_tokens=122), content="Summary of Findings:\n\n1. Dwyane Wade was the Miami Heat player with the highest points in the 2006-2007 season, scoring a total of 1,397 points.\n2. Dwyane Wade's total rebounds during the 2007-2008 season were 214.\n3. Dwyane Wade's total rebounds during the 2008-2009 season were 398.\n4. The percentage change in Dwyane Wade's total rebounds between the 2007-2008 and 2008-2009 seasons was approximately 85.98%.\n\nTERMINATE", type='TextMessage')], stop_reason="Text 'TERMINATE' mentioned")
```

As we can see, after the Web Search Agent conducts the necessary searches and the Data Analyst Agent completes the necessary calculations, we find that Dwayne Wade was the Miami Heat player with the highest points in the 2006-2007 season, and the percentage change in his total rebounds between the 2007-2008 and 2008-2009 seasons is 85.98%!

### Custom Selector Function

Often times we want better control over the selection process. To this end, we can set the `selector_func` argument with a custom selector function to override the default model-based selection. For instance, we want the Planning Agent to speak immediately after any specialized agent to check the progress.

> [!note] Note
> Returning `None` from the custom selector function will use the default model-based selection.

```
def selector_func(messages: Sequence[AgentEvent | ChatMessage]) -> str | None:
    if messages[-1].source != planning_agent.name:
        return planning_agent.name
    return None

# Reset the previous team and run the chat again with the selector function.
await team.reset()
team = SelectorGroupChat(
    [planning_agent, web_search_agent, data_analyst_agent],
    model_client=OpenAIChatCompletionClient(model="gpt-4o-mini"),
    termination_condition=termination,
    selector_func=selector_func,
)

await Console(team.run_stream(task=task))
```

```
---------- user ----------
Who was the Miami Heat player with the highest points in the 2006-2007 season, and what was the percentage change in his total rebounds between the 2007-2008 and 2008-2009 seasons?
---------- PlanningAgent ----------
To address this query, we'll need to break it down into a few specific tasks:

1. Web search agent: Identify the Miami Heat player with the highest points in the 2006-2007 NBA season.
2. Web search agent: Find the total number of rebounds by this player in the 2007-2008 NBA season.
3. Web search agent: Find the total number of rebounds by this player in the 2008-2009 NBA season.
4. Data analyst: Calculate the percentage change in his total rebounds between the 2007-2008 and 2008-2009 seasons.

Let's get started with these tasks.
[Prompt tokens: 159, Completion tokens: 132]
---------- WebSearchAgent ----------
[FunctionCall(id='call_TSUHOBKhpHmTNoYeJzwSP5V4', arguments='{"query":"Miami Heat highest points player 2006-2007 season"}', name='search_web_tool')]
[Prompt tokens: 281, Completion tokens: 26]
---------- WebSearchAgent ----------
[FunctionExecutionResult(content='Here are the total points scored by Miami Heat players in the 2006-2007 season:\n        Udonis Haslem: 844 points\n        Dwayne Wade: 1397 points\n        James Posey: 550 points\n        ...\n        ', call_id='call_TSUHOBKhpHmTNoYeJzwSP5V4')]
---------- WebSearchAgent ----------
Tool calls:
search_web_tool({"query":"Miami Heat highest points player 2006-2007 season"}) = Here are the total points scored by Miami Heat players in the 2006-2007 season:
        Udonis Haslem: 844 points
        Dwayne Wade: 1397 points
        James Posey: 550 points
        ...

---------- PlanningAgent ----------
1. Web search agent: Find the total number of rebounds by Dwayne Wade in the 2007-2008 NBA season.
2. Web search agent: Find the total number of rebounds by Dwayne Wade in the 2008-2009 NBA season.
[Prompt tokens: 382, Completion tokens: 54]
---------- DataAnalystAgent ----------
[FunctionCall(id='call_BkPBFkpuTG6c3eeoACrrRX7V', arguments='{"query": "Dwyane Wade total rebounds 2007-2008 season"}', name='search_web_tool'), FunctionCall(id='call_5LQquT7ZUAAQRf7gvckeTVdQ', arguments='{"query": "Dwyane Wade total rebounds 2008-2009 season"}', name='search_web_tool')]
[Prompt tokens: 416, Completion tokens: 68]
---------- DataAnalystAgent ----------
[FunctionExecutionResult(content="Error: The tool 'search_web_tool' is not available.", call_id='call_BkPBFkpuTG6c3eeoACrrRX7V'), FunctionExecutionResult(content="Error: The tool 'search_web_tool' is not available.", call_id='call_5LQquT7ZUAAQRf7gvckeTVdQ')]
---------- DataAnalystAgent ----------
Tool calls:
search_web_tool({"query": "Dwyane Wade total rebounds 2007-2008 season"}) = Error: The tool 'search_web_tool' is not available.
search_web_tool({"query": "Dwyane Wade total rebounds 2008-2009 season"}) = Error: The tool 'search_web_tool' is not available.
---------- PlanningAgent ----------
It seems there was a miscommunication in task assignment. Let me reassess and reassign the tasks correctly.

1. Web search agent: Find the total number of rebounds by Dwayne Wade in the 2007-2008 NBA season.
2. Web search agent: Find the total number of rebounds by Dwayne Wade in the 2008-2009 NBA season.
[Prompt tokens: 525, Completion tokens: 76]
---------- WebSearchAgent ----------
[FunctionCall(id='call_buIWOtu1dJqPaxJmqMyuRkpj', arguments='{"query": "Dwyane Wade total rebounds 2007-2008 season"}', name='search_web_tool'), FunctionCall(id='call_qcnHKdoPsNAzMlPvoBvqmt8n', arguments='{"query": "Dwyane Wade total rebounds 2008-2009 season"}', name='search_web_tool')]
[Prompt tokens: 599, Completion tokens: 70]
---------- WebSearchAgent ----------
[FunctionExecutionResult(content='The number of total rebounds for Dwayne Wade in the Miami Heat season 2007-2008 is 214.', call_id='call_buIWOtu1dJqPaxJmqMyuRkpj'), FunctionExecutionResult(content='The number of total rebounds for Dwayne Wade in the Miami Heat season 2008-2009 is 398.', call_id='call_qcnHKdoPsNAzMlPvoBvqmt8n')]
---------- WebSearchAgent ----------
Tool calls:
search_web_tool({"query": "Dwyane Wade total rebounds 2007-2008 season"}) = The number of total rebounds for Dwayne Wade in the Miami Heat season 2007-2008 is 214.
search_web_tool({"query": "Dwyane Wade total rebounds 2008-2009 season"}) = The number of total rebounds for Dwayne Wade in the Miami Heat season 2008-2009 is 398.
---------- PlanningAgent ----------
With this information, we can proceed to calculate the percentage change in Dwyane Wade's total rebounds from the 2007-2008 season to the 2008-2009 season.

1. Data analyst: Calculate the percentage change in Dwyane Wade's total rebounds between the 2007-2008 (214 rebounds) and the 2008-2009 (398 rebounds) NBA seasons.
[Prompt tokens: 711, Completion tokens: 83]
---------- DataAnalystAgent ----------
[FunctionCall(id='call_RjbFpLCehz1Nlk5kYmyMUenB', arguments='{"start":214,"end":398}', name='percentage_change_tool')]
[Prompt tokens: 806, Completion tokens: 20]
---------- DataAnalystAgent ----------
[FunctionExecutionResult(content='85.98130841121495', call_id='call_RjbFpLCehz1Nlk5kYmyMUenB')]
---------- DataAnalystAgent ----------
Tool calls:
percentage_change_tool({"start":214,"end":398}) = 85.98130841121495
---------- PlanningAgent ----------
Based on the data collected, Dwyane Wade was the Miami Heat player with the highest points in the 2006-2007 NBA season, scoring a total of 1,397 points. Between the 2007-2008 and 2008-2009 seasons, Dwyane Wade's total rebounds increased from 214 to 398. This represents an approximate 85.98% increase in his total rebounds.

TERMINATE
[Prompt tokens: 834, Completion tokens: 90]
---------- Summary ----------
Number of messages: 18
Finish reason: Text 'TERMINATE' mentioned
Total prompt tokens: 4713
Total completion tokens: 619
Duration: 11.72 seconds
```

```
TaskResult(messages=[TextMessage(source='user', models_usage=None, content='Who was the Miami Heat player with the highest points in the 2006-2007 season, and what was the percentage change in his total rebounds between the 2007-2008 and 2008-2009 seasons?', type='TextMessage'), TextMessage(source='PlanningAgent', models_usage=RequestUsage(prompt_tokens=159, completion_tokens=132), content="To address this query, we'll need to break it down into a few specific tasks:\n\n1. Web search agent: Identify the Miami Heat player with the highest points in the 2006-2007 NBA season.\n2. Web search agent: Find the total number of rebounds by this player in the 2007-2008 NBA season.\n3. Web search agent: Find the total number of rebounds by this player in the 2008-2009 NBA season.\n4. Data analyst: Calculate the percentage change in his total rebounds between the 2007-2008 and 2008-2009 seasons.\n\nLet's get started with these tasks.", type='TextMessage'), ToolCallRequestEvent(source='WebSearchAgent', models_usage=RequestUsage(prompt_tokens=281, completion_tokens=26), content=[FunctionCall(id='call_TSUHOBKhpHmTNoYeJzwSP5V4', arguments='{"query":"Miami Heat highest points player 2006-2007 season"}', name='search_web_tool')], type='ToolCallRequestEvent'), ToolCallExecutionEvent(source='WebSearchAgent', models_usage=None, content=[FunctionExecutionResult(content='Here are the total points scored by Miami Heat players in the 2006-2007 season:\n        Udonis Haslem: 844 points\n        Dwayne Wade: 1397 points\n        James Posey: 550 points\n        ...\n        ', call_id='call_TSUHOBKhpHmTNoYeJzwSP5V4')], type='ToolCallExecutionEvent'), TextMessage(source='WebSearchAgent', models_usage=None, content='Tool calls:\nsearch_web_tool({"query":"Miami Heat highest points player 2006-2007 season"}) = Here are the total points scored by Miami Heat players in the 2006-2007 season:\n        Udonis Haslem: 844 points\n        Dwayne Wade: 1397 points\n        James Posey: 550 points\n        ...\n        ', type='TextMessage'), TextMessage(source='PlanningAgent', models_usage=RequestUsage(prompt_tokens=382, completion_tokens=54), content='1. Web search agent: Find the total number of rebounds by Dwayne Wade in the 2007-2008 NBA season.\n2. Web search agent: Find the total number of rebounds by Dwayne Wade in the 2008-2009 NBA season.', type='TextMessage'), ToolCallRequestEvent(source='DataAnalystAgent', models_usage=RequestUsage(prompt_tokens=416, completion_tokens=68), content=[FunctionCall(id='call_BkPBFkpuTG6c3eeoACrrRX7V', arguments='{"query": "Dwyane Wade total rebounds 2007-2008 season"}', name='search_web_tool'), FunctionCall(id='call_5LQquT7ZUAAQRf7gvckeTVdQ', arguments='{"query": "Dwyane Wade total rebounds 2008-2009 season"}', name='search_web_tool')], type='ToolCallRequestEvent'), ToolCallExecutionEvent(source='DataAnalystAgent', models_usage=None, content=[FunctionExecutionResult(content="Error: The tool 'search_web_tool' is not available.", call_id='call_BkPBFkpuTG6c3eeoACrrRX7V'), FunctionExecutionResult(content="Error: The tool 'search_web_tool' is not available.", call_id='call_5LQquT7ZUAAQRf7gvckeTVdQ')], type='ToolCallExecutionEvent'), TextMessage(source='DataAnalystAgent', models_usage=None, content='Tool calls:\nsearch_web_tool({"query": "Dwyane Wade total rebounds 2007-2008 season"}) = Error: The tool \'search_web_tool\' is not available.\nsearch_web_tool({"query": "Dwyane Wade total rebounds 2008-2009 season"}) = Error: The tool \'search_web_tool\' is not available.', type='TextMessage'), TextMessage(source='PlanningAgent', models_usage=RequestUsage(prompt_tokens=525, completion_tokens=76), content='It seems there was a miscommunication in task assignment. Let me reassess and reassign the tasks correctly.\n\n1. Web search agent: Find the total number of rebounds by Dwayne Wade in the 2007-2008 NBA season.\n2. Web search agent: Find the total number of rebounds by Dwayne Wade in the 2008-2009 NBA season.', type='TextMessage'), ToolCallRequestEvent(source='WebSearchAgent', models_usage=RequestUsage(prompt_tokens=599, completion_tokens=70), content=[FunctionCall(id='call_buIWOtu1dJqPaxJmqMyuRkpj', arguments='{"query": "Dwyane Wade total rebounds 2007-2008 season"}', name='search_web_tool'), FunctionCall(id='call_qcnHKdoPsNAzMlPvoBvqmt8n', arguments='{"query": "Dwyane Wade total rebounds 2008-2009 season"}', name='search_web_tool')], type='ToolCallRequestEvent'), ToolCallExecutionEvent(source='WebSearchAgent', models_usage=None, content=[FunctionExecutionResult(content='The number of total rebounds for Dwayne Wade in the Miami Heat season 2007-2008 is 214.', call_id='call_buIWOtu1dJqPaxJmqMyuRkpj'), FunctionExecutionResult(content='The number of total rebounds for Dwayne Wade in the Miami Heat season 2008-2009 is 398.', call_id='call_qcnHKdoPsNAzMlPvoBvqmt8n')], type='ToolCallExecutionEvent'), TextMessage(source='WebSearchAgent', models_usage=None, content='Tool calls:\nsearch_web_tool({"query": "Dwyane Wade total rebounds 2007-2008 season"}) = The number of total rebounds for Dwayne Wade in the Miami Heat season 2007-2008 is 214.\nsearch_web_tool({"query": "Dwyane Wade total rebounds 2008-2009 season"}) = The number of total rebounds for Dwayne Wade in the Miami Heat season 2008-2009 is 398.', type='TextMessage'), TextMessage(source='PlanningAgent', models_usage=RequestUsage(prompt_tokens=711, completion_tokens=83), content="With this information, we can proceed to calculate the percentage change in Dwyane Wade's total rebounds from the 2007-2008 season to the 2008-2009 season.\n\n1. Data analyst: Calculate the percentage change in Dwyane Wade's total rebounds between the 2007-2008 (214 rebounds) and the 2008-2009 (398 rebounds) NBA seasons.", type='TextMessage'), ToolCallRequestEvent(source='DataAnalystAgent', models_usage=RequestUsage(prompt_tokens=806, completion_tokens=20), content=[FunctionCall(id='call_RjbFpLCehz1Nlk5kYmyMUenB', arguments='{"start":214,"end":398}', name='percentage_change_tool')], type='ToolCallRequestEvent'), ToolCallExecutionEvent(source='DataAnalystAgent', models_usage=None, content=[FunctionExecutionResult(content='85.98130841121495', call_id='call_RjbFpLCehz1Nlk5kYmyMUenB')], type='ToolCallExecutionEvent'), TextMessage(source='DataAnalystAgent', models_usage=None, content='Tool calls:\npercentage_change_tool({"start":214,"end":398}) = 85.98130841121495', type='TextMessage'), TextMessage(source='PlanningAgent', models_usage=RequestUsage(prompt_tokens=834, completion_tokens=90), content="Based on the data collected, Dwyane Wade was the Miami Heat player with the highest points in the 2006-2007 NBA season, scoring a total of 1,397 points. Between the 2007-2008 and 2008-2009 seasons, Dwyane Wade's total rebounds increased from 214 to 398. This represents an approximate 85.98% increase in his total rebounds.\n\nTERMINATE", type='TextMessage')], stop_reason="Text 'TERMINATE' mentioned")
```

You can see from the conversation log that the Planning Agent always speaks immediately after the specialized agents.