## Build Cross-Language Multi-Agent Team with Google’s Agent Development Kit and A2A

[Shubham Saboo](https://developers.googleblog.com/search/?author=Shubham+Saboo) Senior AI Product Manager

[Eric Dong](https://developers.googleblog.com/search/?author=Eric+Dong) Developer Relations Engineer

![banner](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/banner.original.jpg)

## How a Python agent and a Go agent collaborate on contract compliance using the Agent2Agent protocol

Your contract compliance pipeline has a problem. The data science team wrote a brilliant extraction agent in Python. It uses Gemini to parse legal contracts and pull out every key term. The security engineering team built a blazing-fast compliance validator in Go, using all deterministic logic and no LLM. Both work perfectly in isolation. But now you need them to work together, as a single coordinated pipeline, and neither team is willing to rewrite their service in another language.

This is the reality of production AI systems: different teams, different languages, different deployment targets. The question isn't whether you'll face this; it's how you'll solve it.

In this post, we'll build a **Contract Compliance Multi-Agent Pipeline** where a Python agent extracts contract terms using Gemini and a Go agent validates them against corporate policy. The two services are connected by the **Agent2Agent (A2A)** protocol and orchestrated by **Google's** [**Agent Development Kit (ADK)**](https://adk.dev/).

Along the way, you'll learn three architectural patterns that separate production multi-agent systems from single-language demos:

- **Cross-language agent collaboration** using the A2A protocol so teams can build agents in the best language for the job without rewriting code.
- **ADK's RemoteA2aAgent abstraction** that turns any remote A2A-compliant service into a local sub-agent with a few lines of code
- **Multi-agent pipeline orchestration** where specialized agents with narrow responsibilities replace monolithic prompts that try to do everything

The complete source code is available on [GitHub](https://github.com/GoogleCloudPlatform/generative-ai/tree/main/agents/adk/contract-compliance-pipeline).

![diagram_1 (2)](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/diagram_1_2.original.png)

## When one agent isn't enough

Most AI projects start the same way: one big agent, one massive prompt, every tool crammed into a single context window. It works for demos. It falls apart in production for three key reasons:

- **Context degradation:** As tools multiply beyond 10-15, the model starts missing instructions, calling wrong tools, or hallucinating parameters. Each additional tool dilutes the model's attention across a wider surface area. A contract extraction agent that also handles translation, summarization, and email drafting will eventually get confused about which tool to call when.
- **Blast radius**: One unhandled exception in a minor feature crashes the entire agent turn. A rate limit on a translation API shouldn't bring down your entire workflow. But in a monolithic agent, every failure is a total failure.
- **Untestable**: You can't cleanly unit test a system with 50 entangled responsibilities. When every prompt change potentially affects every downstream behavior, evaluating regressions becomes guesswork.

The fix is the same pattern that transformed backend engineering a decade ago: decompose the monolith into specialized microservices. Each agent gets one job, a focused prompt, and a minimal toolset.

![table](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/table.original.jpg)

## The A2A protocol: how agents discover and talk to each other

The Agent-to-Agent (A2A) protocol is an open standard that enables agents built in any language or framework to interoperate. Think of it as the HTTP of the agent world: a shared contract that lets any two agents communicate regardless of how they're built internally.

A2A solves three fundamental problems:

- **Discovery:** Agents advertise their capabilities through Agent Cards, JSON metadata served at /.well-known/agent.json. Similar to OpenAPI specs for REST APIs, the card declares the agent's name, URL, version, skills, and supported input/output formats. A calling agent fetches the card first to understand what the remote agent can do.
- **Communication:** All data exchange happens over JSON-RPC 2.0, routed through a single endpoint. The core method for agent communication is message/send (used by our implementation to submit contract data and receive results synchronously), alongside other protocol methods like tasks/send and tasks/get for task submission and retrieval. Data travels inside typed Message Parts: TextParts for natural language and DataParts for structured JSON.
- **Task lifecycle:** Every interaction is wrapped in a Task that transitions through well-defined states: submitted, working, completed, or failed. This state machine means agents can handle both synchronous workflows (check this contract now) and asynchronous ones (verify this document over 48 hours) with the same protocol.

The beauty of this approach is that neither agent needs to know anything about the other's implementation. The Python agent doesn't import Go packages. The Go agent doesn't run Python code. They just speak a shared protocol over HTTP.

![image (6)](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/image_6.original.png)

### What an Agent Card Actually looks like

Here is the Agent Card the Go compliance service exposes at ‘/.well-known/agent.json’:

```
// go-compliance-agent/internal/agentcard/card.go
func GetCard() AgentCard {
    agentURL := os.Getenv("AGENT_URL")
    if agentURL == "" {
        agentURL = "http://localhost:8888"
    }

    return AgentCard{
        Name:        "Security Compliance Validator",
        Description: "Go-based validation engine that checks vendor contracts against corporate compliance policy rules.",
        Version:     "1.0.0",
        SupportedInterfaces: []AgentInterface{
            {
                URL:             agentURL,
                ProtocolBinding: "JSONRPC",
                ProtocolVersion: "1.0",
            },
        },
        Capabilities: Capabilities{
            ExtendedAgentCard: false,
        },
        DefaultInputModes:  []string{"application/json"},
        DefaultOutputModes: []string{"application/json"},
        Skills: []Skill{
            {
                ID:          "contract_compliance_check",
                Name:        "Contract Compliance Check",
                Description: "Validates extracted contract fields against corporate policy rules.",
                Tags:        []string{"compliance", "contract", "validation"},
                Examples: []string{
                    "Check this contract for compliance violations",
                    "Validate vendor agreement terms against policy",
                },
            },
        },
    }
}
```

The URL is read from an environment variable so the same code works locally (‘localhost:8888’) and in containers (‘go-compliance-agent:8888’). The Skills array means a single agent can advertise multiple capabilities.

## Code Implementation Walkthrough

Here is how easily this cross-language team is assembled using the ADK in Python and a standard HTTP server in Go.

### Shared state: the data bus between agents

Before diving into individual agents, it's important to understand how they communicate. ADK's ToolContext.state provides a shared dictionary that all sub-agents in a pipeline read and write to. Rather than passing data between agents through function arguments or return values, agents communicate through a shared session state.

Each step in our compliance pipeline maps to a specific checkpoint:

```python
class ComplianceStep(str, Enum):
    INGESTED = "INGESTED"                     # Contract uploaded, awaiting extraction
    EXTRACTED = "EXTRACTED"                    # Fields parsed by Gemini
    COMPLIANCE_PENDING = "COMPLIANCE_PENDING"  # Sent to Go agent, awaiting result
    COMPLIANCE_COMPLETE = "COMPLIANCE_COMPLETE"# Go agent returned verdict
    MANUAL_REVIEW = "MANUAL_REVIEW"           # Timeout or error, routed to human
    REVIEW_READY = "REVIEW_READY"             # Report generated, violations found
    APPROVED = "APPROVED"                      # All checks passed
```

The MANUAL\_REVIEW state is worth highlighting. If the Go compliance agent is unreachable for reasons like server crash, network timeout, container not started - the pipeline doesn't just fail. It transitions to MANUAL\_REVIEW, routing the case to a human legal reviewer. This fail-safe pattern is essential for production systems where downstream services may be intermittently unavailable.

### 1\. Full Multi-Agent Pipeline: Wrapping the Go Agent in Python

Using the ADK, you can define a **remote A2A-compliant** agent locally using \`RemoteA2aAgent\`. The SDK automatically handles the Agent Card handshake, parameter serialization, and JSON-RPC network requests behind the scenes.

```python
# python-extraction-agent/app/agent.py
from google.adk.agents import Agent, SequentialAgent
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent
from google.adk.models import Gemini

# Sub-Agent 1: Ingests & extracts details using LLM reasoning
extractor_agent = Agent(
   name="extractor_agent",
   model=Gemini(model="gemini-3.5-flash"),
   instruction="You are a Legal Data Extraction Agent. Extract contract fields: value, contractor, dates, insurance...",
   tools=[read_contract_text, save_extracted_fields, classify_risk_level]
)

# Sub-Agent 2: Go A2A Compliance Service wrapped as a local agent
compliance_agent = RemoteA2aAgent(
   name="compliance_agent",
   agent_card=GO_AGENT_CARD_URL,
   description="Validates extracted contract fields against corporate policies."
)

# Sub-Agent 3: Generates the final audit summary report
report_agent = Agent(
   name="report_agent",
   model=Gemini(model="gemini-3.5-flash"),
   instruction="Generate the final compliance report and Markdown summary.",
   tools=[generate_summary_report]
)

# Coordinator: Chains them together sequentially
root_agent = SequentialAgent(
   name="contract_compliance_coordinator",
    description="Orchestrates contract parsing, A2A compliance validation, and final reporting in sequence.",
   sub_agents=[extractor_agent, compliance_agent, report_agent],
)
```

### 2\. The Go Compliance Endpoint

On the Go side, the compliance agent is a standard HTTP server that implements the A2A protocol. It exposes an Agent Card for discovery and a single JSON-RPC endpoint that accepts message/send requests, runs deterministic policy checks against the extracted contract fields, and returns a pass/fail verdict. No AI frameworks or SDKs needed — just the Go standard library.

Here's the simplified flow (the [full implementation](https://github.com/GoogleCloudPlatform/generative-ai/tree/main/agents/adk/contract-compliance-pipeline/go-compliance-agent) is in the repository):

```
// Simplified pseudo-code — see GitHub repository for full implementation

func HandleJSONRPC(w http.ResponseWriter, r *http.Request) {
    var req JSONRPCRequest
    json.NewDecoder(r.Body).Decode(&req)

    // Extract contract details from the A2A message
    var details compliance.ContractDetails
    extractContractFromMessage(req.Params, &details)

    // Run deterministic policy checks
    result := compliance.CheckCompliance(details, policy)

    // Return verdict as a JSON-RPC response
    writeJSONRPCResult(w, req.ID, result)
}
```

## Open source App: Contract Compliance Engine

The complete pipeline ships as an open source application you can deploy and extend. The [repository](https://github.com/GoogleCloudPlatform/generative-ai/tree/main/agents/adk/contract-compliance-pipeline) includes a full-featured operations cockpit served by the FastAPI service.

- **Three-panel operations cockpit:** The left panel lets operators select or upload contracts. The center panel shows live results: compliance certificates for passing contracts and violation reports for failures. The right panel is a developer console with policy controls, network simulation, and a real-time view of the data flowing between the two agents.
- **Network fault simulation:** A toggle lets you switch the Go agent between Normal, Delayed, and Crashed states. Setting it to Crashed shows the fail-safe in action: the Python agent detects the outage, halts the pipeline, and routes the contract for manual human review instead of silently failing.
- **Live agent handoff inspector:** The right panel displays the exact request sent from Python to Go and the response coming back, so you can see the structured contract data crossing the language boundary in real time.

![application_interface](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/application_interface.original.png)

## Benefits of the ADK and A2A Approach

1. **Freedom of Technology**: Your data science team can write complex cognitive agents in Python, and your systems team can write high-performance, secure compliance validators in Go, Rust, or C++.
2. **Simplified Integration**: The Python orchestrator communicates with the Go agent as if it were a local class. You do not have to write custom HTTP clients or handle manual JSON-RPC payload wrapping.
3. **Resilience**: Because the agents are decoupled, you can configure granular timeouts and retry logic. If the Go validator is down, the Python agent saves the current state checkpoint and waits for manual approval.
4. **Isolated Auditing**: The Go compliance validator is completely deterministic. For audit purposes, you can pass the same inputs and verify they produce identical policy verdicts, bypassing LLM non-determinism.

## Conclusion

Multi-agent orchestration isn't just about chaining prompts; it's about building robust, cross-language distributed systems.

By bridging Python's AI ecosystem and Go's runtime reliability using Google ADK and the open A2A protocol, you get the best of both worlds: cognitive reasoning where there is ambiguity, and deterministic enforcement where there is policy.

Ready to run this yourself?

- Clone the [contract-compliance-engine](https://github.com/GoogleCloudPlatform/generative-ai/tree/main/agents/adk/contract-compliance-pipeline) and run the live demo locally
- Explore the [ADK documentation](https://adk.dev/) for session management, multi-agent patterns, and evaluation frameworks
- Explore the [Agent2Agent Protocol](https://a2a-protocol.org/latest/) documentation for more details.