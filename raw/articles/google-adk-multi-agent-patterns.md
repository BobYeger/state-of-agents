Title: Developer’s guide to multi-agent patterns in ADK

URL Source: https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/

Published Time: 2025-12-16

Markdown Content:
DEC. 16, 2025

The world of software development has already learned this lesson: monolithic applications don't scale. Whether you're building a massive e-commerce platform or a complex AI application, relying on a single, all-in-one entity creates bottlenecks, increases debugging costs, and limits specialized performance.

The same principle applies to an AI agent. A single agent tasked with too many responsibilities becomes a "Jack of all trades, master of none." As the complexity of instructions increases, adherence to specific rules degrades, and error rates compound, leading to more and more "hallucinations." If your agent fails, you shouldn't have to tear down the entire prompt to find the bug.

Reliability comes from decentralization and specialization. Multi-Agent Systems (MAS) allow you to build the AI equivalent of a microservices architecture. By assigning specific roles (a Parser, a Critic, a Dispatcher) to individual agents, you build systems that are inherently more modular, testable, and reliable.

In this guide we’ll be using the Google Agent Development Kit (ADK) to illustrate 8 essential design patterns, from the Sequential Pipeline to the Human-in-the-loop design pattern, providing you with the concrete patterns and pseudocode you need to build production-grade agent teams.

### **1. Sequential Pipeline Pattern (aka the assembly line)**

Let’s start with the bread and butter of agent workflows. Think of this pattern as a classic assembly line where Agent A finishes a task and hands the baton directly to Agent B. It is linear, deterministic, and refreshingly easy to debug because you always know exactly where the data came from.

This is your go-to architecture for data processing pipelines. In the example below, we see a flow for processing raw documents: a Parser Agent turns a raw PDF into text, an Extractor Agent pulls out structured data, and a Summarizer Agent generates the final synopsis.


In ADK, the SequentialAgent primitive handles the orchestration for you. The secret sauce here is state management: simply use the output_key to write to the shared session.state so the next agent in the chain knows exactly where to pick up the work.

```
# ADK Pseudocode
# Step 1: Parse the PDF
parser = LlmAgent(
    name="ParserAgent",
    instruction="Parse raw PDF and extract text.",
    tools=[PDFParser],
    output_key="raw_text" 
)

# Step 2: Extract structured data
extractor = LlmAgent(
    name="ExtractorAgent",
    instruction="Extract structured data from {raw_text}.",
    tools=[RegexExtractor],
    output_key="structured_data"
)

# Step 3: Summarize
summarizer = LlmAgent(
    name="SummarizerAgent",
    instruction="Generate summary from {structured_data}.",
    tools=[SummaryEngine]
)

# Orchestrate the Assembly Line
pipeline = SequentialAgent(
    name="PDFProcessingPipeline",
    sub_agents=[parser, extractor, summarizer]
)
```

Python

Copied

### **2. Coordinator/Dispatcher Pattern (aka the concierge)**

Sometimes you don't need a chain; you need a decision maker. In this pattern, a central, intelligent agent acts as a dispatcher. It analyzes the user's intent and routes the request to a specialist agent best suited for the job.

This is ideal for complex customer service bots where you might need to send a user to a "Billing" specialist for invoice issues versus a "Tech Support" specialist for troubleshooting.


This relies on LLM-driven delegation. You simply define a parent CoordinatorAgent and provide a list of specialist sub_agents. The ADK's AutoFlow mechanism takes care of the rest, transferring execution based on the descriptions you provide for the children.

```
# ADK Pseudocode
billing_specialist = LlmAgent(
    name="BillingSpecialist", 
    description="Handles billing inquiries and invoices.",
    tools=[BillingSystemDB]
)

tech_support = LlmAgent(
    name="TechSupportSpecialist", 
    description="Troubleshoots technical issues.",
    tools=[DiagnosticTool]
)

# The Coordinator (Dispatcher)
coordinator = LlmAgent(
    name="CoordinatorAgent",
    # The instructions guide the routing logic
    instruction="Analyze user intent. Route billing issues to BillingSpecialist and bugs to TechSupportSpecialist.",
    sub_agents=[billing_specialist, tech_support]
)
```

Python

Copied

### **3. Parallel Fan-Out/Gather Pattern (aka the octopus)**

Speed matters. If you have tasks that don't depend on each other, why run them one by one? In this pattern, multiple agents execute tasks simultaneously to reduce latency or gain diverse perspectives. Their outputs are then aggregated by a final "synthesizer" agent .

This is ideal for something like Automated Code Review. Instead of running checks sequentially, you can spawn a "Security Auditor," a "Style Enforcer," and a "Performance Analyst" to review a Pull Request simultaneously. Once they finish, a "Synthesizer" agent combines their feedback into a single, cohesive review comment.


The ParallelAgent in ADK should be used to run sub-agents simultaneously. Be aware that although these agents operate in separate execution threads, they share the session state. To prevent race conditions, make sure each agent writes its data to a unique key.

```
# ADK Pseudocode

# Define parallel workers
security_scanner = LlmAgent(
    name="SecurityAuditor", 
    instruction="Check for vulnerabilities like injection attacks.",
    output_key="security_report"
)

style_checker = LlmAgent(
    name="StyleEnforcer", 
    instruction="Check for PEP8 compliance and formatting issues.",
    output_key="style_report"
)

complexity_analyzer = LlmAgent(
    name="PerformanceAnalyst", 
    instruction="Analyze time complexity and resource usage.",
    output_key="performance_report"
)

# Fan-out (The Swarm)
parallel_reviews = ParallelAgent(
    name="CodeReviewSwarm",
    sub_agents=[security_scanner, style_checker, complexity_analyzer]
)

# Gather/Synthesize
pr_summarizer = LlmAgent(
    name="PRSummarizer",
    instruction="Create a consolidated Pull Request review using {security_report}, {style_report}, and {performance_report}."
)

# Wrap in a sequence
workflow = SequentialAgent(sub_agents=[parallel_reviews, pr_summarizer])
```

Python

Copied

### **4. Hierarchical decomposition (aka the russian doll)**

Sometimes a task is too big for one agent context window. High-level agents can break down complex goals into sub-tasks and delegate them. Unlike the routing pattern, the parent agent might delegate just _part_ of a task and wait for the result to continue its own reasoning.

In this diagram, we see a ReportWriter that doesn't do the research itself. It delegates to a ResearchAssistant, which in turn manages WebSearch and Summarizer tools.


You can treat a sub-agent as a tool here. By wrapping an agent in AgentTool, the parent agent can call it explicitly, effectively treating the sub-agent's entire workflow as a single function call.

```
# ADK Pseudocode
# Level 3: Tool Agents
web_searcher = LlmAgent(name="WebSearchAgent", description="Searches web for facts.")
summarizer = LlmAgent(name="SummarizerAgent", description="Condenses text.")

# Level 2: Coordinator Agent
research_assistant = LlmAgent(
    name="ResearchAssistant",
    description="Finds and summarizes info.",
    # Coordinator manages the tool agents
    sub_agents=[web_searcher, summarizer] 
)

# Level 1: Top-Level Agent
report_writer = LlmAgent(
    name="ReportWriter",
    instruction="Write a comprehensive report on AI trends. Use the ResearchAssistant to gather info.",
    # Wrap the sub-agent hierarchy as a tool for the parent
    tools=[AgentTool(research_assistant)] 
)
```

Python

Copied

### **5. Generator and critic (aka the editor's desk)**

Generating high-quality, reliable output often requires a second pair of eyes. In this pattern, you separate the creation of content from the validation of content. One agent acts as the Generator, producing a draft, while a second agent acts as the Critic, reviewing it against specific, hard-coded criteria or logical checks.

This architecture is distinct because of its conditional looping. If the review passes, the loop breaks, and the content is finalized. If it fails, specific feedback is routed back to the Generator to produce a compliant draft. This is incredibly useful for code generation that needs syntax checking or content creation requiring compliance review.


To implement this in ADK, you separate concerns into two specific primitives: a SequentialAgent that manages the draft-and-review interaction, and a parent LoopAgent that enforces the quality gate and exit condition.

```
# ADK Pseudocode

# The Generator 
generator = LlmAgent(
    name="Generator",
    instruction="Generate a SQL query. If you receive {feedback}, fix the errors and generate again.",
    output_key="draft"
)

# The Critic 
critic = LlmAgent(
    name="Critic",
    instruction="Check if {draft} is valid SQL. If correct, output 'PASS'. If not, output error details.",
    output_key="feedback"
)

# The Loop 
loop = LoopAgent(
    name="ValidationLoop",
    sub_agents=[generator, critic],
    condition_key="feedback",
    exit_condition="PASS" 
)
```

Python

Copied

### **6. Iterative refinement (aka the sculptor)**

Great work rarely happens in a single draft. Just like a human writer needs to revise, polish, and edit, sometimes your agents need a few attempts to get an answer exactly right. In this pattern, agents enter a cycle of generating, critiquing, and refining until the output meets a specific quality threshold.

Unlike the Generator and Critic pattern, which focuses on correctness (Pass/Fail), this pattern focuses on qualitative improvement. A Generator creates a rough draft, a Critique Agent provides optimization notes, and a Refinement Agent polishes the output based on those notes


This pattern is implemented using the LoopAgent. A critical component here is the exit mechanism. While you can set a hard limit using max_iterations, ADK also allows agents to signal early completion. An agent can trigger an exit by signaling escalate=True within its EventActions if the quality threshold is met before the maximum iterations are reached.

```
# ADK Pseudocode

# Generator
generator = LlmAgent(
    name="Generator",
    instruction="Generate an initial rough draft.",
    output_key="current_draft"
)

# Critique Agent 
critic = LlmAgent(
    name="Critic",
    instruction="Review {current_draft}. List ways to optimize it for performance.",
    output_key="critique_notes"
)

# Refiner Agent 
refiner = LlmAgent(
    name="Refiner",
    instruction="Read {current_draft} and {critique_notes}. Rewrite the draft to be more efficient.",
    output_key="current_draft" # Overwrites the draft with better version
)

# The Loop (Critique -> Refine)
loop = LoopAgent(
    name="RefinementLoop",
    max_iterations=3, 
    sub_agents=[critic, refiner]
)

# Complete Workflow
workflow = SequentialAgent(sub_agents=[generator, loop])
```

Python

Copied

### **7. Human-in-the-loop (the human safety net)**

AI Agents are powerful, but sometimes you need a human in the driver's seat for critical decision-making. In this model, agents handle the groundwork, but a human must authorize high-stakes actions - specifically those that are irreversible or carry significant consequences. This includes executing financial transactions, deploying code to production, or taking action based on sensitive data (as opposed to merely processing it), ensuring safety and accountability.

The diagram shows a Transaction Agent processing routine work. When a high-stakes check is needed, it calls an ApprovalTool Agent, which pauses execution and waits for a Human Reviewer to say "Yes" or "No."


ADK allows you to implement this via custom tools. An agent can call an approval_tool which pauses execution or triggers an external system to request human intervention.

```
# ADK Pseudocode
transaction_agent = LlmAgent(
    name="TransactionAgent",
    instruction="Handle routine processing. If high stakes, call ApprovalTool.",
    tools=[ApprovalTool] 
)

approval_agent = LlmAgent(
    name="ApprovalToolAgent",
    instruction="Pause execution and request human input."
)

workflow = SequentialAgent(sub_agents=[transaction_agent, approval_agent])
```

Python

Copied

### **8. Composite patterns (the mix-and-match)**

Real-world enterprise applications rarely fit into a single box. You will likely combine these patterns to build production-grade applications.

For example, a robust Customer Support system might use a **Coordinator** to route requests. If the user has a technical issue, that branch might trigger a **Parallel** search of documentation and user history. The final answer might then go through a **Generator and Critic** loop to ensure tone consistency before being sent to the user.


### **A few pro-tips before you start:**

*   **State management is vital:** In ADK, session.state is your whiteboard. Use descriptive keys when using output_key so downstream agents know exactly what they are reading.
*   **Clear descriptions:** When using routing, the description field of your sub-agents is effectively your API documentation for the LLM. Be precise.
*   **Start simple:** Do not build a nested loop system on day one. Start with a sequential chain, debug it, and then add complexity.

## Get Started Now

Ready to build your team of agents? Check out the[ADK Documentation](https://google.github.io/adk-docs/) to get started. We can’t wait to see what you build.

[](https://developers.googleblog.com/dont-trust-verify-building-end-to-end-confidential-applications-on-google-cloud/)
Previous

Next

[](https://developers.googleblog.com/mediatek-npu-and-litert-powering-the-next-generation-of-on-device-ai/)
