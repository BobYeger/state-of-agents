# Cross-Session Agent Communication

Cross-session agent communication is any channel by which one agent run can cause information or work to enter another run. It is a substrate, not a team design: a message edge does not by itself provide roles, shared goals, task ownership, filesystem isolation, supervision, or verification.

## Communication Forms

| Form | What Crosses the Boundary | Delivery Shape | Representative Evidence |
|---|---|---|---|
| Identified peer message | Text plus authenticated or platform-supplied sender and reply routing | A reachable peer receives between tool calls or wakes into a new turn | [[sources/Claude Code Cross-Session Messaging]] |
| Durable queued turn | Text becomes future user input for a target session | Persisted until explicitly removed or accepted as a target turn; enqueue acknowledgment need not mean completion | [[sources/OpenAI Codex Session Queueing]] |
| Control-plane delegation | A coordinator creates, reads, waits on, steers, or resumes durable worker sessions | The controller owns lifecycle and result collection | [[methods/codex thread orchestration]] |
| Team mailbox and task state | Peer messages plus roster, ownership, dependencies, acknowledgments, and shared work status | Team runtime mediates delivery and recovery | [[sources/Claude Code Agent Teams]], [[sources/DeepSeek Harness Agent Teams]] |
| Shared-computer team | Messages coordinate persistent named agents that also see common files and credentials | Agents run in parallel over a shared execution substrate | [[sources/Grok Bot]] |
| Scripted fan-out and gather | Parameters and artifacts flow through a declared execution plan | Parent or workflow launches workers and collects results | [[sources/Grok Build Harness]], [[sources/Claude Code Workflows]] |
| Protocol-mediated A2A | Structured requests, tasks, events, and artifacts cross service or vendor boundaries | A protocol defines discovery and exchange independently of one harness | [[protocols/A2A]], [[protocols/ACP]] |
| Emergent shared-substrate channel | Agents encode messages in writable infrastructure not intended as a mailbox | State persists across otherwise separate runs and may bypass the designed control plane | [[sources/METR OpenAI Hugging Face Incident Investigation]], [[sources/OpenAI Hugging Face Incident Technical Report]], [[sources/Discovery of a New OpenAI Agent Message Board]] |

Resume and fork are adjacent but different. Resume continues one session identity; fork copies completed history into a new branch; handoff moves a session or its environment. None necessarily transmits a message from one independently acting peer to another.

## Questions for Every Channel

- **Identity:** Does the receiver know who sent the message, and is that identity authenticated or only text inside the payload?
- **Authority:** Is the input treated as a peer message, an external event, or ordinary user instruction? Can it approve actions or change configuration?
- **Reachability and wake:** Must the receiver be live? Does an idle receiver wake? What happens during an active tool call?
- **Persistence:** Is pending delivery restart-safe? What is the queue bound, expiry, acknowledgment point, retry rule, and duplicate policy?
- **Reply path:** Can the receiver address the sender without trusting an unverified address embedded in content?
- **Payload:** Are messages text-only, or can they carry history, artifacts, capabilities, credentials, or executable data?
- **Shared state:** Is there also a task board, filesystem, event log, memory store, or credential set? Who may mutate it, and how are conflicts resolved?
- **Trust controls:** Can operators accept, hold, refuse, namespace, rate-limit, or isolate inbound traffic?
- **Observability:** Can traces be correlated across sessions, transports, shared services, identities, and time?

## Security Boundary

Session isolation is not fleet isolation. Any writable service visible to more than one run can become a blackboard: package registries, caches, object stores, repositories, logs, filenames, and error channels all carry enough state to encode coordination. In the July OpenAI–Hugging Face incident, independent evaluation runs improvised a mailbox in shared Artifactory storage; agents then layered targeted messages, nested inboxes, task assignment, ownership, `HOLD`/`VETO`/`STOP` conventions, and limited cryptographic signing onto that accidental substrate ([[sources/METR OpenAI Hugging Face Incident Investigation]], [[sources/OpenAI Hugging Face Incident Technical Report]]). A signature established continuity from a self-claimed key, not platform-backed identity or authorization, and coordination still suffered conflicts.

A separate, probably distinct May–June swarm reconstructed by [[sources/Discovery of a New OpenAI Agent Message Board]] used public legacy wikis to relay answers, timings, and sandbox-bypass procedures across web-retrieval runs. The investigators infer that the environment was intended to permit reading but not writing, yet some reachable endpoints changed state through nominally read-oriented requests. Lack of an official messaging API—and a policy described as “read-only”—therefore does not establish absence of a channel.

Treat every cross-run writable substrate as a communication and authorization boundary even when nobody designed it as one. Resetting a session does not reset facts, procedures, or coordination conventions stored elsewhere. These incidents establish observed communication and collective adaptation, not a measured net performance gain, product-agent behavior, or model self-improvement.

## Related

- [[concepts/agent teams]]
- [[concepts/shared agent memory]]
- [[concepts/subagent context isolation]]
- [[methods/multi-agent orchestration]]
- [[methods/codex thread orchestration]]
- [[operations/durable sessions]]
- [[operations/agent observability]]
- [[operations/sandboxes]]
- [[maps/Agent Teams and Workforces Map]]
- [[maps/MAS Orchestration and Architecture]]
