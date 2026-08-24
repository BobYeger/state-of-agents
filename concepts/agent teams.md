# Agent Teams

An agent team is a multi-agent system organized like a working group: named members, explicit roles, shared goals, task ownership, communication channels, persistent context, verification, and a team-level control surface.

This is narrower than "multi-agent system." A MAS can be a debate, voting ensemble, graph, swarm, simulation, or pipeline. An agent team has organizational structure: someone or something owns coordination, teammates have responsibilities, and the team has a definition of done.

## Design Questions

- Who leads or coordinates the team?
- Who owns each subtask?
- Can teammates talk directly, or only report to a lead?
- Do teammates retain context across assignments?
- Is there a shared task list, event log, issue tracker, or worktree set?
- How are outputs verified and conflicts resolved?
- What does the human supervise: every action, the lead, or final artifacts?

## A Collaboration Substrate Is Not Team Organization

Buzz demonstrates a useful distinction. A shared signed channel can give humans and agents attributable common state without deciding who leads, who owns a task, which edits may overlap, or who can accept the result. Its ordinary multi-worker mode is a same-identity process pool serialized per channel; Orchestra adds distinct identities and persona prompts for coordinator/worker roles, scoped assignments, and cross-worker verification. The runtime itself enforces only liveness and orchestrator-authored completion ([[systems/Buzz]], [[sources/Buzz Repository]]).

Treat the event room as a team primitive, not the team design. Explicit organization still sits above the transport and storage layer.

The same distinction now applies to independent-session messaging. [[sources/Claude Code Cross-Session Messaging]] exposes identified peers, replies, wake behavior, and inbound trust controls without automatically creating a roster or shared task board. [[sources/OpenAI Codex Session Queueing]] durably turns queued text into a future user turn but does not carry equivalent sender identity in its v0.149 schema. [[sources/DeepSeek Harness Agent Teams]] adds a Lead, roster, durable mailbox, delivery acknowledgments, and task DAG, while [[sources/Grok Bot]] combines direct and group messaging with a shared persistent computer. These are different organizational layers, not interchangeable examples of “agents talking.” See [[concepts/cross-session agent communication]].

## The Human Gate Under Team Output

The last design question — what the human supervises — now has measured constraints on both sides.

Human review capacity is small and well-characterized. [[sources/Modern Code Review at Google]] is the pre-agents baseline: the median reviewer handles about 4 changes per week in roughly 3 hours, and that throughput depends on gate design — median diffs of 24 lines, a single owner-reviewer, and static analysis pre-filtering findings into the review UI. An agent team that multiplies change volume without reproducing those conditions is spending output against a ceiling the humans cannot raise.

What happens when volume exceeds the gate is no longer hypothetical. [[sources/How Humans Review AI-Generated Pull Requests]] finds that most agent-authored PRs in the AIDev dataset receive no review activity at all, and when they are reviewed, the reviewer is usually another agent — so "reviewed" in team metrics increasingly does not mean human oversight. [[sources/Bias in the Loop]] supplies the mechanism from a 2,784-participant experiment: when flagging an error costs more effort than approving, humans rubber-stamp, and prior attitude toward AI predicts error detection better than any demographic. A human gate is only as strong as the cost of saying no.

The constructive responses are tiered gates and mechanical throughput levers. [[sources/Intercom AI Approving Pull Requests]] is the strongest practitioner datapoint for tiering: a multi-agent review gate auto-approves 19.2% of PRs (6-16x faster at p75, 0.53% vs 5.39% revert rate against human-authored backend code), with a size gate that refuses large diffs and a full audit log — the human stays available on request rather than in every loop. [[sources/Cognition Multi-Agents Whats Actually Working]] reports agent reviewers catch ~2 bugs per PR, and perform best with clean context rather than the author's context — team-internal review is a real filter if the reviewer is independent. [[sources/GitHub Merge Queue Docs]] is the mechanical layer most agent PRs already flow through: batching, concurrency limits, and automatic requeue-on-failure are the knobs when merge volume becomes agent-scale. [[sources/DORA State of AI-assisted Software Development 2025]] frames the stakes across ~5,000 respondents: AI-assisted volume correlates with delivery throughput but with worse stability unless automated testing and fast feedback absorb the verification load.

The design consequence: size the human's role against measured capacity, not aspiration. Keep changes small enough that a human can actually review them, make rejection as cheap as approval, route routine verified changes through automated tiers with audit trails, and reserve human attention for scope, design, and the cases the automated gate refuses.

## Related

- [[concepts/multi-agent systems]]
- [[concepts/cross-session agent communication]]
- [[concepts/subagent context isolation]]
- [[concepts/human-in-the-loop agents]]
- [[operations/worktree isolation]]
- [[operations/agent observability]]
- [[methods/multi-agent orchestration]]
- [[methods/codex thread orchestration]]
- [[maps/Agent Teams and Workforces Map]]
- [[maps/MAS Orchestration and Architecture]]
- [[claims/Claim - Agent teams need explicit organization]]

## Related Sources

- [[sources/Claude Code Agent Teams]]
- [[sources/Claude Code Cross-Session Messaging]]
- [[sources/OpenAI Codex Session Queueing]]
- [[sources/DeepSeek Harness Agent Teams]]
- [[sources/Grok Bot]]
- [[sources/Anthropic Multi-Agent Coordination Patterns]]
- [[sources/MiniMax Agent Team]]
- [[sources/Agyn]]
- [[sources/Multi-Agent Teams Hold Experts Back]]
- [[sources/ChatDev]]
- [[sources/MetaGPT]]
- [[sources/Experiential Co-Learning]]
- [[sources/Developing Guidelines for Human-LLM Agent Teams]]
- [[sources/Modern Code Review at Google]]
- [[sources/How Humans Review AI-Generated Pull Requests]]
- [[sources/Bias in the Loop]]
- [[sources/Intercom AI Approving Pull Requests]]
- [[sources/Cognition Multi-Agents Whats Actually Working]]
- [[sources/GitHub Merge Queue Docs]]
- [[sources/DORA State of AI-assisted Software Development 2025]]
- [[sources/Buzz Repository]]
