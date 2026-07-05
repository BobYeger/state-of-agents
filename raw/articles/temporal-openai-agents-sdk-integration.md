Title: Production-ready agents with the OpenAI Agents SDK + Temporal

URL Source: https://temporal.io/blog/announcing-openai-agents-sdk-integration

Published Time: 2025-07-30

Markdown Content:
_Update: As of March 23rd, 2026, the integration between the OpenAI Agents SDK and Temporal's Python SDK is now [Generally Available](https://github.com/temporalio/sdk-python/releases)._

AI agents have become the dominant approach to building applications that leverage LLMs. They are AI-powered applications that don’t just respond to input, but actively pursue objectives using LLMs, memory, and tools. While I don’t believe there will ever be a single way to build these agents, some patterns are proving to be broadly applicable, and they are starting to show up as primitives in AI-centric programming frameworks, like the [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/).

I [worked](https://www.linkedin.com/posts/corneliadavis_i-got-a-sneak-peek-of-openais-new-typescript-activity-7335715652113965056-W0x3?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAAhTwsBq4aUmU3cyayfty14XAtw6XElih8) with the [TypeScript](https://openai.github.io/openai-agents-js/) version of OpenAI’s SDK a couple of months ago, but as of late have had a reason to dig deeper into the original [Python](https://openai.github.io/openai-agents-python/) one, and it’s pretty darn slick. I personally love anything where one of the stated goals is to keep the model as simple as possible, but only when it also stays the heck out of the way of the developer (nod to my friend and former boss Tom). These are the two stated goals of the OpenAI Agents SDK.

But the reason I come to you today is to share the news that things just got even better.

**OpenAI and Temporal have teamed up to add [_Durable Execution_](https://temporal.io/blog/what-is-durable-execution) to agents built using OpenAI’s Agents SDK, and today we released the new integration in Public Preview.**

This means that AI agents you build with the OpenAI Agents SDK will stand up to any manner of challenges thrown at them in production. Rate-limited LLMs? Your apps will hang on and automatically progress when there is once again sufficient capacity. Sporadic network connectivity? Your app will retry downstream requests until they get through. Your app crashes when it’s just about done with a long-running task? Restart it, and Temporal will see to it that it picks up where it left off, saving you compute and token costs! That crash was due to a bug you hadn’t caught yet? Yup, you can even fix that bug and continue execution of running apps.

[Video 3](https://www.youtube.com/watch?v=fwh21RV6bRo)

That’s what Durable Execution gives you — crash-proof execution. Once the app starts running, Temporal will keep it running even in the face of all of these types of problems.

But here’s the thing. You get all of this without an increase in code complexity. In fact, if you are new to Temporal, let me share with you one of the core Temporal values: With Temporal, you get to code the happy path, and Temporal does the error handling for you.

That’s right. **Both OpenAI and Temporal share the foundational tenet of making the developer productive, yet both also give the developer the agency to do any manner of complex things.** This is an integration that’s making this developer’s heart sing!

And let me draw your attention to the title of this post — it carries the word “production-ready.” While there are a fair number of frameworks out there that can help you build AI agent proof-of-concepts with relative ease, solutions that allow you to carry those experiments forward to production with comparable ease are few and far between.

In this post, I want to tell you about the new integration that does exactly that — allows you to get started quickly, and helps you achieve the durability you need for deploying this in the real world. I’ll cover how it works, what you can do with it, and the value it brings. I’ll start with a super quick intro to the most relevant parts of the Agents SDK and of Temporal — just enough to understand the magic that the integration brings. (Feel free to skip those parts if you are already aficionados thereof.) Then I’ll jump into the details of the magic. I’ll also share a set of steps you can follow to take your existing Agent SDK apps and add the Temporal integration.

## OpenAI Agents SDK: Easy-to-use agent primitives[#](https://temporal.io/blog/announcing-openai-agents-sdk-integration#openai-agents-sdk-easy-to-use-agent-primitives)

With the goal of simplicity, the OpenAI Agents SDK defines only four primitives:

*   Agents
*   Handoffs
*   Guardrails
*   Sessions

For today, we’ll focus on only the first two, but for a bit of context, guardrails are about putting some bumpers around user input (prompts), and sessions are about managing your application’s memory.

An agent is, if you will, the core compute abstraction for your agentic apps. It starts with an LLM (and yes, each agent you define can point to a different model) and attaches to it:

*   Instructions that focus the LLM on very specific goals (e.g., “you are a research assistant…”),
*   Tools that the LLM can decide to execute in pursuit of that goal,
*   A list of other agents that it may handoff control to,
*   And a bit of other configuration.

Here’s a definition of a triage agent that will take in user input and decide whether it should hand off to a weather reporting agent or a local businesses agent:

```
from agents import Agent
agent = Agent(name="Triage Agent", 
              model="gpt-4o-mini",
              instructions="You are to decide whether the user is asking about " +
                           "weather or information about local businesses. You " + 
                           "will handoff to the appropriate agent.",
              handoffs=[weather_agent, local_biz_agent],
)
```

A handoff is just what you think — it passes application control from one agent to another.

In order to understand how the Temporal/OpenAI Agents SDK integration works, it’s important for you to think of these agents as independent units, and your application will orchestrate a bunch of these units — agents — to get a job done. Handoffs are one way to orchestrate agents (we’ll come to the other momentarily).

To run an agent, you will use another entity supplied by the Agents SDK — a Runner. A Runner establishes a context and then runs the agent in that context. To run the above agent, for example, you would execute the following:

`result = Runner.run_sync(agent, "How late is Costco open?")`
Of course, you can write application logic that runs an agent, takes the output and uses that as input to the next agent, and so on. This is the second way that you can orchestrate the agents that make up your application. The triage agent could, for example, have been written as follows:

```
from agents import Agent
triage_agent = Agent(name="Triage Agent", 
              model="gpt-4o-mini",
              instructions="You are to decide ...",
)
weather_agent = Agent(...)
local_biz_agent = Agent(...)
query="How late is Costco open?"
result = Runner.run_sync(triage_agent, query)
if "weather" in result:
    Runner.run_sync(weather_agent, query, ...)
elif "business" in result:
    Runner.run_sync(local_biz_agent, query. ...)
else:
    <throw an exception>
```

The difference between handoffs and orchestrations written in native Python code is an interesting discussion for another time. For today, just know that whether an agent is invoked with a `Runner.run` or via agent-to-agent handoffs, each agent runs as its own independent unit of execution (I promise the relevance of this will become clear very shortly).

With the OpenAI Agents SDK model, you will find yourself building a set of smaller agents that do one thing and do one thing well (Any Unix fans out there? Yeah, this makes me really happy too!), and then stitching them together to form your agentic applications.

Okay, I think that’s enough Agents SDK context for us to carry on.

## Temporal: Guaranteed reliable execution of your agents[#](https://temporal.io/blog/announcing-openai-agents-sdk-integration#temporal-guaranteed-reliable-execution-of-your-agents)

Temporal has a similarly minimalistic (yet extremely powerful) set of core primitives:

*   Workflows
*   Activities
*   Updates
*   Queries

Again, we will focus on the first two today, but for context, Updates are a way to inject control and data into a running Workflow, and Queries are a way to get data out.

A Temporal Workflow holds the orchestration logic of your application, and it’s just native code. Today we’ll be looking at Python examples, but know that Temporal also supports TypeScript, Java, Golang, .Net, Ruby and PHP. Don’t let the name “Workflow” fool you — this isn’t the BPM (Business Process Management) of the 90s. It’s not some obscure representation of your business logic. It’s just code (with some fairy dust sprinkled on it 🧚). Really, just think of the Workflow as your application’s `main`.

What a Temporal Workflow primarily orchestrates are Temporal Activities. Where Workflows house the boring control flow things — loops, branching, parallelism, etc., Activities are where the most unpredictable parts of your application are implemented. A downstream call to an API (that might be unavailable due to a network hiccup). A call to an LLM (that might be rate-limited, or most certainly gives back a different response even when the same question is repeatedly asked). These are the things that Activities are expressly designed for (and yes, I am foreshadowing a bit here — check out [this video](https://www.youtube.com/watch?v=3Ox9Wqjn1Hk) for a good, quick overview.)

But Temporal Activities have some special properties. Whenever Activities are run, Temporal steps in and oversees progress. Temporal doesn’t get into the details of what is happening inside of an Activity, but it does keep track of when an Activity is invoked, what the arguments were, whether the Activity has completed, and if so, it also keeps track of the return values.

And the Workflow, which is orchestrating a bunch of Activity calls, keeps track of how all of those Activity calls have come together. If you follow up an LLM invocation with a tool execution and then a handoff to another agent, Temporal keeps track of all of that progress, and if something goes wrong, Temporal will compensate. Remember what I said earlier about Temporal picking up where it left off in the event of a crash? This is how you get that Durable Execution: Temporal keeps track of application progress and stores all Activity results, and that’s how it can simply keep going when latent troubles have been resolved.

The following shows how you might implement an agentic loop in Temporal. Implemented in the Workflow, it’s just a simple Python loop in which a couple of activities are called:

```
while True:
   # Call the first activity: invoke model
   result_one = await client.execute_activity(
       "invoke_model",
       agent_memory,
       task_queue="openai-agents-task-queue",
       schedule_to_close_timeout=10,
   )

   if result_one.next_step == "done"
       break

   # Call the second activity: invoke tool
   result_two = await client.execute_activity(
       "invoke_tool",
       result_one,
       task_queue="openai-agents-task-queue",
       schedule_to_close_timeout=10,
   )
```

In short, Temporal is a Durable Execution framework that makes distributed systems more resilient, even as the development thereof gets easier.

And AI agents are distributed systems.

## Let’s put them together: Durable, scalable agents[#](https://temporal.io/blog/announcing-openai-agents-sdk-integration#lets-put-them-together-durable-scalable-agents)

At this point, I bet you’re getting a sense of how these two technologies can come together to deliver more than the sum of their parts. The OpenAI Agents SDK provides a framework specially designed to enable developers to rapidly build AI agents. And Temporal provides a framework specially designed to enable developers to rapidly build production-ready distributed systems. Production-ready AI agents? That sounds good.

When using these two products together, you will:

*   Define your AI agents exactly as you normally would using the OpenAI agents SDK. You will designate an LLM, provide it instructions, supply it with a list of tools it may leverage, and designate a set of agents this one may hand off to.
*   Orchestrate your agents in Temporal Workflows. This is not much of a departure from what you were already doing, as Temporal Workflows are Python code, just as your agent orchestrations were before. Using the [Temporal Python SDK](https://github.com/temporalio/sdk-python), you will define a class and annotate it as a Temporal Workflow definition, and within that class you will define a method and designate it as the entrypoint for that Workflow.
*   In the Workflow, you will define your agents (as shown above) and run them with the appropriate call to the OpenAI Agents SDK Runner class (as shown above).
*   Handoffs designated as a part of an agent definition operate exactly as they did before.

So the programming model is largely the same as it would be if you were using the Agents SDK alone, but under the covers, we’ve done things to make the agents and your agentic application durable. Specifically, and here are the key insights:

→ every agent invocation is executed through a Temporal Activity,

→ **and because the orchestration is now running as a Workflow, Temporal automatically delivers all of the reliability we talked about above.**

The following is a very simple agent built using the OpenAI Agents SDK and Temporal integration:

```
from agents import Agent, Runner
from temporalio import workflow

@workflow.defn
class HelloWorldAgent:
   @workflow.run
   async def run(self, prompt: str) -> str:
       agent = Agent(
           name="Assistant",
           instructions="You only respond in haikus.",
       )

       result = await Runner.run(agent, input=prompt)
       return result.final_output
```

How this is all done is at once simple and clever. Around a month or two ago, OpenAI [made the Runner an abstract base class](https://github.com/openai/openai-agents-python/pull/720), which allowed Temporal to [provide an implementation](https://github.com/temporalio/sdk-python/blob/main/temporalio/contrib/openai_agents/_openai_runner.py) of that class that would create an Activity for each agent invocation. The integration goes one step further and also emits data that integrates the execution running in these activities into the Open AI tracing system.

The behavior I am describing is most easily seen by viewing the dashboards of both Temporal and OpenAI. Let’s run the very simple Haiku agent defined above:

```
$ uv run openai_agents/run_hello_world_workflow.py "Tell me about quantum computing"
Result: Bits dance in twilight,
Quantum whispers unfold dreams,
New worlds in a chip.
```

I’d like to draw your attention to the fact that the above code has **nary a mention of a Temporal Activity**. An agent is defined and run, with the `await Runner.run(agent, input=prompt)` call, yet in the following screenshot from the Temporal GUI, you can clearly see that an Activity was invoked.

![Image 1: event-history-agents](https://images.ctfassets.net/0uuz8ydxyd9p/6SaRrL8kQu1UXmBauxCEjA/8144fcc09904c98f132bd3f843f4d7a9/Screenshot_2025-07-28_at_4.15.09%C3%A2__PM.png)

Okay, so the first time I saw this → implicit Temporal Activities ← I thought, “Oh. Now, oh. That’s so cool.”

To show you the power of the integrated tracing, let me show you the dashboards for a more involved application. My colleague [Steve](https://www.linkedin.com/in/steveandroulakis/) has also been working with this integrated offering and built a [version of deep research](https://github.com/temporal-community/openai-agents-demos) — an extension of the [research bot example](https://github.com/openai/openai-agents-python/tree/main/examples/research_bot) that was inspired by the [deep research API cookbook](https://cookbook.openai.com/examples/deep_research_api/introduction_to_deep_research_api_agents). This agent takes in a user prompt, uses a triage agent to decide whether more input is needed from the user, if so, it leverages a clarification agent to guide that engagement, uses instruction, planning, and search agents to conduct research and a writing agent to produce a final report. ![Image 2: diagram-agent](https://images.ctfassets.net/0uuz8ydxyd9p/1btdmmSKgTLLI6z09tWzRj/82cd755b3045a80c706a694f42f88a17/Screenshot_2025-07-28_at_4.16.31%C3%A2__PM.png) In the Temporal GUI, this Workflow execution looks like this: ![Image 3: event-history-agent-2](https://images.ctfassets.net/0uuz8ydxyd9p/2wQ7RJ7hayh3m2NGHIJPGP/65d54e0978c69e312ba56b8101693f92/Screenshot_2025-07-28_at_4.18.18%C3%A2__PM.png) You can see that every agent execution was done with a separate Activity invocation, whether invoked via handoff — as done when the triage agent handed off to the instruction agent, or whether invoked from the Temporal Workflow — as done when the numerous (not predetermined) search agents were invoked in parallel. The corresponding trace is shown in the OpenAI dashboard: ![Image 4: oai-dashboard](https://images.ctfassets.net/0uuz8ydxyd9p/76Zau8aEAQEHJVLmRYJitT/49be32baf3de6c6ba75ac09220fd8b35/Screenshot_2025-07-28_at_4.19.15%C3%A2__PM.png) You saw a short version of this demo in the video at the top of this post. Steve also put together a [more comprehensive one](https://www.youtube.com/watch?v=fFBZqzT4DD8) — I assure you it’s worth a view. You’ll find this sample and a few others in [this repo](https://github.com/temporal-community/openai-agents-demos). Do also have a look at the [README here](https://github.com/temporalio/sdk-python/tree/main/temporalio/contrib/openai_agents) for some guidelines on how to configure your Workflows with the integration.

* * *

So here’s the tl;dr: you can build durable, reliable, production-ready AI agents using the OpenAI Agents SDK, along with Temporal. And all of that reliability comes without adding any extra complexity to your implementation. 🎤

## But wait, that’s not all! You also get horizontal scale[#](https://temporal.io/blog/announcing-openai-agents-sdk-integration#but-wait-thats-not-all-you-also-get-horizontal-scale)

I try my best not to bury the lede in these types of blogs, yet perhaps today I’ve done just that. In my defense, I do think that all of the above context is needed to get to the following point.

**In addition to delivering retries, state management and implicit checkpoint-like recovery in the case of an agent crash, this integration brings another very important production-ready feature: scalability!**

Without Temporal, your Agents SDK applications effectively run in a single process. If you want to scale the app, you are going to have to figure out how to manage a bunch of instances of your app and how to distribute work among them (plus many other challenges). And what happens when you need different capacity for different (micro)agents? For example, in the deep research example above, you might not need a lot more triage capacity, but you need a whole lot more search agent capacity. Hmm, this sounds eerily reminiscent of microservice scaling challenges, and it’s just as tricky.

**When you integrate Temporal with the Agents SDK, each (micro)agent is run in its own process or thread.** That’s right — as soon as you use this approach, your agents are loosely coupled from an operational perspective. Need more capacity? Just add more workload (Workflow and Activity/agent) capacity. That added capacity will be used for whatever work shows up. If your search agents are doing more work than your triage agents, Temporal simply uses the capacity for that work. The details of how this works are beyond what we can cover here, but if you're thinking this sounds like an event-driven system, you are absolutely right. I do hope I’ve convinced you that it’s worth a deeper look.

## Get started building production-ready agents[#](https://temporal.io/blog/announcing-openai-agents-sdk-integration#get-started-building-production-ready-agents)

You want to build some experimental agents and see potential before investing too much effort in prod-readiness. At the same time, you’d love to avoid throwing away proof-of-concept code when your ideas are ready for prime time.

With the integration we’ve announced here today, you get it all: the ability to get started quickly, all while being on the track for production deployment. You can either take your existing Agent SDK applications and make them production-ready using the steps we’ve outlined above, or you can build your orchestrations as Temporal Workflows from the get-go. The programming model is intuitive, and we offer a local dev instance to start prototyping with zero friction. To learn more and get started:

*   Watch the [demo video](https://www.youtube.com/watch?v=fFBZqzT4DD8).
*   Check out the Temporal Python SDK [GitHub repo](https://github.com/temporalio/sdk-python) and be sure to follow the configuration steps [found here](https://github.com/temporalio/sdk-python/tree/main/temporalio/contrib/openai_agents).
*   [Sign up for our webinar](https://pages.temporal.io/webinar-bringing-resilience-to-agents.html?utm_source=temporal&utm_medium=website&utm_campaign=launch-openai-agents-sdk&utm_content=webinar-openai-agents-sdk) on September 23rd to learn exactly how the integration works and how you can achieve production-readiness. 
    *   The first 100 registrants get a limited-edition t-shirt!
    *   Presented by my colleague Steve, Dominik Kundel from OpenAI, and yours truly.

As always, we’d love to hear from you. The integration is open-source and in Public Preview — we welcome feedback and contributions from the community. Or, let us know what you’re building and what we can do to help. Come join us in the [Temporal community](https://temporal.io/community), in **#topic-ai**!
